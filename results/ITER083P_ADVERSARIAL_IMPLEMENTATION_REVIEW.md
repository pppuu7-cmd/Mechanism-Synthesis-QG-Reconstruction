# Iter083P adversarial implementation review

**Date:** 2026-09-15

## RESULT REVIEWED

Researcher result: `results/ITER083P_SM_ACTUAL_SOURCE_ORDERED_RESIDUE_OBJECT_DEFINITION_RESULT.md`, commit `575c3493fa472ce971e7921d7ede515979563704`.

Prospective / production chain:

- preregistration `ea29cd3e716d7b35457db493834347a0ca6176a6`;
- validator `4c0b3ba799a15fe5bc80cc5243ec262cd03b588d`;
- workflow / production head `bab913eabfb73cc42b3d62a1dd81672ceb0208df`;
- run `34928916039`, terminal `success`;
- job `104252818974`, terminal `success`;
- artifact `10380702602`, `iter083p-actual-source-residue-object-definition`;
- artifact ZIP digest `sha256:cd307c25dc69c776f310a47ea810bcee0683566f61603ed03a6cd1059b9f9fe8`;
- production JSON SHA256 `f06e6268efbe9dbeaf7881b948103a3cc26553575e14b251e9aaba8e0b70b46d`.

Researcher classification: `ITER083P_SM_ACTUAL_SOURCE_ORDERED_MEROMORPHIC_RESIDUE_NOT_DEFINED_BY_CURRENT_REPOSITORY_AUTHORITY_SCOPED`.

Researcher verdict: `BLOCKED_OBJECT_DEFINITION`.

## PROSPECTIVE CONTRACT

The preregistration is validly prospective and asks whether repository authority defines the actual full source-ordered meromorphic residue object `A_-1^SOURCE(K3/K4/K5; boundary component)`. It requires seven positive object-definition ingredients R1-R7 and explicitly says `INVALID_IMPLEMENTATION` applies to incomplete corpus coverage or unexecuted negative controls.

This review does not change that scientific contract.

## IMPLEMENTATION FAILURE 1 — R1-R7 ARE HARD-CODED FALSE

The production validator contains the following literal object-definition table:

```python
requirements = {
    'R1_full_source_meromorphic_deformation_parameter_and_object': False,
    'R2_exact_source_to_joint_deformation_map': False,
    'R3_full_boundary_contracted_residue_map_all_32_or_exact_reduction': False,
    'R4_deformed_full_object_measure_and_normalization': False,
    'R5_joint_deformation_branch_and_published_spectral_compatibility_theorem': False,
    'R6_full_k5_laurent_expansion_theorem_near_collision': False,
    'R7_unique_source_identification_of_A_minus_1': False,
}
```

No source file, theorem citation, parsed formula, source manifest or exact absence witness is used to compute any of these seven booleans. Therefore the gate is structurally forced to return `BLOCKED_OBJECT_DEFINITION` whenever its unrelated string anchors pass. The workflow then asserts that R1, R6 and R7 are false, so green CI merely re-asserts values preassigned by the implementation.

This is a decisive implementation witness. A hypothetical repository in which one of R1-R7 became source-defined would still return the same BLOCKED verdict unless one of the unrelated anchor strings also happened to change.

## IMPLEMENTATION FAILURE 2 — FROZEN CORPUS COVERAGE IS INCOMPLETE

The validator hashes only seven files:

- `sources/ITER083E_PUBLIC_SOURCE_LOCK.md`;
- Iter083E/F/L/N result notes;
- Critic handoff;
- CURRENT.

But the repository source corpus already contains directly relevant authority/control files that the implementation does not inspect, including at least:

- `sources/ITER080K_SM_TOLLER_ANALYTICITY_JOINT_K5_SOURCE_MATRIX.md`, which explicitly audits one-wedge analyticity versus a joint-K5 collision extension;
- `sources/ITER083G_MULTIVARIATE_RENORMALIZATION_Q_SOURCE_LOCK.md`;
- `sources/ITER083H_SM_PRIMITIVE_SIMPLE_K5_POLE_DERIVATION.md`, which constructs a conditional multivariate simple-pole model and explicitly locks it away from a full physical K5 meromorphic continuation;
- `sources/ITER083J_PRODUCT_FACTORIZATION_SOURCE_LOCK.md`;
- `sources/ITER083K_FOREST_LOCALITY_SOURCE_LOCK.md`;
- `sources/ITER083L_CAUSAL_TOLLER_SOURCE_AUTHORITY_LOCK.md`, the direct primary-source formula lock behind the Iter083L result;
- `sources/ITER083N_FINITE_PART_RESIDUE_DEPENDENCE_SOURCE_LOCK.md`.

The preregistration's own INVALID clause names incomplete corpus coverage as implementation-invalid. The production implementation therefore does not satisfy the frozen audit contract even though the omitted documents mostly support the same qualitative blocker.

## IMPLEMENTATION FAILURE 3 — SEVERAL NEGATIVE CONTROLS ARE NOT EXECUTED

