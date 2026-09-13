# Iter077F-SM result — all-spin-half rank-9 contact reaches a nonunique n_eff=3 scaling channel

**Date:** 2026-09-14

## Authority

Stable alias: `Iter077F-SM`.

- source/derived scaling supplement: `7606b7697c80859ff300199bac21c3ea3705fd76`
- prospective preregistration: `5d8a7d51f0c87a50c6f94de3a8bb1ec2c7689259`
- implementation: `cd95d2fba1e884e6f110a370e63381829d0981b0`
- production/workflow head: `8b67eb90cf38d81ff6c63bb8e9145b6d66cb4ccf`
- authoritative run: `34785560537`
- jobs: A `103800283759`, B `103800283686`, C `103800283713`, D `103800283737`, aggregate `103800333026`

Artifacts:

- A `10326391883`, `sha256:049163aefa42a7ad60f97cd876bc0aba6be5e912959dc1cc92780e825366b914`
- B `10326531510`, `sha256:6c86fd0eee7fa6ca8fbeaf926896b32b0ea829e90cc11b7559a75b801c8d54ab`
- C `10326652124`, `sha256:b5fb46b37c97cc81f5215f06e4d1bae0d63e67e525e4a4aa6b0cccb9b1d9d1bf`
- D `10326143861`, `sha256:8b1051ed5ae219e09e1b6910ce0094c3148521d372d406461792441e00057af7`
- aggregate `10326721126`, `sha256:b955e2ad1701cb672560b31dfda8c19c2fa3667350f46a4d17e1cf3318f7d341`

All frozen lanes A/B/C/D and the aggregate completed successfully.

## Frozen classification

`ITER077F_SM_ALL_SPIN_HALF_RANK9_CONTACT_REACHES_N3_SCALING_NONUNIQUENESS_SOURCE_I_EPSILON_EXTENSION_REQUIRED_EXACT_SCOPED`

## Exact all-spin-half contact coefficient

For `j=1/2`, the exact contact distribution is

`delta^(rho,1/2)(x) = -delta(x) + [rho/(rho^2+1/4)] delta'(x)`.

With gamma-simple `rho=gamma/2`,

`a_gamma = 2 gamma/(1+gamma^2)`.

This is nonzero for every finite real `gamma != 0`.

## Frozen self-stress excess order

At the `Iter077C-SM` rank-9 self-stress

`lambda=(1,-1,0,0,1,0,0,0,0,0)`,

only edges `01`, `02`, `12` have nonzero self-stress weight. After choosing target coordinate `s=lambda.B`, only those three wedge derivatives can feed `partial_s`.

In the all-spin-half ten-contact product the highest pure excess order is therefore exactly

`n_eff=3`.

The unique pre-contraction order-3 term chooses the delta-prime component on `01`, `02`, `12` and the ordinary delta component on the other seven wedges. Its exact coefficient is proportional to

`-8 gamma^3/(1+gamma^2)^3`,

up to the nonzero product of causal signs and an invertible target-coordinate Jacobian convention. It is nonzero for finite real `gamma != 0`.

No wedge outside the self-stress support can generate `partial_s`, so there is no second all-spin-half target term of the same highest excess order available for a pre-contraction cancellation.

This does not exclude cancellation after the exact smooth Toller phases, CP1 integrations and boundary intertwiner contraction.

## Six-dimensional scaling threshold

`Iter077D-SM` gives a nondegenerate quadratic normal form `q` in six transverse dimensions. For the punctured critical neighborhood,

`sd[delta^(n)(q)] = 2(n+1)`.

Therefore:

- `n=0`: scaling degree `2 < 6`, unique local extension;
- `n=1`: scaling degree `4 < 6`, unique distributional extension;
- `n=2`: scaling degree `6`, first marginal extension ambiguity;
- `n=3`: scaling degree `8 > 6`, nonunique by scaling alone, with critical-origin supported ambiguity through total derivative order at most `2` before additional source symmetries/prescriptions are imposed.

The ordinary `delta(q)` channel is therefore not itself a fatal obstruction. The exact all-spin-half source contact product, however, reaches the nonunique `n_eff=3` regime.

## Refined missing object

The first concrete local missing object is now

`SOURCE_SELECTED_CORRELATED_I_EPSILON_EXTENSION_OF_RANK9_N_EFF_3_CONTACT_CHANNEL`.

For the full K5 handoff this sits inside the broader missing object

`SOURCE_SELECTED_CORRELATED_I_EPSILON_K5_EXTENSION_AND_FULL_CONTRACTION`.

The source spectral `i epsilon` prescription may select a unique correlated extension. Scaling degree alone does not. Arbitrary fitted counterterms/finite parts remain forbidden.

## Scientific consequence

The distributional funnel is no longer blocked by an unspecified singularity. It is split into:

1. generic rank-10 region — canonical local pullback;
2. tested rank-9 geometry — exact codimension-3 self-stress locus with nondegenerate mixed quadratic normal form;
3. ordinary `n=0` critical contact — unique local extension;
4. all-spin-half highest self-stress contact `n_eff=3` — nonunique by scaling alone;
5. remaining required work — derive the correlated source-selected `i epsilon` extension, perform full CP1/Toller/intertwiner contraction, and cover the remaining exceptional strata before any global K5/regulator-removal theorem.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no causal-vertex finiteness/divergence theorem; no assertion that the source-selected `i epsilon` extension is nonunique; no arbitrary counterterm; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal `epsilon^-1` coefficient; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion.