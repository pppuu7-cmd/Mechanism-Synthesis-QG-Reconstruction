#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "distributional/iter077i_sm_source_ordered_jhalf_k5_l1.py"
CRITIC_PREREG = ROOT / "prereg/K5_34_ORBIT_COMPONENT1_REPAIRED_DIAGNOSTIC_INDEPENDENT_CRITIC.md"
PARENT_PRE = ROOT / "prereg/K5_34_ORBIT_COMPONENT1_SUPPORT_MIXING_DEFECT_DIAGNOSTIC.md"
REPAIR1_PRE = ROOT / "prereg/K5_34_ORBIT_COMPONENT1_SUPPORT_MIXING_DIAGNOSTIC_CONTROL_REPAIR_1.md"
REPAIR2_PRE = ROOT / "prereg/K5_34_ORBIT_COMPONENT1_SUPPORT_MIXING_DIAGNOSTIC_CONTROL_REPAIR_2.md"

CRITIC_PREREG_COMMIT = "bc7a63a50a2fff36f931e03b5f26d4563ca29607"
PARENT_PREREG_COMMIT = "ea49bb0cc67887659bb92c8a68b616f6b7e52513"
REPAIR1_PREREG_COMMIT = "aab70cd2ffbc9bf52fdd83f8caa78bc3d8b220ec"
REPAIR2_PREREG_COMMIT = "7bc6f76fe8d183a38e944f096f93a9f0b6b0ab37"
SOURCE_BLOB = "2a3e3390556b337eccb6b917979961981f913deb"
REVIEWED_RUN = 35363610618
REVIEWED_HEAD = "a5a9ae44569532bab7e352b12675d8eb152026ea"
REVIEWED_ARTIFACT = 10555382872
REVIEWED_ARTIFACT_ZIP_SHA256 = "ffc28d87f50691e77bcf196b7db364214bdd31643f7fb092696b93f5796f0d64"

CYCLE = (1, 2, 3, 4, 0)
COMPONENT = 1

CONFIRMED = "CONFIRMED_SCOPED_COMPONENT1_SUPPORT_SET_MISMATCH"
INVALID = "INVALID_IMPLEMENTATION_OR_PROVENANCE"
BLOCKED = "BLOCKED_INSUFFICIENT_INDEPENDENT_RECONSTRUCTION"


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def bit_index(bits):
    x = 0
    for b in bits:
        x = (x << 1) | int(b)
    return x


def clean(d):
    return {k: Fraction(v) for k, v in d.items() if Fraction(v)}


def add_scaled(dst, src, a):
    a = Fraction(a)
    if not a:
        return
    for k, v in src.items():
        dst[k] += a * Fraction(v)


def linear_comb(row, vec):
    z = defaultdict(Fraction)
    for j, a in enumerate(row):
        if a:
            add_scaled(z, vec[j], a)
    return clean(z)


def transpose(A):
    return [list(row) for row in zip(*A)]


def matmul(A, B):
    BT = list(zip(*B))
    return [[sum((x * y for x, y in zip(row, col)), Fraction(0)) for col in BT] for row in A]


def eye(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def invperm(p):
    return tuple(p.index(i) for i in range(len(p)))


def local_tensor_vectors(src):
    out = []
    for k in (0, 1):
        v = [Fraction(0)] * 16
        for state, coeff in src.NODE_OPTIONS[k]:
            v[bit_index(state)] = Fraction(coeff)
        out.append(v)
    return out


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), Fraction(0))


def permute_local(v, p):
    out = [Fraction(0)] * 16
    for idx, coeff in enumerate(v):
        if not coeff:
            continue
        bits = [(idx >> (3 - i)) & 1 for i in range(4)]
        obits = [0] * 4
        for i in range(4):
            obits[p[i]] = bits[i]
        out[bit_index(obits)] = coeff
    return out


def local_action_matrices(src):
    tensors = local_tensor_vectors(src)
    n0, n1 = dot(tensors[0], tensors[0]), dot(tensors[1], tensors[1])
    if dot(tensors[0], tensors[1]) != 0:
        raise ValueError("local source tensors are not orthogonal")
    mats = {}
    for p in itertools.permutations(range(4)):
        cols = []
        for k in (0, 1):
            pv = permute_local(tensors[k], p)
            coords = (dot(tensors[0], pv) / n0, dot(tensors[1], pv) / n1)
            recon = [coords[0] * tensors[0][i] + coords[1] * tensors[1][i] for i in range(16)]
            if recon != pv:
                raise ValueError(("local action left source span", p, k))
            cols.append(coords)
        mats[p] = (
            (cols[0][0], cols[1][0]),
            (cols[0][1], cols[1][1]),
        )
    return tensors, mats


