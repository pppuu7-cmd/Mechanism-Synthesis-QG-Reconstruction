import argparse, hashlib, json, os, re
import sympy as sp
N=10
a=sp.symbols('a0:10'); t=sp.symbols('t')

def canon(x): return sp.cancel(sp.together(x))
def zero(x): return canon(x)==0

def omega_form(alpha_vals):
    return {tuple(j for j in range(N) if j!=i): ((-1)**i)*alpha_vals[i] for i in range(N)}
def interior(form,vec):
    out={}
    for basis,c in form.items():
        for pos,idx in enumerate(basis):
            key=basis[:pos]+basis[pos+1:]; out[key]=out.get(key,0)+((-1)**pos)*c*vec[idx]
    return {k:canon(v) for k,v in out.items() if not zero(v)}
def forms_equal(f,g): return all(zero(f.get(k,0)-g.get(k,0)) for k in set(f)|set(g))

def chart(Z,variant,tag):
    Z=tuple(sorted(Z)); O=tuple(i for i in range(N) if i not in Z); k=len(Z)
    bdep=Z[-1] if variant==0 or k==1 else Z[0]; odep=O[-1] if variant==0 or len(O)==1 else O[0]
    bind=[i for i in Z if i!=bdep]; oind=[i for i in O if i!=odep]
    bs=list(sp.symbols(f'b{tag}_0:{len(bind)}')); ys=list(sp.symbols(f'y{tag}_0:{len(oind)}'))
    amap={}; bcoord={}; ycoord={}
    for i,x in zip(bind,bs): amap[i]=t*x; bcoord[i]=x
    amap[bdep]=t*(1-sum(bs))
    for i,x in zip(oind,ys): amap[i]=x; ycoord[i]=x
    amap[odep]=1-t-sum(ys)
    return {'Z':Z,'O':O,'bdep':bdep,'odep':odep,'bind':bind,'oind':oind,'bs':bs,'ys':ys,'face':bs+ys,'amap':amap,'bcoord':bcoord,'ycoord':ycoord}

def frozen_point(c):
    sub={}; m=len(c['bs'])
    if m:
        sw=sum(range(1,m+1))
        for j,x in enumerate(c['bs']): sub[x]=sp.Rational(j+1,2*sw)
    m=len(c['ys'])
    if m:
        sw=sum(range(1,m+1))
        for j,x in enumerate(c['ys']): sub[x]=sp.Rational(j+1,3*sw)
    return sub

def q_generic(alpha): return [sp.Integer(i+3)+2*alpha[(i+2)%N]-alpha[(i+5)%N] for i in range(N)]
def q_exception(alpha): return [sp.Integer(2)+(i+1)**2*alpha[0] for i in range(N)]
def q_generic_permuted(alpha,p):
    q=[None]*N
    for i in range(N): q[p[i]]=sp.Integer(i+3)+2*alpha[p[(i+2)%N]]-alpha[p[(i+5)%N]]
    return q

def u_from(alpha,q):
    v=[canon(alpha[i]*q[i]) for i in range(N)]; S=canon(sum(v)); return v,[canon(v[i]-S*alpha[i]) for i in range(N)]

def poly_witness(c,pt,qbuilder):
    alpha=[canon(c['amap'][i].subs(pt,simultaneous=True)) for i in range(N)]; assert zero(sum(alpha)-1)
    q=qbuilder(alpha); v,u=u_from(alpha,q)
    E=sp.Matrix(alpha); T=sp.Matrix([sp.diff(c['amap'][i],t).subs(pt,simultaneous=True) for i in range(N)])
    F=[sp.Matrix([sp.diff(c['amap'][i],z).subs(pt,simultaneous=True) for i in range(N)]) for z in c['face']]
    scalar=canon(sp.Matrix.hstack(E,T,*F).det(method='domain-ge'))
    flux=canon(sp.Matrix.hstack(E,sp.Matrix(u),*F).det(method='domain-ge'))
    normal=canon(sum(u[i] for i in c['Z']))
    return scalar,flux,normal

def numeric_witness(c,pt,tval,qbuilder):
    s,f,n=poly_witness(c,pt,qbuilder); ev={t:sp.Rational(tval)}
    return canon(s.subs(ev)),canon(f.subs(ev)),canon(n.subs(ev))

def order(expr):
    expr=canon(expr)
    if expr==0:return None,sp.Integer(0)
    num,den=sp.fraction(expr); Pn=sp.Poly(sp.expand(num),t); Pd=sp.Poly(sp.expand(den),t)
    on=min(m[0] for m,c in Pn.terms() if c!=0); od=min(m[0] for m,c in Pd.terms() if c!=0)
    return int(on-od),canon(Pn.coeff_monomial(t**on)/Pd.coeff_monomial(t**od))

