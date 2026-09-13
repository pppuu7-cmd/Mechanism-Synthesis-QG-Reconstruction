# Iter073A result — K4 signed cut-space proper-face atlas

Date: 2026-09-13

## Authority

- frozen preregistration commit: `8b87abc4aea6636b9e554729bba4670b91d9e7f3`
- authoritative workflow run: `34746503186`
- authoritative head: `9fb30be9831c01b4e13571e5dac2569fb95667d5`
- aggregate job: `103695339471`
- aggregate artifact: `10314755546`
- aggregate digest: `sha256:b1c46b3ac61eb4416df337514f1610a34c40e74901e6b765c8ffbd84f345fe7a`

All eight exact lanes and the aggregate completed successfully.

## Frozen classification

`ITER073A_K4_SIGNED_CUTSPACE_PROPER_FACE_ATLAS_EXACT_SCOPED`

The aggregate reports `all_exact_lanes_valid=true` and the preregistered negative control passes.

## Exact source-class split

For the four source classes whose full six-edge tournament is transitive,

- `++++`
- `+++-`
- `++--`
- `+---`

the maximal positive-admissible **proper-face** nullity is exactly `2`.  Each has the same basis- and S4-invariant proper-face histogram:

- two faces with `(m,nu)=(3,1)`;
- one face with `(m,nu)=(4,1)`;
- three faces with `(m,nu)=(5,2)`.

For the four nontransitive source classes,

- `++-+`
- `+-++`
- `+-+-`
- `+--+`

there is **no positive-admissible nonempty proper face at all** under the frozen signed cut-space criterion.  The aggregate records `max_feasible_proper_nullity=-1` and an empty proper-face histogram for each of these four classes.

## Full-set cross-check

The six-edge full-set result reproduces Iter072B exactly:

- transitive source classes have a strict-positive cut-space kernel of nullity `3`;
- nontransitive source classes do not;
- every full-set signed matrix nevertheless has algebraic nullity `3`, so nullity alone is not a positivity criterion.

## What this closes

Within the **reduced K4 common-epsilon rational family**, the source sign geometry is now completely classified at the level of positive Schwinger full and proper faces.  In particular, the four nontransitive source classes have neither a positive full-collision face nor any positive proper-collision face in this exact atlas.

## What this does not close

The face nullity is a geometric collision-degree indicator only.  This result does not prove that a corresponding `epsilon^-2`, `epsilon^-1`, or finite coefficient of the complete regulated Schwartz action is nonzero, nor does absence of a positive face by itself prove existence of a finite `epsilon -> 0+` distributional boundary value.  Oscillatory cancellation, boundary-value existence, Eq.(5)/(6) inheritance, the full Toller numerator/group dependence, K5, G3, F9 and G8 remain separate questions.

No physical causal-sector selection, causal-vertex finiteness/divergence theorem, complete-QG claim, or `NEW_PHYSICS_FOUND` claim is authorized by Iter073A.
