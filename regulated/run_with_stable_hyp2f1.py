#!/usr/bin/env python3
"""Run a diagnostic script with a robust 2F1 wrapper for integer c-a-b.

mpmath's 1-z continuation can enter an internal comparison path that attempts
to order an exactly-real complex number when c-a-b is an integer. Toller
matrix elements hit this case structurally. We keep the same analytic function:
first try the ordinary evaluator; on that internal TypeError, evaluate the
symmetric c -> c +/- delta limit at high precision and average the two sides.
"""
from __future__ import annotations

import runpy
import sys
from pathlib import Path

import mpmath as mp

_ORIG_HYP2F1 = mp.hyp2f1


def stable_hyp2f1(a, b, c, z, **kwargs):
    try:
        return _ORIG_HYP2F1(a, b, c, z, **kwargs)
    except TypeError as exc:
        if "no ordering relation is defined for complex numbers" not in str(exc):
            raise
        # At 80-90 dps, a 10^(-dps/2) perturbation is far below the requested
        # output accuracy while leaving ample guard digits for the removable
        # hypercomb degeneracy. Symmetric averaging cancels the O(delta) term.
        delta = mp.power(10, -(max(20, mp.mp.dps // 2)))
        kw = dict(kwargs)
        kw.setdefault("maxprec", max(1000, mp.mp.prec * 30))
        vp = _ORIG_HYP2F1(a, b, c + delta, z, **kw)
        vm = _ORIG_HYP2F1(a, b, c - delta, z, **kw)
        return (vp + vm) / 2


mp.hyp2f1 = stable_hyp2f1

if len(sys.argv) < 2:
    raise SystemExit("usage: run_with_stable_hyp2f1.py TARGET.py [args ...]")

target = Path(sys.argv[1]).resolve()
repo_root = target.parent.parent
sys.path.insert(0, str(repo_root))
sys.path.insert(0, str(target.parent))
sys.argv = [str(target)] + sys.argv[2:]
runpy.run_path(str(target), run_name="__main__")
