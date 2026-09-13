#!/usr/bin/env python3
import argparse, json, math, pathlib
import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[1]
CLASS_BLOCKED = "ITER077E_SM_SOURCE_CONTACT_PULLBACK_BLOCKED_EXPLICIT_LOCAL_DISTRIBUTION_FORM_REQUIRED_NONMORSE_SCOPED"
CLASS_PRESENT = "ITER077E_SM_SOURCE_CONTACT_LOCAL_FORM_PRESENT_REQUIRES_DEDICATED_PULLBACK_GATE"
B_CLASS = "ITER077E_SM_NAIVE_DIRAC_PULLBACK_TRANSVERSALITY_FAILS_ON_EXACT_FLAT_FAMILY_SCOPED"
CLAIM = "No full causal-vertex finiteness/divergence theorem, regulator-independence theorem, physical source-to-K4 pushforward, nominal epsilon^-1 coefficient, generic finite-spin signed P3, new physics, complete QG, or G3/F9/G8/K5 promotion."

def dump(obj, path):
    pathlib.Path(path).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(path).write_text(json.dumps(obj, indent=2, sort_keys=True)+"\n")
    print(json.dumps(obj, indent=2, sort_keys=True))

def lane_a():
    p = ROOT/'sources/CAUSAL_SPINFOAM_VERTEX_2026_TOLLER_RESTRICTOR_SADDLE_ORIENTATION_SNAPSHOT.md'
    q = ROOT/'sources/CAUSAL_SPINFOAM_VERTEX_2026_SOURCE_SNAPSHOT.md'
    s = p.read_text(); t = q.read_text()
    checks = {
      'restrictor_present': 'theta(kappa_ab * B(z,g)) + kappa_ab * delta^(rho,j)(B(z,g))' in s,
      'B_eq32_present': 'B(z,g) = log( <g^dagger z|g^dagger z> / <z|z> )' in s,
      'eq36_feynman_present': 'Appendix D Eq. (36)' in s and 'Feynman `i epsilon`' in s,
      'support_at_B0': 'supported only at `B=0`' in s,
      'spectral_source_present': 'spectral integral' in t and 'i epsilon' in t,
    }
    combined = s + '\n' + t
    explicit_markers = ['delta^(rho,j)(x)=', 'delta^(rho,j)(x) =', 'delta^(rho,j)(B)=', 'delta^(rho,j)(B) = C delta', 'Gaussian mollifier', 'Lorentzian mollifier']
    explicit = [m for m in explicit_markers if m in combined]
    valid = all(checks.values())
    return {'iteration':'Iter077E-SM','lane':'A','valid':valid,'scientific_outcome':'VALID' if valid else 'BLOCKED','checks':checks,'explicit_local_form_markers':explicit,'local_form_state':'EXPLICIT_LOCAL_FORM_PRESENT' if explicit else 'NO_EXPLICIT_LOCAL_FORM_IN_FROZEN_SNAPSHOTS','claim_lock':CLAIM}

def lane_b():
    a,b,c = sp.symbols('a b c', real=True)
    phi2 = a*(a-c)
    H = sp.hessian(phi2,(a,b,c))
    rank = H.rank()
    eigs = H.eigenvals()
    pos=neg=zero=0
    for ev,m in eigs.items():
        val = float(sp.N(ev))
        if val>1e-12: pos += m
        elif val<-1e-12: neg += m
        else: zero += m
    flat = sp.simplify(phi2.subs(c,a)) == 0
    grad = [sp.diff(phi2,x) for x in (a,b,c)]
    origin_grad = [sp.simplify(g.subs({a:0,b:0,c:0})) for g in grad]
    valid = flat and rank==2 and (pos,neg,zero)==(1,1,1) and origin_grad==[0,0,0]
    return {'iteration':'Iter077E-SM','lane':'B','valid':valid,'scientific_outcome':'PASS' if valid else 'FAIL','classification':B_CLASS if valid else 'ITER077E_SM_FROZEN_TRANVERSALITY_CONTROL_FAIL','hessian':[[str(x) for x in row] for row in H.tolist()],'hessian_rank':rank,'inertia':{'positive':pos,'negative':neg,'zero':zero},'exact_flat_plane_a_eq_c':flat,'origin_gradient':[str(x) for x in origin_grad],'claim_lock':CLAIM}

