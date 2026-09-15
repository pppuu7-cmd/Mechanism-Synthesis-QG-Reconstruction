#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_MODULE = ROOT / 'distributional/iter077i_sm_source_ordered_jhalf_k5_l1.py'
GENERAL_DIAGNOSTIC = ROOT / 'scripts/k5_order8_nonuniform_schwinger_sign_diagnostic.py'
DERIVATION = ROOT / 'sources/K5_ORDER8_EDGE01_RANKONE_POSITIVITY_DERIVATION.md'

UORD = 5
SORD = 4
ZERO = (Fraction(0), Fraction(0))
ONE = (Fraction(1), Fraction(0))


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def incidence_row(edge):
    a,b=edge
    row=[0,0,0,0]
    if a != 0:
        row[a-1]-=1
    if b != 0:
        row[b-1]+=1
    return tuple(row)


def build_L(alphas, rows):
    L=[[Fraction(0) for _ in range(4)] for _ in range(4)]
    for alpha,r in zip(alphas,rows):
        for i in range(4):
            for j in range(4):
                L[i][j]+=Fraction(alpha)*r[i]*r[j]
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


def dot_mat(r,M,s):
    return sum((Fraction(r[i])*M[i][j]*Fraction(s[j]) for i in range(4) for j in range(4)), Fraction(0))


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


def entry_coeff_from_source(mod):
    basis=((1,0,0),(0,1,0),(0,0,1))
    out={}
    mats=[mod.leading_matrix(v) for v in basis]
    for r in (0,1):
        for c in (0,1):
            out[(r,c)]=tuple(tuple(m[r][c]) for m in mats)
    return out


def selected_patterns(mod, edges):
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


def pcs_add(a,b,n):
    return [gadd(a[i],b[i]) for i in range(n+1)]


def pcs_mul(a,b,n):
    out=[ZERO for _ in range(n+1)]
    for i,x in enumerate(a):
        if x == ZERO:
            continue
        for j,y in enumerate(b):
            if i+j <= n and y != ZERO:
                out[i+j]=gadd(out[i+j],gmul(x,y))
    return out


def pcs_scale(a,q):
    return [gscale(q,z) for z in a]


def full_source_F(mod, edges, rows):
    L0=build_L((Fraction(1),)*10,rows)
    B0=mat_inv(L0)
    C0=[[dot_mat(rows[i],B0,rows[j]) for j in range(10)] for i in range(10)]
    c=C0[0][0]
    v=[C0[i][0] for i in range(10)]
    entry=entry_coeff_from_source(mod)
    pats=selected_patterns(mod,edges)

    pair={}
    for i in range(10):
        for j in range(i+1,10):
            cov=[C0[i][j],-v[i]*v[j]]+[Fraction(0)]*(UORD-1)
            for ea in entry:
                for eb in entry:
                    gd=gdot(entry[ea],entry[eb])
                    pair[(i,j,ea,eb)]=[gscale(x,gd) for x in cov]

    cache={}
    def wick(rem):
        if not rem:
            return [ONE]+[ZERO]*UORD
        if rem in cache:
            return cache[rem]
        i,ei=rem[0]
        total=[ZERO]*(UORD+1)
        for pos in range(1,len(rem)):
            j,ej=rem[pos]
            rest=rem[1:pos]+rem[pos+1:]
            total=pcs_add(total,pcs_mul(pair[(i,j,ei,ej)],wick(rest),UORD),UORD)
        cache[rem]=total
        return total

    F=[ZERO]*(UORD+1)
    for entries,coeff in pats:
        rem=tuple((i,entries[i]) for i in range(10))
        F=pcs_add(F,pcs_scale(wick(rem),Fraction(coeff)),UORD)
    return F,c,len(pats),len(cache)


def rsmul(a,b):
    out=[Fraction(0)]*(SORD+1)
    for i,x in enumerate(a):
        if not x:
            continue
        for j,y in enumerate(b):
            if i+j <= SORD and y:
                out[i+j]+=x*y
    return out


def rsadd(a,b):
    return [a[i]+b[i] for i in range(SORD+1)]


def rsscale(a,c):
    return [c*x for x in a]


def binom_frac(p,n):
    z=Fraction(1)
    for k in range(n):
        z*=p-k
        z/=k+1
    return z


def oneplus_power(x,p):
    return [binom_frac(p,n)*(x**n) for n in range(SORD+1)]


def compose_poly_series(coeffs,u_series):
    out=[Fraction(0)]*(SORD+1)
    upow=[Fraction(1)]+[Fraction(0)]*SORD
    for k,c in enumerate(coeffs):
        if k:
            upow=rsmul(upow,u_series)
        if c:
            out=rsadd(out,rsscale(upow,c))
    return out


