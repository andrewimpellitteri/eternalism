# Independent review: arXiv edition and title checks

## Finding

**Contract blocker, strict-online false pass (high severity for the gate):** when a pinned arXiv edition exists but its page does not yield a `citation_title` meta tag, the checker can certify the record against the latest DataCite/base title instead of the cited edition's title.

In `Net.arxiv`, lines 311–318 initialize `hit["title"]` from DataCite and add `version_title` only when the HTML regex finds the edition title. An HTTP 200 response without a matching tag therefore leaves a normal `status: ok` response with only the base/latest title. In `check_online`, lines 362–365 strict mode chooses the version title only if present; with it absent, strict mode compares against `hit["title"]`. A stale-edition title mismatch can consequently pass when the current title matches the source record.

Minimal mocked reproduction against the current checker:

```python
row = {
    "id": "x",
    "title": "Current title of arXiv record",
    "url": "https://arxiv.org/abs/1234.56789v1",
    "version": "arXiv:1234.56789v1",
}
mock = {"1234.56789v1": {"status": "ok", "title": row["title"]}}
# patch Net.arxiv to return `mock`, patch Net.save to no-op, then:
check_online([("fixture", 1, row)], report, False, strict=True)
# report.items == []
```

The mock represents an HTTP 200 edition lookup whose page supplied no parseable version title; `title` is the DataCite latest title. The result is a false pass because the checker has no evidence that the cited version has that title. Strict mode should fail closed or report a warning (which already makes strict CLI fail) when an exact version was queried but its title could not be obtained. The HTML parser should also tolerate ordinary attribute order/quote variants if the metadata endpoint remains the source.

## Reviewed behavior

The latest shared snapshot recognizes numeric and legacy arXiv IDs pinned in the version field, including `ID (v2)` and URL forms. It associates pins with the corresponding paper ID, checks conflicting versions, and queries the pinned edition online. I did not find a remaining concrete parser false pass in those paths during this review. The parenthetical-ID support appeared in the live diff during review and was checked against the current implementation.

The strict path also correctly compares each identifier independently, so a matching arXiv record does not conceal a wrong DOI title. When `version_title` is present, strict mode uses that title and does not let the DataCite latest title mask an edition-title mismatch.

## Checks and limits

- `python3 -m unittest discover -s tests -p test_check_sources.py -v`: **33 tests passed**.
- Ran the minimal reproduction above using only mocked metadata; it returned an empty report as described.
- No network calls, installs, source-record edits, checker edits, or board edits were made.
- This is a code-path review with mocked metadata, not a live audit of arXiv HTML variants or of the citation corpus.

## Coordinator fix review and disposition

Reviewed the updated shared diff. The false-pass path is closed: for a strict lookup of a versioned arXiv ID, missing `version_title` now emits a warning that the latest title cannot verify the edition. Strict CLI returns failure on warnings. If the version title exists, strict title matching uses only that edition title. This preserves a clean pass when the cited edition title matches even if the latest title differs, and catches the reverse mismatch.

Re-ran the minimal mocked reproduction after the fix. It now yields:

```text
WARN x [fixture:1]
arXiv 1234.56789v1: exact-version title unavailable; latest title cannot verify this edition
```

Also confirmed the current diff includes the intended ID (vN) spelling support and exact pinned IDs in strict online lookup. **No remaining concrete blocker found in the assigned arXiv identity/version and online edition/title scope.**

Final checks:

- `python3 -m unittest discover -s tests -p test_check_sources.py -v`: **38 tests passed**.
- Minimal mocked reproduction: now fails strict acceptance as intended.
- No network calls or edits outside this report were made.

## Final compatibility refinement

Reviewed the follow-up change allowing edition-only version fields (`vN`, `Version vN`, optionally followed by a date in parentheses) when exactly one arXiv paper is cited. The edition is bound to that sole paper, so strict online lookup checks the actual `...vN` endpoint. The full-field regex does not accept arbitrary prose such as `uses Lean v4`; that record remains unpinned in strict mode. With multiple paper identities, the shorthand is not attached and strict mode continues to report unpinned IDs.

- `python3 -m unittest discover -s tests -p test_check_sources.py -v`: **39 tests passed**.
- The new edition-only fixture covers `v3`, `v3 (2011-09-21)`, and `Version v3`, including the resolved strict lookup ID.
- **No remaining blocker found** in the assigned arXiv identity/version and online edition/title scope.
