#!/usr/bin/env python3
"""One-time, snapshot-bound migration; refuses to overwrite already migrated refs."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent


def digest(record):
    return hashlib.sha256(json.dumps(record, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def write(path, rows):
    (ROOT / path).write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows))


def main():
    snapshot = [json.loads(s) for s in (OUT / 'before-records.jsonl').read_text().splitlines()]
    revision = json.loads((OUT / 'before-manifest.json').read_text())['revision']
    canonical = {json.loads(s)['id']: json.loads(s)['canonical'] for s in
                 (ROOT / 'research/redteam/source-canonicalization/canonical-map.jsonl').read_text().splitlines()}
    measurement = 'frontier-page-wootters-measurements-2023'
    canonical[measurement] = {'file': 'knowledge/ico-qrf/sources.jsonl'}
    root_paths = ['knowledge/frontier/sources.jsonl', 'knowledge/ico-qrf/sources.jsonl',
                  'research/theory-map/sources.jsonl']
    for path in root_paths:
        assert not (ROOT / path.replace('sources.jsonl', 'source-refs.jsonl')).exists(), 'Already migrated'
        # These three files are exclusively coordinator-owned during this task.
        original = [row for row in snapshot if row['path'] == path]
        live = [json.loads(s) for s in (ROOT / path).read_text().splitlines() if s.strip()]
        assert live == [row['record'] for row in original], 'Source changed since snapshot: ' + path
    for path in root_paths:
        keep, refs = [], []
        for row in (r for r in snapshot if r['path'] == path):
            record, rid = row['record'], row['record']['id']
            target = canonical.get(rid)
            if target and target['file'] != path:
                decision = ('Primary-backed measurement canonical choice: knowledge/audits/fulltext-spotcheck/clocks-methods/findings.jsonl; arXiv:2308.10967v1 header (2023-08-21).'
                            if rid == measurement else
                            'Explicit ico-qrf supersession: knowledge/REVIEW_NOTES.md:179-183.'
                            if target['file'] == 'knowledge/ico-qrf/sources.jsonl' else
                            'Canonical knowledge-lane policy: knowledge/REVIEW_NOTES.md:131-134; research/redteam/source-canonicalization/MERGE_GATE.md.')
                refs.append({'id': rid, 'canonical_file': target['file'], 'relation': 'inherited-source',
                             'decision': decision,
                             'prior_reading': {'snapshot': 'research/redteam/source-repairs/before-records.jsonl',
                                 'revision': revision, 'path': path, 'line': row['line'],
                                 'record_sha256': digest(record), 'read_depth': record['read_depth'],
                                 'version': record.get('version'), 'checked_on': record['checked_on'],
                                 'reader': record.get('inherited_from', 'Original task-lane reader; personal identity not recorded'),
                                 'map_role': record.get('map_role')},
                             'limits': 'Reference resolves the current canonical extraction; it does not upgrade or verify the prior reader\u2019s reading.'})
            else:
                keep.append(record)
        write(path, keep)
        if refs:
            write(path.replace('sources.jsonl', 'source-refs.jsonl'), refs)
    # This is a new, explicitly pinned reading, not an inferred edition for the old reader.
    path = 'knowledge/frontier/sources.jsonl'
    records = [json.loads(s) for s in (ROOT / path).read_text().splitlines()]
    for r in records:
        if r['id'] == 'frontier-records-time-asymmetry-1993':
            old = next(x for x in snapshot if x['path'] == path and x['record']['id'] == r['id'])
            r['reading_history'] = [{'reader': 'Original frontier lane', 'checked_on': r['checked_on'],
                'read_depth': r['read_depth'], 'version': r['version'],
                'snapshot': 'research/redteam/source-repairs/before-records.jsonl', 'path': path,
                'line': old['line'], 'record_sha256': digest(old['record']),
                'limits': 'Original HTML URL was unversioned; exact edition was not recorded.'},
                {'reader': 'codex-source-repairs coordinator', 'checked_on': '2026-10-20',
                 'read_depth': 'full-text', 'version': 'arXiv:gr-qc/9304027v2 (1993-04-19)',
                 'url': 'https://arxiv.org/html/gr-qc/9304027v2',
                 'locators': 'Theorem 1, Eqs. (1)-(17); discussion following Eq. (22); closing interpretation paragraphs',
                 'limits': 'Bounded body-text check; no independent proof reconstruction or journal collation.'}]
            r['url'] = 'https://arxiv.org/html/gr-qc/9304027v2'
            r['version'] = 'arXiv:gr-qc/9304027v2 (1993-04-19); explicitly checked by coordinator 2026-10-20'
            r['checked_on'] = '2026-10-20'
            r['locators'] = 'Theorem 1, Eqs. (1)-(17); discussion after Eq. (22) and closing interpretive paragraphs'
            r['assumptions'] = 'CPT-invariant Hamiltonian; commuting, separately CPT-invariant initial/final density matrices; exhaustive histories and their CPT reverses both decohere, so both probability assignments exist.'
            r['conclusion'] = 'Theorem 1 equates probabilities of corresponding CPT-reversed histories under these hypotheses. This need not make an individual history symmetric. Page separately offers interpretive criticism of reading the decoherence-functional asymmetry as an independent arrow; no claim about objective passage follows.'
            r['proof_status'] = 'Coordinator inspected the bounded theorem/proof and discussion at the pinned HTML edition; neither independently reconstructed nor numerically reproduced.'
    write(path, records)


if __name__ == '__main__':
    main()
