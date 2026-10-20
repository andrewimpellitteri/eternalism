"""Regression tests for scripts/grid.py gates: enumeration, validation, provenance
and stage transitions. Every test runs in a temporary root; nothing touches the
live board, results, claims, network or models."""
import contextlib
import copy
import importlib.util
import io
import itertools
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

PROJECT = Path(__file__).resolve().parents[1]
FIXTURES = PROJECT / "tests/fixtures/grid"
spec = importlib.util.spec_from_file_location("grid", PROJECT / "scripts/grid.py")
grid = importlib.util.module_from_spec(spec)
spec.loader.exec_module(grid)

CLAIM = "In the fixture model, statement S holds under hypotheses H1 and H2."


def valid_record(cell, verdict="advance", claim=CLAIM):
    record = {"cell": cell, "verdict": verdict, "kill_reason": None, "claim": claim, "move": "M1",
              "smallest_instance": "Two-element model checked by hand.",
              "predecessors": [{"ref": f"src-{n}", "read_depth": "full-text",
                                "shows": "a related result", "differs": "different hypotheses"}
                               for n in range(3)],
              "defeat_queries": [f"query {n} -> no statement of S" for n in range(5)],
              "bridge_premises": [], "falsifier": "A model satisfying H1, H2 without S.",
              "notes": ""}
    if verdict == "kill":
        record["kill_reason"] = "known"
    return record


class GridCase(unittest.TestCase):
    """Temporary root with fixture axes, an empty board and no results."""

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "grid").mkdir()
        shutil.copyfile(FIXTURES / "axes.json", self.root / "grid/axes.json")
        self.board = self.root / "WORKBOARD.jsonl"
        self.board.write_text("")
        self.patches = [patch.object(grid, "ROOT", self.root),
                        patch.object(grid, "AXES", self.root / "grid/axes.json"),
                        patch.object(grid, "BOARD", self.board)]
        for item in self.patches:
            item.start()
        self.ax = grid.load_axes()

    def tearDown(self):
        for item in self.patches:
            item.stop()
        self.temp.cleanup()

    def assign(self, tid, *cell_ids):
        task = {"id": tid, "title": tid, "priority": 7, "blocked_by": [],
                "owns": [f"grid/results/{tid}/"], "done_when": ["x"],
                "brief": f"Intro.\n\nCells: {', '.join(cell_ids)}\n\n- listing"}
        with self.board.open("a") as handle:
            handle.write(json.dumps(task) + "\n")

    def write_results(self, tid, *records, raw=()):
        folder = self.root / "grid/results" / tid
        folder.mkdir(parents=True, exist_ok=True)
        lines = [json.dumps(r) for r in records] + list(raw)
        with (folder / "cells.jsonl").open("a") as handle:
            handle.write("".join(line + "\n" for line in lines))

    def adv_ids(self):
        return [cell for cell, _ in grid.cells(self.ax, "adv")]

    def s2_ids(self):
        return [cell for cell, _ in grid.cells(self.ax, "s2")]

    def problems(self):
        return grid.results(False)[1]

    def run_main(self, *argv):
        out, err = io.StringIO(), io.StringIO()
        with patch.object(sys, "argv", ["grid.py", *argv]), \
                contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            try:
                code = grid.main()
            except SystemExit as exc:
                code = exc.code if isinstance(exc.code, int) else 2
        return code, out.getvalue(), err.getvalue()

    def promote_parent(self, cell="S1-P01-B01", claim=CLAIM):
        """A valid, assigned stage-1 advance and its assigned adversary cell."""
        self.assign("grid-s1-01", cell)
        self.write_results("grid-s1-01", valid_record(cell, claim=claim))
        self.assign("grid-adv-01", f"A-{cell}")


