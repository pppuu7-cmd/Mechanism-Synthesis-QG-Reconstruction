# K5 full-source boundary S5 transport symbolic generator theorem — terminal Researcher result

Date: 2026-09-17

Classification: **`K5_FULL_SOURCE_BOUNDARY_S5_SYMBOLIC_ALL_ALPHA_TRIVIAL_CHARACTER_EXACT_SCOPED`**.

Researcher status: **`PASS_EXACT_SCOPED`**. Independent adversarial Critic review is required before the already-frozen exact-leading-coefficient cancellation resolver consumes this theorem as confirmed coefficient-level transport authority.

## Prospective authority

Parent scientific preregistration:

`prereg/K5_FULL_SOURCE_BOUNDARY_S5_TRANSPORT_SYMBOLIC_GENERATOR_THEOREM.md`, commit `4f65cff503db976b6ff52b8519e5fdaa0bf4a4f8`.

The gate was frozen before symbolic implementation/output. It asks whether the complete all-`j=1/2` source-ordered K5 order-zero boundary Wick covector satisfies the ordinary contragredient S5 law as an exact rational-function identity in formal Schwinger variables, with no extra permutation-sign character.

Existing parent cancellation preregistration remains unchanged:

`prereg/K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION.md`, commit `d6b0e805101c8590eafac71398cc2b1466691752`.

## Historical invalid implementation and prospective repair

Initial implementation/workflow head `d802304d0c4d9ba61d5e06b72864325065de651a` produced run `35200249024`, job `105133013586`. The workflow was terminal failure but uploaded artifact `10488005998`, ZIP digest `sha256:4260cd4669fc0e5420a2cddaa1b36e03adfd3e8a60b0b27701d9cd86d0b359ec`.

That attempt is **`INVALID_IMPLEMENTATION`** and has no scientific verdict. It correctly verified group size 120, the 125-tree Kirchhoff polynomial and exact C/T covariance transport, but it placed the canonical-edge orientation sign in a raw source-pattern subfactor while comparing that subfactor directly to the contragredient boundary law. The malformed-control branch therefore failed before a scientific classification was admissible.

Before changing implementation, control-only repair 1 was prospectively frozen:

`prereg/K5_FULL_SOURCE_BOUNDARY_S5_TRANSPORT_SYMBOLIC_GENERATOR_THEOREM_CONTROL_REPAIR_1.md`, commit `73b8f65f05e3945e8c4d517e73b938cdd3299e39`.

The repair changed only formal sign bookkeeping and validation placement. The parent scientific hypothesis, source object, generators, PASS/FAIL meanings and interpretation ceiling were unchanged.

## Exact formal object

The gate retains source ordering

`one-wedge spectral/spinor integration -> Toller function -> product of ten Toller matrices -> full boundary contraction -> K5 group/distributional object`.

It works before invariant-dual projection on the complete unprojected 32-component boundary covector with exactly `100000` original source node-choice terms. No numerical Schwinger witness, interpolation grid, fitted phase, fitted two-channel matrix or floating tolerance enters the theorem.

Two exact formal layers are tested:

1. the K5 Kirchhoff polynomial `Psi_K5(alpha)` and every edge-edge covariance numerator are represented as sparse multivariate polynomial dictionaries;
2. the complete all-32 source/boundary coefficient dictionaries are transported using the source-defined endpoint convention, including `(row,col)->(col,row)` on canonical-edge reversal.

The frozen S5 generators are

`C=(1,2,3,4,0)` and `T=(1,0,2,3,4)`.

Their exact boundary and edge/orientation actions are then closed under composition and verified to generate all 120 elements of S5.

## Orientation-sign accounting

For a vertex permutation `p`, let `s_e=+-1` be the canonical-edge orientation sign. In every complete order-zero Wick monomial, each of the ten K5 edges occurs exactly once across the five covariance pairings.

The source matrix reversal contributes

`g_source = product_e s_e`.

The exact formal covariance pullback contributes independently

`g_cov = product_e s_e`.

Therefore the complete source-faithful Wick coefficient carries

