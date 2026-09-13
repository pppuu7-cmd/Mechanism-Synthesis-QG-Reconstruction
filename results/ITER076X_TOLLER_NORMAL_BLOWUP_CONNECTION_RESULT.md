# Iter076X result — Toller normal-blow-up angular connection survives generic intertwiners

**Date:** 2026-09-13

## Authority

- source supplement: `ddeb96b666e11f88f99e868302c0916deb008f63`
- prospective preregistration: `e6b1c94dd3fd29a4bc763c45cd757c4de34c83e3`
- implementation: `e2fbd7bb2d0a3ece95a33a6b7e11999ef6bb8e6d`
- production/workflow head: `0382d068c42a48e8bad3c24cde5e47ab04e0c68a`
- authoritative run: `34783825102`
- jobs: A `103795555679`, B `103795555684`, C `103795555541`, D `103795555831`, aggregate `103795601967`

Artifacts:

- A `10326001615`, `sha256:352ea727a96b71aab82ff6fee32839ea74e33c8eaaa838a4883f13943db5acde`
- B `10326245990`, `sha256:bd1366e9da13ccf2682e3994a3efe79d38a7cdf76bcb83717e83356d1fbbe8c6`
- C `10325752215`, `sha256:5a01027b140e432c278cd20c15450bbd0465c86bc3cee8ba158cc045d8cd10b3`
- D `10325941689`, `sha256:3689555f7ff758595357cd9a2a9dc27ee7d079ad42b4608de44db411df48a421`
- aggregate `10326171246`, `sha256:0f0c104731eaa338c37ce354053b2ef04ed8df7882f615b799ff28bcda86a6e1`

All frozen lanes A/B/C/D and aggregate completed successfully.

## Frozen classification

`ITER076X_TOLLER_NORMAL_BLOWUP_ANGULAR_CONNECTION_SURVIVES_GENERIC_INTERTWINERS_EXACT_SCOPED`

## Exact leading-family result

The exact leading magnetic recurrence from Iter076V has primitive shape

`C_m proportional to (-1)^(j+m) binom(2j,j+m)`.

For a unit boost-normal direction `n`, source Eq.(7) gives the equivariant leading family

`C_n = D^j(U_n) C_z D^j(U_n)^(-1)`.

Because `C_z` is diagonal in `J_z`, it commutes with the stabilizer of the north-pole direction. Therefore `C_n` is independent of the section representative `U_n -> U_n exp(phi J_z)`.

For a transverse angular generator `A`, the right-relative connection is

`C_z^(-1)[A,C_z] = C_z^(-1) A C_z - A`.

It is invariant under the causal branch leading-scale flip `C -> -C`.

## Exact single-edge connection

For all frozen spins `j=1/2,1,3/2,2,5/2,3`:

- `C_z` is invertible;
- `[J_z,C_z]=0`;
- `C_z^(-1) J_+ C_z` and `C_z^(-1) J_- C_z` obey the frozen nonconstant magnetic-weight formulas exactly.

For `j>=1`, the transverse connection is not a scalar multiple of `J_+` over all nonzero magnetic steps. The `j=1/2` case is the expected one-step special control.

## Exact intertwiner survival census

The seven exact 4-valent invariant controls from Iter076V/W were transformed by the tensor product of the leading `C_z` matrices.

Results:

- total `J_z` still annihilates all `7/7` transformed tensors; this is the stabilizer/non-direction-changing control;
- transverse total `J_+` and `J_-` both vanish for exactly the two `(1/2,1/2,1/2,1/2)` intertwiners;
- transverse total `J_+` and `J_-` are both nonzero for the remaining `5/7` controls.

In the two all-spin-half cases, `tensor C_z` acts as one common scalar on all nonzero invariant-support components. In every surviving control there are at least two distinct leading weights, so the transformed tensor leaves the SU(2)-invariant subspace.

Therefore the angular connection survives exact boundary-intertwiner contraction generically in the frozen control family.

## Scientific consequence

The 24 pure generator-direction zeros of Iter076W do **not** assemble into a direction-independent zero factorized germ. The leading singular Toller coefficient is naturally a matrix-valued equivariant object over the sphere of boost normals and carries a nontrivial transverse connection.

This is not an ordinary linear Frechet source one-jet at the identity. It is a normal-blow-up compatibility datum. Because mixed compact/boost source paths can move the boost-normal direction at the subleading radial order, this connection must be tracked separately in any source-derived degree-two calculation.

## Next admissible gate

Derive a concrete second-order polar/KAK jet for a mixed source path such as

`g(t)=exp[t(B_z + A_y)]`,

with `B_z` Hermitian boost and `A_y` compact anti-Hermitian rotation. Freeze the exact coefficient with which the normal direction rotates at order `t`, identify the corresponding right compact factor, and test whether the induced mixed subleading boundary tensor survives the same exact intertwiner controls.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no ordinary full source one-jet; no physical nonlinear source-to-K4 map; no nominal `epsilon^-1` coefficient; no physical causal-vertex finiteness/divergence theorem; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; retain the source spectral `i epsilon` prescription.