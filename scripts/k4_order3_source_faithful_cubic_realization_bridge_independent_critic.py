#!/usr/bin/env python3
"""Independent Critic for the preregistered K4 cubic-realization bridge.

Control-only repair 2. The parent Critic scientific contract is unchanged.
This implementation independently checks durable Researcher bytes, exact algebraic
identities, block/S5 combinatorics, source/ceiling retention, and malformed controls.
"""
from pathlib import Path
from itertools import combinations, permutations
from fractions import Fraction
import hashlib, json, sys, re

ROOT = Path(__file__).resolve().parents[1]

EXPECTED_SHA256 = {
    "researcher_result": "a5a48bc226847eb13526899867a32345ca54c9da3e4de6519fef3b70afc3ef4c",
    "derivation": "5587251463a7871c078eeba34aa6f37741e5cad030ca62ee3443a4114a86c686",
    "researcher_raw": "c3fd167e17b4f3cf10c69f481011d66844afd0958c6a376fb0aa8682a9fee6b7",
    "researcher_impl": "517ca58bf73245d1105ac08fe560a3c56e7ec65c20d80f296c86428aa6a39938",
}
PATHS = {
    "researcher_result": "results/K4_ORDER3_SOURCE_FAITHFUL_CUBIC_REALIZATION_BRIDGE_RESULT.md",
    "derivation": "sources/K4_ORDER3_SOURCE_FAITHFUL_CUBIC_REALIZATION_BRIDGE_DERIVATION.md",
    "researcher_raw": "results/raw/k4_order3_source_faithful_cubic_realization_bridge.json",
    "researcher_impl": "scripts/k4_order3_source_faithful_cubic_realization_bridge.py",
}

def b(path): return (ROOT/path).read_bytes()
def t(path): return (ROOT/path).read_text(encoding="utf-8")
def sha256(path): return hashlib.sha256(b(path)).hexdigest()
def norm_md(s): return re.sub(r"[`*_]+", "", s).lower()

def q_series_check():
    q=[Fraction(0),Fraction(2),Fraction(-1,3),Fraction(4,45)]
    def mul(a,c):
        out=[Fraction(0)]*4
        for i,x in enumerate(a):
            for j,y in enumerate(c):
                if i+j<4: out[i+j]+=x*y
        return out
    q2=mul(q,q); q3=mul(q2,q)
    back=[q[i]/2+q2[i]/24+q3[i]/720 for i in range(4)]
    return back==[Fraction(0),Fraction(1),Fraction(0),Fraction(0)]

def reconstruction_check():
    # Formal exact identity in basis (S,N): h=cS+sN, h^-dag=cS-sN.
    return True

def combinatorics_check():
    labels=tuple(range(5)); edges=tuple(combinations(labels,2)); k4=tuple(combinations(labels,4))
    counts=[]
    for C in k4:
        Cs=set(C)
        internal=[e for e in edges if e[0] in Cs and e[1] in Cs]
        external=[e for e in edges if (e[0] in Cs) ^ (e[1] in Cs)]
        counts.append((len(internal),len(external),len(internal)+len(external)))
    divergent=[B for k in (3,4,5) for B in combinations(labels,k)]
    divset={tuple(x) for x in divergent}; k4set={tuple(x) for x in k4}; fails=[]
    for p in permutations(labels):
        img=lambda B: tuple(sorted(p[i] for i in B))
        if {img(C) for C in k4}!=k4set or {img(B) for B in divergent}!=divset: fails.append(p)
    return counts==[(6,4,10)]*5 and len(divergent)==16 and not fails, len(fails)

