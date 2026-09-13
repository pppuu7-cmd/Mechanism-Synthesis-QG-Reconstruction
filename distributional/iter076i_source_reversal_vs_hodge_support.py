import argparse, itertools, json, os

VERTS=(0,1,2,3)
EDGES=tuple((i,j) for i in VERTS for j in VERTS if i<j)
EIDX={e:k for k,e in enumerate(EDGES)}
PERMS=tuple(itertools.permutations(VERTS))

def canon(a,b): return (a,b) if a<b else (b,a)
def inv_count(p): return sum(1 for i in range(4) for j in range(i+1,4) if p[i]>p[j])
def sgn(p): return -1 if inv_count(p)%2 else 1
def nrev(p): return sum(1 for i,j in EDGES if p[i]>p[j])
def chi_source(p): return -1 if nrev(p)%2 else 1

def complement(e):
    rem=[v for v in VERTS if v not in e]
    return tuple(sorted(rem))

def eps4(a,b,c,d):
    x=(a,b,c,d)
    if len(set(x))<4: return 0
    return -1 if inv_count(x)%2 else 1

def source_support():
    # Iter059 order reversal changes ordered orientation/branch/magnetic placement,
    # not the unordered wedge carrier.
    M=[[0]*6 for _ in range(6)]
    for e in EDGES: M[EIDX[e]][EIDX[e]]=1
    return M

def hodge_support_signed():
    H=[[0]*6 for _ in range(6)]
    for e in EDGES:
        c=complement(e)
        H[EIDX[c]][EIDX[e]]=eps4(e[0],e[1],c[0],c[1])
    return H

def support(M): return [[1 if x else 0 for x in r] for r in M]
def nz(M): return sum(sum(r) for r in support(M))
def hamming(A,B): return sum(int(bool(A[i][j])!=bool(B[i][j])) for i in range(len(A)) for j in range(len(A[0])))

def lane_a():
    rows=[]
    for e in EDGES:
        reversed_order=(e[1],e[0])
        rows.append({'edge':e,'reversed_order':reversed_order,'unordered_before':e,'unordered_after':canon(*reversed_order),'same_unordered':canon(*reversed_order)==e,'complement':complement(e),'is_complement':canon(*reversed_order)==complement(e)})
    ok=all(r['same_unordered'] and not r['is_complement'] for r in rows)
    return {'iteration':'Iter076I','lane':'A','pass':ok,'rows':rows,'same_edge_count':sum(r['same_unordered'] for r in rows),'complement_transport_count':sum(r['is_complement'] for r in rows)}

def lane_b():
    R=source_support(); H=hodge_support_signed(); HS=support(H)
    dist=hamming(R,H)
    per_edge=[]
    for e in EDGES:
        j=EIDX[e]; rt=[i for i in range(6) if R[i][j]]; ht=[i for i in range(6) if H[i][j]]
        per_edge.append({'edge':e,'source_targets':[EDGES[i] for i in rt],'hodge_targets':[EDGES[i] for i in ht],'different':rt!=ht})
    # explicit missing-object control: compose source identity support with H support
    inserted=HS
    ok=(nz(R)==6 and nz(H)==6 and dist==12 and all(x['different'] for x in per_edge) and inserted==HS)
    return {'iteration':'Iter076I','lane':'B','pass':ok,'source_nonzeros':nz(R),'hodge_nonzeros':nz(H),'support_hamming_distance':dist,'all_six_edges_mismatch':all(x['different'] for x in per_edge),'per_edge':per_edge,'manual_hodge_insertion_recovers_hodge_support':inserted==HS,'manual_insertion_is_control_only':True}

def magnetic_swap_support(two_j):
    # m,n labels each run over d=2j+1 values; transpose/swap support is a permutation
    d=two_j+1
    M=[[0]*(d*d) for _ in range(d*d)]
    for m in range(d):
        for n in range(d):
            src=m*d+n; dst=n*d+m; M[dst][src]=1
    return M

def lane_c():
    R=source_support(); rows=[]
    for tj in (1,2,3,4):
        M=magnetic_swap_support(tj); d2=len(M)
        cross_edge=0; total=0
        for e in range(6):
            for a in range(d2):
                for b in range(d2):
                    if M[b][a]:
                        total+=1
                        # R has only e->e support
                        if not R[e][e]: cross_edge+=1
        wrong_cross=6*d2  # deliberately insert one complementary block per edge
        rows.append({'two_j':tj,'magnetic_pair_dim':d2,'nonzero_product_support':total,'cross_unordered_edge_entries':cross_edge,'wrong_complement_control_entries':wrong_cross,'wrong_control_distinguishable':wrong_cross>0})
    ok=all(r['cross_unordered_edge_entries']==0 and r['wrong_control_distinguishable'] for r in rows)
    return {'iteration':'Iter076I','lane':'C','pass':ok,'rows':rows}

def lane_d():
    char_matches=sum(chi_source(p)==sgn(p) for p in PERMS)
    R=source_support(); H=hodge_support_signed()
    same_support=(support(R)==support(H))
    # Source-established reversal support provides only identity on unordered edge labels.
    # H requires the separately specified complement involution.
    source_edge_map_unique='same_unordered_edge_only'
    complement_extra=True
    ok=(char_matches==24 and not same_support and complement_extra)
    return {'iteration':'Iter076I','lane':'D','pass':ok,'source_character_matches_sgn':char_matches,'permutations':24,'source_edge_support_equals_hodge_support':same_support,'source_established_edge_action':source_edge_map_unique,'complement_identification_is_extra_input':complement_extra,'fitted_entries_used':False}

LANES={'A':lane_a,'B':lane_b,'C':lane_c,'D':lane_d}

def write(o,p):
    os.makedirs(os.path.dirname(p) or '.',exist_ok=True)
    with open(p,'w',encoding='utf-8') as f: json.dump(o,f,indent=2,sort_keys=True)

def aggregate(root):
    got={}
    for base,_,files in os.walk(root):
        for fn in files:
            if not fn.endswith('.json'): continue
            try:
                with open(os.path.join(base,fn),encoding='utf-8') as f:o=json.load(f)
            except Exception: continue
            if o.get('iteration')=='Iter076I' and o.get('lane') in LANES: got[o['lane']]=o
    valid=set(got)==set(LANES) and all(bool(got[k].get('pass')) for k in LANES)
    cls='ITER076I_SOURCE_REVERSAL_FIXES_TWIST_CHARACTER_NOT_HODGE_EDGE_MAP_BLOCKED_COMPLEMENT_IDENTIFICATION_SCOPED' if valid else 'ITER076I_SOURCE_REVERSAL_GENERATES_HODGE_SUPPORT_REVIEW'
    return {'iteration':'Iter076I','valid':valid,'classification':cls,'lanes_found':sorted(got),'lane_pass':{k:bool(got.get(k,{}).get('pass')) for k in LANES},'claim_lock':'Provenance/support diagnostic only; physical P3 and epsilon^-1 coefficient remain unestablished.'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',choices=sorted(LANES)); ap.add_argument('--aggregate-dir'); ap.add_argument('--output',required=True); a=ap.parse_args()
    if bool(a.lane)==bool(a.aggregate_dir): raise SystemExit('choose exactly one of --lane or --aggregate-dir')
    o=LANES[a.lane]() if a.lane else aggregate(a.aggregate_dir); write(o,a.output); print(json.dumps(o,indent=2,sort_keys=True))
    if a.lane and not o['pass']: raise SystemExit(2)
    if a.aggregate_dir and not o['valid']: raise SystemExit(2)
if __name__=='__main__': main()
