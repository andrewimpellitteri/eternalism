"""Independent temporary-fixture tests for the generalized dual-archive checker.

Run from repository root:
  python3 -m unittest discover -s research/redteam/new-lane-canonicalization/review -v
No live source registers are modified.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[4]
SCRIPT=ROOT/'research/redteam/new-lane-canonicalization/check_references.py'
spec=importlib.util.spec_from_file_location('dual_archive_checker',SCRIPT)
CHECKER=importlib.util.module_from_spec(spec); spec.loader.exec_module(CHECKER)
ARCHIVES=CHECKER.ARCHIVES

def dump(path,rows):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows))

def sha(data): return hashlib.sha256(data).hexdigest()
def record_hash(r): return hashlib.sha256(json.dumps(r,sort_keys=True,ensure_ascii=False).encode()).hexdigest()

class DualArchiveFixture(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.root=Path(self.tmp.name)
        self.seed={'id':'seed-clock','read_depth':'abstract','version':None,'checked_on':'2026-10-19'}
        self.seed_path=self.root/'knowledge/seed-sources.jsonl'; dump(self.seed_path,[self.seed])
        self.seed_hash=sha(self.seed_path.read_bytes())
        self.canonical_path='knowledge/canonical/sources.jsonl'
        self.canonical={'id':'paper-x','title':'Paper X','read_depth':'full-text','version':'arXiv:1234.5678v3','checked_on':'2026-10-20'}
        dump(self.root/self.canonical_path,[self.canonical])
        self.old_path='knowledge/frontier/sources.jsonl'
        self.new_path='knowledge/sector-conditioning/sources.jsonl'
        self.old_record={'id':'paper-x','read_depth':'abstract','version':'arXiv:1234.5678v1','checked_on':'2026-10-19','inherited_from':'frontier reader'}
        self.new_record={'id':'paper-x','read_depth':'full-text','version':'arXiv:1234.5678v2','checked_on':'2026-10-20','inherited_from':'sector reader'}
        self.archive1=[{'path':self.old_path,'line':1,'record':dict(self.old_record)}]
        self.archive2=[{'path':self.old_path,'line':1,'record':dict(self.old_record)},
                       {'path':self.new_path,'line':1,'record':dict(self.new_record)}]
        self.write_archive(0,self.archive1,'rev-a')
        self.write_archive(1,self.archive2,'rev-b')
        self.write_refs()
        alias={'work_id':'paper-x','canonical':{'file':self.canonical_path,'id':'paper-x'},
               'members':[{'file':self.canonical_path,'id':'paper-x','version':self.canonical['version'],'read_depth':'full-text'},
                          {'file':'knowledge/seed-sources.jsonl','id':'seed-clock','version':None,'read_depth':'abstract'}],
               'identity_basis':{'identifier':'doi:fixture','method':'exact identifier'}}
        dump(self.root/'knowledge/canonical-aliases.jsonl',[alias])

    def tearDown(self): self.tmp.cleanup()

    def write_archive(self,index,rows,revision):
        archive=self.root/ARCHIVES[index]
        dump(archive,rows)
        manifest={'revision':revision,'records':len(rows),'snapshot_sha256':sha(archive.read_bytes()),
                  'files':{'knowledge/seed-sources.jsonl':self.seed_hash}}
        (archive.parent/'before-manifest.json').write_text(json.dumps(manifest))

    def ref(self,path,line,record,snapshot,index,revision):
        return {'id':record['id'],'canonical_file':self.canonical_path,'relation':'inherited-source',
                'decision':'fixture reviewed source correspondence',
                'prior_reading':{'snapshot':snapshot,'revision':revision,'path':path,'line':line,
                    'record_sha256':record_hash(record),'read_depth':record['read_depth'],
                    'version':record.get('version'),'checked_on':record['checked_on'],
                    'reader':record.get('inherited_from')},
                'limits':'Does not upgrade the archived reading.'}

    def write_refs(self):
        dump(self.root/'knowledge/frontier/source-refs.jsonl',[
            self.ref(self.old_path,1,self.old_record,ARCHIVES[0],0,'rev-a')])
        dump(self.root/'knowledge/sector-conditioning/source-refs.jsonl',[
            self.ref(self.new_path,1,self.new_record,ARCHIVES[1],1,'rev-b')])

    def check(self): return CHECKER.check(self.root)

    def test_both_archives_and_repeated_identical_copy_pass(self):
        result=self.check()
        self.assertTrue(result['reference_integrity_passed'],result['errors'])
        self.assertEqual(result['references'],2)
        # A single ref to archive A also covers the identical path/id/payload in archive B.
        self.assertEqual(len(result['archives']),2)

    def test_removed_copy_in_second_snapshot_requires_reference_even_if_id_survives(self):
        dump(self.root/'knowledge/sector-conditioning/source-refs.jsonl',[])
        result=self.check()
        self.assertFalse(result['reference_integrity_passed'])
        self.assertTrue(any('Removed copy lacks preserved reference' in e and ARCHIVES[1] in e
                            and self.new_path in e for e in result['errors']),result['errors'])

    def test_wrong_direct_target_fails(self):
        refs=[json.loads(x) for x in (self.root/'knowledge/frontier/source-refs.jsonl').read_text().splitlines()]
        refs[0]['canonical_file']='knowledge/missing/sources.jsonl'
        dump(self.root/'knowledge/frontier/source-refs.jsonl',refs)
        self.assertTrue(any('Missing explicit canonical target' in e for e in self.check()['errors']))

    def test_current_global_duplicate_fails_and_reports_paths(self):
        dup=dict(self.canonical); dup['title']='A copied payload'
        dump(self.root/'knowledge/other-lane/sources.jsonl',[dup])
        result=self.check()
        self.assertFalse(result['reference_integrity_passed'])
        self.assertIn('Global duplicate ID: paper-x',result['errors'])
        self.assertEqual(set(result['global_duplicate_ids']['paper-x']),
                         {'knowledge/canonical/sources.jsonl','knowledge/other-lane/sources.jsonl'})

    def test_archive_digest_and_seed_hash_are_enforced(self):
        archive=self.root/ARCHIVES[1]
        archive.write_text(archive.read_text()+'\n')
        self.assertTrue(any('Archived snapshot digest mismatch: '+ARCHIVES[1] in e for e in self.check()['errors']))
        # Restore a valid snapshot before testing the shared seed pin.
        self.write_archive(1,self.archive2,'rev-b')
        dump(self.seed_path,[{'id':'mutated-seed'}])
        errors=self.check()['errors']
        self.assertTrue(any('Shared seed changed since snapshot: '+name in errors for name in ARCHIVES))

    def test_prior_depth_version_date_hash_revision_and_lane_are_bound(self):
        mutations=[('read_depth','discovery','Altered prior read_depth'),
                   ('version','wrong-version','Altered prior version'),
                   ('checked_on','1999-01-01','Altered prior checked_on'),
                   ('record_sha256','0'*64,'Archived hash mismatch')]
        for field,value,expected in mutations:
            self.write_refs()
            refs=[json.loads(x) for x in (self.root/'knowledge/frontier/source-refs.jsonl').read_text().splitlines()]
            refs[0]['prior_reading'][field]=value
            dump(self.root/'knowledge/frontier/source-refs.jsonl',refs)
            self.assertTrue(any(expected in e for e in self.check()['errors']),(field,self.check()['errors']))
        self.write_refs()
        refs=[json.loads(x) for x in (self.root/'knowledge/frontier/source-refs.jsonl').read_text().splitlines()]
        refs[0]['prior_reading']['revision']='wrong-rev'; dump(self.root/'knowledge/frontier/source-refs.jsonl',refs)
        self.assertTrue(any('Unpinned prior snapshot' in e for e in self.check()['errors']))
        self.write_refs()
        refs=[json.loads(x) for x in (self.root/'knowledge/frontier/source-refs.jsonl').read_text().splitlines()]
        refs[0]['prior_reading']['path']=self.new_path; dump(self.root/'knowledge/frontier/source-refs.jsonl',refs)
        self.assertTrue(any('Prior reading belongs to another lane' in e for e in self.check()['errors']))

    def test_missing_alias_registry_and_alias_metadata_drift_fail(self):
        aliases=self.root/'knowledge/canonical-aliases.jsonl'; aliases.unlink()
        self.assertIn('Missing curated alias registry',self.check()['errors'])
        alias={'work_id':'paper-x','canonical':{'file':self.canonical_path,'id':'paper-x'},
               'members':[{'file':self.canonical_path,'id':'paper-x','version':'wrong','read_depth':'abstract'}],
               'identity_basis':'fixture'}
        dump(aliases,[alias]); errors=self.check()['errors']
        self.assertTrue(any('Alias edition/depth drift: paper-x' in e for e in errors),errors)

    def test_alias_does_not_upgrade_shallow_seed_member(self):
        result=self.check(); self.assertTrue(result['reference_integrity_passed'],result['errors'])
        group=json.loads((self.root/'knowledge/canonical-aliases.jsonl').read_text().splitlines()[0])
        seed=next(m for m in group['members'] if m['id']=='seed-clock')
        self.assertEqual(seed['read_depth'],'abstract'); self.assertIsNone(seed['version'])

if __name__=='__main__': unittest.main()
