"""Evidence-contract regressions; temporary records and mocked metadata only."""

import contextlib
import copy
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

PROJECT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("check_sources", PROJECT / "scripts/check_sources.py")
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


def record(**changes):
    r = {
        "id": "test-clean", "title": "A precise source title for the clean fixture",
        "url": "https://arxiv.org/abs/1234.56789v2", "checked_on": "2026-10-20",
        "read_depth": "full-text", "kind": "primary-paper", "relevance": "Test only.",
        "limits": "Synthetic fixture; not evidence about a paper.",
        "authors": ["Test Author"], "version": "arXiv:1234.56789v2",
        "locator": "Section 2", "assumptions": "Finite fixture domain.",
        "conclusion": "A fixture conclusion.", "proof_status": "Not audited.",
        "dependencies": [], "related_source_ids": [], "open_questions": [],
    }
    r.update(changes)
    return r


class SourceCheckerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        # Even accidental online calls may neither contact the network nor read
        # or overwrite the project's metadata cache.
        self.enterContext(patch.object(checker, "ROOT", self.root))
        self.enterContext(patch.object(checker, "CACHE", self.root / "cache.json"))
        self.enterContext(patch.object(checker.urllib.request, "urlopen",
                                       side_effect=AssertionError("network forbidden in tests")))

    def write(self, name, *rows):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("".join(json.dumps(r) + "\n" for r in rows))
        return path

    def offline(self, *rows, strict=True):
        rep = checker.Report()
        path = self.write("sources.jsonl", *rows)
        checker.check_offline(checker.load([path], rep), rep, strict=strict)
        return rep

    def cli(self, path, *flags):
        output = io.StringIO()
        with patch.object(sys, "argv", ["check_sources.py", str(path), *flags]):
            with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
                code = checker.main()
        return code, output.getvalue()

    def test_clean_record_and_explicit_empty_lists_pass_strict_cli(self):
        path = self.write("sources.jsonl", record())
        before = path.read_bytes()
        code, output = self.cli(path, "--strict")
        self.assertEqual(code, 0, output)
        self.assertIn("0 errors, 0 warnings", output)
        self.assertEqual(before, path.read_bytes())
        self.assertFalse(checker.CACHE.exists())

    def test_each_missing_full_text_field_is_an_error_only_in_strict_mode(self):
        for key in [*checker.FULL_TEXT_EXTRA, "locator"]:
            with self.subTest(key=key):
                row = record()
                del row[key]
                default = self.offline(row, strict=False)
                strict = self.offline(row)
                self.assertEqual(default.count("ERROR"), 0)
                self.assertEqual(default.count("WARN"), 1)
                self.assertEqual(strict.count("ERROR"), 1)
                self.assertIn(key, strict.items[0][3])

    def test_empty_author_list_does_not_count_as_evidence(self):
        self.assertEqual(self.offline(record(authors=[])).count("ERROR"), 1)

    def test_empty_or_null_contract_text_is_missing(self):
        for value in ("", None):
            with self.subTest(value=value):
                self.assertEqual(self.offline(record(assumptions=value)).count("ERROR"), 1)

    def test_doi_does_not_excuse_missing_full_text_contract(self):
        row = record(url="https://doi.org/10.1063/1.522898")
        del row["version"]
        del row["conclusion"]
        self.assertIn("version, conclusion", self.offline(row).items[0][3])

    def test_unversioned_arxiv_is_warning_by_default_and_error_in_strict(self):
        row = record(url="https://arxiv.org/abs/1234.56789", version="Unpinned preprint")
        self.assertEqual(self.offline(row, strict=False).count("WARN"), 1)
        self.assertEqual(self.offline(row).count("ERROR"), 1)

    def test_numeric_and_old_style_ids_accept_explicit_versions_in_version_field(self):
        for aid in ("1234.56789", "gr-qc/9304027", "math.GT/0309136"):
            with self.subTest(aid=aid):
                row = record(url="https://arxiv.org/abs/" + aid,
                             version=f"arXiv:{aid}v2 (dated edition)")
                self.assertEqual(self.offline(row).count("ERROR"), 0)

    def test_version_must_belong_to_the_cited_identifier(self):
        row = record(url="https://arxiv.org/abs/1234.56789",
                     version="arXiv:9876.54321v2")
        self.assertEqual(self.offline(row).count("ERROR"), 1)

    def test_one_pinned_url_does_not_hide_a_second_unpinned_identifier(self):
        row = record(text_url="https://arxiv.org/html/9876.54321", version="Version v2")
        rep = self.offline(row)
        self.assertEqual(rep.count("ERROR"), 1)
        self.assertIn("9876.54321", rep.items[0][3])

    def test_reproduced_arxiv_record_also_requires_a_pinned_version(self):
        row = record(url="https://arxiv.org/abs/1234.56789", version="Unpinned",
                     read_depth="reproduced")
        self.assertEqual(self.offline(row).count("ERROR"), 1)

    def test_same_file_duplicate_is_always_an_error(self):
        for strict in (False, True):
            self.assertEqual(self.offline(record(), record(), strict=strict).count("ERROR"), 1)

    def copies(self, second, strict):
        files = [self.write("one/sources.jsonl", record()),
                 self.write("two/sources.jsonl", second)]
        rep = checker.Report()
        checker.check_offline(checker.load(files, rep), rep, strict=strict)
        return rep

    def test_identical_cross_file_copy_is_info_by_default_error_in_strict(self):
        self.assertEqual(self.copies(record(), False).count("INFO"), 1)
        rep = self.copies(record(), True)
        self.assertEqual(rep.count("ERROR"), 1)
        self.assertIn("canonical source record", rep.items[0][3])

    def test_read_depth_conflict_is_reported_alongside_duplicate_in_strict(self):
        row = record(read_depth="abstract")
        self.assertEqual(self.copies(row, False).count("WARN"), 1)
        rep = self.copies(row, True)
        self.assertEqual(rep.count("ERROR"), 2)
        self.assertTrue(any("read_depth" in item[3] for item in rep.items))

    def test_same_id_different_titles_is_always_an_error(self):
        self.assertEqual(self.copies(record(title="Unrelated title"), False).count("ERROR"), 1)
        self.assertEqual(self.copies(record(title="Unrelated title"), True).count("ERROR"), 2)

    def test_malformed_json_and_nonobject_do_not_stop_other_records(self):
        path = self.root / "sources.jsonl"
        path.write_text('{broken\n[]\n' + json.dumps(record()) + '\n')
        rep = checker.Report()
        rows = checker.load([path], rep)
        self.assertEqual(rep.count("ERROR"), 2)
        self.assertEqual(len(rows), 1)

    def test_required_base_field_and_unknown_depth_always_fail(self):
        self.assertEqual(self.offline(record(title="", read_depth="skimmed")).count("ERROR"), 2)

    def test_all_locator_aliases_are_supported(self):
        for key in checker.LOCATOR_KEYS:
            with self.subTest(key=key):
                row = record()
                del row["locator"]
                row[key] = "Section 3"
                self.assertEqual(self.offline(row).count("ERROR"), 0)

    def test_default_cli_still_allows_warnings_but_strict_fails(self):
        row = record()
        del row["assumptions"]
        path = self.write("sources.jsonl", row)
        self.assertEqual(self.cli(path)[0], 0)
        code, output = self.cli(path, "--strict")
        self.assertEqual(code, 1)
        self.assertIn("ERROR", output)

    def test_no_source_files_is_a_distinct_cli_failure(self):
        self.assertEqual(self.cli(self.root)[0], 2)

    def online(self, row, metadata, arxiv=None, strict=True):
        rep = checker.Report()
        with patch.object(checker.Net, "crossref", return_value=copy.deepcopy(metadata)):
            with patch.object(checker.Net, "arxiv", return_value=arxiv or {}):
                checker.check_online([("fixture", 1, row)], rep, refresh=False, strict=strict)
        return rep

    def test_historical_bisognano_wichmann_wrong_doi_is_rejected(self):
        # Historical wrong DOI/title documented in knowledge/REVIEW_NOTES.md.
        # Metadata snapshot: project Crossref cache, not a fresh online query.
        row = record(url="https://doi.org/10.1063/1.522676",
                     title="On the duality condition for a Hermitian scalar field. II",
                     version="DOI 10.1063/1.522676")
        hit = {"status": "ok", "title": "Eigenvalues of the invariant operators of the orthogonal and symplectic groups"}
        self.assertEqual(self.online(row, hit).count("ERROR"), 1)

    def test_matching_arxiv_does_not_mask_a_wrong_doi_in_strict_mode(self):
        row = record(doi="10.1063/1.522676")
        ax = {"1234.56789v2": {"status": "ok", "title": row["title"]}}
        hit = {"status": "ok", "title": "An unrelated metadata title"}
        self.assertEqual(self.online(row, hit, ax, strict=False).count("WARN"), 1)
        self.assertEqual(self.online(row, hit, ax).count("ERROR"), 1)

    def test_generic_doi_title_requires_review_and_cannot_pass_strict(self):
        row = record(url="https://doi.org/10.1063/1.522898", version="Published edition")
        hit = {"status": "ok", "title": "Reply"}
        self.assertEqual(self.online(row, hit, strict=False).count("WARN"), 1)
        self.assertEqual(self.online(row, hit).count("ERROR"), 1)

    def test_correct_identifier_title_passes_strict_online_check(self):
        row = record(url="https://doi.org/10.1063/1.522898", version="Published edition")
        rep = self.online(row, {"status": "ok", "title": row["title"]})
        self.assertEqual(rep.items, [])

    def test_online_cli_passes_strict_flag_to_metadata_check(self):
        path = self.write("sources.jsonl", record())
        with patch.object(checker, "check_online", return_value=(1, 0)) as check:
            self.assertEqual(self.cli(path, "--strict", "--online")[0], 0)
        self.assertTrue(check.call_args.kwargs["strict"])


if __name__ == "__main__":
    unittest.main()
