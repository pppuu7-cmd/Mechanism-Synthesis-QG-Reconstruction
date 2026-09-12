#!/usr/bin/env python3
"""Accelerated driver for Iteration 013 heavy endpoint diagnostics.

Physics is unchanged. We memoize repeated Toller and Wigner evaluations inside
magnetic recoupling sums. The precontracted scan keeps the complete 16-mask
physics grid. The expensive cutoff-only diagnostic uses one representative of
each four-leg branch Hamming class (0..4 plus signs), because its purpose is
only to expose regulator scaling rather than enumerate distinct vertex causal
patterns.
"""
from __future__ import annotations

import argparse
import json
from functools import lru_cache
from pathlib import Path

import mpmath as mp

from regulated import endpoint_precontraction_scan as ep

mp.mp.dps = 80

# Preserve originals before monkey-patching the module-level functions used by
# ep.precontracted and ep.precontracted_report.
_orig_tbranch = ep.tbranch
_orig_w4jm = ep.w4jm
_orig_allowed_p = ep.allowed_p


@lru_cache(maxsize=200000)
def _tbranch_cached(branch:int, tj:int, tl:int, tp:int, beta_key:str, gamma_key:str):
    old = ep.GAMMA
    ep.GAMMA = mp.mpf(gamma_key)
    try:
        return _orig_tbranch(branch, tj, tl, tp, mp.mpf(beta_key))
    finally:
        ep.GAMMA = old


def tbranch_cached(branch:int, tj:int, tl:int, tp:int, beta):
    return _tbranch_cached(branch, tj, tl, tp, mp.nstr(beta, 55), mp.nstr(ep.GAMMA, 40))


@lru_cache(maxsize=20000)
def w4jm_cached(tj1,tj2,tj3,tj4,tm1,tm2,tm3,tm4,ti):
    return _orig_w4jm(tj1,tj2,tj3,tj4,tm1,tm2,tm3,tm4,ti)


@lru_cache(maxsize=128)
def allowed_p_cached(tj):
    return tuple(_orig_allowed_p(tj))


ep.tbranch = tbranch_cached
ep.w4jm = w4jm_cached
ep.allowed_p = allowed_p_cached


def cfmt(z, n=18):
    return [mp.nstr(mp.re(z),n), mp.nstr(mp.im(z),n)]


def finite_complex(z):
    return bool(mp.isfinite(mp.re(z)) and mp.isfinite(mp.im(z)))


def cutoff_fast_report():
    # One mask per Hamming weight 0..4: ----, +---, ++--, +++-, ++++.
    masks=[0,1,3,7,15]
    rows=[]
    tl=1
    for ti,tk in ((0,0),(2,2)):
        for mask in masks:
            vals=[]
            for bmin in ep.CUTOFFS:
                f=lambda b,m=mask: ep.precontracted(m,1,tl,ti,tk,b)
                try:
                    val=mp.quad(f,[bmin,mp.mpf('0.5'),mp.mpf('1.5'),mp.mpf('4.0')])
                except Exception:
                    val=mp.mpc(mp.nan,mp.nan)
                vals.append(val)
            rows.append({
                'two_i':ti,'two_k':tk,'mask':mask,'hamming_weight':int(mask).bit_count(),
                'finite':all(finite_complex(v) for v in vals),
                'cutoff_values':[cfmt(v) for v in vals],
                'cutoff_magnitudes':[mp.nstr(abs(v),18) for v in vals],
            })
    return {
        'cutoffs':[mp.nstr(x,18) for x in ep.CUTOFFS],
        'beta_max':'4.0','representative_masks':masks,'rows':rows,
        'guardrail':'real-axis cutoff diagnostic only; not equivalent to the Feynman i-epsilon prescription',
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--mode', choices=['precontracted','cutoff-fast'], required=True)
    ap.add_argument('--output', required=True)
    args=ap.parse_args()
    report=ep.precontracted_report() if args.mode=='precontracted' else cutoff_fast_report()
    report.update({
        'mode':args.mode,'gamma':mp.nstr(ep.GAMMA,20),'mp_dps':mp.mp.dps,
        'cache_info':{
            'tbranch':str(_tbranch_cached.cache_info()),
            'w4jm':str(w4jm_cached.cache_info()),
            'allowed_p':str(allowed_p_cached.cache_info()),
        },
        'interpretation_guardrail':'Acceleration only; no change to Toller formula, recoupling convention, or causal prescription.'
    })
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(report,indent=2),encoding='utf-8')
    summary={k:v for k,v in report.items() if k not in ('rows',)}
    print(json.dumps(summary,indent=2))

if __name__=='__main__':
    main()
