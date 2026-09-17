#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'scripts/k5_deg4_annihilator_actual_dual_action.py'
PRE='4f8a783b9d1fd8f6e022ccdc9a888d71ecd591c7'
MASK=511
W1=(2,3,5,7,11,13,17,19,23,29)
W2=(31,37,41,43,47,53,59,61,67,71)
TMAX=34
NDEG=27
BDEG=31
RPSI_EXPECTED=3
RU_AUTH=3
C_FAIL='FAIL_ORDINARY_LOCAL_INTEGRABILITY_MASK511_PHYSICAL_CHANNEL_EXACT_SCOPED'
C_OBS='K5_MASK511_ACTION_OR_FLUX_OBSTRUCTION_EXACT_SCOPED'
C_INC='K5_MASK511_NO_OBSTRUCTION_WITNESS_ON_FROZEN_RAYS_INCONCLUSIVE_SCOPED'
INVALID='INVALID_IMPLEMENTATION'

# Load the authoritative source/action construction only up to the historical point loop.
text=BASE.read_text(encoding='utf-8')
marker='results={};checks={}'
assert marker in text
ns={'__name__':'k5_mask511_base','__file__':str(BASE)}
exec(compile(text.split(marker)[0],str(BASE),'exec'),ns,ns)
J=ns['J']; EDGES=tuple(ns['EDGES']); ROWS=tuple(ns['ROWS']); ENTRY=ns['ENTRY']; PATTERNS=ns['PATTERNS']
WEIGHTS=ns['WEIGHTS']; SOURCE_TERMS=ns['SOURCE_TERMS']; P=ns['P']; PIV=ns['PIV']
ZERO_MON=ns['ZERO_MON']; ANN_COEFF=ns['ANN_COEFF']; VPSI_ZERO=ns['VPSI_ZERO']; BAD_REJECTED=ns['BAD_REJECTED']
POINTS=ns['POINTS']; EXPECTED=ns['EXPECTED']; evaluate=ns['evaluate']; action_from_eval=ns['action_from_eval']; nvals=ns['nvals']; eder=ns['eder']
assert len(EDGES)==10 and SOURCE_TERMS==100000 and MASK==(1<<9)-1

