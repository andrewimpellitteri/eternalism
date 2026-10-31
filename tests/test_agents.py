"""Checks for coordination failures that would let workers collide or skip gates."""
import argparse
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

PROJECT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("agents", PROJECT / "scripts/agents.py")
agents = importlib.util.module_from_spec(spec)
spec.loader.exec_module(agents)


class WorkboardTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.patch = patch.object(agents, "ROOT", self.root)
        self.patch.start()
        (self.root / "scripts").mkdir()
        shutil.copyfile(PROJECT / "scripts/agents.py", self.root / "scripts/agents.py")
        self.book = [self.row("first", "knowledge/first/"),
                     self.row("second", "knowledge/second/", ["first"]),
                     self.row("collision", "knowledge/first/detail/")]
        self.write_book()

    def tearDown(self):
        self.patch.stop()
        self.temp.cleanup()

    def row(self, tid, owns, deps=None):
        return {"id": tid, "title": tid, "priority": 10, "blocked_by": deps or [],
                "owns": [owns], "brief": "A bounded task.", "done_when": ["output reviewed"]}

    def write_book(self):
        (self.root / "WORKBOARD.jsonl").write_text(
            "".join(json.dumps(row) + "\n" for row in self.book))

    def test_dependency_waits_for_acceptance_not_submission(self):
        agents.transition("claim", "first", "one")
        agents.transition("review", "first", "one")
        with self.assertRaisesRegex(ValueError, "blocked"):
            agents.transition("claim", "second", "two")
        agents.transition("accept", "first", "one", "Independently reviewed and integrated.")
        agents.transition("claim", "second", "two")
        self.assertEqual(agents.snapshot()["second"]["status"], "claimed")

    def test_owner_and_file_overlap_enforced_through_review(self):
        agents.transition("claim", "first", "one")
        with self.assertRaisesRegex(ValueError, "another agent"):
            agents.transition("release", "first", "two", "Attempt to steal")
        agents.transition("review", "first", "one")
        with self.assertRaisesRegex(ValueError, "overlaps"):
            agents.transition("claim", "collision", "two")
        agents.transition("release", "first", "one", "Stopped and outputs preserved.")
        agents.transition("claim", "collision", "two")

    def test_concurrent_claims_have_one_winner(self):
        processes = [subprocess.Popen(
            [sys.executable, str(self.root / "scripts/agents.py"), "claim", "first",
             "--agent", f"worker-{index}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            for index in range(2)]
        codes = []
        for process in processes:
            process.communicate(timeout=15)
            codes.append(process.returncode)
        self.assertEqual(sorted(codes), [0, agents.REFUSED])
        self.assertEqual(agents.snapshot()["first"]["status"], "claimed")

    def test_concurrent_overlapping_tasks_have_one_winner(self):
        processes = [subprocess.Popen(
            [sys.executable, str(self.root / "scripts/agents.py"), "claim", tid,
             "--agent", tid], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            for tid in ("first", "collision")]
        codes = []
        for process in processes:
            process.communicate(timeout=15)
            codes.append(process.returncode)
        self.assertEqual(sorted(codes), [0, agents.REFUSED])

    def test_invalid_graph_and_unsafe_path_rejected(self):
        self.book[0]["blocked_by"] = ["second"]
        self.write_book()
        with self.assertRaisesRegex(ValueError, "cycle"):
            agents.tasks()
        self.book[0]["blocked_by"] = []
        self.book[0]["owns"] = ["../outside"]
        self.write_book()
        with self.assertRaisesRegex(ValueError, "unsafe"):
            agents.tasks()

    def test_owns_paths_must_be_plain_relative(self):
        # Dot and empty components normalize to ordinary paths; reject the
        # spellings outright so ownership comparisons always see one form.
        for bad in (["./escape"], ["a//b"], ["a/./b"], ["//share/x"], ["a/b//"]):
            self.book[0]["owns"] = bad
            self.write_book()
            with self.assertRaisesRegex(ValueError, "unsafe"):
                agents.tasks()

    def test_stale_claim_for_retired_task_neither_crashes_nor_blocks(self):
        agents.transition("claim", "first", "one")
        state_path = self.root / ".agent-runtime/coordination/state.json"
        state = json.loads(state_path.read_text())
        state["retired"] = {"status": "claimed", "agent": "gone"}  # task left the board
        state_path.write_text(json.dumps(state))
        self.assertEqual(len(agents.tasks()), len(self.book))  # no KeyError from the stale record
        with self.assertRaisesRegex(ValueError, "overlaps"):
            agents.transition("claim", "collision", "two")  # live claims still guard
        agents.transition("release", "first", "one", "Stopped and outputs preserved.")
        agents.transition("claim", "collision", "two")  # stale record is skipped, not fatal
        self.assertEqual(agents.snapshot()["collision"]["status"], "claimed")

    def test_render_board_rewrites_generated_file(self):
        agents.render_board()
        text = (self.root / "WORKBOARD.md").read_text()
        self.assertIn("`first`", text)
        self.assertIn("`second`", text)

    def test_dry_run_does_not_claim_or_create_runtime(self):
        agents.launch(argparse.Namespace(tasks=["first"], dry_run=True, model=agents.DEFAULT_MODEL))
        self.assertFalse((self.root / ".agent-runtime").exists())
        self.assertFalse((self.root / ".worktrees").exists())

    def test_resume_dry_run_keeps_previous_result(self):
        agents.transition("claim", "first", "glm-first")
        (self.root / ".worktrees/first").mkdir(parents=True)
        run = self.root / ".agent-runtime/runs/first"
        run.mkdir(parents=True)
        (run / "result.json").write_text("{}")
        agents.resume(argparse.Namespace(task="first", dry_run=True, model=agents.DEFAULT_MODEL))
        self.assertEqual(sorted(path.name for path in run.iterdir()), ["result.json"])

    def test_committed_launch_preserves_disjoint_work_and_rejects_unsafe_inputs(self):
        def run_git(*args):
            return subprocess.run(["git", *args], cwd=self.root, check=True,
                                  capture_output=True, text=True)
        (self.root / "active").mkdir()
        active = self.root / "active/model.py"
        active.write_text("committed = True\n")
        run_git("init", "-b", "main")
        run_git("add", "WORKBOARD.jsonl", "scripts/agents.py", "active/model.py")
        run_git("-c", "user.name=Test", "-c", "user.email=test@example.invalid",
                "commit", "-m", "Fixture")
        baseline = run_git("rev-parse", "HEAD").stdout.strip()
        active.write_text("concurrent = True\n")
        untracked = self.root / "active/report.md"
        untracked.write_text("unfinished report\n")
        with self.assertRaisesRegex(ValueError, "current changes"):
            agents.launch_baseline(agents.tasks(), ["first"])
        self.assertEqual(agents.launch_baseline(agents.tasks(), ["first"], True), baseline)
        worker = self.root / "worker"
        run_git("worktree", "add", "--detach", str(worker), baseline)
        self.assertEqual((worker / "active/model.py").read_text(), "committed = True\n")
        self.assertFalse((worker / "active/report.md").exists())
        self.assertEqual(active.read_text(), "concurrent = True\n")
        self.assertEqual(untracked.read_text(), "unfinished report\n")
        board = self.root / "WORKBOARD.jsonl"
        original = board.read_text()
        board.write_text(original + "\n")
        with self.assertRaisesRegex(ValueError, "clean coordination"):
            agents.launch_baseline(agents.tasks(), ["first"], True)
        board.write_text(original)
        output = self.root / "knowledge/first"
        output.mkdir(parents=True)
        (output / "uncommitted.md").write_text("preserve me\n")
        with self.assertRaisesRegex(ValueError, "task output"):
            agents.launch_baseline(agents.tasks(), ["first"], True)
        self.assertEqual((output / "uncommitted.md").read_text(), "preserve me\n")

    def test_main_and_worktree_share_claim_store(self):
        def run_git(*args):
            return subprocess.run(["git", *args], cwd=self.root, check=True,
                                  capture_output=True, text=True)
        run_git("init", "-b", "main")
        run_git("add", "WORKBOARD.jsonl", "scripts/agents.py")
        run_git("-c", "user.name=Test", "-c", "user.email=test@example.invalid",
                "commit", "-m", "Fixture")
        wt = self.root / "worker"
        run_git("worktree", "add", "-b", "worker", str(wt))
        agents.transition("claim", "first", "one")
        with patch.object(agents, "ROOT", wt):
            self.assertEqual(agents.snapshot()["first"]["agent"], "one")
            with self.assertRaisesRegex(ValueError, "claimed"):
                agents.transition("claim", "first", "two")

    def test_accept_allows_required_root_report_but_rejects_other_unowned_files(self):
        def run_git(*args, cwd=None):
            return subprocess.run(["git", *args], cwd=cwd or self.root, check=True,
                                  capture_output=True, text=True)
        def commit(message, cwd=None):
            run_git("-c", "user.name=Test", "-c", "user.email=test@example.invalid",
                    "commit", "-m", message, cwd=cwd)
        run_git("init", "-b", "main")
        run_git("add", "WORKBOARD.jsonl", "scripts/agents.py")
        commit("Fixture")
        baseline = run_git("rev-parse", "HEAD").stdout.strip()
        wt = self.root / "worker"
        run_git("worktree", "add", "-b", "worker", str(wt))
        agents.transition("claim", "first", "glm-first", extra={
            "worktree": str(wt), "branch": "worker", "base": baseline})
        (wt / "knowledge/first").mkdir(parents=True)
        (wt / "knowledge/first/result.md").write_text("Owned result\n")
        (wt / "AGENT_REPORT.md").write_text("Required handback\n")
        (wt / "unowned.txt").write_text("Must reject\n")
        run_git("add", "knowledge/first/result.md", "AGENT_REPORT.md", "unowned.txt", cwd=wt)
        commit("Submission with rogue file", cwd=wt)
        run_git("merge", "--ff-only", "worker")
        agents.transition("review", "first", "glm-first")
        with self.assertRaisesRegex(ValueError, "out-of-scope"):
            agents.transition("accept", "first", "glm-first", "Reviewed fixture")
        run_git("rm", "unowned.txt", cwd=wt)
        commit("Remove rogue file", cwd=wt)
        run_git("merge", "--ff-only", "worker")
        agents.transition("accept", "first", "glm-first", "Reviewed and integrated fixture")
        self.assertEqual(agents.snapshot()["first"]["status"], "done")


class FreshSubmissionTests(unittest.TestCase):
    """Use actual Git history: an inherited report must never imply delivery."""

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.git("init", "-b", "main")
        (self.root / "AGENT_REPORT.md").write_text("Report inherited from another task\n")
        (self.root / "owned").mkdir()
        (self.root / "owned/old.md").write_text("Inherited owned output\n")
        self.commit("Baseline", "AGENT_REPORT.md", "owned/old.md")
        self.base = self.git("rev-parse", "HEAD").stdout.strip()

    def tearDown(self):
        self.temp.cleanup()

    def git(self, *args):
        return subprocess.run(["git", *args], cwd=self.root, check=True,
                              capture_output=True, text=True)

    def commit(self, message, *files):
        if files:
            self.git("add", *files)
        self.git("-c", "user.name=Test", "-c", "user.email=test@example.invalid",
                 "commit", "-m", message)

    def deliver(self):
        (self.root / "AGENT_REPORT.md").write_text("This task's fresh report\n")
        (self.root / "owned/result.md").write_text("This task's result\n")
        self.commit("Deliver", "AGENT_REPORT.md", "owned/result.md")

    def outcome(self, code=0, quota=None):
        return agents.worker_outcome(self.root, self.base, ["owned/"], code, quota)

    def test_inherited_report_rejected_after_zero_exit_and_quota_failure(self):
        for code, quota in ((0,None),(1,"Usage limit reached for 5 hour")):
            outcome, reason = self.outcome(code,quota)
            self.assertEqual(outcome, "failed")
            self.assertIn("no fresh committed", reason)
            if quota:
                self.assertIn(quota,reason)

    def test_fresh_handback_survives_zero_nonzero_and_post_commit_quota(self):
        self.deliver()
        for code, quota in ((0,None),(1,None),(1,"quota after commit")):
            outcome,reason = self.outcome(code,quota)
            self.assertEqual(outcome,"review")
            self.assertIn(f"exit {code}",reason)
            if quota:
                self.assertIn(quota,reason)

    def test_fresh_report_without_owned_output_does_not_deliver(self):
        (self.root / "AGENT_REPORT.md").write_text("New report only\n")
        self.commit("Report only", "AGENT_REPORT.md")
        self.assertIn("no task-owned output",self.outcome()[1])

    def test_owned_output_with_inherited_report_does_not_deliver(self):
        (self.root / "owned/result.md").write_text("New result\n")
        self.commit("Output only", "owned/result.md")
        self.assertIn("no fresh committed",self.outcome()[1])

    def test_dirty_fresh_report_and_untracked_output_do_not_deliver(self):
        self.deliver()
        (self.root / "owned/incomplete.md").write_text("Interrupted work\n")
        self.assertEqual(self.outcome()[0],"failed")
        self.assertIn("dirty",self.outcome()[1])

    def test_out_of_scope_committed_file_does_not_deliver(self):
        self.deliver()
        (self.root / "rogue.md").write_text("Unowned change\n")
        self.commit("Unowned change", "rogue.md")
        self.assertIn("out-of-scope",self.outcome()[1])

    def test_missing_or_unavailable_launch_base_fails_closed(self):
        self.deliver()
        for base in (None,"main","0"*40):
            outcome,_ = agents.worker_outcome(self.root,base,["owned/"],0)
            self.assertEqual(outcome,"failed")

    def test_deleted_report_or_deletion_only_output_does_not_deliver(self):
        (self.root / "AGENT_REPORT.md").write_text("New report\n")
        self.git("rm","owned/old.md")
        self.commit("Deletion only", "AGENT_REPORT.md")
        self.assertIn("no surviving",self.outcome()[1])
        self.git("rm","AGENT_REPORT.md")
        self.commit("Remove report")
        self.assertIn("no fresh committed",self.outcome()[1])


class ProjectContractTests(unittest.TestCase):
    def test_live_task_graph_is_valid(self):
        # tasks() raises on duplicate IDs, bad IDs, unsafe owns, unknown or cyclic deps;
        # compare against the raw file so a silently dropped row is also caught.
        rows = [json.loads(line) for line in
                (PROJECT / "WORKBOARD.jsonl").read_text().splitlines() if line.strip()]
        book = agents.tasks()
        self.assertEqual(set(book), {row["id"] for row in rows})
        for row in rows:  # Every field the runner and brief renderer index directly.
            for key in ("title", "priority", "blocked_by", "owns", "brief", "done_when"):
                self.assertIn(key, row, f"{row['id']} lacks {key}")
            self.assertTrue(row["owns"], f"{row['id']} owns nothing")

    def test_seed_sources_contract(self):
        records = [json.loads(line) for line in
                   (PROJECT / "knowledge/seed-sources.jsonl").read_text().splitlines()]
        self.assertEqual(len(records), len({row["id"] for row in records}))
        for row in records:
            self.assertTrue(row["url"].startswith("https://"))
            self.assertIn(row["read_depth"], {"discovery", "abstract", "full-text",
                                             "reproduced", "code-audited"})
            self.assertTrue(row["limits"])

    def test_worker_permission_contract(self):
        config = json.loads((PROJECT / "scripts/agents/opencode-agent.json").read_text())
        self.assertNotIn("mcp", config)  # Do not disable the user's search MCP.
        self.assertEqual(config["permission"]["webfetch"], "allow")

    def test_validation_is_board_size_agnostic(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(agents, "ROOT", Path(temp)):
            rows = [{"id": f"t{index}", "title": "t", "priority": 1,
                     "blocked_by": [f"t{index - 1}"] if index else [], "owns": [f"out/t{index}/"],
                     "brief": "b", "done_when": ["d"]} for index in range(5)]
            (Path(temp) / "WORKBOARD.jsonl").write_text(
                "".join(json.dumps(row) + "\n" for row in rows))
            self.assertEqual(len(agents.tasks()), 5)
            del rows[2]["owns"]  # The 2026-10-19 half-written row that killed six workers.
            (Path(temp) / "WORKBOARD.jsonl").write_text(
                "".join(json.dumps(row) + "\n" for row in rows))
            with self.assertRaisesRegex(ValueError, "t2 lacks owns"):
                agents.tasks()


if __name__ == "__main__":
    unittest.main()
