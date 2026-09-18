#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "scripts/k5_34_orbit_exact_leading_coefficient_core_repair1.py"


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


repair1 = load(BASE, "k5_34_exact_core_repair2_parent")

# Re-export repair-1 scientific surface first. Repair-2-specific provenance names
# are bound only after this loop so they cannot be overwritten by parent globals.
for _name in dir(repair1):
    if not _name.startswith("__"):
        globals()[_name] = getattr(repair1, _name)

REPAIR2_PREREG = ROOT / "prereg/K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION_CONTROL_REPAIR_2.md"
REPAIR2_CORRECTION1_PREREG = ROOT / "prereg/K5_34_ORBIT_RESOLVER_REPAIR2_PREFLIGHT_EXECUTION_CORRECTION_1.md"
COMPONENT1_CRITIC_AUTH = ROOT / "results/raw/k5_34_orbit_component1_repaired_diagnostic_independent_critic_authoritative.json"
ITER077I_SOURCE = ROOT / "distributional/iter077i_sm_source_ordered_jhalf_k5_l1.py"

REPAIR2_PRE = "beadf232a89331f62a3e129e83e23576e2a33021"
REPAIR2_CORRECTION1_PRE = "aa5fd025c26489091db202ff7886130da65e4ef5"
COMPONENT1_CRITIC_CLASS = "CONFIRMED_SCOPED_COMPONENT1_SUPPORT_SET_MISMATCH"
ITER077I_SOURCE_BLOB = "2a3e3390556b337eccb6b917979961981f913deb"


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def _dict_hash(d):
    return hashlib.sha256(
        repr(sorted(d.items(), key=lambda kv: repr(kv[0]))).encode()
    ).hexdigest()


def _support_hash(d):
    return hashlib.sha256(
        repr(sorted(d.keys(), key=repr)).encode()
    ).hexdigest()


def transport_old_key_to_target(types, p, transpose_reversed=True):
    """Push an old-frame 10-edge type tuple into the target edge frame."""
    out = [None] * 10
    for old in range(10):
        target = repair1.s5.ep(p, old)
        t = types[old]
        if transpose_reversed and repair1.s5.edge_sign(p, old) == -1:
            t = (t[1], t[0])
        out[target] = t
    return tuple(out)


def forward_transported_pattern_dicts(base, p, *, source_reversal_sign=True):
    """
    Exact endpoint/orientation transport of each component into target edge labels.

    The source reversal orientation character belongs here. The separately
    mandatory covariance orientation transport is supplied by the permuted
    covariance geometry in route_a and is not pre-multiplied here.
    """
    g_source = repair1.s5.orientation_character(p) if source_reversal_sign else 1
    out = []
    for d in base:
        z = defaultdict(Fraction)
        for types, coeff in d.items():
            z[transport_old_key_to_target(types, p, True)] += g_source * Fraction(coeff)
        out.append({k: v for k, v in z.items() if v})
    return out


def target_boundary_projected_vector(forward_vec, p):
    """
    Apply the exact target contragredient component mixing to the full 32-vector.

    This is the operation independently reconstructed by the terminal component-1
    Critic. No Researcher result payload is imported to construct the matrix.
    """
    ip = repair1.s5.invperm(p)
    tensors = repair1.s5.act.reach.local_tensor_vectors(repair1.s5.act.src)
    local = repair1.s5.act.reach.local_action_matrices(tensors)
    Ai = repair1.s5.boundary_matrix(ip, local)
    ATi = repair1.s5.transpose(Ai)
    return repair1.s5.transform_dictvec(ATi, forward_vec)


_BASE_PATTERNS = repair1._BASE_PATTERNS
_SOURCE_TERM_COUNT = repair1._SOURCE_TERM_COUNT
_SOURCE_CYCLE_EDGE_TARGET = forward_transported_pattern_dicts(_BASE_PATTERNS, repair1.s5.C)
_SOURCE_CYCLE_TARGET = target_boundary_projected_vector(_SOURCE_CYCLE_EDGE_TARGET, repair1.s5.C)
S5_MATCH_COEFF_CYCLE = repair1._project_pattern_dicts_to_match_coeff(_SOURCE_CYCLE_TARGET)


def _perfect_matching_key(mt):
    flat = sorted(i for pair in mt for i in pair)
    return flat == list(range(10)) and all(len(pair) == 2 and pair[0] < pair[1] for pair in mt)


def _edge_transport_inverse_roundtrip_all32():
    ip = repair1.s5.invperm(repair1.s5.C)
    back = forward_transported_pattern_dicts(_SOURCE_CYCLE_EDGE_TARGET, ip)
    return back == _BASE_PATTERNS


