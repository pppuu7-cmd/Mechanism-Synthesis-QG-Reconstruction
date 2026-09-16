# K5 34-orbit exact cancellation resolver — implementation freeze

Status: **PROSPECTIVELY FROZEN BEFORE PRODUCTION COEFFICIENTS**.

Parent scientific preregistration: `d6b0e805101c8590eafac71398cc2b1466691752`.

This file freezes implementation details required by that preregistration. It does not change the scientific objective, orbit set, channel space, weights, S5 action, normalization, or classifier.

## Frozen exact supports

Use the same frozen linear corner substitution as the parent audit:

`alpha_e(t) = w_e t` for `e in Z`, and `alpha_e(t)=w_e` for `e not in Z`,

with the two parent asymmetric weight assignments and their transported values under the frozen K5/S5 cycle.

Complete coefficient supports are fixed before production as:

- physical numerator `N_c`: `t^0 ... t^27`;
- polynomial annihilator action `B_v[N_c]`: `t^0 ... t^31`;
- projective-normal polynomial numerator `U_Z`: `t^0 ... t^5`.

No support may be enlarged after observing coefficients.

## Projective-normal degree ceiling

The frozen degree-four annihilator has `v_i = alpha_i q_i` with `deg q_i = 3`, hence `deg v_i = 4` and `deg S = 4`. With `s1=sum_i alpha_i`, `deg s1=1`, and `A_Z=sum_{e in Z} alpha_e`, `deg A_Z=1`, the polynomial numerator of the tangent normal component is

`U_Z = s1 * sum_{e in Z} v_e - S * A_Z`.

Both summands have degree `1+4=5`, so the prospectively frozen exact ceiling is

`deg U_Z <= 5`.

The resolver must retain coefficients `t^0 ... t^5` even if lower observed orders would appear sufficient.

## Primary exact route

Arithmetic: Python exact `fractions.Fraction`; no floating-point zero test and no modular reconstruction.

Use the already-authoritative compressed all-32 source/Wick coefficients and the same canonical degree-27 numerator DAG authority, but evaluate them in a denominator-cleared univariate polynomial algebra.

Let `Psi` be the authoritative 125-tree polynomial and `Adj(L)` the exact Laplacian adjugate. Define scaled inverse-series matrices

`C_0 = Adj(L)`,
`C_n = -Adj(L) Q C_(n-1)` for `n=1,...,4`.

Then `B_n = C_n / Psi^(n+1)`. This removes Laurent inversion from the coefficient extractor without changing the canonical recurrence.

For the determinant factor, set `A=Adj(L)Q` and expand

`det(I+x A)^(-3/2) = sum_{i=0}^4 F_i x^i + O(x^5)`.

Then the original coefficient is `F_i/Psi^i`.

For each Wick pairing, use the scaled covariance series obtained from the `C_n`; a five-pair term of series order `j` has denominator `Psi^(j+5)`. Therefore every order-four contribution after multiplication by the determinant factor has the common denominator `Psi^9`, exactly cancelled by the authoritative numerator definition. The resulting `N_c` is evaluated directly as a polynomial object, never through a one-leading-term approximation.

Propagate a first directional derivative in parallel through the same polynomial DAG with seed `d alpha_i = v_i`; this gives exact `v(N_c)`. Then compute

`B_v[N_c] = s1*v(N_c) + {s1[div v +(1/2)sum_i q_i]-3S} N_c`

as a degree-31 polynomial before division by `s1^4`.

## Frozen S5 covariance controls

Use exactly the parent audit values:

- `W1=(2,3,5,7,11,13,17,19,23,29)`;
- `W2=(31,37,41,43,47,53,59,61,67,71)`;
- frozen cycle `(1,2,3,4,0)` with the parent edge-permutation/orientation convention.

For every physical orbit and both channels, compute complete coefficient vectors at `W1`, `W2` and their correctly transported permuted lanes. S5 covariance is coefficient-by-coefficient equality of the complete vectors, not equality of a guessed leading term.

## Independent reconstruction route

Freeze interpolation nodes before production to the 32 positive integers

`t = 1,2,...,32`.

For the representative selected for every distinct `(collision_size, orbit_size)` class, independently evaluate the original rational point algebra using direct matrix inversion/cofactor/determinant-factor/Wick contraction with exact Fractions and the same static source coefficients, then reconstruct by exact polynomial interpolation:

- `N_c` from the full 32 nodes, requiring reconstructed coefficients `t^28...t^31` to vanish and retaining `t^0...t^27`;
- `B_v[N_c]` from the same 32 nodes through degree 31;
- `U_Z` through degree 5, checked against the first six and all remaining frozen nodes.

This route must not call the primary polynomial-propagation evaluator.

## Frozen negative controls

The production must pass all of the following before a scientific classification is valid:

1. cancellation control: polynomial `[1,-2,1]` after subtraction of its frozen leading candidate must resolve to a finite higher order, not exact zero;
2. exact-zero control: an identically zero complete-support vector is classified `EXACT_ZERO_WITHIN_COMPLETE_SUPPORT`;
3. truncation control: dropping the last nonzero coefficient from a synthetic degree-5 vector is detected by full-support hash/equality;
4. wrong-substitution control: swapping one scaled and one unscaled edge changes a synthetic coefficient vector and is detected;
5. wrong-permutation control: an intentionally untransported asymmetric weight vector fails coefficient covariance;
6. channel-swap control: synthetic unequal two-channel vectors detect a swap;
7. degree-ceiling control: generated vectors must have exactly lengths 28, 32 and 6 for `N`, `B`, `U` respectively;
8. one-leading-term shortcut control: a synthetic object with cancelled first candidate and nonzero next coefficient must not be classified from the first coefficient alone.

## Terminal classifier

Unchanged from parent preregistration.

- `INVALID_IMPLEMENTATION` if complete supports, lineage, coverage, exact arithmetic, independent reconstruction, or covariance controls fail.
- `K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION_PARTIAL_BLOCKED_SCOPED` if implementation is valid but any required target remains uncertified.
- `K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION_EXACT_SCOPED` only if all 64 physical channel-orbit components have exact numerator/action/projective-normal resolutions and all frozen S5 covariance controls pass.

No global Stokes/IBP or integrated-period conclusion is authorized by this implementation freeze.
