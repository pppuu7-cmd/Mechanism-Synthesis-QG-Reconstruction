# Prospective preregistration — symbolic full-source boundary S5 transport theorem

Date: 2026-09-17

This gate is frozen before implementation or inspection of any symbolic transport result. It is a new Researcher theorem gate, not an independent Critic review and not a competing reclassification of the witness-scoped gate.

## HYPOTHESIS

For the exact all-`j=1/2` source-ordered K5 order-zero boundary Wick covector, simultaneous permutation of Schwinger edge variables, source wedge endpoint/orientation data, and the complete 32-state boundary basis obeys the ordinary contragredient S5 law as an exact rational-function identity in the Schwinger variables:

`a_p(p alpha) = A_p^(-T) a(alpha)`.

There is no additional permutation-sign character once canonical-edge reversal is handled by the source-defined endpoint transpose and the exact source reversal sign `M(-v)=-M(v)`.

It is sufficient to prove the identity for the frozen generators

- `C=(1,2,3,4,0)` (five-cycle),
- `T=(1,0,2,3,4)` (transposition),

provided the same exact transport maps are also verified to compose and generate all 120 elements of S5.

## exact OBJECT

The object is the complete unprojected 32-component source boundary covector before invariant-dual projection, retaining the exact source ordering

`one-wedge spectral/spinor integration -> Toller function -> product of ten Toller matrices -> full boundary contraction -> K5 group/distributional object`.

At this gate only the already-authoritative order-zero source/Wick kernel is used. Every boundary component is represented by its complete source node-choice expansion; across the 32 components the source support is exactly 100000 node-choice terms.

The theorem is to be proved without choosing numerical Schwinger witnesses. The implementation must separate the identity into two exact formal layers:

1. **Schwinger/covariance layer.** Construct `Psi_K5(alpha)` and the edge-edge covariance numerators as exact multivariate polynomial dictionaries. Verify under `C` and `T` that the rational covariance kernel transforms with precisely the canonical-edge orientation signs dictated by the incidence vectors.
2. **Source/boundary layer.** Construct the complete source-entry pattern coefficient dictionaries for all 32 boundary components. Apply the source-defined endpoint/orientation transport, including `(row,col)->(col,row)` on canonically reversed target edges and the exact reversal sign. Verify coefficient-dictionary equality with the exact 32-dimensional contragredient boundary action, before any covariance value is substituted.

If both formal layers hold and their transport maps compose, the all-alpha rational-function boundary law follows algebraically. No finite-witness interpolation is permitted as theorem authority.

## DEPENDENCY

Tests the bridge

`source-defined endpoint/orientation transport + exact K5 Schwinger covariance + complete 32-state boundary action -> symbolic coefficient-level S5 covariance`.

This gate does not consume the witness-scoped Researcher classification as confirmed authority; it independently uses the same underlying source formulas and terminal parent objects. Its purpose is to determine whether the source transport needed by the already-frozen exact-leading-coefficient cancellation resolver is available as a structural identity rather than only on frozen witnesses.

## SOURCE AUTHORITY

Locked inputs:

- corrected Iter077I source ordering and full all-32 boundary contraction authority;
- published one-wedge spectral `i epsilon` retained;
- exact all-`j=1/2` leading source matrix and source endpoint convention from `distributional/iter077i_sm_source_ordered_jhalf_k5_l1.py`;
- exact boundary tensor/action construction used by `scripts/k5_order8_invariant_dual_projective_ibp_reachability.py` and the terminal invariant-dual object;
- exact source pattern construction used by the terminal physical numerator DAG/action machinery;
- exact orientation-sensitive source-entry transport established separately: on a canonically reversed edge transpose the endpoint entry and retain the source reversal sign from `M(-v)=-M(v)`;
- source-fixed repair-5 mismatch remains quarantined as a negative object-definition control and is not rewritten.

Historical source-lock-invalid Iter077E/F remain quarantined. No scalar K4/K5 surrogate is admissible.

## FROZEN INPUTS

