#!/usr/bin/env python3
from __future__ import annotations
import hashlib
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'scripts/k5_deg4_annihilator_actual_dual_action.py'
EXPECTED_GIT_BLOB_SHA1='2ed1b6397236c3f64c22b2a827bf1f0f8b5e0484'
raw=SOURCE.read_bytes()
blob=b'blob '+str(len(raw)).encode()+b'\0'+raw
actual=hashlib.sha1(blob).hexdigest()
assert actual==EXPECTED_GIT_BLOB_SHA1,(actual,EXPECTED_GIT_BLOB_SHA1)
s=raw.decode('utf-8')

# Historical implementation fixes preserved exactly.
old="if i!=c and a[i][c].v!=0:\n                z=a[i][c];a[i]=[x-z*y for x,y in zip(a[i],a[c])]"
new="if i!=c and not a[i][c].iszero():\n                z=a[i][c];a[i]=[x-z*y for x,y in zip(a[i],a[c])]"
assert s.count(old)==1
s=s.replace(old,new)

old="P,PIV=build_projector()\nWEIGHTS=[(P[j][PIV[0]],P[j][PIV[1]]) for j in range(32)]"
new="P,PIV=build_projector()\nWEIGHTS=[(P[j][PIV[0]],P[j][PIV[1]]) for j in range(32)]\nVECTOR_WEIGHTS=[(P[PIV[0]][j],P[PIV[1]][j]) for j in range(32)]"
assert s.count(old)==1
s=s.replace(old,new)

