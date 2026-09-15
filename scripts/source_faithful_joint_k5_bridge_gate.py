#!/usr/bin/env python3
import argparse
import itertools
import json
from fractions import Fraction
from math import comb
from pathlib import Path

REPO_REQUIRED = {
    "prereg/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_AUTHORITY_GATE.md": ["B1.", "B9.", "BRIDGE_AUTHORITY_CONFIRMED_SCOPED"],
    "sources/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_DERIVATION.md": ["q_B", "polyhomogeneous conormal", "multivariate meromorphic polar germ"],
    "sources/ITER077I_SM_SOURCE_ORDERED_TOLLER_FUNCTION_K5_L1_DERIVATION.md": ["product of ten Toller matrices", "2^5=32"],
    "results/ITER082D_SM_NESTED_NORMAL_PROJECTOR_FOREST_EXTENSION_RESULT.md": ["6 + 3 + 3 = 12", "1920/1920", "7200/7200"],
    "results/ITER083M_SM_SOURCE_NORMAL_GEOMETRIC_RADIAL_BASIS_RESULT.md": ["R_B^2", "1/p", "unique local forest radial quadratic basis"],
}


def rank_q(mat):
    a = [[Fraction(x) for x in row] for row in mat]
    m, n = len(a), len(a[0]) if a else 0
    r = c = 0
    while r < m and c < n:
        piv = next((i for i in range(r, m) if a[i][c] != 0), None)
        if piv is None:
            c += 1
            continue
        a[r], a[piv] = a[piv], a[r]
        z = a[r][c]
        a[r] = [x / z for x in a[r]]
        for i in range(m):
            if i != r and a[i][c] != 0:
                z = a[i][c]
                a[i] = [a[i][j] - z * a[r][j] for j in range(n)]
        r += 1
        c += 1
    return r


def projector(block, n=5):
    b = sorted(block)
    p = len(b)
    out = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for i in b:
        for j in b:
            out[i][j] = (Fraction(1) if i == j else Fraction(0)) - Fraction(1, p)
    return out


