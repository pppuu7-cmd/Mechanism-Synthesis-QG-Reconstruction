# Iter077I-SM preregistration — source-ordered j=1/2 Toller-function K5 full-32 local L1 gate

**Date:** 2026-09-14  
**Status:** prospective / frozen before implementation

## Source/object lock

Controlling source/derived supplement:
`sources/ITER077I_SM_SOURCE_ORDERED_TOLLER_FUNCTION_K5_L1_DERIVATION.md`, commit `f7f0a957e7a0379be39f164bd6903a6e78425f95`.

This gate tests the source ordering

`one-wedge spectral/spinor construction -> Toller function -> K5 product -> group integration`.

It does **not** multiply the ten spinor-contact distributions termwise.

Frozen sector:

- all ten boundary spins `j_ab=1/2`;
- gamma-simple `rho=gamma/2`, finite real gamma;
- five four-valent boundary intertwiners, each in recoupling channel `k=0` or `k=1`;
- complete basis size `2^5=32`;
- one fixed factorized causal vertex at a time, with branch pattern `kappa_ab=sigma_a sigma_b`.

## Frozen common-collision witness

In gauge-fixed boost coordinates use exactly

`x_0=(0,0,0)`

`x_1=(1,2,3)`

`x_2=(2,3,5)`

`x_3=(3,5,7)`

`x_4=(5,7,11)`.

No coordinate may be changed after implementation starts.

For wedge `(a,b)`, use the exact Gaussian-integer zero/nonzero-equivalent leading matrix

`M(v_ab)=[[v_z,-v_x-i v_y],[-v_x+i v_y,-v_z]]`,

`v_ab=x_a-x_b`,

in ascending magnetic order `(-1/2,+1/2)`.

Use the scaled integer node tensors frozen in the source supplement. Stripped normalizations and omitted edge factors are all explicitly nonzero and may affect only the common coefficient, not zero/nonzero status.

## Lane A — primary-source and leading-power lock

PASS iff:

1. primary source Eq. (4) places ten Toller matrices inside the four-group vertex integral;
2. companion source identifies Toller matrices as polynomially bounded functions on `SL(2,C)` and the Feynman prescription as the unique branch projector;
3. gamma-simple source Eq. (9)/(46) is the one-wedge function used;
4. exact `j=1/2` small-beta derivation gives branch powers `beta^-2` and leading shapes `+diag(1,-1)` / `-diag(1,-1)` up to common nonzero scalar `2/(1+gamma^2)`;
5. all frozen ray differences are nonzero;
6. no spinor-contact termwise pullback is imported into this gate.

If the source function/order or leading power cannot be fixed, aggregate is BLOCKED.

## Lane B — complete exact 32-component leading contraction

Contract the full K5 leading tensor exactly for every one of the 32 boundary basis tuples

`(k_0,k_1,k_2,k_3,k_4) in {0,1}^5`.

All arithmetic must be exact. A Gaussian-integer representation is preferred; floating-point nonzero thresholds are forbidden.

Frozen PASS prediction:

- all `32/32` scaled contractions at the frozen ray are nonzero.

For every component record:

- the five `k_a` labels;
- the exact scaled Gaussian-integer contraction `(Re,Im)`;
- zero/nonzero status;
- a deterministic checksum of all 32 exact pairs.

If any component is exactly zero, Lane B is scientific FAIL relative to the frozen prediction. Preserve the actual count; do not change the ray.

## Lane C — causal-branch sign transport

Enumerate the 16 inequivalent factorized causal assignments by fixing `sigma_0=+1` and varying `sigma_1,...,sigma_4`.

For each of 32 boundary components and each of 16 causal assignments, replace every edge leading matrix by

`kappa_ab M(v_ab)`, `kappa_ab=sigma_a sigma_b`,

which is the exact leading branch-sign transport in this scoped all-jhalf source limit.

PASS prediction:

- all `32*16=512` contractions are nonzero;
- for each boundary component, every causal assignment differs from the all-plus leading contraction only by the predicted product `prod_(a<b) kappa_ab`.

Because `prod_(a<b) sigma_a sigma_b = prod_a sigma_a^4 = +1` on K5, the frozen stronger prediction is that the ten-edge branch signs cancel globally and all 16 leading contractions are exactly equal, not merely equal up to sign.

This lane tests fixed causal structures only. It is not a causal-sector-sum cancellation theorem.

## Lane D — local absolute-integrability verdict

Freeze:

- wedge leading power `p_e=2` for ten wedges;
- total source-ordered leading power `P=20`;
- transverse boost dimension `d=12`;
- radial density power `d-1=11`.

For each boundary component with nonzero Lane-B leading coefficient, compute

`q=-20`,

`q+d=-8`,

and radial absolute-integrand exponent

`d-1+q=-9`.

PASS prediction:

- every one of the 32 complete boundary components fails local absolute `L1` at the common collision because `q+d<0`;
- the nonzero exact angular witness implies an open angular neighborhood with the same leading nonzero property.

This is a local absolute-integrability statement only.

## Aggregate PASS

All lanes A-D PASS:

`ITER077I_SM_SOURCE_ORDERED_JHALF_TOLLER_FUNCTION_K5_LEADING_TERM_NONZERO_ALL_32_BOUNDARY_COMPONENTS_NOT_LOCALLY_L1_EXACT_SCOPED`

## Aggregate FAIL

If source/object definition is valid but one or more frozen predictions fail:

`ITER077I_SM_SOURCE_ORDERED_JHALF_K5_FULL32_L1_PREDICTION_FAILS_EXACT_SCOPED`.

Scientific FAIL must remain a successful workflow execution with the actual exact data preserved.

## Aggregate BLOCKED

If source ordering / one-wedge function / leading power cannot be established:

`ITER077I_SM_SOURCE_ORDERED_JHALF_K5_L1_BLOCKED_OBJECT_DEFINITION`.

## Scientific consequence on PASS

A PASS establishes that **after performing the one-wedge source construction first**, the resulting ordinary Toller-function K5 integrand still fails local absolute integrability at the common collision in every basis component of the frozen all-jhalf boundary space.

It does not establish nonexistence of the vertex as an oscillatory/distributional boundary value. The next admissible gate must test the source-selected correlated/improper group-integral boundary value with the complete 32-component contraction and exact smooth subleading phase/measure structure.

## Claim locks

No full causal-vertex divergence/nonexistence theorem; no conditional/convergent-integral theorem; no regulator-independence theorem; no causal-sector-sum theorem; no physical source-to-K4 pushforward; no nominal epsilon^-1 coefficient; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; retain source spectral i epsilon.