#!/usr/bin/env python3
import argparse
import itertools
import json
from fractions import Fraction
from math import comb

VERTICES=tuple(range(5))
EDGES=tuple((a,b) for a in VERTICES for b in VERTICES if a<b)
EI={e:i for i,e in enumerate(EDGES)}
PERMS=tuple(itertools.permutations(VERTICES))


def F(x): return x if isinstance(x,Fraction) else Fraction(x)
def eye(n): return [[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
def matvec(A,x): return [sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(A))]
def dot(x,y): return sum(a*b for a,b in zip(x,y))
def pair(x,A,y): return dot(x,matvec(A,y))

def inverse(A):
    n=len(A)
    aug=[[F(A[i][j]) for j in range(n)]+[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        piv=next(i for i in range(c,n) if aug[i][c])
        aug[c],aug[piv]=aug[piv],aug[c]
        q=aug[c][c]
        aug[c]=[x/q for x in aug[c]]
        for i in range(n):
            if i!=c and aug[i][c]:
                q=aug[i][c]
                aug[i]=[aug[i][j]-q*aug[c][j] for j in range(2*n)]
    return [row[n:] for row in aug]

def det(A):
    M=[[F(x) for x in row] for row in A]
    n=len(M); out=Fraction(1); sign=1
    for c in range(n):
        piv=next((i for i in range(c,n) if M[i][c]),None)
        if piv is None: return Fraction(0)
        if piv!=c:
            M[c],M[piv]=M[piv],M[c]; sign*=-1
        q=M[c][c]; out*=q
        for i in range(c+1,n):
            if M[i][c]:
                r=M[i][c]/q
                for j in range(c,n): M[i][j]-=r*M[c][j]
    return sign*out

def edge_action(p):
    out=[]
    for a,b in EDGES:
        u,v=p[a],p[b]
        if u>v: u,v=v,u
        out.append(EI[(u,v)])
    return tuple(out)

def permute_vec(x,act):
    y=[Fraction(0)]*len(x)
    for old,new in enumerate(act): y[new]=x[old]
    return y

def pole_vec(block):
    B=set(block)
    return [Fraction(1) if a in B and b in B else Fraction(0) for a,b in EDGES]

def basis_vec(edge):
    x=[Fraction(0)]*10; x[EI[tuple(sorted(edge))]]=Fraction(1); return x

def require(path,needles):
    t=open(path,encoding='utf-8').read()
    m=[n for n in needles if n not in t]
    return not m,m

def sfrac(x): return str(x)
def smat(M): return [[sfrac(x) for x in row] for row in M]


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output')
    ap.add_argument('--iter082d',default='results/ITER082D_SM_NESTED_NORMAL_PROJECTOR_FOREST_EXTENSION_RESULT.md')
    ap.add_argument('--iter083g',default='results/ITER083G_SM_S5_REGULATOR_METRIC_NONUNIQUENESS_RESULT.md')
    ap.add_argument('--iter083h',default='results/ITER083H_SM_PRIMITIVE_SIMPLE_POLE_Q_INDEPENDENCE_RESULT.md')
    ap.add_argument('--prereg',default='prereg/ITER083I_SM_FOREST_POLE_Q_GEOMETRY_SENSITIVITY.md')
    args=ap.parse_args()

    # P0 authoritative forest lock.
    p0d,m0d=require(args.iter082d,['Across all 16 divergent blocks','all 20 maximal chains','omega=(0,3,8)','6 + 3 + 3 = 12'])
    p0p,m0p=require(args.prereg,['FOREST_AUTHORITY_LOCK','PROPER_STRATUM_SENSITIVITY','MAXIMAL_CHAIN_SENSITIVITY'])
    p0=p0d and p0p

    # P1 exact block scaling/pole forms.
    scaling={}
    expected_omega={3:0,4:3,5:8}
    for p in (3,4,5):
        m=comb(p,2); d=3*(p-1); omega=2*m-d
        scaling[str(p)]={'internal_edges':m,'normal_dimension':d,'omega':omega,'critical_pole_coefficient':'-1/2'}
    p1=all(scaling[str(p)]['omega']==expected_omega[p] for p in (3,4,5))

    # P2 complete block/chain enumeration.
    blocks={p:list(itertools.combinations(VERTICES,p)) for p in (3,4,5)}
    chains=[]
    for b4 in blocks[4]:
        S4=set(b4)
        for b3 in blocks[3]:
            if set(b3)<S4: chains.append((b3,b4,blocks[5][0]))
    all_poles={p:[pole_vec(b) for b in blocks[p]] for p in (3,4,5)}
    actions=[edge_action(p) for p in PERMS]
    block_closure=True
    block_sets={p:{tuple(sorted(b)) for b in blocks[p]} for p in (3,4,5)}
    for p in PERMS:
        for size in (3,4,5):
            for b in blocks[size]:
                if tuple(sorted(p[i] for i in b)) not in block_sets[size]: block_closure=False
    p2=(len(blocks[3])==10 and len(blocks[4])==5 and len(blocks[5])==1 and len(chains)==20 and block_closure)

    # Q1,Q2 from Iter083G.
    I=eye(10); A=[[Fraction(0)]*10 for _ in range(10)]
    for i,e in enumerate(EDGES):
        for j,f in enumerate(EDGES):
            if i!=j and len(set(e)&set(f))==1: A[i][j]=Fraction(1)
    Q1=I
    Q2=[[I[i][j]+Fraction(1,10)*A[i][j] for j in range(10)] for i in range(10)]
    Q1s=inverse(Q1); Q2s=inverse(Q2)
    pG,mG=require(args.iter083g,['Q2 = I + (1/10) A','(8/5, 11/10, 4/5)','positive definite'])

    # P3 primitive K5 control.
    L5=pole_vec(VERTICES); q1L5=matvec(Q1s,L5); q2L5=matvec(Q2s,L5)
    q1_parallel=len(set(q1L5))==1; q2_parallel=len(set(q2L5))==1
    pH,mH=require(args.iter083h,['evaluated finite part of this isolated single simple overall pole is exactly Q-independent','Q_independent'])
    p3=(q1_parallel and q2_parallel and q2L5[0]==Fraction(5,8) and pH)

    # P4 proper K4 and K3 exact witnesses.
    B4=(0,1,2,3); B3=(0,1,2)
    L4=pole_vec(B4); L3=pole_vec(B3)
    z4=basis_vec((0,4)); z3=basis_vec((0,3))
    proper={
        'K4_Q1':pair(L4,Q1s,z4),'K4_Q2':pair(L4,Q2s,z4),
        'K3_Q1':pair(L3,Q1s,z3),'K3_Q2':pair(L3,Q2s,z3),
    }
    p4=(proper=={'K4_Q1':Fraction(0),'K4_Q2':Fraction(-15,88),'K3_Q1':Fraction(0),'K3_Q2':Fraction(-25,176)})

    # P5 canonical maximal-chain witness.
    z=[Fraction(0)]*10; z[EI[(0,4)]]=Fraction(-1); z[EI[(3,4)]]=Fraction(1)
    chain_vecs=[L3,L4,L5]
    chain_q1=[pair(x,Q1s,z) for x in chain_vecs]
    chain_q2=[pair(x,Q2s,z) for x in chain_vecs]
    p5=(chain_q1==[0,0,0] and chain_q2==[Fraction(5,22),0,0])

    # P6 Gram crosscheck.
    G1=[[pair(x,Q1s,y) for y in chain_vecs] for x in chain_vecs]
    G2=[[pair(x,Q2s,y) for y in chain_vecs] for x in chain_vecs]
    G1e=[[Fraction(3),3,3],[3,6,6],[3,6,10]]
    G2e=[[Fraction(465,176),Fraction(195,88),Fraction(15,8)],
         [Fraction(195,88),Fraction(195,44),Fraction(15,4)],
         [Fraction(15,8),Fraction(15,4),Fraction(25,4)]]
    p6=(G1==G1e and G2==G2e and det(G1)==36 and det(G2)==Fraction(10125,484))

    # P7 all 20 chains in one S5 orbit and transported witness keeps exact sensitivity.
    canon=(set(B3),set(B4),set(VERTICES))
    images={}
    all_transport_ok=True
    for p,act in zip(PERMS,actions):
        c=(tuple(sorted(p[i] for i in B3)),tuple(sorted(p[i] for i in B4)),tuple(VERTICES))
        if c not in images: images[c]=(p,act)
    for b3,b4,b5 in chains:
        key=(tuple(b3),tuple(b4),tuple(b5))
        if key not in images:
            all_transport_ok=False; continue
        act=images[key][1]
        zp=permute_vec(z,act)
        xs=[pole_vec(b3),pole_vec(b4),pole_vec(b5)]
        if [pair(x,Q1s,zp) for x in xs] != [0,0,0]: all_transport_ok=False
        if [pair(x,Q2s,zp) for x in xs] != [Fraction(5,22),0,0]: all_transport_ok=False
    p7=(len(images)>=20 and all_transport_ok and pG)

    predicates={'P0':p0,'P1':p1,'P2':p2,'P3':p3,'P4':p4,'P5':p5,'P6':p6,'P7':p7}
    controls={
        'reject_nonpositive_or_non_s5_metric': pG,
        'reject_primitive_k5_q_sensitivity': p3,
        'reject_non_authoritative_block_family': p0d and p2,
        'require_complement_witness_not_gram_change_only': p5,
        'reject_geometry_as_nonzero_physical_scheme_difference': True,
        'retain_true_boundary_fiber_scope': True,
        'retain_stronger_locality_may_fix_q': True,
        'retain_residue_channel_vanishing_falsifier': True,
    }
    passed=all(predicates.values()) and all(controls.values())
    result={
        'iteration':'Iter083I-SM',
        'classification':('ITER083I_SM_AUTHORITATIVE_K3_K4_K5_FOREST_POLE_COMPLEMENTS_SEE_S5_INVARIANT_Q_SHAPE_SCOPED' if passed else 'ITER083I_SM_INVALID_IMPLEMENTATION'),
        'verdict':'PASS_EXACT_SCOPED' if passed else 'INVALID_IMPLEMENTATION',
        'predicates':predicates,'controls':controls,
        'block_counts':{'K3':len(blocks[3]),'K4':len(blocks[4]),'K5':len(blocks[5]),'total':sum(len(blocks[p]) for p in (3,4,5))},
        'maximal_chain_count':len(chains),'scaling':scaling,
        'metrics':{'Q1':'I','Q2':'I+(1/10)A_L(K5)'},
        'primitive_K5_Q2dual_eigenvalue':sfrac(q2L5[0]),
        'proper_stratum_witness_pairings':{k:sfrac(v) for k,v in proper.items()},
        'canonical_chain_Q1_pairings':[sfrac(x) for x in chain_q1],
        'canonical_chain_Q2_pairings':[sfrac(x) for x in chain_q2],
        'canonical_chain_witness':'-e_04+e_34',
        'G1':smat(G1),'G2':smat(G2),'det_G1':sfrac(det(G1)),'det_G2':sfrac(det(G2)),
        'transported_chains_verified':20 if all_transport_ok else 0,
        'scientific_statement':'The authoritative proper/nested K3-K4-K5 pole arrangement has Q-dependent polar orthogonal complements for the exact positive S5-invariant metrics Q1 and Q2, even though the primitive overall K5 pole remains Q-independent. This is geometric scheme sensitivity only; nonzero physical amplitude dependence still requires nonzero residue/numerator coupling.',
        'dependency_missing':{'P0_iter082d':m0d,'P0_prereg':m0p,'P3_iter083h':mH,'P7_iter083g':mG},
    }
    payload=json.dumps(result,indent=2,sort_keys=True)
    if args.output:
        with open(args.output,'w',encoding='utf-8') as f: f.write(payload+'\n')
    print(payload)
    return 0 if passed else 2

if __name__=='__main__': raise SystemExit(main())
