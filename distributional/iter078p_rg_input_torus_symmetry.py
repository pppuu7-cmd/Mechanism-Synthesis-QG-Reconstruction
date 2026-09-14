#!/usr/bin/env python3
"""Iter078P-RG: exact multiplicative input symmetry of Iter078H tensor map."""
from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import math
import os
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
H_PATH = ROOT / "distributional" / "iter078h_rg_full32_orderzero_1to5.py"
spec = importlib.util.spec_from_file_location("iter078h", H_PATH)
h = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(h)


def tensor_point(name):
    if name == "A": return [i + 1 for i in range(32)]
    if name == "B": return [((-1) ** i.bit_count()) * (i + 1) for i in range(32)]
    if name == "C": return [(i + 1) ** 2 for i in range(32)]
    if name == "L": return h.compact_tensor()
    raise ValueError(name)


def charge_rows():
    raw = 0
    unique = set()
    for external in h.TUPLES:
        for bits in itertools.product((0, 1), repeat=10):
            raw += 1
            kd = h.internal_dict(bits)
            counts = [0] * 32
            for a in range(5):
                counts[h.INDEX[h.local_tuple(a, external, kd)]] += 1
            unique.add(tuple(counts))
    return raw, sorted(unique)


def rref_full(rows, ncol=32):
    m = [[Fraction(x) for x in row] for row in rows]
    pivots = []
    r = 0
    for c in range(ncol):
        p = next((rr for rr in range(r, len(m)) if m[rr][c] != 0), None)
        if p is None:
            continue
        m[r], m[p] = m[p], m[r]
        q = m[r][c]
        m[r] = [x / q for x in m[r]]
        for rr in range(len(m)):
            if rr == r or m[rr][c] == 0:
                continue
            q = m[rr][c]
            m[rr] = [x - q * y for x, y in zip(m[rr], m[r])]
        pivots.append(c)
        r += 1
        if r == len(m):
            break
    return m, pivots


