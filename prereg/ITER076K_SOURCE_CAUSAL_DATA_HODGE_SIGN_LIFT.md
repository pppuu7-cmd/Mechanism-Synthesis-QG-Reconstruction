# Iter076K preregistration — can source causal data fix the global Hodge sign?

Date: 2026-09-13

## Purpose
Iter076J establishes that the gauge-fixed Eq.(4) K5 incidence canonically fixes the **unsigned** complementary-edge support on the six internal K4 wedges. Iter076F/H establish that the signed cut-to-cycle intertwiner is a one-dimensional sign-twisted line, realized canonically by the tetrahedral Hodge complement up to overall sign. Iter076G establishes that source-backed wedge reversal carries the required S4 sign character, while Iter076I shows wedge reversal itself does not create complementary-edge support.

This prospective gate asks the remaining source-provenance question at the discrete level: can the source causal edge data `sigma_a=±1`, together with the gauge-fixed K5 incidence and the established reversal character, select one of the two signed Hodge lifts `+H` or `-H` in a relabeling-covariant way?

No production output exists at preregistration time. Frozen criteria below may not be changed after viewing results.

## Source authority and scope
Use only the source-defined data represented in `sources/CAUSAL_SPINFOAM_VERTEX_2026_SOURCE_SNAPSHOT.md`:
- five source edge labels `a=1,...,5`;
- causal orientations `sigma_a=±1` meaning ingoing/outgoing;
- wedge branch signs `kappa_ab=sigma_a sigma_b`;
- gauge-fixed Eq.(4) K5 incidence and ordered wedge convention `a<b`, `g_b^-1 g_a`.

The source causal `sigma_a` are not to be reinterpreted as a Levi-Civita orientation of the 4-simplex. No label-order convention may be promoted to physical data unless it survives relabeling covariance.

## Frozen objects
For each gauge root `r`, let `U_r` be the four unfixed source nodes and `C_r` the unique unsigned complement support from Iter076J. A signed lift assigns one sign to each complementary pair so that the resulting six-edge operator is an involution and obeys the Iter076F/H twisted covariance law.

## Independent frozen lanes

### Lane A — signed-lift solution space
For a canonical root, enumerate all sign assignments on the three complementary-edge pairs compatible with:
1. `H^2=I`;
2. fixed Iter076J complement support;
3. exact twisted covariance `H R(p)=sgn(p) R(p) H` for all `p in S4`.
PASS iff exactly two solutions exist and they are global opposites `+H` and `-H`.

### Lane B — source-causal pseudoscalar census
Enumerate every assignment of the four unfixed causal variables `sigma_i in {±1}` (and both values of the fixed-root `sigma_r`). Search exhaustively for a nonzero selector `q(sigma) in {±1}` that can be built as a function on the source causal configurations and satisfies the required sign-equivariance
`q(p.sigma)=sgn(p) q(sigma)`
for every `p in S4`.
PASS iff no such selector exists. Record exact obstruction witnesses from odd stabilizers of causal configurations.

### Lane C — wedge-sign (`kappa`) census
Repeat the selector test using only the induced internal wedge signs `kappa_ij=sigma_i sigma_j`, including the global `sigma -> -sigma` redundancy. PASS iff no nonzero sign-equivariant selector exists on the source-induced wedge-sign configurations. This independently tests whether causal branch data can fix the Hodge global sign.

### Lane D — label-order and root-change controls
Construct the obvious label-order Levi-Civita sign as a deliberately extra convention. Verify it can select one Hodge lift for one labelled tetrahedron but flips under odd relabelings; therefore treating raw label order as invariant source physics fails the frozen covariance requirement. Across all five roots, verify the unsigned complement family remains covariant while the signed lift requires an extra orientation choice. Reject an orientation-blind same-sign control.

## Frozen interpretation
If A-D pass, classify:
`ITER076K_SOURCE_K5_INCIDENCE_AND_CAUSAL_SIGMA_FIX_HODGE_LINE_NOT_GLOBAL_SIGN_BLOCKED_ORIENTATION_PSEUDOSCALAR_SCOPED`

Meaning: source Eq.(4) incidence plus causal `sigma/kappa` data determine the complement support and required twist character, but they do not covariantly choose between `+H` and `-H`. A genuine source orientation/pseudoscalar or equivalent contraction-derived sign is still required before physical P3 can be promoted.

If a valid sign-equivariant selector is found from the frozen source causal data, classify:
`ITER076K_SOURCE_CAUSAL_DATA_SELECT_HODGE_SIGN_REVIEW`
and require independent source/manual review before any P3 promotion.

Technical/runtime errors are `INFRASTRUCTURE_OR_NUMERICAL_FAIL`, not scientific FAIL.

## Claim locks
Even a full PASS is a scoped provenance result. It does not establish physical P3, the source numerator/Jacobian, the nominal `epsilon^-1` coefficient, causal-vertex finiteness/divergence, K5, G3/F9/G8, physical sector selection, complete QG, or new physics.