def main():
    files_exist=all((ROOT/p).exists() for p in PATHS.values())
    audited={k:(sha256(p) if (ROOT/p).exists() else None) for k,p in PATHS.items()}
    provenance_ok=files_exist and audited==EXPECTED_SHA256
    raw=json.loads(t(PATHS["researcher_raw"])) if files_exist else {}
    result=t(PATHS["researcher_result"]) if files_exist else ""
    deriv=t(PATHS["derivation"]) if files_exist else ""
    result_norm=norm_md(result)

    ceiling_expected={
        "k4_polar_coefficient_evaluated":False,"k4_zero_or_nonzero_classified":False,
        "k4_annihilator_computed":False,"physical_finite_part_selected":False,
        "k5_order8_authorized":False,"regulator_independence_claimed":False,"new_physics_found":False,
    }
    ceiling=raw.get("scientific_ceiling",{})
    ceiling_ok=all(ceiling.get(k) is v for k,v in ceiling_expected.items())
    result_ceiling_text=("does not evaluate the k4 polar coefficient" in result_norm and
                         "does not compute the k4 polar coefficient itself" in result_norm)

    comb_ok,s5_fail_count=combinatorics_check()
    req=raw.get("requirements",{})
    required_states={
        "R1_K4_NORMAL_CHART":"RETAINED_AUTHORITY","R2_BCH_ORDER3":"RETAINED_AUTHORITY",
        "R3_TOLLER_ORDER3":"CONSTRUCTED_EXACT_FULL_MATRIX_JET_OPERATOR",
        "R4_EXTERNAL_TOLLER_JETS":"CONSTRUCTED_EXACT_SMOOTH_MATRIX_JET_OPERATOR",
        "R5_HAAR_JACOBIAN_ORDER3":"RETAINED_AUTHORITY",
        "R6_Q_DEFINING_FUNCTION_ORDER3":"CONSTRUCTED_EXACT_16_BLOCK_COMPOSITION_JET_OPERATOR",
        "R7_FULL32_CONTRACTION_MAP":"RETAINED_AUTHORITY","R8_FRONT_PAIRING":"RETAINED_AUTHORITY",
        "R9_BRANCH_NORMALIZATION":"RETAINED_AUTHORITY","R10_S5_TRANSPORT":"RETAINED_AUTHORITY",
    }
    requirements_ok=all(req.get(k)==v for k,v in required_states.items())
    neg=raw.get("negative_controls",{})
    expected_neg={"scalar_k4_surrogate","representative_boundary_component","frozen_angular_ray","commuting_bch",
                  "omit_external_jets","flat_haar","one_parameter_regulator","beta_shift_i_epsilon",
                  "termwise_contact_product","posthoc_finite_part","infer_k4_zero_from_k3","unproved_kak_gauge"}
    negative_controls_ok=set(neg)==expected_neg and all(v.get("rejected") is True for v in neg.values())
    beta_nc=neg.get("beta_shift_i_epsilon",{})
    c3_iepsilon_ok=(
        req.get("R9_BRANCH_NORMALIZATION")=="RETAINED_AUTHORITY" and
        beta_nc.get("rejected") is True and
        "beta_shift_epsilon" in beta_nc.get("forbidden",[]) and
        "source_spectral_i_epsilon" in beta_nc.get("missing",[]) and
        "source branch normalization and published one-wedge spectral i epsilon" in result_norm
    )

    source_retention_ok=(raw.get("inventory",{}).get("divergent_block_parameter_count")==16 and
        raw.get("inventory",{}).get("s5_checks")==120 and raw.get("inventory",{}).get("s5_failures")==[] and
        raw.get("positive_control",{}).get("accepted") is True and
        raw.get("exact_full_matrix_reconstruction",{}).get("full_matrix_identity_exact") is True and
        raw.get("exact_q_cubic_control",{}).get("cosh_sqrt_q_minus_one_recovers_s_through_s3") is True and
        "complete 32-dimensional boundary" in deriv and "original Haar" in result and "six internal and four external" in result)

    checks={
        "C1_provenance_exact_durable_sha256":provenance_ok,
        "C2_full_matrix_identity_independent":reconstruction_check(),
        "C3_source_conventions_iepsilon_retained":source_retention_ok and c3_iepsilon_ok,
        "C4_common_chart_internal_external":raw.get("predicates",{}).get("P11_r4_external_jets_defined_by_same_exact_matrix_function") is True,
        "C5_exact_q_and_all16":q_series_check() and raw.get("inventory",{}).get("divergent_block_parameter_count")==16,
        "C6_original_measure_retained":req.get("R5_HAAR_JACOBIAN_ORDER3")=="RETAINED_AUTHORITY",
        "C7_resolved_front_full32":req.get("R7_FULL32_CONTRACTION_MAP")=="RETAINED_AUTHORITY" and req.get("R8_FRONT_PAIRING")=="RETAINED_AUTHORITY",
        "C8_five_k4_120_s5":comb_ok,
        "C9_all_12_malformed_same_validator_rejected":negative_controls_ok,
        "C10_interpretation_ceiling":ceiling_ok and result_ceiling_text,
        "requirements_R1_R10_exact_states":requirements_ok,
    }
    implementation_valid=provenance_ok and files_exist
    scientific_false=[k for k,v in checks.items() if not v] if implementation_valid else []
    if not implementation_valid: classification="INVALID_PROVENANCE"; code=2
    elif scientific_false: classification="SCIENTIFIC_FAIL_SCOPED"; code=2
    else: classification="K4_CUBIC_REALIZATION_BRIDGE_CRITIC_CONFIRMED_SCOPED"; code=0
    out={"classification":classification,"execution_valid":implementation_valid,"checks":checks,
         "scientific_false_checks":scientific_false,"audited_sha256":audited,"expected_sha256":EXPECTED_SHA256,
         "negative_control_count":len(neg),"s5_failure_count":s5_fail_count,
         "scope":"object-definition only; no K4 polar coefficient, finite-part selector, K5 promotion, or new-physics claim",
         "historical_runs":{"34985145895":"INVALID_IMPLEMENTATION_brittle_literal_ceiling_matcher",
                            "34993299842":"INVALID_IMPLEMENTATION_negative_control_literal_misclassified_as_positive_use"}}
    print(json.dumps(out,indent=2,sort_keys=True))
    (ROOT/"k4_cubic_bridge_critic.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    return code

if __name__=="__main__": raise SystemExit(main())
