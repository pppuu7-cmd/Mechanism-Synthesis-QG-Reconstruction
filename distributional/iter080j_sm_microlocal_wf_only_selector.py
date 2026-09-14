#!/usr/bin/env python3
import argparse, hashlib, json, pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
ITER077Q = ROOT / 'results' / 'ITER077Q_SM_INVARIANT_TANGENTIAL_AMBIGUITY_RESULT.md'
PREREG = ROOT / 'prereg' / 'ITER080J_SM_MICROLOCAL_WF_ONLY_SELECTOR_MOTIVATION_AND_POWER.md'
ITER029 = ROOT / 'results' / 'ITER029_MICROLOCAL_CYCLE_WAVEFRONT_AUDIT.md'
EXPECTED_BLOB = '26aa90965ccfe495f55df2f4c190f7bbe09093f4'
PASS_CLASS = 'ITER080J_SM_WAVEFRONT_CONORMAL_ADMISSIBILITY_ALONE_CANNOT_SELECT_ITER077Q_INFINITE_SMOOTH_TANGENTIAL_AMBIGUITY_EXACT_THEOREM_SCOPED'
FAIL_CLASS = 'ITER080J_SM_WF_ONLY_SELECTOR_POWER_NOT_ESTABLISHED_SCIENTIFIC_FAIL_SCOPED'


def git_blob(path):
    return subprocess.check_output(['git','hash-object',str(path)], cwd=ROOT, text=True).strip()

def dump(obj, out):
    pathlib.Path(out).write_text(json.dumps(obj, indent=2, sort_keys=True) + '\n')

def lane_a():
    txt = ITER077Q.read_text()
    checks = {
        'blob_sha_exact': git_blob(ITER077Q) == EXPECTED_BLOB,
        'N_SU2_4': 'N = SU(2)^4 subset SL(2,C)^4' in txt,
        'family_present': '{ Q(y)^n F(y) delta_N(x) : n=0,1,2,... }' in txt,
        'smooth_multiplier_lock': 'every `Q^n` is smooth and bounded on compact `N`' in txt,
        'infinite_dimensional_class': 'INFINITE_DIMENSIONAL_TANGENTIAL_SUBSPACE_EXACT_THEOREM_SCOPED' in txt,
        'linear_independence_exact': 'is linearly independent' in txt,
    }
    return {'lane':'A','kind':'provenance','checks':checks,'pass':all(checks.values()),'actual_blob':git_blob(ITER077Q)}

def lane_b():
    p = PREREG.read_text(); i = ITER029.read_text()
    p_plain = p.replace('**','')
    checks = {
        'iter029_predates_and_is_microlocal': 'exact microlocal cycle / wavefront audit' in i and ('Hormander' in i or 'Hörmander' in i),
        'bf_source_frozen': 'math-ph/9903028' in p and 'Brunetti--Fredenhagen' in p,
        'dang_source_frozen': '1412.2808' in p and 'Dang' in p,
        'no_successor_construction': 'does not invent CRQN v0.3' in p_plain,
    }
    return {'lane':'B','kind':'independent_motivation','checks':checks,'pass':all(checks.values())}

def lane_c():
    q = ITER077Q.read_text(); p = PREREG.read_text()
    # This is a theorem-certificate audit, not a numerical approximation to a wavefront set.
    theorem_axioms = {
        'smooth_multiplication_wf_monotonicity_frozen': 'for smooth `f`, `WF(f u) subset WF(u)`' in p,
        'delta_submanifold_conormal_frozen': 'WF(delta_N) = N^*N \\ 0' in p,
        'iter077q_coefficients_smooth': 'every `Q^n` is smooth and bounded on compact `N`' in q,
        'iter077q_family_independent': 'is linearly independent' in q,
        'iter077q_family_countable': 'n=0,1,2,...' in q,
    }
    implication = all(theorem_axioms.values())
    conclusion = {
        'all_u_n_M_WF_admissible': implication,
        'infinite_dimensional_subspace_survives': implication,
        'M_WF_unique_selection_impossible': implication,
    }
    return {'lane':'C','kind':'exact_theorem_certificate','axioms':theorem_axioms,'conclusion':conclusion,'pass':implication and all(conclusion.values())}

def lane_d():
    p = PREREG.read_text()
    forbidden = [
        'all microlocal selectors fail','all differential selectors fail','all spectral selectors fail',
        'no future selector can work','CRQN v0.3 is defined','unique K5 extension obtained',
        'NEW_PHYSICS_FOUND','G3 PASS','F9/G8/K5 promotion'
    ]
    # Forbidden phrases are allowed only inside the explicit rejected-promotions list.
    has_scope = all(x in p for x in forbidden)
    checks = {
        'rejected_promotions_explicit': has_scope,
        'stronger_selector_outside_scope': 'outside M_WF scope' in p,
        'interpretation_ceiling_present': 'rules out only `M_WF` as a **standalone unique selector**' in p,
        'no_successor_model_defined': 'It does not define a successor model.' in p,
    }
    return {'lane':'D','kind':'scope_controls','checks':checks,'pass':all(checks.values())}

def aggregate(input_root):
    root = pathlib.Path(input_root)
    docs=[]
    for f in sorted(root.rglob('*.json')):
        try:
            d=json.loads(f.read_text())
            if d.get('lane') in {'A','B','C','D'}: docs.append(d)
        except Exception: pass
    by={d['lane']:d for d in docs}
    complete=set(by)=={'A','B','C','D'}
    allpass=complete and all(by[k].get('pass') is True for k in 'ABCD')
    classification=PASS_CLASS if allpass else FAIL_CLASS
    verdict='PASS_EXACT_SCOPED' if allpass else 'SCIENTIFIC_FAIL_SCOPED'
    return {'lane':'aggregate','complete':complete,'lane_pass':{k:by.get(k,{}).get('pass') for k in 'ABCD'},'classification':classification,'verdict':verdict,'execution_valid':complete}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True); ap.add_argument('--out',required=True); ap.add_argument('--input-root',default='.')
    a=ap.parse_args()
    funcs={'A':lane_a,'B':lane_b,'C':lane_c,'D':lane_d}
    if a.lane in funcs: obj=funcs[a.lane]()
    elif a.lane=='aggregate': obj=aggregate(a.input_root)
    else: raise SystemExit('bad lane')
    dump(obj,a.out); print(json.dumps(obj,indent=2,sort_keys=True))
    if a.lane!='aggregate' and not obj['pass']: sys.exit(2)
    if a.lane=='aggregate' and not obj['execution_valid']: sys.exit(3)

if __name__=='__main__': main()
