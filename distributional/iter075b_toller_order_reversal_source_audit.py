import json
from pathlib import Path

EVIDENCE = {
    "source_toller_2026": {
        "arxiv": "2604.24945",
        "facts": {
            "T_not_representation": True,
            "eq14_noncomposition_explicit": True,
            "eq15_additive_Tplus_Tminus_equals_D": True,
            "wigner_D_inverse_identity_explicit": True,
            "explicit_full_group_branchwise_T_inversion_found": False,
            "explicit_branch_map_under_g_inverse_found": False,
            "explicit_phase_index_label_map_under_g_inverse_found": False,
        },
    },
    "source_causal_vertex_2026": {
        "arxiv": "2601.23162",
        "facts": {
            "wedge_argument_gb_inverse_ga_explicit": True,
            "branch_selected_by_kappa_sigma_a_sigma_b": True,
            "global_edge_reversal_leaves_kappa_unchanged": True,
            "feynman_iepsilon_definition_explicit": True,
            "explicit_wedge_order_reversal_T_branch_law_found": False,
        },
    },
}

invalid_inference_rejected = (
    EVIDENCE["source_toller_2026"]["facts"]["T_not_representation"]
    and EVIDENCE["source_toller_2026"]["facts"]["wigner_D_inverse_identity_explicit"]
)

requirements = {
    "branch_map": EVIDENCE["source_toller_2026"]["facts"]["explicit_branch_map_under_g_inverse_found"],
    "phase_index_label_map": EVIDENCE["source_toller_2026"]["facts"]["explicit_phase_index_label_map_under_g_inverse_found"],
    "full_group_T_inverse": EVIDENCE["source_toller_2026"]["facts"]["explicit_full_group_branchwise_T_inversion_found"],
    "wedge_order_reversal": EVIDENCE["source_causal_vertex_2026"]["facts"]["explicit_wedge_order_reversal_T_branch_law_found"],
}

if not invalid_inference_rejected:
    classification = "ITER075B_SOURCE_AUDIT_INVALID"
elif all(requirements.values()):
    classification = "ITER075B_TOLLER_ORDER_REVERSAL_SOURCE_LAW_QUALIFIED_SCOPED"
else:
    classification = "ITER075B_TOLLER_ORDER_REVERSAL_BLOCKED_SOURCE_LAW_NOT_ESTABLISHED"

out = {
    "iteration": "Iter075B",
    "classification": classification,
    "evidence": EVIDENCE,
    "requirements": requirements,
    "negative_control_invalid_unitary_inference_rejected": invalid_inference_rejected,
    "scientific_summary": (
        "The audited 2026 sources explicitly establish that Toller branches are not representations, "
        "give T+ + T- = D, the Wigner-D inverse law, the causal-vertex wedge argument gb^-1 ga, and "
        "the kappa=sigma_a sigma_b branch selector. The frozen audit does not find an explicit full-group "
        "branchwise Toller inversion / wedge-order-reversal law fixing branch, indices, conjugation, labels, "
        "and phases. Therefore tournament/sign geometry cannot yet be promoted through edge reversal."
    ),
    "claim_lock": (
        "No physical causal-sector selection, no K5/G3/F9/G8 promotion, no causal-vertex finiteness/divergence theorem, "
        "no representation-law substitution for Toller functions, no complete-QG or new-physics claim."
    ),
}

Path("out").mkdir(exist_ok=True)
Path("out/iter075b-source-audit.json").write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(out, indent=2, sort_keys=True))
if classification == "ITER075B_SOURCE_AUDIT_INVALID":
    raise SystemExit(2)
