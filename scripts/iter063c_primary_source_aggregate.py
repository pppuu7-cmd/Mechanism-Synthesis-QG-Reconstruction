#!/usr/bin/env python3
import glob,json,pathlib,sys
files=sorted(glob.glob('lanes/**/iter063c_*.json',recursive=True))
rows=[]
for f in files:
    try: rows.append(json.loads(pathlib.Path(f).read_text()))
    except Exception as e: rows.append({'lane':f,'valid':False,'classification':'ITER063C_IMPLEMENTATION_INVALID','error':str(e)})
expected={'vertex_object','eprl_control','causal_conventions','representation_guard'}
seen={r.get('lane') for r in rows}
if len(rows)!=4 or seen!=expected or any(r.get('classification')=='ITER063C_IMPLEMENTATION_INVALID' for r in rows):
    cls='ITER063C_IMPLEMENTATION_INVALID'
elif not all(r.get('valid') for r in rows):
    # Dedicated conflation classifier if the EPRL-control lane is the blocker.
    er=next((r for r in rows if r.get('lane')=='eprl_control'),None)
    cls='ITER063C_FAIL_EPRL_CONTROL_CONFLATED_WITH_CAUSAL_SUM' if er and not er.get('valid') else 'ITER063C_BLOCKED_SOURCE_OBJECT_INCOMPLETE'
else:
    cls='ITER063C_PRIMARY_SOURCE_VERTEX_CONTROL_PINNED'
out={'iteration':'Iter063C','classification':cls,'valid_lanes':sum(bool(r.get('valid')) for r in rows),'total_lanes':len(rows),'lanes':rows,'prereg_commit':'66ce9c87bcdf5b08e4c1e5604568766847321d98','source_snapshot_commit':'7df82d28dd6426aa7aaac353a1e0abf795e6fdee','interpretation':'source qualification only; PASS authorizes later direct Eq4 gate but does not establish amplitude finiteness, K5/F9/G3/G8, or new physics'}
pathlib.Path('iter063c_aggregate.json').write_text(json.dumps(out,indent=2,sort_keys=True),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='lanes'},indent=2,sort_keys=True))
if cls=='ITER063C_IMPLEMENTATION_INVALID': sys.exit(4)
