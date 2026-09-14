# Iter080A-SM — K5 finite-permutation covariance versus tangential extension ambiguity

**Date:** 2026-09-14

## Provenance

- Prospective preregistration: `prereg/ITER080A_SM_K5_FINITE_PERMUTATION_SYMMETRY_SELECTOR_PREREG.md`, commit `19f03d40929c7f7fc7aa9c82eed6485646028876`.
- Implementation: `analysis/iter080a_sm_k5_finite_permutation_selector.py`, commit `eaef2c647c338767622187b293b0b3f476b60103`.
- Production workflow/head: `.github/workflows/iter080a_sm_k5_finite_permutation_selector.yml`, commit `431e3cc4056c06885cf0ba4c468ff886ba2bb9a3`.
- Authoritative terminal Actions run: `34820372854`.
- Lane jobs: A `103900365276`, B `103900365214`, C `103900365168`, D `103900364995`; all terminal-successful.
- Aggregate job: `103900533687`.
- Aggregate artifact: `10337479168`, digest `sha256:981c7a994ee481fbe3663c66054cfb1ea7a956933f4f5452f480c8cd1eb5dcce`.
- Durable raw aggregate: `results/ITER080A_SM_K5_FINITE_PERMUTATION_SELECTOR_RAW.json`, commit `58cb5eef07f36956d31745152f1b3f99e338b358`.

Green CI is execution evidence only. The scientific conclusion below follows from the prospectively frozen exact construction plus the exact rank/invariance checks.

## Frozen object

The gate acts only on the already authoritative Iter077Q smooth tangential supported-ambiguity sector over the actual common-collision manifold

`N = SU(2)^4 subset SL(2,C)^4`

after fixing one K5 group variable. It tests whether finite K5 vertex relabeling/permutation covariance alone can collapse that ambiguity to a unique or finite-dimensional extension. It does not define a distributional extension and does not introduce a regulator.

## Exact witness

Before gauge fixing define

`F(g_1,...,g_5) = sum_(a<b) |Tr(g_a^-1 g_b)|^2`.

The unordered-pair sum is invariant under all `120` permutations of the five K5 labels. Under a common-left transformation `g_a -> h g_a`, each relative element is unchanged:

`(h g_a)^-1 (h g_b) = g_a^-1 g_b`.

On the frozen path

`g_1=g_3=g_4=g_5=I`,
`g_2=diag(exp(i t),exp(-i t))`,
`x=cos^2(t)`,

the exact value is

`F(t)=24+16 x`.

Hence `F` is nonconstant and its image contains the interval `[24,40]`.

For the frozen `M=12`, evaluation of `1,F,...,F^12` at thirteen distinct rational values `x=k/12`, `k=0,...,12`, gives exact rank `13` over `Q`. Since `F` takes an interval of values, the analytic conclusion is stronger than the finite control: if a polynomial `P(F)` vanished identically, then `P` would vanish on an interval and therefore be the zero polynomial. Thus the invariant powers `1,F,F^2,...` are linearly independent.

## Classification

`ITER080A_SM_FINITE_K5_PERMUTATION_COVARIANCE_LEAVES_INFINITE_DIMENSIONAL_TANGENTIAL_EXTENSION_AMBIGUITY_EXACT_SCOPED`

Scientific verdict: `PASS_EXACT_SCOPED`.

Finite K5 relabeling covariance by itself does not select a unique K5 distributional extension and does not even reduce the already-authorized smooth tangential ambiguity sector to finite dimension.

## Novelty qualification

This gate is an independent exact witness, not a new primary blocker. Iter077Q already established the stronger controlling fact using the fully `S5`-invariant nonconstant function

`Q(g)=sum_(a<b) tr_(1/2)(g_b^-1 g_a)`

and its powers. Therefore Iter080A confirms the finite-permutation non-selection conclusion by a distinct invariant `|Tr|^2` class function but does not increase the dimensional lower bound or supersede Iter077Q.

The durable new information is robustness of the obstruction under a second exact K5-invariant multiplier construction. Administrative test count is not interpreted as increased CRQN readiness.

## CRQN effect

The local-amplitude arrow remains blocked:

`source-ordered off-collision K5 object -> non-L1 common collision -> same-scaling-degree extensions -> infinite-dimensional tangential ambiguity -> unique source-selected local amplitude ?`

Iter080A removes one possible rescue: finite K5 permutation covariance alone cannot serve as the missing selector. It does not provide a selector.

## Interpretation ceiling

No claim is made that stronger analytic, positivity, causality, locality, composition, infinite-family consistency, or genuinely source-defined selection principles cannot reduce the ambiguity. No K5/F9/G3/G8 promotion, regulator-independence theorem, full causal-vertex finiteness/divergence theorem, RG closure, new physics, or complete-QG claim follows.

The published one-wedge spectral `i epsilon` remains one-wedge authority only.

## Next admissible gate

Do not spend another gate on finite permutation symmetry. The highest-information successor should attack either:

1. a genuinely source-motivated selector strong enough to act on the full Iter077Q function space; or
2. the already authorized joint generalized-causal primary-source bridge question for E3/E4/E6, with no toy contraction-count repetition.

E7/E8 transport remains physically inadmissible until both a local extension selector and an actual composed causal E3-E6 functional exist.
