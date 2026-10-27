"""Offline inventory and arithmetic checks. No network or external dependencies."""
from pathlib import Path, PurePosixPath
import argparse, collections, csv, hashlib, json, re, sys
ROOT=Path(__file__).resolve().parent
UUID=re.compile(r'^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$')
SHA=re.compile(r'^[0-9a-f]{64}$')
def require(ok,message):
 if not ok:raise ValueError(message)
def load(path):
 require(path.stat().st_size<=2_000_000,'Input exceeds cap')
 return json.loads(path.read_text(encoding='utf-8'))
def is_2xx(value):
 if isinstance(value,bool):return False
 if isinstance(value,int):return 200<=value<=299
 return isinstance(value,str) and bool(re.fullmatch(r'2[0-9]{2}',value))
def status_key(value):
 if value is None or value=='':return 'Missing'
 require(type(value) is int or isinstance(value,str),'Invalid HTTP status type')
 require(re.fullmatch(r'[1-5][0-9]{2}',str(value)) is not None,'Invalid HTTP status value')
 return str(value)
def selection_summary(selection,captures):
 require(isinstance(selection,list) and len(selection)<=1000,'Bad selection list')
 require(all(set(r)=={'report_id','acquisition_status'} for r in selection),'Invalid selection columns')
 require(all(UUID.fullmatch(r['report_id']) for r in selection),'Invalid selection ID')
 require(len({r['report_id'] for r in selection})==len(selection),'Duplicate selection ID')
 require(all(r['acquisition_status'] in {'acquired','not_acquired'} for r in selection),'Invalid acquisition status')
 held={r['report_id'] for r in selection if r['acquisition_status']=='acquired'}
 require(held=={r['report_id'] for r in captures},'Selection and acquired capture IDs disagree')
 absent=sorted(r['report_id'] for r in selection if r['acquisition_status']=='not_acquired')
 return {'selected':len(selection),'acquired':len(held),'not_acquired':len(absent),'not_acquired_report_ids':absent}
def headline_tables(captures,events,rows,selection):
 coverage=selection_summary(selection,captures)
 programs=collections.Counter(r['program_sha256'] for r in captures)
 statuses=collections.Counter(status_key(e['status']) for e in events if e['method']=='POST')
 years=collections.Counter(r['date'][:4] for r in rows)
 return {'selection':{k:coverage[k] for k in ('selected','acquired','not_acquired')},
  'programs':{'captures':len(captures),'exact_programs':len(programs),'duplicate_groups':sum(n>1 for n in programs.values()),'reports_in_duplicate_groups':sum(n for n in programs.values() if n>1),'singleton_programs':sum(n==1 for n in programs.values()),'repeated_captures':sum(n-1 for n in programs.values())},
  'post_statuses':dict(sorted(statuses.items())),'catalog_years':dict(sorted(years.items()))}
def markdown_tables(tables):
 titles={'selection':'Selection coverage (section 3)','programs':'Exact-program grouping (section 5.4)','post_statuses':'Recorded POST statuses (section 5.2)','catalog_years':'Catalog provenance queue (section 5.3)'}
 parts=[]
 for key,rows in tables.items():
  parts.extend(['## '+titles[key],'','| Item | Count |','|---|---:|'])
  parts.extend('| '+str(k)+' | '+str(v)+' |' for k,v in rows.items())
  if key in {'post_statuses','catalog_years'}:parts.append('| Total | '+str(sum(rows.values()))+' |')
  parts.append('')
 return '\n'.join(parts)
