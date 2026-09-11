#!/usr/bin/env python3
"""Back-test tail extrapolators against the deepest published EPRL Delta_4 series.

We deliberately treat the Dl=25 value only as a finite-cutoff reference, not as
the exact amplitude.  The question is operational: how early could a cheap
estimator have predicted the deepest published value to sub-percent accuracy?
"""
from __future__ import annotations
import argparse, json, math, statistics, urllib.request
from pathlib import Path
URL='https://raw.githubusercontent.com/PietropaoloFrisoni/HowToSpinFoamAmplitude/master/Delta_4_ampls/Immirzi_1.2/j_1.0/CSV_format/Delta_4_ampls_Dl_max_25.csv'
TOLS=(1e-2,5e-3,2e-3)

def fetch():
    with urllib.request.urlopen(URL,timeout=30) as r: txt=r.read().decode()
    return [[float(x) for x in line.split()] for line in txt.splitlines() if line.strip()]

def aitken(vals,k):
    if k<2:return None
    x0,x1,x2=vals[k-2],vals[k-1],vals[k]
    den=x2-2*x1+x0
    if abs(den)<1e-300:return None
    return x0-(x1-x0)**2/den

def geometric(vals,k,ratio_window=4):
    if k<3:return None
    diffs=[vals[i]-vals[i-1] for i in range(1,k+1)]
    ratios=[]
    for i in range(max(1,len(diffs)-ratio_window+1),len(diffs)):
        if abs(diffs[i-1])>1e-300: ratios.append(abs(diffs[i]/diffs[i-1]))
    if not ratios:return None
    r=statistics.median(ratios)
    if not (0<r<1):return None
    d=diffs[-1]
    return vals[k]+d*r/(1-r)

def relerr(x,ref):
    return None if x is None else abs(x-ref)/max(abs(ref),1e-300)

def earliest_sustained(errors,tol,start=6):
    for k in range(start,len(errors)):
        tail=[e for e in errors[k:] if e is not None]
        if tail and len(tail)==len(errors[k:]) and max(tail)<tol:return k
    return None

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',default='results/eprl_tail_estimator_validation.json');args=ap.parse_args()
    rows=fetch();cols=list(zip(*rows));outcols=[]
    for ci,col in enumerate(cols):
        vals=list(col);ref=vals[-1]
        ea=[relerr(aitken(vals,k),ref) for k in range(len(vals))]
        eg=[relerr(geometric(vals,k),ref) for k in range(len(vals))]
        outcols.append({'column':ci,'reference_Dl':len(vals)-1,'reference_value':ref,
            'aitken_relative_error_by_Dl':ea,'geometric_relative_error_by_Dl':eg,
            'earliest_sustained':{
              'aitken':{str(t):earliest_sustained(ea,t) for t in TOLS},
              'geometric':{str(t):earliest_sustained(eg,t) for t in TOLS}}})
    # choose estimator/cutoff only if all columns share a sustained threshold
    choices=[]
    for method in ('aitken','geometric'):
        for t in TOLS:
            ds=[c['earliest_sustained'][method][str(t)] for c in outcols]
            if all(x is not None for x in ds):choices.append({'method':method,'tolerance':t,'Dl':max(ds)})
    choices.sort(key=lambda x:(x['Dl'],x['tolerance']))
    out={'dataset':'gamma=1.2,j=1.0,maxDl=25','reference_is_finite_cutoff':True,'columns':outcols,'validated_choices':choices,
         'cheapest_validated_choice':choices[0] if choices else None,
         'verdict':'TAIL_ESTIMATOR_BACKTEST_COMPLETE',
         'scope':'back-test to the published Dl=25 value; does not establish the infinite-Dl error'}
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps({'verdict':out['verdict'],'choice':out['cheapest_validated_choice'],'validated_choices':choices},indent=2))
if __name__=='__main__':main()
