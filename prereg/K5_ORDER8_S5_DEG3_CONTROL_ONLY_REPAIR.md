# Prospective preregistration — K5 S5 degree-three logarithmic IBP control-only repair

Date: 2026-09-16

Parent scientific preregistration: `prereg/K5_ORDER8_S5_DEG3_FACE_TANGENT_LOG_IBP_SYZYGY.md`, commit `b93145159d9535992208a15a56c33b13732ad155`.

Outcome-independent implementation audit: `results/K5_ORDER8_S5_DEG3_IMPLEMENTATION_AUDIT.md`, commit `cf618ae9a3bbe8a4b97171dce973c2a4cb1b803f`.

This repair is frozen before any repaired implementation or repaired production output is inspected. It changes controls only; the scientific object, ansatz, exact identity, radial quotient, outcome labels, and interpretation ceiling are identical to the parent preregistration.

## Frozen scientific object

Use the same exact K5 125-term coefficient-one Kirchhoff polynomial on edge order `(01),(02),(03),(04),(12),(13),(14),(23),(24),(34)`.

Use the complete S5-equivariant regular face-tangent component-degree-three field

`v_e = alpha_e Q_e(alpha)`,

with homogeneous quadratic `Q_e` constructed from all fixed-edge-stabilizer orbits on degree-two edge monomials.

Use the complete S5-invariant homogeneous quadratic quotient space `H_2` and solve exactly over Q

`sum_e v_e d_e Psi_K5 = H_2 Psi_K5`.

The radial subspace remains all `F_2(alpha) E` with invariant quadratic `F_2`; the scientific quantity remains the exact quotient dimension by that full radial subspace.

## Frozen scientific outcomes

Exactly the parent labels remain allowed:

- `K5_S5_FACE_TANGENT_LOG_IBP_DEG3_NONRADIAL_EXISTS_EXACT_SCOPED` iff the exact repaired quotient dimension is positive;
- `K5_S5_FACE_TANGENT_LOG_IBP_DEG3_RADIAL_ONLY_EXACT_SCOPED` iff it is exactly zero;
- `K5_S5_FACE_TANGENT_LOG_IBP_DEG3_INCONCLUSIVE_SCOPED` iff the exact system is valid but exact rank/nullspace closure is not obtained;
- `INVALID_IMPLEMENTATION`, `INVALID_PROVENANCE`, or `INFRASTRUCTURE_FAILURE` for non-scientific failures.

No threshold or post-hoc ansatz change is permitted.

## Mandatory repaired controls

The repaired implementation must use a generic exact matrix/nullspace builder for both the real K5 polynomial and the synthetic fixture.

It must actually execute and pass all of the following:

1. **Non-face-tangent rejection.** Construct an explicit malformed vector field with at least one component containing a monomial not divisible by the corresponding `alpha_e`; the validator must reject face tangency.
2. **S5-breaking rejection.** Construct an explicit face-tangent polynomial vector field whose components are not related by the S5 edge action; the equivariance validator must reject it.
3. **Fake-logarithmic rejection.** Supply a candidate coefficient vector that fails the exact polynomial identity; matrix substitution must reject it.
4. **Synthetic same-engine positive control.** Use `Psi_syn=prod_e alpha_e`, build the same complete equivariant degree-three/logarithmic matrix from the same orbit basis, solve it exactly, and establish a positive non-radial quotient dimension. In addition, explicitly verify the known non-radial direction `v_e=alpha_e^3` with quotient `H_2=sum_e alpha_e^2` through that same matrix.
5. **K5 exact reconstruction.** Recover 125 degree-four coefficient-one spanning-tree monomials and exact 120-permutation equivariance.
6. **Exact basis substitution.** Substitute every repaired K5 nullspace basis vector back into the complete coefficient system.
7. **Full radial inclusion.** Verify every invariant-quadratic Euler multiple lies in the K5 nullspace and compute the quotient dimension by exact rank.
8. **No period promotion.** The output field `scientific_invariant_dual_period_verdict` must remain null.

## Provenance rule

The non-terminal/terminal output of original run `35042066501` is not scientific authority because implementation commit `9ac72afa...` failed the frozen mandatory-control contract. The repaired production must run from a new immutable head containing this preregistration and the repaired implementation.

## Interpretation ceiling

Unchanged from the parent gate: this can classify only the S5-equivariant regular face-tangent logarithmic module at component degree three. It cannot establish either invariant-dual K5 projective period, the full 217-dimensional tensor/annihilator, a physical finite-part selector, regulator independence, downstream G3/F9/G8, `NEW_PHYSICS_FOUND`, or complete quantum gravity.
