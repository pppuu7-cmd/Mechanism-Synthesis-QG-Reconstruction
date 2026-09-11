#!/usr/bin/env python3
"""Diagnose causal-sector degeneracy of gamma-simple Toller poles under a hypothetical Immirzi flow.

For gamma-simple data, Re omega_n^+ = -gamma*j and Re omega_n^- = +gamma*j (j>0).
Thus gamma=0 is a degeneracy surface for a causal split identified by boost-frequency sign.
This script tests sample trajectories only. It neither supplies nor assumes a physical beta_gamma
for causal EPRL; any real running must come from a same-realization RG calculation.
"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path

def trajectories(t):
    return {
      'constant_positive': 0.274,
      'positive_running_no_cross': 0.12 + 0.20/(1.0+t),
      'positive_to_negative': 0.30 - 0.60*t,
      'tanh_crossing': 0.25*math.tanh(4.0*(0.5-t)),
      'positive_asymptote_zero': 0.30*math.exp(-6.0*t),
      'constant_negative': -0.274,
    }

def classify(vals,eps=1e-10):
    signs=[]
    for v in vals:
        signs.append(0 if abs(v)<=eps else (1 if v>0 else -1))
    crossings=sum(1 for a,b in zip(signs,signs[1:]) if a*b<0)
    touches=any(s==0 for s in signs)
    minabs=min(abs(v) for v in vals)
    if crossings or touches: verdict='CAUSAL_FREQUENCY_LABEL_DEGENERACY_OR_EXCHANGE'
    elif minabs<1e-4: verdict='APPROACHES_PROJECTOR_DEGENERACY_SURFACE'
    else: verdict='FREQUENCY_SIGN_LABEL_STABLE_ON_SAMPLED_INTERVAL'
    return signs,crossings,touches,minabs,verdict

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--steps',type=int,default=1001);ap.add_argument('--output',default='results/gamma_flow_causal_sector.json');args=ap.parse_args()
    ts=[i/(args.steps-1) for i in range(args.steps)]
    names=list(trajectories(0.0).keys());rows=[]
    for name in names:
        vals=[trajectories(t)[name] for t in ts]
        signs,cross,touch,minabs,verdict=classify(vals)
        rows.append({'trajectory':name,'gamma_initial':vals[0],'gamma_final':vals[-1],'min_abs_gamma':minabs,'sign_crossings':cross,'touches_zero_on_grid':touch,'verdict':verdict})
    out={'source_relation':'gamma-simple Toller poles: Re omega_n^+ = -gamma*j, Re omega_n^- = +gamma*j for j>0','diagnostic_surface':'gamma = 0','rows':rows,'interpretation':'If causal branches are tracked by the sign of boost frequency, a gamma flow that crosses zero makes that labeling degenerate and exchanges the signs. A physical RG construction could instead transport projectors continuously, so this is a topology/labeling warning rather than a no-go theorem.','scope':'hypothetical trajectories only; no causal-EPRL beta_gamma is inferred'}
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
