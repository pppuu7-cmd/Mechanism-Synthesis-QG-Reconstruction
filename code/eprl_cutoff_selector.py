#!/usr/bin/env python3
"""Select the smallest *observationally stable* shell cutoff in published EPRL data.

This is a truncation-planning diagnostic, not a rigorous error bound.  For each
published numerical column we ask for the earliest Dl at which the previous
`window` relative shell increments are all below a requested tolerance.  The
result is useful for choosing the cheapest configuration worth carrying into a
future same-realization Toller/CCI calculation.
"""
from __future__ import annotations
import argparse, json, urllib.request
from pathlib import Path

BASE='https://raw.githubusercontent.com/PietropaoloFrisoni/HowToSpinFoamAmplitude/master/Delta_4_ampls'
DATASETS={
 'g0.1_j0.5':f'{BASE}/Immirzi_0.1/j_0.5/CSV_format/Delta_4_ampls_Dl_max_15.csv',
 'g1.0_j0.5':f'{BASE}/Immirzi_1.0/j_0.5/CSV_format/Delta_4_ampls_Dl_max_15.csv',
 'g1.2_j0.5':f'{BASE}/Immirzi_1.2/j_0.5/CSV_format/Delta_4_ampls_Dl_max_15.csv',
 'g1.2_j1.0':f'{BASE}/Immirzi_1.2/j_1.0/CSV_format/Delta_4_ampls_Dl_max_25.csv',
}
TOLS=(1e-2,5e-3,2e-3,1e-3)

def fetch(url):
    with urllib.request.urlopen(url,timeout=30) as r: txt=r.read().decode()
    return [[float(x) for x in line.split()] for line in txt.splitlines() if line.strip()]

def relsteps(vals):
    out=[]
    for i in range(1,len(vals)):
        den=max(abs(vals[i]),1e-300)
        out.append(abs(vals[i]-vals[i-1])/den)
    return out

def first_stable(steps,tol,window):
    # steps[k-1] is the relative change entering Dl=k.
    for dl in range(window,len(steps)+1):
        recent=steps[dl-window:dl]
        if len(recent)==window and max(recent)<tol:
            return dl
    return None

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--window',type=int,default=3);ap.add_argument('--output',default='results/eprl_cutoff_selector.json');args=ap.parse_args()
    rows=[]
    for name,url in DATASETS.items():
        data=fetch(url); cols=list(zip(*data))
        for ci,col in enumerate(cols):
            steps=relsteps(list(col)); sels={str(t):first_stable(steps,t,args.window) for t in TOLS}
            rows.append({'dataset':name,'column':ci,'max_Dl':len(col)-1,'final_relative_step':steps[-1],'selected_Dl':sels})
    # A conservative planning baseline: require every column in one dataset to meet 0.2%.
    by={}
    for r in rows: by.setdefault(r['dataset'],[]).append(r)
    candidates=[]
    for name,rr in by.items():
        ds=[r['selected_Dl'][str(2e-3)] for r in rr]
        if all(x is not None for x in ds): candidates.append({'dataset':name,'required_Dl':max(ds)})
    candidates.sort(key=lambda x:x['required_Dl'])
    out={'window':args.window,'tolerances':TOLS,'series':rows,'datasets_meeting_0p2_percent_observed_stability':candidates,
         'planning_choice':candidates[0] if candidates else None,
         'verdict':'OBSERVED_STABLE_CUTOFFS_IDENTIFIED' if candidates else 'NO_DATASET_MEETS_0P2_PERCENT_WITH_PUBLISHED_RANGE',
         'scope':'empirical shell-increment criterion only; not a rigorous truncation-error bound and not F9 evidence'}
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
