import argparse, itertools, json, os

VERTS=(0,1,2,3)
EDGES=tuple((i,j) for i in VERTS for j in VERTS if i<j)
PERMS=tuple(itertools.permutations(VERTS))

def inv_count(p):
    return sum(1 for i in range(4) for j in range(i+1,4) if p[i]>p[j])

def sgn(p):
    return -1 if inv_count(p)%2 else 1

def edge_orientation_sign(a,b):
    return 1 if a<b else -1

def nrev(p):
    return sum(1 for i,j in EDGES if p[i]>p[j])

def chi_source(p):
    return -1 if nrev(p)%2 else 1

def compose(p,q):
    # p after q
    return tuple(p[q[i]] for i in VERTS)

def canonical_pair(a,b):
    return (a,b) if a<b else (b,a)

def lane_a():
    rows=[]
    for p in PERMS:
        rows.append({'p':p,'nrev':nrev(p),'chi_source':chi_source(p),'sgn':sgn(p),'match':chi_source(p)==sgn(p)})
    odd=sum(1 for r in rows if r['sgn']==-1)
    even=len(rows)-odd
    ok=all(r['match'] for r in rows) and odd==12 and even==12
    return {'lane':'A','pass':ok,'permutations':len(rows),'odd':odd,'even':even,'all_character_matches':all(r['match'] for r in rows),'rows':rows}

def lane_b():
    char_fail=[]; edge_fail=[]
    for p in PERMS:
        for q in PERMS:
            r=compose(p,q)
            if chi_source(r)!=chi_source(p)*chi_source(q):
                char_fail.append((p,q))
            for i,j in EDGES:
                qa,qb=q[i],q[j]
                sq=edge_orientation_sign(qa,qb)
                u,v=canonical_pair(qa,qb)
                sp=edge_orientation_sign(p[u],p[v])
                sr=edge_orientation_sign(r[i],r[j])
                if sr!=sq*sp:
                    edge_fail.append((p,q,(i,j),sr,sq,sp))
    ok=(not char_fail and not edge_fail)
    return {'lane':'B','pass':ok,'pair_count':len(PERMS)**2,'edge_checks':len(PERMS)**2*len(EDGES),'character_failures':len(char_fail),'edge_composition_failures':len(edge_fail)}

def lane_c():
    matches=[chi_source(p)==sgn(p) for p in PERMS]
    return {'lane':'C','pass':all(matches),'matches':sum(matches),'total':len(matches),'interpretation':'character-level compatibility only; physical P3 not defined'}

def lane_d():
    odd=[p for p in PERMS if sgn(p)==-1]
    orientation_blind_mismatches=sum(1 for p in PERMS if 1!=sgn(p))
    # Explicitly drop canonical edge-reorientation signs: every edge contributes +1.
    dropped_sign_mismatches=orientation_blind_mismatches
    ok=(len(odd)==12 and orientation_blind_mismatches==12 and dropped_sign_mismatches==12)
    return {'lane':'D','pass':ok,'odd_permutations':len(odd),'orientation_blind_mismatches':orientation_blind_mismatches,'drop_edge_reorientation_mismatches':dropped_sign_mismatches,'fitted_sign_rule_used':False}

LANES={'A':lane_a,'B':lane_b,'C':lane_c,'D':lane_d}

def write(obj,path):
    os.makedirs(os.path.dirname(path) or '.',exist_ok=True)
    with open(path,'w',encoding='utf-8') as f: json.dump(obj,f,indent=2,sort_keys=True)

def aggregate(root):
    got={}
    for base,_,files in os.walk(root):
        for fn in files:
            if not fn.endswith('.json'): continue
            try:
                with open(os.path.join(base,fn),encoding='utf-8') as f: obj=json.load(f)
            except Exception:
                continue
            lane=obj.get('lane')
            if lane in LANES: got[lane]=obj
    valid=(set(got)==set(LANES) and all(bool(got[x].get('pass')) for x in LANES))
    cls=('ITER076G_EQUAL_SPIN_SOURCE_REVERSAL_CHARACTER_MATCHES_REQUIRED_S4_TWIST_EXACT_SCOPED' if valid else 'ITER076G_SOURCE_REVERSAL_CHARACTER_INCOMPATIBLE_WITH_REQUIRED_TWIST')
    return {'iteration':'Iter076G','classification':cls,'valid':valid,'lanes_found':sorted(got),'lane_pass':{k:bool(got.get(k,{}).get('pass')) for k in LANES},'claim_lock':'Character-level source compatibility only; no physical P3 pushforward, epsilon^-1 coefficient, K5, G3/F9/G8, new physics or complete-QG claim.'}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--lane',choices=sorted(LANES))
    ap.add_argument('--aggregate-dir')
    ap.add_argument('--output',required=True)
    a=ap.parse_args()
    if bool(a.lane)==bool(a.aggregate_dir): raise SystemExit('choose exactly one of --lane or --aggregate-dir')
    obj=LANES[a.lane]() if a.lane else aggregate(a.aggregate_dir)
    write(obj,a.output)
    print(json.dumps(obj,indent=2,sort_keys=True))
    if a.lane and not obj['pass']: raise SystemExit(2)
    if a.aggregate_dir and not obj['valid']: raise SystemExit(2)

if __name__=='__main__': main()
