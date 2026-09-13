#!/usr/bin/env python3
import glob,json,pathlib,sys
rows=[]; invalid=[]
for f in sorted(glob.glob('lanes/**/iter064b_*.json',recursive=True)):
    try: rows.append(json.loads(pathlib.Path(f).read_text()))
    except Exception as e: invalid.append({'file':f,'error':str(e)})
expected={'source_order','basis_permutation','eprl_control','scope_lock'}
seen={r.get('lane') for r in rows}
structural=(not invalid and len(rows)==4 and seen==expected and all(r.get('classification')!='ITER064B_IMPLEMENTATION_INVALID' for r in rows))
if not structural: cls='ITER064B_IMPLEMENTATION_INVALID'
elif all(r.get('valid') for r in rows): cls='ITER064B_K4_SOURCE_PREREQUISITES_CLOSED_FOR_K5_QUALIFICATION'
else: cls='ITER064B_K5_REMAINS_BLOCKED_PREREQUISITE_GAP'
out={'iteration':'Iter064B','classification':cls,'valid_lanes':sum(bool(r.get('valid')) for r in rows),'total_lanes':len(rows),'lanes':rows,'invalid':invalid,'prereg_commit':'90e835e5c77290f768c6db2984441f8d30334882','interpretation':'qualification only; PASS permits a later prospectively preregistered K5 distributional-extension gate but does not pass K5 or establish finiteness/new physics'}
pathlib.Path('iter064b_aggregate.json').write_text(json.dumps(out,indent=2,sort_keys=True),encoding='utf-8'); print(json.dumps({k:v for k,v in out.items() if k!='lanes'},indent=2,sort_keys=True))
if cls=='ITER064B_IMPLEMENTATION_INVALID': sys.exit(4)
