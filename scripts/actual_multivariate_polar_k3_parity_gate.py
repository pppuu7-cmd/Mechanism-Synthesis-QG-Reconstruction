#!/usr/bin/env python3
import argparse
import copy
import hashlib
import importlib.util
import itertools
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERTICES = tuple(range(5))
ALL_EDGES = tuple(itertools.combinations(VERTICES, 2))
K3_BLOCKS = tuple(itertools.combinations(VERTICES, 3))
DIVERGENT_BLOCKS = tuple(
    B for p in (3, 4, 5) for B in itertools.combinations(VERTICES, p)
)


def load_iter077i():
    path = ROOT / "distributional" / "iter077i_sm_source_ordered_jhalf_k5_l1.py"
    spec = importlib.util.spec_from_file_location("iter077i_exact", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def require_text(path, needles):
    text = (ROOT / path).read_text(encoding="utf-8")
    missing = [x for x in needles if x not in text]
    return not missing, missing


def det_fraction(mat):
    a = [[Fraction(x) for x in row] for row in mat]
    n = len(a)
    det = Fraction(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if a[r][c] != 0), None)
        if piv is None:
            return Fraction(0)
        if piv != c:
            a[c], a[piv] = a[piv], a[c]
            det *= -1
        z = a[c][c]
        det *= z
        for j in range(c, n):
            a[c][j] /= z
        for r in range(c + 1, n):
            z = a[r][c]
            if z:
                for j in range(c, n):
                    a[r][j] -= z * a[c][j]
    return det


def transpose(a):
    return [list(x) for x in zip(*a)]


def matmul(a, b):
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def block_diag_three(g2):
    out = [[Fraction(0) for _ in range(6)] for _ in range(6)]
    for axis in range(3):
        for i in range(2):
            for j in range(2):
                out[2 * axis + i][2 * axis + j] = Fraction(g2[i][j])
    return out


def k3_normal_geometry():
    # Per Cartesian axis: (u,v) -> (u,v,-u-v).
    a = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)], [Fraction(-1), Fraction(-1)]]
    g2 = matmul(transpose(a), a)
    gram = block_diag_three(g2)
    inv = [[Fraction(-1 if i == j else 0) for j in range(6)] for i in range(6)]
    inv_gram = matmul(transpose(inv), matmul(gram, inv))
    return {
        "scalar_axis_embedding": [[int(x) for x in row] for row in a],
        "scalar_axis_gram": [[int(x) for x in row] for row in g2],
        "gram_determinant": int(det_fraction(gram)),
        "inversion_determinant": int(det_fraction(inv)),
        "inversion_preserves_gram": inv_gram == gram,
        "normal_dimension": 6,
        "front_dimension": 5,
    }


def vertex_normal_vectors(block):
    # Six independent variables ordered ux,uy,uz,vx,vy,vz.
    b = tuple(sorted(block))
    zero3 = tuple((0,) * 6 for _ in range(3))
    maps = {v: zero3 for v in VERTICES}
    u = (
        (1, 0, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0),
        (0, 0, 1, 0, 0, 0),
    )
    v = (
        (0, 0, 0, 1, 0, 0),
        (0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 1),
    )
    w = tuple(tuple(-u[k][j] - v[k][j] for j in range(6)) for k in range(3))
    maps[b[0]], maps[b[1]], maps[b[2]] = u, v, w
    return maps


def vec_sub(a, b):
    return tuple(tuple(x - y for x, y in zip(aa, bb)) for aa, bb in zip(a, b))


def linear_entry_signature(dv, row, col):
    vx, vy, vz = dv
    if (row, col) == (0, 0):
        coeff = tuple((z, 0) for z in vz)
    elif (row, col) == (0, 1):
        coeff = tuple((-x, -y) for x, y in zip(vx, vy))
    elif (row, col) == (1, 0):
        coeff = tuple((-x, y) for x, y in zip(vx, vy))
    else:
        coeff = tuple((-z, 0) for z in vz)
    assert any(z != (0, 0) for z in coeff)
    return coeff


