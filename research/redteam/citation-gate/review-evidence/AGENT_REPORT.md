# Evidence and input-handling review

Review target: the current uncommitted `scripts/check_sources.py` and
`tests/test_check_sources.py` for `rt-citation-gate-hardening`. Read-only review;
no checker, test, board, source-register, or cache files were changed.

## Finding

**Malformed JSON values can crash the checker instead of producing a diagnostic.**
I reproduced this with a one-record temporary JSONL fixture containing
`"id": []`. `load()` raises `TypeError: cannot use 'list' as a set element`
when it checks `rid in ids`. A truthy non-string depth such as
`"read_depth": ["full-text"]` also raises `TypeError` at membership testing
against `DEPTHS`. These are valid JSON documents with invalid field shapes.
The current regression test covers malformed JSON syntax and a non-object row,
but not malformed field types.

This does not undermine the required evidence checks on valid source records,
and the stated acceptance criteria do not define a complete JSON type schema.
It is a focused robustness gap worth fixing if malformed-record handling is
part of the intended gate: validate `id` and `read_depth` as scalar strings
before set membership / set-key use, emit an `ERROR`, and continue with later
records. Avoid expanding this task into a full schema redesign.

## Reviewed behavior

- Required and full-text fields use `has_content`, so absent, null, empty, and
  whitespace-only strings fail. Empty author lists fail. Full-text
  `dependencies`, `related_source_ids`, and `open_questions` accept an
  explicitly empty list, while missing, null, or nonempty-but-blank lists
  fail. This is a coherent presence policy: an empty list records “none,”
  though it cannot establish that the assertion is true.
- Strict mode turns missing full-text fields / locators and unpinned arXiv
  editions into errors. Cross-file duplicate IDs are errors in strict mode;
  differing read depths also produce an error. Same-file repeated IDs already
  fail in both modes. If the same ID has both a title and depth conflict, the
  duplicate and title errors are reported, while the depth branch is skipped;
  the strict duplicate still blocks acceptance, so this is not a separate
  acceptance blocker.
- The tests isolate filesystem effects: `ROOT` and `CACHE` are patched to each
  test's temporary directory, every test forbids `urlopen`, online metadata
  methods are mocked, and the clean CLI fixture confirms no project cache is
  created. I found no test-network or live-cache leak.

## Checks and limits

- `python3 -m unittest discover -s tests -p test_check_sources.py -v`: all 33
  tests passed offline.
- The malformed-field reproductions used temporary directories and did not
  touch the source-check cache or source registers.
- I did not re-run live online metadata lookup. This review does not verify
  source reading depth, locator accuracy, or title/claim entailment.

## Recheck of coordinator fixes

Rechecked the updated checker after the coordinator added ID/depth/title type
guards. The malformed-input finding above is **resolved**: invalid IDs are
reported and skipped while later valid rows continue; list/dict `read_depth`
values now produce errors without reaching set membership; non-string titles
are diagnosed and safe during cross-file comparison. Empty unhashable depth
values `[]` and `{}` also produce errors (both the required-field gap and the
invalid-depth diagnostic), without crashing.

- `python3 -m unittest discover -s tests -p test_check_sources.py -v`: all 38
  tests pass offline.
- Additional temporary-fixture checks for `read_depth` values `[]`, `{}`,
  `['full-text']`, and `{'depth': 'full-text'}` all returned error diagnostics
  and did not crash.
- No remaining blocker found in the assigned evidence-presence, empty-list,
  duplicate/depth, malformed-input, or test-isolation areas. This is limited to
  the reviewed checker behavior and does not accept the task overall.
