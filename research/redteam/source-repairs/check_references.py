#!/usr/bin/env python3
"""Validate explicit reference targets/provenance; report global duplicates separately.

Exit zero means reference integrity only. Run scripts/check_sources.py --strict
knowledge research separately for the global source-record contract.
"""
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REPORT = Path('research/redteam/source-repairs')


def digest(record):
    return hashlib.sha256(json.dumps(record, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def rows(path):
    return [json.loads(s) for s in path.read_text().splitlines() if s.strip()]


def check(root):
    errors, records, by_id = [], {}, defaultdict(list)
    for folder in ('knowledge', 'research'):
        for path in sorted((root / folder).rglob('*sources.jsonl')):
            relative = str(path.relative_to(root))
            for record in rows(path):
                key = (relative, record['id'])
                if key in records:
                    errors.append('Duplicate ID within ' + relative + ': ' + record['id'])
                records[key] = record
                by_id[record['id']].append(relative)
    old = rows(root / REPORT / 'before-records.jsonl')
    archived = {(r['path'], r['line']): r['record'] for r in old}
    missing = {r['record']['id'] for r in old} - set(by_id)
    errors.extend('Lost source ID: ' + rid for rid in sorted(missing))
    manifest = json.loads((root / REPORT / 'before-manifest.json').read_text())
    if hashlib.sha256((root / REPORT / 'before-records.jsonl').read_bytes()).hexdigest() != manifest.get('snapshot_sha256'):
        errors.append('Archived snapshot digest mismatch')
    seed = 'knowledge/seed-sources.jsonl'
    if hashlib.sha256((root / seed).read_bytes()).hexdigest() != manifest['files'][seed]:
        errors.append('Shared seed changed since snapshot')
    count, covered = 0, set()
    for folder in ('knowledge', 'research'):
        for path in sorted((root / folder).rglob('source-refs.jsonl')):
            local_ids = set()
            for ref in rows(path):
                count += 1
                rid, target = ref['id'], ref['canonical_file']
                if rid in local_ids:
                    errors.append('Repeated reference in ' + str(path) + ': ' + rid)
                local_ids.add(rid)
                if (target, rid) not in records:
                    errors.append('Missing explicit canonical target: ' + target + ': ' + rid)
                if (str(path.relative_to(root)).replace('source-refs.jsonl', 'sources.jsonl'), rid) in records:
                    errors.append('Reference still has local copied payload: ' + rid)
                prior = ref.get('prior_reading', {})
                original = archived.get((prior.get('path'), prior.get('line')))
                archive_key = (prior.get('path'), prior.get('line'))
                if archive_key in covered:
                    errors.append('Archived copy referenced twice: ' + rid)
                covered.add(archive_key)
                if original is None or original.get('id') != rid:
                    errors.append('Missing archived provenance: ' + rid)
                else:
                    for field in ('read_depth', 'version', 'checked_on'):
                        if prior.get(field) != original.get(field):
                            errors.append('Altered prior ' + field + ': ' + rid)
                    if prior.get('record_sha256') != digest(original):
                        errors.append('Archived hash mismatch: ' + rid)
                if prior.get('revision') != manifest['revision'] or prior.get('snapshot') != str(REPORT / 'before-records.jsonl'):
                    errors.append('Unpinned prior snapshot: ' + rid)
                if not ref.get('decision') or not prior.get('reader'):
                    errors.append('Missing decision/reader provenance: ' + rid)
    for prior in old:
        if (prior['path'], prior['record']['id']) not in records and (prior['path'], prior['line']) not in covered:
            errors.append('Removed copy lacks preserved reference: ' + prior['path'] + ': ' + prior['record']['id'])
    aliases = root / 'knowledge/canonical-aliases.jsonl'
    seen_members, seen_works = set(), set()
    alias_count = 0
    if not aliases.exists():
        errors.append('Missing curated alias registry')
    else:
        for group in rows(aliases):
            alias_count += 1
            if group['work_id'] in seen_works:
                errors.append('Duplicate alias work ID: ' + group['work_id'])
            seen_works.add(group['work_id'])
            members = group['members']
            keys = {(m['file'], m['id']) for m in members}
            canonical = group['canonical']
            if (canonical['file'], canonical['id']) not in keys:
                errors.append('Alias canonical is not a member: ' + group['work_id'])
            for member in members:
                key = (member['file'], member['id'])
                if key in seen_members:
                    errors.append('Alias member assigned twice: ' + member['id'])
                seen_members.add(key)
                if key not in records:
                    errors.append('Alias member missing: ' + member['id'])
                else:
                    if member['version'] != records[key].get('version') or member['read_depth'] != records[key]['read_depth']:
                        errors.append('Alias edition/depth drift: ' + member['id'])
            if not group.get('identity_basis'):
                errors.append('Alias identity unsupported: ' + group['work_id'])
    return {'reference_integrity_passed': not errors, 'errors': errors,
            'references': count, 'alias_groups': alias_count,
            'records': sum(len(v) for v in by_id.values()), 'unique_ids': len(by_id),
            'global_duplicate_ids': {rid: paths for rid, paths in sorted(by_id.items()) if len(paths) > 1},
            'limits': 'Explicit targets and preserved provenance checked; global duplicates are reported, not cleared. No semantic or primary-source verification.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    result = check(args.root)
    print(json.dumps(result, indent=2))
    return int(not result['reference_integrity_passed'])


if __name__ == '__main__':
    raise SystemExit(main())
