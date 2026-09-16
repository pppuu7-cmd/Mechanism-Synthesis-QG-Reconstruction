# K5 invariant-dual degree-27 numerator — exact polynomial-DAG derivation

Date: 2026-09-16

Status: outcome-independent algebraic derivation supporting `prereg/K5_INVARIANT_DUAL_DEG27_CANONICAL_DAG_MATERIALIZATION.md`, commit `faa436e10301ecb92f2e4558411f0d1af6f4594f`. It assigns no integrated-period value.

## 1. Gaussian family

Let `L(alpha)` be the exact reduced weighted K5 Laplacian and `Psi=det L`. Let the source K5 quadratic-radius matrix be the fixed rational matrix

`Q=L_uniform/5`.

For the order-eight radial insertion introduce

`L_s=L+sQ`.

The normalized Gaussian source moment is

`J(s)=[det(L_s)/det L]^(-3/2) W_source(L_s^(-1))`,

where `W_source` is the Wick contraction of the ten source linear edge numerators. The desired radial moment is

`J_4 = d^4 J/ds^4 |_(s=0) = 4! [s^4]J(s)`.

The complete projective integrand includes the baseline Gaussian determinant factor `Psi^(-3/2)`. The ten source factors plus four quadratic-radius insertions contain nine covariance contractions in total. Hence the complete denominator is `Psi^(3/2+9)=Psi^(21/2)`.

## 2. Polynomial-scaled inverse coefficients

Write

`B(s)=L_s^(-1)=sum_(n>=0) B_n s^n`.

The exact inverse recurrence is

`B_0=L^(-1)=adj(L)/Psi`,

`B_n=-B_0 Q B_(n-1)`.

Therefore

`B_n=(-1)^n Psi^(-(n+1)) adj(L) [Q adj(L)]^n`.

Define the scaled polynomial matrices

`K_n = Psi^(n+1) B_n`.

Then every entry of `K_n` is polynomial homogeneous degree

`3(n+1)`.

For source-edge incidence rows `r_e`, the scaled pair-covariance coefficient

`G_(ef,n)=r_e^T K_n r_f`

is likewise polynomial degree `3(n+1)`.

## 3. Polynomial-scaled determinant-ratio coefficients

Write

`D(s)=det(L+sQ)/Psi = 1 + sum_(k=1)^4 d_k/Psi * s^k`,

where `d_k` is homogeneous degree `4-k` in the Schwinger variables.

Let

`D(s)^(-3/2)=sum_(j>=0) rho_j s^j`.

Every order-`j` term has denominator exactly at most `Psi^j`. Define

`R_j=Psi^j rho_j`.

By the binomial expansion, `R_j` is an exact polynomial of homogeneous degree `3j`.

No square root or irrational coefficient remains: the only coefficients are rational binomial numbers.

## 4. Polynomial-scaled source Wick series

The ten source linear factors require exactly five pair contractions. Write their Wick series as

`W_source(s)=sum_(k=0)^4 W_k s^k + O(s^5)`.

A term contributing to order `k` chooses covariance orders `n_1,...,n_5` with

`sum_a n_a=k`.

Its denominator is

`Psi^(sum_a(n_a+1))=Psi^(k+5)`.

Define

`S_k=Psi^(k+5) W_k`.

Then `S_k` is an exact polynomial homogeneous degree

`3(k+5)=15+3k`.

The full all-32 source contraction and invariant-dual Reynolds projection are linear operations on these polynomial DAG nodes, so they preserve this statement.

## 5. Exact degree-27 numerator DAG

At order four,

`[s^4]J(s)=sum_(j=0)^4 rho_j W_(4-j)`.

Every summand has total denominator

`Psi^j * Psi^(9-j)=Psi^9`.

Thus define

`N = Psi^9 J_4`.

Equivalently,

`N = 4! * sum_(j=0)^4 R_j S_(4-j)`.

Each summand has homogeneous degree

`3j + [15+3(4-j)] = 27`.

Therefore the degree-27 numerator is represented exactly by a finite polynomial DAG built from:

- `Psi`;
- `adj(L)`;
- multiplication by the fixed rational `Q`;
- incidence-row contractions;
- rational binomial coefficients;
- the finite ten-factor Wick-pairing recursion;
- the finite all-32 source sum;
- the two-row invariant-dual projection.

This proves algebraically that a canonical DAG representation is an exact polynomial representation, not a rational approximation or representative-component surrogate.

## 6. Consequences for later differentiation

A polynomial vector field such as the confirmed degree-four Kirchhoff annihilator can act on this DAG by ordinary product/chain rules without first expanding all degree-27 monomials. The resulting differentiated DAG remains exact and hashable.

For Schwinger-boundary valuation work, the same scaled form is useful because each DAG node has a known polynomial degree and no hidden `Psi` denominator. Cancellations must still be checked at the summed-channel level; degree bookkeeping alone is not a boundary-integrability theorem.

## Interpretation ceiling

This derivation establishes exact polynomial representability and degree counting only. It does not assert that the production materialization gate has passed, does not give the integrated periods, and does not authorize dropping higher-codimension Schwinger boundary terms in an IBP identity.
