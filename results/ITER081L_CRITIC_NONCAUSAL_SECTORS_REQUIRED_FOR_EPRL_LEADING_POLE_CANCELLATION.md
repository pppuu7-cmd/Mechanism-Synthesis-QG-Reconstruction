# Iter081L Critic exact combinatorial-source corollary — non-causal orientation sectors are required for the standard EPRL leading Toller-pole cancellation on the frozen K5 minimal-sector collision

Date: 2026-09-14
Status: **EXACT LEADING-ORDER MINIMAL-SECTOR COROLLARY; NOT A STATEMENT THAT NON-CAUSAL SECTORS ARE PHYSICALLY REQUIRED IN A FINAL THEORY**

## Inputs

1. BCG causal decomposition: on each wedge `T^+ + T^- = D`. The ordinary EPRL vertex is recovered by summing all branch assignments.
2. Beltran `arXiv:2603.22661v2` Eqs. (23)-(25): all wedge assignments split into `eta=+1` causal, `eta=-1` causal, and non-causal sectors; summing all assignments recovers EPRL-KKL.
3. Iter077I exact `j=1/2` small-collision source-Toller leading transport: for each wedge, the two branches have opposite leading matrix shapes `+M_e` and `-M_e`, with the same nonzero scalar magnitude.
4. Iter077I exact full K5 boundary contraction: for all 32 frozen boundary components, the all-plus leading coefficient `C_alpha` is nonzero.
5. Iter081K: all 32 proper causal assignments across both `eta` sectors have the same leading coefficient `+C_alpha`.

## Full 10-wedge branch cube
For a fixed frozen boundary component `alpha`, let a branch assignment be

`epsilon=(epsilon_e)_(e in E(K5))`, `epsilon_e in {+1,-1}`.

At the exact Iter077I leading order its coefficient relative to the all-plus contraction is

`prod_e epsilon_e`.

There are `2^10=1024` assignments. Therefore the unrestricted leading coefficient sum is

`C_alpha * sum_epsilon prod_e epsilon_e`

`= C_alpha * prod_(e=1)^10 [(+1)+(-1)]`

`= 0`.

This is the leading-order combinatorial form of the Toller-pole cancellation behind the unrestricted identity `prod_e(T_e^+ + T_e^-)=prod_e D_e`.

## Proper causal sectors
For eta=+1 K5 causal assignments,

`epsilon_ab=sigma_a sigma_b`,

so

`prod_(a<b) epsilon_ab = prod_a sigma_a^4 = +1`.

For eta=-1, every one of ten wedge signs is additionally reversed, so

`prod_(a<b) epsilon_ab = (-1)^10 prod_a sigma_a^4 = +1`.

Thus all `16+16=32` proper causal assignments lie in the **positive product-parity class** and contribute

`+32 C_alpha`

at order `r^-20`.

## Non-causal sectors
The remaining number of assignments is

`1024-32=992`.

Since the unrestricted leading sum is exactly zero, their collective leading contribution is forced to be

`-32 C_alpha`.

Equivalently, among all 1024 branch assignments there are 512 with product parity `+1` and 512 with parity `-1`. Removing the 32 proper-causal assignments, all of which have positive parity, leaves the non-causal set with

- `480` positive-parity assignments;
- `512` negative-parity assignments;

and net parity sum

`480-512=-32`.

Hence the non-causal sectors supply exactly the leading contribution required to cancel the `+32 C_alpha` from the proper causal sectors.

## Exact conclusion
On the authoritative all-`j=1/2` K5 collision patch, the standard unrestricted EPRL leading Toller-pole cancellation **cannot occur inside the proper causal sectors alone**. The missing cancellation at order `r^-20` is furnished by the non-causal orientation assignments included in the unrestricted branch sum.

Classification:

`ITER081L_SM_NONCAUSAL_ORIENTATION_SECTORS_ARE_NECESSARY_FOR_UNRESTRICTED_EPRL_R_MINUS20_LEADING_TOLLER_POLE_CANCELLATION_ON_FROZEN_JHALF_K5_COLLISION_EXACT_COROLLARY_SCOPED`.

## Relation to causal amplitudes
This explains the coexistence of two established facts:

- unrestricted EPRL reconstructs products of bounded Wigner matrices and cancels the selected-branch Toller poles;
- Beltran proper-causal sums retain the Iter077I `r^-20` leading singularity (Iter081H/K).

The causal restriction removes precisely a set of branch assignments whose net leading parity contribution is required for the unrestricted cancellation.

## Scope ceiling
This is a statement about the exact leading branch-sign structure on the validated minimal-spin K5 common-collision geometry. It does **not** imply that non-causal configurations must be retained in a physically correct quantum-gravity theory. A different causal definition, subtraction, correlated boundary value, renormalized face functional, or new dynamics could alter the mechanism. It does not prove full causal-vertex divergence/nonexistence, generic-spin behavior, regulator dependence, or complete QG.

## Research consequence
A future causal cure cannot appeal to the **same** cancellation mechanism as ordinary EPRL while retaining only Beltran proper-causal orientation sectors: at the authoritative minimal-sector leading order, those sectors all have the same sign after full K5 contraction. Restoring boundedness requires genuinely new content (a correlated extension/boundary value, subtraction/renormalization, modified weights, or other source-motivated mechanism), not merely summing the existing proper causal assignments.
