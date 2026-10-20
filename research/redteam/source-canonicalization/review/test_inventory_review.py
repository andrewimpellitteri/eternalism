"""Read-only review fixtures for the source canonicalization inventory."""
import importlib.util
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
SCRIPT = REPO / "research/redteam/source-canonicalization/inventory.py"
SPEC = importlib.util.spec_from_file_location("source_inventory_under_review", SCRIPT)
inventory = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(inventory)


def row(rid="example", **updates):
    value = {
        "id": rid,
        "title": "Example source",
        "url": "https://doi.org/10.1000/example",
        "read_depth": "abstract",
        "version": "DOI 10.1000/example",
        "relevance": "fixture",
        "limits": "fixture only",
    }
    value.update(updates)
    return value


class InventoryReviewTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "knowledge/lane").mkdir(parents=True)
        (self.root / "research/theory-map").mkdir(parents=True)

    def tearDown(self):
        self.temp.cleanup()

    def write_records(self, path, records):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("".join(json.dumps(r) + "\n" for r in records), encoding="utf-8")

    def rows(self):
        return inventory.inventory(self.root)[0]

    def test_equal_source_payload_ignores_provenance_annotations(self):
        base = row("same")
        research_copy = dict(base, inherited_from="knowledge/lane/sources.jsonl", map_role="inherited")
        self.write_records("knowledge/lane/sources.jsonl", [base])
        self.write_records("research/theory-map/sources.jsonl", [research_copy])
        result = next(r for r in self.rows() if r["id"] == "same")
        self.assertEqual(result["classification"], "identical-copy")
        self.assertEqual(result["canonical"]["file"], "knowledge/lane/sources.jsonl")
        self.assertEqual({d["field"] for d in result["field_differences"]},
                         {"inherited_from", "map_role"})

    def test_stale_research_copy_keeps_knowledge_canonical(self):
        canonical = row("stale", url="https://doi.org/10.2307/correct")
        stale = row("stale", url="https://doi.org/10.2307/wrong")
        self.write_records("knowledge/foundations/sources.jsonl", [canonical])
        self.write_records("research/theory-map/sources.jsonl", [stale])
        result = next(r for r in self.rows() if r["id"] == "stale")
        self.assertEqual(result["classification"], "stale-copy")
        self.assertEqual(result["canonical"]["file"], "knowledge/foundations/sources.jsonl")
        self.assertIn("url", [d["field"] for d in result["field_differences"]])

    def test_explicit_deeper_lane_supersession_selects_named_copy(self):
        rid = "frontier-qrf-indefinite-order-2022v3"
        shallow = row(rid, read_depth="discovery")
        deep = row(rid, read_depth="full-text", section_locator="Sec. 4")
        self.write_records("knowledge/frontier/sources.jsonl", [shallow])
        self.write_records("knowledge/ico-qrf/sources.jsonl", [deep])
        self.write_records("research/theory-map/sources.jsonl", [shallow])
        result = next(r for r in self.rows() if r["id"] == rid)
        self.assertEqual(result["classification"], "depth-superseding")
        self.assertEqual(result["canonical"]["file"], "knowledge/ico-qrf/sources.jsonl")
        self.assertEqual(result["canonical"]["read_depth"], "full-text")

    def test_equal_depth_conflicting_knowledge_copies_stay_unresolved(self):
        self.write_records("knowledge/lane-a/sources.jsonl", [row("conflict", title="Edition A")])
        self.write_records("knowledge/lane-b/sources.jsonl", [row("conflict", title="Edition B")])
        result = next(r for r in self.rows() if r["id"] == "conflict")
        self.assertEqual(result["classification"], "true-conflict")
        self.assertIsNone(result["canonical"])
        self.assertTrue(result["decision_needed"])

    def test_field_diff_distinguishes_missing_from_explicit_null(self):
        missing = row("null-diff")
        explicit_null = row("null-diff", doi=None)
        self.write_records("knowledge/lane/sources.jsonl", [missing])
        self.write_records("research/theory-map/sources.jsonl", [explicit_null])
        result = next(r for r in self.rows() if r["id"] == "null-diff")
        diff = next(d for d in result["field_differences"] if d["field"] == "doi")
        self.assertEqual([v["present"] for v in diff["values"]], [False, True])
        self.assertEqual([v["value"] for v in diff["values"]], [None, None])

    def test_cli_gate_returns_nonzero_for_new_id_requiring_review(self):
        self.write_records("knowledge/lane/sources.jsonl", [row("existing")])
        incoming_path = self.root / "incoming.jsonl"
        incoming_path.write_text(json.dumps(row("new")) + "\n", encoding="utf-8")
        output = StringIO()
        with redirect_stdout(output):
            code = inventory.main(["--root", str(self.root), "--incoming", str(incoming_path)])
        result = json.loads(output.getvalue())[0]
        self.assertEqual(result["action"], "review-new-id")
        self.assertNotEqual(code, 0, "a gate requiring review must not report a passing exit status")

    def test_incoming_stale_stein_doi_copy_is_held_with_url_diff(self):
        # Historical case: cc5344e theory-map carried this wrong DOI; 1ee2847
        # replaced it with the corrected knowledge/foundations copy.
        canonical = row("found-stein-1968", url="https://doi.org/10.2307/2024512")
        stale = row("found-stein-1968", url="https://doi.org/10.2307/2023910")
        self.write_records("knowledge/foundations/sources.jsonl", [canonical])
        rows = self.rows()
        incoming = [{"file": "incoming/sources.jsonl", "line": 1, "record": stale}]
        result = inventory.incoming_gate(incoming, rows)[0]
        self.assertEqual(result["action"], "hold-existing-id")
        self.assertFalse(result["unresolved"])
        self.assertIn("url", result["changed_fields"])


if __name__ == "__main__":
    unittest.main()
