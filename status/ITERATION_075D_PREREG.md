# Iter075D preregistration — Toller branch-flip kernel recurrence certificate

Date: 2026-09-13

## Frozen objective

Test whether the Iter075C surviving kernel-level candidate

`K_s(j,l; rho, rtilde, epsilon) = - conjugate(K_-s(l,j; rho, rtilde, epsilon))`

is robust under held-out parameters and reducible to a recurrence-controlled identity of the source Feynman kernel, rather than a coincidence of the original panel.

## Frozen source object

Use exactly the published Feynman-i-epsilon coefficient form already used in Iter075C:

`K_s = s/(rtilde-rho-i s epsilon) * Gamma(-j-i rho) Gamma(l-i rtilde+1) / [Gamma(-j-i rtilde) Gamma(l-i rho+1)]`.

No replacement `beta+i epsilon`, no fitted phases, no contour deformation and no post-hoc parameter changes.

## Frozen independent lanes

Matrix over six `(j,l)` pairs:
`(1/2,1/2), (1,2), (3/2,5/2), (2,1), (5/2,1/2), (3,4)`.

Within each lane test all combinations:
- `s = +/-1`;
- `rho = 0.23, 0.91, 1.77`;
- `rtilde = -3.1, -1.37, -0.41, 0.28, 1.64, 3.05`;
- `epsilon = 1e-2, 3e-4, 1e-6`.

All values are frozen before production.

## Frozen predicates

1. Every source coefficient and comparison coefficient is finite and nonzero.
2. Branch-flip residual
   `|K_s + conj(K_-s(l,j))| / max(|K_s|, |conj(...)|)`
   must be `<= 1e-40` for every record at 100-digit arithmetic.
3. Same-branch negative control must fail the identity on at least 90% of records by residual `>= 1e-10`.
4. Epsilon variation may not change predicate 2.
5. For every lane, the ratio `K_s/conj(K_-s(l,j))` must be compatible with the frozen constant `-1` within `1e-40`.

## Frozen interpretation

- PASS: `ITER075D_BRANCH_FLIP_KERNEL_RECURRENCE_CERTIFICATE_SUPPORTED_SCOPED`.
- SCIENTIFIC FAIL: `ITER075D_BRANCH_FLIP_KERNEL_RECURRENCE_CERTIFICATE_OBSTRUCTED_SCOPED` if valid finite records violate a frozen predicate.
- INVALID/NUMERICAL: only if source coefficients cannot be evaluated reliably or controls malfunction.

Even PASS is only a source-kernel certificate. It is not the full Toller-function inversion law on the group and does not authorize K5/G3/F9/G8 promotion, a physical sector selection, a causal-vertex finiteness theorem, or any new-physics claim.
