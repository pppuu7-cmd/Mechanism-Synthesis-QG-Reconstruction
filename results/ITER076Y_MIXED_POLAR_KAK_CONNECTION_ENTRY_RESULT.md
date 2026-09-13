# Iter076Y result — concrete mixed polar/KAK path feeds the half-angle Toller connection

**Date:** 2026-09-13

## Authority

- source/derived supplement: `f26a998dcf0a7889e6aa68cdf2ac6fc2624058d0`
- prospective preregistration: `ddb19be25386bf9c4a0622733d8b393809a7cbb8`
- implementation: `0edaba2df2095a822e788ae622f5819317969f40`
- production/workflow head: `c8b030f6a30585282485ef33a6179f546a7755c9`
- authoritative run: `34783973208`
- jobs: A `103795982352`, B `103795982237`, C `103795982243`, D `103795982384`, aggregate `103796030454`

Artifacts:

- A `10326275405`, `sha256:a1d0e00c65f7ce6685802746f99f3239c70c2299d057b6b8685083017097d9f1`
- B `10326191347`, `sha256:af640be7378e40fc46529ab07317e824a50bbf080048b2befb11ee142108cc64`
- C `10325911933`, `sha256:e764a4129b2d30b7e337877bffd4106ad3cfb427b1187b0df8e15cc2f13491c2`
- D `10326350328`, `sha256:2ae61d93b5ff079e1112bfa18b32af827a3f79ff889919bc451c40633c7495f6`
- aggregate `10326041750`, `sha256:bc6d48f02a06e615b251e078ee97a228c01eedfd356f4106feab5e5313ca20ae`

All frozen lanes A/B/C/D and aggregate completed successfully.

## Frozen classification

`ITER076Y_MIXED_POLAR_KAK_JET_FEEDS_HALF_ANGLE_TOLLER_CONNECTION_SURVIVING_GENERIC_INTERTWINERS_EXACT_SCOPED`

## Exact mixed polar/KAK jet

In the defining representation, for

`B=sigma_z/2`, `A=-i alpha sigma_y/2`,

`g(t)=exp[t(A+B)]`,

the exact second-order polar jet gives

`log(g^dagger g)=2tB-t^2[A,B]+O(t^3)`,

`[A,B]=alpha sigma_x/2`,

`log p=tB-(t^2/2)[A,B]+O(t^3)`.

Thus the boost radius obeys `beta=t+O(t^3)` while the boost-normal direction is

`n(t)=z-(alpha/2)t x+O(t^2)`.

With

`R(t)=exp(+i alpha t sigma_y/4)`,

the positive factor is

`p=R exp(tB) R^(-1)+O(t^3)`.

The unitary polar factor has `log u=tA+O(t^3)`, and the compatible Cartan factors both have first derivative

`U_1'(0)=U_2'(0)=-i alpha sigma_y/4`.

Therefore the original compact rotation angle is split equally: each compact Cartan factor carries `alpha t/2` at first order.

## Induced Toller subleading matrix

For the gamma-simple reduced branch

`t_red=t^(-n)[C+tD+o(t)]`, `D=C(i gamma J_z)`,

the full mixed-path matrix has

`T=t^(-n)[C+tT_1+o(t)]`,

`T_1=-i(alpha/2)J_y C + D - i(alpha/2)C J_y`.

After right factoring `C`,

`T_1 C^(-1)=-i(alpha/2)J_y+i gamma J_z-i(alpha/2)C J_y C^(-1)`.

The first two relative terms are standard common node generators and are removed by the exact intertwiner closure mechanisms already closed in Iter076V/W. The last term is the nontrivial leading-matrix angular response identified in Iter076X.

Setting `alpha=0` reduces exactly to the pure boost relative operator `i gamma J_z`.

## Boundary survival

For the same seven exact 4-valent intertwiner controls, the surviving mixed term is

`-(i alpha/2) F_z sum_e J_y^(e)`,

where `F_z=(tensor C)iota` is the outgoing leading tensor.

Exact census:

- `2/7` controls vanish: the two `(1/2,1/2,1/2,1/2)` intertwiners;
- `5/7` controls survive exactly;
- `alpha=0` kills the mixed survivor for all controls;
- changing a nonzero individual leading branch scale does not change the zero/nonzero classification.

Thus the normal-bundle connection of Iter076X is reached by a concrete source-group path with exact coefficient `alpha/2`.

## Scientific consequence

The separate pure-direction zeros of Iter076W cannot be promoted to a zero mixed factorized germ. A genuine mixed compact/boost source path feeds the matrix-valued normal-direction connection at the first subleading radial order, and that contribution survives generic boundary-intertwiner contraction in the frozen exact controls.

This surviving datum is local to the source group/blow-up geometry. It is not yet the reduced physical K4 numerator coefficient and is distinct from the nonlinear source-to-K4 curvature channel identified in Iter076R-S.

## Next admissible gate

Audit whether a single ordinary `C^1` factorized extension through the identity can be compatible simultaneously with:

1. the exact compact-gauge/pure-direction zeros of Iter076W, and
2. the nonzero mixed directional coefficient of this iteration.

If linearity of an ordinary Frechet derivative is incompatible with these source-backed directional data, the smooth source-jet premise must be replaced by a blow-up/polyhomogeneous boundary object before any physical `epsilon^-1` coefficient can be defined.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no ordinary full source one-jet; no physical nonlinear source-to-K4 map; no nominal `epsilon^-1` coefficient; no physical causal-vertex finiteness/divergence theorem; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; retain the source spectral `i epsilon` prescription.