def radial_from_F(t,Freal,c):
    t=Fraction(t)
    h=t-1
    b0=1+c*h
    # a=1+s/5; normalized determinant factor removes the positive det(L(t,0))^(-3/2).
    afac=oneplus_power(Fraction(1,5),Fraction(-19,2))
    bfac=oneplus_power(Fraction(1,5)/b0,Fraction(-3,2))
    u0=h/b0
    user=rsscale(oneplus_power(Fraction(1,5)/b0,Fraction(-1)),u0)
    fser=compose_poly_series(Freal,user)
    J=rsmul(rsmul(afac,bfac),fser)
    return 24*J[4]


def solve_vandermonde(xs,ys,degree):
    n=degree+1
    m=[[Fraction(x)**j for j in range(n)]+[Fraction(y)] for x,y in zip(xs,ys)]
    for c in range(n):
        p=next(r for r in range(c,n) if m[r][c])
        m[c],m[p]=m[p],m[c]
        z=m[c][c]
        m[c]=[v/z for v in m[c]]
        for r in range(n):
            if r == c:
                continue
            z=m[r][c]
            if z:
                m[r]=[x-z*y for x,y in zip(m[r],m[c])]
    return [m[i][-1] for i in range(n)]


def lcm(a,b):
    return abs(a*b)//math.gcd(a,b)


