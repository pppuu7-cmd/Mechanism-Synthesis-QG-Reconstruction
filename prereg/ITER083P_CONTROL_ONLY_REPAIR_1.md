# Iter083P control-only repair 1

Date: 2026-09-15
Status: **PROSPECTIVELY FROZEN BEFORE REPAIR IMPLEMENTATION / REPAIRED PRODUCTION OUTPUT**

Parent scientific preregistration: `prereg/ITER083P_SM_ACTUAL_SOURCE_ORDERED_RESIDUE_OBJECT_DEFINITION.md`, commit `ea29cd3e716d7b35457db493834347a0ca6176a6`.
Critic implementation review: `results/ITER083P_ADVERSARIAL_IMPLEMENTATION_REVIEW.md`, commit `d5641407ce661f6fe125d926880c7f36ef8b7625`.
Controlling `CURRENT.md` head before this repair: `60dcceff9e6b0624670b1770bcc3ddb7389355d5`.

## Repair scope

This is a **control-only implementation repair**. It does not change HYPOTHESIS, exact OBJECT, DEPENDENCY, SOURCE AUTHORITY, FROZEN INPUTS, PASS, FAIL, BLOCKED, INVALID, negative-control meanings, or INTERPRETATION CEILING of the parent Iter083P scientific preregistration.

No substantive Iter083P Researcher verdict is assumed. The historical production `34928916039` remains `INVALID_IMPLEMENTATION` and is quarantined.

## Frozen authority-manifest rule

The repaired validator must mechanically enumerate, hash and report the complete directly relevant repository authority/control corpus present at its production head, at minimum:

- `status/CURRENT.md`;
- `status/MSQGR_ADVERSARIAL_CRITIC_HANDOFF.md`;
- `status/ITER077_CONTACT_FORMULA_ERRATUM.md`;
- parent Iter083P preregistration and this repair preregistration;
- all files under `sources/` whose basename begins with `ITER080K_` or `ITER083E_` through `ITER083N_`;
- all result/review files under `results/` whose basename begins with `ITER080K_` or `ITER083E_` through `ITER083N_`;
- repaired Iter083M / provenance-correct Iter083N authority referenced by `CURRENT.md`;
- the Iter083P Critic implementation review.

The runtime manifest must include path and SHA256 for every included file. Missing required direct locks named by the Critic is `INVALID_IMPLEMENTATION`.

The minimum named direct-lock set is frozen as:

1. `sources/ITER080K_SM_TOLLER_ANALYTICITY_JOINT_K5_SOURCE_MATRIX.md`;
2. `sources/ITER083G_MULTIVARIATE_RENORMALIZATION_Q_SOURCE_LOCK.md`;
3. `sources/ITER083H_SM_PRIMITIVE_SIMPLE_K5_POLE_DERIVATION.md`;
4. `sources/ITER083J_PRODUCT_FACTORIZATION_SOURCE_LOCK.md`;
5. `sources/ITER083K_FOREST_LOCALITY_SOURCE_LOCK.md`;
6. `sources/ITER083L_CAUSAL_TOLLER_SOURCE_AUTHORITY_LOCK.md`;
7. `sources/ITER083N_FINITE_PART_RESIDUE_DEPENDENCE_SOURCE_LOCK.md`.

## Frozen R1-R7 derivation rule

The repaired validator may not initialize R1-R7 to desired booleans. For each requirement it must produce an evidence record containing:

- exact positive-evidence matches, if any, from the enumerated repository authority corpus;
- exact negative/absence-evidence matches from direct source locks where present;
- the full set of searched corpus paths;
- a mechanically derived status `DEFINED`, `ABSENT_OR_ONLY_CONDITIONAL`, or `CONTRADICTORY`.

A requirement is `DEFINED` only if the corpus contains a direct physical/source-authority statement or formula defining that exact full-object ingredient, not merely a conditional mathematical framework, auxiliary regulator, one-wedge theorem, or generic extension theorem.

A requirement is `ABSENT_OR_ONLY_CONDITIONAL` when no direct physical/source-authority positive definition is found and the complete manifest plus exact source-lock evidence records absence/conditional-only status.

A requirement is `CONTRADICTORY` only if direct physical/source authority both defines and forbids the same ingredient in the same scope; this maps to the parent FAIL/INVALID rules as appropriate and may not be manufactured from conditional controls.

The seven requirements remain exactly the parent R1-R7:

- R1 full source meromorphic deformation parameter and object;
- R2 exact source-to-joint-deformation map;
- R3 full all-32 boundary-contracted residue map or exact reduction;
- R4 deformed full-object measure and normalization;
- R5 joint branch/sign plus published spectral-prescription compatibility theorem;
- R6 full K5 Laurent-expansion theorem near the collision;
- R7 unique source identification of `A_-1`.

## Frozen positive fixture

The repaired implementation must include a synthetic in-memory authority fixture that supplies all seven exact full-object ingredients, correct source order, ten wedges, all 32 boundary components, measure/normalization, branch/sign compatibility and a unique residue coefficient.

The fixture must be passed through the **same requirement and candidate validator** used for repository authority. It must return `PASS_OBJECT_DEFINED_SCOPED`. This fixture is a control only and may never enter the scientific corpus or result as authority.

## Frozen malformed-object negative controls

The same candidate/type/order validator must mechanically reject at least these injected malformed candidates:

1. representative-component candidate with fewer than all 32 boundary components and no exact reduction theorem;
2. auxiliary-Q/Hodge/scalar surrogate presented as the physical family;
3. termwise contact-distribution product/pullback order in place of source order;
4. post-hoc finite-part/defining-function/subtraction-scale/regulator candidate lacking source authorization;
5. generic distribution-extension theorem with no exact source-to-full-K5 map;
6. one-wedge spectral epsilon relabelled as a joint K5 meromorphic parameter;
7. Iter083N formal `rho^z u` family relabelled as the actual Toller source family.

Each malformed candidate must be created as data, run through the same validator, and reported with explicit rejection reasons. Literal `True` controls are forbidden.

## Frozen source-order/type locks

The validator must require exactly:

`one-wedge spectral/spinor integration -> Toller function -> product of ten Toller matrices -> full boundary contraction -> K5 group integration / distributional extension`.

It must require all ten wedges, true K5 incidence, all 32 boundary components unless an exact reduction theorem is present, actual source measure/normalization, source branch/sign conventions, and published one-wedge spectral `i epsilon` only in its source-defined scope.

## Verdict taxonomy

Unchanged from parent preregistration:

- `PASS_OBJECT_DEFINED_SCOPED` only if all R1-R7 are `DEFINED` and all execution/manifest/control checks pass;
- `FAIL_EXACT_SCOPED` only for an already-defined full object with an exact source-authority contradiction/internal inconsistency under the parent definition;
- `BLOCKED_OBJECT_DEFINITION` if at least one indispensable R1-R7 ingredient is `ABSENT_OR_ONLY_CONDITIONAL`, with otherwise valid execution and controls;
- `INVALID_IMPLEMENTATION` for incomplete manifest, stale/missing authority, malformed execution, failed positive fixture, unexecuted/ineffective negative controls, or provenance defects.

The workflow must not assert a preselected scientific verdict. It may assert only execution validity, positive-fixture sensitivity, negative-control effectiveness, and that the emitted verdict belongs to the frozen taxonomy.

## Interpretation ceiling / claim locks

Unchanged. No physical residue value/sign/order/cancellation, no finite-part selector, no regulator dependence/independence, no unique K5 extension, no F9/G3 promotion, no downstream QG claim, no `NEW_PHYSICS_FOUND`, and no complete-QG claim may follow from this repair alone.
