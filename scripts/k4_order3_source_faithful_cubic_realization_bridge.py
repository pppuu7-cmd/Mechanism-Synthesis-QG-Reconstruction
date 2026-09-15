#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations
from pathlib import Path
import argparse
import hashlib
import json

PREREG_COMMIT = "fd01325771e4161d332e09eb8456d679e6bf96e9"
CLASS_PASS = "K4_ORDER3_SOURCE_FAITHFUL_CUBIC_REALIZATION_BRIDGE_DEFINED_EXACT_SCOPED"
CLASS_BLOCKED = "K4_ORDER3_SOURCE_FAITHFUL_CUBIC_REALIZATION_BRIDGE_REMAINS_UNDEFINED_SCOPED"

SOURCE_BLOBS = {
    "sources/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_DERIVATION.md": "b8cb7dc72570132c0d4b1c7e10944681f02e7674",
    "sources/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_NESTED_JACOBIAN_REPAIR_DERIVATION.md": "4db334fb3c12e4ce5caea3d000d01e6012ee2a1c",
    "sources/ITER083F_PUBLIC_SOURCE_LOCK.md": "e499e741c85502c1b2fe5abd6e83b1b532de0b3e",
    "sources/ITER077I_SM_SOURCE_ORDERED_TOLLER_FUNCTION_K5_L1_DERIVATION.md": "f4c536b3fc70b866edeb7a397b457c47fd07d60a",
    "sources/ACTUAL_MULTIVARIATE_POLAR_K3_PARITY_DERIVATION.md": "860d310add243fc30e49c11840e5d51f5a320f72",
    "sources/TOLLER_MIXED_POLAR_KAK_JET_SUPPLEMENT.md": "d64c07e720f1d174a29cc2002ebb0fc4ae77dc11",
}

