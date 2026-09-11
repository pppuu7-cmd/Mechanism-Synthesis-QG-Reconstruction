#!/usr/bin/env python3
"""Fail-closed readiness gate for the *backend*, not for physical F9.

The gate asks whether one published Lorentzian EPRL configuration is numerically
stable enough to serve as the first target for a Toller-projector prototype.
Passing this gate grants zero F9/novelty credit; it only prevents us from adding
causal projectors on top of an obviously unconverged amplitude.
"""
from __future__ import annotations
import argparse,json,urllib.request
from pathlib import Path
U15='https://raw.githubusercontent.com/PietropaoloFrisoni/HowToSpinFoamAmplitude/master/Delta_4_ampls/Immirzi_1.2/j_1.0/CSV_format/Delta_4_ampls_Dl_max_15.csv'
U25='https://raw.githubusercontent.com/PietropaoloFrisoni/HowToSpinFoamAmplitude/master/Delta_4_ampls/Immirzi_1.2/j_1.0/CSV_format/Delta_4_ampls_Dl_max_25.csv'

def fetch(u):
 with urllib.request.urlopen(u,timeout=30) as r:txt=r.read().decode()
 return [[float(x) for x in l.split()] for l in txt.splitlines() if l.strip()]
def metrics(col):
 v=list(col);steps=[abs(v[i]-v[i-1])/max(abs(v[i]),1e-300) for i in range(1,len(v))];span=(max(v[-4:])-min(v[-4:]))/max(abs(v[-1]),1e-300)
 return {'last_step':steps[-1],'last4_span':span}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',default='results/eprl_backend_readiness_gate.json');args=ap.parse_args();a=fetch(U15);b=fetch(U25)
 prefix=(a==b[:len(a)]);mm=[metrics(c) for c in zip(*b)]
 checks={
  'published_prefix_reproducible':prefix,
  'all_columns_last_step_lt_0p2pct':all(x['last_step']<2e-3 for x in mm),
  'all_columns_last4_span_lt_0p5pct':all(x['last4_span']<5e-3 for x in mm),
  'at_least_25_shells_available':len(b)-1>=25,
 }
 passed=all(checks.values())
 out={'target':{'gamma':1.2,'j':1.0,'Dl':25,'reason':'deepest published same-configuration Lorentzian EPRL Delta4 series currently attached to this audit'},'metrics':mm,'checks':checks,'passed':passed,'verdict':'BACKEND_READY_FOR_CAUSAL_PROJECTOR_PROTOTYPE' if passed else 'BACKEND_NOT_READY','scientific_credit':'NONE_FOR_F9','next_object':'construct same-realization P_plus/P_minus and measure P_minus iota P_plus plus P_plus iota P_minus'}
 p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out,indent=2))
 # Fail closed only if the intended baseline is not ready.
 if not passed:raise SystemExit(2)
if __name__=='__main__':main()