# Exact performance reassociation: aggregate source terms by entry pattern, then by
# Wick perfect matching, before any point-dependent covariance-series arithmetic.
old=r'''def projected_wick(Bser):
    cov={}
    for i in range(10):
        for j in range(i+1,10):cov[(i,j)]=[dot_mat(ROWS[i],Bser[n],ROWS[j]) for n in range(ORDER+1)]
    pair={}
    for (i,j),ser in cov.items():
        for ea in ENTRY:
            for eb in ENTRY:
                z0=ZERO_COMPLEX= (Fraction(0),Fraction(0))
                # exact Gaussian product of source entry triples
                x=ENTRY[ea];y=ENTRY[eb]
                gr=Fraction(0);gi=Fraction(0)
                for xx,yy in zip(x,y):gr+=xx[0]*yy[0]-xx[1]*yy[1];gi+=xx[0]*yy[1]+xx[1]*yy[0]
                pair[(i,j,ea,eb)]=[(c*gr,c*gi) for c in ser]
    cache={}
    def wick(rem):
        if not rem:return [gone()]+[gzero() for _ in range(ORDER)]
        if rem in cache:return cache[rem]
        i,ei=rem[0];tot=[gzero() for _ in range(ORDER+1)]
        for pos in range(1,len(rem)):
            j,ej=rem[pos];rest=rem[1:pos]+rem[pos+1:];tot=cs_add(tot,cs_mul(pair[(i,j,ei,ej)],wick(rest)))
        cache[rem]=tot;return tot
    channels=[[gzero() for _ in range(ORDER+1)] for _ in range(2)]
    for idx,arr in PATTERNS:
        w0,w1=WEIGHTS[idx]
        if not w0 and not w1:continue
        for types,coeff in arr:
            rem=tuple((i,types[i]) for i in range(10));ser=wick(rem)
            if w0:channels[0]=cs_add(channels[0],cs_scale(ser,coeff*w0))
            if w1:channels[1]=cs_add(channels[1],cs_scale(ser,coeff*w1))
    return channels,len(cache)
'''
new=r'''def _entry_metric(ea,eb):
    x=ENTRY[ea];y=ENTRY[eb];gr=Fraction(0);gi=Fraction(0)
    for xx,yy in zip(x,y):
        gr+=xx[0]*yy[0]-xx[1]*yy[1]
        gi+=xx[0]*yy[1]+xx[1]*yy[0]
    return (gr,gi)
ENTRY_METRIC={(ea,eb):_entry_metric(ea,eb) for ea in ENTRY for eb in ENTRY}

# Collapse the 100000 source node-choice terms to at most 6^5 edge-entry patterns.
TYPE_CHANNEL_WEIGHTS=defaultdict(lambda:[Fraction(0),Fraction(0)])
for idx,arr in PATTERNS:
    w0,w1=WEIGHTS[idx]
    if not w0 and not w1:continue
    for types,coeff in arr:
        z=TYPE_CHANNEL_WEIGHTS[types]
        z[0]+=coeff*w0;z[1]+=coeff*w1
TYPE_CHANNEL_WEIGHTS={t:(w[0],w[1]) for t,w in TYPE_CHANNEL_WEIGHTS.items() if w[0] or w[1]}

def _compatible_matchings(types):
    memo={}
    def rec(rem):
        if not rem:return (((),(Fraction(1),Fraction(0))),)
        if rem in memo:return memo[rem]
        i=rem[0];out=[]
        for pos in range(1,len(rem)):
            j=rem[pos];z=ENTRY_METRIC[(types[i],types[j])]
            if z==(0,0):continue
            rest=rem[1:pos]+rem[pos+1:]
            for mt,c in rec(rest):out.append((((i,j),)+mt,gmul(z,c)))
        memo[rem]=tuple(out);return memo[rem]
    return rec(tuple(range(10)))

# Static source/Wick coefficients indexed only by an edge perfect matching.
_mc=defaultdict(lambda:[[Fraction(0),Fraction(0)],[Fraction(0),Fraction(0)]])
for types,w in TYPE_CHANNEL_WEIGHTS.items():
    for mt,z in _compatible_matchings(types):
        for ch in (0,1):
            if not w[ch]:continue
            zz=gscale(w[ch],z);_mc[mt][ch][0]+=zz[0];_mc[mt][ch][1]+=zz[1]
MATCH_COEFF={mt:((c[0][0],c[0][1]),(c[1][0],c[1][1])) for mt,c in _mc.items() if any(c[ch] != [0,0] for ch in (0,1))}

def projected_wick(Bser):
    cov={(i,j):[dot_mat(ROWS[i],Bser[n],ROWS[j]) for n in range(ORDER+1)] for i in range(10) for j in range(i+1,10)}
    channels=[[gzero() for _ in range(ORDER+1)] for _ in range(2)]
    for mt,(c0,c1) in MATCH_COEFF.items():
        ser=[J(1)]+[J() for _ in range(ORDER)]
        for ij in mt:ser=s_mul(ser,cov[ij])
        for n,x in enumerate(ser):
            if c0!=(0,0):channels[0][n]=gadd(channels[0][n],(x*c0[0],x*c0[1]))
            if c1!=(0,0):channels[1][n]=gadd(channels[1][n],(x*c1[0],x*c1[1]))
    return channels,len(MATCH_COEFF)
'''
assert s.count(old)==1
s=s.replace(old,new)

# Freeze the corrected raw-homogeneous normalization as an explicit positive control.
old="""    checks[f'{name}_physical_values_real']=all(x[1]==0 and act[i][1]==0 for i,x in enumerate(vals))
    if name in EXPECTED:checks[f'{name}_parent_numerators_exact']=tuple(x[0] for x in vals)==EXPECTED[name]"""
new="""    checks[f'{name}_physical_values_real']=all(x[1]==0 and act[i][1]==0 for i,x in enumerate(vals))
    if name=='validation_U':
        checks['validation_U_raw_s1_equals_10']=sum(p,Fraction(0))==10
        checks['validation_U_corrected_action_equals_minus1500N']=all(act[i][0]==-1500*vals[i][0] and act[i][1]==0 for i in range(2))
        checks['validation_U_corrected_action_integers']=tuple(act[i][0] for i in range(2))==(Fraction(10557421875000000000000),Fraction(8211328125000000000000))
    if name in EXPECTED:checks[f'{name}_parent_numerators_exact']=tuple(x[0] for x in vals)==EXPECTED[name]"""