class EnumerationTests(GridCase):
    def test_s1_and_t1_enumeration_is_legal_and_unique(self):
        s1 = [cell for cell, _ in grid.cells(self.ax, "s1")]
        t1 = [cell for cell, _ in grid.cells(self.ax, "t1")]
        self.assertEqual(len(s1), 3 * 2)
        self.assertEqual(len(set(s1)), len(s1))
        self.assertEqual(len(t1), 3)  # Unordered pairs, no self-pairs.
        self.assertEqual(set(t1), {"T1-P01-P02", "T1-P01-P03", "T1-P02-P03"})

    def test_live_axes_ids_unique_and_counts_follow_axes(self):
        live = json.loads((PROJECT / "grid/axes.json").read_text())
        for key in ("physics", "bridges", "ontologies", "moves"):
            ids = [item["id"] for item in live[key]]
            self.assertEqual(len(ids), len(set(ids)), key)
        with patch.object(grid, "AXES", PROJECT / "grid/axes.json"):
            ax = grid.load_axes()
        n, b = len(live["physics"]), len(live["bridges"])
        self.assertEqual(len(grid.cells(ax, "s1")), n * b)
        self.assertEqual(len(grid.cells(ax, "t1")), n * (n - 1) // 2)

    def test_tasks_assign_each_cell_once_and_never_reassign(self):
        code, _, _ = self.run_main("tasks", "s1", "--batch", "4", "--append")
        self.assertEqual(code, 0)
        named = list(itertools.chain.from_iterable(
            grid.CELLS_RE.search(json.loads(line)["brief"]).group(1).split(", ")
            for line in self.board.read_text().splitlines()))
        self.assertEqual(sorted(named), sorted(c for c, _ in grid.cells(self.ax, "s1")))
        before = self.board.read_bytes()
        code, _, _ = self.run_main("tasks", "s1", "--batch", "4", "--append")
        self.assertNotEqual(code, 0)
        self.assertEqual(self.board.read_bytes(), before)

    def test_dry_run_does_not_write(self):
        code, out, _ = self.run_main("tasks", "s1", "--batch", "2")
        self.assertEqual(code, 0)
        self.assertEqual(len(out.splitlines()), 3)
        self.assertEqual(self.board.read_text(), "")
        self.assertFalse((self.root / "grid/results").exists())

    def test_invalid_batch_size_rejected_without_writing(self):
        for batch in ("0", "-1"):
            code, _, _ = self.run_main("tasks", "s1", "--batch", batch, "--append")
            self.assertNotEqual(code, 0, batch)
            self.assertEqual(self.board.read_text(), "")

    def test_duplicate_assignment_reported(self):
        self.assign("grid-s1-01", "S1-P01-B01")
        self.assign("grid-s1-02", "S1-P01-B01")
        code, out, _ = self.run_main("status")
        self.assertNotEqual(code, 0)
        self.assertIn("S1-P01-B01", out)

    def test_non_grid_task_with_grid_prefix_is_not_an_assignment(self):
        task = {"id": "grid-regression-tests", "title": "t", "priority": 1, "blocked_by": [],
                "owns": ["tests/"], "done_when": ["x"], "brief": "Notes.\nCells: S1-P01-B01\n"}
        self.board.write_text(json.dumps(task) + "\n")
        self.assertNotIn("S1-P01-B01", grid.assigned())


class ValidationTests(GridCase):
    def test_complete_valid_records_pass(self):
        self.assertEqual(grid.contract_problems(valid_record("S1-P01-B01")), [])
        self.assertEqual(grid.contract_problems(valid_record("S1-P01-B01", "kill")), [])
        hold = valid_record("T1-P01-P02", "hold")
        hold["predecessors"], hold["defeat_queries"] = [], []
        self.assertEqual(grid.contract_problems(hold), [])

    def test_minimal_malformed_advance_rejected(self):
        # DESIGN_REVIEW.md: empty predecessor objects and empty queries passed the gate.
        record = {"cell": "S1-P01-B01", "verdict": "advance", "claim": "C",
                  "predecessors": [{}, {}, {}], "defeat_queries": ["", "", "", "", ""],
                  "smallest_instance": "x", "bridge_premises": []}
        self.assertTrue(grid.contract_problems(record))

    def test_each_required_advance_field_enforced(self):
        for field in ("move", "falsifier", "smallest_instance", "bridge_premises", "claim"):
            record = valid_record("S1-P01-B01")
            del record[field]
            self.assertTrue(grid.contract_problems(record), field)

    def test_field_types_enforced(self):
        cases = {"claim": ["not", "a", "string"], "bridge_premises": "none",
                 "predecessors": ["src-1", "src-2", "src-3"], "defeat_queries": "q1; q2; q3; q4; q5",
                 "move": "M9"}
        for field, value in cases.items():
            record = valid_record("S1-P01-B01")
            record[field] = value
            self.assertTrue(grid.contract_problems(record), field)

    def test_predecessor_content_enforced(self):
        for key, value in (("ref", ""), ("read_depth", "skimmed"), ("shows", ""), ("differs", "")):
            record = valid_record("S1-P01-B01")
            record["predecessors"][0][key] = value
            self.assertTrue(grid.contract_problems(record), key)

    def test_kill_reason_enum_enforced(self):
        record = valid_record("S1-P01-B01", "kill")
        record["kill_reason"] = "seems weak"
        self.assertTrue(grid.contract_problems(record))
        for reason in ("incoherent", "trivial-by-definition", "known", "refuted",
                       "no-checkable-instance", "ontology-leap", "out-of-scope"):
            record["kill_reason"] = reason
            self.assertEqual(grid.contract_problems(record), [], reason)

    def test_stage_specific_verdicts(self):
        self.assertTrue(grid.contract_problems(valid_record("S1-P01-B01", "survive")))
        self.assertTrue(grid.contract_problems(valid_record("A-S1-P01-B01", "advance")))
        self.assertEqual(grid.contract_problems(valid_record("A-S1-P01-B01", "survive")), [])

    def test_unknown_cell_id_rejected(self):
        for cell in ("S1-P99-B01", "S1-P01", "T1-P01-P01", "T1-P02-P01", "X1-P01-B01", "A-S1-P99-B01"):
            self.assertTrue(grid.contract_problems(valid_record(cell)), cell)

    def test_malformed_and_non_object_lines_reported_not_fatal(self):
        self.assign("grid-s1-01", "S1-P01-B01")
        self.write_results("grid-s1-01", raw=("{not json", "[1, 2]", "\"text\"", "7"))
        problems = self.problems()
        self.assertEqual(len(problems), 4)
        self.assertEqual(self.adv_ids(), [])


class PromotionTests(GridCase):
    def test_valid_assigned_advance_promotes_once(self):
        self.assign("grid-s1-01", "S1-P01-B01")
        self.write_results("grid-s1-01", valid_record("S1-P01-B01"))
        self.assertEqual(grid.cells(self.ax, "adv"), [("A-S1-P01-B01", CLAIM)])
        self.assertEqual(self.problems(), [])

    def test_invalid_advance_is_not_promoted(self):
        self.assign("grid-s1-01", "S1-P01-B01")
        record = valid_record("S1-P01-B01")
        record["predecessors"] = [{}, {}, {}]
        self.write_results("grid-s1-01", record)
        self.assertEqual(self.adv_ids(), [])
        self.assertTrue(self.problems())

    def test_unassigned_cell_is_not_promoted(self):
        self.write_results("grid-s1-01", valid_record("S1-P01-B01"))
        self.assertEqual(self.adv_ids(), [])
        self.assertTrue(self.problems())

    def test_result_outside_assigned_batch_is_not_promoted(self):
        self.assign("grid-s1-01", "S1-P01-B01")
        self.assign("grid-s1-02", "S1-P02-B01")
        self.write_results("grid-s1-02", valid_record("S1-P01-B01"))
        self.assertEqual(self.adv_ids(), [])
        self.assertTrue(self.problems())

    def test_identical_duplicates_deduplicate(self):
        self.assign("grid-s1-01", "S1-P01-B01")
        self.write_results("grid-s1-01", valid_record("S1-P01-B01"), valid_record("S1-P01-B01"))
        self.assertEqual(self.adv_ids(), ["A-S1-P01-B01"])
        self.assertEqual(self.problems(), [])

    def test_conflicting_claims_quarantined(self):
        self.assign("grid-s1-01", "S1-P01-B01")
        self.write_results("grid-s1-01", valid_record("S1-P01-B01"),
                           valid_record("S1-P01-B01", claim="A different claim."))
        self.assertEqual(self.adv_ids(), [])
        self.assertTrue(any("conflict" in p for p in self.problems()))

    def test_conflicting_verdicts_reported(self):
        self.assign("grid-s1-01", "S1-P01-B01")
        self.write_results("grid-s1-01", valid_record("S1-P01-B01"),
                           valid_record("S1-P01-B01", "kill"))
        self.assertEqual(self.adv_ids(), [])
        self.assertTrue(any("conflict" in p for p in self.problems()))

    def test_invalid_kill_is_not_coverage(self):
        self.assign("grid-s1-01", "S1-P01-B01")
        record = valid_record("S1-P01-B01", "kill")
        record["kill_reason"] = "boring"
        self.write_results("grid-s1-01", record)
        code, out, _ = self.run_main("status")
        self.assertNotEqual(code, 0)
        self.assertNotIn('"kill": 1', out)


class StageTransitionTests(GridCase):
    def test_survivor_with_exact_parent_expands(self):
        self.promote_parent()
        self.write_results("grid-adv-01", valid_record("A-S1-P01-B01", "survive"))
        expanded = self.s2_ids()
        self.assertTrue(expanded)
        self.assertTrue(all(cell.startswith("S2-S1-P01-B01-") for cell in expanded))
        self.assertEqual(self.problems(), [])

    def test_orphan_survivor_not_expanded(self):
        self.assign("grid-adv-01", "A-S1-P01-B01")
        self.write_results("grid-adv-01", valid_record("A-S1-P01-B01", "survive"))
        self.assertEqual(self.s2_ids(), [])
        self.assertTrue(self.problems())

    def test_unassigned_survivor_not_expanded(self):
        self.assign("grid-s1-01", "S1-P01-B01")
        self.write_results("grid-s1-01", valid_record("S1-P01-B01"))
        self.write_results("grid-adv-01", valid_record("A-S1-P01-B01", "survive"))
        self.assertEqual(self.s2_ids(), [])

    def test_stale_survivor_claim_not_expanded(self):
        self.promote_parent()
        self.write_results("grid-adv-01",
                           valid_record("A-S1-P01-B01", "survive", claim="An edited claim."))
        self.assertEqual(self.s2_ids(), [])
        self.assertTrue(self.problems())

    def test_survivor_of_invalidated_parent_not_expanded(self):
        self.promote_parent()
        self.write_results("grid-s1-01", valid_record("S1-P01-B01", claim="A conflicting claim."))
        self.write_results("grid-adv-01", valid_record("A-S1-P01-B01", "survive"))
        self.assertEqual(self.s2_ids(), [])

    def test_survivor_of_killed_parent_not_expanded(self):
        self.assign("grid-s1-01", "S1-P01-B01")
        self.write_results("grid-s1-01", valid_record("S1-P01-B01", "kill"))
        self.assign("grid-adv-01", "A-S1-P01-B01")
        self.write_results("grid-adv-01", valid_record("A-S1-P01-B01", "survive"))
        self.assertEqual(self.s2_ids(), [])

    def test_expansion_cells_never_reenter_adversary(self):
        self.promote_parent()
        self.write_results("grid-adv-01", valid_record("A-S1-P01-B01", "survive"))
        s2 = self.s2_ids()[0]
        self.assign("grid-s2-01", s2)
        self.write_results("grid-s2-01", valid_record(s2))
        self.assertEqual(self.adv_ids(), ["A-S1-P01-B01"])
        self.assertNotIn(f"A-{s2}", self.adv_ids())

    def test_s2_cardinality_is_one_cell_per_ontology(self):
        # CONTRACT.md since 2026-10-20: S2-<cell>-Oz, the move being fixed by the claim.
        self.promote_parent()
        self.write_results("grid-adv-01", valid_record("A-S1-P01-B01", "survive"))
        self.assertEqual(self.s2_ids(), [f"S2-S1-P01-B01-{o['id']}" for o in self.ax["ontologies"]])
        self.assertTrue(grid.contract_problems(valid_record("S2-S1-P01-B01-O1-M1")))


class ScientificControlTests(unittest.TestCase):
    """Fixture dispositions are proposals for independent review. These tests check
    the finite witnesses and fixture completeness; they do not certify entailment,
    priority, novelty or metaphysical truth."""

    def setUp(self):
        self.controls = {row["id"]: row for row in map(
            json.loads, (FIXTURES / "controls.jsonl").read_text().splitlines())}

    def test_fixtures_state_domain_witness_and_limits(self):
        for row in self.controls.values():
            for key in ("domain", "claim", "witness_or_argument", "expected_disposition",
                        "review_limits", "source"):
                self.assertTrue(row.get(key), f"{row['id']} lacks {key}")
            self.assertNotIn("novel", row["expected_disposition"].lower())

    def test_observation_does_not_fix_intervention(self):
        def outcomes(y_rule, do_x=None):
            dist = {}
            for z in (0, 1):
                x = z if do_x is None else do_x
                key = (x, y_rule(x, z))
                dist[key] = dist.get(key, 0) + 0.5
            return dist
        model_a, model_b = (lambda x, z: x), (lambda x, z: z)
        self.assertEqual(outcomes(model_a), outcomes(model_b))
        self.assertNotEqual(outcomes(model_a, do_x=0), outcomes(model_b, do_x=0))

    def test_finite_witness_is_existential_only(self):
        dynamics = {f"{a}{b}": {0: a, 1: b} for a in (0, 1) for b in (0, 1)}
        has_q = {name: f[0] == 0 for name, f in dynamics.items()}
        self.assertTrue(has_q["01"])  # Identity: the instance that motivated the claim.
        self.assertFalse(all(has_q.values()))  # Constant-1 refutes the universal claim.

    def test_completed_paths_need_not_be_deterministic(self):
        omega = [(0, 0), (0, 1)]
        continuations = {}
        for x0, x1 in omega:
            continuations.setdefault(x0, set()).add(x1)
        self.assertGreater(len(continuations[0]), 1)

    def test_gate_checks_shape_not_bridge_quality(self):
        # A shape-valid advance is only eligible for an adversary. The unargued-leap
        # control passes the shape gate exactly as the defended-bridge control does,
        # which is why both need human adjudication.
        with patch.object(grid, "AXES", FIXTURES / "axes.json"):
            for cid in ("control-defended-bridge", "control-unargued-leap"):
                record = valid_record("S1-P01-B01", claim=self.controls[cid]["claim"])
                record["bridge_premises"] = ["stated in the control fixture"]
                self.assertEqual(grid.contract_problems(record), [], cid)


if __name__ == "__main__":
    unittest.main()
