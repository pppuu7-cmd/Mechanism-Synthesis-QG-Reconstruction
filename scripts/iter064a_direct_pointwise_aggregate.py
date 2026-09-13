#!/usr/bin/env python3
import glob,json,pathlib,sys

files=sorted(glob.glob('lanes/**/iter064a_*.json',recursive=True))
rows=[]
invalid=[]
for f in files:
    try:
        r=json.loads(pathlib.Path(f).read_text())
        rows.append(r)
    except Exception as e:
        invalid.append({'file':f,'error':str(e)})
expected={(g,s) for g in ('0.4','1.2') for s in (1701,1702,1703)}
seen={(str(r.get('gamma')),int(r.get('seed',-1))) for r in rows}
checks=[]
for r in rows:
    try:
        checks.append({
          'gamma':str(r['gamma']),'seed':int(r['seed']),
          'kak_ok':float(r['max_kak_reconstruction_error']) < 1e-10,
          'additive_ok':float(r['max_edge_additive_relative_error']) < 1e-35,
          'eprl_ok':float(r['unconstrained_vs_eprl_relative_error']) < 1e-35,
          'global_flip_ok':float(r['global_flip_duplication_error']) < 1e-60,
          'min_beta_ok':float(r['min_pair_beta']) >= 0.12,
          'carrier_verdict':r.get('verdict')
        })
    except Exception as e:
        invalid.append({'row':r,'error':str(e)})
structural=(not invalid and len(rows)==6 and seen==expected and len(checks)==6)
scientific=structural and all(c['kak_ok'] and c['additive_ok'] and c['eprl_ok'] and c['global_flip_ok'] and c['min_beta_ok'] and c['carrier_verdict']=='DIRECT_CAUSAL_INTEGRAND_SMOKE_PASS' for c in checks)
if not structural:
    cls='ITER064A_IMPLEMENTATION_OR_NUMERICAL_INVALID'
elif scientific:
    cls='ITER064A_DIRECT_CAUSAL_POINTWISE_EPRL_CONTROL_PASS'
else:
    cls='ITER064A_DIRECT_CAUSAL_POINTWISE_CONTROL_FAIL'
out={'iteration':'Iter064A','classification':cls,'valid_lanes':sum(all(c[k] for k in ('kak_ok','additive_ok','eprl_ok','global_flip_ok','min_beta_ok')) and c['carrier_verdict']=='DIRECT_CAUSAL_INTEGRAND_SMOKE_PASS' for c in checks),'total_lanes':len(rows),'expected_lanes':6,'checks':checks,'invalid':invalid,'prereg_commit':'3f3c8fa03ab5d35e2a70784924502eb653894bf5','source_snapshot_commit':'7df82d28dd6426aa7aaac353a1e0abf795e6fdee','scope':'pointwise direct ten-wedge carrier only; no Haar integration/intertwiner contraction/finiteness/K5/F9/G3/G8/new-physics claim'}
pathlib.Path('iter064a_aggregate.json').write_text(json.dumps(out,indent=2,sort_keys=True),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='checks'},indent=2,sort_keys=True))
if cls=='ITER064A_IMPLEMENTATION_OR_NUMERICAL_INVALID': sys.exit(4)