- all ten K5 edges with the repository canonical ordering;
- all five vertices;
- all 32 all-spin-half boundary intertwiner components;
- exactly 100000 source node-choice terms in the complete boundary vector;
- generator `C=(1,2,3,4,0)`;
- generator `T=(1,0,2,3,4)`;
- exact rational / Gaussian-rational arithmetic for source coefficients;
- exact sparse integer/rational polynomial dictionaries for formal Schwinger identities;
- the existing exact 32-dimensional boundary action, reconstructed from source boundary tensors rather than fitted from amplitudes;
- canonical edge orientation and source endpoint transpose on reversal;
- no boundary state selection, no fitted phase, no fitted 2x2 matrix, no numerical alpha witness, no interpolation grid, no floating-point tolerance.

## POSITIVE CONTROLS

P1. `C` and `T` generate exactly 120 vertex permutations under the frozen composition convention.

P2. Boundary matrices satisfy exact generator/group controls, including `T^2=I`, `C^5=I`, and exact inverse matrices from inverse permutations.

P3. Source matrix reversal is exact: `M(-v)=-M(v)` on a basis spanning the source leading matrix.

P4. The edge permutation/orientation map is bijective and composes exactly on all ten edges.

P5. The Kirchhoff polynomial has 125 coefficient-one spanning-tree monomials and is exactly invariant under both frozen generators after variable transport.

P6. Every formal covariance numerator transforms with the exact incidence/orientation sign required by simultaneous edge transport; denominator transport is exactly `Psi -> Psi`.

P7. The source-pattern census retains all 32 components and exactly 100000 original source terms.

P8. Source-pattern transport and inverse transport are exact round trips.

P9. The full formal source/boundary coefficient dictionaries obey the contragredient boundary law for both `C` and `T` componentwise, without covariance substitution.

P10. The generator-level formal transport action composes consistently; therefore the proven law extends to all 120 S5 elements without adding a post-hoc character.

P11. Invariant-dual rank-two/pivots `[1,4]` remain a control only; the theorem verdict is decided by the complete 32-vector formal identity.

## NEGATIVE CONTROLS

N1. Omitting `(row,col)->(col,row)` on reversed edges must be detected as a failure for the odd generator `T`.

N2. Removing the source reversal sign while retaining transpose must be detected.

N3. Substituting the deliberately source-fixed repair-5 transport object for the simultaneous source transport must not satisfy the new formal theorem contract.

N4. A fabricated extra `sgn(p)` character must be rejected by the odd-generator formal identity whenever the exact transported formal covector is nonzero.

N5. A fitted constant two-channel matrix is forbidden and must not enter the theorem implementation.

N6. Numerical witness equality, interpolation, or floating arithmetic cannot satisfy the symbolic-theorem acceptance path.

## PASS

Classify

`K5_FULL_SOURCE_BOUNDARY_S5_SYMBOLIC_ALL_ALPHA_TRIVIAL_CHARACTER_EXACT_SCOPED`

iff P1-P11 and N1-N6 all pass and the exact formal generator identities imply the full rational-function law for all `p in S5` on the domain `Psi_K5 != 0`.

## FAIL

Classify

`K5_FULL_SOURCE_BOUNDARY_S5_SYMBOLIC_TRANSPORT_OBSTRUCTION_EXACT_SCOPED`

if the correctly source-transported formal covariance/source/boundary object violates the frozen contragredient law for either generator, or if the generator transport maps fail exact composition, while provenance and implementation controls remain valid. Such a FAIL is an obstruction to using S5 covariance to move exact cancellation data between orbit representatives under the current source object.

## BLOCKED

Classify `BLOCKED_OBJECT_DEFINITION` if a source-faithful formal covariance numerator, source-pattern transport, boundary action, orientation map, or composition law cannot be constructed from repository authority without inventing a surrogate or normalization.

## INVALID

Use `INVALID_IMPLEMENTATION`, `INVALID_PROVENANCE`, or `INFRASTRUCTURE_FAILURE` for non-scientific failures, including incomplete source-term coverage, malformed polynomial transport, arithmetic fallback to floating point, or failure of a required positive/negative control.

## INTERPRETATION CEILING

A PASS proves only the exact order-zero full-source boundary S5 transport identity and supplies coefficient-level covariance authority for later prospectively frozen/repaired cancellation work after independent Critic review. It does not itself compute any degree-27 numerator cancellation order, degree-31 action cancellation order, projective-normal flux coefficient, physical Schwinger-corner exponent, local finiteness/divergence result, global Stokes/IBP relation, invariant-dual K5 period, full 217-dimensional tensor theorem, reduction of `dim_C F_8=377`, physical finite-part selector, regulator independence, G3/F9/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete quantum gravity.
