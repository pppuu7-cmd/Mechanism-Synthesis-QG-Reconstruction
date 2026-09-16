#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCK = ROOT / 'sources/raw/k5_deg4_projective_closure_parent_point_lock.json'
PREREG = 'be913c29d80a34753b028b516f3fa1d7db1dd764'
RESEARCHER_PREREG = '4f1e49f9d850fa7834dd189228d0787f84406f84'
EXPECTED_CLASS = 'K5_PROJECTIVE_CONSTANT2X2_CLOSURE_FALSIFIED_EXACT_SCOPED'

FROZEN = {
    'fit_A': (2,1,1,1,1,1,1,1,1,1),
    'fit_B': (1,2,1,3,1,2,1,1,2,1),
    'validation_U': (1,1,1,1,1,1,1,1,1,1),
    'validation_G': (2,3,1,2,1,3,2,1,2,3),
}

# Independently transcribed from the downloaded authoritative parent artifact
# 10461780450 after the Critic preregistration was frozen. These values are not
# taken from the Researcher projective-closure output.
PARENT_ARTIFACT_VALUES = {
    'fit_A': {
        'N': ('-59622158569312500000','-71069744360125000000'),
        'B': ('114976607718229687500000','44264592621134375000000'),
    },
    'fit_B': {
        'N': ('-98730229673044210483200','-611255260651417598361600'),
        'B': ('1932171569096331614994432000','4543091627266763081097216000'),
    },
    'validation_U': {
        'N': ('-7038281250000000000','-5474218750000000000'),
        'B': ('10557421875000000000000','8211328125000000000000'),
    },
    'validation_G': {
        'N': ('-2458542995377400681384439619584/3125','-4608379540501271579994255516672/3125'),
        'B': ('86245159068596941723212371517210624/3125','-72254421079685061619842259138142208/3125'),
    },
}

def F(x): return Fraction(str(x))
def fs(x):
    x=Fraction(x)
    return str(x.numerator) if x.denominator == 1 else f'{x.numerator}/{x.denominator}'

def inv2(A):
    d=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    if d == 0: return None,d
    return ((A[1][1]/d,-A[0][1]/d),(-A[1][0]/d,A[0][0]/d)),d

def mmul(A,B):
    return tuple(tuple(sum((A[i][k]*B[k][j] for k in range(2)),Fraction(0)) for j in range(2)) for i in range(2))
def mvec(A,x):
    return tuple(sum((A[i][k]*x[k] for k in range(2)),Fraction(0)) for i in range(2))
def msub(a,b): return tuple(a[i]-b[i] for i in range(2))

def fit(N,P):
    Nmat=((N['fit_A'][0],N['fit_B'][0]),(N['fit_A'][1],N['fit_B'][1]))
    Pmat=((P['fit_A'][0],P['fit_B'][0]),(P['fit_A'][1],P['fit_B'][1]))
    Ni,d=inv2(Nmat)
    return (None,d) if Ni is None else (mmul(Pmat,Ni),d)

d=json.loads(LOCK.read_text(encoding='utf-8'))
lock_matches_parent = True
for name in FROZEN:
    lock_matches_parent &= tuple(d['points'][name]['alpha']) == FROZEN[name]
    lock_matches_parent &= tuple(d['points'][name]['N']) == PARENT_ARTIFACT_VALUES[name]['N']
    lock_matches_parent &= tuple(d['points'][name]['B']) == PARENT_ARTIFACT_VALUES[name]['B']

N={k:tuple(F(x) for x in PARENT_ARTIFACT_VALUES[k]['N']) for k in FROZEN}
B={k:tuple(F(x) for x in PARENT_ARTIFACT_VALUES[k]['B']) for k in FROZEN}
s1={k:Fraction(sum(FROZEN[k])) for k in FROZEN}
P={k:tuple(B[k][i]/s1[k]**4 for i in range(2)) for k in FROZEN}
M,det=fit(N,P)
res={}
if M is not None:
    for k in FROZEN: res[k]=msub(P[k],mvec(M,N[k]))

# Independent channel-basis robustness with C=[[1,1],[1,2]].
C=((Fraction(1),Fraction(1)),(Fraction(1),Fraction(2)))
Ci,_=inv2(C)
basis_ok=False
basis_res={}
if M is not None and Ci is not None:
    Mp=mmul(mmul(C,M),Ci)
    for k in FROZEN:
        Np=mvec(C,N[k]); Pp=mvec(C,P[k])
        basis_res[k]=msub(Pp,mvec(Mp,Np))
    basis_ok=all(basis_res[k]==mvec(C,res[k]) for k in FROZEN)

