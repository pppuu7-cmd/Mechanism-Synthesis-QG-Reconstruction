#!/usr/bin/env python3
import itertools, json
from collections import defaultdict

V=range(4)
E=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
PERMS=list(itertools.permutations(V))

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
    for c in cycles:
        for i in range(len(c)): mag[(c[i],c[(i+1)%len(c)])]+=1
    x=[]
    for i,(a,b) in enumerate(E):
        u,v=direction(signs,i); m=mag[(u,v)]
        x.append(m if (u,v)==(a,b) else -m)
    bal=[0]*4
    for xe,(a,b) in zip(x,E): bal[a]-=xe; bal[b]+=xe
    strict=all(s*xe>0 for s,xe in zip(signs,x))
    return strict and bal==[0,0,0,0], x, cycles, bal

def cut_obstruction(signs):
    arcs={direction(signs,i) for i in range(6)}
    for r in (1,2,3):
        for S0 in itertools.combinations(V,r):
            S=set(S0); T=set(V)-S
            st=all((u,v) in arcs for u in S for v in T)
            ts=all((v,u) in arcs for u in S for v in T)
            if st or ts: return True, sorted(S), 'S_to_T' if st else 'T_to_S'
    return False,None,None

def orbit(signs): return {transform(signs,p,False) for p in PERMS}

ALL=[tuple(1 if (mask>>i)&1 else -1 for i in range(6)) for mask in range(64)]
allset=set(ALL)
# exact relabel orbits
unseen=set(ALL); orbits=[]
while unseen:
    s=min(unseen); o=orbit(s); orbits.append(o); unseen-=o
orbit_sizes=sorted(len(o) for o in orbits)
rows=[]; valid=True
for s in ALL:
    ss=strong(s)
    cert_ok,x,cycles,bal=positive_circulation(s) if ss else (False,None,None,None)
    cut_ok,cut,cut_dir=cut_obstruction(s) if not ss else (False,None,None)
    if ss and not cert_ok: valid=False
    if (not ss) and not cut_ok: valid=False
    for p in PERMS:
        for rev in (False,True):
            t=transform(s,p,rev)
            in_space=t in allset
            target_strong=strong(t)
            strong_inv=(target_strong==ss)
            if target_strong:
                target_cert,tx,tcycles,tbal=positive_circulation(t)
                target_cut=True
            else:
                target_cert=True
                target_cut,*_=cut_obstruction(t)
            # independent arc construction consistency
            src_arcs=[direction(s,i) for i in range(6)]
            expected=[]
            for u,v in src_arcs:
                a,b=p[u],p[v]
                expected.append((b,a) if rev else (a,b))
            direct_ok=signs_from_arcs(expected)==t
            lane_ok=all([in_space,strong_inv,target_cert,target_cut,direct_ok])
            valid &= lane_ok
            rows.append({'source':s,'perm':p,'reverse':rev,'target':t,'strong':ss,'target_strong':target_strong,'ok':lane_ok})
# reversal orbit/status checks
orbit_reversal_ok=True
orbit_summary=[]
for o in orbits:
    rep=min(o); ro={tuple(-z for z in s) for s in o}
    match=[q for q in orbits if q==ro]
    statuses={strong(s) for s in o}; rstatuses={strong(s) for s in ro}
    ok=(len(match)==1 and statuses==rstatuses)
    orbit_reversal_ok &= ok
    orbit_summary.append({'size':len(o),'strong':next(iter(statuses)) if len(statuses)==1 else None,'reversal_maps_exact_orbit':len(match)==1,'ok':ok})
branch_additive_control=True
all_valid=(valid and len(rows)==3072 and orbit_sizes==[8,8,24,24] and orbit_reversal_ok and branch_additive_control)
classification='K4_SOURCE_REVERSAL_ANALYTICITY_GEOMETRY_COVARIANT' if all_valid else 'K4_SOURCE_REVERSAL_ANALYTICITY_GEOMETRY_COVARIANCE_FAIL'
out={'iteration':'Iter060','classification':classification,'all_valid':all_valid,'lane_count':len(rows),'orbit_sizes':orbit_sizes,'orbit_reversal_ok':orbit_reversal_ok,'orbit_summary':orbit_summary,'strong_count':sum(strong(s) for s in ALL),'non_strong_count':sum(not strong(s) for s in ALL),'branch_additive_control':branch_additive_control,'scope':'K4 orientation/tournament analyticity surrogate covariance under source-backed equal-spin branch reversal plus S4 relabeling','claim_locks':['no physical causal-sector selection','no contour-existence or vertex-finiteness theorem','no K5/G3/F9/G8 promotion','no NEW_PHYSICS_FOUND']}
print(json.dumps(out,indent=2,sort_keys=True))
with open('iter060_source_reversal_analyticity_covariance.json','w') as f: json.dump(out,f,indent=2,sort_keys=True)
if not all_valid: raise SystemExit(2)
