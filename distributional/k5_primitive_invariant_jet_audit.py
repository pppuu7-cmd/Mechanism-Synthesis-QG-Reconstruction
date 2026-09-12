#!/usr/bin/env python3
"""Iter040: quotient S5/A5 invariant jets by descendants of the quadratic invariant."""
from __future__ import annotations
import argparse, itertools, json
from pathlib import Path
import numpy as np
from distributional.k5_extension_invariant_jet_audit import cycle_basis, cycle_rep, parity, inv_dim

N=5

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--degree',type=int,required=True)
    ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args(); d=a.degree
    if not 2<=d<=16: raise SystemExit('degree must be in [2,16]')
    q=cycle_basis(); s5=list(itertools.permutations(range(N))); a5=[p for p in s5 if parity(p)==0]
    reps={p:cycle_rep(p,q) for p in s5}
    s5d,r1=inv_dim(s5,reps,d); s5m,r2=inv_dim(s5,reps,d-2)
    a5d,r3=inv_dim(a5,reps,d); a5m,r4=inv_dim(a5,reps,d-2)
    ps5=s5d-s5m; pa5=a5d-a5m
    maxres=max(r1,r2,r3,r4)
    gates={'integrality_residual_ok':maxres<2e-8,'s5_quotient_nonnegative':ps5>=0,'a5_quotient_nonnegative':pa5>=0}
    result={'iteration':'Iter040','degree':d,
            's5_dimension':s5d,'s5_quadratic_descendant_dimension':s5m,'s5_primitive_dimension':ps5,
            'a5_dimension':a5d,'a5_quadratic_descendant_dimension':a5m,'a5_primitive_dimension':pa5,
            'max_integrality_residual':maxres,'numerical_gates':gates,
            'scientific_discriminator':{'quadratic_generates_all_s5_at_degree':ps5==0},
            'classification':('NO_NEW_S5_PRIMITIVE_AT_DEGREE' if ps5==0 else 'NEW_SYMMETRY_ALLOWED_S5_PRIMITIVE_JET_SHAPES'),
            'claim_lock':'Invariant-ring quotient only; not a physical extension/counterterm prescription.'}
    a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
    if not all(gates.values()): raise SystemExit(1)
if __name__=='__main__': main()
