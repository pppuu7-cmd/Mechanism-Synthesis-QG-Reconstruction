# Iter083K-SM preregistration — authoritative forest-external regulator decoupling forces the Euclidean metric ray

Date: 2026-09-15
Status: PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION/PRODUCTION

## Scientific question
Iter083J proved that universal tensor-product factorization forces Q to the Euclidean ray, but its physical applicability to connected K5 is open. Is a much weaker condition tied directly to the authoritative K3/K4 subdivergence forest already sufficient?

Candidate locality axiom: for every proper divergent forest block B and every edge regulator coordinate x_e with e not internal to B, the simple polar direction L_B must be Q*-orthogonal to e_e^*. Equivalently a pure subgraph pole `1/L_B` multiplied by a holomorphic external regulator coordinate must not generate a holomorphic constant under the Q-based projection.

This gate proves the algebraic consequence of that axiom. It does not yet prove the Lorentzian causal-K5 source physically authorizes it.

## Authoritative forest input
Use exactly Iter082D/Iter083I:

- ten K3 blocks;
- five K4 blocks;
- one K5 overall block;
- twenty maximal chains;
- proper-block pole covectors `L_B=sum_(e internal B) x_e`.

Only proper K3/K4 blocks constrain external coordinates; K5 has no external edge coordinate inside the ten-edge regulator space.

## General invariant dual metric
Write the most general S5-invariant symmetric dual form as

`Q* = alpha I + beta A + gamma B`,

where A pairs distinct adjacent K5 edges and B pairs disjoint edges.

Nondegeneracy/positivity are not needed to solve the linear decoupling constraints, except that the surviving alpha must be nonzero/positive for an admissible metric.

## Prospective predicates
P0 AUTHORITY_LOCK: exact repository locks must confirm Iter082D forest counts and Iter083G three-dimensional invariant metric basis.

P1 COMPLETE_EXTERNAL_PAIR_ENUMERATION: enumerate every pair (proper block B, edge e not internal to B). Required totals:

- each K3 has 7 external edges -> 70 K3 pairs;
- each K4 has 4 external edges -> 20 K4 pairs;
- total 90 conditions.

P2 EQUATION_TYPES: for Q*=alpha I+beta A+gamma B, because e is not internal, alpha never enters. Exact coefficient types must be:

- K3 cross edge (one endpoint in B): `(n_adj,n_disjoint)=(2,1)`, equation `2 beta + gamma=0`;
- K3 complement edge (both endpoints outside B): `(0,3)`, equation `3 gamma=0`;
- K4 external/cross edge: `(3,3)`, equation `3 beta + 3 gamma=0`.

Required multiplicities over the whole forest: 60, 10, 20 respectively.

P3 CONSTRAINT_RANK: the exact 90x2 coefficient system in variables (beta,gamma) must have rank 2 and nullspace only `(0,0)`.

P4 MINIMAL_SUBSETS: independently show two reduced locality sets already force the result:

- K3 cross plus K3 complement: `(2,1)` and `(0,3)` rank 2;
- K3 cross plus K4 external: `(2,1)` and `(3,3)` rank 2.

Thus the conclusion is not driven by redundant enumeration.

P5 EUCLIDEAN_RAY: after beta=gamma=0, S5-invariant Q*=alpha I. Nondegenerate positive metrics have alpha>0, so Q=alpha^-1 I. Overall scale remains projection-irrelevant.

P6 ITER083I_RECONCILIATION: authoritative Q2 must violate the locality axiom with the already observed nonzero K3/K4 external pairings `-25/176` and `-15/88`, while remaining valid in the broader S5-only class.

P7 SOURCE_APPLICABILITY_FIREWALL: import external renormalization locality only as motivation: Dang–Zhang locality separates renormalized internal subgraphs from cross-edge factors on spatially separated vertex sets and yields exact factorization for disjoint unions. Do not claim this proves the regulator-coordinate orthogonality axiom for the connected Lorentzian Toller K5 vertex. A separate source/microlocal bridge remains required.

## Negative controls
- reject deriving beta=gamma=0 from S5 alone;
- reject using K5 overall pole as an external-decoupling constraint;
- reject omitting K3 complement-edge conditions from the complete enumeration;
- reject a preferred labelled K3/K4 block instead of all S5 images;
- reject treating Q2 as mathematically invalid outside the locality subclass;
- reject fixing alpha as a physical scale;
- reject promoting conditional forest locality to a unique physical K5 extension;
- retain non-Q renormalization schemes and source-authority gap.

## Expected classification if PASS
`ITER083K_SM_AUTHORITATIVE_FOREST_EXTERNAL_DECOUPLING_PLUS_S5_FORCES_Q_EUCLIDEAN_RAY_SCOPED`

Verdict: `PASS_EXACT_SCOPED`.

## Research consequence if PASS
The two metric-shape parameters activated geometrically by Iter083I are eliminated by a locality axiom tied directly to the actual K3/K4 forest rather than arbitrary regulator-coordinate tensor factorization. The remaining decisive issue becomes source applicability: prove or falsify that the Lorentzian causal-K5 extension must satisfy forest-external decoupling. If source-backed, the Euclidean Q-based projection becomes a serious selector candidate; if not, the broader S5-only Q freedom remains.

## Interpretation ceiling
No source authorization of the locality axiom; no actual unique physical extension; no full K5 meromorphic continuation; no regulator independence; no generic-spin theorem; no G3/F9/G8/K5 promotion; no NEW_PHYSICS_FOUND; no complete-QG claim.