import importlib.util
import pathlib
import subprocess
import tempfile
import unittest

SCRIPT = pathlib.Path(__file__).resolve().parent.parent / "scripts" / "check_links.py"
spec = importlib.util.spec_from_file_location("check_links", SCRIPT)
check_links = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check_links)


class BrokenLinks(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.dir.cleanup)
        self.root = pathlib.Path(self.dir.name)
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)

    def write(self, text, name="doc.md"):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    def test_reports_missing_relative_target(self):
        self.write("[gone](missing.md)\n")
        self.assertEqual(check_links.broken_links(self.root), [("doc.md", 1, "missing.md")])

    def test_accepts_existing_target_with_anchor_or_line(self):
        self.write("x\n", "sub/there.md")
        self.write("[a](sub/there.md#part) [b](sub/there.md:12)\n")
        self.assertEqual(check_links.broken_links(self.root), [])

    def test_resolves_relative_to_the_linking_file(self):
        self.write("x\n", "top.md")
        self.write("[up](../top.md)\n", "sub/doc.md")
        self.assertEqual(check_links.broken_links(self.root), [])

    def test_ignores_urls_anchors_and_fenced_code(self):
        self.write("[u](https://example.com/x) [a](#here)\n```\n[f](missing.md)\n```\n")
        self.assertEqual(check_links.broken_links(self.root), [])


if __name__ == "__main__":
    unittest.main()
