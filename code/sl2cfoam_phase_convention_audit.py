#!/usr/bin/env python3
"""Infer the phase map between Ruhl d-matrices and sl2cfoam-next dsmall.

The Toller closed forms used in the 2026 analytic paper adopt Ruhl's convention,
while standard spinfoam numerical codes use a rho-dependent phase.  This script
compares upstream sl2cfoam pointwise dsmall values against Ruhl Eq. (71) under
several explicit phase candidates and selects the unique low-residual mapping.
"""
from __future__ import annotations
import argparse,csv,json
from pathlib import Path
import mpmath as mp
from toller_general_eprl_reference import d_ruhl
mp.mp.dps=80

def phase_phi(rho,j,l):
    # Eq. (4): exp[-i*pi*(j-l)/2] times unit-modulus Gamma phases.
    a=mp.gamma(j+1+1j*rho); b=mp.gamma(l+1-1j*rho)
    return mp.e**(-1j*mp.pi*(j-l)/2)*(a/abs(a))*(b/abs(b))

def rel(a,b): return float(abs(a-b)/max(abs(b),mp.mpf('1e-60')))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--probe',default='results/sl2cfoam_dsmall_probe.tsv');ap.add_argument('--output',default='results/sl2cfoam_phase_convention_audit.json');args=ap.parse_args()
    rows=[]
    with open(args.probe,newline='') as f:
      for r in csv.DictReader(f,delimiter='\t'):
        tj=int(r['two_j']);tl=int(r['two_l']);tm=int(r['two_m']);j=mp.mpf(tj)/2;l=mp.mpf(tl)/2;m=mp.mpf(tm)/2;g=mp.mpf(r['gamma']);beta=mp.mpf(r['beta']);rho=g*j
        ds=mp.mpc(mp.mpf(r['re']),mp.mpf(r['im']));dr=d_ruhl(j,l,m,j,rho,beta);ph=phase_phi(rho,j,l)
        candidates={
          'ruhl':dr,
          'phi_times_ruhl':ph*dr,
          'conj_phi_times_ruhl':mp.conj(ph)*dr,
          'minus_phi_times_ruhl':-ph*dr,
          'minus_conj_phi_times_ruhl':-mp.conj(ph)*dr,
          'i_phi_times_ruhl':1j*ph*dr,
          'minus_i_phi_times_ruhl':-1j*ph*dr,
        }
        errs={k:rel(v,ds) for k,v in candidates.items()}
        rows.append({'two_j':tj,'two_l':tl,'two_m':tm,'gamma':float(g),'beta':float(beta),'sl2cfoam':[float(mp.re(ds)),float(mp.im(ds))],'ruhl':[float(mp.re(dr)),float(mp.im(dr))],'phi':[float(mp.re(ph)),float(mp.im(ph))],'errors':errs})
    names=list(rows[0]['errors']);scores={n:{'max':max(r['errors'][n] for r in rows),'median':float(mp.median([r['errors'][n] for r in rows]))} for n in names}
    winner=min(names,key=lambda n:scores[n]['max']);passed=scores[winner]['max']<1e-8
    out={'cases':len(rows),'phase_formula':'Phi=exp[-i*pi*(j-l)/2] Gamma(j+i rho+1)/|Gamma| Gamma(l-i rho+1)/|Gamma|','candidate_scores':scores,'winner':winner,'winner_max_relative_error':scores[winner]['max'],'passed':passed,'rows':rows,'verdict':'SL2CFOAM_PHASE_MAP_IDENTIFIED' if passed else 'PHASE_MAP_UNRESOLVED','next_action':'multiply both general Toller branches by the empirically identified phase before comparing/inserting into sl2cfoam booster convention','scope':'pointwise ordinary dsmall convention audit only; no causal booster/F9 credit'}
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out,indent=2))
    if not passed: raise SystemExit(2)
if __name__=='__main__':main()
