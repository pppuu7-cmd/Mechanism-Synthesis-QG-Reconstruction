# Iter077H-SM preregistration — finite spectral epsilon contact persistence

**Date:** 2026-09-14
**Status:** prospective / frozen before implementation

## Dependencies

- primary source Eq. (35)-(39), arXiv:2601.23162;
- exact finite-epsilon derivation frozen in `sources/ITER077H_SM_FINITE_EPSILON_JHALF_CONTACT_DERIVATION.md`, source commit `b7abbd430313b0624e1b0dfeb12025f5e8753539`;
- authoritative corrected `Iter077G-SM`;
- frozen rank-9 self-stress `lambda=(1,-1,0,0,1,0,0,0,0,0)`.

## Lane A — exact spectral division

Starting from

`Theta_(sigma,epsilon)=int dp/(2pi i) sigma/(p-i sigma epsilon) F_(1/2)(rho+p,rho)e^(ipx)`,

PASS iff exact polynomial division and Fourier identities produce

`Theta = [1+(2 i sigma rho epsilon-epsilon^2)/D] theta(sigma x)e^(-epsilon |x|)`

`      + [(epsilon-2 i sigma rho)/D] delta(x)`

`      - [sigma/D] delta'(x)`,

`D=rho^2+1/4`.

## Lane B — epsilon persistence

PASS iff:

1. the delta-prime coefficient is exactly `-sigma/D`, independent of epsilon;
2. for gamma-simple `rho=gamma/2`, `C_sigma=-4 sigma/(1+gamma^2)`;
3. finite `epsilon>0` does not remove the local contact derivative;
4. the `epsilon->0+` limit reproduces the corrected Appendix-D contact distribution.

## Lane C — rank-9 pure-contact self-stress order

For arbitrary wedge signs `sigma_e=+/-1`, gamma-simple finite-epsilon contact factors have

`A_e=4(epsilon-i sigma_e gamma)/(1+gamma^2)`,

`C_e=-4 sigma_e/(1+gamma^2)`.

At frozen rank-9 `lambda`, PASS iff the pure-contact Fourier restriction has exact degree 3 in `t`, and the leading coefficient

`prod_(lambda_e=0) A_e * prod_(lambda_e!=0) (i C_e lambda_e)`

is nonzero for every one of the `2^10` wedge-sign assignments at frozen `gamma=6/5`, `epsilon=1/7`.

The finite rational epsilon is only an exact nonzero control; symbolic nonvanishing conditions must also be recorded.

## Lane D — scope/no-go contract

PASS iff the result is classified only as:

`FINITE_SPECTRAL_EPSILON_DOES_NOT_TERMwise_SMOOTH_THE_JHALF_CONTACT_SUBTERM`

and explicitly does **not** claim:

- nonexistence of the full source-selected correlated boundary value;
- non-cancellation after summing Heaviside/contact strata;
- full causal-vertex divergence;
- regulator independence;
- physical source-to-K4 pushforward;
- nominal epsilon^-1 coefficient.

## Aggregate PASS

`ITER077H_SM_FINITE_SPECTRAL_EPSILON_LEAVES_NONZERO_RANK9_N3_PURE_CONTACT_SUBTERM_CORRELATED_SOURCE_ORDERING_STILL_REQUIRED_EXACT_SCOPED`

## FAIL

A valid contradiction of the frozen finite-epsilon formula or an exact vanishing of the degree-3 coefficient for an allowed sign assignment is a scientific FAIL and must be preserved.

## BLOCKED

Only missing primary/source object definition gives BLOCKED.

## Next admissible step on PASS

The source-selected extension cannot be identified with naive finite-epsilon termwise pullback. The next gate must test an actual **ordering of source operations**—for example, CP1 wedge integration to Toller functions before K5 multiplication, or a jointly defined spectral/group boundary value—and then include the smooth phase/measure/intertwiner factors.