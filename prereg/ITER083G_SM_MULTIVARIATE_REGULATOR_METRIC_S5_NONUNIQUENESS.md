# Iter083G-SM preregistration — S5-invariant multivariate regulator metric nonuniqueness

Date: 2026-09-15
Status: PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION/PRODUCTION

## Scientific question
Can a Dang–Zhang / Speer-style multivariate analytic renormalization of the ten-edge K5 product be promoted to a symmetry-canonical joint-K5 selector solely from the already-authoritative source symmetries, or does the projection to the holomorphic germ require extra regulator-metric data not fixed by S5?

This gate is deliberately narrower than constructing the actual K5 meromorphic germ. It tests whether the regulator-parameter metric entering the multivariate projection is uniquely determined by the exact K5 relabeling symmetry.

## Frozen object
Let E be the real 10-dimensional vector space with basis indexed by the unordered edges {a,b} of K5. S5 acts by permuting vertices and hence edges. A candidate regulator-parameter quadratic form is a real symmetric 10x10 matrix Q. It is admissibly relabeling-covariant iff

P_sigma^T Q P_sigma = Q

for every sigma in S5.

The source-order firewall remains

one-wedge source construction -> ordinary Toller functions -> ten-wedge K5 product -> joint analytic regularization / extension.

No historical pre-product contact-distribution multiplication is reintroduced.

## External mathematical input to be source-locked
Dang–Zhang, JEMS 23 (2021), Sec. 6.2-6.3, defines a projection pi_p from meromorphic germs to holomorphic germs; Remark 6.8 states that the polar-germ subspace, and therefore pi_p, is determined by the quadratic form Q fixed in that section. Definition 6.10 then defines renormalization by evaluation of pi_p of the multivariate regularized amplitude.

This gate uses that statement only as a mathematical candidate framework, not as physical source authority for MSQGR.

## Prospective predicates
P0 SOURCE_ORDER_FIREWALL: the gate acts only on the post-Toller ten-edge K5 regulator-parameter space.

P1 EDGE_ACTION_COMPLETE: enumerate all 120 permutations of S5 and their exact 10x10 edge-permutation matrices.

P2 INVARIANT_FORM_DIMENSION: solve exactly over Q the linear system Q=Q^T and P_sigma^T Q P_sigma=Q for all sigma. Required result for the targeted theorem: invariant symmetric-form dimension 3. If not 3, theorem fails.

P3 ORBIT_BASIS: independently construct the three pair-orbit matrices: I (same edge), A (distinct edges sharing one vertex, line graph L(K5)), B (disjoint edges). Verify exact linear independence and invariance and that they span the solved invariant space.

P4 REPRESENTATION_CROSSCHECK: independently verify the 10-edge permutation representation has character decomposition [5] + [4,1] + [3,2], dimensions 1+4+5=10, hence one symmetric scalar on each real multiplicity-one irrep and therefore three invariant quadratic-form sectors.

P5 POSITIVE_INEQUIVALENT_METRICS: exhibit two positive-definite S5-invariant forms not related by common scalar, e.g. Q1=I and Q2=I+(1/10)A, and verify exact eigenvalues using the three irreducible sectors.

P6 LITERATURE_PROJECTION_LOCK: exact source-lock must state that the holomorphic projection pi_p is determined by the chosen quadratic form Q and that renormalization evaluates the projected holomorphic germ.

P7 AFFINE_TORSOR_SCOPE: consume authoritative Iter083B only for the statement that if two such schemes produce admissible same-off-collision, same-symmetry, same-scaling-degree K5 extensions, their difference lies in F8 with dim_C F8=377. Do not infer that changing Q actually gives a nonzero physical difference without computing the real K5 meromorphic germ.

## Exact expected invariant basis/eigenvalues
With A the adjacency matrix of L(K5) and B=J-I-A, every S5-invariant symmetric form should be

Q=a I + b A + c B.

Expected eigenvalues on [5], [4,1], [3,2]:

lambda_[5]   = a + 6 b + 3 c,
lambda_[4,1] = a + b - 2 c,
lambda_[3,2] = a - 2 b + c.

Positive definiteness is equivalent to all three being positive.

For Q2=I+(1/10)A the exact eigenvalues should be 8/5, 11/10, 4/5, so Q2 is positive definite and not proportional to I.

## Negative controls
- reject any preferred edge label or unequal diagonal edge weights;
- reject the false claim that S5-invariant Q is unique up to overall scale;
- reject interpreting the 3-dimensional Q-space as three physical counterterm coefficients;
- reject interpreting the exact 377-dimensional F8 as proof that Q-dependence is nonzero;
- reject treating Dang–Zhang Euclidean spectral-zeta renormalization as source authority for the Lorentzian causal vertex;
- reject reusing the one-wedge spectral epsilon as this regulator metric (Iter083F already excludes that move);
- retain the falsifier that the actual K5 meromorphic germ may be independent of Q;
- retain the possibility that a future source-derived composition/positivity/RG law uniquely fixes Q or bypasses Q entirely.

## Success classification
If P0-P7 and all controls pass:

ITER083G_SM_S5_INVARIANT_TEN_EDGE_REGULATOR_METRIC_HAS_THREE_SECTORS_SO_Q_BASED_MULTIVARIATE_PROJECTION_NOT_SYMMETRY_UNIQUE_SCOPED

Verdict: PASS_EXACT_SCOPED.

## Interpretation ceiling
A PASS does not prove that the physical K5 renormalized amplitude depends on Q. It proves only that S5 symmetry and the presently validated local source data do not uniquely determine the Q-input required by this class of multivariate holomorphic-projection schemes. The next nonredundant test must construct or model the actual K5 multivariate meromorphic germ/polar part and test whether its projected value is Q-independent or Q-dependent.

No generic-spin theorem, no full causal-vertex finiteness theorem, no regulator independence, no unique extension impossibility against all future laws, no G3/F9/G8/K5 promotion, no NEW_PHYSICS_FOUND, and no complete-QG claim.