def primitive(v):
    den = 1
    for x in v: den = math.lcm(den, x.denominator)
    ints = [int(x * den) for x in v]
    g = 0
    for x in ints: g = math.gcd(g, abs(x))
    if g > 1: ints = [x // g for x in ints]
    first = next((x for x in ints if x != 0), 1)
    if first < 0: ints = [-x for x in ints]
    return ints


def nullspace_basis(rows, ncol=32):
    rr, pivots = rref_full(rows, ncol)
    free = [c for c in range(ncol) if c not in pivots]
    basis = []
    for f in free:
        x = [Fraction(0) for _ in range(ncol)]
        x[f] = Fraction(1)
        for i, pc in enumerate(pivots):
            x[pc] = -rr[i][f]
        basis.append(primitive(x))
    return len(pivots), pivots, basis


def verify_basis(rows, basis):
    return [all(sum(a*b for a,b in zip(row,q)) == 0 for row in rows) for q in basis]


def vector_rank(vectors):
    if not vectors: return 0
    _, piv = rref_full(vectors, len(vectors[0]))
    return len(piv)


def generator(q, C):
    return [a*b for a,b in zip(q,C)]


def jacobian_annihilates(J, v):
    return all(sum(a*b for a,b in zip(row,v)) == 0 for row in J)


def charge_data():
    raw, rows = charge_rows()
    rank, pivots, basis = nullspace_basis(rows, 32)
    verified = verify_basis(rows, basis)
    return raw, rows, rank, pivots, basis, verified


def solve_affine_charge(q):
    # q(k)=a0 + sum_{r=0}^4 a_{r+1} k_r
    A = []
    for t, y in zip(h.TUPLES, q):
        A.append([Fraction(1)] + [Fraction(x) for x in t] + [Fraction(y)])
    nvar = 6; r = 0; piv=[]
    for c in range(nvar):
        p = next((rr for rr in range(r,len(A)) if A[rr][c] != 0), None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        z=A[r][c]; A[r]=[x/z for x in A[r]]
        for rr in range(len(A)):
            if rr==r or A[rr][c]==0: continue
            z=A[rr][c]; A[rr]=[x-z*y for x,y in zip(A[rr],A[r])]
        piv.append(c); r+=1
    inconsistent = any(all(row[c]==0 for c in range(nvar)) and row[nvar]!=0 for row in A)
    if inconsistent or len(piv)<nvar: return None
    sol=[Fraction(0)]*nvar
    for i,c in enumerate(piv[:nvar]): sol[c]=A[i][nvar]
    if not all(Fraction(y)==sol[0]+sum(sol[i+1]*t[i] for i in range(5)) for t,y in zip(h.TUPLES,q)):
        return None
    return [str(x) for x in sol]


def lane_a():
    raw, rows, rank, pivots, basis, verified = charge_data()
    valid = raw == 32768 and all(verified) and rank + len(basis) == 32
    return {
        "iteration":"Iter078P-RG","lane":"A","valid":valid,
        "raw_configurations":raw,"unique_exponent_rows":len(rows),
        "charge_matrix_rank_Q":rank,"charge_nullity":len(basis),
        "pivot_columns":pivots,"primitive_charge_basis":basis,
        "basis_verified_all_rows":verified,
    }


def lane_b():
    _, rows, rank, pivots, basis, verified = charge_data()
    points={}
    valid=all(verified)
    for name in ("A","B","C","L"):
        C=tensor_point(name); J=h.jacobian_at(C,"eprl")
        jrank,_,jnull=h.rref_rank_null(J)
        gens=[generator(q,C) for q in basis]
        gen_rank=vector_rank([g for g in gens if any(g)]) if any(any(g) for g in gens) else 0
        annih=[jacobian_annihilates(J,g) for g in gens]
        spans_full = gen_rank == (32-jrank) and all(annih) if gens else False
        points[name]={
            "jacobian_rank_Q":jrank,"jacobian_nullity":32-jrank,
            "generated_vectors":gens,"generated_span_rank":gen_rank,
            "all_generators_annihilated":annih,
            "generated_span_equals_full_kernel_dimension":spans_full,
            "historical_single_null":jnull,
        }
        valid &= all(annih)
    return {"iteration":"Iter078P-RG","lane":"B","valid":bool(valid),"charge_nullity":len(basis),"points":points}


def lane_c():
    raw, rows, rank, pivots, basis, verified=charge_data()
    affine=[solve_affine_charge(q) for q in basis]
    # row-wise verification is the finite monomial-symmetry proof
    all_zero=all(verified)
    return {
        "iteration":"Iter078P-RG","lane":"C","valid":all_zero,
        "raw_monomials_verified":raw,"unique_exponent_rows":len(rows),
        "finite_symmetry_coefficientwise_verified":all_zero,
        "primitive_charge_basis":basis,
        "affine_5bit_ansatz_coefficients":affine,
        "affine_ansatz_matches":[x is not None for x in affine],
    }


def lane_d():
    _, rows, rank, pivots, basis, verified=charge_data()
    d=len(basis); controls={}; valid=all(verified)
    for name in ("A","B","C"):
        C=tensor_point(name); J=h.jacobian_at(C,"eprl")
        jrank,_,_=h.rref_rank_null(J)
        gens=[generator(q,C) for q in basis]
        gr=vector_rank(gens) if gens else 0
        controls[name]={"jacobian_rank":jrank,"jacobian_nullity":32-jrank,"generator_span_rank":gr,"bound_saturated":jrank==32-gr}
        valid &= jrank <= 32-gr
    return {
        "iteration":"Iter078P-RG","lane":"D","valid":bool(valid),
        "charge_nullity":d,"generic_rank_upper_bound_if_generators_independent":32-d,
        "controls":controls,
    }

LANES={"A":lane_a,"B":lane_b,"C":lane_c,"D":lane_d}


def aggregate(root):
    got={}
    for base,_,files in os.walk(root):
        for fn in files:
            if not fn.endswith('.json'): continue
            try: obj=json.loads(Path(base,fn).read_text(encoding='utf-8'))
            except Exception: continue
            if obj.get('iteration')=='Iter078P-RG' and obj.get('lane') in LANES: got[obj['lane']]=obj
    complete=set(got)==set(LANES); valid=complete and all(bool(got[k].get('valid')) for k in LANES)
    if not valid: return {"iteration":"Iter078P-RG","execution_valid":False,"verdict":"INVALID_IMPLEMENTATION","lanes_found":sorted(got)}
    d=got['A']['charge_nullity']
    if d>0 and got['C']['finite_symmetry_coefficientwise_verified']:
        verdict='PASS'; classification='ITER078P_RG_FIXED_JHALF_1TO5_CONTROL_HAS_EXACT_INPUT_TORUS_SYMMETRY_STRUCTURAL_JACOBIAN_KERNEL_SCOPED'
    else:
        verdict='FAIL'; classification='ITER078P_RG_NO_NONTRIVIAL_INPUT_MULTIPLICATIVE_CHARGE_SYMMETRY'
    return {
        "iteration":"Iter078P-RG","execution_valid":True,"verdict":verdict,"classification":classification,
        "charge_matrix_rank_Q":got['A']['charge_matrix_rank_Q'],"charge_nullity":d,
        "primitive_charge_basis":got['A']['primitive_charge_basis'],
        "affine_5bit_ansatz_coefficients":got['C']['affine_5bit_ansatz_coefficients'],
        "pointwise_controls":got['B']['points'],
        "generic_rank_upper_bound_if_generators_independent":got['D']['generic_rank_upper_bound_if_generators_independent'],
        "interpretation_ceiling":"Exact redundancy of the fixed labelled all-j=1/2 pure order-zero tensor-network control coordinates only; not automatically a physical causal-Toller gauge symmetry.",
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',choices=LANES); ap.add_argument('--aggregate-dir'); ap.add_argument('--output',required=True); args=ap.parse_args()
    if bool(args.lane)==bool(args.aggregate_dir): raise SystemExit('choose lane or aggregate')
    obj=LANES[args.lane]() if args.lane else aggregate(args.aggregate_dir)
    out=Path(args.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(obj,indent=2,sort_keys=True),encoding='utf-8'); print(json.dumps(obj,indent=2,sort_keys=True))
    if args.lane and not obj.get('valid',False): raise SystemExit(1)
    if args.aggregate_dir and not obj.get('execution_valid',False): raise SystemExit(1)

if __name__=='__main__': main()
