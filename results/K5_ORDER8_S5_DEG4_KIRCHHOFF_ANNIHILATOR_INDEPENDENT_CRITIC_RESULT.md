# Independent Critic — K5 S5 degree-four Kirchhoff annihilator

Date: 2026-09-16

## Prospective authority

Critic preregistration: `prereg/K5_ORDER8_S5_DEG4_KIRCHHOFF_ANNIHILATOR_INDEPENDENT_CRITIC.md`, commit `7cde5bd6838e40b7d10fe7dd9707f04cc3198662`, frozen while Researcher run `35043883583` was still queued and before its rank/nullity/classification/annihilator representative were known.

Critic implementation: `scripts/critic_k5_order8_s5_deg4_kirchhoff_annihilator.py`, commit `782f3e960b188d598c5605bef3f1cd6f5d2ece1f`.

Workflow/head: `.github/workflows/critic_k5_order8_s5_deg4_kirchhoff_annihilator.yml`, head `3ea822da929ebe8c4fe34c11383efd800b3979e9`.

Reviewed Researcher result: `results/K5_ORDER8_S5_DEG4_KIRCHHOFF_ANNIHILATOR_RESULT.md`, commit `686268eddb3f0e2aece5857ef75cec52716eccc6`.

Reviewed production summary: `results/raw/k5_order8_s5_deg4_kirchhoff_annihilator_production_summary.json`, commit `2db15ad006b4e14e97e7ae0834d793ff8b387e50`.

## Critic production

- run `35044426437`, terminal `success`;
- job `104631081292`, terminal `success`;
- artifact `10426875582`;
- artifact ZIP digest `sha256:b7f477067778424f6d37d749317096c47056e7f47af447f30816612e820ffb36`;
- Critic JSON SHA256 `48bfa209b9f01e8e6bca351bced9211134f76f73bd46692b8078a7e4083732db`;
- verdict `CONFIRMED_SCOPED`.

## Independent reconstruction

The Critic does not import Researcher rank/nullity as mathematical inputs. It independently reconstructs:

1. the weighted reduced K5 Laplacian and its determinant polynomial;
2. the K5 spanning-tree polynomial separately and proves exact equality to the determinant, with 125 coefficient-one monomials;
3. all 220 cubic edge monomials;
4. the order-12 fixed-edge stabilizer and its complete 33-orbit partition;
5. the seven global S5 cubic orbits;
6. the full logarithmic coefficient matrix and the vector-only annihilator matrix.

It independently obtains

- system `7180 x 40`;
- exact rank `32`;
- nullity `8`;
- radial invariant-cubic Euler dimension `7`;
- non-radial quotient dimension `1`;
- vector-only rank `32`;
- annihilator dimension `1`.

These exactly reproduce the Researcher dimensions.

## Direct attack on the emitted representative

The Critic reads the 33 coefficients emitted by the Researcher production summary; it does not use a separately hard-coded expected K5 annihilator.

For that emitted representative the Critic independently verifies:

- `sum_e v_e d_e Psi_K5 = 0` coefficient-by-coefficient;
- logarithmic quotient coordinates are exactly zero;
- the field is outside the complete seven-dimensional invariant-cubic Euler span;
- every component is divisible by its corresponding `alpha_e`, hence face-tangent;
- full equivariance holds under all 120 vertex permutations.

Thus the one-dimensional non-radial class is genuinely represented by an exact Kirchhoff annihilator.

## Counterexample controls

The same independent engine rejects:

- an explicit non-face-tangent field;
- an explicit S5-breaking field;
- a fake logarithmic relation;
- a fake annihilator.

It also independently reconstructs the synthetic `prod_e alpha_e` fixture and verifies a nontrivial annihilator kernel, including the known synthetic zero-quotient direction.

## Verdict

`CONFIRMED_SCOPED`

The exact scoped Researcher theorem

`K5_S5_DEG4_NONRADIAL_ANNIHILATOR_EXISTS_EXACT_SCOPED`

survives independent reconstruction and direct adversarial substitution.

## Interpretation ceiling

This confirms a structural denominator-preserving projective-IBP direction. It does not evaluate either invariant-dual projective period, does not determine the full 217-dimensional K5 tensor, does not reduce the 377-dimensional supported-extension ambiguity, and does not select a physical finite part.
