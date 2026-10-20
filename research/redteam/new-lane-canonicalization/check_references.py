#!/usr/bin/env python3
"""Check live sources, references and aliases against both preserved migrations.

This supersedes the first migration's snapshot-specific validator for the live
corpus. The older script and its evidence remain historical and unchanged.
"""
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ARCHIVES = (
    'research/redteam/source-repairs/before-records.jsonl',
    'research/redteam/new-lane-canonicalization/before-records.jsonl',
)


def digest(record):
    return hashlib.sha256(json.dumps(record, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def rows(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


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
    duplicates = {rid: paths for rid, paths in sorted(by_id.items()) if len(paths) > 1}
    for rid in duplicates:
        errors.append('Global duplicate ID: ' + rid)

    archives, manifests = {}, {}
    for name in ARCHIVES:
        path = root / name
        manifest_path = path.parent / 'before-manifest.json'
        if not path.exists() or not manifest_path.exists():
            errors.append('Missing migration archive/manifest: ' + name)
            continue
        manifest = json.loads(manifest_path.read_text())
        manifests[name] = manifest
        if hashlib.sha256(path.read_bytes()).hexdigest() != manifest.get('snapshot_sha256'):
            errors.append('Archived snapshot digest mismatch: ' + name)
        indexed = {}
        for row in rows(path):
            key = (row['path'], row['line'])
            if key in indexed:
                errors.append('Repeated archive position: ' + name + ': ' + str(key))
            indexed[key] = row['record']
            if row['record']['id'] not in by_id:
                errors.append('Lost source ID: ' + row['record']['id'])
        archives[name] = indexed
        seed = 'knowledge/seed-sources.jsonl'
        if (not (root / seed).exists() or
                hashlib.sha256((root / seed).read_bytes()).hexdigest() != manifest.get('files', {}).get(seed)):
            errors.append('Shared seed changed since snapshot: ' + name)

    count, covered, used_archive_entries = 0, set(), set()
    for folder in ('knowledge', 'research'):
        for path in sorted((root / folder).rglob('source-refs.jsonl')):
            local_ids = set()
            for ref in rows(path):
                count += 1
                rid, target = ref['id'], ref['canonical_file']
                if rid in local_ids:
                    errors.append('Repeated reference in ' + str(path.relative_to(root)) + ': ' + rid)
                local_ids.add(rid)
                if (target, rid) not in records:
                    errors.append('Missing explicit canonical target: ' + target + ': ' + rid)
                local_source = str(path.relative_to(root)).replace('source-refs.jsonl', 'sources.jsonl')
                if (local_source, rid) in records:
                    errors.append('Reference still has local copied payload: ' + rid)
                prior = ref.get('prior_reading', {})
                archive_name = prior.get('snapshot')
                position = (prior.get('path'), prior.get('line'))
                archive_entry = (archive_name, *position)
                original = archives.get(archive_name, {}).get(position)
                valid = True
                if archive_entry in used_archive_entries:
                    errors.append('Archived copy referenced twice: ' + rid)
                used_archive_entries.add(archive_entry)
                if original is None or original.get('id') != rid:
                    errors.append('Missing archived provenance: ' + rid)
                    valid = False
                else:
                    for field in ('read_depth', 'version', 'checked_on'):
                        if prior.get(field) != original.get(field):
                            errors.append('Altered prior ' + field + ': ' + rid)
                            valid = False
                    if prior.get('record_sha256') != digest(original):
                        errors.append('Archived hash mismatch: ' + rid)
                        valid = False
                manifest = manifests.get(archive_name)
                if manifest is None or prior.get('revision') != manifest.get('revision'):
                    errors.append('Unpinned prior snapshot: ' + rid)
                    valid = False
                if prior.get('path') != local_source:
                    errors.append('Prior reading belongs to another lane: ' + rid)
                    valid = False
                if (not ref.get('decision') or not prior.get('reader') or
                        ref.get('relation') != 'inherited-source'):
                    errors.append('Missing decision/reader/relation provenance: ' + rid)
                    valid = False
                if valid:
                    # Identical copies recur in consecutive archives. A ref to
                    # either snapshot preserves that exact lane payload; changed
                    # versions require separate evidence, never ID-only coverage.
                    covered.add((prior['path'], rid, digest(original)))

    for name, archived in archives.items():
        for (path, line), original in archived.items():
            rid = original['id']
            if (path, rid) not in records and (path, rid, digest(original)) not in covered:
                errors.append('Removed copy lacks preserved reference: ' + name + ': ' + path + ': ' + rid)

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
                elif (member['version'] != records[key].get('version') or
                      member['read_depth'] != records[key]['read_depth']):
                    errors.append('Alias edition/depth drift: ' + member['id'])
            if not group.get('identity_basis'):
                errors.append('Alias identity unsupported: ' + group['work_id'])

    return {'reference_integrity_passed': not errors, 'errors': errors,
            'references': count, 'alias_groups': alias_count,
            'archives': list(archives), 'records': sum(len(v) for v in by_id.values()),
            'unique_ids': len(by_id), 'global_duplicate_ids': duplicates,
            'limits': 'Identity, references and preserved provenance only; no source-entailment, theorem, reading, novelty or ontology certification. Manifest digests are integrity checks, not signatures.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    result = check(args.root)
    print(json.dumps(result, indent=2))
    return int(not result['reference_integrity_passed'])


if __name__ == '__main__':
    raise SystemExit(main())
