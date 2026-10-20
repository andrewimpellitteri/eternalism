"""Temporary fixture tests for source reference migration/checker behavior.

Run from repository root: python3 -m unittest discover -s research/redteam/source-repairs/review -v
The tests never edit the live workspace source registers.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[4]
REPAIR = ROOT / 'research/redteam/source-repairs'

def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

CHECKER = load_module('ref_checker', REPAIR / 'check_references.py')
INTEGRATOR = load_module('ref_integrator', REPAIR / 'integrate_references.py')


def dump(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows))


def digest(record):
    return hashlib.sha256(json.dumps(record, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


class ReferenceCheckerFixtureTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.rep = self.root / 'research/redteam/source-repairs'
        self.canonical_path = 'knowledge/ico-qrf/sources.jsonl'
        self.source = {'id': 'paper-a', 'title': 'Paper A', 'read_depth': 'full-text',
                       'version': 'arXiv:1234.5678v2', 'checked_on': '2026-10-19'}
        self.archive_row = {'path': 'knowledge/frontier/sources.jsonl', 'line': 1,
                            'record': dict(self.source)}
        dump(self.root / self.canonical_path, [dict(self.source)])
        dump(self.root / 'knowledge/seed-sources.jsonl', [{'id':'seed-x'}])
        seed_hash = hashlib.sha256((self.root / 'knowledge/seed-sources.jsonl').read_bytes()).hexdigest()
        dump(self.rep / 'before-records.jsonl', [self.archive_row])
        snapshot_hash = hashlib.sha256((self.rep / 'before-records.jsonl').read_bytes()).hexdigest()
        (self.rep / 'before-manifest.json').write_text(json.dumps({
            'revision': 'rev0', 'records': 1, 'snapshot_sha256': snapshot_hash,
            'files': {'knowledge/seed-sources.jsonl': seed_hash}}))
        self.ref_path = self.root / 'knowledge/frontier/source-refs.jsonl'
        dump(self.ref_path, [self.reference()])

    def tearDown(self):
        self.tmp.cleanup()

    def reference(self):
        return {'id': 'paper-a', 'canonical_file': self.canonical_path,
                'relation': 'inherited-source', 'decision': 'fixture decision',
                'prior_reading': {'snapshot': 'research/redteam/source-repairs/before-records.jsonl',
                    'revision': 'rev0', 'path': self.archive_row['path'], 'line': 1,
                    'record_sha256': digest(self.source), 'read_depth': self.source['read_depth'],
                    'version': self.source['version'], 'checked_on': self.source['checked_on'],
                    'reader': 'fixture lane'}, 'limits': 'No reading upgrade.'}

    def check(self):
        return CHECKER.check(self.root)

    def test_absent_alias_registry_fails(self):
        result=self.check()
        self.assertFalse(result['reference_integrity_passed'])
        self.assertIn('Missing curated alias registry', result['errors'])

    def test_valid_target_provenance_and_alias_pass(self):
        alias = {'work_id':'work-a', 'canonical': {'file':self.canonical_path,'id':'paper-a'},
                 'members':[{'file':self.canonical_path,'id':'paper-a','version':self.source['version'],
                             'read_depth':self.source['read_depth']}], 'identity_basis':'fixture identity evidence'}
        dump(self.root / 'knowledge/canonical-aliases.jsonl', [alias])
        result=self.check()
        self.assertTrue(result['reference_integrity_passed'], result['errors'])
        self.assertEqual(result['references'],1)
        self.assertEqual(result['alias_groups'],1)

    def test_wrong_target_and_lost_id_fail(self):
        ref=self.reference(); ref['canonical_file']='knowledge/missing/sources.jsonl'; dump(self.ref_path,[ref])
        self.assertTrue(any('Missing explicit canonical target' in e for e in self.check()['errors']))
        (self.root / self.canonical_path).unlink(); dump(self.ref_path,[])
        self.assertTrue(any('Lost source ID: paper-a' == e for e in self.check()['errors']))

    def test_prior_depth_version_hash_tampering_fail(self):
        for field, value, fragment in [('read_depth','abstract','Altered prior read_depth'),
                                       ('version','arXiv:1234.5678v3','Altered prior version'),
                                       ('record_sha256','0'*64,'Archived hash mismatch')]:
            ref=self.reference(); ref['prior_reading'][field]=value; dump(self.ref_path,[ref])
            self.assertTrue(any(fragment in e for e in self.check()['errors']), (field,self.check()))

    def test_changed_seed_fails(self):
        dump(self.root/'knowledge/seed-sources.jsonl',[{'id':'changed'}])
        self.assertTrue(any(e=='Shared seed changed since snapshot' for e in self.check()['errors']))

    def test_broken_aliases_fail(self):
        # Canonical must be a member; members must resolve and preserve version/depth.
        alias={'work_id':'work-a','canonical':{'file':self.canonical_path,'id':'paper-missing'},
               'members':[{'file':self.canonical_path,'id':'paper-a','version':'wrong','read_depth':'abstract'}],
               'identity_basis':'fixture'}
        dump(self.root/'knowledge/canonical-aliases.jsonl',[alias])
        errors=self.check()['errors']
        self.assertTrue(any('Alias canonical is not a member' in e for e in errors))
        self.assertTrue(any('Alias edition/depth drift' in e for e in errors))

    def test_cross_file_duplicate_is_reported_without_failing_reference_integrity(self):
        # Cross-register duplicates are surfaced as inventory debt, not silently cleared.
        duplicate_path=self.root/'knowledge/sector-conditioning/sources.jsonl'
        dump(duplicate_path,[dict(self.source)])
        alias={'work_id':'work-a','canonical':{'file':self.canonical_path,'id':'paper-a'},
               'members':[{'file':self.canonical_path,'id':'paper-a','version':self.source['version'],
                           'read_depth':self.source['read_depth']}], 'identity_basis':'fixture exact-ID relation'}
        dump(self.root/'knowledge/canonical-aliases.jsonl',[alias])
        result=self.check()
        self.assertTrue(result['reference_integrity_passed'],result['errors'])
        self.assertEqual(set(result['global_duplicate_ids']['paper-a']),
                         {'knowledge/ico-qrf/sources.jsonl','knowledge/sector-conditioning/sources.jsonl'})

    def test_same_file_duplicate_id_fails(self):
        dump(self.root/self.canonical_path,[dict(self.source),dict(self.source)])
        self.assertTrue(any('Duplicate ID within knowledge/ico-qrf/sources.jsonl: paper-a' in e
                            for e in self.check()['errors']))

    def test_deleted_inherited_copy_requires_its_own_reference(self):
        # The ID survives in the canonical ico-qrf record, but the archived frontier
        # copy has lost its lane-specific provenance reference.
        self.ref_path.unlink()
        result=self.check()
        self.assertFalse(result['reference_integrity_passed'])
        self.assertTrue(any(e.startswith('Removed copy lacks preserved reference: knowledge/frontier/sources.jsonl: paper-a')
                            for e in result['errors']), result['errors'])

    def test_recomputed_snapshot_and_ref_hash_are_detected(self):
        # Even if ref fields and record digest are recomputed, the manifest binds the
        # exact archived snapshot bytes.
        forged=dict(self.source); forged['read_depth']='abstract'; forged['version']='forged-version'
        dump(self.rep/'before-records.jsonl',[{'path':self.archive_row['path'],'line':1,'record':forged}])
        ref=self.reference(); ref['prior_reading'].update({'read_depth':forged['read_depth'],
            'version':forged['version'],'record_sha256':digest(forged)})
        dump(self.ref_path,[ref])
        result=self.check()
        self.assertFalse(result['reference_integrity_passed'])
        self.assertIn('Archived snapshot digest mismatch', result['errors'])


class MigrationFixtureTests(unittest.TestCase):
    def test_migrator_keeps_one_target_and_writes_pinned_reference(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); repair=root/'research/redteam/source-repairs'; repair.mkdir(parents=True)
            paths=['knowledge/frontier/sources.jsonl','knowledge/ico-qrf/sources.jsonl','research/theory-map/sources.jsonl']
            canonical={'id':'paper-a','title':'Paper A','read_depth':'full-text','version':'v1','checked_on':'2026-10-19'}
            inherited=dict(canonical); inherited['map_role']='inherited'; inherited['inherited_from']='frontier lane'
            records={paths[0]:[inherited],paths[1]:[canonical],paths[2]:[]}
            snap=[]
            for path, rows in records.items():
                dump(root/path,rows)
                for i,r in enumerate(rows,1): snap.append({'path':path,'line':i,'record':r})
            dump(repair/'before-records.jsonl',snap)
            snapshot_hash=hashlib.sha256((repair/'before-records.jsonl').read_bytes()).hexdigest()
            source_map=[{'id':'paper-a','canonical':{'file':paths[1]}}]
            dump(root/'research/redteam/source-canonicalization/canonical-map.jsonl',source_map)
            seed=root/'knowledge/seed-sources.jsonl'; dump(seed,[{'id':'seed'}])
            manifest={'revision':'rev0','snapshot_sha256':snapshot_hash,'files':{'knowledge/seed-sources.jsonl':hashlib.sha256(seed.read_bytes()).hexdigest()}}
            (repair/'before-manifest.json').write_text(json.dumps(manifest))
            INTEGRATOR.ROOT=root; INTEGRATOR.OUT=repair
            INTEGRATOR.main()
            self.assertEqual([json.loads(s) for s in (root/paths[0]).read_text().splitlines()],[])
            refs=[json.loads(s) for s in (root/'knowledge/frontier/source-refs.jsonl').read_text().splitlines()]
            self.assertEqual(len(refs),1)
            self.assertEqual(refs[0]['canonical_file'],paths[1])
            prior=refs[0]['prior_reading']
            self.assertEqual(prior['read_depth'],'full-text')
            self.assertEqual(prior['version'],'v1')
            self.assertEqual(prior['record_sha256'],digest(inherited))
            alias={'work_id':'work-a','canonical':{'file':paths[1],'id':'paper-a'},
                   'members':[{'file':paths[1],'id':'paper-a','version':'v1','read_depth':'full-text'}],
                   'identity_basis':'fixture exact-ID relation'}
            dump(root/'knowledge/canonical-aliases.jsonl',[alias])
            result=CHECKER.check(root)
            self.assertTrue(result['reference_integrity_passed'], result['errors'])


class LiveCorpusReportingTest(unittest.TestCase):
    def test_live_alias_provenance_integrity(self):
        result=CHECKER.check(ROOT)
        self.assertTrue(result['reference_integrity_passed'],result['errors'])
        aliases=[json.loads(x) for x in (ROOT/'knowledge/canonical-aliases.jsonl').read_text().splitlines()]
        work_ids={a['work_id'] for a in aliases}
        self.assertIn('brading-presentism-2013',work_ids)
        self.assertIn('putnam-time-geometry-1967',work_ids)
        self.assertEqual(result['alias_groups'],len(aliases))
        records={}
        for folder in ('knowledge','research'):
            for path in (ROOT/folder).rglob('*sources.jsonl'):
                rel=str(path.relative_to(ROOT))
                for line in path.read_text().splitlines():
                    row=json.loads(line); records[(rel,row['id'])]=row
        for group in aliases:
            for member in group['members']:
                row=records[(member['file'],member['id'])]
                self.assertEqual(member['read_depth'],row['read_depth'])
                self.assertEqual(member['version'],row.get('version'))
        brading=next(a for a in aliases if a['work_id']=='brading-presentism-2013')
        seed_member=next(m for m in brading['members'] if m['id']=='seed-brading-presentism')
        self.assertEqual(seed_member['read_depth'],'abstract')
        self.assertIsNone(seed_member['version'])
        mctaggart=next(a for a in aliases if a['work_id']=='mctaggart-unreality-1908')
        primary=next(m for m in mctaggart['members'] if m['id']=='phil-mctaggart')
        self.assertEqual(primary['read_depth'],'discovery')
        mctaggart_record=records[(primary['file'],primary['id'])]
        self.assertEqual(mctaggart_record['read_depth'],'discovery')
        self.assertEqual(mctaggart['additional_readings'][0]['read_depth'],'full-text')

    def test_every_removed_live_archived_copy_has_exact_reference(self):
        old=[json.loads(x) for x in (ROOT/'research/redteam/source-repairs/before-records.jsonl').read_text().splitlines()]
        for lane in ('knowledge/frontier/sources.jsonl','research/theory-map/sources.jsonl'):
            live={json.loads(x)['id'] for x in (ROOT/lane).read_text().splitlines() if x.strip()}
            ref_path=ROOT/lane.replace('sources.jsonl','source-refs.jsonl')
            refs=[json.loads(x) for x in ref_path.read_text().splitlines() if x.strip()]
            keys={(r['prior_reading']['path'],r['prior_reading']['line'],r['id'],r['prior_reading']['record_sha256']) for r in refs}
            removed=[x for x in old if x['path']==lane and x['record']['id'] not in live]
            self.assertEqual(len(removed), 4 if lane.startswith('knowledge/frontier') else 59)
            for item in removed:
                self.assertIn((lane,item['line'],item['record']['id'],digest(item['record'])),keys)
        manifest=json.loads((ROOT/'research/redteam/source-repairs/before-manifest.json').read_text())
        seed_hash=hashlib.sha256((ROOT/'knowledge/seed-sources.jsonl').read_bytes()).hexdigest()
        self.assertEqual(seed_hash,manifest['files']['knowledge/seed-sources.jsonl'])
        snapshot_hash=hashlib.sha256((ROOT/'research/redteam/source-repairs/before-records.jsonl').read_bytes()).hexdigest()
        self.assertEqual(snapshot_hash,manifest['snapshot_sha256'])


if __name__=='__main__':
    unittest.main()
