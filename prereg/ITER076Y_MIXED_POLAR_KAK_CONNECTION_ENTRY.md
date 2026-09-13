# Iter076Y preregistration — concrete mixed polar/KAK jet feeds the surviving normal-bundle connection

Date: 2026-09-13

## Purpose

Iter076X established a nontrivial transverse connection of the leading Toller singular matrix over boost-normal directions, with exact survival in `5/7` frozen intertwiner controls. This gate asks whether that connection is reached by a concrete source-group path or is merely a formal variation of the blown-up leading family.

Use a mixed compact/boost one-parameter source path and derive its polar/KAK jet through the first subleading radial order. The frozen prediction is that the compact rotation splits equally between the two Cartan compact factors, causing the right factor to feed exactly one half of the transverse connection into the boundary tensor.

## Frozen source/derived input

Use `sources/TOLLER_MIXED_POLAR_KAK_JET_SUPPLEMENT.md`, committed before implementation, source Eq.(7), and the authoritative Iter076X result.

In the defining two-dimensional representation set

`B=sigma_z/2`, `A=-i alpha sigma_y/2`, real `alpha != 0`,

`g(t)=exp[t(A+B)]`, `t>0`.

## Frozen lanes

### Lane A — provenance and scope locks

PASS iff the committed supplement contains:

- the source Cartan convention `g=U_1 exp(beta sigma_z/2) U_2`;
- the frozen mixed path and generator conventions;
- the second-order polar jet;
- the half-angle Cartan split;
- the induced `T_1` formula;
- the inherited `5/7` boundary-survival prediction;
- the firewall that this is a local source-group control, not the physical source-to-K4 map.

The authoritative Iter076X result must contain its PASS classification.

### Lane B — exact defining-representation polar/KAK jet

Use exact `2x2` Pauli matrices and symbolic real `alpha,t`. Verify through the frozen orders:

- `[A,B]=alpha sigma_x/2`;
- `log(g^dagger g)=2tB-t^2[A,B]+O(t^3)` by direct second-order matrix expansion;
- `log p=tB-(t^2/2)[A,B]+O(t^3)`;
- the positive-factor boost vector is `t z-(alpha/2)t^2 x`, hence `beta=t+O(t^3)` and `n=z-(alpha/2)t x+O(t^2)`;
- with `R(t)=exp(+i alpha t sigma_y/4)`,
  `R B R^-1 = B-alpha t sigma_x/4+O(t^2)`;
- `p=R exp(tB) R^-1+O(t^3)`;
- `log u=tA+O(t^3)` for `u=g p^-1`;
- both Cartan compact factors have first derivative `-i alpha sigma_y/4`, i.e. physical rotation angle `alpha t/2` each.

### Lane C — induced spin-j first subleading matrix

For exact spins `j in {1/2,1,3/2,2}`, construct standard `J_y,J_z`, the primitive leading matrix `C`, and radial subleading matrix

`D=C(i gamma J_z)`.

PASS iff the first mixed coefficient

`T_1=-i(alpha/2)J_y C + D - i(alpha/2) C J_y`

obeys exactly

`T_1 C^-1 = -i(alpha/2)J_y + i gamma J_z - i(alpha/2) C J_y C^-1`.

The first two relative terms must be standard Lie generators. Setting `alpha=0` must reduce exactly to the pure boost relative operator `i gamma J_z`.

The final conjugated `C J_y C^-1` term must be non-scalar relative to `J_y` for every frozen `j>=1`; the `j=1/2` one-step special case is retained as a control.

### Lane D — exact boundary survival and controls

Use the same seven exact 4-valent intertwiner controls as Iter076V-W-X. Form the leading outgoing tensor

`F_z=(tensor C) iota`.

The mixed path survivor after standard node-common generator closure is

`-(i alpha/2) F_z sum_e J_y^(e)`.

PASS iff:

- this mixed survivor vanishes for exactly the two `(1/2)^4` controls;
- it is nonzero for exactly the other `5/7` controls;
- setting `alpha=0` kills the mixed survivor for all `7/7` controls;
- multiplying any individual edge leading `C` by a nonzero common branch scale does not change its zero/nonzero classification;
- the aggregate records:
  - `concrete_mixed_source_path_feeds_normal_connection=true`;
  - `mixed_survival_generic_controls=5`;
  - `iter076W_pure_direction_zeros_unchanged=true`;
  - `ordinary_full_source_onejet_established=false`;
  - `physical_source_to_K4_curvature_selected=false`;
  - `epsilon_minus1_coefficient_established=false`;
  - no generic finite-spin signed P3 or G3/F9/G8/K5 promotion.

## PASS classification

`ITER076Y_MIXED_POLAR_KAK_JET_FEEDS_HALF_ANGLE_TOLLER_CONNECTION_SURVIVING_GENERIC_INTERTWINERS_EXACT_SCOPED`

## Scientific meaning on PASS

The normal-bundle connection of Iter076X is physically reachable inside the source group carrier: a concrete mixed compact/boost path produces it at first subleading radial order with exact coefficient `alpha/2`. The separate pure-direction zeros of Iter076W therefore cannot be promoted to a zero mixed factorized germ.

The surviving term is still a source-group/blow-up datum, not the physical reduced K4 coefficient. The next task is to encode this connection covariantly in the full source relative-coordinate cut complex and determine what extra data are required to transport it through the cut-to-cycle/Hodge bridge.

## FAIL classification

`ITER076Y_MIXED_POLAR_KAK_CONNECTION_ENTRY_CONFIRMATION_FAIL`

A failure is an exact local group/KAK result, not a physical finiteness/divergence theorem.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no ordinary full source one-jet; no physical nonlinear source-to-K4 map; no nominal `epsilon^-1` coefficient; no physical causal-vertex finiteness/divergence theorem; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; retain the source spectral `i epsilon` prescription.