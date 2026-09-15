# Prospective preregistration — K5 S5-equivariant degree-two face-tangent logarithmic IBP/syzygy gate

Date: 2026-09-16

Parent terminal authority: `results/K5_ORDER8_INVARIANT_DUAL_PROJECTIVE_IBP_REACHABILITY_RESULT.md`, commit `e9ed372a91ac1bd219dc7671a916c70405e9cd43`.

This gate is frozen before implementation or inspection of the exact logarithmic-derivation solution space. No criterion below may be changed after seeing the result.

## Scientific question

Does the exact K5 Kirchhoff polynomial admit any non-radial, S5-equivariant, regular face-tangent polynomial logarithmic IBP vector field of component degree at most two? Equivalently, is there a lowest-degree same-denominator projective IBP direction beyond polynomial multiples of the Euler field before introducing the full degree-27 invariant-dual numerator?

This is a structural successor to the first projective-IBP reachability gate. It does not evaluate either invariant-dual period.

## Frozen object

Use the authoritative K5 edge variables `alpha_e` in edge order

`(01),(02),(03),(04),(12),(13),(14),(23),(24),(34)`

and reconstruct

`Psi_K5(alpha)=det L(alpha)`

independently as the 125-term spanning-tree polynomial with coefficient one on each K5 spanning tree.

A regular face-tangent vector field must satisfy `v_e|_(alpha_e=0)=0`, hence every component is divisible by `alpha_e`.

### Degree one

The complete S5-equivariant face-tangent degree-one ansatz is

`v_e = a alpha_e`.

The logarithmic condition is

`v(Psi)=k Psi`.

Coefficient matching must recover the Euler relation and determine the exact solution-space dimension.

### Degree two

For a fixed edge `e`, its stabilizer in S5 has exactly three orbits on the ten edges:

1. `e` itself;
2. the six edges sharing one endpoint with `e`;
3. the three edges disjoint from `e`.

Therefore the complete S5-equivariant face-tangent homogeneous degree-two ansatz is

`v_e = alpha_e [ a alpha_e + b sum_(f adjacent e) alpha_f + c sum_(f disjoint e) alpha_f ]`.

No other S5-equivariant linear coefficient map is allowed.

Because `Psi_K5` is homogeneous degree four and S5-invariant, any S5-invariant degree-one logarithmic quotient is a multiple of

`s1=sum_e alpha_e`.

The exact logarithmic condition is therefore

`v(Psi_K5) = k s1 Psi_K5`.

Solve this identity by exact polynomial coefficient matching over Q. Point sampling, floating point fitting and post-hoc factor selection are forbidden.

The known radial solution `v=s1 E` corresponds to `(a,b,c,k)=(1,1,1,4)` and is a provenance/control anchor only; the solver must determine the full nullspace independently.

## Frozen outcomes

Return exactly one scoped classification:

- `K5_S5_FACE_TANGENT_LOG_IBP_DEG2_NONRADIAL_EXISTS_EXACT_SCOPED` if the exact degree-two logarithmic solution space contains at least one direction linearly independent of `s1 E`;
- `K5_S5_FACE_TANGENT_LOG_IBP_DEG2_RADIAL_ONLY_EXACT_SCOPED` if the exact degree-two logarithmic solution space is precisely the one-dimensional span of `s1 E`, while the degree-one space is precisely the Euler span;
- `K5_S5_FACE_TANGENT_LOG_IBP_DEG2_INCONCLUSIVE_SCOPED` if the exact system is constructed but a complete exact nullspace cannot be certified;
- `INVALID_IMPLEMENTATION`, `INVALID_PROVENANCE`, or `INFRASTRUCTURE_FAILURE` for non-scientific failures.

## Mandatory checks and controls

A valid implementation must:

- independently reconstruct all 125 K5 spanning-tree monomials and coefficient-one Kirchhoff polynomial;
- verify the edge-stabilizer orbit sizes `(1,6,3)` and therefore completeness of the three-parameter degree-two equivariant ansatz;
- solve degree-one and degree-two systems by exact rational row reduction;
- verify the returned basis vectors by direct polynomial substitution;
- verify that `(1,1,1,4)` is in the degree-two nullspace;
- quotient the degree-two nullspace by the radial span rather than merely count raw unknowns;
- reject a fake vector that does not satisfy the polynomial logarithmic identity;
- reject a field that is not face-tangent;
- reject an ansatz that breaks S5 edge equivariance;
- include a synthetic homogeneous polynomial fixture for which the same solver finds genuine non-radial degree-two logarithmic directions, so a hard-coded `radial-only` answer cannot pass;
- retain the interpretation that this gate does not evaluate the invariant-dual periods and does not prove absence of higher-degree, non-equivariant, or denominator-shifting IBP relations.

## Interpretation ceiling

If the result is `RADIAL_ONLY`, only the S5-equivariant regular face-tangent logarithmic class through component degree two is exhausted. The next admissible routes remain: degree three or higher logarithmic derivations; non-equivariant fields organized into exact S5 orbits; or denominator-shifting/index-changing IBP identities with a fresh Schwinger-boundary audit.

If a non-radial direction exists, the next gate must compute its exact action on the two actual invariant-dual degree-27 numerators and determine whether the resulting projective integral relation is nontrivial.

No K5 period zero/nonzero theorem, no full 217-dimensional tensor result, no finite-part selector, no regulator-independence result, no G3/F9/G8 promotion, no `NEW_PHYSICS_FOUND`, and no complete-QG claim follows from this gate.