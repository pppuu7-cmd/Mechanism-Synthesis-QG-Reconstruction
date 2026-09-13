#!/usr/bin/env python3
import argparse, itertools, json
from fractions import Fraction

V=range(4)
E=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]

def perms(): return list(itertools.permutations(V))

def connected(edges):
    seen={0}; changed=True
    while changed:
        changed=False
        for a,b in edges:
            if a in seen and b not in seen: seen.add(b); changed=True
            if b in seen and a not in seen: seen.add(a); changed=True
    return len(seen)==4

def trees():
    out=[]
    for comb in itertools.combinations(E,3):
        if connected(comb): out.append(tuple(comb))
    assert len(out)==16
    return out

def incidence_vec(edge_signs):
    # column e has -1 at tail, +1 at head, tail/head set by sign on canonical edge
    B=[[0]*6 for _ in V]
    for j,(a,b) in enumerate(E):
        if edge_signs[j]==1: tail,head=a,b
        else: tail,head=b,a
        B[tail][j]=-1; B[head][j]=1
    return B

def matvec(B,x): return [sum(B[i][j]*x[j] for j in range(6)) for i in range(4)]

def tree_path(tree,u,v):
    adj={i:[] for i in V}
    for a,b in tree: adj[a].append(b); adj[b].append(a)
    stack=[(u,[u])]; seen=set()
    while stack:
        x,p=stack.pop()
        if x==v: return p
        if x in seen: continue
        seen.add(x)
        for y in adj[x]:
            if y not in seen: stack.append((y,p+[y]))
    raise RuntimeError('no path')

def fundamental_basis(tree):
    basis=[]
    chords=[e for e in E if e not in tree]
    for chord in chords:
        a,b=chord
        # orient chord canonically a->b, then path b->a closes cycle
        vec=[0]*6
        vec[E.index(chord)]=1
        path=tree_path(tree,b,a)
        for u,v in zip(path,path[1:]):
            ce=(min(u,v),max(u,v)); idx=E.index(ce)
            vec[idx]=1 if (u,v)==ce else -1
        basis.append(vec)
    return basis

def rank_q(cols):
    A=[[Fraction(cols[c][r]) for c in range(len(cols))] for r in range(6)]
    m,n=len(A),len(A[0]); rr=0
    for cc in range(n):
        piv=next((i for i in range(rr,m) if A[i][cc]),None)
        if piv is None: continue
        A[rr],A[piv]=A[piv],A[rr]
        q=A[rr][cc]; A[rr]=[x/q for x in A[rr]]
        for i in range(m):
            if i!=rr and A[i][cc]:
                q=A[i][cc]; A[i]=[A[i][j]-q*A[rr][j] for j in range(n)]
        rr+=1
    return rr

def solve_basis(basis,target):
    # solve 6x3 exact by Gaussian augmented system
    A=[[Fraction(basis[c][r]) for c in range(3)]+[Fraction(target[r])] for r in range(6)]
    rr=0; pivcols=[]
    for cc in range(3):
        piv=next((i for i in range(rr,6) if A[i][cc]),None)
        if piv is None: continue
        A[rr],A[piv]=A[piv],A[rr]
        q=A[rr][cc]; A[rr]=[x/q for x in A[rr]]
        for i in range(6):
            if i!=rr and A[i][cc]:
                q=A[i][cc]; A[i]=[A[i][j]-q*A[rr][j] for j in range(4)]
        pivcols.append(cc); rr+=1
    for row in A:
        if not any(row[c] for c in range(3)) and row[3]: raise RuntimeError('inconsistent')
    if rr!=3: raise RuntimeError('rank')
    x=[Fraction(0) for _ in range(3)]
    for i,c in enumerate(pivcols): x[c]=A[i][3]
    rec=[sum(Fraction(basis[c][r])*x[c] for c in range(3)) for r in range(6)]
    assert rec==[Fraction(t) for t in target]
    return x

