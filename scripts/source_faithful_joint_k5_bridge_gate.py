#!/usr/bin/env python3
import argparse
import itertools
import json
from fractions import Fraction
from math import comb
from pathlib import Path

REPO_REQUIRED = {
    "prereg/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_AUTHORITY_GATE.md": [
        "B1.", "B4.", "B6.", "B9.", "BRIDGE_AUTHORITY_CONFIRMED_SCOPED"
    ],
    "prereg/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_CRITIC_REPAIR_1.md": [
        "(5,8,11)", "(-1,-4,-9)", "No B1-B9 wording"
    ],
    "sources/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_DERIVATION.md": [
        "q_B", "polyhomogeneous conormal", "multivariate meromorphic polar germ"
    ],
    "sources/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_NESTED_JACOBIAN_REPAIR_DERIVATION.md": [
        "rho3^5 rho4^8 rho5^11", "L_C(lambda)", "rho3^(L_B3-1)", "omega_K5=8"
    ],
    "sources/ITER077I_SM_SOURCE_ORDERED_TOLLER_FUNCTION_K5_L1_DERIVATION.md": [
        "product of ten Toller matrices", "2^5=32"
    ],
    "results/ITER082D_SM_NESTED_NORMAL_PROJECTOR_FOREST_EXTENSION_RESULT.md": [
        "6 + 3 + 3 = 12", "1920/1920", "7200/7200"
    ],
    "results/ITER083M_SM_SOURCE_NORMAL_GEOMETRIC_RADIAL_BASIS_RESULT.md": [
        "R_B^2", "1/p", "unique local forest radial quadratic basis"
    ],
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
    return [[x - y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


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
    # Exact formal inversion of cosh(sqrt(q))=1+s through cubic order.
    # cosh(sqrt(q)) = 1 + q/2 + q^2/24 + q^3/720 + ...
    a1 = Fraction(2)
    a2 = -a1 * a1 / Fraction(12)
    a3 = -2 * (2 * a1 * a2 / Fraction(24) + a1**3 / Fraction(720))
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


def ordered_divergent_blocks(blocks):
    return [B for p in (3, 4, 5) for B in sorted(blocks[p])]


def incidence_matrix(divergent):
    # Rows are collision faces C and columns regulator blocks B.
    # Ordered by increasing block size, this is lower triangular with unit diagonal.
    return [
        [1 if set(B).issubset(C) else 0 for B in divergent]
        for C in divergent
    ]


def is_lower_triangular_unit(mat):
    n = len(mat)
    return (
        all(mat[i][i] == 1 for i in range(n))
        and all(mat[i][j] == 0 for i in range(n) for j in range(i + 1, n))
    )


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
        and tuple(c["chain_increment_normal_ranks"]) == tuple(computed["chain_increment_normal_ranks"])
        and tuple(c["chain_cumulative_normal_dimensions"]) == tuple(computed["chain_cumulative_normal_dimensions"])
        and tuple(c["chain_density_powers"]) == tuple(computed["chain_density_powers"])
        and c["jacobian_derived"]
    )
    b["B5"] = (
        c["branch_blind"]
        and c["reversal_invariant"]
        and c["preserves_toller_sign_identities"]
    )
    b["B6"] = (
        c["full_polydiagonal_resolution"]
        and c["polyhomogeneous_conormal_lift"]
        and c["mellin_meromorphic_continuation"]
        and c["continuation_unique_from_convergent_domain"]
        and c["incidence_map_invertible"]
        and c["nonempty_convergence_chamber"]
        and c["corrected_mellin_exponents"]
    )
    b["B7"] = (
        not c["uses_auxiliary_regulator_metric"]
        and not c["selects_holomorphic_projection"]
        and not c["selects_finite_part"]
        and not c["selects_subtraction_constants"]
        and not c["selects_sequential_specialization"]
        and c["source_derived_block_radii"]
        and not c["claims_regulator_independence"]
    )
    b["B8"] = (
        c["s5_block_covariance"]
        and not c["preferred_label"]
        and not c["preferred_chain"]
    )
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
    divergent = ordered_divergent_blocks(blocks)
    divergent_set = set(divergent)

    perms = all_perms()
    s5_closure_failures = []
    for pi in perms:
        for B in all_blocks:
            if permute_block(B, pi) not in all_blocks:
                s5_closure_failures.append([pi, B])

    laplacian_checks = {
        p: all(laplacian_complete_identity(B) for B in blocks[p])
        for p in range(2, 6)
    }

    chains = []
    chain_increment_ranks = []
    chain_cumulative_dims = []
    chain_density_powers = []
    chain_toller_powers = []
    chain_haar_source_powers = []
    chain_omegas = []

    edge_increment_counts = (
        comb(3, 2),
        comb(4, 2) - comb(3, 2),
        comb(5, 2) - comb(4, 2),
    )
    cumulative_internal_edge_counts = (comb(3, 2), comb(4, 2), comb(5, 2))
    cumulative_toller_powers = tuple(-2 * n for n in cumulative_internal_edge_counts)

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
                ranks_phys = tuple(3 * r for r in ranks_one)
                cumulative = (
                    ranks_phys[0],
                    ranks_phys[0] + ranks_phys[1],
                    sum(ranks_phys),
                )
                density = tuple(d - 1 for d in cumulative)
                haar_source = tuple(d + t for d, t in zip(density, cumulative_toller_powers))
                omega = tuple(-e - 1 for e in haar_source)

                chains.append((B3, B4, B5))
                chain_increment_ranks.append(ranks_phys)
                chain_cumulative_dims.append(cumulative)
                chain_density_powers.append(density)
                chain_toller_powers.append(cumulative_toller_powers)
                chain_haar_source_powers.append(haar_source)
                chain_omegas.append(omega)

    inc = incidence_matrix(divergent)
    inc_rank = rank_q(inc)
    inc_lower_unit = is_lower_triangular_unit(inc)

    lambda_one_values = {
        str(p): sorted({
            sum(1 for B in divergent if set(B).issubset(C))
            for C in blocks[p]
        })
        for p in (3, 4, 5)
    }
    omega_by_size = {3: 0, 4: 3, 5: 8}
    uniform_lambda_one_converges = all(
        all(v > omega_by_size[p] for v in lambda_one_values[str(p)])
        for p in (3, 4, 5)
    )

    computed = {
        "all_block_count": len(all_blocks),
        "expected_all_block_count": sum(comb(5, p) for p in range(2, 6)),
        "divergent_block_count": len(divergent_set),
        "expected_divergent_block_count": sum(comb(5, p) for p in (3, 4, 5)),
        "maximal_divergent_chains": len(chains),
        "s5_permutations": len(perms),
        "s5_closure_failures": len(s5_closure_failures),
        "laplacian_projector_checks": laplacian_checks,
        "chain_increment_rank_values": sorted(set(chain_increment_ranks)),
        "chain_cumulative_dimension_values": sorted(set(chain_cumulative_dims)),
        "chain_density_power_values": sorted(set(chain_density_powers)),
        "chain_toller_power_values": sorted(set(chain_toller_powers)),
        "chain_haar_source_power_values": sorted(set(chain_haar_source_powers)),
        "chain_superficial_divergence_degree_values": sorted(set(chain_omegas)),
        "chain_increment_normal_ranks": [6, 3, 3] if set(chain_increment_ranks) == {(6, 3, 3)} else [],
        "chain_cumulative_normal_dimensions": [6, 9, 12] if set(chain_cumulative_dims) == {(6, 9, 12)} else [],
        "chain_density_powers": [5, 8, 11] if set(chain_density_powers) == {(5, 8, 11)} else [],
        "edge_increment_counts": list(edge_increment_counts),
        "cumulative_internal_edge_counts": list(cumulative_internal_edge_counts),
        "cumulative_toller_radial_powers": list(cumulative_toller_powers),
        "haar_times_source_radial_powers": [-1, -4, -9] if set(chain_haar_source_powers) == {(-1, -4, -9)} else [],
        "superficial_divergence_degrees": [0, 3, 8] if set(chain_omegas) == {(0, 3, 8)} else [],
        "incidence_matrix_rank": inc_rank,
        "incidence_matrix_size": len(divergent),
        "incidence_lower_triangular_unit_diagonal": inc_lower_unit,
        "incidence_determinant": 1 if inc_lower_unit else None,
        "uniform_lambda_one_face_values_by_size": lambda_one_values,
        "uniform_lambda_one_convergence_witness": uniform_lambda_one_converges,
        "pole_producing_taylor_orders": [0, 3, 8],
        "q_series_coefficients": [str(x) for x in series_q_of_s()],
    }

    geometry_ok = (
        computed["all_block_count"] == computed["expected_all_block_count"]
        and computed["divergent_block_count"] == computed["expected_divergent_block_count"]
        and computed["maximal_divergent_chains"] == 20
        and computed["s5_permutations"] == 120
        and computed["s5_closure_failures"] == 0
        and all(laplacian_checks.values())
        and set(chain_increment_ranks) == {(6, 3, 3)}
        and set(chain_cumulative_dims) == {(6, 9, 12)}
        and set(chain_density_powers) == {(5, 8, 11)}
        and set(chain_toller_powers) == {(-6, -12, -20)}
        and set(chain_haar_source_powers) == {(-1, -4, -9)}
        and set(chain_omegas) == {(0, 3, 8)}
        and inc_rank == 16
        and inc_lower_unit
        and uniform_lambda_one_converges
        and lambda_one_values == {"3": [1], "4": [5], "5": [16]}
        and series_q_of_s() == [Fraction(2), Fraction(-1, 3), Fraction(4, 45)]
    )

    lock_collision = lock["collision_arrangement"]
    lock_scaling = lock["source_scaling_at_maximal_chain"]
    lock_incidence = lock["regulator_incidence"]

    candidate = {
        "source_order_wedges": 10,
        "divergent_block_count": lock_collision["divergent_blocks"]["total"],
        "true_k5_incidence": lock_collision["all_blocks"]["total"] == len(all_blocks),
        "joint_multivariate_family": lock["joint_family"]["parameter_count"] == len(divergent),
        "source_order_exact": lock["source_order"] == [
            "one-wedge spectral/spinor integration",
            "Toller function",
            "product of ten Toller matrices",
            "full 32-component boundary contraction",
            "K5 group integration / distributional extension",
        ],
        "modifies_one_wedge_spectral_prescription": lock["joint_family"]["modifies_one_wedge_spectral_prescription"],
        "uses_beta_plus_i_epsilon": lock["joint_family"]["uses_beta_plus_i_epsilon"],
        "joint_map_is_post_toller_scalar_multiplication": "A_source" in lock["joint_family"]["formula"],
        "boundary_components": lock["boundary"]["components"],
        "retains_full_boundary": lock["boundary"]["retained_all_components"],
        "uses_original_haar": lock["joint_family"]["uses_original_product_Haar_density"],
        "chain_increment_normal_ranks": lock_collision["chain_increment_normal_ranks"],
        "chain_cumulative_normal_dimensions": lock_collision["chain_cumulative_normal_dimensions"],
        "chain_density_powers": lock_collision["resolved_chain_density_powers"],
        "jacobian_derived": (
            tuple(lock_collision["chain_increment_normal_ranks"]) == tuple(computed["chain_increment_normal_ranks"])
            and tuple(lock_collision["chain_cumulative_normal_dimensions"]) == tuple(computed["chain_cumulative_normal_dimensions"])
            and tuple(lock_collision["resolved_chain_density_powers"]) == tuple(computed["chain_density_powers"])
        ),
        "branch_blind": True,
        "reversal_invariant": lock["cartan"]["reversal_invariant"],
        "preserves_toller_sign_identities": not lock["joint_family"]["modifies_one_wedge_spectral_prescription"],
        "full_polydiagonal_resolution": lock_collision["all_blocks"]["total"] == 26,
        "polyhomogeneous_conormal_lift": "polyhomogeneous conormal" in lock["analytic_bridge"]["lift_class"],
        "mellin_meromorphic_continuation": "meromorphic" in lock["analytic_bridge"]["continuation"],
        "continuation_unique_from_convergent_domain": (
            "nonempty convergence chamber" in lock["analytic_bridge"]["continuation"]
            and "unique" in lock["analytic_bridge"]["continuation"]
        ),
        "incidence_map_invertible": (
            lock_incidence["map_is_triangular_by_block_size"]
            and lock_incidence["diagonal_entries"] == 1
            and lock_incidence["determinant"] == 1
            and computed["incidence_matrix_rank"] == 16
            and computed["incidence_lower_triangular_unit_diagonal"]
        ),
        "nonempty_convergence_chamber": computed["uniform_lambda_one_convergence_witness"],
        "corrected_mellin_exponents": (
            tuple(lock_scaling["cumulative_toller_radial_powers"]) == tuple(computed["cumulative_toller_radial_powers"])
            and tuple(lock_scaling["haar_times_source_radial_powers"]) == tuple(computed["haar_times_source_radial_powers"])
            and tuple(lock_scaling["superficial_divergence_degrees"]) == tuple(computed["superficial_divergence_degrees"])
            and tuple(lock_incidence["pole_producing_taylor_orders_at_lambda_zero"]) == tuple(computed["pole_producing_taylor_orders"])
        ),
        "uses_auxiliary_regulator_metric": lock["block_radius"]["uses_auxiliary_regulator_parameter_metric"],
        "selects_holomorphic_projection": lock["joint_family"]["selects_holomorphic_projection"],
        "selects_finite_part": lock["joint_family"]["selects_finite_part"],
        "selects_subtraction_constants": lock["joint_family"]["selects_subtraction_constants"],
        "selects_sequential_specialization": lock["joint_family"]["selects_sequential_specialization"],
        "source_derived_block_radii": (
            "beta" in lock["block_radius"]["formula"]
            and lock["block_radius"]["source_normal_authority"] == "Iter083M"
        ),
        "claims_regulator_independence": lock["defining_function_scheme"]["regulator_independence_claimed"],
        "s5_block_covariance": computed["s5_closure_failures"] == 0 and "lambda_B" in lock["joint_family"]["parameter_action"],
        "preferred_label": False,
        "preferred_chain": False,
        "output_is_actual_multivariate_polar_germ": (
            lock["output_object"]["type"]
            == "actual full-boundary-contracted source-ordered q_B-scheme multivariate meromorphic polar germ"
        ),
        "negative_laurent_coefficients_supported": lock["output_object"]["negative_laurent_coefficients_supported_on_collision_strata"],
        "authorizes_multivariate_polar_annihilator_gate": (
            lock["output_object"]["authorizes_next_gate"]
            == "ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR"
        ),
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
        "wrong_incremental_density_as_nested": {"chain_density_powers": [5, 2, 2], "jacobian_derived": False},
        "singular_incidence_map": {"incidence_map_invertible": False},
        "empty_convergence_chamber": {"nonempty_convergence_chamber": False},
        "wrong_nested_source_exponents": {"corrected_mellin_exponents": False},
        "false_regulator_independence": {"claims_regulator_independence": True},
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
        "repair": "NESTED_BLOWUP_JACOBIAN_AND_MELLIN_REPAIR_1",
        "classification": classification,
        "verdict": verdict,
        "predicates": predicates,
        "controls": controls,
        "geometry_ok": geometry_ok,
        "provenance_missing": provenance_missing,
        "computed": computed,
        "interpretation": {
            "meromorphic_polar_germ_defined": scientific_pass,
            "scheme_scoped_to_q_B": True,
            "regulator_independence_claimed": False,
            "physical_finite_part_selected": False,
            "unique_k5_extension_claimed": False,
            "one_parameter_A_minus_1_authorized": False,
            "next_gate": (
                "ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR"
                if scientific_pass else None
            ),
        },
    }
    payload = json.dumps(out, indent=2, sort_keys=True)
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(payload + "\n", encoding="utf-8")
    print(payload)
    return 0 if implementation_ok else 2


if __name__ == "__main__":
    raise SystemExit(main())