def summarize(captures,events,rows):
 require(isinstance(captures,list) and len(captures)<=1000,'Bad capture list')
 require(isinstance(events,list) and len(events)<=10000,'Bad event list')
 require(isinstance(rows,list) and len(rows)<=50000,'Bad catalog list')
 ids={r['report_id'] for r in captures}
 require(len(ids)==len(captures),'Duplicate report IDs')
 require(all(UUID.fullmatch(r['report_id']) and SHA.fullmatch(r['program_sha256']) and SHA.fullmatch(r['file_sha256']) for r in captures),'Invalid identifiers')
 require(len({e['event_id'] for e in events})==len(events),'Duplicate event IDs')
 require(all(e['report_id'] in ids for e in events),'Orphan event')
 require(len({r['report_id'] for r in rows})==len(rows),'Duplicate catalog IDs')
 posts=[e for e in events if e['method']=='POST']
 for e in posts:status_key(e['status'])
 success=[e for e in posts if is_2xx(e['status'])]
 programs={r['report_id']:r['program_sha256'] for r in captures}
 groups=collections.Counter(programs.values())
 return {'captures':len(captures),'programs':len(groups),'duplicate_groups':sum(n>1 for n in groups.values()),'repeated_captures':sum(n-1 for n in groups.values()),'post_events':len(posts),'post_reports':len({e['report_id'] for e in posts}),'post_2xx':len(success),'post_2xx_reports':len({e['report_id'] for e in success}),'post_2xx_programs':len({programs[e['report_id']] for e in success}),'post_missing_status':sum(e['status'] in ('',None) for e in posts),'review_rows':len(rows),'review_years':dict(sorted(collections.Counter(r['date'][:4] for r in rows).items()))}
def verify_inventory(root):
 manifest=load(root/'MANIFEST.json')
 require(isinstance(manifest,dict) and len(manifest)<100,'Bad manifest')
 actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts}
 # Bytecode caches generated by Python are not release members; all other extras fail.
 require(actual==set(manifest)|{'MANIFEST.json'},'Unexpected or missing package member')
 for name,expected in manifest.items():
  part=PurePosixPath(name)
  require(not part.is_absolute() and '..' not in part.parts and '\\' not in name and ':' not in name,'Unsafe member name')
  path=root.joinpath(*part.parts)
  require(path.resolve().is_relative_to(root.resolve()) and not path.is_symlink(),'Unsafe member path')
  require(path.stat().st_size<=10_000_000,'Member exceeds cap')
  require(SHA.fullmatch(expected) is not None,'Invalid digest')
  require(hashlib.sha256(path.read_bytes()).hexdigest()==expected,'Hash mismatch: '+name)
 return len(manifest)
def main():
 parser=argparse.ArgumentParser(description=__doc__)
 mode=parser.add_mutually_exclusive_group()
 mode.add_argument('--tables',action='store_true',help='Print the four derived headline tables as Markdown')
 mode.add_argument('--missing',action='store_true',help='Print the exact not-acquired report IDs as JSON')
 args=parser.parse_args()
 members=verify_inventory(ROOT)
 with (ROOT/'data/catalog-review.csv').open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f))
 with (ROOT/'data/capture-selection.csv').open(encoding='utf-8',newline='') as f:selection=list(csv.DictReader(f))
 captures=load(ROOT/'data/captures.json');events=load(ROOT/'data/post-events.json')
 result=summarize(captures,events,rows)
 expected={'captures':71,'programs':42,'duplicate_groups':8,'repeated_captures':29,'post_events':56,'post_reports':48,'post_2xx':13,'post_2xx_reports':13,'post_2xx_programs':8,'post_missing_status':22,'review_rows':432,'review_years':{'2023':113,'2024':56,'2025':111,'2026':152}}
 require(result==expected,'Claim aggregate mismatch')
 coverage=selection_summary(selection,captures)
 require((coverage['selected'],coverage['acquired'],coverage['not_acquired'])==(116,71,45),'Selection count mismatch')
 tables=headline_tables(captures,events,rows,selection)
 if args.tables:print(markdown_tables(tables))
 elif args.missing:print(json.dumps(coverage['not_acquired_report_ids'],indent=2))
 else:print(json.dumps({'verified_members':members,'results':result,'selection':coverage,'tables':tables,'scope':'Released-metadata integrity and arithmetic only; raw extraction and independent historical validation are not performed.'},indent=2))
if __name__=='__main__':main()
