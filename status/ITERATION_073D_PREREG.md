# Iter073D preregistration — transitive proper-face cone geometry

Date: 2026-09-13

## Objective
Resolve the internal geometry of every positive-admissible proper face found by Iter073A for the four transitive source classes. The purpose is to distinguish a merely positive nullity from a genuinely nondegenerate positive cone with explicit rational relative-interior witnesses and extreme rays.

## Scope
Reduced K4 common-epsilon signed cut-space geometry only. This is not an asymptotic coefficient theorem and not a distributional boundary-value result.

## Frozen panel
Source classes exactly `++++`, `+++-`, `++--`, `+---`; cycle bases exactly `S0,S1,P0,P1`. Recompute all nonempty proper subsets and retain only positive-admissible faces.

For each retained subset S form `A_S=L_S^T diag(s_S)` and the polyhedral cone `C_S={t>=0:A_S t=0}`.

## Frozen calculations
1. compute exact rank/nullity;
2. enumerate primitive nonnegative rational/integer extreme rays of `C_S` by exact support-minimal nullspace enumeration;
3. construct an exact strictly positive relative-interior witness as the primitive sum of all extreme rays and verify every active component is positive;
4. normalize the witness by `sum(t)=1` and record exact rational coordinates;
5. determine the affine dimension of the normalized section `C_S cap {sum t=1}` and verify it equals `nu_S-1`;
6. record extreme-ray count/support pattern and S4 orbit signature.

## Frozen predicates
P1. Every Iter073A-positive proper face is recovered and no new face is introduced.
P2. Every cone has at least one extreme ray and an exact strictly positive relative-interior witness.
P3. Normalized-section affine dimension equals `nu_S-1` exactly.
P4. The three `(m,nu)=(5,2)` faces per source class have a nondegenerate one-dimensional normalized section with at least two distinct extreme rays.
P5. Results are basis-consistent after mapping back to canonical edge coordinates.
P6. S4-related source classes have identical orbit-level cone signatures.
P7. Negative control: a nontransitive source class (`++-+`) has no proper positive cone and therefore no relative-interior witness.

## Classification
PASS: `ITER073D_TRANSITIVE_PROPER_FACE_CONES_NONDEGENERATE_EXACT_SCOPED`

otherwise: `ITER073D_PROPER_FACE_CONE_GEOMETRY_FAIL`

## Claim lock
A PASS proves nondegeneracy of the allowed positive Schwinger face cones only. It does not prove a nonzero epsilon-asymptotic coefficient, because the full coefficient may include numerator, phase, transverse Jacobian and cancellations between strata. No physical sector selection, vertex finiteness/divergence theorem, K5, G3, F9, G8, complete-QG or new-physics claim follows.
