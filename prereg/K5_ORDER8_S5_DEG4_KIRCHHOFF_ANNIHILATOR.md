# Prospective preregistration — K5 S5-equivariant degree-four Kirchhoff logarithmic/annihilator gate

Date: 2026-09-16

Parent terminal authorities:
- full invariant-dual projective object/reachability: commit `e9ed372a91ac1bd219dc7671a916c70405e9cd43`;
- S5 component-degree-two radial-only theorem: commit `ee965976e0af8f3b569407e917b0046f02b79649`;
- repaired S5 component-degree-three radial-only theorem: commit `ed7a2aa05e0fa6bb75d63fa5328665059d0a012b`.

This gate is frozen before implementation or production inspection of the degree-four solution space. No outcome definition or ansatz may be changed after seeing the result.

## Scientific question

For the exact K5 Kirchhoff polynomial, is component degree four the first S5-equivariant regular face-tangent polynomial logarithmic class containing a genuinely non-radial direction? If so, does the non-radial class contain an exact Kirchhoff annihilator with zero logarithmic quotient,

`v(Psi_K5)=0`,

rather than merely a non-radial logarithmic field with `v(Psi_K5)=H_3 Psi_K5`?

This is a structural projective-IBP gate. It does not yet act on the two actual invariant-dual degree-27 numerators.

## Frozen exact object

Use edge order `(01),(02),(03),(04),(12),(13),(14),(23),(24),(34)` and independently reconstruct the coefficient-one 125-tree K5 Kirchhoff polynomial `Psi_K5`.

A complete regular face-tangent component-degree-four field is

`v_e = alpha_e Q_e(alpha)`,

where `Q_e` is homogeneous cubic. Construct the **complete** S5-equivariant cubic coefficient space from all fixed-edge-stabilizer orbits on the 220 degree-three edge monomials, including repeated powers. Guessing a reduced ansatz is forbidden.

Construct independently the complete S5-invariant homogeneous cubic quotient space from global S5 orbits on the same 220 monomials. Solve the full exact identity over Q:

`sum_e v_e d_e Psi_K5 = H_3(alpha) Psi_K5`.

The full radial subspace is all `F_3(alpha) E`, where `F_3` ranges over the complete S5-invariant cubic space and `E=sum_e alpha_e d/dalpha_e`.

Separately compute the exact **annihilator kernel** by setting the quotient coordinates identically to zero and solving

`sum_e v_e d_e Psi_K5 = 0`

using the complete vector-field coefficient space.

## Frozen primary outcomes

Return exactly one scientific classification:

- `K5_S5_DEG4_NONRADIAL_ANNIHILATOR_EXISTS_EXACT_SCOPED` iff the exact logarithmic quotient by the full radial subspace has positive dimension **and** the zero-quotient annihilator kernel contains a nonzero field;
- `K5_S5_DEG4_NONRADIAL_LOG_NO_ANNIHILATOR_EXACT_SCOPED` iff the logarithmic quotient has positive dimension but the exact zero-quotient annihilator kernel is trivial;
- `K5_S5_DEG4_RADIAL_ONLY_EXACT_SCOPED` iff the exact logarithmic quotient dimension is zero;
- `K5_S5_DEG4_INCONCLUSIVE_SCOPED` iff the complete exact object is constructed but exact rank/nullspace closure is not obtained;
- `INVALID_IMPLEMENTATION`, `INVALID_PROVENANCE`, or `INFRASTRUCTURE_FAILURE` for non-scientific failures.

The annihilator classification may not be inferred merely from a non-radial logarithmic class; zero quotient must be checked exactly.

## Mandatory checks

A valid implementation must:

1. recover 10 edges and all 125 coefficient-one degree-four K5 spanning-tree monomials;
2. enumerate the fixed-edge stabilizer exactly (order 12) and all its orbits on the 220 cubic monomials, with complete census;
3. enumerate all global S5 orbits on the same 220 monomials, giving the complete invariant cubic quotient space;
4. build the complete transported equivariant component basis and verify covariance under all 120 node permutations;
5. build the full polynomial coefficient matrix and solve exact rank/nullspace over Q;
6. substitute every returned logarithmic nullspace basis vector into the full identity exactly;
7. construct the complete invariant-cubic Euler subspace, verify its inclusion, and compute the exact non-radial quotient dimension;
8. independently solve the vector-only zero-quotient matrix, substitute every annihilator basis vector exactly, and report annihilator dimension;
9. if an annihilator exists, emit at least one deterministic primitive-integer representative in the fixed-edge-orbit basis and verify that its quotient coordinates are exactly zero;
10. retain the established regular face-tangent Schwinger-boundary audit; no singular `1/alpha_e` field enters this gate.

## Mandatory adversarial controls

The same validator must actually execute and pass:

- rejection of an explicit non-face-tangent field;
- rejection of an explicit face-tangent but S5-breaking field;
- rejection of a fake logarithmic coefficient vector;
- rejection of a fake annihilator whose vector-only coefficient identity is nonzero;
- a synthetic same-engine positive control using `Psi_syn=prod_e alpha_e`;
- for that synthetic fixture, exact recovery of a positive non-radial logarithmic quotient and a nonzero annihilator kernel;
- exact verification of the known synthetic annihilator
  `Q_e = 9 alpha_e^3 - sum_(f != e) alpha_f^3`, so `v_e=alpha_e Q_e` and `sum_e Q_e=0`;
- no invariant-dual period verdict may be emitted.

## Dependency rule

If `NONRADIAL_ANNIHILATOR_EXISTS` is terminal, the immediate successor must **not** be another blind degree search. Prospectively freeze a projective-form action gate for a deterministic annihilator basis on both actual invariant-dual degree-27 numerator channels. That successor must derive the correct projective `(n-2)`-form/IBP identity and audit all Schwinger-simplex boundary terms; affine-gauge tangency may not be assumed.

If only `NONRADIAL_LOG_NO_ANNIHILATOR` occurs, freeze the corresponding nonzero-quotient logarithmic relation on the actual numerators. If `RADIAL_ONLY`, choose between higher degree, non-equivariant modules, or denominator-shifting identities by information gain.

## Interpretation ceiling

Even a genuine Kirchhoff annihilator proves only a structural denominator-preserving IBP direction. It does not by itself prove either invariant-dual projective period zero/nonzero, determine the full 217-dimensional K5 tensor, select a physical finite part, prove regulator independence, authorize G3/F9/G8, establish `NEW_PHYSICS_FOUND`, or complete quantum gravity.
