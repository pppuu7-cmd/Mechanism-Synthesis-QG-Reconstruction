# Iter078P-RG preregistration — exact multiplicative input symmetry of the fixed-j=1/2 refinement control

**Date:** 2026-09-14

## Scientific question

Iter078M found Jacobian rank `31` at four distinct points; Iter078N ruled out a fixed universal left-null/output-hyperplane explanation. Does the exact degree-5 tensor network possess a nontrivial **input multiplicative symmetry**

`C_i -> z^(q_i) C_i`

that leaves every contraction monomial invariant and therefore enforces a structural right-kernel of the Jacobian?

## Frozen map

Use exactly the Iter078H EPRL-edge-weight fixed-all-`j=1/2` map. A raw contraction configuration is specified by:

- one of 32 external tuples `e=(e_0,...,e_4)`;
- one of `2^10=1024` internal intertwiner assignments;
- five local component indices `i_a in {0,...,31}` entering the product `prod_a C_(i_a)`.

There are exactly `32768` raw configurations.

The edge/face weights multiply monomial coefficients but do not affect the exponent count of the input variables. Therefore the same charge-equation analysis is also an exact topology/slot-convention control for the unit-edge-weight map.

## Lane A — exact charge-nullspace

For every raw configuration form one integer row `m in Z^32` whose component `m_i` counts how many of the five local factors use tensor component `C_i`.

A multiplicative charge vector `q in Q^32` leaves every monomial invariant iff

`m·q = 0`

for every one of the 32768 rows.

Compute the exact row rank over `Q` of this integer charge matrix and the full right-nullspace dimension.

If nonzero, emit a deterministic primitive integer basis for the nullspace and verify every basis vector against all 32768 rows exactly.

## Lane B — pointwise Jacobian generator verification

For each nonzero primitive charge vector `q` from Lane-A recomputation, define the infinitesimal generator at a tensor `C` by

`n_q(C)_i = q_i C_i`.

At the frozen Iter078M generic points A/B/C:

- verify `J(C)n_q(C)=0` exactly;
- compare the span of these generated vectors with the full exact right-nullspace of `J(C)`.

At the compact tensor `L`, record separately whether `n_q(L)` vanishes, spans the observed Iter078J null line, or is only part of a larger/special kernel.

No conclusion about L is frozen in advance.

## Lane C — exact finite symmetry, not only infinitesimal

For every primitive charge vector `q` and every raw monomial with exponent-count row `m`, verify `m·q=0`. This proves coefficientwise that for any formal nonzero parameter `z`

`R(z^q ⊙ C)=R(C)`

exactly, not merely to first order.

Also record the charge patterns in the 5-bit component basis and compare prospectively against the frozen simple ansatz space

`q(k_0,...,k_4)=a_0 + sum_r a_r k_r`

by solving for rational `a_r`. This comparison is descriptive only; the exact nullspace is primary.

## Lane D — structural rank consequence

If the charge-nullspace has dimension `d>0`, prove the exact rank bound

`rank J(C) <= 32-d`

on the Zariski-open set where the `d` infinitesimal generators `q^(s)⊙C` are linearly independent.

Use the frozen A/B/C points as positive controls: the generated symmetry span must account for their observed Jacobian nullity.

If the charge-nullspace is zero, classify the multiplicative-symmetry hypothesis as FAIL and do not infer a structural rank bound.

## PASS

PASS iff a nonzero exact charge-nullspace is found and coefficientwise invariance is verified for every raw contraction configuration.

Classification:

`ITER078P_RG_FIXED_JHALF_1TO5_CONTROL_HAS_EXACT_INPUT_TORUS_SYMMETRY_STRUCTURAL_JACOBIAN_KERNEL_SCOPED`

The result must report the exact charge-nullspace dimension and primitive basis.

## FAIL

`ITER078P_RG_NO_NONTRIVIAL_INPUT_MULTIPLICATIVE_CHARGE_SYMMETRY`

if the exact charge matrix has nullity zero.

## Interpretation ceiling

Even PASS identifies a redundancy of the **fixed-spin pure order-zero tensor-network control parameterization**, not automatically a physical gauge symmetry of the causal-Toller theory. Quotienting by it in a physical RG flow requires a separate bridge from the control tensor coordinates to the actual extension-coupling space.

No unique K5 extension, physical RG fixed point, regulator independence, generic-spin theorem, G3 or complete-QG claim follows.