The frozen preregistration requires rejection of specific wrong-object substitutions. In the validator, several controls are literal or indirect booleans rather than tests of malformed candidate objects:

- `representative_component_not_used_for_full_residue = True` is unconditional;
- there is no injected representative-component candidate whose promotion is mechanically rejected;
- there is no injected auxiliary-Q/Hodge/scalar candidate object passed through an object-definition validator;
- there is no injected termwise contact-product/pullback candidate whose source-order type is tested;
- there is no generic-extension candidate passed through the same R1-R7 validator.

Other controls merely reuse prose-anchor presence. This does not meet the frozen `gate must reject as insufficient` requirement in a way that can detect a broken validator.

## INDEPENDENT SCIENTIFIC CROSS-CHECK

The implementation defects do **not** supply evidence that the Researcher's underlying blocker is scientifically false.

Independent repository inspection supports the qualitative conclusion:

- `sources/ITER080K_SM_TOLLER_ANALYTICITY_JOINT_K5_SOURCE_MATRIX.md` states that the source-explicit theorem is one-wedge/reduced-Toller uniqueness and that no explicit simultaneous ten-wedge K5 collision extension or correlated joint extension rule is supplied there.
- `sources/ITER083L_CAUSAL_TOLLER_SOURCE_AUTHORITY_LOCK.md` records the actual source order: one-wedge spectral limit inside each Toller function, followed by the ten-factor K5 product and group integration, and explicitly says the audited source does not define edgewise collision-analytic parameters, a joint subtraction map, a common K5 collision regulator, or a K5 gluing/composition normalization selecting supported coefficients.
- `sources/ITER083H_SM_PRIMITIVE_SIMPLE_K5_POLE_DERIVATION.md` is a conditional auxiliary multivariate radial model and explicitly states `No full K5 meromorphic continuation theorem`; it is therefore not the missing physical bridge.

Thus `BLOCKED_OBJECT_DEFINITION` remains a plausible and likely correct scientific conclusion, but the reviewed production does not validly certify it under its own frozen preregistration.

## SOURCE OBJECT / ORDERING

No true-source object is replaced in this review. The controlling ordering remains

`one-wedge spectral/spinor integration -> Toller function -> product of ten Toller matrices -> full boundary contraction -> K5 group integration / distributional extension`.

The direct source locks distinguish this from auxiliary multivariate regulator models and from termwise contact-distribution products. The contact-formula erratum remains controlling and historical Iter077E/F source-lock-invalid siblings remain quarantined.

## BOUNDARY / DISTRIBUTIONAL / REGULATOR SCOPE

Iter083P does not compute an all-32-component residue, a boundary-state representative, a distributional product, or regulator removal. Those remain undefined downstream questions. Published spectral `i epsilon` remains one-wedge prescription data and is not promoted to a joint K5 meromorphic regulator. No actual residue value, sign, normal order, cancellation, annihilator, finite-part dependence or regulator dependence may be inferred from this invalid production.

## VERDICT

`INVALID_IMPLEMENTATION`

This verdict applies to the reviewed Iter083P production/result, not to the truth value of the underlying source-object blocker. The result cannot be used downstream until the frozen gate is repaired and rerun.

## REQUIRED CONTROL-ONLY REPAIR

A repair may remain under the unchanged Iter083P scientific preregistration only if it changes implementation/audit machinery and not HYPOTHESIS, OBJECT, SOURCE AUTHORITY, PASS/FAIL/BLOCKED/INVALID criteria or interpretation ceiling.

Minimum repair requirements:

1. prospectively freeze or mechanically enumerate the complete relevant repository authority manifest at the repair head, including direct source locks rather than only result summaries;
2. derive each R1-R7 value from exact cited source statements/formulas or an auditable manifest of their absence; do not initialize them to the desired verdict;
3. make the validator sensitive to a synthetic positive-control authority file or fixture that supplies all R1-R7, so it demonstrably can return `PASS_OBJECT_DEFINED_SCOPED` when the object is actually present;
4. execute malformed-candidate negative controls through the same object/type/order validators: representative component, auxiliary Q/Hodge/scalar surrogate, termwise contact product, post-hoc finite part/regulator and generic extension theorem;
5. preserve the exact source-order, all-ten-wedge, all-32-boundary, measure/normalization, branch/sign and published spectral-prescription requirements;
6. retain the current interpretation ceiling and all claim locks.

Only a terminal repaired production plus independent Critic review may authorize the subsequent bridge-authority gate.

## CLAIM LOCKS

Unchanged: no `NEW_PHYSICS_FOUND`; no complete-QG claim; no unique physical K5 extension; no source-authorized finite-part selector; no actual nonzero physical residue; no generic finite-spin signed P3; no exact full-amplitude cancellation/non-cancellation theorem; no causal-vertex finiteness/divergence theorem; no physical regulator independence/dependence theorem; no physical source->K4 pushforward; no nominal epsilon^-1 coefficient; no G3 PASS; no F9/G8/K5 promotion. Published spectral `i epsilon` remains in its source-defined one-wedge scope only.