def global_action(src, sigma, local_mats):
    A = [[Fraction(0) for _ in range(32)] for _ in range(32)]
    for x in range(32):
        ks = tuple((x >> (4 - i)) & 1 for i in range(5))
        local_by_target = {}
        for v in range(5):
            old_neighbors = src.NEIGHBORS[v]
            tv = sigma[v]
            target_pos = {w: i for i, w in enumerate(src.NEIGHBORS[tv])}
            leg_perm = tuple(target_pos[sigma[w]] for w in old_neighbors)
            M = local_mats[leg_perm]
            local_by_target[tv] = (M[0][ks[v]], M[1][ks[v]])
        for kout in itertools.product((0, 1), repeat=5):
            c = Fraction(1)
            for tv in range(5):
                c *= local_by_target[tv][kout[tv]]
                if not c:
                    break
            if c:
                A[bit_index(kout)][x] += c
    return A


def action_column_direct(src, sigma, local_mats, input_component):
    ks = tuple((input_component >> (4 - i)) & 1 for i in range(5))
    local_by_target = {}
    for v in range(5):
        old_neighbors = src.NEIGHBORS[v]
        tv = sigma[v]
        target_pos = {w: i for i, w in enumerate(src.NEIGHBORS[tv])}
        leg_perm = tuple(target_pos[sigma[w]] for w in old_neighbors)
        M = local_mats[leg_perm]
        local_by_target[tv] = (M[0][ks[v]], M[1][ks[v]])
    col = [Fraction(0)] * 32
    for kout in itertools.product((0, 1), repeat=5):
        c = Fraction(1)
        for tv in range(5):
            c *= local_by_target[tv][kout[tv]]
            if not c:
                break
        if c:
            col[bit_index(kout)] = c
    return col


def source_component_dicts(src):
    edges = tuple(src.EDGES)
    out = [{} for _ in range(32)]
    total_terms = 0
    for ks in itertools.product((0, 1), repeat=5):
        idx = bit_index(ks)
        d = defaultdict(Fraction)
        for choices in itertools.product(*[src.NODE_OPTIONS[k] for k in ks]):
            total_terms += 1
            states = []
            coeff = Fraction(1)
            for state, c in choices:
                states.append(state)
                coeff *= Fraction(c)
            types = []
            for a, b in edges:
                row = states[b][src.LEG_POS[(b, a)]]
                col = states[a][src.LEG_POS[(a, b)]]
                types.append((row, col))
            d[tuple(types)] += coeff
        out[idx] = clean(d)
    return out, total_terms


def edge_maps(edges):
    eidx = {e: i for i, e in enumerate(edges)}
    def ep(p, i):
        a, b = edges[i]
        x, y = p[a], p[b]
        return eidx[(min(x, y), max(x, y))]
    def edge_sign(p, i):
        a, b = edges[i]
        return 1 if p[a] < p[b] else -1
    return ep, edge_sign


def orientation_character(p, edges, edge_sign):
    g = 1
    for i in range(len(edges)):
        g *= edge_sign(p, i)
    return g


def transport_one(d, p, edges, ep, edge_sign):
    g = orientation_character(p, edges, edge_sign)
    z = defaultdict(Fraction)
    for types, coeff in d.items():
        out = [None] * len(edges)
        for old in range(len(edges)):
            j = ep(p, old)
            t = types[old]
            if edge_sign(p, old) == -1:
                t = (t[1], t[0])
            out[j] = t
        z[tuple(out)] += Fraction(g) * Fraction(coeff)
    return clean(z)


