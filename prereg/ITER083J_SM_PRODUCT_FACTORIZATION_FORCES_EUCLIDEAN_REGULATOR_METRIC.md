# Iter083J-SM preregistration — universal product factorization forces the Euclidean regulator-metric ray

Date: 2026-09-15
Status: PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION/PRODUCTION

## Scientific question
Iter083G found a three-sector family of positive S5-invariant regulator metrics and Iter083I showed that generic members change proper/nested forest pole complements. Does the stronger **universal product-factorization/naturality** property of the multivariate holomorphic projection force the metric family back to the Euclidean ray `Q_p proportional I_p`?

This is a theorem about the Q-based projection framework. It is not yet a claim that the connected Lorentzian K5 source object physically authorizes the full universal tensor-product axiom.

## External mathematical framework lock
Dang–Zhang JEMS 23 (2021), Lemma 7.2, proves for their projection family that for independent tensor-product meromorphic distributions with regulator blocks of sizes p1,p2,

`pi_(p1+p2)(t1 tensor t2) = pi_p1(t1) tensor pi_p2(t2)`.

The same paper defines polar germs using the Q*-orthogonality of pole linear forms and numerator variables and fixes the standard Euclidean Q on each regulator parameter space.

Iter083J asks whether these two structural properties, abstracted to a general nondegenerate Q-family, force the Euclidean ray.

## Frozen algebraic test
For distinct regulator coordinates i != j, take

`t_i=1/x_i` (pure simple polar germ),

`h_j=x_j` (holomorphic independent factor).

Product factorization requires

`pi_p(x_j/x_i)=0`.

For a general nondegenerate Q, decompose the numerator covector

`e_j^* = c_ij e_i^* + ell_perp`,

where `Q*(e_i^*,ell_perp)=0`. Then

`c_ij = Q*(e_i^*,e_j^*) / Q*(e_i^*,e_i^*)`

and

`x_j/x_i = c_ij + ell_perp/x_i`.

The second term is polar, so

`pi_p(x_j/x_i)=c_ij`.

Therefore universal factorization for all i!=j implies all off-diagonal entries of Q* vanish.

## Prospective predicates
P0 FRAMEWORK_SOURCE_LOCK: exact source lock must record Dang–Zhang polar Q*-orthogonality and Lemma 7.2 product factorization, while retaining the Lorentzian-K5 applicability ceiling.

P1 TWO_COORDINATE_THEOREM: mechanically derive the projection constant `c_ij=Q*ij/Q*ii` and verify factorization iff `Q*ij=0` for every ordered pair i!=j.

P2 ALL_PAIR_ORTHOGONALITY: for p=10, universal 1+(p-1) factorization over all 90 ordered distinct coordinate pairs forces Q* diagonal.

P3 S5_EQUAL_DIAGONALS: because the K5 vertex-relabeling action is transitive on the ten edge coordinates, S5 invariance of a diagonal Q* forces all ten diagonal entries equal. Hence `Q*=c I` and `Q=c^-1 I`.

P4 SCALE_IRRELEVANCE: multiplying Q by one nonzero common scalar does not change orthogonality, polar germs or pi_Q. Thus the projection is unique on the Euclidean ray; positivity fixes c>0 but no physical scale is selected.

P5 ITER083G_Q2_REJECTION: for authoritative `Q2=I+(1/10)A_L(K5)`, verify exactly

- Q2* diagonal entries `185/176`;
- adjacent-edge off-diagonal entries `-15/176`;
- disjoint-edge off-diagonal entries `5/176`;
- resulting factorization-violation constants `-3/37` and `1/37`.

Therefore Q2 is S5 invariant and positive but not compatible with the universal product-factorization axiom.

P6 ITER083I_RECONCILIATION: consume Iter083I only to state that its forest Q-sensitivity uses a metric excluded by the stronger naturality class. Do not erase the valid result that S5 alone is insufficient.

P7 K5_SOURCE_APPLICABILITY_FIREWALL: theorem must explicitly distinguish universal tensor-product naturality across independent regulator blocks/graphs from the connected K5 product of ten Toller factors sharing group variables. A successor source audit is required before promoting this mathematical uniqueness to a physical K5 selector.

## Negative controls
- reject deriving Q proportional I from S5 alone;
- reject assuming Q2 is invalid before the factorization test;
- reject identifying universal tensor-product factorization with ordinary multiplication of ten connected K5 wedge functions;
- reject fixing the overall positive scalar as physical data;
- reject claiming a unique physical K5 extension from this theorem;
- retain Iter083G/I as valid in the broader S5-only scheme class;
- retain the possibility that connected-K5 source locality does not license arbitrary regulator-block factorization;
- retain the possibility of non-Q-based renormalization schemes.

## Expected classification if PASS
`ITER083J_SM_UNIVERSAL_PRODUCT_FACTORIZATION_PLUS_K5_EDGE_TRANSITIVITY_FORCES_Q_EUCLIDEAN_RAY_SCOPED`

Verdict: `PASS_EXACT_SCOPED`.

## Research consequence if PASS
The Q ambiguity discovered in Iter083G and geometrically activated in Iter083I is not intrinsic to the strongest natural product-factorizing projection class: it collapses to the Euclidean ray. The next decisive question is then source applicability — whether the physical connected causal-K5 construction supplies or requires the same universal factorization/naturality law. If it does, a canonical Q-based projection becomes a serious physical selector candidate; if not, Q-shape freedom remains available.

## Interpretation ceiling
No physical source authorization of the factorization axiom; no full K5 meromorphic continuation theorem; no unique physical extension; no regulator independence; no generic-spin theorem; no G3/F9/G8/K5 promotion; no `NEW_PHYSICS_FOUND`; no complete-QG claim.