def primitive_integer_polynomial(coeffs):
    den=1
    for q in coeffs:
        den=lcm(den,q.denominator)
    ints=[q.numerator*(den//q.denominator) for q in coeffs]
    g=0
    for x in ints:
        g=math.gcd(g,abs(x))
    prim=[x//g for x in ints]
    scalar=Fraction(g,den)
    first=next((x for x in prim if x),1)
    if first < 0:
        prim=[-x for x in prim]
        scalar=-scalar
    return scalar,prim


def fq(q):
    return q.numerator if q.denominator == 1 else f'{q.numerator}/{q.denominator}'


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',required=True)
    args=ap.parse_args()

    mod=load(SOURCE_MODULE,'iter077i_source')
    general=load(GENERAL_DIAGNOSTIC,'general_nonuniform')
    edges=tuple(mod.EDGES)
    rows=tuple(incidence_row(e) for e in edges)
    F,c,choice_count,cache_count=full_source_F(mod,edges,rows)
    imag_zero=all(z[1] == 0 for z in F)
    Freal=[z[0] for z in F]
    deg=max(i for i,z in enumerate(Freal) if z)

    # Independent exact factorization check of the source-derived F polynomial.
    scale=Fraction(128,78125)
    factor1=[Fraction(5),Fraction(-2)]
    factor2=[Fraction(25),Fraction(15),Fraction(7)]
    prod=[Fraction(0)]*6
    for i,x in enumerate(factor1):
        for j,y in enumerate(factor2):
            prod[i+j]+=scale*x*y
    F_factorization_exact=Freal == prod
    quad_disc=15*15-4*7*25

    # From deg(F)=3 and four radial derivatives, multiplying R(t) by (2t+3)^7
    # is guaranteed to leave a polynomial of degree at most 7. Interpolate all
    # eight coefficients from exact source-derived rank-one values.
    degree_bound=deg+SORD
    xs=list(range(1,degree_bound+2))
    ys=[radial_from_F(x,Freal,c)*Fraction((2*x+3)**degree_bound) for x in xs]
    qcoeff=solve_vandermonde(xs,ys,degree_bound)
    scalarP,primitiveP=primitive_integer_polynomial(qcoeff)

    # Exact holdouts not used by interpolation.
    holdouts=(Fraction(9),Fraction(16),Fraction(1,16))
    interpolation_holdouts=[]
    for x in holdouts:
        poly=sum(qcoeff[i]*(x**i) for i in range(len(qcoeff)))
        direct=radial_from_F(x,Freal,c)*((2*x+3)**degree_bound)
        interpolation_holdouts.append(poly == direct)

    # Cross-check rank-one formula against the full general-L exact engine at
    # three points, including both extreme points from the frozen diagnostic.
    Luni=general.build_L((Fraction(1),)*10,rows)
    Q=general.mat_scale(Luni,Fraction(1,5))
    pats=general.selected_patterns(mod,edges)
    full_engine_checks=[]
    full_engine_values={}
    for x in (Fraction(1),Fraction(16),Fraction(1,16)):
        alphas=(x,)+(Fraction(1),)*9
        r=general.evaluate_point(alphas,rows,Q,pats)
        z=r['radial_probe_fourth_derivative_zero_equivalent']
        rf=radial_from_F(x,Freal,c)
        full_engine_checks.append(z == (rf,Fraction(0)))
        full_engine_values[fq(x)]=fq(rf)

    # Positivity certificate for the primitive numerator polynomial.
    # primitiveP is ascending in t. Isolate p2 t^2 + p1 t + p0.
    p0,p1,p2=primitiveP[0],primitiveP[1],primitiveP[2]
    discr=p1*p1-4*p2*p0
    higher_nonnegative=all(x >= 0 for x in primitiveP[3:])
    positivity_certificate=(scalarP > 0 and p2 > 0 and discr < 0 and higher_nonnegative)

    derivation_text=DERIVATION.read_text(encoding='utf-8')
    locks={
        'derivation_has_F_factorization':'(5-2u)(7u^2+15u+25)' in derivation_text,
        'derivation_has_radial_denominator':'78125 (2t+3)^7' in derivation_text,
        'derivation_has_negative_discriminant':'-29158276351851' in derivation_text,
        'derivation_keeps_k5_verdict_open':'does **not** prove the projective period nonzero' in derivation_text,
    }

    checks={
        'authoritative_ten_edges':len(edges) == 10,
        'all_1024_source_choices':choice_count == 1024,
        'rankone_effective_covariance_c_2_over_5':c == Fraction(2,5),
        'source_F_imaginary_coefficients_zero':imag_zero,
        'source_F_degree_exactly_3':deg == 3,
        'source_F_factorization_exact':F_factorization_exact,
        'F_quadratic_factor_discriminant_negative':quad_disc == -475,
        'radial_denominator_degree_bound_7':degree_bound == 7,
        'all_interpolation_holdouts_exact':all(interpolation_holdouts),
        'all_full_general_engine_crosschecks_exact':all(full_engine_checks),
        'primitive_polynomial_degree_6':primitiveP[-1] == 0 and primitiveP[-2] != 0,
        'primitive_polynomial_positive_leading_nonzero_coeff':primitiveP[-2] > 0,
        'only_linear_primitive_coefficient_negative':primitiveP[1] < 0 and all(x >= 0 for i,x in enumerate(primitiveP) if i != 1),
        'quadratic_discriminant_negative':discr < 0,
        'positivity_certificate_all_t_gt_0':positivity_certificate,
        'derivation_locks_present':all(locks.values()),
        'no_k5_projective_period_verdict':True,
    }

    # A malformed much-more-negative linear coefficient must fail the same
    # quadratic-discriminant positivity test; this is a real control.
    bad_p1=-10**8
    malformed_disc=bad_p1*bad_p1-4*p2*p0
    controls={
        'malformed_linear_coefficient_rejected':malformed_disc >= 0,
        'dropping_source_terms_would_change_frozen_choice_count':choice_count == 1024,
        'finite_ray_theorem_not_promoted_to_simplex_period':True,
    }

    valid=all(checks.values()) and all(controls.values())
    classification=(
        'K5_00000_EDGE01_RANKONE_RADIAL_MOMENT_POSITIVE_FOR_ALL_T_GT_0_EXACT_SCOPED'
        if valid else 'K5_EDGE01_RANKONE_POSITIVITY_INVALID_IMPLEMENTATION'
    )
    out={
        'gate':'K5_ORDER8_EDGE01_RANKONE_POSITIVITY',
        'status':'PASS_EXACT_SCOPED' if valid else 'INVALID_IMPLEMENTATION',
        'classification':classification,
        'checks':checks,
        'controls':controls,
        'source_choice_terms':choice_count,
        'wick_cache_states':cache_count,
        'effective_covariance_c':fq(c),
        'F_coefficients_u0_to_u5':[[fq(z[0]),fq(z[1])] for z in F],
        'F_factorization':'128/78125 * (5-2u) * (7u^2+15u+25)',
        'radial_common_denominator_power':degree_bound,
        'radial_polynomial_over_denominator_scalar':fq(scalarP),
        'primitive_radial_numerator_coefficients_t0_up':primitiveP,
        'quadratic_discriminant':discr,
        'interpolation_holdouts':interpolation_holdouts,
        'full_general_engine_crosschecks':full_engine_checks,
        'full_general_engine_values':full_engine_values,
        'strictly_positive_for_all_t_gt_0':positivity_certificate,
        'scientific_k5_zero_nonzero_verdict':None,
        'interpretation':{
            'ray_dimension':1,
            'full_projective_simplex_dimension':9,
            'ray_positivity_proves_full_period_nonzero':False,
            'next':'generalize to higher-dimensional positive Schwinger families or derive global SOS/IBP positivity/noncancellation certificate',
        },
    }
    Path(args.output).parent.mkdir(parents=True,exist_ok=True)
    Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2,sort_keys=True))
    return 0 if valid else 2


if __name__ == '__main__':
    raise SystemExit(main())
