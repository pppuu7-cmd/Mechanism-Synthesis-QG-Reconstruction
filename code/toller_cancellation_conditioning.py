#!/usr/bin/env python3
"""Quantify t+ / t- cancellation in booster-relevant EPRL kinematics.

Because t+ + t- = d can involve individually large branches, a causal booster may
require substantially more precision than the ordinary EPRL booster.  We scan
k=j, rho=gamma*j, l>=j and report K=(|t+|+|t-|)/|d|.  Roughly log10(K)
decimal digits can be lost when reconstructing d from both branches.
"""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
import mpmath as mp
from toller_general_eprl_reference import tplus,tminus,d_ruhl
mp.mp.dps=80

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--max-dl',type=int,default=4);ap.add_argument('--output',default='results/toller_cancellation_conditioning.json');args=ap.parse_args()
    betas=[mp.mpf(x) for x in ('0.1','0.2','0.4','0.8','1.6','3.0')]
    gammas=[mp.mpf(x) for x in ('0.1','0.4','1.2')]
    rows=[]
    for two_j in (1,2):
      j=mp.mpf(two_j)/2;k=j
      for dl in range(args.max_dl+1):
       l=j+dl
       for two_m in range(-two_j,two_j+1,2):
        m=mp.mpf(two_m)/2
        for gamma in gammas:
         rho=gamma*j
         for beta in betas:
          tp=tplus(j,l,m,k,rho,beta);tm=tminus(j,l,m,k,rho,beta);d=d_ruhl(j,l,m,k,rho,beta)
          K=(abs(tp)+abs(tm))/max(abs(d),mp.mpf('1e-70'))
          rows.append({'j':float(j),'l':float(l),'m':float(m),'gamma':float(gamma),'beta':float(beta),'condition':float(K),'digits_lost':max(0.0,float(mp.log10(K)))})
    rows.sort(key=lambda r:r['condition'],reverse=True)
    ks=[r['condition'] for r in rows]
    worst=rows[0]
    def pct(q):
      s=sorted(ks);return s[min(len(s)-1,int(q*(len(s)-1)))]
    out={'cases':len(rows),'max_Dl':args.max_dl,'worst_case':worst,'condition_percentiles':{'p50':pct(.50),'p90':pct(.90),'p99':pct(.99)},'max_digits_lost':worst['digits_lost'],'recommended_extra_decimal_digits_for_branch_sum':math.ceil(worst['digits_lost'])+4,'top20':rows[:20],
      'verdict':'CAUSAL_BRANCH_CANCELLATION_REQUIRES_GUARDED_PRECISION' if worst['digits_lost']>2 else 'DOUBLE_PRECISION_CONDITIONING_MILD',
      'scope':'pointwise reduced Toller matrices; booster integration can add further conditioning and must be audited separately'}
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
