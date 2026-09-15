# K5 order-8 edge01/edge02 rank-two exact sign-change derivation

Date: 2026-09-16

Prospective parent gate: `prereg/K5_ORDER8_EDGE01_EDGE02_RANKTWO_POSITIVITY_LANE.md`, commit `ef26d063354d0def5af3fdba4fe0d8b537a038d1`.

Status: POST-PREREG EXACT DERIVATION. The sign witnesses below were obtained only after the rank-two gate and its outcome taxonomy were frozen. They must be checked independently by the full general-L exact engine before becoming scientific authority.

## 1. Frozen two-edge family

Use the authoritative K5 edge order

`(01),(02),(03),(04),(12),(13),(14),(23),(24),(34)`

and set

`alpha_01=t`, `alpha_02=u`, all other `alpha_e=1`, with `t>0`, `u>0`.

The boundary component used in the rank-one predecessor and here is the stripped component `k=(0,0,0,0,0)`, retaining all `4^5=1024` source node-tensor choice terms. This is a source-faithful component-level noncancellation lane inside the already-authorized full-32 K5 object; it is not a replacement for the full boundary tensor.

Let `L0=L(1,...,1)` be the reduced uniform K5 Laplacian and let `r_01,r_02` be the two authoritative incidence rows. Their exact uniform covariance Gram matrix is

`G = [[2/5,1/5],[1/5,2/5]]`.

Write `h=t-1`, `k=u-1`. With the radial insertion parameter encoded as `a=1+s/5`, the rank-two update is

`L(t,u;s)=a L0 + h r_01 r_01^T + k r_02 r_02^T`.

Woodbury gives an exact rational inverse. The corresponding 2x2 denominator is

`d(a,h,k)=a^2 + (2/5)a(h+k) + (3/25)hk`.

At `s=0`,

`25 d(1,h,k) = D(t,u) = 3tu + 7t + 7u + 8`.

For every `t,u>0`, `D(t,u)>0`. The reduced determinant is exactly

`det L(t,u)=5 D(t,u)`.

Hence no sign statement below comes from a determinant singularity or a boundary point of the positive Schwinger cone.

## 2. Exact bivariate rational object

The leading numerator has degree ten, so its Gaussian Wick contraction is degree five in the covariance. Combining the rank-two Woodbury inverse with the determinant factor and four radial derivatives defines an exact rational radial moment `R(t,u)` on the complete open quadrant.

After clearing the positive determinant denominator, the exact object has the structural form

`R(t,u) = 672 P(t,u) / [15625 D(t,u)^8]`,

where `P(t,u)` is an exact integer bivariate polynomial. The implementation reconstructs/evaluates this rational object with exact `Fraction` arithmetic from all 1024 source choices and cross-checks it against the independent full general-L order-four series engine at all prospectively frozen rational points plus the sign-changing witness below.

The full bivariate coefficient table is not needed to establish the preregistered `SIGN_CHANGE` outcome: because the denominator is strictly positive on `t,u>0`, two independently verified exact rational values of opposite sign are decisive.

## 3. Exact t=1 slice

On the interior slice `t=1`, only the `02` covariance is deformed from the uniform point. Repeating the exact source contraction on that slice gives the rank-one source polynomial

`F_02(z)=-(64/78125)(2z-5)(7z^2-60z+50)`.

The actual order-eight radial-probe moment is

`R(1,u)=1344 P_02(u) / [78125(2u+3)^7]`,

with

`P_02(u)=15347529 + 18446466 u + 6476985 u^2 - 1743180 u^3 - 2084965 u^4 - 625974 u^5 - 66861 u^6`.

This is not sign-definite on the positive axis. In particular,

`P_02(2)=6533249 > 0`,

while

`P_02(3)=-287821584 < 0`.

Therefore the two exact rational witnesses are

`R(1,2)=1254383808/9191328125 > 0`,

`R(1,3)=-14327118848/13839609375 < 0`.

The point `(1,2)` is one of the nine prospectively frozen direct cross-check points. The point `(1,3)` is a post-prereg counterexample witness and is admissible because the frozen outcome taxonomy explicitly assigns `SIGN_CHANGE` when independently verified positive and negative rational witnesses exist.

## 4. Scientific consequence inside the frozen gate

If the full general-L exact engine reproduces both witness values and all preregistered source/provenance/positive-definiteness controls pass, the frozen gate classification is

`K5_EDGE01_EDGE02_RANKTWO_SIGN_CHANGE_EXACT_SCOPED`.

This falsifies a globally pointwise-positive certificate for boundary component `00000` on the complete positive rank-two Schwinger family. In particular, the successful edge01 one-dimensional positivity theorem cannot be extended to the two-edge positive cone by continuity or symmetry.

The sign change does **not** imply that the 9-dimensional projective period vanishes. A sign-changing integrand can have a nonzero integral. It also does not assign the parent K5 order-eight zero/nonzero verdict.

## 5. Interpretation ceiling

No K5 full-period zero/nonzero theorem; no physical finite part or selector; no regulator-independence result; no causal multivertex result; no G3/F9/G8 promotion; no `NEW_PHYSICS_FOUND`; no complete-QG claim. The published one-wedge spectral `i epsilon` remains unchanged.

After a terminal `SIGN_CHANGE` result, further rank-three/rank-four pointwise-positivity lanes have low information value. The admissible high-value successor is exact projective integration/noncancellation (for example invariant-dual IBP/symmetry evaluation), because pointwise sign-definiteness is already falsified.