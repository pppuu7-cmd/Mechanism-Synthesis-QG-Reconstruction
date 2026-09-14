# Iter079K-SM — E6 parent gauge-fixing inheritance source audit (prospective preregistration)

## Status
Prospectively frozen before source extraction, implementation, production, or result inspection.

## Scientific question
Does the primary Lorentzian EPRL/KKL parent construction provide an explicit per-vertex `SL(2,C)` quotient/gauge-fixing prescription (including the integration removed/fixed, measure/normalization convention, and gluing compatibility), and does the primary generalized causal/Toller construction explicitly authorize inheriting that prescription when the local EPRL vertex factor is replaced by the causal/Toller vertex?

## Frozen source authority
Primary papers only for the scientific classification. Repository notes may be used only for provenance and consistency checks, never to manufacture a missing source statement.

## Frozen lanes

### A — parent Lorentzian EPRL/KKL local gauge treatment
Extract exact source-backed statements for all of:
1. existence of the common-left `SL(2,C)` redundancy of vertex group variables;
2. explicit rule for removing/fixing/dividing the redundant integration at a vertex;
3. explicit measure or normalization convention after that removal/fixing.

A is `COMPLETE` only if items 1–3 are source-explicit. A statement merely saying that one group integration can be omitted, without defining the resulting normalization convention sufficiently to fix an amplitude, is not enough for item 3.

### B — parent gluing compatibility
Test whether the same primary parent authority explicitly makes the local quotient/fixing prescription compatible with the KKL gluing/composition normalization used for multi-vertex foams. Algebraic plausibility is insufficient; this lane is source-audit, not a fitted reconstruction.

### C — causal inheritance bridge
Test whether the primary generalized causal/Toller authority explicitly states or derives that the parent EPRL/KKL quotient/fixing measure and normalization remain unchanged under the causal local-vertex replacement. Similarity of the integrand, the same group variables, or preservation of the common-left redundancy is not enough by itself.

### D — exact consistency / negative controls
Recheck against the already closed Iter079F/I/J facts:
- common-left redundancy exists conditionally at one vertex;
- the vertex-only gluing control carries `G^V`;
- gauge invariance alone does not fix normalization.
No arbitrary group-volume division, Faddeev-Popov factor, Haar normalization rescaling, preferred vertex, or post-hoc selector may be introduced.

## Frozen classifications

1. `ITER079K_SM_E6_PARENT_QUOTIENT_FIXING_AND_NORMALIZATION_EXPLICIT_AND_CAUSAL_INHERITANCE_SOURCE_EXPLICIT_EXACT_SCOPED`
   only if A, B, and C are all source-explicit and D is valid.

2. `ITER079K_SM_PARENT_E6_GAUGE_FIXING_PRESCRIPTION_EXISTS_BUT_CAUSAL_INHERITANCE_BRIDGE_MISSING_SOURCE_BLOCKED_EXACT_SCOPED`
   if parent A+B are explicit but C is absent/insufficient.

3. `ITER079K_SM_PARENT_E6_QUOTIENT_NORMALIZATION_NOT_FULLY_DEFINED_IN_PRIMARY_SOURCE_BLOCKED_OBJECT_DEFINITION_EXACT_SCOPED`
   if the parent source itself does not fully supply the frozen A/B object.

4. `ITER079K_SM_E6_SOURCE_PRESCRIPTIONS_INCONSISTENT_INVALID`
   if primary authorities explicitly conflict under the frozen inheritance hypothesis.

5. `ITER079K_SM_INVALID_PROVENANCE_OR_CONTROL`
   for missing/incorrect source provenance, failed D controls, or implementation/infrastructure invalidity.

## Scope ceiling
A PASS may establish only a source-backed/conditional E6 inheritance statement. It cannot establish K5 extension uniqueness, E7/E8 extension transport, convergence/finiteness, regulator independence, G3, F9/G8, RG, `NEW_PHYSICS_FOUND`, or a complete quantum-gravity theory.

Frozen criteria must not be changed after source/result inspection.
