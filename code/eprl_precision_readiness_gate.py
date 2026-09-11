#!/usr/bin/env python3
"""Power-tail-aware readiness tiers for the first causal EPRL calculation.

The observed last shell increment is not itself the remaining truncation error.
Run #5 strongly preferred a power law for all published tails, so this gate fits
late increments with |Delta A_n|=C n^-p over windows 5..10 and estimates the
unresolved infinite tail.  It distinguishes a ~2% prototype target from a 1%
quantitative target.  Neither tier grants F9 credit.
"""
from __future__ import annotations
import argparse,json,math,statistics,urllib.request
from pathlib import Path
URL='https://raw.githubusercontent.com/PietropaoloFrisoni/HowToSpinFoamAmplitude/master/Delta_4_ampls/Immirzi_1.2/j_1.0/CSV_format/Delta_4_ampls_Dl_max_25.csv'

def data():
 with urllib.request.urlopen(URL,timeout=30) as r:txt=r.read().decode()
 return [[float(x) for x in l.split()] for l in txt.splitlines() if l.strip()]
def linfit(x,y):
 n=len(x);mx=sum(x)/n;my=sum(y)/n;sxx=sum((v-mx)**2 for v in x);b=sum((x[i]-mx)*(y[i]-my) for i in range(n))/sxx;a=my-b*mx;return a,b
def ztail(N,p):
 n=float(N);return n**(1-p)/(p-1)+.5*n**(-p)+(p/12)*n**(-p-1)-p*(p+1)*(p+2)/720*n**(-p-3)
def one(v,w):
 d=[v[i]-v[i-1] for i in range(1,len(v))];ii=list(range(1,len(v)));dd=d[-w:];ix=ii[-w:];a,b=linfit([math.log(i) for i in ix],[math.log(abs(x)) for x in dd]);p=-b;C=math.exp(a);tail=(1 if statistics.median(dd)>0 else -1)*C*ztail(len(v),p);ainf=v[-1]+tail;return {'window':w,'p':p,'tail_fraction':abs(tail)/abs(ainf),'Ainf':ainf}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',default='results/eprl_precision_readiness_gate.json');args=ap.parse_args();cols=list(zip(*data()));rows=[]
 for ci,col in enumerate(cols):
  fits=[one(list(col),w) for w in range(5,11)];lims=[f['Ainf'] for f in fits];med=statistics.median(lims);spread=(max(lims)-min(lims))/abs(med);tail=statistics.median([f['tail_fraction'] for f in fits]);rows.append({'column':ci,'median_tail_fraction':tail,'fit_window_spread':spread,'fits':fits})
 maxt=max(r['median_tail_fraction'] for r in rows);maxs=max(r['fit_window_spread'] for r in rows);proto=maxt<.02 and maxs<.005;precision=maxt<.01 and maxs<.005
 out={'target':{'gamma':1.2,'j':1.0,'Dl':25},'columns':rows,'max_median_tail_fraction':maxt,'max_fit_window_spread':maxs,'prototype_2pct_ready':proto,'quantitative_1pct_ready':precision,'verdict':'PROTOTYPE_READY__QUANTITATIVE_NOT_READY' if proto and not precision else ('PROTOTYPE_AND_1PCT_READY' if precision else 'PROTOTYPE_NOT_READY'),'scientific_credit':'NONE_FOR_F9','next_precision_action':'extend the same gamma/j series beyond Dl=25 until the power-tail estimate is below 1% before precision F9 claims'}
 p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
