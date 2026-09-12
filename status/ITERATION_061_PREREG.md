# Iteration 061 preregistration — orientation-blind kappa→spectral-sign identification audit

Preregistered prospectively after terminal Iter060 and before any Iter061 production result.

## Motivation
Current source-backed objects distinguish:
- physical causal wedge data `kappa_ab = sigma_a sigma_b`, symmetric under exchanging the unordered face labels `a,b` in the existing causal sign-class map;
- orientation-dependent Toller spectral branch sign, which Iter059 proves flips `T+ <-> T-` under group inversion / wedge-order reversal.

The next bridge question is whether one may identify the two signs directly without an additional orientation datum. This must be decided before using physical causal classes as tournament selectors.

## Frozen object and domain
Use the K4 restriction of the existing source-backed causal classes:
- vertices `{0,1,2,3}`;
- gauge global sigma flip by `sigma_0=+1`;
- all `2^3=8` physical sigma classes;
- six unordered edges;
- two candidate orientation-blind identifications only: `s_ab = kappa_ab` and `s_ab = -kappa_ab`.

## Frozen tests
For each physical class and candidate identification:
1. construct `kappa_ab=sigma_a sigma_b` on unordered edges;
2. verify kappa is unchanged under swapping the order of the same wedge labels;
3. apply source-backed full wedge-order reversal from Iter059, which requires spectral branch sign `s -> -s` on every edge;
4. test whether the orientation-blind identification recomputed from unchanged kappa equals the required reversed spectral sign;
5. independently check the abstract edge-local theorem: no function `f:{-1,+1}->{-1,+1}` that depends only on unordered kappa can satisfy both `s=f(kappa)` and reversal covariance `f(kappa)=-f(kappa)`.

## Frozen classifiers
- `ITER061_SOURCE_OR_IMPLEMENTATION_INVALID`
- `K4_ORIENTATION_BLIND_KAPPA_SPECTRAL_IDENTIFICATION_COMPATIBLE`
- `K4_ORIENTATION_BLIND_KAPPA_SPECTRAL_IDENTIFICATION_OBSTRUCTED`

## Interpretation rule
If obstructed, the result only proves that an orientation-blind direct identification of physical kappa with the spectral pole sign is impossible under the jointly frozen source laws. It does not rule out an orientation-sensitive bridge `s = eta(a,b,order,...) * kappa`, does not select eta, and does not establish a physical causal sector, contour, finiteness/divergence, K5, G3, F9, G8, or new physics.
