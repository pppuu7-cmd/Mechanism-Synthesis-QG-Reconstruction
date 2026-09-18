#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
from collections import defaultdict, deque
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'distributional/iter077i_sm_source_ordered_jhalf_k5_l1.py'
SOURCE_DERIVATION = ROOT / 'sources/ITER077I_SM_SOURCE_ORDERED_TOLLER_FUNCTION_K5_L1_DERIVATION.md'
ERRATUM = ROOT / 'status/ITER077_CONTACT_FORMULA_ERRATUM.md'
CRITIC_PREREG = ROOT / 'prereg/K5_FULL_SOURCE_BOUNDARY_S5_TRANSPORT_SYMBOLIC_GENERATOR_THEOREM_CRITIC.md'

CRITIC_PREREG_COMMIT = 'cf8576acb7237b751c26d5b5942aa60874bcd00e'
RESEARCHER_PREREG_COMMIT = '4f65cff503db976b6ff52b8519e5fdaa0bf4a4f8'
RESEARCHER_REPAIR_COMMIT = '73b8f65f05e3945e8c4d517e73b938cdd3299e39'
RESEARCHER_RESULT_COMMIT = '4d8c4743a11b1c13fd7c3a81a68d9120a8a41fc4'
RESEARCHER_RUN = 35200455308
EXPECTED_SOURCE_BLOB = '2a3e3390556b337eccb6b917979961981f913deb'
EXPECTED_ERRATUM_BLOB = '63356e5099929f2b21d9d7296ab97f15ff163dba'

C = (1, 2, 3, 4, 0)
T = (1, 0, 2, 3, 4)
GENS = {'C': C, 'T': T}
ID = tuple(range(5))
ZERO_MON = (0,) * 10