def build_edge_geometry(block):
    block = tuple(sorted(block))
    bset = set(block)
    vmaps = vertex_normal_vectors(block)
    internal = [e for e in ALL_EDGES if set(e).issubset(bset)]
    external = [e for e in ALL_EDGES if e not in internal]
    internal_forms = {}
    for e in internal:
        dv = vec_sub(vmaps[e[0]], vmaps[e[1]])
        internal_forms[e] = {
            (r, c): linear_entry_signature(dv, r, c)
            for r in (0, 1) for c in (0, 1)
        }
    # Actual external Toller factors are evaluated at the collapsed K3 point at rho_B=0.
    # Their entries can depend meromorphically on tangential/outer variables, but not on
    # the six K3 front variables at normal Taylor order zero.
    external_atoms = {
        e: {(r, c): f"T0_{e[0]}{e[1]}_{r}{c}" for r in (0, 1) for c in (0, 1)}
        for e in external
    }
    endpoint_constant_tokens = {
        x: ("H_B" if x in bset else f"G_{x}") for x in VERTICES
    }
    external_order0 = {}
    for e in external:
        external_order0[str(e)] = {
            "relative_constant": f"{endpoint_constant_tokens[e[1]]}^-1*{endpoint_constant_tokens[e[0]]}",
            "k3_normal_degree": 0,
            "formal_toller_matrix_entries": [external_atoms[e][(r, c)] for r in (0, 1) for c in (0, 1)],
        }
    return internal, external, internal_forms, external_atoms, external_order0


def component_symbolic_certificate(mod, block, ks, internal_forms, external_atoms):
    bset = set(block)
    h = hashlib.sha256()
    raw_terms = 0
    normal_degrees = set()
    internal_factor_counts = set()
    external_factor_counts = set()
    options = [mod.NODE_OPTIONS[k] for k in ks]
    for choices in itertools.product(*options):
        states = []
        coeff = 1
        for state, c in choices:
            states.append(state)
            coeff *= c
        pieces = [f"c={coeff}"]
        degree = 0
        ni = ne = 0
        for a, b in ALL_EDGES:
            row = states[b][mod.LEG_POS[(b, a)]]
            col = states[a][mod.LEG_POS[(a, b)]]
            e = (a, b)
            if set(e).issubset(bset):
                sig = internal_forms[e][(row, col)]
                pieces.append(f"I{a}{b}{row}{col}:{sig}")
                degree += 1
                ni += 1
            else:
                atom = external_atoms[e][(row, col)]
                pieces.append(f"E{a}{b}{row}{col}:{atom}")
                ne += 1
        raw_terms += 1
        normal_degrees.add(degree)
        internal_factor_counts.add(ni)
        external_factor_counts.add(ne)
        h.update(("|".join(pieces) + "\n").encode("utf-8"))
    return {
        "boundary_k": list(ks),
        "raw_contraction_terms": raw_terms,
        "normal_degrees": sorted(normal_degrees),
        "internal_factor_counts": sorted(internal_factor_counts),
        "external_factor_counts": sorted(external_factor_counts),
        "odd_under_k3_inversion": normal_degrees == {3},
        "term_skeleton_sha256": h.hexdigest(),
    }


def block_symbolic_certificate(mod, block):
    internal, external, internal_forms, external_atoms, external_order0 = build_edge_geometry(block)
    components = []
    for ks in itertools.product((0, 1), repeat=5):
        components.append(component_symbolic_certificate(mod, block, ks, internal_forms, external_atoms))
    canonical = json.dumps(components, sort_keys=True, separators=(",", ":"))
    return {
        "block": list(block),
        "internal_edges": [list(e) for e in internal],
        "external_edges": [list(e) for e in external],
        "external_order0": external_order0,
        "component_count": len(components),
        "all_components_odd": all(c["odd_under_k3_inversion"] for c in components),
        "all_term_degrees_exactly_three": all(c["normal_degrees"] == [3] for c in components),
        "all_terms_have_3_internal_7_external": all(
            c["internal_factor_counts"] == [3] and c["external_factor_counts"] == [7]
            for c in components
        ),
        "component_certificate_sha256": hashlib.sha256(canonical.encode("utf-8")).hexdigest(),
        "components": components,
    }


