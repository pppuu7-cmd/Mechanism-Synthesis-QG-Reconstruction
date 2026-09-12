# Iteration 056 — orientation-cocycle covariance of the K4 affine denominator geometry

## Preregistration

This file is committed **before** Iter056 implementation and production output.

Iter055 terminal result is `K4_SIGNED_NORMAL_CIRCUIT_ATLAS_S4_NONCOVARIANT`: the naive action that permutes only the factorized causal class `s_e=sigma_a sigma_b` does not preserve the exact signed-normal circuit atlas. Iter056 tests one specific algebraic explanation fixed prospectively here.

## Frozen hypothesis

The K4 surrogate uses canonically oriented edge-flow variables for edge order

`01,02,03,12,13,23`,

with denominator factors

`x_e - i s_e epsilon`.

Under a vertex permutation `p`, an old canonically oriented edge `(a,b)` maps to `(p(a),p(b))`. If `p(a)>p(b)`, the canonical orientation of the target edge is reversed. Define the exact orientation sign

`q_e(p)=+1` if `p(a)<p(b)`, and `q_e(p)=-1` otherwise.

For the corresponding target canonically oriented variable,

`x_old = q_e x_new`,

hence exactly

`x_old - i s_old epsilon = q_e [x_new - i (q_e s_old) epsilon]`.

Therefore the prospectively frozen **effective oriented pole sign** is

`s_eff,new = q_e s_old`

after edge permutation. No other sign correction is allowed.

## Exact covariance test

For every source causal class, every one of 24 vertex permutations, every source tree/cycle basis and every target frozen tree/cycle basis:

1. construct the unsigned edge-permutation matrix `E`;
2. construct `Q=diag(q)` in target edge order and oriented edge map `H=Q E`;
3. verify that `H A_source` lies exactly in the K4 cycle space;
4. solve the exact 3x3 coordinate change `C` satisfying

   `A_target C = H A_source`;

5. require `det(C)=±1` and exact reconstruction;
6. form `s_eff` by the frozen rule above;
7. verify exact signed-normal covariance

   `diag(s_eff) A_target C = E diag(s_source) A_source`.

This identity is the primary gate. It is algebraic and contains no numerical tolerance.

## Factorized-class closure subtest

Independently ask whether each effective target edge-sign vector `s_eff` can still be written in the original factorized form

`s_eff,ab = tau_a tau_b`, with `tau_0=+1`.

The factorization test is exact: set `tau_v=s_eff,0v` for `v=1,2,3`, then verify the remaining three edges. Report the number of the `8×24=192` class/permutation actions that remain inside the original eight factorized classes.

This subtest does not alter the primary covariance identity.

## Frozen matrix

- 8 source factorized causal classes;
- 24 vertex permutations;
- 4 source cycle bases;
- 4 target cycle bases;
- total signed-normal covariance checks: `8×24×4×4 = 3072`.

## Frozen terminal classifications

- `ITER056_ORIENTATION_COCYCLE_AUDIT_INVALID` if any edge permutation/orientation map, cycle-space reconstruction, or exact coordinate-change validation fails.
- `K4_ORIENTATION_COCYCLE_COVARIANCE_FAIL` if the audit is valid but any primary signed-normal covariance identity fails.
- `K4_ORIENTATION_COCYCLE_RESTORES_COVARIANCE_FACTOR_CLASS_CLOSED` if all 3072 covariance identities pass and all 192 effective sign vectors remain factorized.
- `K4_ORIENTATION_COCYCLE_RESTORES_COVARIANCE_FACTOR_CLASS_NOT_CLOSED` if all 3072 covariance identities pass but at least one effective sign vector lies outside the original eight factorized classes.

## Interpretation locks

A PASS establishes only the exact transformation law of the **frozen oriented-flow denominator/signed-normal surrogate**. It does not by itself prove the full Toller vertex permutation law, because Toller matrices are functions rather than representations and the full transformation also involves group-element inversion/index structure. The 2026 Toller paper establishes branch relations and `T+ + T-=D`, but Iter056 does not assume an unsourced full-vertex inversion identity.

No physical amplitude, K5, G3, F9, G8, new-physics, or general causal-EPRL no-go claim is permitted from this gate.