`g_source * g_cov = (product_e s_e)^2 = 1`.

This is why the correctly transported complete object has no residual `sgn(p)` character. For the odd generator `T`, omitting source reversal alone is rejected, omitting covariance orientation alone is rejected, and omitting the endpoint transpose is rejected.

## Authoritative production

Repaired implementation/head:

`bb0274946226538e9ef6682e11de5ee896df837e`.

Authoritative run `35200455308` is terminal `success`; job `105133686282` is terminal `success`.

Artifact:

- ID `10487318071`;
- name `k5-full-source-boundary-s5-symbolic-transport-theorem`;
- ZIP digest `sha256:054325eaf134bf8a8b0fe3a48d156cfb8c52df660d32f37168b40df1f6d23387`.

Authoritative result JSON SHA256:

`c1c834a626bdb15c3564679396479d731eb87d52a3f01ed4c727c603f5208fbc`.

Executed script SHA256:

`0cf7ef8344ec464bca8d2cb210c194cfe17b7fa7c015745267c44fa9de5300b2`.

Durable machine aggregate:

`results/raw/k5_full_source_boundary_s5_transport_symbolic_theorem_authoritative.json`.

## Exact result

All required positive and malformed controls passed in the repaired production.

- `C` and `T` generate exactly 120 vertex permutations.
- Boundary representation matrices compose exactly over all generated words.
- Edge permutation/orientation maps compose exactly over all generated words.
- `Psi_K5` consists of exactly 125 coefficient-one spanning-tree monomials and is invariant under both generators.
- Every formal covariance numerator obeys the exact C and T transport identity with the canonical incidence/orientation sign.
- The full formal source/boundary coefficient dictionaries contain all 32 boundary components and exactly 100000 source node-choice terms.
- For both C and T, the fully transported formal dictionaries equal the exact contragredient prediction componentwise.
- For C the transported/predicted dictionary hash is `489e72220baf1cab93bfea78051e8c46aabc44d5cf574c8e0c83fbe10e7c967b`.
- For T the transported/predicted dictionary hash is `994832f0c65a21a8a0b20ea102c96ffda3b6090c6e7a9342e3a4fc8b5cb9ac65`.
- The odd-generator negative controls reject omitted transpose, omitted source reversal sign, omitted covariance orientation sign, the source-fixed diagnostic object and an extra permutation-sign character.

Since the exact generator transport maps compose and generate S5, the gate proves on the formal domain `Psi_K5 != 0` the scoped rational-function identity

`a_p(p alpha) = A_p^(-T) a(alpha)`

for every `p in S5`, with **trivial residual character**.

## New scientific fact

The earlier witness-scoped full-source transport result is strengthened from equality on prospectively frozen generic Schwinger witnesses to an exact symbolic coefficient-level theorem for the order-zero full-source boundary object.

The source-fixed repair-5 mismatch remains valid as a negative object-definition control; it is not a physical S5 obstruction. The complete source-faithful object is S5-covariant because source endpoint reversal and covariance orientation transport contribute matching orientation characters that cancel in every complete Wick monomial.

Thus there is no symbolic source/boundary S5 transport obstruction at this layer, and there is no need for a fitted phase or nontrivial constant two-channel mixing mechanism.

## Interpretation ceiling

This theorem supplies a Researcher-level coefficient-transport bridge only for the exact order-zero source/boundary object and must still be independently adversarially reviewed before parent cancellation work consumes it as confirmed authority.

It does **not** compute the actual lowest nonzero `t` order of either degree-27 physical numerator, degree-31 annihilator action, or projective-normal numerator at any Schwinger corner. It does not classify a physical corner finite/divergent, prove global projective Stokes/IBP, determine an invariant-dual K5 period, prove the full 217-dimensional order-eight tensor zero/nonzero, reduce `dim_C F_8=377`, select a physical finite part, prove regulator independence, promote F9/G3/G8/K5, establish `NEW_PHYSICS_FOUND`, or complete quantum gravity.

Published one-wedge spectral `i epsilon` remains retained.
