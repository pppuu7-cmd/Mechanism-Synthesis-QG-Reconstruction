#!/usr/bin/env python3
from __future__ import annotations
import importlib.util, math
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CORE=ROOT/'scripts/k5_34_orbit_physical_numerator_action_flux_audit.py'
spec=importlib.util.spec_from_file_location('k5_static_probe_core',CORE)
core=importlib.util.module_from_spec(spec); spec.loader.exec_module(core)

def lcm(a,b): return abs(a*b)//math.gcd(a,b) if a and b else 0

den=1; maxnum=0; nonzero=0
for mt,chs in core.MATCH_COEFF.items():
    for ch in chs:
        for x in ch:
            q=Fraction(x)
            if q:
                nonzero+=1; den=lcm(den,q.denominator); maxnum=max(maxnum,abs(q.numerator))
qden=1
for row in core.Q:
    for x in row:qden=lcm(qden,Fraction(x).denominator)
ann_den=1
for x in core.ANN_COEFF:ann_den=lcm(ann_den,Fraction(x).denominator)
print('MATCH_COEFF_COUNT=',len(core.MATCH_COEFF))
print('MATCH_NONZERO_SCALARS=',nonzero)
print('MATCH_DEN_LCM=',den)
print('MATCH_MAX_ABS_NUM=',maxnum)
print('Q_DEN_LCM=',qden)
print('ANN_DEN_LCM=',ann_den)
print('SOURCE_TERMS=',core.SOURCE_TERMS)
print('PSI_TERMS=',len(core.PSI_POLY))
print('ORBIT_COUNT=',len(core.orbit_reps()))