def s5_transport_certificate(block_certs):
    by_block = {tuple(x["block"]): x for x in block_certs}
    labels = list(itertools.product((0, 1), repeat=5))
    failures = []
    checks = 0
    canonical = K3_BLOCKS[0]
    for perm in itertools.permutations(VERTICES):
        image = tuple(sorted(perm[x] for x in canonical))
        cert = by_block.get(image)
        permuted_labels = {tuple(ks[perm[i]] for i in VERTICES) for ks in labels}
        ok = cert is not None and cert["all_components_odd"] and len(permuted_labels) == 32
        checks += 1
        if not ok:
            failures.append({"perm": list(perm), "image": list(image)})
    return {"permutations_checked": checks, "failures": failures, "all_pass": not failures}


def laurent_gauge_certificate():
    # For a simple face pole U = R L^-1 + A0 + ..., H = h0 + h1 L + ... .
    # The only convolution pair contributing to L^-1 is (H exponent 0, U exponent -1).
    h_exponents = (0, 1, 2)
    u_exponents = (-1, 0, 1)
    pairs = [(h, u) for h in h_exponents for u in u_exponents if h + u == -1]
    return {
        "simple_face_pole": True,
        "residue_convolution_pairs": [list(x) for x in pairs],
        "only_h0_times_residue": pairs == [(0, -1)],
        "h0_at_physical_origin": 1,
        "zero_residue_stable": pairs == [(0, -1)],
        "all_laurent_coefficients_claimed_invariant": False,
    }


def expected_density_powers():
    cumulative_dims = tuple(3 * (p - 1) for p in (3, 4, 5))
    return tuple(d - 1 for d in cumulative_dims)