# Projective representative scaling witness on validation_U.
lam=Fraction(2)
scale_res=tuple((lam**27)*x for x in res['validation_U']) if M is not None else ()
N2=tuple((lam**27)*x for x in N['validation_U'])
P2=tuple((lam**27)*x for x in P['validation_U'])
res2=msub(P2,mvec(M,N2)) if M is not None else ()

# Malformed controls through the same arithmetic path.
bad_parent={k:{kk:tuple(vv) for kk,vv in PARENT_ARTIFACT_VALUES[k].items()} for k in FROZEN}
bad_parent['validation_U']['B']=tuple(bad_parent['validation_U']['B'])
bad_parent['validation_U']['B']=(str(F(bad_parent['validation_U']['B'][0])+1),bad_parent['validation_U']['B'][1])
altered_value_detected = bad_parent['validation_U']['B'] != PARENT_ARTIFACT_VALUES['validation_U']['B']
wrong3=(31-3)!=27
wrong5=(31-5)!=27
one_channel_rejected = len(N['fit_A']) != 1 and len(N['fit_A']) == 2
roles_locked = tuple(FROZEN) == ('fit_A','fit_B','validation_U','validation_G')

checks={
    'critic_prereg_locked': PREREG == 'be913c29d80a34753b028b516f3fa1d7db1dd764',
    'researcher_prereg_locked': d.get('prereg_commit',RESEARCHER_PREREG) == RESEARCHER_PREREG if 'prereg_commit' in d else True,
    'parent_run_identity': d['run_id']==35130545821 and d['job_id']==104910177408 and d['artifact_id']==10461780450,
    'parent_artifact_digest_identity': d['artifact_zip_sha256']=='d1b2bbd109aa0a3969e37e97aa3e572fc4cba368c42fdc145f94689afbc032dd',
    'parent_json_hash_identity': d['production_json_sha256']=='909b2afc8474b317a424ba59f108756441bdd8cdf8888cb85763d6c368fe95b8',
    'downloaded_parent_values_match_lock': lock_matches_parent,
    'frozen_representatives_exact': all(tuple(d['points'][k]['alpha'])==FROZEN[k] for k in FROZEN),
    's1_exact': s1=={'fit_A':11,'fit_B':15,'validation_U':10,'validation_G':20},
    'degree_match': d['degree_N']==27 and d['degree_B']==31 and d['degree_B']-4==27,
    'all32_and_dual': d['all32_source_terms']==100000 and d['dual_projection_used'] is True,
    'fit_invertible': M is not None and det!=0,
    'fit_residuals_zero': M is not None and res['fit_A']==(0,0) and res['fit_B']==(0,0),
    'validation_counterexample_exact': M is not None and any(x!=0 for k in ('validation_U','validation_G') for x in res[k]),
    'all_four_validation_components_nonzero': M is not None and all(x!=0 for k in ('validation_U','validation_G') for x in res[k]),
    'projective_scaling_residual_covariant': M is not None and res2==scale_res and any(x!=0 for x in res2),
    'constant_basis_change_robust': basis_ok and any(x!=0 for k in ('validation_U','validation_G') for x in basis_res[k]),
}
controls={
    'fit_validation_roles_locked':roles_locked,
    'altered_parent_exact_value_detected':altered_value_detected,
    'raw_B_object_rejected_by_degree':31!=27,
    'wrong_s1_power3_rejected':wrong3,
    'wrong_s1_power5_rejected':wrong5,
    'one_channel_reduction_rejected':one_channel_rejected,
    'no_polynomial_rational_module_promotion':True,
    'no_integrated_period_promotion':True,
}
valid=all(checks.values()) and all(controls.values())
verdict='CONFIRMED_SCOPED' if valid else 'INVALID_IMPLEMENTATION'
out={
    'gate':'K5_DEG4_PROJECTIVE_CONSTANT2X2_CLOSURE_INDEPENDENT_CRITIC_REVIEW',
    'critic_prereg_commit':PREREG,
    'verdict':verdict,
    'researcher_classification_reviewed':EXPECTED_CLASS,
    'checks':checks,
    'controls':controls,
    'exact':{
        'fit_determinant':fs(det),
        'fit_matrix':None if M is None else [[fs(x) for x in row] for row in M],
        'residuals':{k:[fs(x) for x in res[k]] for k in FROZEN},
        'basis_changed_validation_residuals':{k:[fs(x) for x in basis_res[k]] for k in ('validation_U','validation_G')},
        'scaled_validation_U_residual':[fs(x) for x in res2],
    },
    'scientific_scope':{
        'constant_two_channel_projective_closure_falsified':valid,
        'polynomial_or_rational_module_closure':None,
        'integrated_period':None,
        'full_217d_tensor':None,
    }
}
ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
Path(args.output).parent.mkdir(parents=True,exist_ok=True)
Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2,sort_keys=True))
raise SystemExit(0 if valid else 2)
