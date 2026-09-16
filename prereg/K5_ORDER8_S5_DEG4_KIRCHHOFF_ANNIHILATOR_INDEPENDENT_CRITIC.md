# Prospective preregistration — independent Critic for K5 S5 degree-four Kirchhoff-annihilator gate

Date: 2026-09-16

Researcher preregistration: `prereg/K5_ORDER8_S5_DEG4_KIRCHHOFF_ANNIHILATOR.md`, commit `00b5ddf78474179281380606fbc3f62ca260e337`.

Researcher implementation head: `53bdd4d6adb5e470192292d7ef2616a57e15fc6e`.

At the time of this Critic freeze, Researcher run `35043883583` is non-terminal/queued. No Researcher rank, nullity, classification, annihilator coefficients, or artifact content has been used to choose the Critic acceptance criteria below.

## Review question

Independently determine whether the Researcher degree-four result, whatever its terminal classification, is mathematically and prospectively valid for the exact K5 Kirchhoff object and the complete S5-equivariant regular face-tangent component-degree-four ansatz.

## Required independent reconstruction

The Critic must not accept Researcher rank/nullity literals as inputs. It must independently reconstruct:

1. the ten K5 edges and weighted reduced 4x4 Laplacian;
2. `Psi_K5=det L(alpha)` directly from the determinant and independently the 125 spanning-tree polynomial, then verify exact equality;
3. all 220 homogeneous cubic edge monomials;
4. the order-12 fixed-edge stabilizer and its complete orbit partition;
5. the full S5 orbit partition giving the invariant cubic quotient space;
6. the complete transported equivariant vector-field coefficient matrix;
7. the logarithmic identity matrix and the vector-only annihilator matrix.

The Critic must compute rank/nullity independently. A valid rank certificate may combine exact rational elimination with modular rank lower bounds plus explicit rational nullvectors, provided equality is logically certified rather than inferred statistically.

## Frozen review logic

Return exactly one review verdict:

- `CONFIRMED_SCOPED` iff Researcher provenance is prospective, object identity matches, all mandatory controls genuinely execute, and independent reconstruction reproduces the Researcher scientific classification and required dimensions/identities;
- `QUALIFIED` iff the core exact theorem survives but an interpretation/scope statement needs narrowing that does not change the mathematical object;
- `INVALID_IMPLEMENTATION` iff frozen controls/object are not actually implemented or the returned classification is not entailed by executed code;
- `INVALID_PROVENANCE` iff chronology/artifact/head identity is insufficient;
- `REQUIRES_NEW_PREREGISTERED_GATE` iff repair would change the scientific object/ansatz/outcome definitions.

No verdict may be chosen from green CI alone.

## Annihilator-specific adversarial requirements

If Researcher reports `NONRADIAL_ANNIHILATOR_EXISTS`, Critic must additionally:

- read the emitted primitive integer annihilator representative rather than a hand-transcribed expected vector;
- substitute it independently into `sum_e v_e d_e Psi_K5` and obtain the zero polynomial coefficient-by-coefficient;
- verify its quotient coordinates are exactly zero;
- prove it is outside the complete invariant-cubic Euler span by exact rank;
- verify face tangency from actual component monomials;
- verify S5 equivariance under all 120 vertex permutations.

If Researcher reports `RADIAL_ONLY`, Critic must independently prove the logarithmic nullspace equals the Euler span. If Researcher reports nonradial-log/no-annihilator, Critic must independently prove the vector-only kernel is trivial.

## Controls

Critic must include at least one malformed non-face-tangent field, one S5-breaking field, one fake logarithmic relation, one fake annihilator, and an independently reconstructed synthetic `prod_e alpha_e` fixture exhibiting a nontrivial annihilator.

## Interpretation ceiling

A confirmed degree-four annihilator is only a structural denominator-preserving projective-IBP direction. It does not evaluate the two invariant-dual periods, determine the full K5 tensor, or supply a physical finite-part selector.
