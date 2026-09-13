#!/usr/bin/env python3
import glob,json,pathlib,sys
rows=[]; bad=[]
for f in sorted(glob.glob('lanes/**/iter065a_*.json',recursive=True)):
    try: rows.append(json.loads(pathlib.Path(f).read_text()))
    except Exception as e: bad.append({'file':f,'error':str(e)})
expected={'source_prescription','extension_selection','order_regulator','eprl_distributional_control'}
seen={r.get('lane') for r in rows}
if bad or len(rows)!=4 or seen!=expected or any(r.get('classification')=='ITER065A_IMPLEMENTATION_INVALID' for r in rows):
    cls='ITER065A_IMPLEMENTATION_INVALID'
elif any(r.get('classification')=='ITER065A_K5_SCIENTIFIC_FAIL_SOURCE_INCOMPATIBLE_EXTENSION' for r in rows):
    cls='ITER065A_K5_SCIENTIFIC_FAIL_SOURCE_INCOMPATIBLE_EXTENSION'
elif all(r.get('valid') for r in rows):
    cls='ITER065A_K5_DISTRIBUTIONAL_EXTENSION_QUALIFIED'
else:
    cls='ITER065A_K5_BLOCKED_CORRELATED_EXTENSION_OBJECT_MISSING'
out={'iteration':'Iter065A','classification':cls,'valid_lanes':sum(bool(r.get('valid')) for r in rows),'total_lanes':len(rows),'lanes':rows,'invalid':bad,'prereg_commit':'987b0b27aaccc9e75ceed5fe209e9944a17f5e94','interpretation':'K5 distributional qualification only; BLOCKED is not a divergence/nonexistence theorem; no F9/G3/G8/new-physics promotion'}
pathlib.Path('iter065a_aggregate.json').write_text(json.dumps(out,indent=2,sort_keys=True),encoding='utf-8'); print(json.dumps({k:v for k,v in out.items() if k!='lanes'},indent=2,sort_keys=True))
if cls=='ITER065A_IMPLEMENTATION_INVALID': sys.exit(4)
