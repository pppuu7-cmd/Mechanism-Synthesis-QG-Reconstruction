# Iter083G adversarial review

Date: 2026-09-15
Verdict: **CONFIRMED_SCOPED**

Reviewed result: `results/ITER083G_SM_S5_REGULATOR_METRIC_NONUNIQUENESS_RESULT.md`.

## 1. Prospective integrity
The scientific target was frozen before implementation at commit `e1312b7c59641e53f978130a506d0f4a3dd0bd1d`: exact S5 edge action, invariant-form dimension, independent representation cross-check, explicit inequivalent positive metrics, source/framework lock, and the requirement not to infer actual K5 Q-dependence.

The first run failed only the literal P6 manifest phrase. Its logs already showed P1-P5 and P7 true, `dim=3`, rank 52, the correct characters, and the positive Q2 witness. The repair added only wording to the manifest. The authoritative run `34915066408` passed all frozen predicates and controls.

No outcome-dependent mathematical criterion was changed.

## 2. Exact combinatorial attack
A symmetric bilinear form on the ten edge basis is determined by its values on unordered pairs of edges. Under S5 there are exactly three such orbits: same edge, adjacent distinct edges, disjoint edges. Therefore the invariant symmetric-form dimension cannot be less than or greater than three.

The production orbit sizes `10,30,15` exhaust all 55 symmetric entries.

This gives an elementary proof independent of the character decomposition.

## 3. Representation-theory attack
The edge permutation character is exactly

`(10,4,2,1,1,0,0)`.

It decomposes as the trivial representation plus the standard representation plus the irreducible character

`(5,1,1,-1,1,-1,0)`.

The last character has class-inner-product norm one and is orthogonal to the first two. Hence

`R^10 = [5] + [4,1] + [3,2]`

with multiplicity one for each real irreducible. Schur’s lemma again gives three invariant symmetric scalar sectors.

No preferred-edge artifact is present.

## 4. Positive-cone attack
A three-dimensional vector space of invariant symmetric forms would not by itself prove multiple admissible metrics if positivity collapsed it to one ray. It does not.

`Q1=I` is positive. `Q2=I+(1/10)A_L(K5)` has exact eigenvalues

`8/5, 11/10, 4/5`.

Thus both are positive and Q2 is not a scalar multiple of Q1. There is an open positive cone with nontrivial shape freedom.

## 5. “But Dang–Zhang call Q canonical” attack
This does not falsify the scoped result. Dang–Zhang choose the standard Euclidean quadratic form on their regulator coordinates and prove a mathematically consistent renormalization theorem using that choice. The result does not claim their theorem is internally ambiguous after that convention is fixed.

The MSQGR question is different: whether the already validated Lorentzian K5 source data plus S5 symmetry *derive* that convention as the unique physical choice. They do not. Exact S5 allows Q1, Q2 and the full positive invariant cone.

Adopting Q=I remains a legitimate mathematical scheme choice, not yet a source-derived K5 normalization law.

## 6. Stronger locality/functoriality loophole — RETAINED
The full multivariate renormalization framework imposes consistency/factorization properties beyond S5 covariance. A stronger requirement that regulator coordinate subspaces for appropriate independent factors be Q-orthogonal could reduce the invariant cone, potentially even to the Euclidean ray.

Iter083G does not test or exclude that stronger possibility for the K5 source object.

This is a real next-step loophole, not a defect in the scoped theorem.

A successor may ask whether source-faithful edge/subgraph factorization, deletion/contraction, forest restriction, or multivertex composition induces enough orthogonality/functoriality to fix the Q sectors.

## 7. Actual-germ independence loophole — RETAINED
Even if the projection map depends on Q on the full meromorphic-germ space, the specific K5 regularized germ might lie in a Q-independent subspace. Therefore

`Q1 != Q2`

does not imply

`R_Q1(K5) != R_Q2(K5)`.

The result explicitly does not make that inference.

The decisive future test is to construct the source-faithful K5 multivariate Laurent/polar germ, or at least its authoritative leading resolved-forest polar part, and evaluate/prove the Q-dependence or Q-independence of its holomorphic projection.

## 8. Relation to F8
If two admissible schemes do differ, Iter083B places their difference in the exact 377-dimensional supported ambiguity `F8`. This is a classification of the target of scheme dependence, not evidence that the difference is nonzero.

The result respects that direction of implication.

## 9. External-framework applicability ceiling
Dang–Zhang work with Euclidean Feynman amplitudes built from Green kernels and spectral zeta regularization. Iter083G uses only the algebraic fact that their holomorphic projection is tied to a quadratic form on regulator-parameter space. It does not assert their analytic continuation theorem applies automatically to Lorentzian Toller K5.

Any actual K5 meromorphic-germ construction must be proved separately.

## 10. Conclusion
The exact scoped statement survives adversarial review:

**S5 relabeling symmetry alone does not uniquely determine the regulator-parameter quadratic form required by this Q-based class of multivariate holomorphic projections.**

What remains open is whether stronger source-derived locality/functoriality fixes Q, or whether the actual K5 polar germ is projection-independent despite the available Q freedom.

No unique-extension impossibility theorem, generic-spin theorem, regulator-dependence theorem, full K5 renormalization theorem, G3/F9/G8/K5 promotion, NEW_PHYSICS_FOUND, or complete-QG claim follows.