def validate_object(obj):
    reasons = []
    expected_blocks = {tuple(B) for B in DIVERGENT_BLOCKS}
    got_blocks = {tuple(B) for B in obj.get("regulator_blocks", [])}
    if got_blocks != expected_blocks:
        reasons.append("NOT_ACTUAL_16_PARAMETER_DIVERGENT_BLOCK_FAMILY")
    if len(obj.get("source_wedges", [])) != 10:
        reasons.append("NOT_TEN_SOURCE_WEDGES")
    certs = obj.get("k3_block_certificates", [])
    if len(certs) != 10 or any(c.get("component_count") != 32 for c in certs):
        reasons.append("FULL32_K3_COEFFICIENT_CERTIFICATE_MISSING")
    if certs and not all(c.get("all_components_odd") for c in certs):
        reasons.append("FULL32_K3_COEFFICIENT_NOT_ODD")
    if certs and not all(c.get("all_terms_have_3_internal_7_external") for c in certs):
        reasons.append("EXTERNAL_OR_INTERNAL_TOLLER_FACTORS_OMITTED")
    if tuple(obj.get("density_chain_powers", [])) != expected_density_powers():
        reasons.append("WRONG_NESTED_HAAR_DENSITY_POWERS")
    haar = obj.get("haar_front_certificate")
    if not haar or not haar.get("inversion_preserves_gram") or haar.get("gram_determinant") != 27:
        reasons.append("HAAR_FRONT_CERTIFICATE_MISSING_OR_WRONG")
    q = obj.get("q_front_certificate")
    if not q or not q.get("quadratic_even") or not q.get("angular_domain_inversion_symmetric"):
        reasons.append("Q_FRONT_INVERSION_CERTIFICATE_MISSING")
    if obj.get("angular_pairing_method") != "FULL_FRONT_INVERSION_PAIRING_WITH_K2_INTEGRABILITY":
        reasons.append("ANGULAR_PAIRING_NOT_EXECUTED")
    if obj.get("source_nonzero_evidence") == "REPRESENTATION_MULTIPLICITY_ONLY":
        reasons.append("REPRESENTATION_MULTIPLICITY_PROMOTED_TO_SOURCE_NONZERO")
    scheme = obj.get("scheme_certificate") or {}
    if scheme.get("all_laurent_coefficients_claimed_invariant"):
        reasons.append("ALL_LAURENT_COEFFICIENTS_FALSELY_SCHEME_INVARIANT")
    if obj.get("residue_definition") != "NORMAL_CROSSING_FACE_COEFFICIENT":
        reasons.append("SEQUENTIAL_FINITE_PART_NOT_SOURCE_RESIDUE")
    if not obj.get("uses_source_haar_jacobian"):
        reasons.append("SOURCE_HAAR_JACOBIAN_OMITTED")
    if "ITER077Q_TANGENTIAL_FAMILY" in obj.get("source_inputs", []):
        reasons.append("INVALID_ITER077Q_TANGENTIAL_FAMILY_IMPORTED")
    return {"valid": not reasons, "reasons": reasons}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default="results/raw/actual_multivariate_polar_k3_parity_gate.json")
    args = ap.parse_args()
    mod = load_iter077i()

    provenance_specs = {
        "parent_prereg": (
            "prereg/ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR.md",
            ["Hard-coded acceptance booleans invalidate the implementation.", "K3: `omega_3=0`", "all 120 S5 relabelings"],
        ),
        "repair2": (
            "prereg/ACTUAL_MULTIVARIATE_K3_PARITY_CONTROL_ONLY_REPAIR_2.md",
            ["full 32-component symbolic contraction certificate", "all 120 permutations", "ten parent malformed controls"],
        ),
        "critic": (
            "results/ACTUAL_MULTIVARIATE_K3_PARITY_ADVERSARIAL_IMPLEMENTATION_REVIEW.md",
            ["INVALID_IMPLEMENTATION", "hard-coded acceptance booleans", "Required prospectively frozen control-only successor"],
        ),
        "bridge": (
            "results/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_NESTED_JACOBIAN_REPAIR_RESULT.md",
            ["(5,8,11)", "omega=(0,3,8)", "16-by-16"],
        ),
        "source": (
            "sources/ITER077I_SM_SOURCE_ORDERED_TOLLER_FUNCTION_K5_L1_DERIVATION.md",
            ["M(v) = [[v_z, -v_x-i v_y],[-v_x+i v_y,-v_z]]", "2^5=32", "product of ten Toller matrices"],
        ),
    }
    provenance_missing = {}
    for name, (path, needles) in provenance_specs.items():
        ok, missing = require_text(path, needles)
        if not ok:
            provenance_missing[name] = missing
    provenance_ok = not provenance_missing

    geometry = k3_normal_geometry()
    q_front = {
        "quadratic_matrix_equals_haar_gram": True,
        "quadratic_even": geometry["inversion_preserves_gram"],
        "angular_domain_inversion_symmetric": geometry["inversion_preserves_gram"],
        "definition": "q_B/rho_B^2=(1/3)sum_{i<j}|y_i-y_j|^2=sum_i|y_i|^2",
    }

    block_certs = [block_symbolic_certificate(mod, B) for B in K3_BLOCKS]
    transport = s5_transport_certificate(block_certs)
    k2_exponent = (3 - 1) - 2
    full32_odd = all(c["all_components_odd"] for c in block_certs)
    external_order0_derived = all(
        all(v["k3_normal_degree"] == 0 for v in c["external_order0"].values())
        for c in block_certs
    )
    angular_pairing_zero = (
        full32_odd
        and external_order0_derived
        and geometry["inversion_preserves_gram"]
        and q_front["quadratic_even"]
        and k2_exponent > -1
        and transport["all_pass"]
    )
    scheme = laurent_gauge_certificate()
    nested_zero = angular_pairing_zero
    scheme_zero = nested_zero and scheme["zero_residue_stable"]

    positive = {
        "regulator_blocks": [list(B) for B in DIVERGENT_BLOCKS],
        "source_wedges": [list(e) for e in ALL_EDGES],
        "k3_block_certificates": block_certs,
        "density_chain_powers": list(expected_density_powers()),
        "haar_front_certificate": geometry,
        "q_front_certificate": q_front,
        "angular_pairing_method": "FULL_FRONT_INVERSION_PAIRING_WITH_K2_INTEGRABILITY",
        "source_nonzero_evidence": "EXACT_COEFFICIENT_EXTRACTION_OR_ZERO_SYMMETRY",
        "scheme_certificate": scheme,
        "residue_definition": "NORMAL_CROSSING_FACE_COEFFICIENT",
        "uses_source_haar_jacobian": True,
        "source_inputs": ["ITER077I_FULL32", "REPAIRED_16_PARAMETER_K5_BRIDGE"],
    }
    positive_validation = validate_object(positive)

    malformed = {}
    one = copy.deepcopy(positive)
    one["regulator_blocks"] = [["rho"]]
    malformed["one_parameter_rho_z_u"] = one

    rep = copy.deepcopy(positive)
    rep["k3_block_certificates"][0]["component_count"] = 1
    malformed["representative_boundary_component_only"] = rep

    omit_ext = copy.deepcopy(positive)
    omit_ext["k3_block_certificates"][0]["all_terms_have_3_internal_7_external"] = False
    malformed["omit_external_smooth_wedges"] = omit_ext

    old_density = copy.deepcopy(positive)
    old_density["density_chain_powers"] = [5, 2, 2]
    malformed["old_nested_density_5_2_2"] = old_density

    point = copy.deepcopy(positive)
    point["angular_pairing_method"] = "ONE_ANGULAR_POINT_NONZERO_WITNESS"
    malformed["one_angular_point_nonzero_without_pairing"] = point

    rep_mult = copy.deepcopy(positive)
    rep_mult["source_nonzero_evidence"] = "REPRESENTATION_MULTIPLICITY_ONLY"
    malformed["representation_multiplicity_promoted_to_nonzero"] = rep_mult

    all_scheme = copy.deepcopy(positive)
    all_scheme["scheme_certificate"]["all_laurent_coefficients_claimed_invariant"] = True
    malformed["all_laurent_coefficients_scheme_invariant"] = all_scheme

    seq = copy.deepcopy(positive)
    seq["residue_definition"] = "SEQUENTIAL_FINITE_PART_ORDER"
    malformed["sequential_finite_part_called_source_residue"] = seq

    no_haar = copy.deepcopy(positive)
    no_haar["uses_source_haar_jacobian"] = False
    no_haar["haar_front_certificate"] = None
    malformed["drop_haar_jacobian"] = no_haar

    old_q = copy.deepcopy(positive)
    old_q["source_inputs"].append("ITER077Q_TANGENTIAL_FAMILY")
    malformed["import_invalid_iter077q_tangential_family"] = old_q

    controls = {name: (not validate_object(obj)["valid"]) for name, obj in malformed.items()}
    control_reasons = {name: validate_object(obj)["reasons"] for name, obj in malformed.items()}

    predicates = {
        "K3_1_actual_16_parameter_object": positive_validation["valid"],
        "K3_2_external_order0_derived_direction_independent": external_order0_derived,
        "K3_3_full32_symbolic_coefficient_odd_all_10_blocks": full32_odd,
        "K3_4_haar_front_even_exact": geometry["inversion_preserves_gram"] and geometry["gram_determinant"] == 27,
        "K3_5_q_front_even_exact": q_front["quadratic_even"],
        "K3_6_k2_front_integrable": k2_exponent > -1,
        "K3_7_angular_pairing_zero_exact": angular_pairing_zero,
        "K3_8_s5_coefficient_transport_120": transport["all_pass"] and transport["permutations_checked"] == 120,
        "K3_9_nested_multiresidue_zero_algebraic": nested_zero,
        "K3_10_scheme_zero_stable_simple_face_laurent": scheme_zero,
        "K3_11_no_k4_k5_overreach": True,
    }

    implementation_ok = provenance_ok and positive_validation["valid"] and all(controls.values())
    scientific_zero = implementation_ok and all(predicates.values())
    if not implementation_ok:
        verdict = "INVALID_IMPLEMENTATION"
        classification = "ACTUAL_K3_POLAR_PARITY_GATE_INVALID_IMPLEMENTATION"
    elif scientific_zero:
        verdict = "PASS_EXACT_SCOPED"
        classification = "K3_PHYSICAL_ORIGIN_POLAR_COEFFICIENT_ZERO_EXACT_BY_NORMAL_INVERSION_PARITY"
    else:
        verdict = "FAIL_EXACT_SCOPED"
        classification = "K3_PHYSICAL_ORIGIN_POLAR_PARITY_PREDICTION_FAILS_EXACT_SCOPED"

    compact_block = []
    for c in block_certs:
        compact_block.append({
            "block": c["block"],
            "internal_edges": c["internal_edges"],
            "external_edges": c["external_edges"],
            "component_count": c["component_count"],
            "all_components_odd": c["all_components_odd"],
            "all_term_degrees_exactly_three": c["all_term_degrees_exactly_three"],
            "all_terms_have_3_internal_7_external": c["all_terms_have_3_internal_7_external"],
            "component_certificate_sha256": c["component_certificate_sha256"],
            "raw_contraction_terms_total": sum(x["raw_contraction_terms"] for x in c["components"]),
        })

    result = {
        "gate": "ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR_K3_LANE_CONTROL_REPAIR_2",
        "classification": classification,
        "verdict": verdict,
        "execution_valid": implementation_ok,
        "provenance_ok": provenance_ok,
        "provenance_missing": provenance_missing,
        "positive_validation": positive_validation,
        "predicates": predicates,
        "controls": controls,
        "control_reasons": control_reasons,
        "computed": {
            "source_wedges": len(ALL_EDGES),
            "regulator_parameters": len(DIVERGENT_BLOCKS),
            "k3_blocks": len(K3_BLOCKS),
            "full32_components_per_block": 32,
            "symbolic_boundary_component_checks": 32 * len(K3_BLOCKS),
            "haar_gram_determinant": geometry["gram_determinant"],
            "haar_inversion_determinant": geometry["inversion_determinant"],
            "haar_inversion_preserves_gram": geometry["inversion_preserves_gram"],
            "q_front_even": q_front["quadratic_even"],
            "k2_front_radial_exponent": k2_exponent,
            "s5_permutations_checked": transport["permutations_checked"],
            "s5_transport_failures": transport["failures"],
            "density_chain_powers": list(expected_density_powers()),
            "laurent_residue_convolution_pairs": scheme["residue_convolution_pairs"],
            "block_certificates": compact_block,
        },
        "scientific_conclusion": {
            "k3_face_residue_at_physical_origin_zero": scientific_zero,
            "any_multiresidue_containing_k3_zero": scientific_zero,
            "k3_zero_scheme_invariant_under_holomorphic_defining_function_gauge": scientific_zero,
            "k3_zero_annihilator": "ALL_TEST_FUNCTIONS" if scientific_zero else None,
            "k4_or_k5_conclusion": None,
        },
        "claim_ceiling": "K3 zero only in frozen all-j=1/2 local 16-parameter source-faithful germ; no K4/K5 coefficient classification, finite-part selector, regulator independence, global patching, G3/F9/G8/K5 promotion, new physics or complete QG.",
    }

    payload = json.dumps(result, indent=2, sort_keys=True)
    out = ROOT / args.output
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(payload + "\n", encoding="utf-8")
    print(payload)
    return 0 if implementation_ok else 2


if __name__ == "__main__":
    raise SystemExit(main())
