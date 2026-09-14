#!/usr/bin/env python3
import itertools, json, sys
from fractions import Fraction
from pathlib import Path

V=tuple(range(5))
K3=[frozenset(x) for x in itertools.combinations(V,3)]
K4=[frozenset(x) for x in itertools.combinations(V,4)]
K5=[frozenset(V)]
BLOCKS=K3+K4+K5
PARAM={3:{'codim':6,'sd':6,'omega':0},4:{'codim':9,'sd':12,'omega':3},5:{'codim':12,'sd':20,'omega':8}}
SOURCE_FIREWALL='one-wedge spectral/spinor integration -> Toller function -> ten-wedge product -> full boundary contraction -> K5 extension'

def zmat(n=5): return [[Fraction(0) for _ in range(n)] for __ in range(n)]
def madd(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def msub(A,B): return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def mmul(A,B): return [[sum((A[i][k]*B[k][j] for k in range(len(B))),Fraction(0)) for j in range(len(B[0]))] for i in range(len(A))]
def mtrans(A): return [list(x) for x in zip(*A)]
def meq(A,B): return A==B
def mzero(A): return all(x==0 for row in A for x in row)
def mrank(A):
    M=[row[:] for row in A]; m=len(M); n=len(M[0]); r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if M[i][c]!=0),None)
        if piv is None: continue
        M[r],M[piv]=M[piv],M[r]
        q=M[r][c]; M[r]=[x/q for x in M[r]]
        for i in range(m):
            if i!=r and M[i][c]!=0:
                q=M[i][c]; M[i]=[M[i][j]-q*M[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r

def P(block):
    b=sorted(block); k=len(b); M=zmat(5)
    for i in b:
        for j in b:
            M[i][j]=(Fraction(1) if i==j else Fraction(0))-Fraction(1,k)
    return M

def perm_matrix(p):
    U=zmat(5)
    for i in V: U[p[i]][i]=1
    return U

def pblock(b,p): return frozenset(p[i] for i in b)
def bad_label_projector(block):
    b=sorted(block); v=[Fraction(0)]*5
    v[b[0]]=1; v[b[1]]=-1; den=sum(x*x for x in v)
    return [[v[i]*v[j]/den for j in V] for i in V]

def compatible(a,b): return a<=b or b<=a or a.isdisjoint(b)
def forests():
    out=[]
    for r in range(4):
        for comb in itertools.combinations(BLOCKS,r):
            if all(compatible(a,b) for a,b in itertools.combinations(comb,2)):
                out.append(tuple(sorted(comb,key=lambda x:(len(x),tuple(x)))))
    return out

def padd(X,Y):
    Z=dict(X)
    for k,v in Y.items():
        Z[k]=Z.get(k,Fraction(0))+v
        if Z[k]==0: del Z[k]
    return Z
def pscale(X,s): return {k:v*s for k,v in X.items() if v*s!=0}
def psub(X,Y): return padd(X,pscale(Y,Fraction(-1)))
def pmul(X,Y):
    Z={}
    for (a,b,c),u in X.items():
        for (d,e,f),v in Y.items():
            k=(a+d,b+e,c+f); Z[k]=Z.get(k,Fraction(0))+u*v
    for k in list(Z):
        if Z[k]==0: del Z[k]
    return Z

def generic_poly(max_total=10):
    P0={}
    for a in range(max_total+1):
        for b in range(max_total+1-a):
            for c in range(max_total+1-a-b):
                num=1+2*a+3*b+5*c+7*a*b+11*b*c+13*a*c
                den=1+a+b+c
                P0[(a,b,c)]=Fraction(num,den)
    return P0

def normal_degree(k,size):
    a,b,c=k
    return a if size==3 else (a+b if size==4 else a+b+c)
def eligible(k,size,omega=None):
    if omega is None: omega=PARAM[size]['omega']
    return normal_degree(k,size)<=omega
def tay(P0,size,omega=None): return {k:v for k,v in P0.items() if eligible(k,size,omega)}
def W(P0,size,weight,omega=None): return psub(P0,pmul(weight,tay(P0,size,omega)))
def unit_jet_valid(weight,size):
    omega=PARAM[size]['omega']
    if weight.get((0,0,0),Fraction(0))!=1: return False
    for k,v in weight.items():
        if k==(0,0,0) or v==0: continue
        if normal_degree(k,size)<=omega: return False
    return True

def make_weights(kind):
    if kind=='chi':
        return {3:{(0,0,0):Fraction(1),(1,0,0):Fraction(1,2)},4:{(0,0,0):Fraction(1),(0,4,0):Fraction(2,3)},5:{(0,0,0):Fraction(1),(0,0,9):Fraction(3,5)}}
    if kind=='eta':
        return {3:{(0,0,0):Fraction(1),(2,0,0):Fraction(-1,3)},4:{(0,0,0):Fraction(1),(4,0,0):Fraction(5,7)},5:{(0,0,0):Fraction(1),(4,5,0):Fraction(-2,5)}}
    raise ValueError(kind)
def chain_apply(P0,weights):
    q=W(P0,3,weights[3]); q=W(q,4,weights[4]); q=W(q,5,weights[5]); return q
def opT(P0,size,weights): return pmul(weights[size],tay(P0,size))
def expanded_apply(P0,weights):
    T3=lambda X: opT(X,3,weights); T4=lambda X: opT(X,4,weights); T5=lambda X: opT(X,5,weights)
    terms=[P0,pscale(T3(P0),-1),pscale(T4(P0),-1),T4(T3(P0)),pscale(T5(P0),-1),T5(T3(P0)),T5(T4(P0)),pscale(T5(T4(T3(P0))),-1)]
    out={}
    for t in terms: out=padd(out,t)
    return out
def basis_monomial(k): return {k:Fraction(1)}
def jet_visible(k):
    a,b,c=k
    return (a==0) or (a+b<=3) or (a+b+c<=8)
def common_kernel(k): return not jet_visible(k)
def source_object_valid(tag): return tag==SOURCE_FIREWALL
def symbolic_config_valid(cfg):
    def rec(x):
        if isinstance(x,dict): return all(rec(v) for v in x.values())
        if isinstance(x,(list,tuple)): return all(rec(v) for v in x)
        return isinstance(x,str) and x.startswith('symbolic:')
    return rec(cfg)
def selector_firewall_valid(obj): return not (obj.get('equation_kind')=='same_graph_reassociation' and obj.get('promote_to_selector') is True)
def radial_exponent(size,sub_order):
    p=PARAM[size]; return p['codim']-1-p['sd']+(sub_order+1)

def main():
    fs=forests(); chains=[f for f in fs if len(f)==3 and sorted(map(len,f))==[3,4,5]]
    reconstruction_ok=(len(BLOCKS)==16 and len(fs)==72 and len(chains)==20)
    block_rows=[]; block_ok=True; one=[Fraction(1)]*5
    for b in BLOCKS:
        Pb=P(b); row={'block':sorted(b),'size':len(b),'rank':mrank(Pb),'symmetric':meq(Pb,mtrans(Pb)),'idempotent':meq(mmul(Pb,Pb),Pb),'translation_annihilated':all(sum(Pb[i][j]*one[j] for j in V)==0 for i in V)}
        row['valid']=row['rank']==len(b)-1 and row['symmetric'] and row['idempotent'] and row['translation_annihilated']; block_ok &= row['valid']; block_rows.append(row)
    chain_geom=[]; chain_geom_ok=True
    for f in chains:
        b3=next(b for b in f if len(b)==3); b4=next(b for b in f if len(b)==4); b5=next(b for b in f if len(b)==5)
        A=P(b3); B=msub(P(b4),P(b3)); C=msub(P(b5),P(b4))
        pairzero=mzero(mmul(A,B)) and mzero(mmul(B,A)) and mzero(mmul(A,C)) and mzero(mmul(C,A)) and mzero(mmul(B,C)) and mzero(mmul(C,B))
        idem=meq(mmul(A,A),A) and meq(mmul(B,B),B) and meq(mmul(C,C),C); ranks=(mrank(A),mrank(B),mrank(C)); sumok=meq(madd(madd(A,B),C),P(b5)); ok=(ranks==(2,1,1) and pairzero and idem and sumok); chain_geom_ok &= ok
        chain_geom.append({'k3':sorted(b3),'k4':sorted(b4),'k5':sorted(b5),'ranks_one_component':ranks,'physical_dims':[3*x for x in ranks],'orthogonal':pairzero,'idempotent':idem,'sum_to_k5':sumok,'valid':ok})
    perms=list(itertools.permutations(V)); s5_block_ok=True; s5_chain_ok=True; s5_block_checks=0; s5_chain_checks=0
    for p in perms:
        U=perm_matrix(p); Ut=mtrans(U)
        for b in BLOCKS:
            s5_block_checks+=1
            if not meq(mmul(mmul(U,P(b)),Ut),P(pblock(b,p))): s5_block_ok=False; break
        if not s5_block_ok: break
        for f in chains:
            b3=next(b for b in f if len(b)==3); b4=next(b for b in f if len(b)==4); b5=next(b for b in f if len(b)==5)
            inc=[P(b3),msub(P(b4),P(b3)),msub(P(b5),P(b4))]
            pb3,pb4,pb5=pblock(b3,p),pblock(b4,p),pblock(b5,p); pinc=[P(pb3),msub(P(pb4),P(pb3)),msub(P(pb5),P(pb4))]
            for X,Y in zip(inc,pinc):
                s5_chain_checks+=1
                if not meq(mmul(mmul(U,X),Ut),Y): s5_chain_ok=False; break
            if not s5_chain_ok: break
        if not s5_chain_ok: break
    G=generic_poly(10); weights_chi=make_weights('chi'); weights_eta=make_weights('eta')
    weights_positive_valid=all(unit_jet_valid(weights_chi[s],s) and unit_jet_valid(weights_eta[s],s) for s in (3,4,5))
    taylor_rows=[]; taylor_ok=True
    for s in (3,4,5):
        om=PARAM[s]['omega']; T=tay(G,s); R=psub(G,T); exact_filter=(all(eligible(k,s) for k in T) and all(not eligible(k,s) for k in R) and padd(T,R)==G); exp_req=radial_exponent(s,om); exp_under=radial_exponent(s,om-1); ok=exact_filter and exp_req==0 and exp_under==-1; taylor_ok &= ok
        taylor_rows.append({'size':s,'omega':om,'eligible_terms':len(T),'remainder_terms':len(R),'exact_filter':exact_filter,'required_radial_exponent':exp_req,'under_subtraction_exponent':exp_under,'valid':ok})
    scheme_distinct=(weights_chi!=weights_eta); scheme_rows=[]; scheme_ok=True; reassoc_ok=True; all_basis=list(G.keys())
    seq_chi=chain_apply(G,weights_chi); seq_eta=chain_apply(G,weights_eta); diff=psub(seq_chi,seq_eta); generic_diff_nonzero=bool(diff); expanded_chi=expanded_apply(G,weights_chi); expanded_eta=expanded_apply(G,weights_eta); seq_exp_equal=(seq_chi==expanded_chi and seq_eta==expanded_eta)
    invisible_violations=[]; nonzero_inputs=[]
    for k in all_basis:
        d=psub(chain_apply(basis_monomial(k),weights_chi),chain_apply(basis_monomial(k),weights_eta))
        if d:
            nonzero_inputs.append(k)
            if common_kernel(k): invisible_violations.append(k)
    common_kernel_annihilated=(len(invisible_violations)==0); input_dependence_jet_visible=all(jet_visible(k) for k in nonzero_inputs)
    for f in chains:
        b3=next(b for b in f if len(b)==3); b4=next(b for b in f if len(b)==4); b5=next(b for b in f if len(b)==5); ok=scheme_distinct and generic_diff_nonzero and common_kernel_annihilated and input_dependence_jet_visible and seq_exp_equal; scheme_ok &= ok; reassoc_ok &= seq_exp_equal
        scheme_rows.append({'k3':sorted(b3),'k4':sorted(b4),'k5':sorted(b5),'scheme_difference_nonzero':generic_diff_nonzero,'nonzero_input_monomials':len(nonzero_inputs),'common_kernel_monomials':sum(common_kernel(k) for k in all_basis),'common_kernel_annihilated':common_kernel_annihilated,'invisible_input_violations':len(invisible_violations),'sequential_equals_noncommutative_expansion':seq_exp_equal,'classification':'SUPPORTED_ALLOWED_SCHEME_DIFFERENCE' if ok else 'INVALID_FOREST_OPERATOR'})
    bad_cov_fails=False
    for p in perms:
        U=perm_matrix(p); Ut=mtrans(U)
        for b in K3:
            if not meq(mmul(mmul(U,bad_label_projector(b)),Ut),bad_label_projector(pblock(b,p))): bad_cov_fails=True; break
        if bad_cov_fails: break
    under_objects=[{'size':s,'sub_order':PARAM[s]['omega']-1} for s in (3,4,5)]; under_rejected=all(radial_exponent(o['size'],o['sub_order'])<=-1 for o in under_objects)
    badw=make_weights('chi'); badw[4]=dict(badw[4]); badw[4][(0,1,0)]=Fraction(1,9); bad_weight_rejected=(not unit_jet_valid(badw[4],4))
    bad_source='termwise contact multiplication -> ten-wedge product -> full boundary contraction'; source_violation_rejected=(source_object_valid(SOURCE_FIREWALL) and not source_object_valid(bad_source))
    good_cfg={'K3':'symbolic:c3(y)','K4':'symbolic:c4(y)','K5':'symbolic:c5','scale':'symbolic:mu'}; bad_cfg=dict(good_cfg); bad_cfg['K5']=Fraction(7,11); numeric_smuggling_rejected=(symbolic_config_valid(good_cfg) and not symbolic_config_valid(bad_cfg))
    good_reassoc={'equation_kind':'same_graph_reassociation','promote_to_selector':False}; bad_reassoc={'equation_kind':'same_graph_reassociation','promote_to_selector':True}; reassoc_smuggling_rejected=(selector_firewall_valid(good_reassoc) and not selector_firewall_valid(bad_reassoc))
    controls={'label_dependent_projector_rejected_by_s5':bad_cov_fails,'under_subtraction_rejected':under_rejected,'bad_weight_unit_jet_rejected':bad_weight_rejected,'source_order_violation_rejected':source_violation_rejected,'numeric_finite_part_smuggling_rejected':numeric_smuggling_rejected,'reassociation_as_selector_smuggling_rejected':reassoc_smuggling_rejected}; controls_ok=all(controls.values())
    valid=(reconstruction_ok and block_ok and chain_geom_ok and s5_block_ok and s5_chain_ok and weights_positive_valid and taylor_ok and scheme_ok and reassoc_ok and controls_ok)
    classification='ITER082D_SM_K5_NESTED_NORMAL_PROJECTOR_TAYLOR_FOREST_SCHEME_CLASS_CONSTRUCTED_EXACT_SCOPED' if valid else 'ITER082D_SM_NESTED_NORMAL_FOREST_SCHEME_CONSTRUCTION_FAILS_EXACT_SCOPED'
    out={'iteration':'Iter082D-SM','execution_valid':valid,'classification':classification,'prereg_scope':'linearized/tubular local nested-normal forest extension scheme; no nonlinear chart-independence or selector claim','source_order_firewall':SOURCE_FIREWALL,'divergent_blocks':len(BLOCKS),'forest_total':len(fs),'maximal_chains':len(chains),'projector_block_rows':block_rows,'chain_geometry_rows':chain_geom,'s5_permutations_checked':len(perms),'s5_block_checks':s5_block_checks,'s5_chain_increment_checks':s5_chain_checks,'s5_block_covariance':s5_block_ok,'s5_chain_covariance':s5_chain_ok,'generic_degree_triples_total_le_10':len(G),'positive_weight_unit_jet_valid':weights_positive_valid,'taylor_rows':taylor_rows,'schemes_mechanically_distinct':scheme_distinct,'generic_scheme_difference_nonzero':generic_diff_nonzero,'scheme_difference_nonzero_input_count':len(nonzero_inputs),'scheme_common_kernel_count':sum(common_kernel(k) for k in all_basis),'scheme_common_kernel_annihilated':common_kernel_annihilated,'scheme_invisible_input_violations':len(invisible_violations),'sequential_equals_noncommutative_expansion':seq_exp_equal,'scheme_rows':scheme_rows,'controls':controls,'finite_parts_selected':False,'physical_selector_derived':False,'unique_k5_extension':False,'nonlinear_chart_independence_established':False}
    Path('iter082d_aggregate.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True)); return 0 if valid else 1
if __name__=='__main__': sys.exit(main())
