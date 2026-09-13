# Iter078I-RG preregistration — can exact EPRL recovery select an individual causal-Toller extension?

**Date:** 2026-09-14

## Scientific question

The primary source has the exact one-wedge identity

`T^(+) + T^(-) = D`.

Expanding all ten wedges gives the exact off-collision identity

`sum_{kappa in {+,-}^10} product_e T_e^(kappa_e) = product_e D_e`,

so the unconstrained sum of `2^10=1024` wedge-sign sectors reproduces the EPRL vertex integrand.

Can requiring the **extended** sector sum to equal the finite/defined EPRL vertex uniquely determine the extension of an individual factorized causal sector `kappa_ab=sigma_a sigma_b`?

## Frozen source facts

1. Primary causal source Eq. (5): `T+ + T- = D`.
2. Eq. (6): EPRL vertex is the unconstrained sum over all independent wedge signs.
3. The same source states that the constrained sum over factorized causal structures `sigma_a` does **not** reproduce the EPRL vertex.
4. Iter077L/G establish admissible supported extension differences on the common-collision set; order-zero `ell(Psi) delta_N` terms have scaling degree below the maximal source degree and leave every off-collision sector unchanged.

## Frozen counterexample test

Assume a family of extended wedge-sign sector functionals `{Pbar_kappa}` satisfies

`sum_kappa Pbar_kappa = A_EPRL`

for the same boundary state.

Choose two distinct sign sectors `kappa=s,t`, with `s` chosen to be one of the 16 factorized causal patterns. For any nonzero boundary functional `ell`, define

`Pbar'_s = Pbar_s + ell delta_N`,

`Pbar'_t = Pbar_t - ell delta_N`,

and leave every other sector unchanged.

Check prospectively:

1. each modified sector has the same off-`N` Toller product;
2. each remains within the allowed same-scaling-degree extension class;
3. the total unconstrained sum is exactly unchanged;
4. the chosen causal-sector extension has changed nontrivially;
5. no primary-source condition forbids compensating supported shifts between independent wedge-sign sectors.

## PASS

PASS iff the counterexample satisfies all five checks. Then EPRL recovery is a normalization constraint on the **sum**, not a unique selector of any individual causal extension.

Classification:

`ITER078I_RG_EPRL_UNCONSTRAINED_SECTOR_SUM_RECOVERY_DOES_NOT_SELECT_INDIVIDUAL_CAUSAL_EXTENSION_EXACT_COUNTEREXAMPLE_SCOPED`

## FAIL

FAIL iff a frozen source identity acts sector-by-sector strongly enough to forbid the compensating shift and uniquely fix the causal sector.

## Interpretation ceiling

PASS does not say EPRL information is useless: it supplies linear relations/normalization conditions among sector extensions. It says only that the exact sum identity is underdetermined and cannot by itself select the causal vertex.

No full dimension count for all 1024 sector ambiguities, no generic-spin theorem, no RG fixed point, no G3 or complete-QG claim follows.