# Iter083J-SM — universal product factorization plus K5 edge transitivity forces the Euclidean regulator-metric ray

Date: 2026-09-15
Status: **PASS_EXACT_SCOPED**

## Provenance
- preregistration `88cf18c9d531986ef19dfe2f8cb502ae5e4af9ce`;
- source/framework lock `f8865c1305b6ad0ab51e8b87e1872778ac834dca`;
- validator initial `2070d06b5d507e750c1922b7566d4cc6f4ed55b3`;
- workflow `cab95384f4a28bbd5b570d0dac01988127616f3c`;
- first run `34916144578` failed only literal provenance locks while P1-P4 and the exact Q2 algebra already passed;
- wording-only validator repair `746b7640944426f61c80059650bf7b6dd0bfe80f`;
- authoritative run `34916275666`, job `104214473636`, terminal success;
- artifact `10375888411`, ZIP digest `sha256:a9036cc50051f3848559b3d4f08958e20eab7056da59ff6c1f2f38927b427d6b`;
- production JSON SHA256 `ab27cfbb7049ce155d2e84110377ec5bda293ef1f7ac538acabd43bbf88fed5b`.

## Classification
`ITER083J_SM_UNIVERSAL_PRODUCT_FACTORIZATION_PLUS_K5_EDGE_TRANSITIVITY_FORCES_Q_EUCLIDEAN_RAY_SCOPED`

Verdict: **PASS_EXACT_SCOPED**.

## Framework statement
For a Q-based polar-germ projection, take two distinct regulator coordinates i != j. Let

`t_i=1/x_i`,

`h_j=x_j`.

Universal tensor-product factorization requires

`pi(x_j/x_i)=pi(1/x_i) x_j=0`.

Decompose the numerator covector with respect to Q*:

`e_j^*=c_ij e_i^* + ell_perp`,

`Q*(e_i^*,ell_perp)=0`.

Then

`c_ij=Q*_(ij)/Q*_(ii)`

and

`x_j/x_i = c_ij + ell_perp/x_i`.

The second term is polar. Therefore the holomorphic projection is exactly the constant

`pi(x_j/x_i)=c_ij`.

Universal product factorization is equivalent, for every distinct coordinate pair, to

`Q*_(ij)=0`.

## Exact ten-edge consequence
For the ten K5 edge regulators production checks all

- 90 ordered distinct-coordinate tests;
- 45 unique off-diagonal entries.

Thus universal factorization forces Q* to be diagonal.

The exact S5 edge action is transitive on all ten coordinates. S5 invariance of a diagonal form therefore forces all ten diagonal entries equal:

`Q*=c I`.

Hence

`Q=c^-1 I`.

A common nonzero scalar does not change Q*-orthogonality, the polar subspace or the projection. For positive metrics the allowed family therefore collapses to the single **Euclidean ray**.

## Explicit rejection of the Iter083G S5-only witness
Iter083G's positive invariant metric

`Q2=I+(1/10)A_L(K5)`

has exact inverse entries

- diagonal `185/176`;
- adjacent-edge off diagonal `-15/176`;
- disjoint-edge off diagonal `5/176`.

Therefore the two-coordinate factorization test produces nonzero constants

- adjacent edges: `-3/37`;
- disjoint edges: `1/37`.

So Q2 is perfectly admissible in the broader S5-only scheme class, but it is excluded by universal product-factorization naturality.

This reconciles Iter083G/I with Iter083J rather than invalidating them.

## Relation to Iter083I
Iter083I showed that Q2 changes proper/nested K3/K4/K5 polar complements. Iter083J shows that this sensitivity disappears if one narrows to the universal tensor-product-factorizing projection family, because Q2 is not in that family.

Thus the regulator-metric ambiguity is **not intrinsic to the strongest natural Q-based projection class**.

## Physical applicability firewall
The mathematical factorization theorem is for independent tensor-product regulator blocks. The causal K5 vertex is a connected product of ten Toller functions sharing group variables. It is not a tensor product of ten independent group-space distributions.

Therefore Iter083J does **not** establish that the connected Lorentzian K5 source object physically requires the full universal factorization axiom.

That bridge remains open.

## Next target
A more source-local criterion should be tested next: proper forest/subgraph counterterms should not acquire holomorphic constants from regulator coordinates external to the subgraph. If this weaker forest-external decoupling already forces Q proportional to I, the Euclidean ray would follow from a locality condition directly tied to the authoritative K3/K4/K5 forest architecture rather than from arbitrary coordinate-block factorization.

## Interpretation ceiling
No physical source authorization of universal factorization; no unique physical K5 extension; no full K5 meromorphic continuation; no regulator independence; no generic-spin theorem; no G3/F9/G8/K5 promotion; no `NEW_PHYSICS_FOUND`; no complete-QG claim.