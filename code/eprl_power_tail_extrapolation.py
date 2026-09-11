#!/usr/bin/env python3
"""Estimate the unresolved Delta_l tail using the power law selected by run #5.

For shell increments Delta A_n = A_n-A_{n-1}, fit
    |Delta A_n| = C n^{-p}
over several late windows.  If p>1 and the late increments have a stable sign,
estimate the infinite remaining tail with an Euler-Maclaurin approximation to
sum_{n=D+1}^infty n^{-p}.  This is a model-based truncation estimate, not a
rigorous bound.  Robustness is measured across fit windows 5..10.
"""
from __future__ import annotations
import argparse,json,math,statistics,urllib.request
from pathlib import Path
URL='https://raw.githubusercontent.com/PietropaoloFrisoni/HowToSpinFoamAmplitude/master/Delta_4_ampls/Immirzi_1.2/j_1.0/CSV_format/Delta_4_ampls_Dl_max_25.csv'

def fetch():
    with urllib.request.urlopen(URL,timeout=30) as r: txt=r.read().decode()
    return [[float(x) for x in line.split()] for line in txt.splitlines() if line.strip()]

def linfit(x,y):
    n=len(x);mx=sum(x)/n;my=sum(y)/n;sxx=sum((z-mx)**2 for z in x);sxy=sum((x[i]-mx)*(y[i]-my) for i in range(n))
    b=sxy/sxx;a=my-b*mx;pred=[a+b*z for z in x];ssr=sum((y[i]-pred[i])**2 for i in range(n));sst=sum((z-my)**2 for z in y)
    return a,b,(1-ssr/sst if sst else 1.0)

def zeta_tail_em(N,p):
    # sum_{n=N}^infinity n^-p, Euler-Maclaurin through B4
    n=float(N)
    return n**(1-p)/(p-1)+0.5*n**(-p)+(p/12.0)*n**(-p-1)-p*(p+1)*(p+2)/720.0*n**(-p-3)

def estimate(vals,w):
    dif=[vals[i]-vals[i-1] for i in range(1,len(vals))]; idx=list(range(1,len(vals)))
    d=dif[-w:];ii=idx[-w:]
    if any(x==0 for x in d): return None
    signs=[1 if x>0 else -1 for x in d]
    stable=(min(signs)==max(signs));sgn=signs[-1]
    x=[math.log(float(i)) for i in ii];y=[math.log(abs(z)) for z in d];a,b,r2=linfit(x,y);p=-b;C=math.exp(a)
    if p<=1 or not stable:return {'window':w,'p':p,'r2':r2,'summable':False,'stable_sign':stable}
    D=len(vals)-1;tail=sgn*C*zeta_tail_em(D+1,p);ainf=vals[-1]+tail
    return {'window':w,'p':p,'r2':r2,'summable':True,'stable_sign':stable,'A_D':vals[-1],'tail_estimate':tail,'A_infinity_estimate':ainf,'relative_remaining_tail':abs(tail)/max(abs(ainf),1e-300)}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',default='results/eprl_power_tail_extrapolation.json');args=ap.parse_args();data=fetch();cols=list(zip(*data));outcols=[]
    for ci,col in enumerate(cols):
        fits=[estimate(list(col),w) for w in range(5,11)];good=[f for f in fits if f and f.get('summable')]
        limits=[f['A_infinity_estimate'] for f in good];tails=[f['relative_remaining_tail'] for f in good]
        med=statistics.median(limits) if limits else None
        spread=(max(limits)-min(limits))/max(abs(med),1e-300) if limits else None
        outcols.append({'column':ci,'Dl':len(col)-1,'fits':fits,'median_A_infinity_estimate':med,'model_spread_relative':spread,'median_relative_remaining_tail':statistics.median(tails) if tails else None,'max_relative_remaining_tail':max(tails) if tails else None})
    maxmed=max(c['median_relative_remaining_tail'] for c in outcols);maxspread=max(c['model_spread_relative'] for c in outcols)
    out={'dataset':'gamma=1.2,j=1.0,maxDl=25','columns':outcols,'max_median_relative_remaining_tail':maxmed,'max_fit_window_spread_relative':maxspread,
         'prototype_precision_2pct':maxmed<0.02 and maxspread<0.005,
         'quantitative_precision_1pct':maxmed<0.01 and maxspread<0.005,
         'verdict':'POWER_TAIL_EXTRAPOLATION_COMPLETE','scope':'model-based finite-tail extrapolation; not a rigorous error bound and not F9 evidence'}
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps({'verdict':out['verdict'],'max_tail':maxmed,'max_spread':maxspread,'prototype_2pct':out['prototype_precision_2pct'],'quantitative_1pct':out['quantitative_precision_1pct']},indent=2))
if __name__=='__main__':main()