def adjacency(signs):
    A={i:set() for i in V}
    for s,(a,b) in zip(signs,E):
        if s==1: A[a].add(b)
        else: A[b].add(a)
    return A

def strong(signs):
    A=adjacency(signs)
    for start in V:
        seen={start}; stack=[start]
        while stack:
            u=stack.pop()
            for v in A[u]:
                if v not in seen: seen.add(v); stack.append(v)
        if len(seen)!=4: return False
    return True

def directed_cycles(signs):
    A=adjacency(signs); cyc=set()
    for L in (3,4):
        for tup in itertools.permutations(V,L):
            if min(tup)!=tup[0]: continue
            if all(tup[(i+1)%L] in A[tup[i]] for i in range(L)):
                rev=(tup[0],)+tuple(reversed(tup[1:]))
                if rev in cyc: continue
                cyc.add(tup)
    return sorted(cyc)

def positive_circulation(signs):
    flow=[0]*6
    for cyc in directed_cycles(signs):
        for u,v in zip(cyc,cyc[1:]+cyc[:1]):
            e=(min(u,v),max(u,v)); idx=E.index(e)
            # signed relative to canonical orientation
            flow[idx]+= 1 if (u,v)==e else -1
    # convert canonical flow to oriented-sign positive coordinates criterion s_e*x_e > 0
    assert all(signs[i]*flow[i]>0 for i in range(6))
    B=incidence_vec([1]*6) # canonical incidence for flow conservation
    assert matvec(B,flow)==[0,0,0,0]
    return flow

def one_way_cut(signs):
    A=adjacency(signs)
    for r in (1,2,3):
        for S0 in itertools.combinations(V,r):
            S=set(S0); T=set(V)-S
            if all(v in A[u] for u in S for v in T): return sorted(S),sorted(T),'S_to_T'
            if all(u in A[v] for u in S for v in T): return sorted(S),sorted(T),'T_to_S'
    return None

def bridge_signs(mask,c,perm):
    sigma=[1]+[1 if (mask>>(i-1))&1 else -1 for i in (1,2,3)]
    # relabel sigma by permutation p: new vertex p[a] carries old sigma[a]
    sig2=[None]*4
    for a in V: sig2[perm[a]]=sigma[a]
    out=[]
    for a,b in E: out.append(c*sig2[a]*sig2[b]) # eta=+1 in canonical ordered edge
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--mask',type=int,required=True); ap.add_argument('--c',type=int,choices=[-1,1],required=True); args=ap.parse_args()
    if not 0<=args.mask<8: raise SystemExit(3)
    Ts=trees(); total=0; strong_n=0; cut_n=0
    for p in perms():
        s=bridge_signs(args.mask,args.c,p); st=strong(s)
        sr=[-x for x in s]
        if strong(sr)!=st: raise AssertionError('reversal feasibility changed')
        if st:
            strong_n+=1; flow=positive_circulation(s)
        else:
            cut=one_way_cut(s)
            if cut is None: raise AssertionError('missing cut'); cut_n+=1
        tree_status=[]
        for T in Ts:
            basis=fundamental_basis(T)
            if rank_q(basis)!=3: raise AssertionError('basis rank')
            B=incidence_vec([1]*6)
            if any(matvec(B,v)!=[0,0,0,0] for v in basis): raise AssertionError('basis not kernel')
            if st: solve_basis(basis,flow)
            tree_status.append(st)
            total+=1
        if len(set(tree_status))!=1: raise AssertionError('tree dependence')
    out={'iteration':'Iter063A','mask':args.mask,'global_c':args.c,'all_valid':True,'permutations':24,'trees':16,'cases':total,'strong_permutations':strong_n,'non_strong_permutations':cut_n,'tree_cycle_independent':True,'reversal_covariant':True}
    fn=f'iter063a_lane_m{args.mask}_c{args.c}.json'; open(fn,'w').write(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
