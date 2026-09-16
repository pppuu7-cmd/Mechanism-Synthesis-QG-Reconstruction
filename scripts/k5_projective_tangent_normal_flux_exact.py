import json
import sympy as sp
from itertools import combinations

# Control repair 1 for the prospectively frozen projective-tangent flux gate.
# Exact antisymmetric forms are dictionaries {ordered_index_tuple: coefficient}.
n=10
a=sp.symbols('a0:10')
t=sp.symbols('t')
s1=sum(a)


def omega9():
    # i_E(da0^...^da9)
    return {tuple(j for j in range(n) if j!=i): (-1)**i*a[i] for i in range(n)}


def contract(form, vec):
    out={}
    for inds,c in form.items():
        for p,i in enumerate(inds):
            key=inds[:p]+inds[p+1:]
            out[key]=sp.expand(out.get(key,0)+(-1)**p*vec[i]*c)
    return {k:sp.expand(v) for k,v in out.items() if sp.expand(v)!=0}


def form_equal(A,B):
    keys=set(A)|set(B)
    return all(sp.expand(A.get(k,0)-B.get(k,0))==0 for k in keys)


def pullback_top_coeff(form, amap, coords):
    # Pull an r-form back to r coordinates and return coefficient of dcoords[0]^... .
    r=len(coords); total=0
    for inds,c in form.items():
        if len(inds)!=r: continue
        J=sp.Matrix([[sp.diff(amap[i],x) for x in coords] for i in inds])
        total += c.subs(amap)*J.det()
    return sp.factor(total)


def valuation(expr):
    e=sp.cancel(expr)
    num,den=sp.fraction(e)
    P=sp.Poly(sp.expand(num),t)
    if P.is_zero: return None,sp.Integer(0)
    mind=min(m[0] for m,c in P.terms() if c!=0)
    lead=sp.expand(P.coeff_monomial(t**mind)/den.subs(t,0)) if den.subs(t,0)!=0 else sp.limit(e/t**mind,t,0)
    return int(mind),sp.factor(lead)


def chart(k, variant):
    Z=list(range(k)); O=list(range(k,n))
    # beta simplex chart: for k>1 choose a dependent beta; variant changes it when possible.
    bdep=Z[-1] if (variant==0 or k<3) else Z[-2]
    bind=[i for i in Z if i!=bdep]
    bs=sp.symbols('b0:'+str(len(bind)))
    # outside simplex chart: choose eliminated outside coordinate; for k=9 only one exists.
    if len(O)>1:
        odep=O[-1] if variant==0 else O[-2]
    else: odep=O[0]
    oind=[i for i in O if i!=odep]
    ys=sp.symbols('y0:'+str(len(oind)))
    amap={}
    for i,b in zip(bind,bs): amap[a[i]]=t*b
    amap[a[bdep]]=t*(1-sum(bs))
    for i,y in zip(oind,ys): amap[a[i]]=y
    amap[a[odep]]=1-t-sum(ys)
    return amap, list(bs)+list(ys), {'bdep':bdep,'odep':odep}


def main():
    Om=omega9(); E=list(a)
    assert form_equal(contract(Om,E),{})
    # Generic nonradial polynomial logarithmic field, exact integer coefficients.
    q=[(i+2)+a[(i+1)%n]+(i%3+1)*a[(i+3)%n] for i in range(n)]
    v=[sp.expand(a[i]*q[i]) for i in range(n)]
    S=sp.expand(sum(v))
    u=[sp.factor(v[i]-S*a[i]/s1) for i in range(n)]
    assert sp.factor(sum(u))==0
    iv=contract(Om,v); iu=contract(Om,u)
    assert form_equal(iv,iu)
    f=2+a[0]-3*a[4]
    vshift=[sp.expand(v[i]+f*a[i]) for i in range(n)]
    assert form_equal(iv,contract(Om,vshift))

    witnesses=[]
    for k in range(1,10):
        vals=[]
        for variant in (0,1):
            amap,facecoords,meta=chart(k,variant)
            # scalar Omega pullback on full chart (t + 8 tangential coordinates)
            scalar=pullback_top_coeff(Om,amap,[t]+facecoords)
            sv,sl=valuation(scalar)
            assert sv==k-1
            # normal flux: pull i_u Omega to t=const face coordinates.
            flux=pullback_top_coeff(iu,amap,facecoords)
            fv,fl=valuation(flux)
            vals.append(fv)
            witnesses.append({'k':k,'chart':variant,'chart_meta':meta,
                'scalar_valuation':sv,'scalar_lead':str(sl),
                'flux_valuation':fv,'flux_lead':str(fl),
                'omega_terms':len(Om),'contracted_terms':len(iu)})
        assert vals[0]==vals[1]

    # Exceptional exact cancellation control: Euler field has identically zero flux.
    assert form_equal(contract(Om,E),{})
    # Nontrivial radial shift remains exactly invisible at form level.
    assert form_equal(contract(Om,[v[i]+f*a[i] for i in range(n)]),iu)
    out={'classification':'K5_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING_EXACT_SCOPED',
         'control_repair':1,'differential_form_exact':True,'radial_form_invariance':True,
         'k_range':'1..9','charts_per_k':2,'witnesses':witnesses,
         'firewall':{'empty':'control_only','full':'control_only'}}
    with open('artifacts/k5_projective_tangent_flux/result.json','w') as fh: json.dump(out,fh,indent=2)
    print('classification='+out['classification'])
    print('exact_witnesses='+str(len(witnesses)))

if __name__=='__main__': main()
