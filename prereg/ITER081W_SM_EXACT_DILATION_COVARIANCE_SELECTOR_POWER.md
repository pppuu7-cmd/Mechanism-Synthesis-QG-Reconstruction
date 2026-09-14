# Iter081W-SM prereg — exact dilation/homogeneity covariance selector power on the repaired K5 invariant jet space

Status: **PROSPECTIVE CRITIC THEOREM GATE — frozen before result**
Date: 2026-09-14

## Motivation
Iter081R proves a 28-dimensional scalar `SO(3) x S5` invariant supported normal-jet lower bound through order 8. A natural mathematical strengthening beyond mere scaling-degree control is to require the extension of the leading common-collision singularity to preserve its exact transverse dilation law (or, more generally, to satisfy the same fixed scaling-anomaly equation).

This is a selector-power test, not a claim that the complete CRQN amplitude is exactly homogeneous.

## Frozen local model
Let `N` have codimension `d=12` and let `u_0` denote the leading homogeneous off-collision K5 distribution in the authoritative all-`j=1/2` common-collision sector, with transverse homogeneity degree

`lambda=-20`.

Let `E` be the transverse Euler vector field. An exactly homogeneous extension `U` would satisfy

`(E-lambda) U = 0`

in the convention where a function homogeneous as `u(rX)=r^lambda u(X)` obeys `(E-lambda)u=0`.

More generally two extensions may satisfy the same fixed anomalous dilation equation

`(E-lambda) U = A`

with the same supported anomaly `A`.

## Frozen ambiguity input
Use only the repaired scalar invariant normal-jet subspace from Iter081R:

`J_inv = direct_sum_(k=0)^8 J_k`,

with

`dim J_k = [1,0,1,0,3,0,7,0,16]`.

A normal derivative of total order `k` of `delta_N` has transverse homogeneity degree

`-d-k = -12-k`.

## Exact question
If `U1` and `U2` are two source-symmetry-compatible extensions of the same leading off-collision `u_0` and satisfy the same exact dilation equation/anomaly, classify the allowed difference

`W=U1-U2`

inside `J_inv`.

## Frozen derivation criterion
Because `W` is supported on `N` and obeys the homogeneous difference equation

`(E-lambda)W=0`,

only jet orders satisfying

`-12-k = -20`

may survive, hence `k=8`.

The gate must verify this distributional Euler-eigenvalue relation explicitly and then use Iter081R's exact `d_8=16` count.

## Frozen classifications
- `ITER081W_SM_EXACT_DILATION_COVARIANCE_LEAVES_16_DIMENSIONAL_INVARIANT_ORDER8_AMBIGUITY_EXACT_SCOPED` if the difference space contains the full repaired degree-8 invariant sector and therefore remains at least 16-dimensional.
- `ITER081W_SM_DILATION_COVARIANCE_UNIQUELY_SELECTS_SCALAR_INVARIANT_EXTENSION_SCOPED` only if a valid additional source identity eliminates all but zero difference.
- `INVALID_OBJECT_OR_SCALING_CONVENTION` if the Euler action/order relation is inconsistent.

## Claim ceiling
This is only a theorem about selector power on the leading homogeneous singularity and demonstrated scalar invariant subspace. It does not impose exact homogeneity on the full amplitude, determine the scaling anomaly, classify representation-valued jets, prove existence of a homogeneous extension, or establish causal-vertex finiteness/divergence, regulator independence, G3/F9/G8/K5, new physics or complete QG.
