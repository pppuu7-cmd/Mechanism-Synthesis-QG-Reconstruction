# Iter079E-SM — KKL gluing inheritance under local causal-vertex replacement

Status: PROSPECTIVELY PREREGISTERED BEFORE IMPLEMENTATION
Date: 2026-09-14

## Question
Can the E5 boundary gluing/duality layer be inherited algebraically from the parent EPRL-KKL spin-foam trace when each parent local vertex factor is replaced by the generalized causal vertex while the boundary state space and parent boundary normalization are kept fixed?

This gate does **not** assume that Beltrán supplied a complete multi-vertex causal state sum. It tests a narrower conditional theorem about the parent KKL gluing algebra.

## Frozen source facts
1. KKL defines the spin-foam trace as a product of internal vertex traces and boundary square-root norm factors, and states the gluing identity for spin-foam traces (arXiv:0909.0939, eqs. 42–44).
2. Beltrán 2026 defines a generalized causal vertex amplitude on the boundary graph of a vertex of an arbitrary 2-complex, i.e. a local vertex replacement on the same generalized EPRL-KKL combinatorial setting (arXiv:2603.22661v2, Secs. 3–4; generalized causal vertex around eq. 26 and causal projection around eq. 36).
3. Beltrán explicitly leaves finiteness of the generalized causal vertex open; therefore E6/noncompact gauge treatment is not promoted by this gate.

## Frozen lanes
### Lane A — parent gluing authority
PASS only if the recorded source contract includes: product over internal vertices, boundary sqrt-norm factors, and the parent gluing identity.

### Lane B — exact locality theorem
Let each internal vertex carry an arbitrary commuting scalar local factor `C_v` depending only on that vertex boundary data. Replace every parent internal vertex trace factor by `C_v` while retaining the parent boundary norm convention. Verify symbolically for a minimal two-foam gluing and for an N-vertex factorized form that the parent multiplicative gluing algebra survives exactly.

PASS criterion: exact polynomial identity, with no fitted coefficients.

### Lane C — negative control
Deform the boundary normalization on one side by an independent non-unit factor `lambda`. Verify that the gluing identity fails generically unless the inherited boundary normalization is matched. This demonstrates that E5 inheritance is conditional on preserving the parent boundary-duality/normalization convention and is not automatic for arbitrary conventions.

### Lane D — scope/provenance lock
PASS only if the conclusion remains conditional and explicitly leaves E3/E4 source inheritance, E6 noncompact gauge fixing, and E7/E8 distributional extension transport unresolved.

## Frozen classifications
If A–D pass:
`ITER079E_SM_E5_KKL_GLUE_DUALITY_CONDITIONALLY_INHERITS_UNDER_LOCAL_CAUSAL_VERTEX_REPLACEMENT_PARENT_BOUNDARY_NORMALIZATION_FIXED_EXACT_SCOPED`

If the algebraic theorem fails:
`ITER079E_SM_E5_KKL_GLUE_INHERITANCE_FAILS_UNDER_FROZEN_LOCAL_REPLACEMENT_EXACT_SCOPED`

If source premises cannot be established:
`ITER079E_SM_E5_GLUE_INHERITANCE_BLOCKED_SOURCE_PREMISE_MISSING`

## Claim locks
- No complete causal multi-vertex theorem.
- No E3/E4 promotion from this gate.
- No E6 gauge-fixing promotion.
- No E7/E8 extension-selector promotion.
- No F9/G3/G8/K5 promotion.
- No NEW_PHYSICS_FOUND.
