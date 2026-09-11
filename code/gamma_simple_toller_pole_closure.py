#!/usr/bin/env python3
"""Exact arithmetic test of naive same-branch composition on the gamma-simple Toller pole lattice.

For gamma-simple EPRL data (rho=gamma*j, k=j), the 2026 Toller boost representation gives
  omega_n^± = ∓ gamma*j - i(2n + j ± m + 1),
because j±m >= 0 for m in {-j,...,j}.

If two same-branch residue modes are naively multiplied at the same boost beta, their
frequencies add. With fixed nonzero gamma, matching the real part to a single coarse
gamma-simple mode forces J=j1+j2. Clebsch-Gordan then permits M=m1+m2. The imaginary
part would require N=n1+n2+1/2, impossible for integer N.

This script exhaustively verifies the obstruction over a configurable finite range.
It is a statement about naive mode multiplication, not about the full glued spin-foam RG map.
"""
from __future__ import annotations
import argparse, json
from fractions import Fraction
from pathlib import Path

def m_values(j2:int):
    # doubled m runs -j2,-j2+2,...,j2
    return range(-j2,j2+1,2)

def decay(j2:int,m2:int,n:int,branch:int)->Fraction:
    # branch +1 corresponds to j+m, branch -1 to j-m in |j ± m|
    return Fraction(2*n+1,1)+Fraction(j2+branch*m2,2)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--max-j2',type=int,default=8,help='maximum doubled spin 2j');ap.add_argument('--max-n',type=int,default=5);ap.add_argument('--output',default='results/gamma_simple_toller_pole_closure.json');args=ap.parse_args()
    tested=0; exact_matches=0; required_N=set(); examples=[]
    for j12 in range(1,args.max_j2+1):
      for j22 in range(1,args.max_j2+1):
        J2=j12+j22
        for m12 in m_values(j12):
          for m22 in m_values(j22):
            M2=m12+m22
            for n1 in range(args.max_n+1):
              for n2 in range(args.max_n+1):
                for branch in (+1,-1):
                  tested+=1
                  dsum=decay(j12,m12,n1,branch)+decay(j22,m22,n2,branch)
                  base=Fraction(J2+branch*M2,2)+1
                  Nreq=(dsum-base)/2
                  required_N.add(Nreq)
                  if Nreq.denominator==1 and Nreq>=0: exact_matches+=1
                  if len(examples)<12:
                    examples.append({'j1':str(Fraction(j12,2)),'j2':str(Fraction(j22,2)),'m1':str(Fraction(m12,2)),'m2':str(Fraction(m22,2)),'n1':n1,'n2':n2,'branch':'+' if branch==1 else '-','J':str(Fraction(J2,2)),'M':str(Fraction(M2,2)),'required_N':str(Nreq)})
    expected={Fraction(k,1)+Fraction(1,2) for k in range(0,2*args.max_n+1)}
    verdict='NO_NAIVE_SAME_BRANCH_GAMMA_SIMPLE_POLE_CLOSURE' if exact_matches==0 and required_N==expected else 'UNEXPECTED'
    out={'source_formula':'omega_n^± = ∓ gamma j - i(2n + j ± m + 1) for gamma-simple k=j, rho=gamma j','fixed_gamma_real_part_condition':'same-branch frequency addition forces J=j1+j2','imaginary_part_condition':'N_required = n1+n2+1/2','tested_configurations':tested,'exact_integer_N_matches':exact_matches,'required_N_values':sorted(str(x) for x in required_N),'verdict':verdict,'interpretation':'Raw multiplication of two same-branch Toller residue modes cannot itself define a single coarse gamma-simple Toller mode at fixed gamma. A physical RG step must include nontrivial gluing/internal sums/embedding and cannot be represented by simple mode multiplication.','scope':'exact pole-lattice obstruction for naive same-beta mode multiplication only; not a no-go theorem for causal EPRL coarse graining','examples':examples}
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps({k:out[k] for k in ['tested_configurations','exact_integer_N_matches','required_N_values','verdict']},indent=2))
    if verdict=='UNEXPECTED': raise SystemExit(1)
if __name__=='__main__':main()
