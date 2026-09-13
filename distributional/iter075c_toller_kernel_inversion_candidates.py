import json
from pathlib import Path
import mpmath as mp

mp.mp.dps = 90
EPS = mp.mpf('1e-4')
RHO_VALUES = [mp.mpf('0.7'), mp.mpf('1.3')]
TILDE = [mp.mpf(x) for x in ['-2.4','-1.1','-0.2','0.4','1.8','2.7']]
JL = [(mp.mpf('1'),mp.mpf('1')),(mp.mpf('1'),mp.mpf('2')),(mp.mpf('1.5'),mp.mpf('0.5')),(mp.mpf('2'),mp.mpf('3'))]
BRANCHES = [1,-1]
THRESH = mp.mpf('1e-20')
CONTROL_THRESH = mp.mpf('1e-60')


def coeff(s,j,l,rho,rt,eps=EPS):
    pole = mp.mpf(s) / (rt-rho-mp.mpc(0,s)*eps)
    gr = mp.gamma(-j-mp.j*rho)*mp.gamma(l-mp.j*rt+1)/(mp.gamma(-j-mp.j*rt)*mp.gamma(l-mp.j*rho+1))
    return pole*gr


def max_norm_dev(vals):
    r0 = vals[0]
    return max(abs(v/r0-1) for v in vals[1:]) if len(vals)>1 else mp.mpf('0')

lanes=[]
all_finite=True
same_all=True
flip_all=True
for j,l in JL:
    for rho in RHO_VALUES:
        for s in BRANCHES:
            row={"j":str(j),"l":str(l),"rho":str(rho),"branch":s,"candidates":{}}
            for name,sp in [("same",s),("flip",-s)]:
                ratios=[]
                finite=True
                for rt in TILDE:
                    a=coeff(s,j,l,rho,rt)
                    b=mp.conj(coeff(sp,l,j,rho,rt))
                    if a==0 or b==0 or not (mp.isfinite(a.real) and mp.isfinite(a.imag) and mp.isfinite(b.real) and mp.isfinite(b.imag)):
                        finite=False
                        break
                    ratios.append(a/b)
                if finite:
                    dev=max_norm_dev(ratios)
                    compatible=dev<=THRESH
                    mag0=abs(ratios[0])
                    phase0=mp.arg(ratios[0])
                else:
                    dev=mp.inf; compatible=False; mag0=mp.nan; phase0=mp.nan
                all_finite = all_finite and finite
                if name=="same": same_all = same_all and compatible
                else: flip_all = flip_all and compatible
                row["candidates"][name]={
                    "finite_nonzero":finite,
                    "max_normalized_deviation":mp.nstr(dev,30),
                    "compatible":compatible,
                    "first_ratio_abs":mp.nstr(mag0,30),
                    "first_ratio_arg":mp.nstr(phase0,30),
                }
            lanes.append(row)

# Frozen synthetic constant-factor control.
phase=mp.e**(mp.j*mp.mpf('0.731'))
control=[phase for _ in TILDE]
control_dev=max_norm_dev(control)
control_pass=control_dev<=CONTROL_THRESH

if not all_finite or not control_pass:
    classification="ITER075C_KERNEL_AUDIT_INVALID"
elif same_all or flip_all:
    classification="ITER075C_SIMPLE_TOLLER_INVERSION_CANDIDATE_SURVIVES_KERNEL_GATE_SCOPED"
else:
    classification="ITER075C_SIMPLE_SAME_CONTOUR_TOLLER_INVERSION_CANDIDATES_OBSTRUCTED_SCOPED"

out={
    "iteration":"Iter075C",
    "classification":classification,
    "source_formula":"arXiv:2601.23162 Eq.(3) / arXiv:2604.24945 Feynman i-epsilon representation",
    "epsilon":str(EPS),
    "tilde_rho_samples":[str(x) for x in TILDE],
    "threshold":str(THRESH),
    "control_threshold":str(CONTROL_THRESH),
    "all_kernels_finite_nonzero":all_finite,
    "same_branch_compatible_all_lanes":same_all,
    "flipped_branch_compatible_all_lanes":flip_all,
    "synthetic_control":{"max_normalized_deviation":mp.nstr(control_dev,30),"pass":control_pass},
    "lanes":lanes,
    "scientific_summary":"Necessary same-real-axis kernel matching test for the two simplest branchwise inversion candidates. Failure is scoped: it does not exclude label changes, contour/variable transformations, or other source-derived factors.",
    "claim_lock":"No physical causal-sector selection, no K5/G3/F9/G8 promotion, no finiteness/divergence theorem, no complete-QG or new-physics claim."
}
Path('out').mkdir(exist_ok=True)
Path('out/iter075c-kernel-audit.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2,sort_keys=True))
if classification=="ITER075C_KERNEL_AUDIT_INVALID":
    raise SystemExit(2)
