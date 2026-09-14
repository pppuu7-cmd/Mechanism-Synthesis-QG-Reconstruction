# Iter082E-SM — K5 nonlinear tubular chart-overlap / extension-class gate

Status: **PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION**
Date: 2026-09-14
Parent authority: Iter082D `ITER082D_SM_K5_NESTED_NORMAL_PROJECTOR_TAYLOR_FOREST_SCHEME_CLASS_CONSTRUCTED_EXACT_SCOPED`.

## Question

Does the local nested K3/K4/K5 Taylor/forest extension *class* constructed in Iter082D survive an explicit nonlinear change of tubular coordinates on the boost-normal neighborhood of the compact collision locus, without selecting any finite part or coefficient?

This is an admissibility / coordinate-covariance gate only. It is **not** a selector equation.

## Frozen charts

Use the Cartan positive-factor normal variable at each node. The compact factor is spectator data and the nonlinear comparison is entirely in the three-dimensional boost vector.

Chart X (rapidity/exponential normal coordinate):

`H_X(x) = exp(x·sigma)` with `r=|x|`.

Chart V (velocity/hyperbolic-sine normal coordinate):

`v = F(x) = (sinh(r)/r) x`, so equivalently

`H_V(v) = sqrt(1+|v|^2) I + v·sigma`.

On the overlap the inverse is

`x = G(v) = (asinh(|v|)/|v|) v`.

The implementation must use exact rational Taylor coefficients through total normal degree 9 (one order above the deepest allowed order 8). No coefficient may be inferred from production output.

The map is applied node-wise with the same frozen formula at all five labels; one overall gauge-fixed/common mode is treated exactly as in the barycentric projector geometry of Iter082D.

## Frozen collision data

All 16 divergent blocks from Iter082B/Iter082D:

- ten K3 blocks, `omega_3=0`;
- five K4 blocks, `omega_4=3`;
- one K5 block, `omega_5=8`.

All 20 maximal chains `K3 subset K4 subset K5` are tested.

## Exact predicates

### P0 — chart validity

1. `F(0)=0`, `G(0)=0`.
2. `DF(0)=DG(0)=I_3`.
3. Exact truncated compositions satisfy `G(F(x))=x+O(|x|^10)` and `F(G(v))=v+O(|v|^10)`.
4. `F` and `G` are SO(3)-equivariant in the formal polynomial sense.

### P1 — label/S5 covariance

The node-wise transition must commute exactly with all 120 label permutations. No preferred label is allowed.

### P2 — collision-stratum preservation

For every divergent block B, the nonlinear node-wise transition must preserve the block diagonal exactly: equal node inputs inside B give equal node outputs inside B.

In barycentric normal variables this is tested prospectively as:

- zero normal input implies zero transformed normal input;
- the linear normal map at the stratum is invertible and equals the Iter082D normal projector action up to the frozen identity tangent map;
- no constant normal term is generated.

### P3 — normal-ideal / jet-filtration preservation

For each B and each required jet order `0..omega_B+1`, the transition and inverse must preserve vanishing order in the normal ideal of B. Equivalently, a polynomial/control monomial invisible through order `omega_B` before the chart change may not generate a visible normal jet of order `<=omega_B` after the chart change.

Frozen bounds are exactly `(omega_3,omega_4,omega_5)=(0,3,8)`.

### P4 — nested-chain filtration

For all 20 maximal chains, transport through the nonlinear chart change must preserve the nested filtration associated with the exact Iter082D increments

`A=P_B3`, `B=P_B4-P_B3`, `C=P_B5-P_B4`.

A higher-order term in a deeper normal ideal may not generate a forbidden lower-order jet for an inner block. The implementation must test both X→V and V→X.

### P5 — extension-class covariance, not representative equality

Let `R_X` denote any symbolic Iter082D admissible local forest representative with all finite coefficients/scales left symbolic. Define the transported V-chart representative by pullback/pushforward through the frozen overlap map, not by refitting.

The gate passes only if the discrepancy between the two chart descriptions is confined to the already-authorized supported-jet class on K3/K4/K5 with orders bounded by `(0,3,8)`. Exact equality of representatives is **not required** and must not be used as a selector.

Operational finite-jet test: the chart-change conjugation of the Taylor visibility maps must induce an automorphism of the quotient by the common invisible ideal through degree 9, with no leakage from invisible classes into forbidden visible orders. All symbolic finite-part coefficients remain symbols.

### P6 — negative controls

The validator must mechanically reject at least these frozen invalid variants:

1. nonzero constant shift `v=F(x)+c` (breaks collision-locus anchoring);
2. label-dependent cubic coefficient at one node (breaks S5 covariance);
3. singular linear normal map (breaks tubular overlap);
4. a transition that maps an invisible order-9 K5 control into an order-8 visible jet (breaks filtration);
5. a rule that sets any finite coefficient/scale numerically (selector smuggling);
6. same-graph reassociation used as an extra selector equation (CDSR T4 violation).

## Frozen classifications

- invalid implementation/provenance → `INVALID_IMPLEMENTATION_OR_PROVENANCE`;
- any P0–P5 failure with valid controls → `K5_NONLINEAR_TUBULAR_CHART_OVERLAP_CLASS_COMPATIBILITY_FAIL_SCOPED`;
- all P0–P6 pass → `K5_NONLINEAR_TUBULAR_CHART_OVERLAP_PRESERVES_ALLOWED_SUPPORTED_JET_CLASS_EXACT_SCOPED`.

The PASS label is deliberately local/scoped. It does not assert a global Toller extension theorem.

## Frozen claim ceiling

Even on PASS, do **not** claim:

- a unique K5 extension or physical finite-part selector;
- exact total ambiguity dimension or sufficiency of 28/16 conditions;
- global chart independence on all of `SL(2,C)^4`;
- regulator independence;
- causal E3/E4/E6 closure;
- G3/F9/G8/K5 promotion;
- `NEW_PHYSICS_FOUND` or complete quantum gravity.

## Production discipline

Preregistration commit must precede implementation commit and production run. Frozen formulas, orders, controls and classification labels above must not be changed after production output is inspected. Any implementation defect is repaired only under a new prospectively recorded control-only repair note; scientific criteria stay frozen.
