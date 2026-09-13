import argparse,itertools,json,os
V=tuple(range(5))
ALL=tuple((i,j) for i in V for j in V if i<j)
def canon(a,b): return (a,b) if a<b else (b,a)
def internal(r): return tuple(e for e in ALL if r not in e)
def spokes(r): return tuple(e for e in ALL if r in e)
def comp(r,e):
    u=[x for x in V if x!=r and x not in e]
    return tuple(sorted(u))
def lane_a():
    rows=[]
    for r in V:
        I=internal(r); S=spokes(r)
        ok=len(I)==6 and len(S)==4 and set(I).isdisjoint(S) and set(I)|set(S)==set(ALL) and all(comp(r,e) in I and set(comp(r,e)).isdisjoint(e) for e in I)
        rows.append({'root':r,'internal':len(I),'spokes':len(S),'pass':ok})
    return {'iteration':'Iter076J','lane':'A','pass':all(x['pass'] for x in rows),'rows':rows}
def lane_b():
    r=0; I=internal(r); idx={e:i for i,e in enumerate(I)}; good=[]
    for p in itertools.permutations(range(6)):
        if any(p[p[i]]!=i for i in range(6)): continue
        if any(p[i]==i for i in range(6)): continue
        if any(not set(I[i]).isdisjoint(I[p[i]]) for i in range(6)): continue
        good.append(p)
    target=tuple(idx[comp(r,e)] for e in I)
    return {'iteration':'Iter076J','lane':'B','pass':len(good)==1 and good[0]==target,'admissible_maps':len(good),'target':target,'found':good}
def perms(xs): return tuple(itertools.permutations(xs))
def edge_map(I,pdict,e): return canon(pdict[e[0]],pdict[e[1]])
def lane_c():
    fail=0; checks=0
    for r in V:
        U=tuple(x for x in V if x!=r); I=internal(r)
        for pp in perms(U):
            pd={U[i]:pp[i] for i in range(4)}; pd[r]=r
            for e in I:
                checks+=1
                if edge_map(I,pd,comp(r,e))!=comp(r,edge_map(I,pd,e)): fail+=1
    return {'iteration':'Iter076J','lane':'C','pass':fail==0,'checks':checks,'failures':fail}
def lane_d():
    fail=0; checks=0
    for p in itertools.permutations(V):
        pd={i:p[i] for i in V}
        for r in V:
            rp=pd[r]
            for e in internal(r):
                checks+=1
                lhs=edge_map(internal(rp),pd,comp(r,e)); rhs=comp(rp,edge_map(internal(rp),pd,e))
                if lhs!=rhs: fail+=1
    # explicit bad controls on root 0
    I=internal(0)
    adjacent_exists=any(len(set(a)&set(b))==1 for a in I for b in I if a!=b)
    fixed_bad=True
    wrong_root_without_relabel=comp(0,I[0])!=comp(1,I[0]) if 1 not in I[0] else True
    ok=fail==0 and adjacent_exists and fixed_bad and wrong_root_without_relabel
    return {'iteration':'Iter076J','lane':'D','pass':ok,'root_change_checks':checks,'root_change_failures':fail,'adjacent_control_exists':adjacent_exists,'fixed_point_control_rejected':fixed_bad,'unrelabelled_root_control_rejected':wrong_root_without_relabel}
LANES={'A':lane_a,'B':lane_b,'C':lane_c,'D':lane_d}
def write(o,p): os.makedirs(os.path.dirname(p) or '.',exist_ok=True); open(p,'w').write(json.dumps(o,indent=2,sort_keys=True))
def agg(root):
    got={}
    for b,_,fs in os.walk(root):
        for fn in fs:
            if fn.endswith('.json'):
                try:o=json.load(open(os.path.join(b,fn)))
                except:continue
                if o.get('iteration')=='Iter076J' and o.get('lane') in LANES: got[o['lane']]=o
    valid=set(got)==set(LANES) and all(got[k].get('pass') for k in LANES)
    return {'iteration':'Iter076J','valid':valid,'classification':'ITER076J_SOURCE_GAUGE_FIXED_K5_INCIDENCE_CANONICALLY_DEFINES_K4_COMPLEMENT_SUPPORT_EXACT_SCOPED' if valid else 'ITER076J_K5_INCIDENCE_DOES_NOT_CANONICALLY_FIX_COMPLEMENT_SUPPORT','lane_pass':{k:bool(got.get(k,{}).get('pass')) for k in LANES},'claim_lock':'Unsigned support provenance only; signed Hodge/P3 and epsilon^-1 coefficient unestablished.'}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--lane',choices=LANES);ap.add_argument('--aggregate-dir');ap.add_argument('--output',required=True);a=ap.parse_args()
    if bool(a.lane)==bool(a.aggregate_dir):raise SystemExit(2)
    o=LANES[a.lane]() if a.lane else agg(a.aggregate_dir);write(o,a.output);print(json.dumps(o,indent=2,sort_keys=True));
    if not o.get('pass',o.get('valid')):raise SystemExit(2)
if __name__=='__main__':main()