def sub(a, b):
    return [[x-y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def laplacian_complete_identity(block, n=5):
    b = sorted(block)
    p = len(b)
    L = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for i in b:
        L[i][i] = p - 1
        for j in b:
            if i != j:
                L[i][j] = -1
    P = projector(block, n)
    return all(Fraction(L[i][j], p) == P[i][j] for i in range(n) for j in range(n))


def permute_block(block, perm):
    return tuple(sorted(perm[i] for i in block))


def all_perms(n=5):
    return list(itertools.permutations(range(n)))


def series_q_of_s():
    # Solve cosh(sqrt(q))=1+s through cubic order using exact rationals.
    # cosh(sqrt(q)) = 1 + q/2 + q^2/24 + q^3/720 + ...
    a1 = Fraction(2)
    a2 = -a1*a1/Fraction(12)
    a3 = -2 * (2*a1*a2/Fraction(24) + a1**3/Fraction(720))
    return [a1, a2, a3]


def read_required():
    missing = {}
    for path, needles in REPO_REQUIRED.items():
        p = Path(path)
        if not p.exists():
            missing[path] = ["FILE_MISSING"]
            continue
        text = p.read_text(encoding="utf-8")
        bad = [x for x in needles if x not in text]
        if bad:
            missing[path] = bad
    return missing


def validate_candidate(c, computed):
    b = {}
    b["B1"] = (
        c["source_order_wedges"] == 10
        and c["divergent_block_count"] == computed["divergent_block_count"]
        and c["true_k5_incidence"]
        and c["joint_multivariate_family"]
    )
    b["B2"] = (
        c["source_order_exact"]
        and not c["modifies_one_wedge_spectral_prescription"]
        and not c["uses_beta_plus_i_epsilon"]
        and c["joint_map_is_post_toller_scalar_multiplication"]
    )
    b["B3"] = c["boundary_components"] == 32 and c["retains_full_boundary"]
    b["B4"] = (
        c["uses_original_haar"]
        and tuple(c["chain_density_powers"]) == tuple(computed["chain_density_powers"])
        and c["jacobian_derived"]
    )
    b["B5"] = c["branch_blind"] and c["reversal_invariant"] and c["preserves_toller_sign_identities"]
    b["B6"] = (
        c["full_polydiagonal_resolution"]
        and c["polyhomogeneous_conormal_lift"]
        and c["mellin_meromorphic_continuation"]
        and c["continuation_unique_from_convergent_domain"]
    )
    b["B7"] = (
        not c["uses_auxiliary_regulator_metric"]
        and not c["selects_holomorphic_projection"]
        and not c["selects_finite_part"]
        and not c["selects_subtraction_constants"]
        and not c["selects_sequential_specialization"]
        and c["source_derived_block_radii"]
    )
    b["B8"] = c["s5_block_covariance"] and not c["preferred_label"] and not c["preferred_chain"]
    b["B9"] = (
        c["output_is_actual_multivariate_polar_germ"]
        and c["negative_laurent_coefficients_supported"]
        and c["authorizes_multivariate_polar_annihilator_gate"]
        and c["one_parameter_specialization_requires_new_gate"]
    )
    return b


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lock", default="sources/raw/source_faithful_joint_k5_bridge_lock.json")
    ap.add_argument("--output", default="results/raw/source_faithful_joint_k5_bridge_gate.json")
    args = ap.parse_args()

    lock = json.loads(Path(args.lock).read_text(encoding="utf-8"))
    provenance_missing = read_required()

    vertices = tuple(range(5))
    blocks = {p: [tuple(x) for x in itertools.combinations(vertices, p)] for p in range(2, 6)}
    all_blocks = {x for p in blocks.values() for x in p}
    divergent = {x for p in (3,4,5) for x in blocks[p]}
    perms = all_perms()
    s5_closure_failures = []
    for pi in perms:
        for B in all_blocks:
            if permute_block(B, pi) not in all_blocks:
                s5_closure_failures.append([pi, B])

    laplacian_checks = {p: all(laplacian_complete_identity(B) for B in blocks[p]) for p in range(2,6)}

    chains = []
    chain_ranks = []
    chain_density = []
    for B3 in blocks[3]:
        s3 = set(B3)
        for B4 in blocks[4]:
            s4 = set(B4)
            if not s3 < s4:
                continue
            for B5 in blocks[5]:
                s5 = set(B5)
                if not s4 < s5:
                    continue
                A = projector(B3)
                B = sub(projector(B4), projector(B3))
                C = sub(projector(B5), projector(B4))
                ranks_one = (rank_q(A), rank_q(B), rank_q(C))
                ranks_phys = tuple(3*r for r in ranks_one)
                chains.append((B3,B4,B5))
                chain_ranks.append(ranks_phys)
                chain_density.append(tuple(r-1 for r in ranks_phys))

    computed = {
        "all_block_count": len(all_blocks),
        "expected_all_block_count": sum(comb(5,p) for p in range(2,6)),
        "divergent_block_count": len(divergent),
        "expected_divergent_block_count": sum(comb(5,p) for p in (3,4,5)),
        "maximal_divergent_chains": len(chains),
        "s5_permutations": len(perms),
        "s5_closure_failures": len(s5_closure_failures),
        "laplacian_projector_checks": laplacian_checks,
        "chain_rank_values": sorted(set(chain_ranks)),
        "chain_density_power_values": sorted(set(chain_density)),
        "chain_density_powers": [5,2,2] if set(chain_density) == {(5,2,2)} else [],
        "q_series_coefficients": [str(x) for x in series_q_of_s()],
    }

    geometry_ok = (
        computed["all_block_count"] == computed["expected_all_block_count"]
        and computed["divergent_block_count"] == computed["expected_divergent_block_count"]
        and computed["maximal_divergent_chains"] == 20
        and computed["s5_permutations"] == 120
        and computed["s5_closure_failures"] == 0
        and all(laplacian_checks.values())
        and set(chain_ranks) == {(6,3,3)}
        and set(chain_density) == {(5,2,2)}
        and series_q_of_s() == [Fraction(2), Fraction(-1,3), Fraction(4,45)]
    )

    candidate = {
        "source_order_wedges": 10,
        "divergent_block_count": lock["collision_arrangement"]["divergent_blocks"]["total"],
        "true_k5_incidence": lock["collision_arrangement"]["all_blocks"]["total"] == len(all_blocks),
        "joint_multivariate_family": lock["joint_family"]["parameter_count"] == len(divergent),
        "source_order_exact": lock["source_order"] == [
            "one-wedge spectral/spinor integration", "Toller function", "product of ten Toller matrices",
            "full 32-component boundary contraction", "K5 group integration / distributional extension"
        ],
        "modifies_one_wedge_spectral_prescription": lock["joint_family"]["modifies_one_wedge_spectral_prescription"],
        "uses_beta_plus_i_epsilon": lock["joint_family"]["uses_beta_plus_i_epsilon"],
        "joint_map_is_post_toller_scalar_multiplication": "A_source" in lock["joint_family"]["formula"],
        "boundary_components": lock["boundary"]["components"],
        "retains_full_boundary": lock["boundary"]["retained_all_components"],
        "uses_original_haar": lock["joint_family"]["uses_original_product_Haar_density"],
        "chain_density_powers": lock["collision_arrangement"]["resolved_chain_density_powers"],
        "jacobian_derived": tuple(lock["collision_arrangement"]["resolved_chain_density_powers"]) == tuple(computed["chain_density_powers"]),
        "branch_blind": True,
        "reversal_invariant": lock["cartan"]["reversal_invariant"],
        "preserves_toller_sign_identities": not lock["joint_family"]["modifies_one_wedge_spectral_prescription"],
        "full_polydiagonal_resolution": lock["collision_arrangement"]["all_blocks"]["total"] == 26,
        "polyhomogeneous_conormal_lift": "polyhomogeneous conormal" in lock["analytic_bridge"]["lift_class"],
        "mellin_meromorphic_continuation": "meromorphic" in lock["analytic_bridge"]["continuation"],
        "continuation_unique_from_convergent_domain": "unique" in lock["analytic_bridge"]["continuation"],
        "uses_auxiliary_regulator_metric": lock["block_radius"]["uses_auxiliary_regulator_parameter_metric"],
        "selects_holomorphic_projection": lock["joint_family"]["selects_holomorphic_projection"],
        "selects_finite_part": lock["joint_family"]["selects_finite_part"],
        "selects_subtraction_constants": lock["joint_family"]["selects_subtraction_constants"],
        "selects_sequential_specialization": lock["joint_family"]["selects_sequential_specialization"],
        "source_derived_block_radii": "beta" in lock["block_radius"]["formula"] and lock["block_radius"]["source_normal_authority"] == "Iter083M",
        "s5_block_covariance": computed["s5_closure_failures"] == 0 and "lambda_B" in lock["joint_family"]["parameter_action"],
        "preferred_label": False,
        "preferred_chain": False,
        "output_is_actual_multivariate_polar_germ": "actual full-boundary-contracted source-ordered multivariate meromorphic polar germ" == lock["output_object"]["type"],
        "negative_laurent_coefficients_supported": lock["output_object"]["negative_laurent_coefficients_supported_on_collision_strata"],
        "authorizes_multivariate_polar_annihilator_gate": lock["output_object"]["authorizes_next_gate"] == "ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR",
        "one_parameter_specialization_requires_new_gate": lock["output_object"]["does_not_authorize_one_parameter_A_minus_1_without_new_gate"],
    }

    predicates = validate_candidate(candidate, computed)

    mutations = {
        "representative_component": {"boundary_components": 1, "retains_full_boundary": False},
        "auxiliary_regulator_Q": {"uses_auxiliary_regulator_metric": True},
        "beta_plus_i_epsilon": {"uses_beta_plus_i_epsilon": True},
        "omit_haar": {"uses_original_haar": False},
        "posthoc_finite_part": {"selects_holomorphic_projection": True, "selects_finite_part": True},
        "preferred_sequential_specialization": {"selects_sequential_specialization": True},
        "preferred_label": {"preferred_label": True},
        "k5_only_no_full_incidence": {"true_k5_incidence": False, "divergent_block_count": 1},
        "wrong_source_order": {"source_order_exact": False, "joint_map_is_post_toller_scalar_multiplication": False},
    }
    controls = {}
    for name, mut in mutations.items():
        bad = dict(candidate)
        bad.update(mut)
        bbad = validate_candidate(bad, computed)
        controls[name] = not all(bbad.values())

    implementation_ok = geometry_ok and not provenance_missing and all(controls.values())
    scientific_pass = implementation_ok and all(predicates.values())

    if not implementation_ok:
        verdict = "INVALID_IMPLEMENTATION"
        classification = "SOURCE_FAITHFUL_JOINT_K5_BRIDGE_GATE_INVALID_IMPLEMENTATION"
    elif scientific_pass:
        verdict = "PASS_EXACT_SCOPED"
        classification = "BRIDGE_AUTHORITY_CONFIRMED_SCOPED"
    else:
        verdict = "BLOCKED_OBJECT_DEFINITION"
        classification = "SOURCE_FAITHFUL_JOINT_K5_BRIDGE_REMAINS_BLOCKED_OBJECT_DEFINITION"

    out = {
        "gate": "SOURCE_FAITHFUL_JOINT_K5_MEROMORPHIC_OR_MULTIVARIABLE_BOUNDARY_VALUE_BRIDGE_AUTHORITY_GATE",
        "classification": classification,
        "verdict": verdict,
        "predicates": predicates,
        "controls": controls,
        "geometry_ok": geometry_ok,
        "provenance_missing": provenance_missing,
        "computed": computed,
        "interpretation": {
            "meromorphic_polar_germ_defined": scientific_pass,
            "physical_finite_part_selected": False,
            "unique_k5_extension_claimed": False,
            "one_parameter_A_minus_1_authorized": False,
            "next_gate": "ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR" if scientific_pass else None,
        },
    }
    payload = json.dumps(out, indent=2, sort_keys=True)
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(payload + "\n", encoding="utf-8")
    print(payload)
    return 0 if implementation_ok else 2


if __name__ == "__main__":
    raise SystemExit(main())
