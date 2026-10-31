"""Local candidate archive/packet helper; never judges science or launches LLMs."""
import argparse
import hashlib
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
QUESTION = HERE/'pilot'/'QUESTION.md'
ARCHIVE = HERE/'candidates.jsonl'
GATES = {'mathematical','source','physical','philosophical'}
VERDICTS = {'pass','fail','conditional','unknown'}


def question_hash():
    return hashlib.sha256(QUESTION.read_bytes()).hexdigest()


def read_archive():
    entries = [json.loads(line) for line in ARCHIVE.read_text().splitlines() if line.strip()]
    by_id = {entry['id']:entry for entry in entries}
    if len(entries) != len(by_id):
        raise ValueError('Candidate IDs must be unique; retain revisions as children.')
    for entry in entries:
        required = {'id','origin','registration','parents','move','mechanism','claim',
                    'assumptions','question_sha256','checks','gates','disposition','evidence'}
        if required-entry.keys():
            raise ValueError(f"Missing fields on {entry['id']}: {sorted(required-entry.keys())}")
        if entry['question_sha256'] != question_hash():
            raise ValueError(f"Question file changed for {entry['id']}; inspect question drift.")
        if set(entry['gates']) != GATES:
            raise ValueError('Keep four distinct gates; do not replace them by a score.')
        for gate,record in entry['gates'].items():
            if record.get('verdict') not in VERDICTS or not record.get('reason'):
                raise ValueError(f"Invalid {gate} gate on {entry['id']}")
        for check in entry['checks']:
            if not check.get('name') or check.get('verdict') not in VERDICTS or not check.get('evidence'):
                raise ValueError(f"Unnamed or unsupported check on {entry['id']}")
        for name in entry['evidence']:
            path = (HERE/name.split('#',1)[0]).resolve()
            if not path.is_relative_to(HERE) or not path.is_file():
                raise ValueError(f'Invalid local evidence path: {name}')
        if any(parent not in by_id for parent in entry['parents']):
            raise ValueError(f"Unknown parent on {entry['id']}")
    seen,active = set(),set()
    def visit(cid):
        if cid in active:
            raise ValueError('Candidate ancestry is cyclic.')
        if cid in seen:
            return
        active.add(cid)
        for parent in by_id[cid]['parents']:
            visit(parent)
        active.remove(cid)
        seen.add(cid)
    for cid in by_id:
        visit(cid)
    return entries,by_id


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command',required=True)
    sub.add_parser('validate')
    sub.add_parser('check')
    packet = sub.add_parser('packet')
    packet.add_argument('id')
    packet.add_argument('--role',choices=['reviewer','proposer'],default='reviewer')
    args = parser.parse_args()
    if args.command == 'check':
        # Fixed owned checker only. Archive text is never executed as a command.
        completed = subprocess.run([sys.executable,str(HERE/'pilot'/'check_access.py'),'--json'])
        raise SystemExit(completed.returncode)
    entries,by_id = read_archive()
    if args.command == 'validate':
        print(json.dumps({'candidates':len(entries),'question_sha256':question_hash(),
                          'dispositions':dict(Counter(e['disposition'] for e in entries)),
                          'note':'Structure checked; no proof, physical or novelty verdict inferred.'},indent=2))
        return
    if args.id not in by_id:
        parser.error('Unknown candidate ID.')
    entry = by_id[args.id]
    print(QUESTION.read_text())
    if args.role == 'reviewer':
        fields = ('id','claim','assumptions','evidence')
        print(json.dumps({field:entry[field] for field in fields},indent=2))
        print('Review mathematical/source/physical/philosophical claims separately. '
              'No proposer confidence, gate verdicts or preferred winner supplied.')
    else:
        print(json.dumps(entry,indent=2))
        print('Make one child changing a named mechanism or assumption; preserve the failed test. '
              'A different question needs its own contract. Do not silently promote a gate.')


if __name__ == '__main__':
    try:
        main()
    except (ValueError,KeyError,json.JSONDecodeError) as error:
        raise SystemExit(str(error))
