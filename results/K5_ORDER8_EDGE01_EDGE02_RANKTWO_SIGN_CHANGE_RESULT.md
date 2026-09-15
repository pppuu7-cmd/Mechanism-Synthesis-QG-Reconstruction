# K5 order-8 edge01/edge02 rank-two exact sign change — terminal result

Date: 2026-09-16

## Authority

Prospective gate:

`prereg/K5_ORDER8_EDGE01_EDGE02_RANKTWO_POSITIVITY_LANE.md`, commit `ef26d063354d0def5af3fdba4fe0d8b537a038d1`.

Post-prereg derivation:

`sources/K5_ORDER8_EDGE01_EDGE02_RANKTWO_SIGN_CHANGE_DERIVATION.md`, commit `b427ddaf39636359898d498d90277dc89c593f06`.

Validator:

`scripts/k5_order8_edge01_edge02_ranktwo_sign_change.py`, commit `c14b8fe2148be20d5bcd62f45065cc909bd302ff`.

Production:

- workflow/head: `6fb57d915cbb20c80674ec2a97121b35ffedd396`;
- run: `35035152999`, terminal `success`;
- job: `104602503455`, terminal `success`;
- artifact: `10422859073`;
- artifact ZIP digest: `sha256:b409c5dfb8c1182da8bcab903a800955c8a34462a179c841f08d511d55625867`;
- production JSON SHA256: `c3abbcaf61bafc13eea2677ce71537d5899e375b3571e513abc1e94a0287a31f`;
- status: `PASS_EXACT_SCOPED`;
- classification: `K5_EDGE01_EDGE02_RANKTWO_SIGN_CHANGE_EXACT_SCOPED`.

All frozen implementation checks and all adversarial controls passed.

## Exact result

Use the authoritative K5 edge order

`(01),(02),(03),(04),(12),(13),(14),(23),(24),(34)`

with

`alpha_01=t`, `alpha_02=u`, all remaining Schwinger weights equal to one, `t,u>0`.

The uniform two-edge covariance Gram matrix is exactly

`[[2/5,1/5],[1/5,2/5]]`.

The reduced weighted-Laplacian determinant is the exact positive polynomial

`det L(t,u)=5*(3tu+7t+7u+8)`.

Thus the two witnesses below lie strictly inside the positive Schwinger cone and the sign change is not caused by a determinant singularity.

The independent edge02 source contraction retains all `1024` source node-tensor choices and gives

`F_02(z)=128/625 - (1024/3125)z + (1984/15625)z^2 - (896/78125)z^3`,

with all higher coefficients through degree five exactly zero. Equivalently,

`F_02(z)=-(64/78125)(2z-5)(7z^2-60z+50)`.

The corresponding order-eight radial slice is

`R(1,u)=1344 P_02(u) / [78125(2u+3)^7]`,

where

`P_02(u)=15347529 + 18446466u + 6476985u^2 - 1743180u^3 - 2084965u^4 - 625974u^5 - 66861u^6`.

Production independently recomputed all nine prospectively frozen rational points with the full general-L order-four Wick engine. All nine are positive-definite and all nine frozen sample values are positive.

However the post-prereg exact counterexample is negative:

`R(1,2)=1254383808/9191328125 > 0`,

`R(1,3)=-14327118848/13839609375 < 0`.

The positive witness `(1,2)` is one of the prospectively frozen cross-check points. Both values were independently reproduced by the specialized source-derived slice engine and by the full general-L engine.

Therefore

`K5_EDGE01_EDGE02_RANKTWO_SIGN_CHANGE_EXACT_SCOPED`.

## Controls

The same classifier/validator also establishes:

- all `1024` source choices are present;
- all nine preregistered direct cross-check points were evaluated exactly;
- all ten full-engine points, including the negative witness, have positive-definite Laplacians;
- the rank-two determinant polynomial is reconstructed exactly;
- the edge02 source polynomial is reconstructed independently from the source tensors;
- a synthetic genuinely-positive fixture reaches the positive branch of the same decision path;
- removing one source term (`1023` instead of `1024`) is rejected;
- flipping one exact `F_02` coefficient changes the witness and is rejected by the independent full-engine cross-check;
- the sign change is not promoted to a full projective-period verdict.

## Scientific consequence

The successful one-dimensional edge01 positivity theorem does **not** extend to the two-edge positive Schwinger cone. A globally pointwise-positive certificate for the frozen `00000` radial integrand is therefore impossible already on the exact two-parameter family.

This kills the mechanical strategy `rank-one positivity -> rank-two positivity -> ... -> full-cone positivity`.

It does **not** imply that the full 9-dimensional K5 projective period is zero. A sign-changing projective integrand can integrate to a nonzero value. It also does not prove that the period is nonzero.

The high-information successor is exact projective integration/noncancellation in the two corrected S5-invariant **dual** boundary channels, using projective parameter-space IBP/symmetry/annihilator methods or another rigorous period-evaluation certificate. Higher-rank pointwise-positivity lanes are no longer the preferred frontier.

## Locks

No K5 full order-eight zero/nonzero theorem; no physical finite part or selector; no regulator-independence theorem; no global all-strata patching; no causal multivertex conclusion; no G3/F9/G8 promotion; no `NEW_PHYSICS_FOUND`; no complete-QG claim. Retain the published one-wedge spectral `i epsilon`.