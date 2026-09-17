# K5 mask-511 physical numerator/action exact corner witness — terminal Researcher result

Date: 2026-09-17

## Terminal classification

`K5_MASK511_NO_OBSTRUCTION_WITNESS_ON_FROZEN_RAYS_INCONCLUSIVE_SCOPED`

Status: `PASS_EXACT_INCONCLUSIVE_SCOPED`.

This is an exact scoped Researcher result on one fixed labeled K5 corner. It is not a proof of angular-uniform integrability, not an S5-orbit theorem, and not a global Stokes/IBP result.

## Prospective authority

Scientific preregistration:

`prereg/K5_MASK511_PHYSICAL_NUMERATOR_ACTION_EXACT_CORNER_WITNESS.md`, commit `4f8a783b9d1fd8f6e022ccdc9a888d71ecd591c7`.

Implementation commit:

`49ecdbe27e5df51c05fa322dc3e3c9085bed74bc`.

Workflow/head:

`0e3fcf8b1e25aee6d4031b927418120274b16e60`.

The gate deliberately does not consume the pending Researcher-only coefficient-level boundary-S5 transport theorem and does not execute the frozen 64-component resolver.

## Production authority

- run `35226938480`, terminal `success`;
- job `105220822338`, terminal `success`;
- artifact `10499776155`, `k5-mask511-physical-numerator-action-exact-corner-witness`;
- artifact ZIP SHA256 `f9f7c841cc4856cc08fa7c516d7d5e2dc1e658191f8300455dab99b0f32e95db`;
- full production JSON SHA256 `d1e8defab3896bb576b1c9cf9ff068f1b567b6f37ddc1673d9295afdcaa429d7`;
- executed script SHA256 `890f679ea1ea6af0f64c4330cc386a8db105196acb609407f3b305b4afb5d91f`.

All frozen checks and malformed controls passed.

## Exact object and geometry

The labeled corner is

`Z_511={0,1,2,3,4,5,6,7,8}`,

with `k=9` and one non-collapsing canonical edge.

Frozen path:

`alpha_e(t)=W_e t` for `e in Z_511`, and `alpha_9(t)=W_9`.

Two prospectively frozen asymmetric angular witnesses were used:

`W1=(2,3,5,7,11,13,17,19,23,29)`,

`W2=(31,37,41,43,47,53,59,61,67,71)`.

Exact denominator/projective authority gives

`r_Psi=3`, `g=k-1=8`, `m=k/2-(21/2)r_Psi=-27`.

Thus

`I=-19+r_N`,

`F=-19+r_N+r_U=-16+r_N`, using terminal `r_U=3`,

and

`A=-19+r_B`.

## Exact bounded reconstruction

For each W1/W2 path the full source-faithful all-32/100000-term physical point object was evaluated exactly at every integer `t=1,...,34`.

`N_c(t)` was reconstructed from `t=1,...,28` under the frozen degree ceiling `27` and validated exactly at all `t=29,...,34`.

`B_v[N_c](t)` was reconstructed from `t=1,...,32` under the frozen degree ceiling `31` and validated exactly at `t=33,34`.

No floating point, modular-only zero test, adaptive weight or post-output witness was used. Corrupted-sample controls and wrong degree-ceiling controls were rejected.

## Result

For **both** physical invariant-dual channels and for **both** independently frozen asymmetric angular witnesses:

`r_N = 19`,

`r_B = 21`.

Therefore every frozen path gives

`I=0`,

`F=3`,

`A=2`.

All three radial exponents are strictly greater than `-1` on both frozen rays.

Exact first coefficients are nonzero and retained in

`results/raw/k5_mask511_physical_numerator_action_exact_corner_witness_authoritative.json`.

In particular the exact reconstruction proves cancellation of all `N_c` coefficients through orders `t^0,...,t^18` on W1 and W2, and all `B_v[N_c]` coefficients through `t^0,...,t^20` on W1 and W2.

## Scientific interpretation

The maximally collapsed proper labeled corner does **not** provide the prospectively sought direct ordinary-nonintegrability witness on either frozen angular ray. The most singular denominator geometry is compensated on both tested full physical channels by substantial exact numerator/action cancellation.

This does **not** prove the lower coefficients vanish as angular polynomials. Two exact angular witnesses cannot certify angular-uniform order `r_N=19` or `r_B=21`. A lower coefficient could vanish on W1 and W2 but be nonzero elsewhere. Therefore the only allowed terminal classification is the frozen inconclusive/no-obstruction-witness outcome.

The agreement of both channels and both asymmetric witnesses at `r_N=19`, `r_B=21` is nevertheless a new exact scoped fact and strongly localizes the next mathematical question: whether the lower-order coefficients vanish identically by structural divisibility/covariance, rather than merely at the frozen rays.

## Claim ceiling

No all-angle corner finiteness theorem follows. No other labeled subset or S5 orbit is inferred. The pending independent Critic reconstruction of coefficient-level full-source boundary S5 transport remains mandatory before the frozen 64-component physical resolver may run.

No global Stokes/IBP relation, invariant-dual K5 period, full 217-dimensional tensor theorem, physical finite-part selector, reduction of `dim_C F_8=377`, regulator independence, F9/G3/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete-QG claim follows.
