#!/usr/bin/env python3
"""Direct ten-wedge causal-vertex *integrand* smoke test.

This deliberately does NOT use B4 booster factorization.  For five explicit
SL(2,C) group elements (g1 gauge-fixed to identity), every relative element
    g_ab = g_b^{-1} g_a
is Cartan-decomposed as U1 exp(beta sigma_z/2) U2.  General Toller matrix
elements are reconstructed from validated reduced residue-series kernels,
    T(g) = D(U1) t(beta) D(U2).

The script then tests at one point of the four-group integration domain:
  1. T+ + T- = D edge by edge for general Lorentz elements;
  2. the unconstrained 2^10 wedge-sign sum equals the EPRL integrand;
  3. the causal sum uses only the 16 factorized classes kappa_ab=sigma_a sigma_b;
  4. global sigma reversal duplicates the same causal class.

It is a carrier/integrand validation, NOT a completed causal vertex integral.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np

from regulated import endpoint_precontraction_scan as ep
from regulated import general_toller_residue_series as gr

mp.mp.dps = 80
PAIRS = [(a,b) for a in range(5) for b in range(a+1,5)]


def mpc(z: complex):
    return mp.mpc(repr(float(np.real(z))), repr(float(np.imag(z))))


def cfmt(z, n=22):
    return [mp.nstr(mp.re(z),n), mp.nstr(mp.im(z),n)]


def sfmt(x, n=22):
    return mp.nstr(x,n)


def relerr(a,b):
    return abs(a-b)/max(abs(b),mp.mpf('1e-70'))


def su2_from_quaternion(q):
    q=np.asarray(q,dtype=float); q=q/np.linalg.norm(q)
    w,x,y,z=q
    return np.array([[w+1j*z, y+1j*x],[-y+1j*x,w-1j*z]],dtype=complex)


def random_su2(rng):
    return su2_from_quaternion(rng.normal(size=4))


def boost(beta):
    return np.diag([math.exp(beta/2),math.exp(-beta/2)]).astype(complex)


def cartan_kak(g):
    """Numerical KAK/SVD: g = U1 diag(e^(b/2),e^(-b/2)) U2, Ui in SU(2)."""
    U,s,Vh=np.linalg.svd(g)
    # SVD gives U,Vh in U(2). Redistribute the phase so both compact factors
    # lie in SU(2). det(g)=1 implies det(U)*det(Vh)=1 to roundoff.
    phi=np.angle(np.linalg.det(U))
    U1=U*np.exp(-0.5j*phi)
    U2=np.exp(0.5j*phi)*Vh
    # remove tiny determinant drift from the relative matrix via singular-value
    # geometric mean; this does not alter the represented SL(2,C) element above
    # double roundoff.
    geom=math.sqrt(float(s[0]*s[1]))
    s=s/geom
    beta=2.0*math.log(float(s[0]))
    H=np.diag([math.exp(beta/2),math.exp(-beta/2)]).astype(complex)
    rec=U1@H@U2
    return U1,beta,U2,float(np.linalg.norm(rec-g)),complex(np.linalg.det(U1)),complex(np.linalg.det(U2))


def sym_basis(two_j):
    n=two_j
    if n==0:
        return np.ones((1,1),dtype=complex)
    dim=2**n; cols=[]
    # basis order m=j,j-1,...,-j; 0=up, 1=down
    for n_up in range(n,-1,-1):
        inds=[]
        for bits in itertools.product((0,1),repeat=n):
            if bits.count(0)==n_up:
                idx=0
                for bit in bits: idx=2*idx+bit
                inds.append(idx)
        v=np.zeros(dim,dtype=complex)
        for idx in inds: v[idx]=1/math.sqrt(len(inds))
        cols.append(v)
    return np.column_stack(cols)


def spin_rep(U,two_j):
    if two_j==0:
        return np.ones((1,1),dtype=complex)
    K=np.array([[1]],dtype=complex)
    for _ in range(two_j): K=np.kron(K,U)
    S=sym_basis(two_j)
    return S.conj().T@K@S


def midx(two_j,two_m):
    if abs(two_m)>two_j or (two_j-two_m)%2:
        raise ValueError('invalid magnetic number')
    return (two_j-two_m)//2


def full_toller(branch,two_j,two_l,two_m,two_n,g,gamma):
    U1,beta,U2,kerr,d1,d2=cartan_kak(g)
    Dj=spin_rep(U1,two_j); Dl=spin_rep(U2,two_l)
    rho=mp.mpf(str(gamma))*mp.mpf(two_j)/2
    total=mp.mpc(0); max_terms=0
    for two_p in range(-min(two_j,two_l),min(two_j,two_l)+1,2):
        if branch>0:
            t,nt,cv,last=gr.toller_plus_series(two_j,two_l,two_p,two_j,rho,mp.mpf(str(beta)))
        else:
            t,nt,cv,last=gr.toller_minus_series(two_j,two_l,two_p,two_j,rho,mp.mpf(str(beta)))
        if not cv: raise RuntimeError('residue series did not converge')
        max_terms=max(max_terms,nt)
        total += mpc(Dj[midx(two_j,two_m),midx(two_j,two_p)])*t*mpc(Dl[midx(two_l,two_p),midx(two_l,two_n)])
    return total,max_terms,beta,kerr,d1,d2


def full_wigner_control(two_j,two_l,two_m,two_n,g,gamma):
    U1,beta,U2,kerr,d1,d2=cartan_kak(g)
    Dj=spin_rep(U1,two_j); Dl=spin_rep(U2,two_l)
    rho=mp.mpf(str(gamma))*mp.mpf(two_j)/2
    total=mp.mpc(0)
    for two_p in range(-min(two_j,two_l),min(two_j,two_l)+1,2):
        b=mp.mpf(str(beta))
        d=ep.toller_plus(two_j,two_l,two_p,two_j,rho,b)+ep.toller_minus(two_j,two_l,two_p,two_j,rho,b)
        total += mpc(Dj[midx(two_j,two_m),midx(two_j,two_p)])*d*mpc(Dl[midx(two_l,two_p),midx(two_l,two_n)])
    return total


def make_groups(seed,min_pair_beta=0.12):
    rng=np.random.default_rng(seed)
    for attempt in range(200):
        gs=[np.eye(2,dtype=complex)]
        for a in range(1,5):
            b=float(rng.uniform(0.35,1.35))
            gs.append(random_su2(rng)@boost(b)@random_su2(rng))
        betas=[]; maxerr=0.0
        for a,b in PAIRS:
            rel=np.linalg.inv(gs[b])@gs[a]
            _,bb,_,er,_,_=cartan_kak(rel)
            betas.append(bb); maxerr=max(maxerr,er)
        if min(betas)>=min_pair_beta:
            return gs,attempt,min(betas),max(betas),maxerr
    raise RuntimeError('could not generate separated group sample')


def ordered_m(a,b):
    # deterministic nontrivial magnetic pattern for j=1/2
    return 1 if ((a+2*b)%2==0) else -1


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--gamma',required=True)
    ap.add_argument('--seed',type=int,required=True)
    ap.add_argument('--output',required=True)
    args=ap.parse_args(); gamma=mp.mpf(args.gamma); ep.GAMMA=gamma

    gs,attempt,min_beta,max_beta,sample_kerr=make_groups(args.seed)
    edges=[]; max_add=mp.mpf('0'); max_terms=0; max_kerr=sample_kerr
    for a,b in PAIRS:
        rel=np.linalg.inv(gs[b])@gs[a]
        m_ab=ordered_m(a,b); m_ba=ordered_m(b,a)
        tp,np_,beta,kerr,d1,d2=full_toller(+1,1,1,m_ba,m_ab,rel,gamma)
        tm,nm,_,_,_,_=full_toller(-1,1,1,m_ba,m_ab,rel,gamma)
        dc=full_wigner_control(1,1,m_ba,m_ab,rel,gamma)
        err=relerr(tp+tm,dc)
        max_add=max(max_add,err); max_terms=max(max_terms,np_,nm); max_kerr=max(max_kerr,kerr)
        edges.append({'a':a+1,'b':b+1,'two_m_ba':m_ba,'two_m_ab':m_ab,
                      'beta':beta,'plus':tp,'minus':tm,'D':dc,'additive_error':err})

    eprl=mp.mpc(1)
    for e in edges: eprl*=e['D']

    unconstrained=mp.mpc(0)
    for mask in range(1<<10):
        z=mp.mpc(1)
        for i,e in enumerate(edges): z*=e['plus'] if (mask>>i)&1 else e['minus']
        unconstrained+=z
    unconstrained_error=relerr(unconstrained,eprl)

    causal_rows=[]; causal_sum=mp.mpc(0)
    # Fix sigma_1=+1: 2^4=16 inequivalent causal sign classes modulo global reversal.
    for tail in itertools.product((-1,1),repeat=4):
        sigma=(1,)+tail; z=mp.mpc(1); kappas=[]
        for e in edges:
            k=sigma[e['a']-1]*sigma[e['b']-1]
            kappas.append(k); z*=e['plus'] if k>0 else e['minus']
        causal_sum+=z
        causal_rows.append({'sigma':list(sigma),'kappa':kappas,'value':cfmt(z),
                            'magnitude':sfmt(abs(z)),'phase':sfmt(mp.arg(z))})

    full32=mp.mpc(0)
    for sigma in itertools.product((-1,1),repeat=5):
        z=mp.mpc(1)
        for e in edges:
            k=sigma[e['a']-1]*sigma[e['b']-1]
            z*=e['plus'] if k>0 else e['minus']
        full32+=z
    global_flip_error=relerr(full32,2*causal_sum)

    # The causal 16-class sum is generically not the EPRL/unconstrained sum.
    causal_eprl_rel=relerr(causal_sum,eprl)
    edge_json=[]
    for e in edges:
        edge_json.append({k:(cfmt(v) if k in ('plus','minus','D') else sfmt(v) if k=='additive_error' else v)
                          for k,v in e.items()})

    verdict=('DIRECT_CAUSAL_INTEGRAND_SMOKE_PASS'
             if max_kerr<1e-10 and max_add<mp.mpf('1e-35')
             and unconstrained_error<mp.mpf('1e-35') and global_flip_error<mp.mpf('1e-60')
             else 'DIRECT_CAUSAL_INTEGRAND_NEEDS_REVIEW')
    out={'gamma':args.gamma,'seed':args.seed,'generation_attempt':attempt,
         'min_pair_beta':min_beta,'max_pair_beta':max_beta,
         'max_kak_reconstruction_error':max_kerr,
         'max_edge_additive_relative_error':sfmt(max_add),
         'max_residue_terms':max_terms,
         'eprl_integrand':cfmt(eprl),'unconstrained_1024_sum':cfmt(unconstrained),
         'unconstrained_vs_eprl_relative_error':sfmt(unconstrained_error),
         'causal_16_sum':cfmt(causal_sum),
         'causal_vs_eprl_relative_difference':sfmt(causal_eprl_rel),
         'full_32_sigma_sum':cfmt(full32),
         'global_flip_duplication_error':sfmt(global_flip_error),
         'edge_rows':edge_json,'causal_classes':causal_rows,'verdict':verdict,
         'guardrail':('Pointwise direct-vertex integrand carrier only. No four-group Haar integration, '
                      'boundary intertwiner contraction, large-spin limit, or physical observable is claimed.')}
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k not in ('edge_rows','causal_classes')},indent=2))
    if verdict!='DIRECT_CAUSAL_INTEGRAND_SMOKE_PASS': raise SystemExit(4)

if __name__=='__main__': main()
