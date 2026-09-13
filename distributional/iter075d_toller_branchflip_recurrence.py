import argparse, json
from pathlib import Path
import mpmath as mp

mp.mp.dps = 100
RHO = [mp.mpf('0.23'), mp.mpf('0.91'), mp.mpf('1.77')]
RT = [mp.mpf(x) for x in ['-3.1','-1.37','-0.41','0.28','1.64','3.05']]
EPS = [mp.mpf('1e-2'), mp.mpf('3e-4'), mp.mpf('1e-6')]
BRANCH = [1,-1]
PASS_TOL = mp.mpf('1e-40')
NEG_FLOOR = mp.mpf('1e-10')


def coeff(s,j,l,rho,rt,eps):
    pole = mp.mpf(s)/(rt-rho-mp.mpc(0,s)*eps)
    gr = mp.gamma(-j-mp.j*rho)*mp.gamma(l-mp.j*rt+1)/(mp.gamma(-j-mp.j*rt)*mp.gamma(l-mp.j*rho+1))
    return pole*gr


def rel(a,b):
    return abs(a-b)/max(abs(a),abs(b))

p=argparse.ArgumentParser()
p.add_argument('--j', required=True)
p.add_argument('--l', required=True)
p.add_argument('--tag', required=True)
a=p.parse_args()
j=mp.mpf(a.j); l=mp.mpf(a.l)
records=[]; valid=True; flip_ok=True; same_fail=0; total=0; max_flip=mp.mpf('0')
for rho in RHO:
  for rt in RT:
    for eps in EPS:
      for s in BRANCH:
        total += 1
        try:
          x=coeff(s,j,l,rho,rt,eps)
          y=mp.conj(coeff(-s,l,j,rho,rt,eps))
          z=mp.conj(coeff(s,l,j,rho,rt,eps))
          finite=all(mp.isfinite(q.real) and mp.isfinite(q.imag) and abs(q)>0 for q in [x,y,z])
          rf=rel(x,-y) if finite else mp.inf
          rs=rel(x,-z) if finite else mp.inf
          ratio=x/y if finite else mp.nan
          rok=finite and rf<=PASS_TOL and abs(ratio+1)<=PASS_TOL
          nfail=finite and rs>=NEG_FLOOR
        except Exception as e:
          finite=False; rf=mp.inf; rs=mp.inf; ratio=mp.nan; rok=False; nfail=False
        valid = valid and finite
        flip_ok = flip_ok and rok
        same_fail += int(nfail)
        max_flip=max(max_flip,rf)
        records.append({'rho':str(rho),'rtilde':str(rt),'epsilon':str(eps),'branch':s,'finite':finite,'flip_residual':mp.nstr(rf,40),'same_branch_residual':mp.nstr(rs,40),'ratio_to_conjugate_flip':mp.nstr(ratio,40)})
neg_fraction=mp.mpf(same_fail)/total
neg_ok=neg_fraction>=mp.mpf('0.9')
if not valid:
  cls='ITER075D_BRANCH_FLIP_KERNEL_RECURRENCE_INVALID_NUMERICAL'
elif flip_ok and neg_ok:
  cls='ITER075D_BRANCH_FLIP_KERNEL_RECURRENCE_CERTIFICATE_SUPPORTED_SCOPED'
else:
  cls='ITER075D_BRANCH_FLIP_KERNEL_RECURRENCE_CERTIFICATE_OBSTRUCTED_SCOPED'
out={'iteration':'Iter075D','tag':a.tag,'j':str(j),'l':str(l),'classification':cls,'valid':valid,'records':records,'record_count':total,'branchflip_all_pass':flip_ok,'max_branchflip_residual':mp.nstr(max_flip,40),'same_branch_negative_fraction':mp.nstr(neg_fraction,30),'same_branch_negative_control_pass':neg_ok,'pass_tolerance':str(PASS_TOL),'negative_floor':str(NEG_FLOOR),'claim_lock':'Kernel-level only; no full Toller group inversion law, no K5/G3/F9/G8 promotion, no physical sector selection or finiteness/new-physics claim.'}
Path('out').mkdir(exist_ok=True)
fn=f'out/iter075d-{a.tag}.json'
Path(fn).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2,sort_keys=True))
if cls.endswith('INVALID_NUMERICAL'):
  raise SystemExit(2)
