#!/usr/bin/env python3
import itertools, json, os
from collections import defaultdict

V=range(4)
E=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
EIDX={e:i for i,e in enumerate(E)}
PERMS=list(itertools.permutations(V))
MASK=int(os.environ['SIGMA_MASK'])
C=int(os.environ['GLOBAL_C'])
assert 0 <= MASK < 8 and C in (-1,1)

sigma=[1]+[1 if (MASK>>(i-1))&1 else -1 for i in (1,2,3)]
kappa=tuple(sigma[a]*sigma[b] for a,b in E)
base=tuple(C*k for k in kappa)

def eta(a,b):
    if a==b: raise ValueError('ordered wedge endpoints must differ')
    return 1 if a<b else -1

def direction(signs,eidx):
    a,b=E[eidx]
    return (a,b) if signs[eidx]>0 else (b,a)

def signs_from_arcs(arcs):
    aset=set(arcs); out=[]
    for a,b in E:
        if (a,b) in aset: out.append(1)
        elif (b,a) in aset: out.append(-1)
        else: raise AssertionError('missing orientation')
    return tuple(out)

def transform(signs,p,reverse=False):
    arcs=[]
    for i in range(6):
        u,v=direction(signs,i)
        u,v=p[u],p[v]
        if reverse: u,v=v,u
        arcs.append((u,v))
    return signs_from_arcs(arcs)

def direct_bridge_after_relabel(p,reverse=False):
    out=[None]*6
    for i,(a,b) in enumerate(E):
        u,v=p[a],p[b]
        key=(min(u,v),max(u,v)); j=EIDX[key]
        val=C*kappa[i]*eta(u,v)
        if reverse: val=-val
        out[j]=val
    assert all(x in (-1,1) for x in out)
    return tuple(out)

def adjacency(signs):
    d={v:[] for v in V}
    for i in range(6):
        u,w=direction(signs,i); d[u].append(w)
    return d

def strong(signs):
    d=adjacency(signs)
    for s in V:
        seen={s}; stack=[s]
        while stack:
            u=stack.pop()
            for w in d[u]:
                if w not in seen: seen.add(w); stack.append(w)
        if len(seen)!=4: return False
    return True

def simple_cycles(signs):
    arcs={direction(signs,i) for i in range(6)}
    cyc=set()
    for L in (3,4):
        for tup in itertools.permutations(V,L):
            if min(tup)!=tup[0]: continue
            if all((tup[i],tup[(i+1)%L]) in arcs for i in range(L)):
                cyc.add(tup)
    return sorted(cyc)

def positive_circulation(signs):
    cycles=simple_cycles(signs); mag=defaultdict(int)
    for cyc in cycles:
        for i in range(len(cyc)): mag[(cyc[i],cyc[(i+1)%len(cyc)])]+=1
    x=[]
    for i,(a,b) in enumerate(E):
        u,v=direction(signs,i); m=mag[(u,v)]
        x.append(m if (u,v)==(a,b) else -m)
    bal=[0]*4
    for xe,(a,b) in zip(x,E): bal[a]-=xe; bal[b]+=xe
    return all(s*xe>0 for s,xe in zip(signs,x)) and bal==[0,0,0,0]

def cut_obstruction(signs):
    arcs={direction(signs,i) for i in range(6)}
    for r in (1,2,3):
        for S0 in itertools.combinations(V,r):
            S=set(S0); T=set(V)-S
            if all((u,v) in arcs for u in S for v in T): return True
            if all((v,u) in arcs for u in S for v in T): return True
    return False

def orbit(signs): return {transform(signs,p,False) for p in PERMS}

# Independent atlas construction from all 64 canonical sign vectors.
ALL=[tuple(1 if (mask>>i)&1 else -1 for i in range(6)) for mask in range(64)]
unseen=set(ALL); atlas=[]
while unseen:
    rep=min(unseen); o=orbit(rep); atlas.append(o); unseen-=o
assert sorted(len(o) for o in atlas)==[8,8,24,24]

def orbit_label(signs):
    hits=[(len(o), strong(next(iter(o)))) for o in atlas if signs in o]
    assert len(hits)==1
    return hits[0]

reversal_local_ok=all(eta(b,a)==-eta(a,b) for a,b in E)
base_strong=strong(base)
convention_control=strong(base)==strong(tuple(-z for z in base))
rows=[]; valid=reversal_local_ok and convention_control
for p in PERMS:
    for rev in (False,True):
        transformed=transform(base,p,rev)
        direct=direct_bridge_after_relabel(p,rev)
        covariance_ok=(transformed==direct)
        target_strong=strong(transformed)
        status_invariant=(target_strong==base_strong)
        cert_ok=positive_circulation(transformed) if target_strong else cut_obstruction(transformed)
        olab=orbit_label(transformed)
        orbit_ok=(olab[1]==target_strong)
        lane_ok=all((covariance_ok,status_invariant,cert_ok,orbit_ok))
        valid &= lane_ok
        rows.append({'perm':p,'reverse':rev,'target':transformed,'strong':target_strong,'orbit_size':olab[0],'ok':lane_ok})

out={
 'iteration':'Iter062','sigma_mask':MASK,'global_c':C,'sigma':sigma,'kappa':kappa,'base_signs':base,
 'base_strong':base_strong,'reversal_local_ok':reversal_local_ok,'convention_control':convention_control,
 'state_count':len(rows),'all_valid':bool(valid),
 'classification':'ITER062_LANE_VALID' if valid else 'ITER062_LANE_INVALID',
 'scope':'ordered-wedge eta bookkeeping bridge only; no physical sector selection',
 'claim_locks':['global c remains unfixed','no contour/finiteness theorem','no K5/G3/F9/G8 promotion','no NEW_PHYSICS_FOUND']
}
name=f'iter062_lane_m{MASK}_c{"p" if C>0 else "m"}.json'
with open(name,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
print(json.dumps(out,indent=2,sort_keys=True))
if not valid: raise SystemExit(2)
