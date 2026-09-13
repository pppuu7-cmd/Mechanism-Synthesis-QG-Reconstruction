#!/usr/bin/env python3
import json
import sympy as sp

x, rho, eps = sp.symbols('x rho eps', real=True)
I = sp.I


def P(dj, dl):
    if (dj + dl) % 2:
        raise ValueError('inadmissible parity: j+l must be integer')
    j = sp.Rational(dj, 2)
    l = sp.Rational(dl, 2)
    N = int(j + l)
    out = sp.Integer(1)
    for n in range(N + 1):
        q = sp.Rational(n) - j
        out *= (I*x - q) / (I*rho - q)
    return sp.cancel(out)


def real_conj(z):
    return sp.cancel(sp.conjugate(z).xreplace({sp.conjugate(x): x, sp.conjugate(rho): rho, sp.conjugate(eps): eps}))


def exact_zero(z):
    num, _ = sp.fraction(sp.cancel(sp.together(z)))
    return sp.expand(num) == 0

rows=[]
all_poly=True
all_kernel=True
all_set=True
wrong_same_fail=False
for dj in range(17):
  for dl in range(17):
    if (dj+dl)%2:
      continue
    j=sp.Rational(dj,2); l=sp.Rational(dl,2); N=int(j+l)
    set_j=[sp.Rational(n)-j for n in range(N+1)]
    set_l=[sp.Rational(n)-l for n in range(N+1)]
    set_ok=sorted(set_j)==sorted([-q for q in set_l])
    pj=P(dj,dl); plj=P(dl,dj)
    poly_ok=exact_zero(pj-real_conj(plj))
    lane_kernel=True
    for s in [1,-1]:
      ks=sp.cancel(sp.Integer(s)/(x-rho-I*s*eps)*pj)
      kflip=sp.cancel(sp.Integer(-s)/(x-rho+I*s*eps)*plj)
      branch_ok=exact_zero(ks + real_conj(kflip))
      lane_kernel &= branch_ok
    if dj != dl:
      wrong_same_fail |= (not exact_zero(pj-real_conj(pj)))
    all_set &= set_ok; all_poly &= poly_ok; all_kernel &= lane_kernel
    rows.append({'two_j':dj,'two_l':dl,'index_set_bijection':bool(set_ok),'polynomial_branchflip_exact':bool(poly_ok),'kernel_branchflip_exact':bool(lane_kernel)})

inadmissible_count=sum(1 for dj in range(17) for dl in range(17) if (dj+dl)%2)
valid=all_set and all_poly and all_kernel and wrong_same_fail and inadmissible_count>0
classification='ITER075E_APPENDIXD_BRANCHFLIP_KERNEL_IDENTITY_EXACT_SCOPED' if valid else 'ITER075E_APPENDIXD_BRANCHFLIP_KERNEL_IDENTITY_OBSTRUCTED_SCOPED'
out={
 'iteration':'Iter075E',
 'classification':classification,
 'admissible_pair_count':len(rows),
 'inadmissible_parity_pair_count':inadmissible_count,
 'all_index_set_bijections_exact':bool(all_set),
 'all_polynomial_branchflip_identities_exact':bool(all_poly),
 'all_kernel_branchflip_identities_exact':bool(all_kernel),
 'unequal_spin_wrong_same_branch_control_obstructed':bool(wrong_same_fail),
 'rows':rows,
 'scope':'Exact Appendix-D polynomial/Feynman-kernel factor identity only; not a full unequal-spin Toller SL(2,C) inversion theorem.',
 'claim_locks':['no physical causal-sector selection','no K5/G3/F9/G8 promotion','no causal-vertex finiteness/divergence theorem','no new-physics/complete-QG claim']
}
print(json.dumps(out,indent=2,sort_keys=True))
with open('iter075e_appendixd_branchflip_exact.json','w') as f:
    json.dump(out,f,indent=2,sort_keys=True)
if not valid:
    raise SystemExit(2)