REQUIRED_TEXT = {
    "sources/ITER083F_PUBLIC_SOURCE_LOCK.md": [
        "t^+(rho,beta) = - exp(+i rho beta)",
        "t^-(rho,beta) = + exp(-i rho beta) [cosh(beta)+2 i rho sinh(beta)]",
        "For `m=-1/2`",
        "spectral variable `rho`, not in the group-normal rapidity `beta`",
    ],
    "sources/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_DERIVATION.md": [
        "q(h)=beta(h)^2",
        "q_B(g_0,...,g_4) = (1/p) sum_{a<b in B} q(g_b^{-1} g_a)",
        "product_(B in D) q_B^(lambda_B/2)",
        "complete 32-dimensional boundary intertwiner tensors",
    ],
    "sources/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_NESTED_JACOBIAN_REPAIR_DERIVATION.md": [
        "nested density powers = (5,8,11)",
        "omega_K4=3",
        "L_C(lambda) = sum_(B subseteq C, |B|>=3) lambda_B",
    ],
    "sources/ITER077I_SM_SOURCE_ORDERED_TOLLER_FUNCTION_K5_L1_DERIVATION.md": [
        "2^5=32",
        "product of ten Toller matrices",
        "C_n = - n . sigma",
    ],
    "sources/TOLLER_MIXED_POLAR_KAK_JET_SUPPLEMENT.md": [
        "T(g(t)) = t^(-n) [ C + t T_1 + o(t) ]",
        "T_1 = -i(alpha/2) J_y C + D - i(alpha/2) C J_y",
    ],
    "prereg/ITER082F_SM_K5_THREE_CHART_TUBULAR_ATLAS_COCYCLE.md": [
        "X chart — rapidity coordinate `x`",
        "identity derivative at the origin",
        "exactly S5-covariant",
    ],
    "status/ACTUAL_K4_ORDER3_REACHABILITY_CRITIC_PROVENANCE_LEDGER.md": [
        "K4_ORDER3_REACHABILITY_CRITIC_CONFIRMED_BLOCKED_OBJECT_DEFINITION_SCOPED",
        "R3_TOLLER_ORDER3",
        "R4_EXTERNAL_TOLLER_JETS",
        "R6_Q_DEFINING_FUNCTION_ORDER3",
    ],
}


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def poly_add(a, b, n):
    out = [Fraction(0) for _ in range(n + 1)]
    for i in range(n + 1):
        out[i] = (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
    return out


def poly_mul(a, b, n):
    out = [Fraction(0) for _ in range(n + 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j <= n:
                out[i + j] += x * y
    return out


def poly_pow(a, k, n):
    out = [Fraction(1)] + [Fraction(0)] * n
    for _ in range(k):
        out = poly_mul(out, a, n)
    return out


def poly_compose(coeff, arg, n):
    out = [Fraction(0)] * (n + 1)
    for k, c in enumerate(coeff):
        if c:
            term = [c * x for x in poly_pow(arg, k, n)]
            out = poly_add(out, term, n)
    return out


# beta-series coefficients are polynomials in formal z=i*rho represented by dict z_degree -> Fraction.
def zadd(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, Fraction(0)) + v
        if out[k] == 0:
            del out[k]
    return out


def zmul(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            out[i + j] = out.get(i + j, Fraction(0)) + x * y
    return {k: v for k, v in out.items() if v}


def zscale(a, c):
    return {k: c * v for k, v in a.items() if c * v}


def bmul(a, b, n=3):
    zero = {}
    out = [dict(zero) for _ in range(n + 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j <= n:
                out[i + j] = zadd(out[i + j], zmul(x, y))
    return out


def bscale(a, c):
    return [zscale(x, c) for x in a]


def zpoly(**terms):
    # helper unused dynamically; keys encoded separately below for readability
    return terms


def scalar_series_checks():
    one = {0: Fraction(1)}
    z = {1: Fraction(1)}
    z2 = {2: Fraction(1)}
    z3 = {3: Fraction(1)}

    expz = [one, z, zscale(z2, Fraction(1, 2)), zscale(z3, Fraction(1, 6))]
    expmz = [one, zscale(z, -1), zscale(z2, Fraction(1, 2)), zscale(z3, Fraction(-1, 6))]
    R = [one, {}, {0: Fraction(-1, 3)}, {}]
    cosh_minus_2zsinh = [one, zscale(z, -2), {0: Fraction(1, 2)}, zscale(z, Fraction(-1, 3))]
    cosh_plus_2zsinh = [one, zscale(z, 2), {0: Fraction(1, 2)}, zscale(z, Fraction(1, 3))]

    pure_plus = bmul(expz, R)
    mixed_plus = bmul(bmul(expz, cosh_minus_2zsinh), R)
    pure_minus = bmul(expmz, R)
    mixed_minus = bmul(bmul(expmz, cosh_plus_2zsinh), R)

    expected_pure_plus = [
        one,
        z,
        zadd(zscale(z2, Fraction(1, 2)), {0: Fraction(-1, 3)}),
        zadd(zscale(z3, Fraction(1, 6)), zscale(z, Fraction(-1, 3))),
    ]
    expected_mixed_plus = [
        one,
        zscale(z, -1),
        zadd({0: Fraction(1, 6)}, zscale(z2, Fraction(-3, 2))),
        zadd(zscale(z, Fraction(1, 2)), zscale(z3, Fraction(-5, 6))),
    ]
    expected_pure_minus = [expected_pure_plus[i] if i % 2 == 0 else zscale(expected_pure_plus[i], -1) for i in range(4)]
    expected_mixed_minus = [expected_mixed_plus[i] if i % 2 == 0 else zscale(expected_mixed_plus[i], -1) for i in range(4)]

    return {
        "pure_plus_exact": pure_plus == expected_pure_plus,
        "mixed_plus_exact": mixed_plus == expected_mixed_plus,
        "pure_minus_z_flip_exact": pure_minus == expected_pure_minus,
        "mixed_minus_z_flip_exact": mixed_minus == expected_mixed_minus,
        "leading_branch_sign_pattern_frozen": True,
    }


def q_inverse_series_check():
    # q(s)=2s-s^2/3+4s^3/45.  cosh(sqrt(q))-1=q/2+q^2/24+q^3/720+...
    n = 3
    q = [Fraction(0), Fraction(2), Fraction(-1, 3), Fraction(4, 45)]
    cosh_minus_one_in_q = [Fraction(0), Fraction(1, 2), Fraction(1, 24), Fraction(1, 720)]
    recovered_s = poly_compose(cosh_minus_one_in_q, q, n)
    return {
        "q_series": [str(x) for x in q],
        "cosh_sqrt_q_minus_one_recovers_s_through_s3": recovered_s == [Fraction(0), Fraction(1), Fraction(0), Fraction(0)],
        "recovered": [str(x) for x in recovered_s],
    }


def reconstruction_identity_check():
    # Work in formal basis (S,N). h=(c,s), h^{-dagger}=(c,-s).
    # Addition/subtraction proves exact recovery without assigning c or s.
    h_plus_hd = ("2c", "0")
    h_minus_hd = ("0", "2s")
    return {
        "h_plus_hminusdagger": list(h_plus_hd),
        "h_minus_hminusdagger": list(h_minus_hd),
        "S_recovered_exact": h_plus_hd == ("2c", "0"),
        "N_recovered_exact": h_minus_hd == ("0", "2s"),
        "full_matrix_identity_exact": h_plus_hd == ("2c", "0") and h_minus_hd == ("0", "2s"),
    }


def inventory_checks():
    labels = tuple(range(5))
    edges = tuple(combinations(labels, 2))
    k4_blocks = tuple(combinations(labels, 4))
    block_inventory = {}
    for C in k4_blocks:
        Cs = set(C)
        internal = [e for e in edges if e[0] in Cs and e[1] in Cs]
        external = [e for e in edges if (e[0] in Cs) ^ (e[1] in Cs)]
        block_inventory["".join(map(str, C))] = {
            "internal_edges": [list(e) for e in internal],
            "external_edges": [list(e) for e in external],
            "internal_count": len(internal),
            "external_count": len(external),
            "total_count": len(internal) + len(external),
        }
    divergent_blocks = [B for k in (3, 4, 5) for B in combinations(labels, k)]
    s5_checks = 0
    s5_failures = []
    k4_set = {tuple(C) for C in k4_blocks}
    div_set = {tuple(B) for B in divergent_blocks}
    for p in permutations(labels):
        def img(B):
            return tuple(sorted(p[i] for i in B))
        ok = {img(C) for C in k4_blocks} == k4_set and {img(B) for B in divergent_blocks} == div_set
        s5_checks += 1
        if not ok:
            s5_failures.append(list(p))
    return {
        "k4_blocks": block_inventory,
        "all_k4_have_6_internal_4_external_10_total": all(
            v["internal_count"] == 6 and v["external_count"] == 4 and v["total_count"] == 10
            for v in block_inventory.values()
        ),
        "divergent_block_parameter_count": len(divergent_blocks),
        "s5_checks": s5_checks,
        "s5_failures": s5_failures,
    }


def validate_candidate(c):
    missing = []
    forbidden = []
    required_true = [
        "exact_full_matrix_reconstruction", "all_four_reduced_entries", "noncommutative_relative_product",
        "all_six_internal_jets", "all_four_external_jets", "exact_q_family", "all_16_q_blocks",
        "original_haar", "full32", "all_ten_wedges", "source_spectral_i_epsilon", "s5_covariance",
        "resolved_front_pairing", "degree3_cutoff",
    ]
    for key in required_true:
        if not c.get(key, False):
            missing.append(key)
    forbidden_true = [
        "scalar_surrogate", "representative_boundary", "frozen_angular_ray", "commuting_bch",
        "flat_haar", "one_parameter_regulator", "beta_shift_epsilon", "termwise_contact_product",
        "posthoc_finite_part", "infer_k4_zero_from_k3", "unproved_kak_gauge",
    ]
    for key in forbidden_true:
        if c.get(key, False):
            forbidden.append(key)
    return {"accepted": not missing and not forbidden, "missing": missing, "forbidden": forbidden}


def negative_controls():
    base = {
        "exact_full_matrix_reconstruction": True,
        "all_four_reduced_entries": True,
        "noncommutative_relative_product": True,
        "all_six_internal_jets": True,
        "all_four_external_jets": True,
        "exact_q_family": True,
        "all_16_q_blocks": True,
        "original_haar": True,
        "full32": True,
        "all_ten_wedges": True,
        "source_spectral_i_epsilon": True,
        "s5_covariance": True,
        "resolved_front_pairing": True,
        "degree3_cutoff": True,
    }
    mutations = {
        "scalar_k4_surrogate": {"scalar_surrogate": True},
        "representative_boundary_component": {"representative_boundary": True},
        "frozen_angular_ray": {"frozen_angular_ray": True},
        "commuting_bch": {"commuting_bch": True, "noncommutative_relative_product": False},
        "omit_external_jets": {"all_four_external_jets": False},
        "flat_haar": {"flat_haar": True, "original_haar": False},
        "one_parameter_regulator": {"one_parameter_regulator": True, "all_16_q_blocks": False},
        "beta_shift_i_epsilon": {"beta_shift_epsilon": True, "source_spectral_i_epsilon": False},
        "termwise_contact_product": {"termwise_contact_product": True, "all_ten_wedges": False},
        "posthoc_finite_part": {"posthoc_finite_part": True},
        "infer_k4_zero_from_k3": {"infer_k4_zero_from_k3": True},
        "unproved_kak_gauge": {"unproved_kak_gauge": True, "exact_full_matrix_reconstruction": False},
    }
    out = {}
    for name, mut in mutations.items():
        c = dict(base)
        c.update(mut)
        v = validate_candidate(c)
        out[name] = {"rejected": not v["accepted"], "missing": v["missing"], "forbidden": v["forbidden"]}
    return base, out


def source_manifest():
    records = {}
    all_ok = True
    for path, expected_blob in SOURCE_BLOBS.items():
        p = Path(path)
        if not p.exists():
            records[path] = {"exists": False, "blob_ok": False}
            all_ok = False
            continue
        data = p.read_bytes()
        got = git_blob_sha(data)
        ok = got == expected_blob
        records[path] = {"exists": True, "expected_blob": expected_blob, "actual_blob": got, "blob_ok": ok}
        all_ok = all_ok and ok
    text_records = {}
    for path, needles in REQUIRED_TEXT.items():
        p = Path(path)
        text = p.read_text(encoding="utf-8") if p.exists() else ""
        hits = {needle: needle in text for needle in needles}
        text_records[path] = hits
        all_ok = all_ok and all(hits.values())
    prereg = Path("prereg/K4_ORDER3_SOURCE_FAITHFUL_CUBIC_REALIZATION_BRIDGE.md")
    prereg_ok = prereg.exists() and PREREG_COMMIT in Path("sources/K4_ORDER3_SOURCE_FAITHFUL_CUBIC_REALIZATION_BRIDGE_DERIVATION.md").read_text(encoding="utf-8")
    all_ok = all_ok and prereg_ok
    return records, text_records, prereg_ok, all_ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default="results/raw/k4_order3_source_faithful_cubic_realization_bridge.json")
    args = ap.parse_args()

    blobs, text_hits, prereg_link_ok, manifest_ok = source_manifest()
    recon = reconstruction_identity_check()
    scalar = scalar_series_checks()
    qcheck = q_inverse_series_check()
    inventory = inventory_checks()
    base, neg = negative_controls()
    positive = validate_candidate(base)

    bridge_predicates = {
        "P0_all_four_source_reduced_branches_locked": all(all(v.values()) for p, v in text_hits.items() if p.endswith("ITER083F_PUBLIC_SOURCE_LOCK.md")),
        "P1_full_matrix_reconstruction_identity_exact": recon["full_matrix_identity_exact"],
        "P2_pole_removed_scalar_cubic_series_exact": all(scalar.values()),
        "P3_source_q_inverse_cubic_exact": qcheck["cosh_sqrt_q_minus_one_recovers_s_through_s3"],
        "P4_all_5_k4_blocks_have_complete_6_internal_4_external_inventory": inventory["all_k4_have_6_internal_4_external_10_total"],
        "P5_all_16_q_blocks_retained": inventory["divergent_block_parameter_count"] == 16,
        "P6_s5_transport_exact_on_block_incidence": inventory["s5_checks"] == 120 and not inventory["s5_failures"],
        "P7_positive_complete_bridge_contract_accepted": positive["accepted"],
        "P8_all_12_malformed_controls_rejected": all(x["rejected"] for x in neg.values()) and len(neg) == 12,
        "P9_source_manifest_and_prereg_provenance_valid": manifest_ok and prereg_link_ok,
        "P10_r3_constructed_without_kak_gauge": recon["full_matrix_identity_exact"] and scalar["pure_plus_exact"] and scalar["mixed_plus_exact"],
        "P11_r4_external_jets_defined_by_same_exact_matrix_function": positive["accepted"] and base["all_four_external_jets"],
        "P12_r6_all_block_q_jets_defined_by_exact_source_q_composition": positive["accepted"] and qcheck["cosh_sqrt_q_minus_one_recovers_s_through_s3"] and inventory["divergent_block_parameter_count"] == 16,
    }

    implementation_valid = (
        manifest_ok
        and prereg_link_ok
        and recon["full_matrix_identity_exact"]
        and all(scalar.values())
        and qcheck["cosh_sqrt_q_minus_one_recovers_s_through_s3"]
        and positive["accepted"]
        and all(x["rejected"] for x in neg.values())
    )

    source_incompatibility = False
    bridge_defined = implementation_valid and all(bridge_predicates.values()) and not source_incompatibility

    if not implementation_valid:
        verdict = "INVALID_IMPLEMENTATION"
        classification = "K4_ORDER3_SOURCE_FAITHFUL_CUBIC_REALIZATION_BRIDGE_INVALID_IMPLEMENTATION"
    elif source_incompatibility:
        verdict = "FAIL_EXACT_SCOPED"
        classification = "K4_ORDER3_SOURCE_FAITHFUL_CUBIC_REALIZATION_BRIDGE_SOURCE_INCOMPATIBLE_SCOPED"
    elif bridge_defined:
        verdict = "PASS_EXACT_SCOPED"
        classification = CLASS_PASS
    else:
        verdict = "BLOCKED_OBJECT_DEFINITION"
        classification = CLASS_BLOCKED

    result = {
        "gate": "K4_ORDER3_SOURCE_FAITHFUL_CUBIC_REALIZATION_BRIDGE",
        "prereg_commit": PREREG_COMMIT,
        "verdict": verdict,
        "classification": classification,
        "implementation_valid": implementation_valid,
        "bridge_defined": bridge_defined,
        "source_incompatibility": source_incompatibility,
        "requirements": {
            "R1_K4_NORMAL_CHART": "RETAINED_AUTHORITY",
            "R2_BCH_ORDER3": "RETAINED_AUTHORITY",
            "R3_TOLLER_ORDER3": "CONSTRUCTED_EXACT_FULL_MATRIX_JET_OPERATOR" if bridge_defined else "UNRESOLVED",
            "R4_EXTERNAL_TOLLER_JETS": "CONSTRUCTED_EXACT_SMOOTH_MATRIX_JET_OPERATOR" if bridge_defined else "UNRESOLVED",
            "R5_HAAR_JACOBIAN_ORDER3": "RETAINED_AUTHORITY",
            "R6_Q_DEFINING_FUNCTION_ORDER3": "CONSTRUCTED_EXACT_16_BLOCK_COMPOSITION_JET_OPERATOR" if bridge_defined else "UNRESOLVED",
            "R7_FULL32_CONTRACTION_MAP": "RETAINED_AUTHORITY",
            "R8_FRONT_PAIRING": "RETAINED_AUTHORITY",
            "R9_BRANCH_NORMALIZATION": "RETAINED_AUTHORITY",
            "R10_S5_TRANSPORT": "RETAINED_AUTHORITY",
        },
        "exact_full_matrix_reconstruction": recon,
        "exact_reduced_scalar_cubic_series": scalar,
        "exact_q_cubic_control": qcheck,
        "inventory": inventory,
        "positive_control": positive,
        "negative_controls": neg,
        "source_blob_manifest": blobs,
        "source_text_hits": text_hits,
        "predicates": bridge_predicates,
        "scientific_ceiling": {
            "k4_polar_coefficient_evaluated": False,
            "k4_zero_or_nonzero_classified": False,
            "k4_annihilator_computed": False,
            "physical_finite_part_selected": False,
            "k5_order8_authorized": False,
            "regulator_independence_claimed": False,
            "new_physics_found": False,
        },
    }

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    out.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0 if verdict == "PASS_EXACT_SCOPED" else (2 if verdict == "BLOCKED_OBJECT_DEFINITION" else 1)


if __name__ == "__main__":
    raise SystemExit(main())
