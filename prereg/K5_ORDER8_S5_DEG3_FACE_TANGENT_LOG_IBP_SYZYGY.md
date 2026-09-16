# Prospective preregistration — K5 S5-equivariant degree-three face-tangent logarithmic IBP/syzygy gate

Date: 2026-09-16

Parent terminal authorities:
- `results/K5_ORDER8_INVARIANT_DUAL_PROJECTIVE_IBP_REACHABILITY_RESULT.md`, commit `e9ed372a91ac1bd219dc7671a916c70405e9cd43`;
- `results/K5_ORDER8_S5_DEG2_FACE_TANGENT_LOG_IBP_SYZYGY_RESULT.md`, commit `ee965976e0af8f3b569407e917b0046f02b79649`.

This gate is frozen before implementation or inspection of the degree-three solution space. Frozen criteria must not be changed after seeing the result.

## Scientific question

Does the exact K5 Kirchhoff polynomial admit a genuinely non-radial, S5-equivariant, regular face-tangent homogeneous polynomial logarithmic vector field of component degree three, after quotienting all polynomial multiples of the Euler field? Degree <=2 is already terminally radial-only, so degree three is the first unresolved equivariant same-denominator class.

This is a structural IBP gate. It does not evaluate either invariant-dual projective period.

## Frozen object

Use edge order `(01),(02),(03),(04),(12),(13),(14),(23),(24),(34)` and independently reconstruct `Psi_K5` as the coefficient-one 125-spanning-tree Kirchhoff polynomial.

A regular face-tangent field has `v_e = alpha_e Q_e(alpha)` with `Q_e` homogeneous quadratic. The implementation must construct the **complete** S5-equivariant quadratic coefficient space from exact fixed-edge-stabilizer orbits on unordered degree-two edge monomials (including squares), rather than guess a reduced ansatz.

The logarithmic condition is

`sum_e v_e d_e Psi_K5 = H_2(alpha) Psi_K5`,

where `H_2` is the complete S5-invariant homogeneous quadratic polynomial space, constructed independently by orbit sums of degree-two monomials.

Solve the full identity by exact rational coefficient matching. Floating-point fitting, random-point-only certification, post-hoc ansatz reduction and selected-monomial matching are forbidden.

## Radial quotient

All fields `v = F_2(alpha) E`, with `F_2` any S5-invariant homogeneous quadratic polynomial and `E=sum_e alpha_e d/dalpha_e`, are radial/logarithmic controls and must be contained in the exact nullspace. The scientific quotient is the exact degree-three logarithmic solution space modulo this full radial subspace, not modulo a single `s1^2 E` direction.

## Frozen outcomes

Return exactly one:
- `K5_S5_FACE_TANGENT_LOG_IBP_DEG3_NONRADIAL_EXISTS_EXACT_SCOPED` iff the exact quotient by the full invariant-quadratic radial subspace has positive dimension;
- `K5_S5_FACE_TANGENT_LOG_IBP_DEG3_RADIAL_ONLY_EXACT_SCOPED` iff that quotient dimension is exactly zero and all completeness/provenance checks pass;
- `K5_S5_FACE_TANGENT_LOG_IBP_DEG3_INCONCLUSIVE_SCOPED` iff the exact system is correctly constructed but complete exact rank/nullspace certification is not obtained;
- `INVALID_IMPLEMENTATION`, `INVALID_PROVENANCE`, or `INFRASTRUCTURE_FAILURE` for non-scientific failures.

## Mandatory checks and controls

A valid implementation must:
- reconstruct all 125 spanning-tree monomials and verify degree four/coefficient one;
- enumerate the fixed-edge stabilizer exactly and derive its orbits on all degree-two monomials, reporting orbit count and sizes;
- independently derive the S5 orbits on degree-two monomials and hence the complete invariant quadratic quotient space;
- build every equivariant degree-three coefficient from orbit data and verify S5 covariance directly on generators and all 120 permutations;
- solve the polynomial identity over Q by exact sparse row reduction or another exact rank/nullspace method with a reproducible certificate;
- substitute every returned basis vector back into the full polynomial identity exactly;
- verify inclusion and exact dimension of the full radial subspace `F_2 E`;
- compute the quotient dimension by exact linear algebra;
- reject at least one non-face-tangent field, one S5-breaking field, and one fake logarithmic field through the same validator;
- include a synthetic homogeneous symmetric fixture for which the same construction has a known genuine non-radial degree-three logarithmic direction, preventing a hard-coded radial-only verdict;
- retain the source Schwinger-face boundary interpretation: regular face-tangent fields have no codimension-one boundary contribution under the established face audit; singular `1/alpha_e` fields are outside this gate.

## Dependency rule

If `NONRADIAL_EXISTS` is terminal, the next gate must prospectively freeze the exact action of a basis of non-radial derivations on both actual degree-27 invariant-dual numerators and test whether the resulting projective IBP relations reduce/evaluate either period. If `RADIAL_ONLY`, do not infer a period theorem; proceed to degree four, non-equivariant S5-orbit modules, or denominator-shifting/index-changing IBP with a fresh boundary audit, choosing the highest-information route.

## Interpretation ceiling

No K5 integrated-period zero/nonzero theorem, no full 217-dimensional tensor/annihilator result, no physical finite-part selector, no regulator-independence theorem, no G3/F9/G8 promotion, no `NEW_PHYSICS_FOUND`, and no complete-QG claim follows from this gate.