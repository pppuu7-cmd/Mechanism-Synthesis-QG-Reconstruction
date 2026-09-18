#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / "scripts/k5_34_orbit_exact_leading_coefficient_core_repair1.py"
CRITIC = ROOT / "results/raw/k5_full_source_boundary_s5_independent_critic_authoritative.json"
PRE = "7d22ea4e5af4c3143317734afe4fecffd704f2a2"
PASS = "K5_34_ORBIT_S5_MATCHING_LABEL_FRAME_COMMUTATION_IDENTIFIED_EXACT_SCOPED"
FAIL = "K5_34_ORBIT_S5_MATCHING_LABEL_FRAME_COMMUTATION_SIMPLE_FRAME_NO_GO_EXACT_SCOPED"
INVALID = "INVALID_IMPLEMENTATION"
BLOCKED = "BLOCKED_OBJECT_DEFINITION"


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


c = load(CORE, "k5_matching_frame_core")
critic = json.loads(CRITIC.read_text(encoding="utf-8"))


def canon_matching(mt):
    pairs = [tuple(sorted((int(i), int(j)))) for i, j in mt]
    return tuple(sorted(pairs))


def reindex_matching(mt, p):
    return canon_matching((c.s5.ep(p, i), c.s5.ep(p, j)) for i, j in mt)


def reindex_object(mc, p):
    out = {}
    for mt, coeff in mc.items():
        k = reindex_matching(mt, p)
        assert k not in out
        out[k] = coeff
    return out


def object_hash(mc):
    h = hashlib.sha256()
    for mt, coeffs in sorted(mc.items()):
        h.update((repr(mt) + "|").encode())
        for ch in coeffs:
            h.update((str(ch[0]) + "," + str(ch[1]) + ";").encode())
        h.update(b"\n")
    return h.hexdigest()


def exact_rational(mc):
    return all(isinstance(x, Fraction) for coeffs in mc.values() for ch in coeffs for x in ch)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    p = c.s5.C
    ip = c.s5.invperm(p)

    base_patterns, term_count = c.s5.aggregate_base_patterns()
    base_mc = c._project_pattern_dicts_to_match_coeff(base_patterns)

    transported_patterns = c.s5.transported_pattern_dicts(
        base_patterns,
        p,
        transpose_reversed=True,
        source_reversal_sign=True,
        covariance_orientation_sign=False,
    )
    source_mc = c._project_pattern_dicts_to_match_coeff(transported_patterns)

    candidates = {
        "identity": base_mc,
        "forward": reindex_object(base_mc, p),
        "inverse": reindex_object(base_mc, ip),
    }
    equality = {name: (obj == source_mc) for name, obj in candidates.items()}
    hits = [name for name, ok in equality.items() if ok]

    roundtrip = reindex_object(reindex_object(base_mc, p), ip) == base_mc
    edge_image = sorted(c.s5.ep(p, i) for i in range(10))
    base_reproduces_parent = base_mc == c.base.MATCH_COEFF

    formal = c.s5.formal_pattern_generator_check(
        base_patterns,
        c._LOCAL,
        p,
    )

    checks = {
        "prereg_locked": PRE == "7d22ea4e5af4c3143317734afe4fecffd704f2a2",
        "critic_confirmed_exact_scoped": critic.get("classification") == "CONFIRMED_EXACT_SCOPED",
        "critic_q18_unused": critic.get("q18_values_used") is False,
        "source_terms_100000": term_count == 100000,
        "base_collapse_reproduces_parent_matching_object": base_reproduces_parent,
        "parent_matching_count_945": len(base_mc) == 945,
        "source_transport_matching_count_945": len(source_mc) == 945,
        "edge_map_bijective_0_9": edge_image == list(range(10)),
        "forward_inverse_roundtrip_exact": roundtrip,
        "base_exact_rational": exact_rational(base_mc),
        "source_transport_exact_rational": exact_rational(source_mc),
        "formal_full_source_boundary_cycle_exact": bool(formal["exact"]),
        "formal_cycle_boundary_inverse_exact": bool(formal["boundary_inverse_exact"]),
        "formal_cycle_source_fixed_rejected": bool(formal["source_fixed_rejected"]),
    }

    execution_valid = all(checks.values())

    if not execution_valid:
        status = INVALID
        classification = INVALID
    elif len(hits) == 1:
        status = "PASS_EXACT_SCOPED"
        classification = PASS
    elif len(hits) == 0:
        status = "FAIL_EXACT_SCOPED"
        classification = FAIL
    else:
        status = BLOCKED
        classification = BLOCKED

    out = {
        "gate": "K5_34_ORBIT_S5_MATCHING_LABEL_FRAME_COMMUTATION_DIAGNOSTIC",
        "prereg_commit": PRE,
        "status": status,
        "classification": classification,
        "execution_valid": execution_valid,
        "checks": checks,
        "candidate_equalities": equality,
        "unique_hit": hits[0] if len(hits) == 1 else None,
        "hit_count": len(hits),
        "matching_counts": {
            "base": len(base_mc),
            "source_transport": len(source_mc),
        },
        "hashes": {
            "base": object_hash(base_mc),
            "source_transport": object_hash(source_mc),
            **{name: object_hash(obj) for name, obj in candidates.items()},
        },
        "scientific_NB_coefficients_consumed": False,
        "invalid_resolver_values_consumed": False,
        "physical_corner_verdict": None,
        "finite_part_selector": None,
        "regulator_independence": False,
    }

    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print("STATUS=" + status)
    print("CLASSIFICATION=" + classification)
    print("CANDIDATE_EQUALITIES=" + json.dumps(equality, sort_keys=True))
    print("UNIQUE_HIT=" + str(out["unique_hit"]))


if __name__ == "__main__":
    main()
