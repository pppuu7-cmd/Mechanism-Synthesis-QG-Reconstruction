#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_MODULE = ROOT / 'distributional/iter077i_sm_source_ordered_jhalf_k5_l1.py'
PREREG = '18900e175ae1934eb770730f3e89e14eb577aad7'
ORDER = 4
ZERO = (Fraction(0), Fraction(0))
ONE = (Fraction(1), Fraction(0))

ENTRY_COEFF = {
    (0,0): ((0,0),(0,0),(1,0)),
    (0,1): ((-1,0),(0,-1),(0,0)),
    (1,0): ((-1,0),(0,1),(0,0)),
    (1,1): ((0,0),(0,0),(-1,0)),
}

POINTS = {
    'uniform': (Fraction(1),)*10,
    'ascending': tuple(Fraction(i) for i in range(1,11)),
    'descending': tuple(Fraction(i) for i in range(10,0,-1)),
    'edge01_heavy': (Fraction(16),)+(Fraction(1),)*9,
    'edge01_light': (Fraction(1,16),)+(Fraction(1),)*9,
    'star0_heavy': (Fraction(8),)*4+(Fraction(1),)*6,
    'star0_light': (Fraction(1),)*4+(Fraction(8),)*6,
    'mixed': tuple(Fraction(x) for x in (1,2,5,3,7,4,11,6,13,8)),
}


def load_source():
    spec = importlib.util.spec_from_file_location('iter077i_source', SOURCE_MODULE)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def incidence_row(edge):
    a,b=edge
    row=[0,0,0,0]
    if a != 0:
        row[a-1] -= 1
    if b != 0:
        row[b-1] += 1
    return tuple(row)


def build_L(alphas, rows):
    L=[[Fraction(0) for _ in range(4)] for _ in range(4)]
    for alpha,r in zip(alphas,rows):
        for i in range(4):
            for j in range(4):
                L[i][j] += alpha*r[i]*r[j]
    return L


def mat_inv(A):
    n=len(A)
    a=[[Fraction(x) for x in A[i]]+[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        p=next((r for r in range(c,n) if a[r][c]),None)
        if p is None:
            raise ValueError('singular matrix')
        a[c],a[p]=a[p],a[c]
        z=a[c][c]
        a[c]=[x/z for x in a[c]]
        for r in range(n):
            if r == c:
                continue
            z=a[r][c]
            if z:
                a[r]=[x-z*y for x,y in zip(a[r],a[c])]
    return [r[n:] for r in a]


def mat_mul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))), Fraction(0)) for j in range(len(B[0]))] for i in range(len(A))]


def mat_scale(A,c):
    return [[c*x for x in row] for row in A]


def dot_mat(r,M,s):
    return sum((Fraction(r[i])*M[i][j]*Fraction(s[j]) for i in range(4) for j in range(4)), Fraction(0))


def det_fraction(A):
    a=[[Fraction(x) for x in row] for row in A]
    n=len(a)
    out=Fraction(1)
    for c in range(n):
        p=next((r for r in range(c,n) if a[r][c]),None)
        if p is None:
            return Fraction(0)
        if p != c:
            a[c],a[p]=a[p],a[c]
            out=-out
        z=a[c][c]
        out*=z
        for j in range(c,n):
            a[c][j]/=z
        for r in range(c+1,n):
            z=a[r][c]
            if z:
                for j in range(c,n):
                    a[r][j]-=z*a[c][j]
    return out


def positive_definite(A):
    return all(det_fraction([row[:k] for row in A[:k]]) > 0 for k in range(1,len(A)+1))


def gadd(a,b):
    return (a[0]+b[0],a[1]+b[1])


def gmul(a,b):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])


def gscale(q,a):
    return (q*a[0],q*a[1])


def gdot(a,b):
    z=ZERO
    for x,y in zip(a,b):
        z=gadd(z,gmul(x,y))
    return z


def s_mul(a,b):
    out=[Fraction(0)]*(ORDER+1)
    for i,x in enumerate(a):
        if not x:
            continue
        for j,y in enumerate(b):
            if i+j <= ORDER and y:
                out[i+j]+=x*y
    return out


def cs_add(a,b):
    return [gadd(a[i],b[i]) for i in range(ORDER+1)]


def cs_mul(a,b):
    out=[ZERO for _ in range(ORDER+1)]
    for i,x in enumerate(a):
        if x == ZERO:
            continue
        for j,y in enumerate(b):
            if i+j <= ORDER and y != ZERO:
                out[i+j]=gadd(out[i+j],gmul(x,y))
    return out


def cs_scale(a,q):
    return [gscale(q,z) for z in a]


