# Iter076Q result — Hodge-line Sym2 quadratic descent

**Date:** 2026-09-13

## Authority

- preregistration: `be8538017835b7a34dafd7340bbadfb07358f46c`
- implementation: `68d34c0f7a4ee240d1f5508a94194bd3d9d15626`
- production/workflow head: `9e067f74c8087b7d91cd88ae8818ed1edd84af28`
- run: `34782102274`
- aggregate job: `103790900275`

Raw artifacts:

- A: `10325462127`, digest `sha256:f95a43f03cff007b64ae4501afca83d37573895a6e28cb9a74c03a44986aa74b`
- B: `10324738059`, digest `sha256:7d2ea597f9a4cfcb666b60b73a4c67381baacd55b98200b65d00f22d30dff4e4`
- C: `10325640317`, digest `sha256:7a3e0b1d2ca5b79d84c502737ff948a09312556b715874ba92fb801dc4a7f5fd`
- D: `10324824440`, digest `sha256:f6099140a474eea68bd9aa83af41b2090014cf08e7d5d5dbb6e82e408be1aec1`
- aggregate: `10324959288`, digest `sha256:33b461b58d7b9b7e56f6cf32e175b7b883ef3d45a9e2c2a4543b8ef12785a5af`

All lanes A/B/C/D and the aggregate completed successfully.

## Frozen classification

`ITER076Q_HODGE_LINE_DESCENDS_TO_UNTWISTED_SYM2_QUADRATIC_TRANSPORT_EXACT_SCOPED`

## Exact content

The exact linear cut-to-cycle Hodge map `X` retains the sign-twisted covariance

`Z(pi) X = sgn(pi) X C(pi)`

for all 24 elements of `S4`, with both representatives `+X` and `-X` retained.

Passing to homogeneous degree two removes the global sign:

`Sym2(+X) = Sym2(-X)`.

The induced `Sym2(X)` is full rank (`6`) and unimodular in the frozen monomial bases. For every permutation,

`Sym2(Z(pi)) Sym2(X) = Sym2(X) Sym2(C(pi))`

with no parity factor. A deliberately unsquared linear control retains the twist on all 12 odd permutations.

## Scope

This establishes only that the unresolved global sign of the exact linear Hodge line is irrelevant for **homogeneous quadratic transport**.

It does not establish the physical source-to-K4 pushforward. In particular, if the actual source-to-cycle coordinate map has quadratic curvature and the source numerator/density has a nonzero one-jet, the one-jet can feed the degree-two coefficient after coordinate change. Therefore the physical numerator/Haar-Jacobian degree-two jet and the nominal `epsilon^-1` coefficient remain open.

## Next admissible gate

Audit prospectively whether:

1. the relevant source numerator/Haar-Jacobian one-jet vanishes; or
2. symmetry forces any nonlinear source-to-cycle curvature contribution from that one-jet to vanish in the physical channel.

No vanishing may be inferred merely from the reduced denominator-skeleton cancellation of Iter074A.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no generic finite-spin signed P3; no physical causal-vertex finiteness/divergence theorem; no nominal `epsilon^-1` coefficient; no G3/F9/G8/K5 promotion; retain the published spectral `i epsilon` prescription.
