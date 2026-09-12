#!/usr/bin/env python3
"""Map endpoint pole powers and T+ + T- cancellation across EPRL sectors.

This is a pointwise high-precision diagnostic of the analytic Toller split. It
measures local beta->0 powers; it does not define a Feynman i-epsilon contour or
claim that individual Toller branches are separately integrable.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp

from regulated import endpoint_precontraction_scan as ep

mp.mp.dps = 90
BETAS = [mp.mpf(x) for x in ("0.02","0.01","0.005","0.002","0.001","0.0005")]


def fit_power(vals):
    pts=[]
    for b,v in zip(BETAS,vals):
        a=abs(v)
        if mp.isfinite(a) and a>0:
            pts.append((mp.log(b),mp.log(a)))
    if len(pts)<4: return mp.nan
    # use last four points to emphasize endpoint behavior
    pts=pts[-4:]
    xb=sum(x for x,_ in pts)/len(pts); yb=sum(y for _,y in pts)/len(pts)
    return sum((x-xb)*(y-yb) for x,y in pts)/sum((x-xb)**2 for x,_ in pts)


def fmt(x): return mp.nstr(x,20)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--gamma",required=True)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    gamma=mp.mpf(args.gamma)
    ep.GAMMA=gamma

    rows=[]
    for tj in (1,2,3,4):  # j = 1/2, 1, 3/2, 2
        for dl in (0,1,2):
            tl=tj+2*dl
            for tp in range(-tj,tj+1,2):
                rho=gamma*(mp.mpf(tj)/2)
                vp=[]; vm=[]; vs=[]; cancellation=[]
                for beta in BETAS:
                    p=ep.toller_plus(tj,tl,tp,tj,rho,beta)
                    m=ep.toller_minus(tj,tl,tp,tj,rho,beta)
                    sm=p+m
                    vp.append(p); vm.append(m); vs.append(sm)
                    cancellation.append(abs(sm)/max(abs(p)+abs(m),mp.mpf("1e-200")))
                qp=fit_power(vp); qm=fit_power(vm); qs=fit_power(vs); qc=fit_power(cancellation)
                finite=all(mp.isfinite(abs(z)) for z in vp+vm+vs)
                rows.append({
                    "two_j":tj,"two_l":tl,"two_p":tp,
                    "q_plus":fmt(qp),"q_minus":fmt(qm),"q_sum":fmt(qs),
                    "cancellation_gain_power":fmt(qc),
                    "endpoint_ratio_sum_over_branches":fmt(cancellation[-1]),
                    "finite":bool(finite),
                    "expected_raw_d_at_beta0":"1 if l=j; 0 if l>j",
                })

    finite=[r for r in rows if r["finite"]]
    pole=[r for r in finite if float(r["q_plus"])<0 or float(r["q_minus"])<0]
    strong_cancel=[r for r in finite if float(r["cancellation_gain_power"])>0.5]
    out={
        "gamma":str(args.gamma),"mp_dps":mp.mp.dps,
        "betas":[fmt(b) for b in BETAS],
        "rows":rows,
        "summary":{
            "sectors":len(rows),"finite_sectors":len(finite),
            "sectors_with_branch_pole":len(pole),
            "sectors_with_positive_cancellation_gain_gt_half_power":len(strong_cancel),
        },
        "interpretation_guardrail":"Negative q_plus/q_minus is an endpoint pole signal. Positive cancellation_gain_power measures how rapidly T+ + T- cancels relative to the separate branches. This does not by itself define a regulated causal integral.",
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding="utf-8")
    print(json.dumps({"gamma":args.gamma,**out["summary"]},indent=2))

if __name__=="__main__": main()