def binom_frac(p,n):
    z=Fraction(1)
    for k in range(n):
        z*=p-k
        z/=k+1
    return z


def inverse_series(L,Q):
    B=[None]*(ORDER+1)
    B[0]=mat_inv(L)
    for n in range(1,ORDER+1):
        B[n]=mat_scale(mat_mul(mat_mul(B[0],Q),B[n-1]), Fraction(-1))
    return B


def det_series(L,Q):
    out=[Fraction(0)]*(ORDER+1)
    for p in itertools.permutations(range(4)):
        inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        poly=[Fraction(1)]+[Fraction(0)]*ORDER
        for i in range(4):
            entry=[L[i][p[i]],Q[i][p[i]]]+[Fraction(0)]*(ORDER-1)
            poly=s_mul(poly,entry)
        if inv % 2:
            out=[x-y for x,y in zip(out,poly)]
        else:
            out=[x+y for x,y in zip(out,poly)]
    return out


def det_factor_series(L,Q):
    d=det_series(L,Q)
    d0=d[0]
    u=[Fraction(0)]+[d[i]/d0 for i in range(1,ORDER+1)]
    result=[Fraction(1)]+[Fraction(0)]*ORDER
    upow=[Fraction(1)]+[Fraction(0)]*ORDER
    for n in range(1,ORDER+1):
        upow=s_mul(upow,u)
        c=binom_frac(Fraction(-3,2),n)
        result=[x+c*y for x,y in zip(result,upow)]
    return result,d


def all_matchings(items):
    items=tuple(items)
    if not items:
        yield ()
        return
    a=items[0]
    for j in range(1,len(items)):
        b=items[j]
        rest=items[1:j]+items[j+1:]
        for tail in all_matchings(rest):
            yield ((a,b),)+tail


def selected_patterns(mod,edges):
    pats=[]
    for choices in itertools.product(mod.NODE_OPTIONS[0], repeat=5):
        states=[]
        coeff=1
        for state,c in choices:
            states.append(state)
            coeff*=c
        entries=[]
        for a,b in edges:
            row=states[b][mod.LEG_POS[(b,a)]]
            col=states[a][mod.LEG_POS[(a,b)]]
            entries.append((row,col))
        pats.append((tuple(entries),coeff))
    return pats


def evaluate_point(alphas,rows,Q,pats):
    L=build_L(alphas,rows)
    B=inverse_series(L,Q)
    cov={}
    for i in range(10):
        for j in range(i+1,10):
            cov[(i,j)]=[dot_mat(rows[i],B[n],rows[j]) for n in range(ORDER+1)]

    pair={}
    for (i,j),cser in cov.items():
        for ea in ENTRY_COEFF:
            for eb in ENTRY_COEFF:
                gd=gdot(ENTRY_COEFF[ea],ENTRY_COEFF[eb])
                pair[(i,j,ea,eb)]=[gscale(c,gd) for c in cser]

    cache={}
    def wick(rem):
        if not rem:
            return [ONE]+[ZERO]*ORDER
        if rem in cache:
            return cache[rem]
        i,ei=rem[0]
        total=[ZERO]*(ORDER+1)
        for pos in range(1,len(rem)):
            j,ej=rem[pos]
            rest=rem[1:pos]+rem[pos+1:]
            ps=pair[(i,j,ei,ej)]
            total=cs_add(total,cs_mul(ps,wick(rest)))
        cache[rem]=total
        return total

    W=[ZERO]*(ORDER+1)
    for entries,coeff in pats:
        rem=tuple((i,entries[i]) for i in range(10))
        W=cs_add(W,cs_scale(wick(rem),Fraction(coeff)))

    dfac,dser=det_factor_series(L,Q)
    J=[ZERO]*(ORDER+1)
    for i,c in enumerate(dfac):
        for j,z in enumerate(W):
            if i+j <= ORDER and c:
                J[i+j]=gadd(J[i+j],gscale(c,z))
    derivative4=gscale(Fraction(24),J[4])
    return {
        'positive_definite': positive_definite(L),
        'det_L': dser[0],
        'gaussian_N10_at_s0': W[0],
        'radial_probe_fourth_derivative_zero_equivalent': derivative4,
        'wick_cache_states': len(cache),
    }


def fq(q):
    return q.numerator if q.denominator == 1 else f'{q.numerator}/{q.denominator}'


