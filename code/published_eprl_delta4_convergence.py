#!/usr/bin/env python3
"""Reproducibility/convergence audit using published Lorentzian EPRL Delta_4 data.

Data source: PietropaoloFrisoni/HowToSpinFoamAmplitude, computed with sl2cfoam-next.
We intentionally do not assign physical meaning to the two tab-separated columns here;
we audit each published numerical series independently as a function of shell cutoff Dl.
"""
from __future__ import annotations
import argparse, io, json, math, urllib.request
from pathlib import Path

BASE='https://raw.githubusercontent.com/PietropaoloFrisoni/HowToSpinFoamAmplitude/master/Delta_4_ampls'
DATASETS=[
 ('g0.1_j0.5',f'{BASE}/Immirzi_0.1/j_0.5/CSV_format/Delta_4_ampls_Dl_max_15.csv'),
 ('g1.0_j0.5',f'{BASE}/Immirzi_1.0/j_0.5/CSV_format/Delta_4_ampls_Dl_max_15.csv'),
 ('g1.2_j0.5',f'{BASE}/Immirzi_1.2/j_0.5/CSV_format/Delta_4_ampls_Dl_max_15.csv'),
 ('g1.2_j1.0_max15',f'{BASE}/Immirzi_1.2/j_1.0/CSV_format/Delta_4_ampls_Dl_max_15.csv'),
 ('g1.2_j1.0_max25',f'{BASE}/Immirzi_1.2/j_1.0/CSV_format/Delta_4_ampls_Dl_max_25.csv'),
]

def fetch(url:str):
    with urllib.request.urlopen(url,timeout=30) as r:
        txt=r.read().decode('utf-8')
    rows=[]
    for line in txt.strip().splitlines():
        if not line.strip(): continue
        parts=line.split()
        rows.append([float(x) for x in parts])
    if not rows or len({len(r) for r in rows})!=1: raise ValueError('malformed dataset')
    return rows

def series_metrics(vals):
    n=len(vals);last=vals[-1]
    eps=1e-300
    increments=[abs(vals[i]-vals[i-1])/(abs(vals[i])+eps) for i in range(1,n)]
    tail3=vals[-4:] if n>=4 else vals
    span=(max(tail3)-min(tail3))/(abs(last)+eps)
    # simple observed ratio of successive absolute increments; diagnostic only
    diffs=[abs(vals[i]-vals[i-1]) for i in range(1,n)]
    ratios=[diffs[i]/diffs[i-1] for i in range(1,len(diffs)) if diffs[i-1]>0]
    return {
      'n_points':n,
      'last_value':last,
      'last_step_relative_change':increments[-1] if increments else None,
      'last_3_step_relative_span':span,
      'median_last_4_increment_ratio': sorted(ratios[-4:])[len(ratios[-4:])//2] if ratios else None,
      'relative_increment_by_Dl':increments,
    }

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',default='results/published_eprl_delta4_convergence.json');args=ap.parse_args()
    raw={name:fetch(url) for name,url in DATASETS}
    outsets={}
    for name,rows in raw.items():
        cols=list(zip(*rows))
        outsets[name]={'url':dict(DATASETS)[name],'rows':len(rows),'columns':[series_metrics(list(c)) for c in cols]}
    a=raw['g1.2_j1.0_max15'];b=raw['g1.2_j1.0_max25']
    overlap=min(len(a),len(b));max_abs=max(abs(a[i][j]-b[i][j]) for i in range(overlap) for j in range(len(a[0])))
    max_rel=max(abs(a[i][j]-b[i][j])/(abs(a[i][j])+1e-300) for i in range(overlap) for j in range(len(a[0])))
    # classify convergence only by observed final-step change; no extrapolated physics claim
    summary=[]
    for name,d in outsets.items():
        for ci,m in enumerate(d['columns']):
            r=m['last_step_relative_change']
            grade='LT_1_PERCENT' if r is not None and r<1e-2 else ('LT_5_PERCENT' if r is not None and r<5e-2 else 'GE_5_PERCENT')
            summary.append({'dataset':name,'column':ci,'last_step_relative_change':r,'grade':grade})
    out={
      'source_repository':'PietropaoloFrisoni/HowToSpinFoamAmplitude',
      'backend':'sl2cfoam-next Lorentzian EPRL amplitudes (published example data)',
      'datasets':outsets,
      'max15_vs_max25_overlap':{'points':overlap,'max_abs_difference':max_abs,'max_relative_difference':max_rel,'verdict':'PREFIX_IDENTICAL' if max_abs==0 else 'PREFIX_DIFFERS'},
      'convergence_summary':summary,
      'verdict':'PUBLISHED_EPRL_BACKEND_DATA_REPRODUCIBLY_PARSED_AND_CUTOFF_CONVERGENCE_QUANTIFIED',
      'scope':'backend/truncation audit only; these published amplitudes do not contain the Toller causal projection required for F9'
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps({'verdict':out['verdict'],'overlap':out['max15_vs_max25_overlap'],'convergence_summary':summary},indent=2))
    if out['max15_vs_max25_overlap']['verdict']!='PREFIX_IDENTICAL': raise SystemExit(1)
if __name__=='__main__':main()
