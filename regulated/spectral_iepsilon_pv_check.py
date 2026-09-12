#!/usr/bin/env python3
"""Numerical check of the published Feynman i-epsilon definition of Toller T.

For a pure boost, Eq. (3) of Bianchi-Chen-Gamonal gives

  T+ = 1/2 D(rho) + (1/(2 pi i)) PV integral d rtilde F(rtilde)/(rtilde-rho)
  T- = 1/2 D(rho) - (1/(2 pi i)) PV integral d rtilde F(rtilde)/(rtilde-rho)

with the gamma-ratio kernel F. We evaluate the PV symmetrically around rho,
so the singularity cancels algebraically:

  PV[-R,R] = integral_0^R [F(rho+s)-F(rho-s)]/s ds.

The Wigner D inside the spectral integral is reconstructed pointwise as T+ + T-
from the already validated reduced-Toller closed forms. Therefore this is a
consistency test of the spectral/Plemelj implementation and regulator handling,
not an independent derivation of the closed-form Toller functions.
"""
from __future__ import annotations

import argparse
import json
from functools import lru_cache
from pathlib import Path

import mpmath as mp

from regulated import endpoint_precontraction_scan as ep

mp.mp.dps = 60


def cfmt(z, n=22):
    return [mp.nstr(mp.re(z), n), mp.nstr(mp.im(z), n)]


def rfmt(x, n=22):
    return mp.nstr(x, n)


def relerr(a, b):
    return abs(a-b) / max(abs(b), mp.mpf('1e-50'))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--gamma', required=True)
    ap.add_argument('--two-l', type=int, required=True)
    ap.add_argument('--two-p', type=int, default=1)
    ap.add_argument('--beta', default='0.7')
    ap.add_argument('--output', required=True)
    args = ap.parse_args()

    tj = 1
    tl = args.two_l
    tp = args.two_p
    tk = tj
    j = mp.mpf(tj)/2
    l = mp.mpf(tl)/2
    gamma = mp.mpf(args.gamma)
    rho = gamma*j
    beta = mp.mpf(args.beta)

    # Closed-form targets.
    tplus_target = ep.toller_plus(tj, tl, tp, tk, rho, beta)
    tminus_target = ep.toller_minus(tj, tl, tp, tk, rho, beta)
    d_target = tplus_target + tminus_target

    gconst = mp.gamma(-j-1j*rho) / mp.gamma(l-1j*rho+1)

    @lru_cache(maxsize=20000)
    def D_of_key(key: str):
        rr = mp.mpf(key)
        return (ep.toller_plus(tj,tl,tp,tk,rr,beta)
                + ep.toller_minus(tj,tl,tp,tk,rr,beta))

    def D_of(rr):
        # Stable decimal cache key at more digits than requested output.
        return D_of_key(mp.nstr(rr, 45))

    def F(rr):
        ratio = gconst * mp.gamma(l-1j*rr+1) / mp.gamma(-j-1j*rr)
        return ratio * D_of(rr)

    f0 = F(rho)
    kernel_identity_error = relerr(f0, d_target)

    def pv_integrand(s):
        if abs(s) < mp.mpf('1e-30'):
            # Symmetric derivative limit; mp.diff avoids evaluating 0/0.
            return 2*mp.diff(F, rho)
        return (F(rho+s)-F(rho-s))/s

    cutoffs = [mp.mpf(x) for x in ('1.5','3.0','5.0','8.0')]
    rows=[]
    previous_plus = None
    for R in cutoffs:
        # Split the interval to help adaptive quadrature follow oscillatory tails.
        knots=[mp.mpf('0'), mp.mpf('0.25'), mp.mpf('0.75'), mp.mpf('1.5')]
        knots=[x for x in knots if x<R]
        if not knots or knots[0] != 0: knots=[mp.mpf('0')]+knots
        if knots[-1] != R: knots.append(R)
        pv = mp.quad(pv_integrand, knots)
        plus = d_target/2 + pv/(2*mp.pi*1j)
        minus = d_target/2 - pv/(2*mp.pi*1j)
        rows.append({
            'R': rfmt(R),
            'pv_integral': cfmt(pv),
            'Tplus_spectral': cfmt(plus),
            'Tminus_spectral': cfmt(minus),
            'Tplus_relative_error': rfmt(relerr(plus,tplus_target)),
            'Tminus_relative_error': rfmt(relerr(minus,tminus_target)),
            'additive_identity_relative_error': rfmt(relerr(plus+minus,d_target)),
            'successive_Tplus_change': None if previous_plus is None else rfmt(relerr(plus,previous_plus)),
        })
        previous_plus = plus

    out={
        'gamma': str(args.gamma), 'two_j':tj, 'two_l':tl, 'two_p':tp,
        'beta':str(args.beta), 'rho':rfmt(rho), 'mp_dps':mp.mp.dps,
        'closed_form':{
            'Tplus':cfmt(tplus_target),'Tminus':cfmt(tminus_target),'D':cfmt(d_target),
        },
        'kernel_at_pole_relative_error':rfmt(kernel_identity_error),
        'rows':rows,
        'best_cutoff_relative_error_plus':rows[-1]['Tplus_relative_error'],
        'best_cutoff_relative_error_minus':rows[-1]['Tminus_relative_error'],
        'interpretation_guardrail':(
            'Finite symmetric rho cutoffs test convergence of the published PV/Plemelj representation. '
            'D inside the integral is reconstructed from T+ + T-, so this validates the spectral implementation '
            'and regulator handling, not the closed-form Toller formula independently. No causal-vertex/F9 credit.'
        )
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k not in ('rows','closed_form')},indent=2))

if __name__=='__main__':
    main()
