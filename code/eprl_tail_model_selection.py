#!/usr/bin/env python3
"""Compare simple tail models for published Lorentzian EPRL shell increments.

Fits are diagnostics only.  We compare log|Delta A_Dl| ~ a+b Dl (exponential)
with log|Delta A_Dl| ~ a-p log(Dl+1) (power law) over the last 8 available
increments.  This helps avoid using a geometric tail estimator when the data
are actually closer to a slowly varying power law.
"""
from __future__ import annotations
import argparse,json,math,urllib.request
from pathlib import Path
BASE='https://raw.githubusercontent.com/PietropaoloFrisoni/HowToSpinFoamAmplitude/master/Delta_4_ampls'
DATA={
'g0.1_j0.5':f'{BASE}/Immirzi_0.1/j_0.5/CSV_format/Delta_4_ampls_Dl_max_15.csv',
'g1.0_j0.5':f'{BASE}/Immirzi_1.0/j_0.5/CSV_format/Delta_4_ampls_Dl_max_15.csv',
'g1.2_j0.5':f'{BASE}/Immirzi_1.2/j_0.5/CSV_format/Delta_4_ampls_Dl_max_15.csv',
'g1.2_j1.0':f'{BASE}/Immirzi_1.2/j_1.0/CSV_format/Delta_4_ampls_Dl_max_25.csv'}

def fetch(u):
 with urllib.request.urlopen(u,timeout=30) as r:txt=r.read().decode()
 return [[float(x) for x in l.split()] for l in txt.splitlines() if l.strip()]
def linfit(x,y):
 n=len(x);mx=sum(x)/n;my=sum(y)/n;sxx=sum((z-mx)**2 for z in x);sxy=sum((x[i]-mx)*(y[i]-my) for i in range(n));b=sxy/sxx if sxx else 0;a=my-b*mx
 pred=[a+b*z for z in x];ssr=sum((y[i]-pred[i])**2 for i in range(n));sst=sum((z-my)**2 for z in y);r2=1-ssr/sst if sst else 1
 return a,b,r2

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--tail',type=int,default=8);ap.add_argument('--output',default='results/eprl_tail_model_selection.json');args=ap.parse_args();rows=[]
 for name,u in DATA.items():
  data=fetch(u)
  for ci,col in enumerate(zip(*data)):
   v=list(col);d=[abs(v[i]-v[i-1]) for i in range(1,len(v))];idx=list(range(1,len(v)))
   pairs=[(i,z) for i,z in zip(idx,d) if z>0][-args.tail:]
   ii=[p[0] for p in pairs];ly=[math.log(p[1]) for p in pairs]
   ae,be,r2e=linfit(ii,ly);xp=[math.log(i+1) for i in ii];apow,bpow,r2p=linfit(xp,ly);p=-bpow
   pref='POWER' if r2p>r2e else 'EXPONENTIAL'
   rows.append({'dataset':name,'column':ci,'points':len(ii),'exp_slope':be,'exp_ratio_per_shell':math.exp(be),'exp_r2':r2e,'power_p':p,'power_r2':r2p,'preferred':pref,'power_tail_summable_if_asymptotic':p>1})
 counts={k:sum(r['preferred']==k for r in rows) for k in ('POWER','EXPONENTIAL')}
 out={'tail_points':args.tail,'fits':rows,'preference_counts':counts,'verdict':'TAIL_MODEL_COMPARISON_COMPLETE','scope':'descriptive fit over the published finite-Dl tail only; not proof of asymptotic form'}
 pth=Path(args.output);pth.parent.mkdir(parents=True,exist_ok=True);pth.write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps({'verdict':out['verdict'],'counts':counts,'fits':rows},indent=2))
if __name__=='__main__':main()
