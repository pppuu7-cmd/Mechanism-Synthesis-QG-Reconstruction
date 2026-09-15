# Iter083F-SM — common finite spectral epsilon does not regularize the K5 common collision

Date: 2026-09-15

Status: **PASS_EXACT_SCOPED**

## Prospective provenance

- preregistration: `prereg/ITER083F_SM_COMMON_SPECTRAL_EPSILON_NOT_K5_COLLISION_REGULATOR.md`, commit `18fbeca191aa05fe09e3e38ed60abec53e09a8c9`;
- public-source lock: `sources/ITER083F_PUBLIC_SOURCE_LOCK.md`, commit `d69eb1b5c187be257c507cdc3527ec4f9e824c97`;
- machine-readable source lock: `sources/raw/iter083f_finite_epsilon_source_lock.json`, commit `66c9a80ca6cecc59131deccca5d6e37a7ef57011`;
- theorem derivation: `sources/ITER083F_SM_COMMON_SPECTRAL_EPSILON_COLLISION_SCALING_DERIVATION.md`, commit `464e54abfb63aa123ff9a6614fc033d98274b733`;
- validator: `scripts/iter083f_common_spectral_epsilon_collision_test.py`, commit `8094d15e62e285da0733852c80386c380fb7451a`;
- workflow/head: `.github/workflows/iter083f_common_spectral_epsilon_collision_test.yml`, commit `d5778a6bc93e5b3b6e129f579299be5a1f0a1b28`;
- GitHub Actions run `34912148095`, terminal success;
- job `104201783021`, terminal success;
- artifact `10374589062`, `iter083f-common-spectral-epsilon-collision-test`;
- artifact ZIP digest `sha256:7f64b3a817ea89cdef21bf75ef001f8afc1699c77fdcb661164e889f0cca45e0`;
- production JSON SHA256 `9242bfeea498e8634bec469ca52907eb1852ec60d9e56c200af4dee2d6e55fa6`.

## Classification

`ITER083F_SM_COMMON_FINITE_SPECTRAL_EPSILON_DOES_NOT_REGULARIZE_K5_COMMON_COLLISION_EXACT_SCOPED`

Verdict: **`PASS_EXACT_SCOPED`**.

## Candidate regulator tested

The published causal vertex takes the one-wedge Feynman `epsilon->0+` limit before forming the ten-Toller K5 product. Iter083F tests a deliberately new construction suggested after Iter083E:

1. keep the spectral Feynman parameter `epsilon>0` finite in every one-wedge Toller contour;
2. use the same finite epsilon in all ten wedges;
3. form the boundary-contracted K5 product/group object first;
4. ask whether finite epsilon has made the simultaneous compact collision locally integrable before any `epsilon->0` limit.

No beta/group-normal cutoff or subtraction is added.

## Exact finite-epsilon contour identity

The Toller kernel cancels all Toller poles. Therefore at fixed admissible `epsilon>0`, before taking the source limit,

`I_epsilon^+[d] = P_jl(rho+i epsilon;rho) t^+(rho+i epsilon,beta)`,

`I_epsilon^-[d] = P_jl(rho-i epsilon;rho) t^-(rho-i epsilon,beta)`.

The opposite-branch contour contains no shifted Feynman pole and vanishes. This uses the same contour/asymptotic argument as the published projector but stops before `epsilon->0`.

## Exact j=1/2 kernel cancellation

For the physical frozen minimal-spin sector,

`j=l=k=1/2`, `rho=gamma/2`.

Eq. (16) gives

`P_(1/2,1/2)(rho_tilde;rho)=(rho_tilde^2+1/4)/(rho^2+1/4)`.

Every Table-II `j=1/2` Toller branch contains the denominator

`rho_tilde^2+1/4`.

At `rho_tilde=rho+-i epsilon` the Toller kernel therefore cancels that entire shifted denominator exactly. Production checks the formal Gaussian-rational polynomial identity

`(i z+1/2)(i z-1/2)=-(z^2+1/4)`

and exact shifted-denominator cancellation without floating-point fitting.

## Four finite-epsilon branches

For `m=+1/2`,

`I_epsilon^+[d] = - exp(+i rho beta) exp(-epsilon beta) / [2(rho^2+1/4)sinh(beta)^2]`,

`I_epsilon^-[d] = + exp(-i rho beta) exp(-epsilon beta) [cosh(beta)+2 i rho sinh(beta)+2 epsilon sinh(beta)] / [2(rho^2+1/4)sinh(beta)^2]`.

