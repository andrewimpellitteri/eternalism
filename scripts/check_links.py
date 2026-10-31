#!/usr/bin/env python3
"""Report relative Markdown links whose target does not exist. Standard library only."""
import argparse
import pathlib
import re
import subprocess
import sys

LINK = re.compile(r"\[[^\]]*\]\(([^()\s]+)(?:\s+\"[^\"]*\")?\)")


def markdown_files(root):
    listing = subprocess.run(["git", "ls-files", "-co", "--exclude-standard", "*.md"], cwd=root,
                             capture_output=True, text=True, check=True).stdout
    return [root / name for name in listing.splitlines() if (root / name).is_file()]


def targets(text):
    """Yield (line number, link target), skipping fenced code."""
    fenced = False
    for number, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("```"):
            fenced = not fenced
        elif not fenced:
            for match in LINK.finditer(line):
                yield number, match.group(1)


def broken_links(root):
    found = []
    for path in markdown_files(root):
        for number, target in targets(path.read_text(errors="ignore")):
            if re.match(r"[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
                continue
            name = re.sub(r":\d+$", "", target.split("#")[0])
            if not re.search(r"[./]", name):  # [x](y) in prose mathematics
                continue
            if not (path.parent / name).exists():
                found.append((path.relative_to(root).as_posix(), number, target))
    return found


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=pathlib.Path, default=pathlib.Path(__file__).resolve().parent.parent)
    args = parser.parse_args(argv)
    found = broken_links(args.root)
    for path, number, target in found:
        print(f"{path}:{number}: {target}")
    print(f"{len(found)} broken links")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main())