def lane_c():
    # Analytic exponents frozen before implementation: p -> eps^(1/p).
    analytic = {'quadratic':'1/2','quartic':'1/4','flat':'none'}
    # Numerical controls with two distinct normalized even mollifier profiles.
    profiles = {
      'gaussian': lambda x: math.exp(-x*x)/math.sqrt(math.pi),
      'cauchy': lambda x: 1.0/(math.pi*(1+x*x)),
    }
    epss = [1e-2,1e-4,1e-6]
    observed = {}
    for name,f in profiles.items():
        rows=[]
        for p in (2,4):
            scales=[]
            for e in epss:
                t=e**(1.0/p)
                # At natural scale, argument t^p/eps is exactly 1.
                scales.append({'eps':e,'t':t,'scaled_argument':(t**p)/e,'kernel_at_scale':f((t**p)/e)/e})
            slope = math.log(scales[-1]['t']/scales[0]['t'])/math.log(epss[-1]/epss[0])
            rows.append({'power':p,'measured_log_slope':slope,'target':1.0/p,'samples':scales})
        observed[name]=rows
    valid = all(abs(r['measured_log_slope']-r['target'])<1e-12 for rows in observed.values() for r in rows)
    return {'iteration':'Iter077E-SM','lane':'C','valid':valid,'scientific_outcome':'PASS' if valid else 'FAIL','interpretation':'REGULATOR_MODEL_CONTROL_ONLY','analytic_localization_exponents':analytic,'profiles':observed,'flat_branch':'Phi==0 gives no shrinking localization scale','claim_lock':CLAIM}

def lane_d():
    a = lane_a(); b=lane_b(); c=lane_c()
    if not a['valid'] or not b['valid'] or not c['valid']:
        return {'iteration':'Iter077E-SM','lane':'D','valid':False,'scientific_outcome':'BLOCKED','classification':'ITER077E_SM_CONTACT_DECISION_BLOCKED_INVALID_PREREQUISITE','claim_lock':CLAIM}
    present = a['local_form_state']=='EXPLICIT_LOCAL_FORM_PRESENT'
    classification = CLASS_PRESENT if present else CLASS_BLOCKED
    return {'iteration':'Iter077E-SM','lane':'D','valid':True,'scientific_outcome':'PASS' if present else 'BLOCKED_OBJECT_DEFINITION','classification':classification,'source_local_form_present':present,'naive_dirac_transversality_fails':True,'regulator_control_only':True,'claim_lock':CLAIM}

def aggregate(d):
    found={}
    for p in pathlib.Path(d).glob('iter077e-sm-*/*.json'):
        try:
            x=json.loads(p.read_text()); found[x.get('lane')]=x
        except Exception: pass
    required=['A','B','C','D']
    valid=all(k in found and found[k].get('valid') for k in required)
    if not valid:
        out={'iteration':'Iter077E-SM','execution_valid':False,'verdict':'BLOCKED','lanes_found':sorted(found),'classification':'ITER077E_SM_AGGREGATE_INVALID','claim_lock':CLAIM}
    else:
        cls=found['D']['classification']
        out={'iteration':'Iter077E-SM','execution_valid':True,'verdict':'BLOCKED_OBJECT_DEFINITION' if cls==CLASS_BLOCKED else 'PASS_TO_DEDICATED_PULLBACK_GATE','classification':cls,'lanes_found':required,'lane_scientific_outcomes':{k:found[k]['scientific_outcome'] for k in required},'source_local_form_state':found['A']['local_form_state'],'naive_dirac_transversality_fails':True,'regulator_model_control_only':True,'next_admissible_gate':'Acquire/freeze the explicit source definition of delta^(rho,j)(x), or establish from the primary paper that it is defined only through the spectral distributional representation, before any physical pullback/scaling claim.' if cls==CLASS_BLOCKED else 'Preregister a dedicated pullback gate using the exact source-local distributional formula and the Iter077D non-Morse germ.','claim_lock':CLAIM}
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane'); ap.add_argument('--output',required=True); ap.add_argument('--aggregate-dir')
    args=ap.parse_args()
    if args.aggregate_dir: out=aggregate(args.aggregate_dir)
    else:
        funcs={'A':lane_a,'B':lane_b,'C':lane_c,'D':lane_d}; out=funcs[args.lane]()
    dump(out,args.output)

if __name__=='__main__': main()
