# Iter082G-SM — K5 supported-jet Čech descent / patching-admissibility gate

Status: **PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION**
Date: 2026-09-15
Parent authority: Iter082F `K5_THREE_CHART_TUBULAR_ATLAS_FINITE_JET_COCYCLE_CLOSED_EXACT_SCOPED`.

## Question

Given the prospectively frozen three-chart X/V/W tubular atlas and its exact finite-jet transition cocycle through degree 9, do chart-to-chart differences that lie in the already-authorized K3/K4/K5 supported-jet modules admit an exact Čech 0-cochain correction, so that the local representatives can be made overlap-compatible **modulo the same supported-jet extension class**, without fixing any physical finite coefficient or subtraction scale?

This is a finite-dimensional algebraic descent/admissibility gate. It is not yet a theorem about global distributions on `SL(2,C)^4`, not a partition-of-unity convergence theorem, and not a selector.

## Frozen coefficient modules

For each divergent block size `k=3,4,5`, use an abstract supported normal-jet coefficient module

`J_k = span{e_0,...,e_omega_k}`

with frozen orders `(omega_3,omega_4,omega_5)=(0,3,8)`.

For the scoped audit, transition maps on each `J_k` are the exact truncated pullback matrices induced by the three Iter082F radial chart maps through order `omega_k`, derived mechanically from the frozen rational series. No coefficient may be fitted from output.

The full module is the direct sum over the 16 divergent K3/K4/K5 blocks. Block labels transform only under the already-established S5 action; no preferred block or vertex is allowed.

## Frozen Čech data

Use the three-chart nerve with vertices X,V,W and all pairwise/triple overlaps present.

A supported-jet 1-cochain consists of symbolic vectors

- `a_XV` on X∩V,
- `a_VW` on V∩W,
- `a_XW` on X∩W,

for every divergent block.

P0 — transition matrices are invertible through the relevant jet order and satisfy the same triple-overlap cocycle as Iter082F.

P1 — generate a deterministic exact basis of 1-cocycles by assigning symbolic/rational basis data on two overlaps and imposing the transported cocycle equation on the third. No random numerical fitting.

P2 — for every generated 1-cocycle, construct a 0-cochain `(b_X,b_V,b_W)` such that its Čech coboundary equals the input 1-cocycle exactly in every block/module.

P3 — verify reconstruction independently on all three overlaps and on the triple overlap. Residual must be exact zero over `Q`.

P4 — S5 covariance: all 120 permutations transport block labels and the reconstructed descent equations into themselves. No absolute-label choice is permitted in the solver.

P5 — nested K3⊂K4⊂K5 filtration compatibility: the correction acts blockwise within the already-authorized supported-jet modules and never lowers the frozen normal-order filtration.

P6 — non-selector criterion: the solution must retain the expected 0-cochain gauge freedom (adding one globally transported supported-jet vector). The implementation must demonstrate non-uniqueness explicitly and must not set finite coefficients or scales by a numerical convention.

P7 — negative controls must reject at least:

1. an intentionally non-cocyclic overlap datum;
2. a corrupted X→W transition coefficient;
3. a singular transition matrix;
4. an absolute-label-dependent block correction;
5. an order-lowering correction;
6. a solver that fixes the free global supported-jet mode by declaring it physical.

## Frozen classifications

- invalid implementation/provenance → `INVALID_IMPLEMENTATION_OR_PROVENANCE`;
- valid implementation but P0 failure → `K5_SUPPORTED_JET_CECH_DESCENT_BLOCKED_TRANSITION_COCYCLE_SCOPED`;
- P0 passes but some valid 1-cocycle is not a coboundary → `K5_SUPPORTED_JET_CECH_DESCENT_NONTRIVIAL_H1_SCOPED`;
- P0–P7 pass → `K5_SUPPORTED_JET_CECH_DESCENT_EXACTLY_SOLVABLE_WITH_GLOBAL_JET_GAUGE_FREEDOM_SCOPED`.

## Interpretation ceiling

A PASS would show only that, on the explicit three-chart finite-jet atlas and within the already-authorized supported-jet modules, overlap ambiguities have no additional algebraic Čech-H1 obstruction and can be reconciled up to global supported-jet gauge freedom.

It would **not** prove existence of globally patched distributions, continuity/topological completeness of a distribution space, partition-of-unity independence for singular amplitudes, physical finite-part selection, regulator independence, causal closure, G3/F9/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete quantum gravity.

## Downstream rule

Only after a PASS may the next gate address an actual distribution-space partition-of-unity/descent construction. Any such later gate must keep finite coefficients/scales symbolic and must not reinterpret the Čech gauge freedom as a physical selector.