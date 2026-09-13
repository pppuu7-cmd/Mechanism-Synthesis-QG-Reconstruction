# Iter076B preregistration — transitive degree-two overlap-jet covariance

Date: 2026-09-13

This gate is frozen prospectively before implementation and production.

## Objective

Construct the exact degree-two local jet bookkeeping that must exist before the nominal `epsilon^-1` collision coefficient can be meaningfully evaluated on the reduced transitive K4 denominator skeleton.

Iter074A established that degree-zero and degree-one local terms cancel after the complete independent-sign/S4 alternating sum, while degree two is the first overlap-sensitive order. Iter076A established the exact 13-node intersection-poset/Möbius bookkeeping for the six positive proper faces of every transitive source class.

Iter076B does **not** assign a physical `epsilon^-1` coefficient. It asks a narrower prerequisite question: do the quadratic jets restricted to all overlap strata, together with the exact Iter076A incidence/Möbius data, define a basis-independent and S4-covariant algebraic restriction complex?

## Frozen inputs

- transitive source classes: `++++`, `+++-`, `++--`, `+---`;
- cycle bases: `S0,S1,P0,P1`;
- K4 six-edge linear map `x=L z` from the existing exact cut/cycle implementation;
- the six positive proper faces and their full nonempty intersection closure are recomputed, not hard-coded;
- degree-two jet basis in cycle coordinates: `z0^2,z1^2,z2^2,z0*z1,z0*z2,z1*z2`;
- no fitted coefficients, no finite-part prescription, no counterterm and no sequential integration order.

## Frozen construction

For each source class and cycle basis:

1. Reconstruct the Iter076A overlap support poset and exact Möbius function.
2. For every support node `S`, compute exactly the linear subspace `V_S = ker(L_S)` in cycle coordinates.
3. Construct the restriction map from the six-dimensional space of homogeneous quadratic jets to quadratic functions on `V_S`. Its rank is computed exactly over the rationals from a canonical nullspace basis.
4. Record for every comparable inclusion `A subseteq B` the induced compatibility of quadratic restrictions under `V_B subseteq V_A`.
5. Form the exact incidence-weighted rank/signature data using the already frozen Möbius coefficients. This is bookkeeping only: Möbius coefficients are not physical subtraction coefficients.

## Frozen predicates

P1. The recomputed support poset and Möbius top column must exactly reproduce Iter076A for every class/basis.

P2. Every node restriction map must have exact rational rank and the expected monotonicity: if `A subseteq B`, then `V_B subseteq V_A` and the quadratic restriction rank on `B` cannot exceed that on `A`.

P3. Restriction compatibility must hold exactly on every comparable pair: restricting a quadratic jet directly to `V_B` must agree with restriction through `V_A` followed by the exact subspace embedding.

P4. Under every unimodular cycle-basis change already used in Iter074A/Iter073D, the complete multiset of `(support-cardinality, nullity, quadratic-rank, mu-to-top)` records must be invariant within each source class.

P5. The canonical unlabeled quadratic-overlap signature must agree across the four S4-related transitive source classes.

P6. At least one proper/intersection stratum must retain nonzero quadratic rank. This is a negative control against an implementation that accidentally annihilates all degree-two data; PASS therefore must **not** be interpreted as cancellation of the nominal `epsilon^-1` term.

P7. The nontransitive control `++-+` must still produce no transitive six-face overlap complex.

## Frozen interpretation

If P1-P7 all pass:

`ITER076B_TRANSITIVE_DEGREE2_OVERLAP_JET_COMPLEX_EXACT_COVARIANT_SCOPED`

Meaning: the reduced K4 transitive overlap geometry supports an exact basis/S4-consistent quadratic restriction complex, so a later coefficient gate may contract a **source-derived** numerator/Jacobian quadratic jet against this object. This does not determine whether the coefficient vanishes.

If an exact scientific predicate fails:

`ITER076B_TRANSITIVE_DEGREE2_OVERLAP_JET_COMPLEX_OBSTRUCTED_SCOPED`

Execution/import/environment failures are infrastructure failures only and do not alter the frozen science.

## Next gate if PASS

Only after terminal PASS may a separate prospectively frozen coefficient gate insert an explicit numerator/Jacobian quadratic jet. That later gate must state the origin of every factor and must not infer cancellation from Möbius bookkeeping alone.

## Claim lock

Reduced denominator-skeleton algebra only. No source-defined distributional Eq.(5)/(6), no physical causal-vertex finiteness/divergence theorem, no K5/G3/F9/G8 promotion, no physical sector selection, no arbitrary counterterm or fitted cancellation, no complete QG or new physics.