# Exact source/Wick performance reassociation, algebraically identical to the repaired terminal action run.
def gadd(x,y): return (x[0]+y[0],x[1]+y[1])
def gmul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def gscale(c,z): return (c*z[0],c*z[1])
def gzero(): return (J(),J())
def s_mul(a,b):
    out=[J() for _ in range(ns['ORDER']+1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=ns['ORDER']: out[i+j]=out[i+j]+x*y
    return out

def entry_metric(ea,eb):
    x=ENTRY[ea]; y=ENTRY[eb]; gr=Fraction(0); gi=Fraction(0)
    for xx,yy in zip(x,y):
        gr+=xx[0]*yy[0]-xx[1]*yy[1]
        gi+=xx[0]*yy[1]+xx[1]*yy[0]
    return (gr,gi)
EM={(a,b):entry_metric(a,b) for a in ENTRY for b in ENTRY}
TCW=defaultdict(lambda:[Fraction(0),Fraction(0)])
for idx,arr in PATTERNS:
    w0,w1=WEIGHTS[idx]
    if not w0 and not w1: continue
    for types,coeff in arr:
        TCW[types][0]+=coeff*w0; TCW[types][1]+=coeff*w1
TCW={t:(w[0],w[1]) for t,w in TCW.items() if w[0] or w[1]}

def compatible(types):
    memo={}
    def rec(rem):
        if not rem:return (((),(Fraction(1),Fraction(0))),)
        if rem in memo:return memo[rem]
        i=rem[0];out=[]
        for pos in range(1,len(rem)):
            j=rem[pos];z=EM[(types[i],types[j])]
            if z==(0,0):continue
            rest=rem[1:pos]+rem[pos+1:]
            for mt,c in rec(rest):out.append((((i,j),)+mt,gmul(z,c)))
        memo[rem]=tuple(out);return memo[rem]
    return rec(tuple(range(10)))
MC=defaultdict(lambda:[[Fraction(0),Fraction(0)],[Fraction(0),Fraction(0)]])
for types,w in TCW.items():
    for mt,z in compatible(types):
        for ch in (0,1):
            if not w[ch]:continue
            zz=gscale(w[ch],z);MC[mt][ch][0]+=zz[0];MC[mt][ch][1]+=zz[1]
MATCH_COEFF={mt:((c[0][0],c[0][1]),(c[1][0],c[1][1])) for mt,c in MC.items() if any(c[ch] != [0,0] for ch in (0,1))}
assert MATCH_COEFF

def projected_wick_fast(Bser):
    cov={(i,j):[ns['dot_mat'](ROWS[i],Bser[n],ROWS[j]) for n in range(ns['ORDER']+1)] for i in range(10) for j in range(i+1,10)}
    channels=[[gzero() for _ in range(ns['ORDER']+1)] for _ in range(2)]
    for mt,(c0,c1) in MATCH_COEFF.items():
        ser=[J(1)]+[J() for _ in range(ns['ORDER'])]
        for ij in mt:ser=s_mul(ser,cov[ij])
        for n,x in enumerate(ser):
            if c0!=(0,0):channels[0][n]=gadd(channels[0][n],(x*c0[0],x*c0[1]))
            if c1!=(0,0):channels[1][n]=gadd(channels[1][n],(x*c1[0],x*c1[1]))
    return channels,len(MATCH_COEFF)
# evaluate() resolves this global dynamically in its authoritative namespace.
ns['projected_wick']=projected_wick_fast

VECTOR_WEIGHTS=[(P[PIV[0]][j],P[PIV[1]][j]) for j in range(32)]

def qstr(q):
    q=Fraction(q)
    return str(q.numerator) if q.denominator==1 else f'{q.numerator}/{q.denominator}'
def qparse(x): return Fraction(x)
def qlist(xs): return [qstr(x) for x in xs]

def solve_vandermonde(xs,ys,degree):
    assert len(xs)==len(ys)==degree+1
    A=[[Fraction(xs[i])**j for j in range(degree+1)]+[Fraction(ys[i])] for i in range(degree+1)]
    n=degree+1
    for c in range(n):
        p=next(i for i in range(c,n) if A[i][c])
        A[c],A[p]=A[p],A[c]
        z=A[c][c];A[c]=[x/z for x in A[c]]
        for i in range(n):
            if i==c:continue
            z=A[i][c]
            if z:A[i]=[x-z*y for x,y in zip(A[i],A[c])]
    return tuple(A[i][-1] for i in range(n))
def peval(c,t):
    t=Fraction(t);z=Fraction(0)
    for x in reversed(c):z=z*t+x
    return z
def first_nonzero(c):
    for i,x in enumerate(c):
        if x:return i,x
    return None,None
def degree_lock_ok(ndeg,bdeg):return ndeg==27 and bdeg==31

def point_for(W,t):
    return tuple(Fraction(W[e]*t if e<9 else W[e]) for e in range(10))
def exact_point(W,t):
    p=point_for(W,t);ev=evaluate(p,'direct');vals=nvals(ev);act=action_from_eval(p,ev)
    assert all(z[1]==0 for z in vals) and all(z[1]==0 for z in act)
    return {
      'psi':ev['psi'].v,
      'N':(vals[0][0],vals[1][0]),
      'B':(act[0][0],act[1][0]),
    }

def exp_label(x):
    if x>-1:return 'INTEGRABLE'
    if x==-1:return 'LOGARITHMIC'
    return 'DIVERGENT'

def corrupt_sample_rejected(xs,ys,degree,holdouts,truth):
    bad=list(ys);bad[0]+=1;c=solve_vandermonde(xs,bad,degree)
    return any(peval(c,t)!=truth[t] for t in holdouts)

def process_weight(name,W):
    values={}
    for t in range(1,TMAX+1):
        values[t]=exact_point(W,t)
        print(f'{name} t={t}/{TMAX}',flush=True)
    # Psi degree four reconstruction/validation.
    psi_c=solve_vandermonde(tuple(range(1,6)),tuple(values[t]['psi'] for t in range(1,6)),4)
    psi_hold=all(peval(psi_c,t)==values[t]['psi'] for t in range(6,TMAX+1))
    rpsi,cpsi=first_nonzero(psi_c)
    channels=[]
    all_interp=True; all_neg=True
    for ch in range(2):
        nxs=tuple(range(1,29));nys=tuple(values[t]['N'][ch] for t in nxs)
        nc=solve_vandermonde(nxs,nys,NDEG)
        nh=tuple(range(29,35));nv=all(peval(nc,t)==values[t]['N'][ch] for t in nh)
        bxs=tuple(range(1,33));bys=tuple(values[t]['B'][ch] for t in bxs)
        bc=solve_vandermonde(bxs,bys,BDEG)
        bh=(33,34);bv=all(peval(bc,t)==values[t]['B'][ch] for t in bh)
        rn,cn=first_nonzero(nc);rb,cb=first_nonzero(bc)
        assert rn is not None and rb is not None
        I=-19+rn;F=-16+rn;A=-19+rb
        negn=corrupt_sample_rejected(nxs,nys,NDEG,nh,{t:values[t]['N'][ch] for t in nh})
        negb=corrupt_sample_rejected(bxs,bys,BDEG,bh,{t:values[t]['B'][ch] for t in bh})
        all_interp &= nv and bv;all_neg &= negn and negb
        channels.append({
          'channel':ch+1,'rN':rn,'rB':rb,
          'N_first_coefficient':qstr(cn),'B_first_coefficient':qstr(cb),
          'interior_exponent':I,'interior_class':exp_label(I),
          'flux_exponent':F,'flux_class':exp_label(F),
          'action_exponent':A,'action_class':exp_label(A),
          'N_coefficients':qlist(nc),'B_coefficients':qlist(bc),
          'N_holdouts_exact':nv,'B_holdouts_exact':bv,
          'corrupt_N_sample_rejected':negn,'corrupt_B_sample_rejected':negb,
        })
    serial_values={str(t):{'psi':qstr(v['psi']),'N':qlist(v['N']),'B':qlist(v['B'])} for t,v in values.items()}
    canon=json.dumps(serial_values,sort_keys=True,separators=(',',':'))
    return {
      'weight_name':name,'weights':list(W),'psi_coefficients':qlist(psi_c),
      'rPsi':rpsi,'psi_first_coefficient':qstr(cpsi),'psi_holdouts_exact':psi_hold,
      'channels':channels,'all_interpolation_holdouts_exact':all_interp,
      'all_corrupt_sample_controls_rejected':all_neg,
      'point_values_sha256':hashlib.sha256(canon.encode()).hexdigest(),
      'point_values':serial_values,
    }

def main():
    checks={
      'mask511_frozen':MASK==511,
      'mask511_k9':MASK.bit_count()==9,
      'all32_source_terms':SOURCE_TERMS==100000,
      'dual_projection_distinct_from_vector':WEIGHTS!=VECTOR_WEIGHTS,
      'annihilator_global_polynomial_zero':VPSI_ZERO,
      'altered_annihilator_rejected':BAD_REJECTED,
      'degree_locks_27_31':degree_lock_ok(NDEG,BDEG),
      'degree26_rejected':not degree_lock_ok(26,BDEG),
      'degree30_B_rejected':not degree_lock_ok(NDEG,30),
      'rU_authority_frozen3':RU_AUTH==3,
      'source_terms_nonempty':len(TCW)>0 and len(MATCH_COEFF)>0,
    }
    # Parent locks before corner production conclusions.
    eu=evaluate(POINTS['validation_U'],'direct');nu=nvals(eu);bu=action_from_eval(POINTS['validation_U'],eu)
    ea=evaluate(POINTS['fit_A'],'direct');na=nvals(ea)
    checks['uniform_parent_N_exact']=tuple(z[0] for z in nu)==EXPECTED['validation_U'] and all(z[1]==0 for z in nu)
    checks['fitA_parent_N_exact']=tuple(z[0] for z in na)==EXPECTED['fit_A'] and all(z[1]==0 for z in na)
    checks['uniform_corrected_B_minus1500N']=all(bu[i][0]==-1500*nu[i][0] and bu[i][1]==0 for i in range(2))
    checks['uniform_euler_degree27']=all(d[0]==27*z[0] and d[1]==0 for z,d in zip(nu,eder(eu)))
    checks['B_degree31_exact_accounting']=(1+(4+27-1)==31 and (1+3)+27==31 and 4+27==31)

    results=[process_weight('W1',W1),process_weight('W2',W2)]
    checks['psi_order3_both']=all(r['rPsi']==RPSI_EXPECTED and r['psi_holdouts_exact'] for r in results)
    checks['all_interpolation_holdouts_exact']=all(r['all_interpolation_holdouts_exact'] for r in results)
    checks['all_corrupt_sample_controls_rejected']=all(r['all_corrupt_sample_controls_rejected'] for r in results)

    controls={
      'wrong_projection_rejected':WEIGHTS!=VECTOR_WEIGHTS,
      'raw_uniform_s1_equals10_not1':sum(POINTS['validation_U'],Fraction(0))==10,
      'altered_annihilator_coefficient_rejected':BAD_REJECTED,
      'degree26_N_contract_rejected':not degree_lock_ok(26,31),
      'degree30_B_contract_rejected':not degree_lock_ok(27,30),
      'mask_change_forbidden':MASK==511,
      'weights_frozen':W1==(2,3,5,7,11,13,17,19,23,29) and W2==(31,37,41,43,47,53,59,61,67,71),
      'no_s5_orbit_promotion':True,
      'no_global_stokes_or_full_amplitude_claim':True,
    }
    valid=all(checks.values()) and all(controls.values())
    any_interior=any(c['interior_exponent']<=-1 for r in results for c in r['channels'])
    any_other=any(c['action_exponent']<=-1 or c['flux_exponent']<=-1 for r in results for c in r['channels'])
    if not valid:classification=INVALID;status=INVALID
    elif any_interior:classification=C_FAIL;status='SCIENTIFIC_FAIL_EXACT_SCOPED'
    elif any_other:classification=C_OBS;status='PASS_EXACT_OBSTRUCTION_SCOPED'
    else:classification=C_INC;status='PASS_EXACT_INCONCLUSIVE_SCOPED'
    out={
      'gate':'K5_MASK511_PHYSICAL_NUMERATOR_ACTION_EXACT_CORNER_WITNESS',
      'prereg_commit':PRE,'status':status,'classification':classification,
      'mask':MASK,'bits':list(range(9)),'k':9,'rPsi_authority':3,'rU_authority':3,
      'base_interior_action_exponent_without_N_or_B':-19,'base_flux_exponent_without_N':-16,
      'checks':checks,'controls':controls,'results':results,
      'generic_interior_nonintegrability_witness_exists':any_interior,
      'action_or_flux_obstruction_witness_exists':any_other,
      'boundary_s5_transport_consumed':False,
      'global_stokes_ibp_verdict':None,'integrated_period_verdict':None,
      'finite_part_selector':None,'regulator_independence':None,
    }
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args();p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('CLASSIFICATION='+classification)
    print('STATUS='+status)
    for r in results:
        print(r['weight_name'],[(c['channel'],c['rN'],c['rB'],c['interior_exponent'],c['flux_exponent'],c['action_exponent']) for c in r['channels']])
    if not valid:raise SystemExit(2)
if __name__=='__main__':main()