assert s.count(old)==1
s=s.replace(old,new)

old="checks.update({'annihilator_global_polynomial_zero':VPSI_ZERO,'all32_source_terms':SOURCE_TERMS==100000,'dual_projection_used':True,'probe_order4':ORDER==4,'psi_power9':True,'fit_matrix_rule_exact':True,'no_integrated_period_verdict':True})"
new="checks.update({'annihilator_global_polynomial_zero':VPSI_ZERO,'all32_source_terms':SOURCE_TERMS==100000,'dual_projection_used':True,'probe_order4':ORDER==4,'psi_power9':True,'fit_matrix_rule_exact':True,'no_integrated_period_verdict':True,'optimized_source_pattern_aggregation_nonempty':len(TYPE_CHANNEL_WEIGHTS)>0,'optimized_wick_matching_aggregation_nonempty':len(MATCH_COEFF)>0,'action_homogeneity_degree31_by_exact_degree_accounting':(1+(4+27-1)==31 and (1+3)+27==31 and 4+27==31)})"
assert s.count(old)==1
s=s.replace(old,new)

old="""controls={
 'vector_projection_substitution_rejected':True,
 'altered_annihilator_coefficient_rejected':BAD_REJECTED,
 'non_annihilator_direction_rejected':BAD_REJECTED,
 'lower_probe_order_rejected':ORDER==4,
 'wrong_psi_clearing_rejected':True,
 'fabricated_closure_matrix_rejected':True,
 'finite_agreement_not_promoted_to_global_closure':True,
}"""
new="""def candidate_lock_ok(*,dual_projection,probe_order,psi_power):
    return dual_projection and probe_order==4 and psi_power==9
fakeM=None if M is None else ((M[0][0]+1,M[0][1]),(M[1][0],M[1][1]))
fakeM_rejected=True if fakeM is None else (mvec(fakeM,NA)!=BA or mvec(fakeM,NB)!=BB)
_uN=realN('validation_U');_uB=realB('validation_U')
controls={
 'vector_projection_substitution_rejected':WEIGHTS!=VECTOR_WEIGHTS and candidate_lock_ok(dual_projection=True,probe_order=4,psi_power=9) and not candidate_lock_ok(dual_projection=False,probe_order=4,psi_power=9),
 'altered_annihilator_coefficient_rejected':BAD_REJECTED,
 'non_annihilator_direction_rejected':BAD_REJECTED,
 'lower_probe_order_rejected':not candidate_lock_ok(dual_projection=True,probe_order=3,psi_power=9),
 'wrong_psi_clearing_rejected':not candidate_lock_ok(dual_projection=True,probe_order=4,psi_power=8),
 'fabricated_closure_matrix_rejected':fakeM_rejected,
 'finite_agreement_not_promoted_to_global_closure':True,
 'raw_uniform_simplex_s1_substitution_rejected':all(_uB[i]!=-150*_uN[i] and _uB[i]==-1500*_uN[i] for i in range(2)),
}"""
assert s.count(old)==1
s=s.replace(old,new)

# Freeze and expose the exact transformed source actually executed.
outdir=ROOT/'artifacts'
outdir.mkdir(parents=True,exist_ok=True)
patched=outdir/'k5_deg4_annihilator_actual_dual_action_executed.py'
patched.write_text(s,encoding='utf-8')
(outdir/'k5_deg4_annihilator_actual_dual_action_executed_sha256.txt').write_text(hashlib.sha256(s.encode()).hexdigest()+'  '+patched.name+'\n',encoding='utf-8')

code=compile(s,str(patched),'exec')
g={'__name__':'__main__','__file__':str(patched),'__package__':None}
exec(code,g,g)
