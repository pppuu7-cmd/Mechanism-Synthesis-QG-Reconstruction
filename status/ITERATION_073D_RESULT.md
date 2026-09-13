# Iter073D result — transitive proper-face cone geometry

Date: 2026-09-13

## Authority

- preregistration commit: `c112d01cecc1aec817dcfdcfbe665a8cb8737729`
- implementation commit: `930b134519f8d684fe42c7db8c6bcfe29a9754c5`
- authoritative workflow head: `48a21509026968b7bd7edc72f1ef759c585f1882`
- workflow run: `34748577817`
- job: `103701076340`
- artifact: `10314703065`
- digest: `sha256:f7509f97716e7736471b850e2205ff0cebf19801b94c6653b88d1d1ef4767b6a`

## Frozen classification

`ITER073D_TRANSITIVE_PROPER_FACE_CONES_NONDEGENERATE_EXACT_SCOPED`

All seven preregistered predicates passed.

## Exact result

For each transitive source class `++++`, `+++-`, `++--`, `+---`, Iter073D exactly recovers the six positive-admissible proper faces from Iter073A and resolves their polyhedral cone geometry.

Every admissible face has:

- at least one exact primitive nonnegative extreme ray;
- an exact strictly positive relative-interior witness obtained from the extreme rays;
- normalized-section affine dimension exactly `nu-1`;
- basis-consistent canonical edge-coordinate geometry;
- the same orbit-level signature across the four S4-related transitive source classes.

In particular, each of the three five-edge/nullity-two faces per transitive class has a genuinely nondegenerate one-dimensional normalized section with at least two distinct extreme rays.

The nontransitive negative control `++-+` has zero positive proper faces and therefore no relative-interior witness.

## Interpretation

The allowed transitive proper strata are genuine positive Schwinger cones, not artifacts of rank/nullity bookkeeping. Therefore the next question is whether their regulated asymptotic coefficients are nonzero after numerator, transverse Jacobian and symmetry/cancellation factors are included.

This result does not prove any `epsilon^-2`, `epsilon^-1` or finite coefficient is nonzero, and does not establish an `epsilon -> 0+` boundary value. No physical sector selection, causal-vertex finiteness/divergence theorem, K5, G3, F9, G8, complete-QG or new-physics claim follows.
