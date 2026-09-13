# Iter076X preregistration — normal-direction leading-matrix connection and generic intertwiner survival

Date: 2026-09-13

## Purpose

Iter076W established exact cancellation of all 24 pure Lie-generator directions at the four integrated source nodes. Those separate directional zeros do not yet define a single direction-independent factorized germ because the leading gamma-simple Toller singular matrix depends on the boost-normal direction.

This gate tests the first angular response of that leading matrix family on the normal blow-up. The central question is whether the response is again pure SU(2) gauge and killed by the boundary intertwiner, or whether a genuinely nontrivial connection datum survives for generic spins/intertwiners.

## Frozen source/derived input

Use `sources/TOLLER_NORMAL_BLOWUP_CONNECTION_SUPPLEMENT.md`, committed before implementation, and the authoritative Iter076V/W results.

For each spin `j>0`, use the primitive leading magnetic shape

`C_m proportional to (-1)^(j+m) binom(2j,j+m)`

which is equivalent to the exact Iter076V recurrence

`C_m/C_(m-1)=-(j-m+1)/(j+m)`.

For a boost-normal direction `n`, source Eq.(7) gives

`C_n=D^j(U_n) C_z D^j(U_n)^(-1)`.

## Frozen lanes

### Lane A — provenance and scope locks

PASS iff the committed supplement contains:

- the exact closed-form leading magnetic shape and recurrence;
- the equivariant family `C_n=D(U_n)C_zD(U_n)^(-1)`;
- section-independence under `U_n -> U_n exp(phi J_z)`;
- the relative angular connection `C_z^(-1)[A,C_z]`;
- the frozen `5/7` survival prediction;
- the explicit firewall that this is a normal-blow-up compatibility datum, not an ordinary Frechet one-jet at the identity.

The authoritative Iter076W result must contain its PASS classification.

### Lane B — exact single-edge angular connection

For exact spins `j in {1/2,1,3/2,2,5/2,3}`, construct `C_z` from the primitive recurrence and exact standard `J_z,J_+,J_-` matrices.

PASS iff:

- `C_z` is invertible;
- `[J_z,C_z]=0` exactly;
- for every allowed magnetic step,
  `C_z^(-1) J_+ C_z |j,m> = -[(j+m+1)/(j-m)] J_+|j,m>`;
- for every allowed magnetic step,
  `C_z^(-1) J_- C_z |j,m> = -[(j-m+1)/(j+m)] J_-|j,m>`;
- for every `j>=1`, the transverse relative connection `C^-1[J_+,C]` is not a scalar multiple of `J_+` across all nonzero magnetic steps;
- replacing `C` by `-C` leaves `C^-1[A,C]` unchanged exactly.

The `j=1/2` scalar-proportional special case is retained as a control and is not generalized.

### Lane C — exact 4-valent intertwiner survival census

Use the same seven exact Clebsch-Gordan invariant tensors as Iter076V/W. For each tensor, form

`F_z = (tensor_e C_{j_e,z}) iota`

(up to the harmless choice of bra/ket placement; all `C_z` are diagonal).

PASS iff the frozen exploratory prediction is reproduced exactly:

- total `J_z` annihilates `F_z` for all `7/7` controls;
- total `J_+` and total `J_-` both annihilate `F_z` for exactly the two `(1/2,1/2,1/2,1/2)` controls;
- total `J_+` and total `J_-` are both nonzero for the remaining `5/7` controls;
- the two all-spin-half cases have `tensor C_z` acting as a common scalar on every nonzero invariant-support component;
- every surviving case has at least two distinct `tensor C_z` weights on its nonzero invariant support.

Because `J_+` and `J_-` land in distinct total-magnetic sectors, simultaneous nonzero ladder results certify nonzero transverse `J_x` and `J_y` angular response.

### Lane D — section/branch independence and firewall

PASS iff exact controls verify:

- `C_z` commutes with every stabilizer matrix `exp(phi J_z)` symbolically/algebraically;
- `C_n` is therefore independent of the representative `U_n` modulo the `J_z` stabilizer;
- the angular relative connection is unchanged under the causal leading-scale flip `C -> -C`;
- `normal_blowup_connection_nontrivial_generic=true` after the Lane C survival result;
- `iter076W_pure_direction_zeros_unchanged=true`;
- `ordinary_Frechet_source_onejet_established=false`;
- `direction_independent_factorized_germ_established=false`;
- `physical_source_to_K4_curvature_selected=false`;
- `epsilon_minus1_coefficient_established=false`;
- no generic finite-spin signed P3 or G3/F9/G8/K5 promotion.

## PASS classification

`ITER076X_TOLLER_NORMAL_BLOWUP_ANGULAR_CONNECTION_SURVIVES_GENERIC_INTERTWINERS_EXACT_SCOPED`

## Scientific meaning on PASS

The pure-direction cancellations of Iter076W do **not** assemble into a direction-independent zero factorized germ. The leading singular Toller matrix defines a nontrivial equivariant object over the sphere of boost normals; its transverse angular connection survives boundary-intertwiner contraction for generic spins/intertwiners (`5/7` frozen exact controls).

This identifies a new, sharply defined source datum that must be propagated into any degree-two/source-to-K4 analysis. It is not an ordinary source one-jet and must be kept distinct from the nonlinear P3 curvature channel of Iter076R-S.

## Next admissible gate

Determine how this normal-bundle connection enters a concrete mixed compact/boost group path through the source relative argument `g_b^{-1}g_a`. Derive the second-order polar/KAK jet for `exp[t(B+A)]` and isolate the coefficient multiplying the angular connection. Then test whether the resulting mixed term survives the full node-5 boundary tensor controls. This must remain separate from the physical source-to-K4 pushforward.

## FAIL classification

`ITER076X_TOLLER_NORMAL_BLOWUP_CONNECTION_CONFIRMATION_FAIL`

A failure is an exact algebra/source-geometry result, not a physical finiteness/divergence theorem.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no ordinary full source one-jet; no physical nonlinear source-to-K4 map; no nominal `epsilon^-1` coefficient; no physical causal-vertex finiteness/divergence theorem; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; retain the source spectral `i epsilon` prescription.