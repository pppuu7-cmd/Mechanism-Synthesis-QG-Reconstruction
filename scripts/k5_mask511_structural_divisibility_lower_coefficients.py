#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DAG_SOURCE = ROOT / 'scripts/k5_invariant_dual_deg27_canonical_dag.py'
ACTION_SOURCE = ROOT / 'scripts/k5_deg4_annihilator_actual_dual_action.py'
PARENT_RAW = ROOT / 'results/raw/k5_mask511_physical_numerator_action_exact_corner_witness_authoritative.json'
PRE = 'bb2fc2636de21d8eed06e3694a128be34e5fede1'
EXPECTED_DAG_BLOB = '5a224105472d022d2357b811e820d66ccfb17a6f'
EXPECTED_ACTION_BLOB = '2ed1b6397236c3f64c22b2a827bf1f0f8b5e0484'
EXPECTED_DAG_HASH = 'f8eaaa5c7923497a67f0354a2d59475f4b6d82022e032fc005c1d9d2add69992'
MASK = 511
MAX_T = 21
N_TARGET = 19
B_TARGET = 21
W1 = (2,3,5,7,11,13,17,19,23,29)
W2 = (31,37,41,43,47,53,59,61,67,71)
CLASS_PASS = 'K5_MASK511_LOWER_COEFFICIENTS_STRUCTURAL_DIVISIBILITY_EXACT_SCOPED'
CLASS_FAIL = 'K5_MASK511_RAY_CANCELLATION_NOT_ANGULAR_UNIFORM_EXACT_SCOPED'
CLASS_BLOCK = 'K5_MASK511_STRUCTURAL_DIVISIBILITY_BLOCKED_SCOPED'
CLASS_INVALID = 'K5_MASK511_STRUCTURAL_DIVISIBILITY_INVALID'
NVAR = 10
ZERO_MON = (0,) * NVAR


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()


def qstr(q):
    q = Fraction(q)
    return str(q.numerator) if q.denominator == 1 else f'{q.numerator}/{q.denominator}'


def tdeg(m):
    return sum(m[:9])


def totaldeg(m):
    return sum(m)


def pconst(c):
    c = Fraction(c)
    return {} if not c else {ZERO_MON: c}


def pvar(i):
    m = [0] * NVAR
    m[i] = 1
    return {tuple(m): Fraction(1)}


def padd(a, b):
    if not a:
        return dict(b)
    out = dict(a)
    for m, c in b.items():
        z = out.get(m, Fraction(0)) + c
        if z:
            out[m] = z
        elif m in out:
            del out[m]
    return out


def pscale(a, c):
    c = Fraction(c)
    if not c or not a:
        return {}
    return {m: c * z for m, z in a.items() if c * z}


def pmul(a, b, max_t=MAX_T):
    if not a or not b:
        return {}
    # Iterate the smaller dictionary outside for lower Python overhead.
    if len(a) > len(b):
        a, b = b, a
    out = defaultdict(Fraction)
    bitems = [(m, c, tdeg(m)) for m, c in b.items()]
    for ma, ca in a.items():
        ta = tdeg(ma)
        for mb, cb, tb in bitems:
            if ta + tb > max_t:
                continue
            m = tuple(ma[i] + mb[i] for i in range(NVAR))
            out[m] += ca * cb
    return {m: c for m, c in out.items() if c}


def ppow(a, n, max_t=MAX_T):
    out = pconst(1)
    base = a
    k = n
    while k:
        if k & 1:
            out = pmul(out, base, max_t)
        k >>= 1
        if k:
            base = pmul(base, base, max_t)
    return out


def pderiv(a, i):
    out = {}
    for m, c in a.items():
        if not m[i]:
            continue
        q = list(m)
        z = q[i]
        q[i] -= 1
        q = tuple(q)
        out[q] = out.get(q, Fraction(0)) + c * z
    return {m: c for m, c in out.items() if c}


