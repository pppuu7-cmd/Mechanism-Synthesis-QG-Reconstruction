#!/usr/bin/env python3
"""Iter051B: preregistered exact residue-zero/cancellation structure audit for K4 RR."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import sympy as sp

from distributional.k4_forest_order_finite_part import (
    TREES,
    _linear_roots_of_denominator,
    build_kernel,
    finite_part_1d,
)
from distributional.k4_fp_channel_decomposition import (
    exact_equal,
    is_zero,
    ordered_channels,
)
from distributional.k4_denominator_pole_topology_control import (
    SIGMA_CLASSES,
    edge_signs_from_class,
)
from distributional.k4_rr_parameter_sensitivity import PAIRS

GAMMA = sp.Rational(178, 100)
EPSILON = sp.Rational(71, 1000)
KFLOW = (sp.Rational(11,100), sp.Rational(33,100), sp.Rational(-29,100), sp.Rational(-15,100))

FEATURES = (
    "first_upper_count_asymmetry",
    "second_upper_count_asymmetry",
    "first_nonzero_residue_count_asymmetry",
    "second_nonzero_residue_count_asymmetry",
    "first_residue_sum_zero_asymmetry",
    "second_residue_sum_zero_asymmetry",
    "internal_cancellation_asymmetry",
    "combined_discrete_residue_signature_asymmetry",
)


def residue_step(expr, var):
    """Return the unchanged R component plus prospectively frozen exact diagnostics."""
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
    if Prn.is_zero:
        a_minus1 = sp.Integer(0)
    elif dn == dd - 1:
        a_minus1 = sp.cancel(Prn.LC() / Prd.LC())
    elif dn < dd - 1:
        a_minus1 = sp.Integer(0)
    else:
        raise RuntimeError(f"improper remainder after division: deg(num)={dn}, deg(den)={dd}")

    roots = _linear_roots_of_denominator(Prd.as_expr(), var)
    Dprime = sp.diff(Prd.as_expr(), var)
    Nexpr = Prn.as_expr()
    selected = []
    for root, imr in roots:
        sign = float(sp.N(imr, 30))
        if abs(sign) < 1e-14:
            raise RuntimeError(f"unexpected real-axis pole: {root}")
        if sign > 0:
            residue = sp.cancel(Nexpr.subs(var, root) / Dprime.subs(var, root))
            selected.append(residue)

    residue_sum = sp.cancel(sum(selected, sp.Integer(0)))
    Rcomp = sp.cancel(2 * sp.pi * sp.I * residue_sum)
    Acomp = sp.cancel(-sp.pi * sp.I * a_minus1)
    frozen, _ = finite_part_1d(expr, var)
    recombination_exact = exact_equal(sp.cancel(Rcomp + Acomp), frozen)
    nonzero_count = sum(not is_zero(r) for r in selected)
    sum_zero = bool(is_zero(residue_sum))
    internal_cancellation = bool(nonzero_count > 0 and sum_zero)
    qdeg = -1 if Q.is_zero else int(Q.degree())

    return {
        "R": Rcomp,
        "A": Acomp,
        "recombination_exact": bool(recombination_exact),
        "meta": {
            "quotient_degree": qdeg,
            "pole_count": len(roots),
            "upper_pole_count": len(selected),
            "nonzero_upper_residue_count": int(nonzero_count),
            "residue_sum_zero": sum_zero,
            "internal_cancellation": internal_cancellation,
        },
    }


def path_signature(first, second):
    f, s = first["meta"], second["meta"]
    return (
        f["pole_count"], f["upper_pole_count"], f["nonzero_upper_residue_count"],
        f["residue_sum_zero"], f["internal_cancellation"],
        s["pole_count"], s["upper_pole_count"], s["nonzero_upper_residue_count"],
        s["residue_sum_zero"], s["internal_cancellation"],
    )


def residue_paths(expr, y, pair):
    i, j = map(int, pair)
    ij_f = residue_step(expr, y[i])
    ij_s = residue_step(ij_f["R"], y[j])
    ji_f = residue_step(expr, y[j])
    ji_s = residue_step(ji_f["R"], y[i])

    frozen_ij = ordered_channels(expr, y, i, j)
    frozen_ji = ordered_channels(expr, y, j, i)
    rr_ij_exact = exact_equal(ij_s["R"], frozen_ij["channels"]["RR"])
    rr_ji_exact = exact_equal(ji_s["R"], frozen_ji["channels"]["RR"])
    rr_delta = sp.cancel(ij_s["R"] - ji_s["R"])

    fim = ij_f["meta"]; sim = ij_s["meta"]
    fjm = ji_f["meta"]; sjm = ji_s["meta"]
    features = {
        "first_upper_count_asymmetry": fim["upper_pole_count"] != fjm["upper_pole_count"],
        "second_upper_count_asymmetry": sim["upper_pole_count"] != sjm["upper_pole_count"],
        "first_nonzero_residue_count_asymmetry": fim["nonzero_upper_residue_count"] != fjm["nonzero_upper_residue_count"],
        "second_nonzero_residue_count_asymmetry": sim["nonzero_upper_residue_count"] != sjm["nonzero_upper_residue_count"],
        "first_residue_sum_zero_asymmetry": fim["residue_sum_zero"] != fjm["residue_sum_zero"],
        "second_residue_sum_zero_asymmetry": sim["residue_sum_zero"] != sjm["residue_sum_zero"],
        "internal_cancellation_asymmetry": (
            (fim["internal_cancellation"], sim["internal_cancellation"]) !=
            (fjm["internal_cancellation"], sjm["internal_cancellation"])
        ),
        "combined_discrete_residue_signature_asymmetry": path_signature(ij_f, ij_s) != path_signature(ji_f, ji_s),
    }
    valid = all([
        ij_f["recombination_exact"], ij_s["recombination_exact"],
        ji_f["recombination_exact"], ji_s["recombination_exact"],
        frozen_ij["ordered_reconstruction"], frozen_ji["ordered_reconstruction"],
        frozen_ij["all_component_matches"], frozen_ji["all_component_matches"],
        rr_ij_exact, rr_ji_exact,
    ])
    return {
        "valid": bool(valid),
        "rr_nonzero": bool(not is_zero(rr_delta)),
        "rr_ij_matches_frozen": bool(rr_ij_exact),
        "rr_ji_matches_frozen": bool(rr_ji_exact),
        "ij": {"first": ij_f["meta"], "second": ij_s["meta"]},
        "ji": {"first": ji_f["meta"], "second": ji_s["meta"]},
        "features": {k: bool(v) for k, v in features.items()},
    }


def compute(args):
    if args.sign_class not in SIGMA_CLASSES:
        raise ValueError(args.sign_class)
    if args.tree not in TREES:
        raise ValueError(args.tree)
    if args.pair not in PAIRS:
        raise ValueError(args.pair)

    sigma, edge_signs, edge_text = edge_signs_from_class(args.sign_class)
    y, source_expr, source_meta = build_kernel(GAMMA, EPSILON, edge_signs, KFLOW, args.tree, control=False)
    cy, control_expr, control_meta = build_kernel(GAMMA, EPSILON, edge_signs, KFLOW, args.tree, control=True)
    source = residue_paths(source_expr, y, args.pair)
    control = residue_paths(control_expr, cy, args.pair)
    factorized_check = all(
        edge_signs[idx] == sigma[a] * sigma[b]
        for idx, (a,b) in enumerate(((0,1),(0,2),(0,3),(1,2),(1,3),(2,3)))
    )
    valid = source["valid"] and control["valid"] and (not control["rr_nonzero"]) and factorized_check
    return {
        "iteration": "Iter051B",
        "gamma": str(GAMMA),
        "epsilon": str(EPSILON),
        "k": list(map(str, KFLOW)),
        "sign_class": args.sign_class,
        "sigma": list(map(int, sigma)),
        "edge_signs": edge_text,
        "tree": args.tree,
        "pair": args.pair,
        "valid": bool(valid),
        "factorized_sign_check": bool(factorized_check),
        "source": source,
        "control": control,
        "source_kernel_meta": source_meta,
        "control_kernel_meta": control_meta,
        "claim_lock": (
            "Preregistered exact residue-zero/cancellation audit of the sequential RR diagnostic only; "
            "no fitted selector, physical amplitude, K5, G3, F9 or G8 claim."
        ),
    }


def aggregate(input_dir: Path):
    rows = []
    for p in sorted(input_dir.rglob("iter051b_*.json")):
        try:
            r = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        if r.get("iteration") == "Iter051B" and "source" in r:
            rows.append(r)
    expected = len(SIGMA_CLASSES) * len(TREES) * len(PAIRS)
    if len(rows) != expected:
        raise RuntimeError(f"expected {expected} Iter051B lanes, found {len(rows)}")
    keys = {(r["sign_class"], r["tree"], r["pair"]) for r in rows}
    if len(keys) != expected:
        raise RuntimeError("duplicate/missing Iter051B matrix keys")

    all_valid = all(r["valid"] for r in rows)
    all_controls_rr_zero = all(not r["control"]["rr_nonzero"] for r in rows)
    all_factorized = all(r["factorized_sign_check"] for r in rows)
    rr_values = [bool(r["source"]["rr_nonzero"]) for r in rows]
    rr_nontrivial = any(rr_values) and not all(rr_values)

    feature_results = {}
    exact_matches = []
    for feature in FEATURES:
        contingency = {"rr1_f1":0, "rr1_f0":0, "rr0_f1":0, "rr0_f0":0}
        values = []
        for r in rows:
            rr = bool(r["source"]["rr_nonzero"])
            fv = bool(r["source"]["features"][feature])
            values.append(fv)
            contingency[f"rr{int(rr)}_f{int(fv)}"] += 1
        exact = all(rr == fv for rr, fv in zip(rr_values, values)) and any(values) and not all(values)
        if exact:
            exact_matches.append(feature)
        feature_results[feature] = {
            "contingency": contingency,
            "true_count": sum(values),
            "exact_match": bool(exact),
        }

    if not (all_valid and all_controls_rr_zero and all_factorized and rr_nontrivial):
        classification = "ITER051B_CONTROL_OR_RECONSTRUCTION_INVALID"
    elif exact_matches:
        classification = "K4_RR_PREREG_RESIDUE_STRUCTURE_EXACT"
    else:
        classification = "K4_RR_BEYOND_PREREG_RESIDUE_STRUCTURE"

    class_summary = {}
    for sc in SIGMA_CLASSES:
        sr = [r for r in rows if r["sign_class"] == sc]
        class_summary[sc] = {
            "rr_nonzero_count": sum(r["source"]["rr_nonzero"] for r in sr),
            "rr_positions": [f"{r['tree']}/{r['pair']}" for r in sr if r["source"]["rr_nonzero"]],
        }

    return {
        "iteration": "Iter051B",
        "lane_count": len(rows),
        "classification": classification,
        "all_lanes_valid": bool(all_valid),
        "all_control_rr_commutators_zero": bool(all_controls_rr_zero),
        "all_factorized_sign_checks": bool(all_factorized),
        "source_rr_nontrivial": bool(rr_nontrivial),
        "source_rr_nonzero_count": sum(rr_values),
        "exact_matching_diagnostics": exact_matches,
        "feature_results": feature_results,
        "class_summary": class_summary,
        "claim_lock": (
            "Residue-zero/cancellation structure audit only. No physical multivariate amplitude, "
            "K5, G3, F9 or G8 promotion."
        ),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["compute", "aggregate"], default="compute")
    ap.add_argument("--sign-class", choices=SIGMA_CLASSES)
    ap.add_argument("--tree", choices=sorted(TREES))
    ap.add_argument("--pair", choices=PAIRS)
    ap.add_argument("--input-dir", default="results")
    ap.add_argument("--output", required=True)
    a = ap.parse_args()
    if a.mode == "compute":
        if any(v is None for v in (a.sign_class, a.tree, a.pair)):
            raise SystemExit("compute requires --sign-class --tree --pair")
        out = compute(a)
    else:
        out = aggregate(Path(a.input_dir))
    p = Path(a.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
