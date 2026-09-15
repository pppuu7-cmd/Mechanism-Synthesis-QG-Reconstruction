# Iter083P provenance ledger

Date: 2026-09-15

## Gate

`ACTUAL_SOURCE_ORDERED_RESIDUE_OBJECT_DEFINITION`

Researcher classification:

`ITER083P_SM_ACTUAL_SOURCE_ORDERED_MEROMORPHIC_RESIDUE_NOT_DEFINED_BY_CURRENT_REPOSITORY_AUTHORITY_SCOPED`

Researcher verdict: `BLOCKED_OBJECT_DEFINITION`.

Independent Critic verdict: **`INVALID_IMPLEMENTATION`**.

Controlling review:

- `results/ITER083P_ADVERSARIAL_IMPLEMENTATION_REVIEW.md`;
- commit `d5641407ce661f6fe125d926880c7f36ef8b7625`.

The Researcher result is therefore quarantined from downstream use pending a control-only repair/retry under the unchanged scientific preregistration.

## Frozen chronology

1. Recovery base `b0eaa4da04b186f9976b7aa1b78fbc15619ca46e`, with Iter083N Critic `CONFIRMED_SCOPED`.
2. Prospective scientific preregistration:
   - `prereg/ITER083P_SM_ACTUAL_SOURCE_ORDERED_RESIDUE_OBJECT_DEFINITION.md`;
   - commit `ea29cd3e716d7b35457db493834347a0ca6176a6`.
3. Validator:
   - `scripts/iter083p_actual_source_residue_object_definition.py`;
   - commit `4c0b3ba799a15fe5bc80cc5243ec262cd03b588d`.
4. Workflow / production head:
   - commit `bab913eabfb73cc42b3d62a1dd81672ceb0208df`.
5. Researcher production:
   - run `34928916039`, terminal success;
   - job `104252818974`, terminal success;
   - artifact `10380702602`;
   - ZIP digest `sha256:cd307c25dc69c776f310a47ea810bcee0683566f61603ed03a6cd1059b9f9fe8`;
   - production JSON SHA256 `f06e6268efbe9dbeaf7881b948103a3cc26553575e14b251e9aaba8e0b70b46d`.
6. Durable raw `f58a55ba79f10520f92f7dc1870f32234738f185`.
7. Researcher result `575c3493fa472ce971e7921d7ede515979563704`.
8. Initial Researcher provenance ledger `13ad4276717985a91033fe247a53097b9259f22d`.
9. Independent Critic implementation review `d5641407ce661f6fe125d926880c7f36ef8b7625`.

Chronology and artifact identity are valid; the defect is scientific implementation, not Actions provenance.

## Controlling implementation defect

The production validator does not determine the seven frozen object-definition requirements from repository authority. It initializes every R1-R7 predicate to literal `False`. The workflow then asserts several of those preassigned values. Therefore terminal-green CI is circular with respect to the `BLOCKED_OBJECT_DEFINITION` classification.

The validator also hashes only seven authority files and omits directly relevant repository source locks/derivations, including `sources/ITER080K_SM_TOLLER_ANALYTICITY_JOINT_K5_SOURCE_MATRIX.md`, `sources/ITER083G_MULTIVARIATE_RENORMALIZATION_Q_SOURCE_LOCK.md`, `sources/ITER083H_SM_PRIMITIVE_SIMPLE_K5_POLE_DERIVATION.md`, `sources/ITER083J_PRODUCT_FACTORIZATION_SOURCE_LOCK.md`, `sources/ITER083K_FOREST_LOCALITY_SOURCE_LOCK.md`, `sources/ITER083L_CAUSAL_TOLLER_SOURCE_AUTHORITY_LOCK.md`, and `sources/ITER083N_FINITE_PART_RESIDUE_DEPENDENCE_SOURCE_LOCK.md`.

Several frozen negative controls are also unconditional or prose-anchor booleans rather than malformed-candidate tests. In particular `representative_component_not_used_for_full_residue=True` is hard-coded.

The preregistration explicitly classifies incomplete corpus coverage and unexecuted negative controls as `INVALID_IMPLEMENTATION`.

## Independent scientific cross-check

The implementation invalidation does not establish that the underlying blocker is false. Independent repository inspection still finds strong support for the qualitative claim:

- Iter080K source matrix: one-wedge analytic uniqueness is explicit, joint simultaneous K5 collision extension is not.
- Iter083L direct source lock: published Eq. (3) one-wedge spectral limit precedes Eq. (4) ten-factor K5 product/group integration; no edgewise collision-analytic parameters, common K5 regulator, joint finite-part map or composition normalization are part of the audited source definition.
- Iter083H primitive simple-pole construction is explicitly conditional/auxiliary and states that it is not a full K5 meromorphic continuation theorem.

Accordingly the likely scientific state remains a missing source-faithful joint residue bridge, but Iter083P production itself is not authoritative evidence for that state until repaired.

## Erratum / quarantine locks

`status/ITER077_CONTACT_FORMULA_ERRATUM.md` remains controlling. Historical source-lock-invalid Iter077E/F siblings remain quarantined. Historical Iter077Q infinite tangential physical application remains invalid under corrected compact-node gauge symmetry.

No historical invalid result is rehabilitated by this review.

## Authority status

`Iter083P-SM` Researcher result is **`INVALID_IMPLEMENTATION`** for downstream purposes. Do not use it to open the bridge-authority gate as if the object-definition audit had been validly executed.

Authorized next work is only a control-only Iter083P repair/retry under the unchanged preregistration. The repaired implementation must mechanically derive R1-R7 from a complete frozen authority manifest, demonstrate a positive fixture that can produce `PASS_OBJECT_DEFINED_SCOPED`, and execute all malformed negative controls through the same validator. If the repaired gate again returns `BLOCKED_OBJECT_DEFINITION` and survives Critic review, then and only then may the source-faithful joint-meromorphic/boundary-value bridge become the authoritative Researcher front.

All claim locks remain unchanged.