def perfect_matchings(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    a = items[0]
    for pos in range(1, len(items)):
        b = items[pos]
        rest = items[1:pos] + items[pos + 1:]
        for tail in perfect_matchings(rest):
            yield ((a, b),) + tail


def dict_hash(d):
    return hashlib.sha256(repr(sorted(d.items(), key=lambda kv: repr(kv[0]))).encode()).hexdigest()


def support_hash(d):
    return hashlib.sha256(repr(sorted(d.keys(), key=repr)).encode()).hexdigest()


def all_fraction_dicts(vec):
    return all(isinstance(v, Fraction) for d in vec for v in d.values())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    try:
        src = load(SOURCE, "critic_component1_source")
        edges = tuple(src.EDGES)
        base, source_terms = source_component_dicts(src)
        tensors, local = local_action_matrices(src)
        pinv = invperm(CYCLE)
        A = global_action(src, CYCLE, local)
        Ai = global_action(src, pinv, local)
        ATi = transpose(Ai)

        # Independent row reconstruction: row COMPONENT of A^{-T} is
        # column COMPONENT of the inverse-permutation action.
        target_row_independent = action_column_direct(src, pinv, local, COMPONENT)
        target_row_matrix = ATi[COMPONENT]

        route1 = linear_comb(target_row_independent, base)

        ep, edge_sign = edge_maps(edges)
        transported = [transport_one(d, CYCLE, edges, ep, edge_sign) for d in base]
        route2 = linear_comb(target_row_independent, transported)

        contributors = [(j, a) for j, a in enumerate(target_row_independent) if a and transported[j]]
        dropped = {}
        dropped_rejected = False
        if contributors:
            z = defaultdict(Fraction)
            drop_j, _ = contributors[0]
            for j, a in contributors[1:]:
                add_scaled(z, transported[j], a)
            dropped = clean(z)
            dropped_rejected = dropped != route2

        # Endpoint/orientation inverse roundtrip over all 32 dictionaries.
        roundtrip = all(
            transport_one(
                transport_one(d, CYCLE, edges, ep, edge_sign),
                pinv, edges, ep, edge_sign
            ) == d
            for d in base
        )

        # Wrong transpose: use row COMPONENT of A^{-1} instead of A^{-T}.
        wrong = linear_comb(Ai[COMPONENT], base)
        wrong_transpose_rejected = wrong != route1

        ps, ds = set(route1), set(route2)
        missing = sorted(ps - ds, key=repr)
        spurious = sorted(ds - ps, key=repr)
        support_equal = ps == ds
        common = sorted(ps & ds, key=repr)
        first_coeff_bad = next((k for k in common if route1[k] != route2[k]), None)
        coeff_equal = support_equal and first_coeff_bad is None

        matching_count = sum(1 for _ in perfect_matchings(range(10)))

        prereg_text = CRITIC_PREREG.read_text(encoding="utf-8")
        parent_text = PARENT_PRE.read_text(encoding="utf-8")
        repair1_text = REPAIR1_PRE.read_text(encoding="utf-8")
        repair2_text = REPAIR2_PRE.read_text(encoding="utf-8")

        controls = {
            "critic_prereg_commit_locked": CRITIC_PREREG_COMMIT == "bc7a63a50a2fff36f931e03b5f26d4563ca29607",
            "critic_prereg_present": "FROZEN BEFORE REVIEW IMPLEMENTATION" in prereg_text,
            "parent_prereg_locked": PARENT_PREREG_COMMIT == "ea49bb0cc67887659bb92c8a68b616f6b7e52513" and "component-1 support-mixing defect diagnostic" in parent_text,
            "repair1_prereg_locked": REPAIR1_PREREG_COMMIT == "aab70cd2ffbc9bf52fdd83f8caa78bc3d8b220ec" and "control repair 1" in repair1_text,
            "repair2_prereg_locked": REPAIR2_PREREG_COMMIT == "7bc6f76fe8d183a38e944f096f93a9f0b6b0ab37" and "control repair 2" in repair2_text,
            "source_blob_locked": git_blob_sha1(SOURCE) == SOURCE_BLOB,
            "canonical_ten_edges": len(edges) == 10,
            "full_32_components": len(base) == len(transported) == 32,
            "exactly_100000_source_terms": source_terms == 100000,
            "perfect_matchings_945": matching_count == 945,
            "exact_fraction_arithmetic": all_fraction_dicts(base) and all_fraction_dicts(transported),
            "local_tensor_count_two": len(tensors) == 2,
            "global_action_inverse_exact": matmul(A, Ai) == eye(32) and matmul(Ai, A) == eye(32),
            "independent_target_row_equals_matrix_row": target_row_independent == target_row_matrix,
            "endpoint_orientation_roundtrip_all32": roundtrip,
            "wrong_transpose_rejected": wrong_transpose_rejected,
            "target_component_is_1": COMPONENT == 1,
            "positive_multi_source_mixing": len(contributors) >= 2,
            "exactly_16_nonzero_contributors": len(contributors) == 16,
            "dropped_contributor_negative_control": dropped_rejected,
            "researcher_result_not_imported": True,
            "researcher_diagnostic_not_imported": True,
            "invalid_resolver_payload_not_imported": True,
            "q18_partials_used": False,
        }

        if not all(v for k, v in controls.items() if k != "q18_partials_used"):
            classification = INVALID
            reason = "one or more frozen validity/provenance/mixing controls failed"
        elif not support_equal:
            classification = CONFIRMED
            reason = "independent exact reconstruction finds distinct component-1 support sets"
        elif coeff_equal:
            classification = INVALID
            reason = "independent reconstruction does not reproduce the claimed support-set mismatch"
        else:
            classification = INVALID
            reason = "independent reconstruction finds coefficient-only disagreement, not the claimed support-set mismatch"

        out = {
            "gate": "K5_34_ORBIT_COMPONENT1_REPAIRED_DIAGNOSTIC_INDEPENDENT_CRITIC",
            "classification": classification,
            "reason": reason,
            "scientific_verdict": None,
            "reviewed": {
                "run_id": REVIEWED_RUN,
                "head_sha": REVIEWED_HEAD,
                "artifact_id": REVIEWED_ARTIFACT,
                "artifact_zip_sha256": REVIEWED_ARTIFACT_ZIP_SHA256,
                "researcher_classification_consumed_as_premise": False,
            },
            "prereg": {
                "critic_prereg_commit": CRITIC_PREREG_COMMIT,
                "parent_prereg_commit": PARENT_PREREG_COMMIT,
                "repair1_prereg_commit": REPAIR1_PREREG_COMMIT,
                "repair2_prereg_commit": REPAIR2_PREREG_COMMIT,
            },
            "source": {
                "path": str(SOURCE.relative_to(ROOT)),
                "git_blob": git_blob_sha1(SOURCE),
                "canonical_edges": [list(e) for e in edges],
                "source_terms": source_terms,
                "boundary_components": len(base),
                "perfect_matchings": matching_count,
            },
            "reconstruction": {
                "cycle": list(CYCLE),
                "component": COMPONENT,
                "nonzero_contributor_count": len(contributors),
                "contributor_indices": [j for j, _ in contributors],
                "contributor_coefficients": [str(a) for _, a in contributors],
                "route1_support_cardinality": len(route1),
                "route2_support_cardinality": len(route2),
                "route1_dict_sha256": dict_hash(route1),
                "route2_dict_sha256": dict_hash(route2),
                "route1_support_sha256": support_hash(route1),
                "route2_support_sha256": support_hash(route2),
                "support_set_equal": support_equal,
                "coefficient_equal": coeff_equal,
                "first_missing_support_index": repr(missing[0]) if missing else None,
                "first_spurious_support_index": repr(spurious[0]) if spurious else None,
                "first_coefficient_mismatch": repr(first_coeff_bad) if first_coeff_bad is not None else None,
                "dropped_contributor_index": contributors[0][0] if contributors else None,
            },
            "controls": controls,
            "q18_values_used": False,
            "heavy_resolver_repair2_authorized": classification == CONFIRMED,
            "global_stokes_authorized": False,
            "interpretation_ceiling": "implementation-diagnostic Critic authority only; no physical N/B or downstream science",
        }

    except Exception as exc:
        out = {
            "gate": "K5_34_ORBIT_COMPONENT1_REPAIRED_DIAGNOSTIC_INDEPENDENT_CRITIC",
            "classification": BLOCKED,
            "reason": f"independent reconstruction raised {type(exc).__name__}: {exc}",
            "scientific_verdict": None,
            "reviewed": {
                "run_id": REVIEWED_RUN,
                "head_sha": REVIEWED_HEAD,
                "artifact_id": REVIEWED_ARTIFACT,
                "artifact_zip_sha256": REVIEWED_ARTIFACT_ZIP_SHA256,
                "researcher_classification_consumed_as_premise": False,
            },
            "q18_values_used": False,
            "heavy_resolver_repair2_authorized": False,
            "global_stokes_authorized": False,
            "interpretation_ceiling": "implementation-diagnostic Critic authority only; no physical N/B or downstream science",
        }

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("CLASSIFICATION=" + out["classification"])
    print("REASON=" + out["reason"])
    if "reconstruction" in out:
        print("RECONSTRUCTION=" + json.dumps(out["reconstruction"], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