def transition_map(c0,c1,include_t):
    sub={t:t} if include_t else {}
    for i,x in c1['bcoord'].items(): sub[x]=canon(c0['amap'][i]/t)
    for i,x in c1['ycoord'].items(): sub[x]=c0['amap'][i]
    src=([t]+c0['face']) if include_t else c0['face']; dst=([t]+c1['face']) if include_t else c1['face']
    mapped=[sub.get(x,x) for x in dst]
    return sub,src,dst,mapped

def transition_det_at(c0,c1,include_t,p0,tval):
    sub,src,dst,mapped=transition_map(c0,c1,include_t); ev=dict(p0); ev[t]=sp.Rational(tval)
    J=sp.Matrix([[sp.diff(mapped[i],x).subs(ev,simultaneous=True) for x in src] for i in range(len(dst))])
    return canon(J.det(method='domain-ge')),sub

def edge_perm():
    edges=[(i,j) for i in range(5) for j in range(i+1,5)]; idx={e:i for i,e in enumerate(edges)}; vp=(1,2,3,4,0); p=[]
    for i,j in edges:
        x,y=sorted((vp[i],vp[j])); p.append(idx[(x,y)])
    return vp,p

def sha(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return h.hexdigest()
def audit_source(text):
    pats=[r'\bjac_exp\s*=\s*k\s*-\s*1\b',r'\bscalar_valuation\s*=\s*k\s*-\s*1\b',r'\bsv\s*=\s*k\s*-\s*1\b',r"['\"]scalar_valuation['\"]\s*:\s*k\s*-\s*1"]
    bad=[p for p in pats if re.search(p,text)]; req=['def pullback_top_coeff','def valuation','sp.Matrix','sp.diff']; miss=[x for x in req if x not in text]
    return not bad and not miss,{'forbidden_assignment_patterns':bad,'missing_mechanical_markers':miss}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--parent-json',required=True); ap.add_argument('--researcher-source',required=True); ap.add_argument('--out',required=True); args=ap.parse_args()
    parent=json.load(open(args.parent_json)); src=open(args.researcher_source).read()
    prov={'parent_json_sha':sha(args.parent_json)=='017f25d431bbf137aefd9f375ddbefbff45d551bfda4fd46a0a55a825aa91fe3','parent_classification':parent.get('classification')=='K5_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING_EXACT_SCOPED','parent_status':parent.get('status')=='PASS_EXACT_SCOPED'}
    hard,hard_detail=audit_source(src)
    cov={'18_parent_witnesses':len(parent.get('witnesses',[]))==18,'9_parent_chart_relations':len(parent.get('chart_relations',[]))==9,'9_parent_permutation_witnesses':len(parent.get('permutation_witnesses',[]))==9,'parent_exceptional_present':isinstance(parent.get('exceptional_witness'),dict),'empty_firewall_nonphysical':parent.get('firewalls',{}).get('empty_set',{}).get('physical_boundary_verdict') is None,'full_firewall_nonphysical':parent.get('firewalls',{}).get('full_set',{}).get('physical_boundary_verdict') is None,'no_forbidden_kminus1_assignment':hard}

    alpha0=[sp.Rational(i+1,55) for i in range(N)]; q0=q_generic(alpha0); v0,u0=u_from(alpha0,q0); Om0=omega_form(alpha0); fr=sp.Rational(7,5); vsh=[v0[i]+fr*alpha0[i] for i in range(N)]
    math={'ambient_u_s1':zero(sum(u0)),'ambient_iE_zero':forms_equal(interior(Om0,alpha0),{}),'ambient_iv_eq_iu':forms_equal(interior(Om0,v0),interior(Om0,u0)),'ambient_radial_shift':forms_equal(interior(Om0,vsh),interior(Om0,u0))}

    W=[]; R=[]; scalar_orders=[]; face_ok=True; trans_ok=True
    for k in range(1,10):
        Z=tuple(range(k)); charts=[]
        for variant in (0,1):
            c=chart(Z,variant,f'k{k}v{variant}'); pt=frozen_point(c); S,F,U=poly_witness(c,pt,q_generic)
            so,sl=order(S); fo,fl=order(F); no,nl=order(U); rel=zero(F-S*U); face_ok &= rel; scalar_orders.append(so)
            W.append({'k':k,'chart':variant,'bdep':c['bdep'],'odep':c['odep'],'scalar_order':so,'flux_order':fo,'normal_order':no,'scalar_lead':str(sl),'flux_lead':str(fl),'normal_lead':str(nl),'face_identity':rel})
            charts.append((c,pt))
        cA,pA=charts[0]; cB,pB=charts[1]; t0=sp.Rational(1,7)
        sA,fA,nA=numeric_witness(cA,pA,t0,q_generic)
        sub9,src9,dst9,map9=transition_map(cA,cB,True); ev=dict(pA); ev[t]=t0
        bpt={x:canon(expr.subs(ev,simultaneous=True)) for x,expr in sub9.items() if x!=t}
        sB,fB,nB=numeric_witness(cB,bpt,t0,q_generic)
        j9,_=transition_det_at(cA,cB,True,pA,t0); j8,_=transition_det_at(cA,cB,False,pA,t0)
        se=zero(sA-sB*j9); fe=zero(fA-fB*j8); distinct=(cA['bdep'],cA['odep'])!=(cB['bdep'],cB['odep']); trans_ok &= se and fe and distinct
        R.append({'k':k,'t_witness':'1/7','distinct':distinct,'scalar_transition_det':str(j9),'flux_transition_det':str(j8),'scalar_equal':se,'flux_equal':fe})
    math['18_explicit_differential_form_witnesses']=face_ok and len(W)==18
    math['mechanical_scalar_orders_0_to_8']=scalar_orders==[j for j in range(9) for _ in (0,1)]
    math['9_orientation_jacobian_relations']=trans_ok

    vp,ep=edge_perm(); PW=[]; perm_ok=True
    for k in range(1,10):
        Z=tuple(range(k)); Zp=tuple(sorted(ep[i] for i in Z)); c=chart(Z,0,f'o{k}'); cp=chart(Zp,0,f'p{k}'); S,F,U=poly_witness(c,frozen_point(c),q_generic)
        def qP(alpha,ep=ep): return q_generic_permuted(alpha,ep)
        SP,FP,UP=poly_witness(cp,frozen_point(cp),qP)
        so,_=order(S); fo,_=order(F); spv,_=order(SP); fpv,_=order(FP); ok=(so,fo)==(spv,fpv); perm_ok &= ok
        PW.append({'k':k,'Z':list(Z),'Zp':list(Zp),'scalar_orders':[so,spv],'flux_orders':[fo,fpv],'ok':ok})
    math['9_s5_permutation_controls']=perm_ok

    ce=chart((0,),0,'ex'); pe=frozen_point(ce); SG,FG,UG=poly_witness(ce,pe,q_generic); SX,FX,UX=poly_witness(ce,pe,q_exception)
    go,gl=order(FG); xo,xl=order(FX); exc={'generic_order':go,'exceptional_order':xo,'exceptional_lead':str(xl),'advanced_to_higher_finite_order':go is not None and xo is not None and xo>go and not zero(FX)}; math['independent_exceptional_advance']=exc['advanced_to_higher_finite_order']

    prov_ok=all(prov.values()); cov_ok=all(cov.values()); math_ok=all(math.values())
    verdict='CONFIRMED_SCOPED' if prov_ok and cov_ok and math_ok else ('INVALID_PROVENANCE' if not prov_ok else ('INVALID_IMPLEMENTATION' if not cov_ok else 'SCIENTIFIC_FAIL_CONFIRMED'))
    out={'verdict':verdict,'provenance_checks':prov,'coverage_checks':cov,'source_hardcode_audit':hard_detail,'math_checks':math,'explicit_witnesses':W,'chart_relations':R,'permutation':{'vertex_perm':list(vp),'edge_perm':ep,'witnesses':PW},'exceptional':exc,'interpretation_ceiling':{'physical_34_orbit_classification':None,'global_stokes_ibp':None,'integrated_k5_period':None,'F8_reduction':None,'finite_part_selector':None,'regulator_independence':None,'F9_G3_G8':None,'new_physics_found':None,'complete_qg':None}}
    os.makedirs(os.path.dirname(args.out) or '.',exist_ok=True); json.dump(out,open(args.out,'w'),indent=2,sort_keys=True)
    print('VERDICT='+verdict); print('PROVENANCE_OK='+str(prov_ok).lower()); print('COVERAGE_OK='+str(cov_ok).lower()); print('MATH_OK='+str(math_ok).lower()); print('EXCEPTIONAL_ORDERS='+str((go,xo)))
if __name__=='__main__':main()