def pslice(a, q):
    return {m: c for m, c in a.items() if tdeg(m) == q and c}


def pmin_t(a):
    return min((tdeg(m) for m in a), default=None)


def pmax_t(a):
    return max((tdeg(m) for m in a), default=None)


def peval(a, weights):
    z = Fraction(0)
    for m, c in a.items():
        v = c
        for i, e in enumerate(m):
            if e:
                v *= Fraction(weights[i]) ** e
        z += v
    return z


def pserial(a):
    return [[list(m), qstr(c)] for m, c in sorted(a.items())]


def phash(a):
    raw = json.dumps(pserial(a), separators=(',', ':'), sort_keys=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def pstats(a):
    if not a:
        return {'terms': 0, 'sha256': phash(a), 'min_t': None, 'max_t': None, 'leading_term': None}
    m = min(a)
    return {
        'terms': len(a), 'sha256': phash(a), 'min_t': pmin_t(a), 'max_t': pmax_t(a),
        'leading_term': [list(m), qstr(a[m])],
    }


def from_tuple_poly(p):
    out = defaultdict(Fraction)
    for mon, c in p.items():
        e = [0] * NVAR
        for i in mon:
            e[i] += 1
        e = tuple(e)
        if tdeg(e) <= MAX_T:
            out[e] += Fraction(c)
    return {m: c for m, c in out.items() if c}


def binom_frac(p, n):
    z = Fraction(1)
    for k in range(n):
        z *= (p - k) / Fraction(k + 1)
    return z


def mat_poly_num_right(A, Q, max_t=MAX_T):
    n, m, r = len(A), len(Q[0]), len(Q)
    out = [[{} for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            z = {}
            for k in range(r):
                if Q[k][j]:
                    z = padd(z, pscale(A[i][k], Q[k][j]))
            out[i][j] = {x:c for x,c in z.items() if tdeg(x) <= max_t}
    return out


def mat_poly_mul(A, B, max_t=MAX_T):
    n, m, r = len(A), len(B[0]), len(B)
    out = [[{} for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            z = {}
            for k in range(r):
                z = padd(z, pmul(A[i][k], B[k][j], max_t))
            out[i][j] = z
    return out


def dot_rows_poly(r, M, s):
    z = {}
    for i in range(4):
        if not r[i]:
            continue
        for j in range(4):
            if r[i] and s[j]:
                z = padd(z, pscale(M[i][j], Fraction(r[i] * s[j])))
    return z


def exact_prefix(path: Path, marker: str, name: str):
    text = path.read_text(encoding='utf-8')
    assert marker in text, (path, marker)
    ns = {'__name__': name, '__file__': str(path), '__package__': None}
    exec(compile(text.split(marker)[0], str(path), 'exec'), ns, ns)
    return ns


def build_det_coeffs(LP, Q):
    # D_r = [s^r] det(L+sQ), exact polynomial in alpha.
    D = [{} for _ in range(5)]
    for perm in itertools.permutations(range(4)):
        inv = sum(perm[i] > perm[j] for i in range(4) for j in range(i+1,4))
        ser = [pconst(1)] + [{} for _ in range(4)]
        for i, j in enumerate(perm):
            nxt = [{} for _ in range(5)]
            Lij = LP[i][j]
            qij = Fraction(Q[i][j])
            for k in range(5):
                if ser[k]:
                    nxt[k] = padd(nxt[k], pmul(ser[k], Lij, MAX_T))
                    if qij and k + 1 <= 4:
                        nxt[k+1] = padd(nxt[k+1], pscale(ser[k], qij))
            ser = nxt
        sgn = -1 if inv % 2 else 1
        for r in range(5):
            D[r] = padd(D[r], pscale(ser[r], sgn))
    return D


def build_cleared_det_factor(D, PSI):
    # F_j = Psi^j [s^j](det(L+sQ)/Psi)^(-3/2), polynomial degree 3j.
    memo = {}
    def tail_power(m, j, max_t):
        key = (m, j, max_t)
        if key in memo:
            return memo[key]
        if m == 0:
            z = pconst(1) if j == 0 else {}
        else:
            z = {}
            for r in range(1, min(4, j) + 1):
                z = padd(z, pmul(D[r], tail_power(m-1, j-r, max_t), max_t))
        memo[key] = z
        return z
    F = [pconst(1)]
    for j in range(1, 5):
        max_t = min(MAX_T, 2*j + 3)
        z = {}
        for m in range(1, j + 1):
            c = binom_frac(Fraction(-3,2), m)
            dprod = tail_power(m, j, max_t)
            term = pmul(ppow(PSI, j-m, max_t), dprod, max_t)
            z = padd(z, pscale(term, c))
        F.append(z)
    return F


def entry_metric(ENTRY, ea, eb):
    x, y = ENTRY[ea], ENTRY[eb]
    gr = Fraction(0); gi = Fraction(0)
    for xx, yy in zip(x, y):
        gr += xx[0]*yy[0] - xx[1]*yy[1]
        gi += xx[0]*yy[1] + xx[1]*yy[0]
    return (gr, gi)


def build_match_coeff(action_ns):
    ENTRY = action_ns['ENTRY']; WEIGHTS = action_ns['WEIGHTS']; PATTERNS = action_ns['PATTERNS']
    EM = {(a,b): entry_metric(ENTRY,a,b) for a in ENTRY for b in ENTRY}
    tcw = defaultdict(lambda:[Fraction(0),Fraction(0)])
    for idx, arr in PATTERNS:
        w0, w1 = WEIGHTS[idx]
        if not w0 and not w1:
            continue
        for types, coeff in arr:
            tcw[types][0] += coeff*w0
            tcw[types][1] += coeff*w1
    tcw = {t:(w[0],w[1]) for t,w in tcw.items() if w[0] or w[1]}
    def compatible(types):
        memo = {}
        def rec(rem):
            if not rem:
                return (((), (Fraction(1),Fraction(0))),)
            if rem in memo:
                return memo[rem]
            i = rem[0]; out = []
            for pos in range(1, len(rem)):
                j = rem[pos]; z = EM[(types[i],types[j])]
                if z == (0,0):
                    continue
                rest = rem[1:pos] + rem[pos+1:]
                for mt, c in rec(rest):
                    zz = (z[0]*c[0]-z[1]*c[1], z[0]*c[1]+z[1]*c[0])
                    out.append((((i,j),)+mt, zz))
            memo[rem] = tuple(out)
            return memo[rem]
        return rec(tuple(range(10)))
    mc = defaultdict(lambda:[[Fraction(0),Fraction(0)],[Fraction(0),Fraction(0)]])
    for types, w in tcw.items():
        for mt, z in compatible(types):
            for ch in (0,1):
                if not w[ch]:
                    continue
                mc[mt][ch][0] += w[ch]*z[0]
                mc[mt][ch][1] += w[ch]*z[1]
    out = {mt:((c[0][0],c[0][1]),(c[1][0],c[1][1])) for mt,c in mc.items()
           if c[0] != [0,0] or c[1] != [0,0]}
    return out, len(tcw)


def matching_series(mt, C):
    ser = [pconst(1)] + [{} for _ in range(4)]
    pairs_done = 0
    for ij in mt:
        pairs_done += 1
        nxt = [{} for _ in range(5)]
        for k in range(5):
            for n in range(k+1):
                if ser[k-n] and C[(ij[0],ij[1],n)]:
                    # For a partial product with p pairs and total source order k,
                    # only three t-grades above the exact minimum can feed N<=21.
                    maxt = min(MAX_T, 2*(pairs_done+k)+3)
                    nxt[k] = padd(nxt[k], pmul(ser[k-n], C[(ij[0],ij[1],n)], maxt))
        ser = nxt
    return ser


def build_source_series(MATCH_COEFF, C, F):
    # S[channel][series_order][real/imag]
    S = [[[{},{ }] for _ in range(5)] for _ in range(2)]
    control = None
    for idx, (mt, coeffs) in enumerate(sorted(MATCH_COEFF.items())):
        ser = matching_series(mt, C)
        for ch in (0,1):
            cr, ci = coeffs[ch]
            for k in range(5):
                if cr:
                    S[ch][k][0] = padd(S[ch][k][0], pscale(ser[k], cr))
                if ci:
                    S[ch][k][1] = padd(S[ch][k][1], pscale(ser[k], ci))
        # Deterministic malformed source-coefficient diagnostic: find the first retained
        # real channel coefficient whose +1 perturbation exposes the otherwise-cancelled q=18 slice.
        if control is None and coeffs[0] != (0,0):
            dz = {}
            for j in range(5):
                dz = padd(dz, pmul(F[j], ser[4-j], 18))
            dz = pscale(pslice(dz,18), 24)
            if dz:
                control = {
                    'matching_index': idx,
                    'matching': [list(x) for x in mt],
                    'perturbed_aggregated_source_coefficient_channel': 1,
                    'delta_N_q18': dz,
                }
    return S, control


def build_q_polys(action_ns):
    coeff = tuple(Fraction(x) for x in action_ns['ANN_COEFF'])
    QBAS = action_ns['QBAS']
    q = []
    for e in range(10):
        z = defaultdict(Fraction)
        for j, c in enumerate(coeff):
            if not c:
                continue
            for m in QBAS[e][j]:
                m = tuple(int(x) for x in m)
                if tdeg(m) <= MAX_T:
                    z[m] += c
        q.append({m:c for m,c in z.items() if c})
    return q


def action_on_poly(N, q):
    alpha = [pvar(i) for i in range(10)]
    v = [pmul(alpha[i], q[i], MAX_T) for i in range(10)]
    S = {}
    sumq = {}
    divv = {}
    for i in range(10):
        S = padd(S, v[i])
        sumq = padd(sumq, q[i])
        divv = padd(divv, q[i])
        divv = padd(divv, pmul(alpha[i], pderiv(q[i],i), MAX_T))
    s1 = {}
    for a in alpha:
        s1 = padd(s1, a)
    bracket = padd(divv, pscale(sumq, Fraction(1,2)))
    K = padd(pmul(s1, bracket, MAX_T), pscale(S, -3))
    vN = {}
    for i in range(10):
        vN = padd(vN, pmul(v[i], pderiv(N,i), MAX_T))
    B = padd(pmul(s1, vN, MAX_T), pmul(K, N, MAX_T))
    return B, {'v':v,'S':S,'sumq':sumq,'divv':divv,'K':K}


def slice_report(p, lo, hi):
    out = {}
    for q in range(lo, hi+1):
        z = pslice(p,q)
        out[str(q)] = pstats(z)
    return out


def exact_expected(parent, wname, ch, key):
    return Fraction(parent[wname][f'channel_{ch}'][key])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    ap.add_argument('--coefficients', required=True)
    args = ap.parse_args()

    checks = {
        'mask511_frozen': MASK == 511,
        'dag_blob_locked': git_blob_sha1(DAG_SOURCE) == EXPECTED_DAG_BLOB,
        'action_blob_locked': git_blob_sha1(ACTION_SOURCE) == EXPECTED_ACTION_BLOB,
    }

    print('loading canonical DAG prefix', flush=True)
    dns = exact_prefix(DAG_SOURCE, '# Evaluate frozen exact points by direct and canonical-DAG paths.', 'mask511_struct_dag')
    checks['canonical_dag_hash_locked'] = dns['dag_hash'] == EXPECTED_DAG_HASH
    checks['canonical_source_terms_100000'] = dns['SOURCE_TERMS'] == 100000
    checks['canonical_dual_rank2_pivots14'] = dns['rank'] == 2 and dns['piv'] == [1,4]
    checks['canonical_psi_125'] = len(dns['PSI']) == 125

    print('loading action prefix', flush=True)
    ans = exact_prefix(ACTION_SOURCE, 'results={};checks={}', 'mask511_struct_action')
    checks['action_source_terms_100000'] = ans['SOURCE_TERMS'] == 100000
    checks['annihilator_global_vpsi_zero'] = bool(ans['VPSI_ZERO'])
    checks['dual_projection_used'] = ans['PIV'] == [1,4]

    PSI = from_tuple_poly(dns['PSI'])
    ADJ = [[from_tuple_poly(dns['ADJ'][i][j]) for j in range(4)] for i in range(4)]
    LP = [[from_tuple_poly(dns['LP'][i][j]) for j in range(4)] for i in range(4)]
    Q = [[Fraction(x) for x in row] for row in dns['Q']]
    ROWS = tuple(tuple(int(x) for x in r) for r in dns['ROWS'])

    checks['psi_min_t3_mask511'] = pmin_t(PSI) == 3
    checks['adj_entries_tdegree_2_or3'] = all(all(tdeg(m) in (2,3) for m in ADJ[i][j]) for i in range(4) for j in range(4))

    print('building determinant factor polynomials', flush=True)
    D = build_det_coeffs(LP,Q)
    checks['det_D0_equals_psi'] = D[0] == PSI
    F = build_cleared_det_factor(D,PSI)
    checks['cleared_det_degrees'] = all(all(totaldeg(m) == 3*j for m in F[j]) for j in range(5))
    checks['cleared_det_min_t'] = all(pmin_t(F[j]) == 2*j for j in range(1,5))

    print('building inverse/covariance numerator series', flush=True)
    AQ = mat_poly_num_right(ADJ,Q)
    BN = [ADJ]
    for n in range(1,5):
        maxt = min(MAX_T, 2*(n+1)+3)
        BN.append([[pscale(z,-1) for z in row] for row in mat_poly_mul(AQ,BN[-1],maxt)])
    C = {}
    for i in range(10):
        for j in range(i+1,10):
            for n in range(5):
                C[(i,j,n)] = dot_rows_poly(ROWS[i],BN[n],ROWS[j])
    checks['covariance_degree_locks'] = all(all(totaldeg(m)==3*(n+1) for m in C[(i,j,n)])
                                                for i in range(10) for j in range(i+1,10) for n in range(5))

    print('aggregating full all32/100000 source coefficients', flush=True)
    MATCH_COEFF, source_pattern_count = build_match_coeff(ans)
    checks['source_pattern_aggregation_nonempty'] = source_pattern_count > 0
    checks['wick_matchings_nonempty'] = len(MATCH_COEFF) > 0
    print('matchings',len(MATCH_COEFF),'source patterns',source_pattern_count,flush=True)

    print('building exact symbolic Wick series', flush=True)
    SNUM, malformed_control = build_source_series(MATCH_COEFF,C,F)
    checks['malformed_control_discriminating'] = malformed_control is not None

    N = []
    imag_zero = True
    for ch in range(2):
        rr = {}; ii = {}
        for j in range(5):
            k = 4-j
            rr = padd(rr, pmul(F[j],SNUM[ch][k][0],MAX_T))
            ii = padd(ii, pmul(F[j],SNUM[ch][k][1],MAX_T))
        rr = pscale(rr,24); ii = pscale(ii,24)
        imag_zero &= not ii
        N.append(rr)
    checks['physical_numerator_imaginary_parts_cancel_exact'] = imag_zero
    checks['N_degree27'] = all(all(totaldeg(m)==27 for m in N[ch]) for ch in range(2))

    print('building exact annihilator action on symbolic numerator', flush=True)
    q = build_q_polys(ans)
    checks['q_degree3'] = all(all(totaldeg(m)==3 for m in q[e]) for e in range(10))
    B=[]; aux=[]
    for ch in range(2):
        b,a = action_on_poly(N[ch],q);B.append(b);aux.append(a)
    checks['B_degree31'] = all(all(totaldeg(m)==31 for m in B[ch]) for ch in range(2))

    parent = json.loads(PARENT_RAW.read_text(encoding='utf-8'))
    checks['parent_authority_run_locked'] = parent['source']['run_id'] == 35226938480
    checks['parent_orders_locked'] = all(parent[w][f'channel_{ch}']['rN']==19 and parent[w][f'channel_{ch}']['rB']==21
                                          for w in ('W1','W2') for ch in (1,2))

    lower_nonzero=[]
    channel_reports=[]
    coeff_payload={'gate':'K5_MASK511_STRUCTURAL_DIVISIBILITY_LOWER_COEFFICIENTS','prereg_commit':PRE,'channels':{}}
    ray_checks=[]
    for ch in range(2):
        nslices={qv:pslice(N[ch],qv) for qv in range(0,N_TARGET+1)}
        bslices={qv:pslice(B[ch],qv) for qv in range(0,B_TARGET+1)}
        for qv in range(N_TARGET):
            if nslices[qv]:lower_nonzero.append({'channel':ch+1,'family':'N','order':qv,'stats':pstats(nslices[qv])})
        for qv in range(B_TARGET):
            if bslices[qv]:lower_nonzero.append({'channel':ch+1,'family':'B','order':qv,'stats':pstats(bslices[qv])})
        nlead=nslices[N_TARGET];blead=bslices[B_TARGET]
        channel_reports.append({
            'channel':ch+1,
            'N_orders_0_19':slice_report(N[ch],0,N_TARGET),
            'B_orders_0_21':slice_report(B[ch],0,B_TARGET),
            'N_first_nonzero_target':pstats(nlead),
            'B_first_nonzero_target':pstats(blead),
        })
        coeff_payload['channels'][str(ch+1)]={
            'N_q19':pserial(nlead),
            'B_q21':pserial(blead),
        }
        for wname,W in (('W1',W1),('W2',W2)):
            en=peval(nlead,W); eb=peval(blead,W)
            okn=en==exact_expected(parent,wname,ch+1,'N_first_coefficient')
            okb=eb==exact_expected(parent,wname,ch+1,'B_first_coefficient')
            ray_checks.append({'channel':ch+1,'weight':wname,'N_q19':qstr(en),'B_q21':qstr(eb),'N_match':okn,'B_match':okb})

    checks['all_targeted_lower_N_coefficients_zero_exact'] = all(not pslice(N[ch],qv) for ch in range(2) for qv in range(N_TARGET))
    checks['all_targeted_lower_B_coefficients_zero_exact'] = all(not pslice(B[ch],qv) for ch in range(2) for qv in range(B_TARGET))
    checks['N_q19_nonzero_both'] = all(bool(pslice(N[ch],N_TARGET)) for ch in range(2))
    checks['B_q21_nonzero_both'] = all(bool(pslice(B[ch],B_TARGET)) for ch in range(2))
    checks['W1_W2_parent_first_coefficients_reproduced'] = all(r['N_match'] and r['B_match'] for r in ray_checks)

    # The malformed control is a +1 perturbation of one retained aggregated source coefficient;
    # this is equivalent to perturbing the retained source-contraction coefficient after exact
    # all-32 aggregation and before Wick summation. It must expose q=18.
    control_delta = malformed_control['delta_N_q18'] if malformed_control else {}
    controls={
        'perturbed_retained_source_coefficient_breaks_lower_zero': bool(control_delta),
        'perturbed_lower_q18_is_exact_nonzero': bool(control_delta) and pmin_t(control_delta)==18,
        'wrong_mask_not_promoted': MASK==511,
        'no_s5_transport_consumed': True,
        'no_numerical_identity_proof': True,
        'no_global_integrability_or_stokes_claim': True,
    }

    valid_provenance = all(checks[k] for k in checks if k not in (
        'all_targeted_lower_N_coefficients_zero_exact','all_targeted_lower_B_coefficients_zero_exact',
        'N_q19_nonzero_both','B_q21_nonzero_both')) and all(controls.values())
    theorem = checks['all_targeted_lower_N_coefficients_zero_exact'] and checks['all_targeted_lower_B_coefficients_zero_exact'] and checks['N_q19_nonzero_both'] and checks['B_q21_nonzero_both']
    if not valid_provenance:
        status=CLASS_INVALID;classification=CLASS_INVALID
    elif theorem:
        status='PASS_EXACT_SCOPED';classification=CLASS_PASS
    elif lower_nonzero:
        status='SCIENTIFIC_FAIL_EXACT_SCOPED';classification=CLASS_FAIL
    else:
        status='BLOCKED_OBJECT_DEFINITION';classification=CLASS_BLOCK

    coeff_payload['malformed_control']={
        'matching_index': malformed_control['matching_index'] if malformed_control else None,
        'matching': malformed_control['matching'] if malformed_control else None,
        'delta_N_q18': pserial(control_delta),
    }
    coeff_raw=json.dumps(coeff_payload,sort_keys=True,separators=(',',':')).encode()
    coeff_sha=hashlib.sha256(coeff_raw).hexdigest()
    cp=Path(args.coefficients);cp.parent.mkdir(parents=True,exist_ok=True)
    with gzip.open(cp,'wb',compresslevel=9) as f:f.write(coeff_raw)

    out={
        'gate':'K5_MASK511_STRUCTURAL_DIVISIBILITY_LOWER_COEFFICIENTS',
        'prereg_commit':PRE,'status':status,'classification':classification,
        'scope':{'mask':MASK,'channels':[1,2],'boundary_s5_transport_consumed':False,'max_exact_t_degree_materialized':MAX_T},
        'authority':{
            'canonical_dag_sha256':dns['dag_hash'],'dag_git_blob_sha1':git_blob_sha1(DAG_SOURCE),
            'action_git_blob_sha1':git_blob_sha1(ACTION_SOURCE),'parent_witness_run':parent['source']['run_id'],
            'parent_witness_full_json_sha256':parent['source']['full_json_sha256'],
        },
        'checks':checks,'controls':controls,
        'source_pattern_count':source_pattern_count,'perfect_matchings_retained':len(MATCH_COEFF),
        'channel_reports':channel_reports,'ray_reproduction':ray_checks,
        'lower_nonzero_witnesses':lower_nonzero,
        'malformed_control':None if malformed_control is None else {
            'matching_index':malformed_control['matching_index'],'matching':malformed_control['matching'],
            'delta_N_q18_stats':pstats(control_delta),
        },
        'coefficient_payload_sha256':coeff_sha,
        'coefficient_payload_gzip':cp.name,
        'scientific_corner_integrability_verdict':None,
        'global_stokes_ibp_verdict':None,'integrated_period_verdict':None,
        'finite_part_selector':None,'regulator_independence':None,
    }
    op=Path(args.output);op.parent.mkdir(parents=True,exist_ok=True)
    op.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('CLASSIFICATION='+classification)
    print('STATUS='+status)
    print('N_MIN_ORDERS=',[pmin_t(N[ch]) for ch in range(2)])
    print('B_MIN_ORDERS=',[pmin_t(B[ch]) for ch in range(2)])
    print('N_Q19_TERMS=',[len(pslice(N[ch],19)) for ch in range(2)])
    print('B_Q21_TERMS=',[len(pslice(B[ch],21)) for ch in range(2)])
    print('COEFF_SHA256='+coeff_sha)
    if status == CLASS_INVALID:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