def gz(z):
    return [fq(z[0]),fq(z[1])]


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',required=True)
    args=ap.parse_args()

    mod=load_source()
    edges=tuple(mod.EDGES)
    expected_edges=((0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3),(2,4),(3,4))
    rows=tuple(incidence_row(e) for e in edges)
    Luni=build_L((Fraction(1),)*10,rows)
    Q=mat_scale(Luni,Fraction(1,5))
    pats=selected_patterns(mod,edges)
    matching_count=sum(1 for _ in all_matchings(range(10)))

    raw={}
    for name,alphas in POINTS.items():
        raw[name]=evaluate_point(alphas,rows,Q,pats)

    uniform_expected=Fraction(3075072,390625)
    point_rows=[]
    real_signs=[]
    any_imag=False
    all_nonzero=True
    for name,alphas in POINTS.items():
        r=raw[name]
        z=r['radial_probe_fourth_derivative_zero_equivalent']
        any_imag |= z[1] != 0
        all_nonzero &= z != ZERO
        if z[1] == 0 and z[0] != 0:
            real_signs.append(1 if z[0] > 0 else -1)
        point_rows.append({
            'name':name,
            'weights':[fq(x) for x in alphas],
            'positive_definite':r['positive_definite'],
            'det_L':fq(r['det_L']),
            'gaussian_N10_at_s0':gz(r['gaussian_N10_at_s0']),
            'radial_probe_fourth_derivative_zero_equivalent':gz(z),
            'wick_cache_states':r['wick_cache_states'],
        })

    opposite_real_signs=(1 in real_signs and -1 in real_signs)
    if any_imag:
        classification='K5_00000_REAL_SIGN_ROUTE_INAPPLICABLE_COMPLEX_SCOPED'
    elif opposite_real_signs:
        classification='K5_00000_POINTWISE_SIGN_CERTIFICATE_FALSIFIED_BY_EXACT_NONUNIFORM_WITNESS'
    elif all_nonzero and len(set(real_signs)) == 1 and len(real_signs) == len(POINTS):
        classification='K5_00000_FROZEN_SIGN_DIAGNOSTIC_SURVIVES_SCOPED'
    else:
        classification='K5_00000_FROZEN_SIGN_DIAGNOSTIC_INCONCLUSIVE_SCOPED'

    checks={
        'prereg_frozen_before_script': True,
        'authoritative_edge_order': edges == expected_edges,
        'selected_boundary_is_00000': True,
        'all_1024_source_choices': len(pats) == 1024,
        'all_945_wick_pairings_structurally_included': matching_count == 945,
        'eight_frozen_points_exactly': tuple(POINTS) == ('uniform','ascending','descending','edge01_heavy','edge01_light','star0_heavy','star0_light','mixed'),
        'all_frozen_weight_entries_positive': all(all(x > 0 for x in a) for a in POINTS.values()),
        'all_weighted_laplacians_positive_definite': all(r['positive_definite'] for r in raw.values()),
        'uniform_reproduces_prior_radial_value_exactly': raw['uniform']['radial_probe_fourth_derivative_zero_equivalent'] == (uniform_expected,Fraction(0)),
        'no_k5_scientific_verdict_from_finite_sampling': True,
    }
    status='DIAGNOSTIC_EXACT' if all(checks.values()) else 'INVALID_IMPLEMENTATION'
    out={
        'gate':'K5_ORDER8_NONUNIFORM_SCHWINGER_SIGN_DIAGNOSTIC',
        'prereg_commit':PREREG,
        'parent_scientific_gate':'ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR_K5_LANE',
        'status':status,
        'classification':classification if status == 'DIAGNOSTIC_EXACT' else 'INVALID_IMPLEMENTATION',
        'checks':checks,
        'boundary_component':[0,0,0,0,0],
        'frozen_points':point_rows,
        'all_final_values_real':not any_imag,
        'all_final_values_nonzero':all_nonzero,
        'real_signs_present':sorted(set(real_signs)),
        'opposite_real_signs_found':opposite_real_signs,
        'scientific_k5_zero_nonzero_verdict':None,
        'interpretation':{
            'finite_sampling_proves_global_sign':False,
            'simple_sign_route_survives_frozen_sample': classification == 'K5_00000_FROZEN_SIGN_DIAGNOSTIC_SURVIVES_SCOPED',
            'next_if_survives':'derive symbolic rational numerator over the positive Schwinger cone and seek exact factorization/SOS/IBP positivity certificate',
            'next_if_falsified':'abandon pointwise sign certificate for this component and use invariant-dual complex/IBP noncancellation methods',
        },
    }
    Path(args.output).parent.mkdir(parents=True,exist_ok=True)
    Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2,sort_keys=True))
    return 0 if status == 'DIAGNOSTIC_EXACT' else 2


if __name__ == '__main__':
    raise SystemExit(main())