For `m=-1/2`,

`I_epsilon^+[d] = + exp(+i rho beta) exp(-epsilon beta) [cosh(beta)-2 i rho sinh(beta)+2 epsilon sinh(beta)] / [2(rho^2+1/4)sinh(beta)^2]`,

`I_epsilon^-[d] = - exp(-i rho beta) exp(-epsilon beta) / [2(rho^2+1/4)sinh(beta)^2]`.

At every fixed finite epsilon,

`exp(-epsilon beta)=1+O(beta)`,

`cosh(beta)=1+O(beta^2)`,

`sinh(beta)=beta+O(beta^3)`.

Hence all four branches retain a nonzero `beta^-2` leading term. Their leading signs are exactly

- `(+,m=+1/2): -1`;
- `(+,m=-1/2): +1`;
- `(-,m=+1/2): +1`;
- `(-,m=-1/2): -1`.

The leading coefficient magnitude is

`1/[2(rho^2+1/4)]`.

With `rho=gamma/2`,

`|c|=2/(1+gamma^2)`.

This is exactly the same leading magnitude as the source Toller branch after the epsilon limit. The finite spectral epsilon changes subleading terms only.

## Full matrix and ten-wedge scaling

In ascending `m=(-1/2,+1/2)` order, the plus branch retains leading reduced matrix

`diag(+1,-1) * [2/(1+gamma^2)] beta^-2`,

while the minus branch is its negative. Restoring the finite SU(2) Cartan factors therefore yields the same leading angular matrix frozen in Iter077I, with no epsilon-dependent leading deformation.

On the same nonzero K5 angular witness, each of the ten wedges contributes order `r^-2`, so the common finite-epsilon ten-wedge product has

`C_kappa r^-20 + O(r^-19)`, `C_kappa !=0`,

with the same leading tensor as at epsilon zero up to the already-frozen branch sign product.

Thus the fixed-epsilon transverse scaling degree remains exactly 20.

## Local integrability

The common-collision normal codimension is 12. The normal radial measure contributes `r^11 dr`, so the leading fixed-epsilon radial behavior is

`r^(11-20) dr = r^-9 dr`.

This is not locally integrable at `r=0`.

Therefore **finite spectral epsilon does not even regularize the K5 common collision before regulator removal**.

The reason is structural: epsilon shifts the representation spectral pole and produces factors like `exp(-epsilon beta)`, but

`exp(-epsilon beta) -> 1`

at the group collision `beta->0`. It is not a UV damping factor in the collision-normal variable.

## Relation to Iter083B/E

Iter083E established that the published one-wedge epsilon prescription does not select the joint K5 extension because it is already taken before the ten-factor product.

Iter083F is stronger against the simplest reversed-order proposal: even if the same spectral epsilon is held finite across all ten wedges and the product is formed first, the common collision remains non-integrable with the same scaling degree.

Consequently the 377-dimensional Iter083B extension problem is not eliminated merely by keeping the existing spectral epsilon finite. An extension/renormalized multiplication is still required at each fixed epsilon unless additional genuinely joint structure is supplied.

## Production controls

All P0-P7 and all eight negative controls passed.

Production explicitly rejects:

- replacing the source factor by fictitious `exp(-epsilon/beta)` damping;
- shifting the group-normal rapidity `beta` instead of spectral `rho`;
- dropping the Toller kernel and retaining a spurious shifted denominator;
- treating the common-epsilon construction as published source authority;
- relying only on the Barrett-Crane `j=0` example;
- taking epsilon to zero before testing finite-epsilon collision scaling.

## Remaining legitimate joint prescriptions

This result rules out only the simplest reuse of the existing **spectral** epsilon as a common K5 collision regulator. It leaves open prescriptions that actually act on the joint singularity, including:

- group-normal/radial regularization;
- analytic regularization of collision scaling exponents;
- several-complex-variable boundary values;
- microlocal/renormalized multiplication with a normalization law;
- composition/gluing, differential, positivity or RG constraints acting on `F_8`.

## Interpretation ceiling

No causal-vertex distributional nonexistence/divergence theorem follows: a non-locally-integrable function can still admit renormalized distributional extensions. No generic-spin completeness, all-strata global patching, regulator dependence/independence, multivertex E3/E4/E6 closure, G3/F9/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete-QG claim follows.
