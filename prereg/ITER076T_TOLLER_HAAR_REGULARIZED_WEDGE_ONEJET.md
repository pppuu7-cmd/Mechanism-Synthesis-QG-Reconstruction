# Iter076T preregistration — exact Toller/Haar regularized wedge one-jet

**Date:** 2026-09-13

**Status:** `PREREGISTERED / SOURCE_FAITHFUL_LOCAL_ONEJET_GATE`

**Source snapshot:** `sources/CAUSAL_VERTEX_TOLLER_ONEJET_SOURCE_SNAPSHOT.md`

## Motivation

Iter076Q removes the global Hodge-line sign ambiguity from homogeneous quadratic linear transport. Iter076R/S then show that a symmetry-allowed nonlinear quadratic curvature channel exists and that a generic source one-jet can contaminate the transitive degree-two face layer. Therefore a source-faithful one-jet audit cannot be bypassed by representation theory alone.

The first admissible source question is deliberately local and exact:

> Does an exact causal Toller wedge, after removing its source collision pole with the matching radial Haar factor, already possess a nonzero one-jet in a gamma-simple source sector?

A positive answer proves only the existence of a source-native one-jet witness. It does not prove that the fully contracted or integrated vertex one-jet is nonzero.

## Frozen source specialization

Use the source Eq. (9) gamma-simple reduced Toller formula with

`j=k=l=1/2`, `rho=gamma/2`.

For the extremal magnetic components freeze:

- `t_plus`: `m=+1/2`;
- `t_minus`: `m=-1/2`.

The source snapshot derives the exact closed forms

`t_plus(beta) = - exp(+i rho beta) / [2 (rho^2+1/4) sinh(beta)^2]`,

`t_minus(beta) = - exp(-i rho beta) / [2 (rho^2+1/4) sinh(beta)^2]`.

Define pole-removed functions

`u_+/- (beta) = sinh(beta)^2 t_+/- (beta)`.

The physical discriminator is `rho != 0`. No `gamma=0` conclusion is permitted.

## Lane A — exact symbolic reduction

Independently reconstruct the `j=1/2` extremal source Eq. (9) formula from:

- the exponential exponent;
- Gamma-function recurrence;
- `2F1(2,b;b,z)=(1-z)^(-2)`;
- `1-exp(-2 beta)=2 exp(-beta) sinh(beta)`.

PASS-A iff the two frozen closed forms above are obtained exactly and

`u_plus'(0) = -i rho/[2(rho^2+1/4)]`,

`u_minus'(0) = +i rho/[2(rho^2+1/4)]`.

## Lane B — independent high-precision Toller oracle

Use the already source-backed general Toller oracle `code/toller_general_eprl_reference.py` rather than the symbolic reduction of Lane A.

For `gamma in {0.4,1.2}` and `beta in {0.3,0.8,1.7}` compare:

- oracle `tplus(j=l=k=1/2,m=+1/2)` to the exact closed form;
- oracle `tminus(j=l=k=1/2,m=-1/2)` to the exact closed form.

PASS-B iff all relative residuals are below `1e-35`.

The lane must also verify the exact derivative using the closed form at each `rho=gamma/2`; finite differences may be reported only as a secondary control.

## Lane C — Haar pole cancellation and one-jet survival

Use the Iter076D source-domain radial Haar/KAK factor. Verify exactly:

1. normalized Haar density `(sinh beta/beta)^2` has zero one-jet at `beta=0`;
2. raw radial factor `sinh(beta)^2` cancels the exact extremal Toller `1/sinh(beta)^2` collision pole;
3. the resulting regular source wedge factors have the nonzero derivatives frozen in Lane A whenever `rho!=0`.

PASS-C means Haar evenness does not erase the causal Toller phase one-jet.

## Lane D — universality and full-vertex firewall

PASS-D requires all of the following scope statements to remain true:

- the exact source Eq. (4) acts on generic magnetic/intertwiner boundary data;
- existence of one nonzero magnetic-component wedge one-jet rules out a universal theorem that all local source Toller/Haar one-jets vanish identically;
- this does **not** prove non-cancellation after the ten-wedge product, magnetic sums, five intertwiner contractions, correlated group collision geometry or the four `SL(2,C)` integrations;
- no physical nonlinear source-to-K4 curvature is selected by this gate;
- no degree-two physical coefficient or nominal `epsilon^-1` coefficient is emitted;
- generic finite-spin signed P3 remains blocked;
- no G3/F9/G8/K5 promotion is emitted.

## Frozen terminal classifications

If A-D all pass:

`ITER076T_EXACT_TOLLER_HAAR_REGULARIZED_WEDGE_HAS_NONZERO_ONEJET_WITNESS_FULL_VERTEX_CONTRACTED_ONEJET_STILL_REQUIRED_SCOPED`

If the source oracle contradicts the exact symbolic specialization or the Haar cancellation fails:

`ITER076T_TOLLER_HAAR_ONEJET_SOURCE_SPECIALIZATION_FAIL`

## Next admissible step on PASS

Audit the **contracted source numerator one-jet** rather than repeating local wedge algebra. The next gate must distinguish at least:

1. magnetic-component cancellation;
2. intertwiner contraction;
3. correlated multi-wedge collision geometry;
4. full group integration.

A zero result at one layer may not be silently promoted to the next.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no generic finite-spin signed P3; no physical source-to-K4 nonlinear map; no physical causal-vertex finiteness/divergence theorem; no nominal `epsilon^-1` coefficient; no G3/F9/G8/K5 promotion; retain the published spectral `i epsilon`.
