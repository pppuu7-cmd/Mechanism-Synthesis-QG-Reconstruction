# Iter079K-SM — E6 parent gauge-fixing inheritance source-audit result

## Authoritative provenance

- Prospective preregistration: `fa6ed0fff963e5db2e6dfba4846b9cc9f10361bd`
- Frozen primary-source matrix: `9c286ec5971f9eb90bce00390cff7d603343f2e2`
- Implementation: `2b8e2cd4cb9144359d1100c2433585470ca11d6c`
- Workflow / production head: `227475923fbb2f3b9d5fc25e5515fe01f785b9b6`
- Run: `34816195887`
- Lane artifacts: A `10336945329`, B `10336571070`, C `10336254710`, D `10336460796`
- Aggregate artifact: `10335744094`
- Aggregate digest: `sha256:096481370c671e1b07b1b5856947116608364f54d5c66f4b585af1da07df2bc0`
- Aggregate job: `103887307649`

## Frozen classification

`ITER079K_SM_PARENT_E6_GAUGE_FIXING_PRESCRIPTION_EXISTS_BUT_CAUSAL_INHERITANCE_BRIDGE_MISSING_SOURCE_BLOCKED_EXACT_SCOPED`

Verdict: `BLOCKED_SOURCE_BRIDGE`.

All four frozen lanes and the aggregate completed successfully. This is a scientific/source-definition blocker, not an infrastructure or numerical failure.

## Primary-source findings

### A — parent Lorentzian EPRL gauge treatment: COMPLETE

Engle–Pereira, arXiv:0805.4696v2, explicitly identifies the redundant `SL(2,C)` volume in the Lorentzian vertex. Section 3 states that the last of the five group integrations contributes the infinite volume of `SL(2,C)` and defines the regularized vertex by dropping that redundant integral; the result is stated to be independent of which one of the five integrations is dropped.

Appendix C supplies the gauge-fixing interpretation in the full triangulation. After the simplicity constraints reduce the tetrahedral gauge symmetry, the remaining vertex gauge freedom permits exactly one `V_tv` per 4-simplex to be fixed to the identity. The paper explicitly states that this is equivalent to the regularization used in the vertex amplitude.

Thus the parent model supplies a definite local prescription: one redundant Lorentz-group integration per 4-simplex is removed / equivalently one local group variable is fixed to identity, rather than leaving an unspecified division by an infinite group volume.

### B — parent full-triangulation compatibility: COMPLETE

The same Appendix C derives the prescription inside the full-triangulation partition function, where the local group integrations are absorbed into the product of vertex amplitudes. Therefore the local removal/fixing is not merely a one-vertex toy convention; it is part of the parent full-triangulation construction used by the frozen source audit.

This is the maximum parent-side statement authorized here. It is not a theorem about arbitrary later modifications of the local vertex factor.

### C — causal/Toller inheritance: PARTIAL ONLY

Bianchi–Chen–Gamonal, arXiv:2601.23162, Eq. (4), defines the causal vertex with the same local group-variable pattern and explicitly gauge-fixes the vertex `SL(2,C)` invariance to `g_1 = 1` by introducing `delta(g_1)`, citing the parent Lorentzian gauge-fixing authority.

So the one-vertex causal construction does **not** leave the local gauge fixing unspecified.

However, the same paper states in its discussion that it focused on the amplitude of a **single vertex**, which is a building block for a future/many-vertex spinfoam path integral. It does not derive a complete causal multi-vertex state sum with a theorem that the parent per-vertex quotient/fixing normalization is inherited unchanged under KKL gluing for all vertices.

Therefore the frozen causal many-vertex inheritance criterion is not met.

### D — controls and claim locks: VALID

Iter079F/I/J remain consistent with the source audit:

- the common-left redundancy is present at a causal vertex;
- the frozen vertex-only gluing control carries a product `G^V` redundancy;
- gauge invariance alone does not select an arbitrary normalization;
- no FP factor, arbitrary Haar rescaling, group-volume division, preferred vertex, or post-hoc extension selector was introduced.

## Scientific consequence

Iter079I's broad statement that the E6 quotient/fixing object is simply absent must now be **narrowed**.

What is source-explicit:

1. the parent Lorentzian EPRL local prescription removing one redundant `SL(2,C)` integration per 4-simplex;
2. its full-triangulation parent interpretation;
3. the same one-vertex gauge choice `g_1=1` in the causal/Toller vertex.

What remains missing is the **multi-vertex causal inheritance bridge**: a primary-source derivation that the parent quotient/fixing normalization composes unchanged with the causal vertex replacement over a general causal foam.

Hence E6 is not `BLOCKED_OBJECT_DEFINITION` at the single-vertex level. The remaining physical blocker is narrower:

`CAUSAL_MULTIVERTEX_E6_PARENT_GAUGE_FIXING_NORMALIZATION_INHERITANCE_BRIDGE`.

## Scope ceiling

This result does not establish a full causal multi-vertex amplitude, K5 extension uniqueness, E7/E8 transport, finiteness/convergence, regulator independence, G3, F9/G8, RG, `NEW_PHYSICS_FOUND`, or a complete quantum-gravity theory. The published one-wedge spectral `i epsilon` remains distinct from any hypothetical joint K5 regulator.
