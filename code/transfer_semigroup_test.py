#!/usr/bin/env python3
"""Compare simple scalar transfer-kernel families against composition/reversal/norm gates.

This is a negative/control calculation.  Actual Toller matrices are not group
representations, so a pass here is not evidence for a physical causal spinfoam vertex.
"""
from __future__ import annotations
import argparse, cmath, json, math
from pathlib import Path
T=[.1,.2,.4,.7,1.0];PAIRS=[(x,y) for x in T for y in T if x+y<=1.4]
def family(name,t,alpha=1.1,gamma=.35):
    if name=="unitary_character": return cmath.exp(1j*alpha*t)
    if name=="damped_character": return cmath.exp((-gamma+1j*alpha)*t)
    if name=="quadratic_phase": return cmath.exp(1j*alpha*t*t)
    if name=="rational_resolvent": return 1/(1-1j*alpha*t)
    if name=="cosine_projector_like": return complex(math.cos(alpha*t),0)
    raise ValueError(name)
def evaluate(name):
    composition=max(abs(family(name,x+y)-family(name,x)*family(name,y)) for x,y in PAIRS);unit=max(abs(abs(family(name,t))-1) for t in T);rev=max(abs(family(name,-t)-family(name,t).conjugate()) for t in T)
    return {"family":name,"composition_max":composition,"unit_modulus_max":unit,"orientation_reversal_max":rev,"total":composition+unit+rev}
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--output",default="results/transfer_semigroup.json");args=ap.parse_args();names=["unitary_character","damped_character","quadratic_phase","rational_resolvent","cosine_projector_like"];rows=sorted((evaluate(n) for n in names),key=lambda r:r["total"])
    out={"tests":["composition","unit_modulus","orientation_reversal"],"rows":rows,"winner":rows[0]["family"],"verdict":"ONE_PARAMETER_UNITARY_GROUP_STRUCTURE_FAVORED","interpretation":"Within the deliberately naive scalar family, a phase character wins but its generator/coupling is unspecified.","claim_scope":"negative control only; no Hilbert-space or spin-foam unitarity claim"}
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding="utf-8");print(json.dumps(out,indent=2))
    if out["winner"]!="unitary_character": raise SystemExit(1)
if __name__=="__main__": main()