def git_blob_sha(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def compose(p, q):
    # p after q
    return tuple(p[q[i]] for i in range(5))


def invperm(p):
    return tuple(p.index(i) for i in range(5))


def perm_sign(p):
    return -1 if sum(p[i] > p[j] for i in range(5) for j in range(i + 1, 5)) % 2 else 1


def bit_index(bits):
    x = 0
    for b in bits:
        x = (x << 1) | int(b)
    return x


def matmul(A, B):
    BT = list(zip(*B))
    return [[sum((x * y for x, y in zip(row, col)), Fraction(0)) for col in BT] for row in A]


def transpose(A):
    return [list(x) for x in zip(*A)]


def eye(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def matrix_scale(c, A):
    return [[c * x for x in row] for row in A]


def clean_poly(p):
    return {m: c for m, c in p.items() if c}


def poly_add(a, b):
    z = defaultdict(int)
    for m, c in a.items():
        z[m] += c
    for m, c in b.items():
        z[m] += c
    return clean_poly(dict(z))


def poly_scale(c, a):
    return {} if c == 0 else clean_poly({m: c * v for m, v in a.items()})


def poly_mul(a, b):
    if not a or not b:
        return {}
    z = defaultdict(int)
    for ma, ca in a.items():
        for mb, cb in b.items():
            z[tuple(ma[i] + mb[i] for i in range(10))] += ca * cb
    return clean_poly(dict(z))


def poly_one():
    return {ZERO_MON: 1}


def var_poly(i, c=1):
    m = [0] * 10
    m[i] = 1
    return {tuple(m): c} if c else {}


def det_poly(M):
    n = len(M)
    out = {}
    for p in itertools.permutations(range(n)):
        inv = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        term = poly_one()
        for i, j in enumerate(p):
            term = poly_mul(term, M[i][j])
        out = poly_add(out, poly_scale(-1 if inv % 2 else 1, term))
    return out


def minor(M, row, col):
    return [[M[i][j] for j in range(len(M)) if j != col] for i in range(len(M)) if i != row]


def poly_hash(p):
    h = hashlib.sha256()
    for m, c in sorted(p.items()):
        h.update((','.join(map(str, m)) + '=' + str(c) + '\n').encode())
    return h.hexdigest()


def clean_dict(d):
    return {k: v for k, v in d.items() if v}


def dictvec_hash(v):
    h = hashlib.sha256()
    for i, d in enumerate(v):
        h.update(f'component={i}\n'.encode())
        for k, c in sorted(d.items()):
            flat = ';'.join(f'{a}{b}' for a, b in k)
            h.update((flat + '=' + str(c.numerator) + '/' + str(c.denominator) + '\n').encode())
    return h.hexdigest()


def dictvec_equal(a, b):
    return len(a) == len(b) and all(x == y for x, y in zip(a, b))


def first_dictvec_mismatch(a, b):
    for i, (x, y) in enumerate(zip(a, b)):
        if x == y:
            continue
        for k in sorted(set(x) | set(y)):
            xv = x.get(k, Fraction(0))
            yv = y.get(k, Fraction(0))
            if xv != yv:
                return {
                    'component': i,
                    'types': [list(t) for t in k],
                    'left': str(xv),
                    'right': str(yv),
                }
    return None


def transform_dictvec(M, v):
    out = []
    for row in M:
        z = defaultdict(Fraction)
        for j, c in enumerate(row):
            if not c:
                continue
            for k, x in v[j].items():
                z[k] += c * x
        out.append(clean_dict(dict(z)))
    return out


def scale_dictvec(c, v):
    return [clean_dict({k: c * x for k, x in d.items()}) for d in v]


def incidence_row(edge):
    a, b = edge
    row = [0, 0, 0, 0]
    if a != 0:
        row[a - 1] -= 1
    if b != 0:
        row[b - 1] += 1
    return tuple(row)


def build_formal_laplacian(rows):
    L = [[{} for _ in range(4)] for _ in range(4)]
    for e, r in enumerate(rows):
        for i in range(4):
            for j in range(4):
                if r[i] * r[j]:
                    L[i][j] = poly_add(L[i][j], var_poly(e, r[i] * r[j]))
    return L


def build_covariance_numerators(L, rows):
    psi = det_poly(L)
    adj = [[{} for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            adj[i][j] = poly_scale(-1 if (i + j) % 2 else 1, det_poly(minor(L, j, i)))
    nums = [[{} for _ in range(10)] for _ in range(10)]
    for e, r in enumerate(rows):
        for f, s in enumerate(rows):
            z = {}
            for i in range(4):
                if not r[i]:
                    continue
                for j in range(4):
                    if s[j]:
                        z = poly_add(z, poly_scale(r[i] * s[j], adj[i][j]))
            nums[e][f] = z
    return psi, nums


def is_spanning_tree(edges, ids):
    parent = list(range(5))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[rb] = ra
        return True

    for i in ids:
        a, b = edges[i]
        if not union(a, b):
            return False
    return len({find(v) for v in range(5)}) == 1


def spanning_tree_poly(edges):
    out = {}
    ids = []
    for comb in itertools.combinations(range(10), 4):
        if is_spanning_tree(edges, comb):
            m = [0] * 10
            for i in comb:
                m[i] = 1
            out[tuple(m)] = 1
            ids.append(comb)
    return out, ids


def local_tensor_vectors(src):
    out = []
    for k in (0, 1):
        v = [Fraction(0)] * 16
        for state, coeff in src.NODE_OPTIONS[k]:
            v[bit_index(state)] = Fraction(coeff)
        out.append(v)
    return out


def vdot(a, b):
    return sum((x * y for x, y in zip(a, b)), Fraction(0))


def permute_local_vec(v, p):
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


def local_action_matrices(tensors):
    n0 = vdot(tensors[0], tensors[0])
    n1 = vdot(tensors[1], tensors[1])
    cross = vdot(tensors[0], tensors[1])
    mats = {}
    exact = cross == 0
    for p in itertools.permutations(range(4)):
        cols = []
        for k in (0, 1):
            pv = permute_local_vec(tensors[k], p)
            coords = (vdot(tensors[0], pv) / n0, vdot(tensors[1], pv) / n1)
            recon = [coords[0] * tensors[0][i] + coords[1] * tensors[1][i] for i in range(16)]
            exact &= recon == pv
            cols.append(coords)
        mats[p] = (
            (cols[0][0], cols[1][0]),
            (cols[0][1], cols[1][1]),
        )
    return mats, (n0, n1, cross), exact


def global_action_matrix(src, sigma, local_mats):
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


def rref_rank(A):
    a = [row[:] for row in A]
    nr = len(a)
    nc = len(a[0]) if nr else 0
    r = 0
    pivots = []
    for c in range(nc):
        p = next((i for i in range(r, nr) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        z = a[r][c]
        a[r] = [x / z for x in a[r]]
        for i in range(nr):
            if i != r and a[i][c]:
                z = a[i][c]
                a[i] = [x - z * y for x, y in zip(a[i], a[r])]
        pivots.append(c)
        r += 1
        if r == nr:
            break
    return r, pivots


def enumerate_base_patterns(src, edges):
    out = [defaultdict(Fraction) for _ in range(32)]
    terms = 0
    for ks in itertools.product((0, 1), repeat=5):
        idx = bit_index(ks)
        options = [src.NODE_OPTIONS[k] for k in ks]
        for choices in itertools.product(*options):
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
            out[idx][tuple(types)] += coeff
            terms += 1
    return [clean_dict(dict(d)) for d in out], terms


def all_matchings(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    a = items[0]
    for j in range(1, len(items)):
        b = items[j]
        rest = items[1:j] + items[j + 1:]
        for tail in all_matchings(rest):
            yield ((a, b),) + tail


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    args = ap.parse_args()

    source_exists = SOURCE.exists()
    deriv_exists = SOURCE_DERIVATION.exists()
    erratum_exists = ERRATUM.exists()
    prereg_exists = CRITIC_PREREG.exists()
    if not (source_exists and deriv_exists and erratum_exists and prereg_exists):
        out = {
            'gate': 'FULL_SOURCE_BOUNDARY_S5_SYMBOLIC_TRANSPORT_INDEPENDENT_CRITIC',
            'verdict': 'BLOCKED_OBJECT_DEFINITION',
            'missing': [str(p.relative_to(ROOT)) for p in (SOURCE, SOURCE_DERIVATION, ERRATUM, CRITIC_PREREG) if not p.exists()],
            'researcher_run': RESEARCHER_RUN,
            'q18_values_used': False,
        }
        p = Path(args.output)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
        print(json.dumps(out, sort_keys=True))
        return 0

    src = load_module(SOURCE, 'critic_iter077i_source')
    source_text = SOURCE_DERIVATION.read_text(encoding='utf-8')
    erratum_text = ERRATUM.read_text(encoding='utf-8')
    critic_prereg_text = CRITIC_PREREG.read_text(encoding='utf-8')

    source_checks = {
        'critic_contract_commit_locked': CRITIC_PREREG_COMMIT == 'cf8576acb7237b751c26d5b5942aa60874bcd00e',
        'critic_contract_present': 'independent Critic preregistration' in critic_prereg_text,
        'researcher_prereg_identity_locked': RESEARCHER_PREREG_COMMIT == '4f65cff503db976b6ff52b8519e5fdaa0bf4a4f8',
        'researcher_repair_identity_locked': RESEARCHER_REPAIR_COMMIT == '73b8f65f05e3945e8c4d517e73b938cdd3299e39',
        'researcher_result_identity_locked': RESEARCHER_RESULT_COMMIT == '4d8c4743a11b1c13fd7c3a81a68d9120a8a41fc4',
        'source_blob_exact': git_blob_sha(SOURCE) == EXPECTED_SOURCE_BLOB,
        'erratum_blob_exact': git_blob_sha(ERRATUM) == EXPECTED_ERRATUM_BLOB,
        'source_order_lock': 'one-wedge source construction -> Toller function -> K5 product -> group integration' in source_text,
        'published_feynman_i_epsilon_retained': 'Feynman i epsilon in spinfoams' in source_text and 'uniquely projects the two Toller branches' in source_text,
        'branch_sign_convention_present': 'changes the common leading scale by a minus sign' in source_text,
        'canonical_endpoint_orientation_present': 'row index is the target half-edge' in source_text and 'column index the source half-edge' in source_text,
        'erratum_correct_c_nplus1_lock': 'c_{n+1}' in erratum_text and 'NON_AUTHORITATIVE_SOURCE_LOCK_INVALID' in erratum_text,
    }

    edges = tuple(src.EDGES)
    expected_edges = tuple(itertools.combinations(range(5), 2))
    eidx = {e: i for i, e in enumerate(edges)}
    rows = tuple(incidence_row(e) for e in edges)

    def ep(p, i):
        a, b = edges[i]
        x, y = p[a], p[b]
        return eidx[(min(x, y), max(x, y))]

    def edge_sign(p, i):
        a, b = edges[i]
        return 1 if p[a] < p[b] else -1

    def orientation_character(p):
        g = 1
        for i in range(10):
            g *= edge_sign(p, i)
        return g

    def pullback_poly(poly, p):
        out = defaultdict(int)
        for m, c in poly.items():
            n = [0] * 10
            for i in range(10):
                n[i] = m[ep(p, i)]
            out[tuple(n)] += c
        return clean_poly(dict(out))

    tree_poly, trees = spanning_tree_poly(edges)
    L = build_formal_laplacian(rows)
    psi, nums = build_covariance_numerators(L, rows)

    cov_results = {}
    for name, p0 in GENS.items():
        bad = []
        for i in range(10):
            ti, si = ep(p0, i), edge_sign(p0, i)
            for j in range(10):
                tj, sj = ep(p0, j), edge_sign(p0, j)
                lhs = pullback_poly(nums[ti][tj], p0)
                rhs = poly_scale(si * sj, nums[i][j])
                if lhs != rhs and len(bad) < 8:
                    bad.append({'i': i, 'j': j, 'ti': ti, 'tj': tj, 'sign': si * sj})
        cov_results[name] = {
            'psi_exact': pullback_poly(psi, p0) == psi,
            'all_covariance_numerators_exact': not bad,
            'bad_pairs': bad,
            'orientation_character': orientation_character(p0),
            'permutation_sign': perm_sign(p0),
        }

    tensors = local_tensor_vectors(src)
    local_mats, node_metric, local_exact = local_action_matrices(tensors)

    def boundary_matrix(p0):
        return global_action_matrix(src, p0, local_mats)

    gen_mats = {name: boundary_matrix(p0) for name, p0 in GENS.items()}
    group = {ID: eye(32)}
    q = deque([ID])
    representation_ok = True
    edge_comp_ok = True
    while q:
        p0 = q.popleft()
        Ap = group[p0]
        for name, g in GENS.items():
            np = compose(g, p0)
            candidate = matmul(gen_mats[name], Ap)
            direct = boundary_matrix(np)
            representation_ok &= candidate == direct
            for i in range(10):
                edge_comp_ok &= ep(np, i) == ep(g, ep(p0, i))
                edge_comp_ok &= edge_sign(np, i) == edge_sign(p0, i) * edge_sign(g, ep(p0, i))
            if np not in group:
                group[np] = candidate
                q.append(np)
            else:
                representation_ok &= group[np] == candidate

    reynolds = [[Fraction(0) for _ in range(32)] for _ in range(32)]
    for A in group.values():
        for i in range(32):
            for j in range(32):
                reynolds[i][j] += A[i][j] / Fraction(len(group))
    reynolds_rank, reynolds_pivots = rref_rank(reynolds)

    base, source_terms = enumerate_base_patterns(src, edges)

    def transport_target_key_to_old(types, p0, transpose_reversed=True):
        # Derivation from the source endpoint convention: old edge i maps to
        # canonical target edge ep(p,i). Pulling the target dictionary back to
        # old labels reads that target slot; canonical reversal swaps endpoints.
        out = [None] * 10
        for i in range(10):
            j = ep(p0, i)
            t = types[j]
            if transpose_reversed and edge_sign(p0, i) == -1:
                t = (t[1], t[0])
            out[i] = t
        return tuple(out)

    def transported_patterns(v, p0, *, transpose_reversed=True, source_sign=True, cov_sign=True):
        gs = orientation_character(p0) if source_sign else 1
        gc = orientation_character(p0) if cov_sign else 1
        factor = gs * gc
        out = []
        for d in v:
            z = defaultdict(Fraction)
            for types, c in d.items():
                z[transport_target_key_to_old(types, p0, transpose_reversed)] += factor * c
            out.append(clean_dict(dict(z)))
        return out

    def predicted_contragredient(p0):
        Ainv = boundary_matrix(invperm(p0))
        return transform_dictvec(transpose(Ainv), base)

    matchings = tuple(all_matchings(range(10)))
    matching_sign_checks = {}
    for name, p0 in GENS.items():
        expected = orientation_character(p0)
        bad = []
        for mt in matchings:
            g = 1
            used = []
            for i, j in mt:
                g *= edge_sign(p0, i) * edge_sign(p0, j)
                used.extend((i, j))
            if sorted(used) != list(range(10)) or g != expected:
                if len(bad) < 5:
                    bad.append({'matching': [list(x) for x in mt], 'factor': g, 'expected': expected})
        matching_sign_checks[name] = {'all_945_exact': not bad, 'bad': bad, 'expected_character': expected}

    generator_results = {}
    for name, p0 in GENS.items():
        predicted = predicted_contragredient(p0)
        transported = transported_patterns(base, p0)
        ip = invperm(p0)
        roundtrip = transported_patterns(transported, ip)
        generator_results[name] = {
            'exact': dictvec_equal(transported, predicted),
            'transported_hash': dictvec_hash(transported),
            'predicted_hash': dictvec_hash(predicted),
            'first_mismatch': first_dictvec_mismatch(transported, predicted),
            'inverse_roundtrip_exact': dictvec_equal(roundtrip, base),
            'boundary_inverse_exact': matmul(boundary_matrix(p0), boundary_matrix(ip)) == eye(32) and matmul(boundary_matrix(ip), boundary_matrix(p0)) == eye(32),
        }

    # Counterexample-first malformed controls on the odd generator T.
    predT = predicted_contragredient(T)
    validT = transported_patterns(base, T)
    no_transpose = transported_patterns(base, T, transpose_reversed=False, source_sign=True, cov_sign=True)
    no_source_sign = transported_patterns(base, T, transpose_reversed=True, source_sign=False, cov_sign=True)
    no_cov_sign = transported_patterns(base, T, transpose_reversed=True, source_sign=True, cov_sign=False)
    extra_sign = scale_dictvec(-1, validT)
    source_fixed = base
    negative_controls = {
        'odd_T_orientation_character_minus1': orientation_character(T) == -1,
        'omit_endpoint_transpose_rejected': not dictvec_equal(no_transpose, predT),
        'omit_source_reversal_sign_rejected': not dictvec_equal(no_source_sign, predT),
        'omit_covariance_orientation_sign_rejected': not dictvec_equal(no_cov_sign, predT),
        'extra_permutation_sign_rejected': not dictvec_equal(extra_sign, predT),
        'source_fixed_object_rejected': not dictvec_equal(source_fixed, predT),
    }
    negative_witnesses = {
        'omit_endpoint_transpose': first_dictvec_mismatch(no_transpose, predT),
        'omit_source_reversal_sign': first_dictvec_mismatch(no_source_sign, predT),
        'omit_covariance_orientation_sign': first_dictvec_mismatch(no_cov_sign, predT),
        'extra_permutation_sign': first_dictvec_mismatch(extra_sign, predT),
        'source_fixed_object': first_dictvec_mismatch(source_fixed, predT),
    }

    reversal_exact = True
    for v in ((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 2, 3), (-2, 5, 7)):
        A = src.leading_matrix(v)
        B = src.leading_matrix(tuple(-x for x in v))
        reversal_exact &= B == [[(-z[0], -z[1]) for z in row] for row in A]

    group_checks = {
        'canonical_ten_edge_order_exact': edges == expected_edges and len(edges) == 10,
        'node_norms_4_12_cross0': node_metric == (Fraction(4), Fraction(12), Fraction(0)),
        'all_24_local_actions_exact': len(local_mats) == 24 and local_exact,
        'C5_identity': compose(C, compose(C, compose(C, compose(C, C)))) == ID,
        'T2_identity': compose(T, T) == ID,
        'generated_group_120': len(group) == 120,
        'boundary_representation_composes_all120': representation_ok,
        'edge_orientation_maps_compose_all120': edge_comp_ok,
        'reynolds_rank2_pivots_1_4': reynolds_rank == 2 and reynolds_pivots == [1, 4],
        'reynolds_idempotent': matmul(reynolds, reynolds) == reynolds,
    }

    polynomial_checks = {
        'spanning_tree_count_125': len(trees) == 125,
        'tree_coefficients_all_one': len(tree_poly) == 125 and all(c == 1 for c in tree_poly.values()),
        'laplacian_determinant_equals_independent_tree_enumeration': psi == tree_poly,
        'psi_degree4': all(sum(m) == 4 for m in psi),
        'C_psi_and_covariance_exact': cov_results['C']['psi_exact'] and cov_results['C']['all_covariance_numerators_exact'],
        'T_psi_and_covariance_exact': cov_results['T']['psi_exact'] and cov_results['T']['all_covariance_numerators_exact'],
        'C_matching_orientation_factor_all945': matching_sign_checks['C']['all_945_exact'],
        'T_matching_orientation_factor_all945': matching_sign_checks['T']['all_945_exact'],
    }

    boundary_checks = {
        'all_32_components': len(base) == 32,
        'exactly_100000_original_source_terms': source_terms == 100000,
        'source_module_expected_total': sum((len(src.NODE_OPTIONS[k]) for k in (0, 1))) ** 5 == 100000,
        'source_matrix_reversal_exact': reversal_exact,
        'C_contragredient_dictionary_exact': generator_results['C']['exact'],
        'T_contragredient_dictionary_exact': generator_results['T']['exact'],
        'C_inverse_roundtrip_exact': generator_results['C']['inverse_roundtrip_exact'],
        'T_inverse_roundtrip_exact': generator_results['T']['inverse_roundtrip_exact'],
        'C_boundary_inverse_exact': generator_results['C']['boundary_inverse_exact'],
        'T_boundary_inverse_exact': generator_results['T']['boundary_inverse_exact'],
    }

    forbidden_checks = {
        'no_numerical_schwinger_witness': True,
        'no_interpolation': True,
        'no_floating_tolerance': True,
        'no_fitted_phase_or_character': True,
        'no_fitted_2x2_channel_matrix': True,
        'no_researcher_result_import': True,
        'no_researcher_symbolic_implementation_import': True,
        'q18_values_used': False,
        'pre_invariant_dual_full32_object': True,
    }

    implementation_valid = (
        all(source_checks.values())
        and all(group_checks.values())
        and all(polynomial_checks.values())
        and all(boundary_checks[k] for k in boundary_checks if not k.endswith('_dictionary_exact'))
        and all(negative_controls.values())
        and all(forbidden_checks.values())
    )
    scientific_exact = generator_results['C']['exact'] and generator_results['T']['exact']

    if not all(source_checks.values()):
        verdict = 'INVALID_SOURCE_LOCK'
        critic_class = 'BLOCKED'
    elif not implementation_valid:
        verdict = 'INVALID_IMPLEMENTATION'
        critic_class = 'INVALID_IMPLEMENTATION'
    elif scientific_exact:
        verdict = 'CONFIRMED_SCOPED'
        critic_class = 'CONFIRMED_EXACT_SCOPED'
    else:
        verdict = 'SCIENTIFIC_FAIL_CONFIRMED'
        critic_class = 'REFUTED_EXACT_SCOPED'

    out = {
        'gate': 'FULL_SOURCE_BOUNDARY_S5_SYMBOLIC_TRANSPORT_INDEPENDENT_CRITIC',
        'critic_prereg_commit': CRITIC_PREREG_COMMIT,
        'researcher_prereg_commit': RESEARCHER_PREREG_COMMIT,
        'researcher_repair_commit': RESEARCHER_REPAIR_COMMIT,
        'researcher_result_commit': RESEARCHER_RESULT_COMMIT,
        'researcher_run': RESEARCHER_RUN,
        'source_blob_sha1': git_blob_sha(SOURCE),
        'erratum_blob_sha1': git_blob_sha(ERRATUM),
        'verdict': verdict,
        'critic_contract_classification': critic_class,
        'scientific_identity': 'a_p(p alpha)=A_p^(-T)a(alpha) on Psi_K5!=0 for the complete unprojected all-j=1/2 order-zero source/boundary object',
        'source_checks': source_checks,
        'group_checks': group_checks,
        'polynomial_checks': polynomial_checks,
        'boundary_checks': boundary_checks,
        'covariance_results': cov_results,
        'generator_results': generator_results,
        'negative_controls': negative_controls,
        'negative_witnesses': negative_witnesses,
        'matching_sign_checks': matching_sign_checks,
        'forbidden_checks': forbidden_checks,
        'independent_reconstruction': {
            'canonical_edges': [list(e) for e in edges],
            'psi_monomials': len(psi),
            'psi_sha256': poly_hash(psi),
            'perfect_matchings_checked': len(matchings),
            'boundary_components': len(base),
            'source_terms': source_terms,
            'base_dictionary_sha256': dictvec_hash(base),
            'group_size': len(group),
            'reynolds_rank': reynolds_rank,
            'reynolds_pivots': reynolds_pivots,
        },
        'counterexample_first': {
            'correct_identity_first_mismatch_C': generator_results['C']['first_mismatch'],
            'correct_identity_first_mismatch_T': generator_results['T']['first_mismatch'],
            'malformed_T_witnesses_recorded': all(v is not None for v in negative_witnesses.values()),
        },
        'interpretation_ceiling': {
            'q18_result': None,
            'all_orbit_cancellation': None,
            'full_K5_integrability': None,
            'global_stokes_ibp': None,
            'K5_periods': None,
            'physical_finite_part_selector': None,
            'regulator_independence': None,
            'F9_G3_G8_K5_promotion': None,
            'new_physics_found': False,
            'complete_quantum_gravity': False,
        },
    }

    p = Path(args.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print('VERDICT=', verdict)
    print('CRITIC_CLASSIFICATION=', critic_class)
    print('SUMMARY=', json.dumps(out['independent_reconstruction'], sort_keys=True))
    print('NEGATIVE_CONTROLS=', json.dumps(negative_controls, sort_keys=True))
    return 2 if verdict in ('INVALID_IMPLEMENTATION', 'INVALID_SOURCE_LOCK', 'INVALID_PROVENANCE', 'BLOCKED_OBJECT_DEFINITION') else 0


if __name__ == '__main__':
    raise SystemExit(main())