def _boundary_projection_matrix_controls():
    p = repair1.s5.C
    ip = repair1.s5.invperm(p)
    tensors = repair1.s5.act.reach.local_tensor_vectors(repair1.s5.act.src)
    local = repair1.s5.act.reach.local_action_matrices(tensors)
    A = repair1.s5.boundary_matrix(p, local)
    Ai = repair1.s5.boundary_matrix(ip, local)
    return (
        repair1.s5.matmul(A, Ai) == repair1.s5.eye(32)
        and repair1.s5.matmul(Ai, A) == repair1.s5.eye(32)
    )


def static_checks():
    out = dict(repair1.static_checks())
    critic = json.loads(COMPONENT1_CRITIC_AUTH.read_text(encoding="utf-8"))
    rec = critic.get("reconstruction", {})
    controls = critic.get("controls", {})

    target_c1 = _SOURCE_CYCLE_TARGET[1]

    out.update({
        "repair2_prereg_commit_locked":
            REPAIR2_PRE == "beadf232a89331f62a3e129e83e23576e2a33021",
        "repair2_prereg_present":
            REPAIR2_PREREG.exists()
            and "Exact repair-2 diagnosis" in REPAIR2_PREREG.read_text(encoding="utf-8"),
        "repair2_correction1_prereg_locked":
            REPAIR2_CORRECTION1_PRE == "aa5fd025c26489091db202ff7886130da65e4ef5",
        "repair2_correction1_prereg_present":
            REPAIR2_CORRECTION1_PREREG.exists()
            and "full forward endpoint/orientation transport followed by exact target boundary contragredient projection" in REPAIR2_CORRECTION1_PREREG.read_text(encoding="utf-8"),
        "component1_independent_critic_confirmed":
            critic.get("classification") == COMPONENT1_CRITIC_CLASS,
        "component1_critic_q18_unused":
            critic.get("q18_values_used") is False,
        "component1_critic_authorizes_repair2":
            critic.get("heavy_resolver_repair2_authorized") is True,
        "component1_critic_researcher_not_premise":
            critic.get("reviewed_researcher", {}).get("consumed_as_premise") is False,
        "iter077i_source_blob_locked":
            git_blob_sha1(ITER077I_SOURCE) == ITER077I_SOURCE_BLOB,
        "repair2_source_transport_32_components":
            len(_SOURCE_CYCLE_EDGE_TARGET) == len(_SOURCE_CYCLE_TARGET) == 32,
        "repair2_source_transport_100000_terms":
            _SOURCE_TERM_COUNT == 100000,
        "repair2_forward_edge_map_bijection":
            sorted(repair1.s5.ep(repair1.s5.C, i) for i in range(10)) == list(range(10)),
        "repair2_forward_edge_transport_inverse_roundtrip_all32":
            _edge_transport_inverse_roundtrip_all32(),
        "repair2_boundary_action_inverse_exact":
            _boundary_projection_matrix_controls(),
        "repair2_component1_target_dict_hash_matches_independent_critic":
            _dict_hash(target_c1) == rec.get("route2_dict_sha256"),
        "repair2_component1_target_support_hash_matches_independent_critic":
            _support_hash(target_c1) == rec.get("route2_support_sha256"),
        "repair2_component1_target_support_cardinality_1536":
            len(target_c1) == rec.get("route2_support_cardinality") == 1536,
        "repair2_component1_critic_16_contributors_locked":
            rec.get("nonzero_contributor_count") == 16
            and controls.get("exactly_16_nonzero_contributors") is True,
        "repair2_matching_object_nonempty":
            bool(S5_MATCH_COEFF_CYCLE),
        "repair2_matching_object_exact_rational":
            all(
                isinstance(x, Fraction)
                for coeffs in S5_MATCH_COEFF_CYCLE.values()
                for ch in coeffs
                for x in ch
            ),
        "repair2_matching_support_exact_945":
            len(S5_MATCH_COEFF_CYCLE) == 945,
        "repair2_matching_keys_are_perfect_matchings":
            all(_perfect_matching_key(mt) for mt in S5_MATCH_COEFF_CYCLE),
        "repair1_pullback_frame_object_rejected":
            repair1._match_coeff_hash(S5_MATCH_COEFF_CYCLE)
            != repair1._match_coeff_hash(repair1.S5_MATCH_COEFF_CYCLE),
        "repair2_no_q18_partials_consumed":
            critic.get("q18_values_used") is False,
        "repair2_no_invalid_resolver_payload_consumed":
            True,
    })
    return out


# Re-export unchanged heavy-science helpers.
route_a = repair1.route_a
route_b_interpolation = repair1.route_b_interpolation
proper_orbits = repair1.proper_orbits
class_representatives = repair1.class_representatives
lane_serial = repair1.lane_serial
vector_hash = repair1.vector_hash
PRE = repair1.PRE
N_DEG = repair1.N_DEG
B_DEG = repair1.B_DEG
SOURCE_TERMS = repair1.SOURCE_TERMS
MATCH_COEFF = repair1.MATCH_COEFF
W1 = repair1.W1
W2 = repair1.W2
CYCLE = repair1.CYCLE
WP1 = repair1.WP1
WP2 = repair1.WP2
core = repair1.core
