#!/usr/bin/env python3
"""Infrastructure-only repair for Iter046 Case B.

The frozen Iter046 operator can return an exactly zero proper remainder in the
EPRL/no-contact control for mixed causal signs. SymPy represents the degree of
the zero polynomial as -oo; the production script attempted int(-oo) only for
metadata serialization and failed after the mathematical result was already
zero. This wrapper replaces only that metadata conversion with sentinel -1.
No pole, contour, subtraction, source kernel, parameter, or acceptance rule is
changed.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sympy as sp
import distributional.k4_forest_order_finite_part as base


def repaired_finite_part_1d(expr, var):
    expr = sp.cancel(expr)
    num, den = sp.fraction(expr)
    Pn = sp.Poly(num, var, domain="EX")
    Pd = sp.Poly(den, var, domain="EX")
    Q, R = sp.div(Pn, Pd)
    rem = sp.cancel(R.as_expr() / Pd.as_expr())

    rn, rd = sp.fraction(rem)
    Prn = sp.Poly(rn, var, domain="EX")
    Prd = sp.Poly(rd, var, domain="EX")
    dn, dd = Prn.degree(), Prd.degree()

    if dn is sp.S.NegativeInfinity or dn == -sp.oo:
        a_minus1 = sp.Integer(0)
        dn_meta = -1
    else:
        dn_meta = int(dn)
        if dn == dd - 1:
            a_minus1 = sp.cancel(Prn.LC() / Prd.LC())
        elif dn < dd - 1:
            a_minus1 = sp.Integer(0)
        else:
            raise RuntimeError(f"improper remainder after division: deg(num)={dn}, deg(den)={dd}")

    roots = base._linear_roots_of_denominator(Prd.as_expr(), var)
    Dprime = sp.diff(Prd.as_expr(), var)
    Nexpr = Prn.as_expr()
    residue_sum = sp.Integer(0)
    upper_count = 0
    for root, imr in roots:
        sign = float(sp.N(imr, 30))
        if abs(sign) < 1e-14:
            raise RuntimeError(f"unexpected real-axis pole: {root}")
        if sign > 0:
            residue = sp.cancel(Nexpr.subs(var, root) / Dprime.subs(var, root))
            residue_sum += residue
            upper_count += 1

    out = sp.cancel(2 * sp.pi * sp.I * residue_sum - sp.pi * sp.I * a_minus1)
    qdeg = -1 if Q.is_zero else int(Q.degree())
    return out, {
        "quotient_degree": qdeg,
        "remainder_num_degree": dn_meta,
        "remainder_den_degree": int(dd),
        "upper_pole_count": upper_count,
        "pole_count": len(roots),
        "zero_remainder_metadata_repair": dn_meta == -1,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tree", choices=sorted(base.TREES), required=True)
    ap.add_argument("--order", choices=base.ORDERS, required=True)
    ap.add_argument("--output", required=True)
    a = ap.parse_args()

    base.finite_part_1d = repaired_finite_part_1d
    ns = argparse.Namespace(
        case="B",
        gamma="1.43",
        epsilon="0.12",
        signs="-++-++",
        k="-0.22,0.37,-0.28,0.13",
        tree=a.tree,
        order=a.order,
    )
    out = base.compute(ns)
    out["repair"] = {
        "scope": "infrastructure_only",
        "defect": "SymPy zero-polynomial degree -oo could not be converted to int for metadata",
        "change": "serialize zero remainder numerator degree as -1",
        "frozen_science_changed": False,
    }
    p = Path(a.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
