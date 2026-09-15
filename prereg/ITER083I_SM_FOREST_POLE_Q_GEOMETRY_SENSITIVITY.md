# Iter083I-SM preregistration — proper/nested K3-K4-K5 pole geometry sees S5-invariant Q shape

Date: 2026-09-15
Status: PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION/PRODUCTION

## Scientific question
Iter083H proves Q-independence for the isolated deepest K5 simple overall pole `L_K5=sum_all_edges x_e`. Does that special independence persist for the actual authoritative K3/K4/K5 forest pole arrangement, or do proper-subgraph and nested pole complements depend on the two S5-invariant regulator-metric shape parameters left open by Iter083G?

This gate tests **polar geometry only**. It does not infer that the physical renormalized K5 amplitude changes with Q unless nonzero residues/numerators are separately established.

## Frozen authoritative forest input
From Iter082D:

- divergent collision blocks are all K3/K4/K5 vertex subsets: 10 K3 blocks, 5 K4 blocks, 1 K5 block, total 16;
- maximal nested chains are all `B3 subset B4 subset B5`, total 20;
- normal codimensions are `6,9,12`;
- subtraction/Taylor ceilings are `omega=(0,3,8)`.

For a block B with internal edge set E(B), attach edge regulators `s_e=1+x_e` and define

`L_B(x)=sum_(e in E(B)) x_e`.

The block radial model at its critical Taylor order must produce a simple pole proportional to `1/L_B`.

## Frozen metric pair
Use the two exact positive S5-invariant metrics already certified by Iter083G:

`Q1 = I`,

`Q2 = I + (1/10) A_L(K5)`.

Their Q2 eigenvalues on `[5],[4,1],[3,2]` are `(8/5,11/10,4/5)`, so Q2 is positive and not proportional to Q1.

Polar covectors are paired with the induced dual metric `Q*`, represented in edge coordinates by `Q^{-1}`.

## Prospective predicates

P0 FOREST_AUTHORITY_LOCK: exact Iter082D source/result lock must confirm 16 divergent blocks, 20 maximal chains, nested normal ranks and `omega=(0,3,8)`.

P1 POLE_FORM_DERIVATION: for block size p=3,4,5 with `m=C(p,2)` internal wedges and normal dimension `d=3(p-1)`, verify `omega=2m-d=(0,3,8)` and that the critical radial factor is `-1/(2L_B)`.

P2 COMPLETE_BLOCK_ENUMERATION: enumerate exactly all 10 K3, 5 K4 and 1 K5 pole covectors in the ten-edge regulator space and all 20 maximal chains; verify S5 closure.

P3 PRIMITIVE_K5_CONTROL: reproduce Iter083H special case: `L_K5` is an eigen-covector of both Q1* and Q2*, so its one-pole orthogonal complement is unchanged.

P4 PROPER_STRATUM_SENSITIVITY: for canonical `B4={0,1,2,3}`, use exact witness `z=e_04`. Required:

`<L_B4,z>_(Q1*) = 0`,

`<L_B4,z>_(Q2*) = -15/88 != 0`.

Also verify a K3 proper-stratum witness, e.g. for `B3={0,1,2}`, `z=e_03` gives Q1*=0 and Q2*=`-25/176`.

P5 MAXIMAL_CHAIN_SENSITIVITY: for canonical chain

`{0,1,2} subset {0,1,2,3} subset {0,1,2,3,4}`

use

`z=-e_04+e_34`.

Required exact pairings:

under Q1*: `(0,0,0)` against `(L3,L4,L5)`;

under Q2*: `(5/22,0,0)`.

Thus the common polar orthogonal complement changes with Q.

P6 GRAM_CROSSCHECK: compute exact canonical-chain Gram matrices under Q1* and Q2*. Required

`G1=[[3,3,3],[3,6,6],[3,6,10]]`, det `36`;

`G2=[[465/176,195/88,15/8],[195/88,195/44,15/4],[15/8,15/4,25/4]]`, det `10125/484`.

Both spans are nondegenerate; the sensitivity is not caused by pole-vector linear dependence.

P7 S5_GLOBALIZATION_AND_SCOPE: verify all 20 maximal chains lie in one S5 orbit and transport the canonical witness accordingly. The conclusion must remain geometric: Q-based polar complements differ for proper/nested forest poles. Do NOT infer a nonzero renormalized-amplitude difference without nonzero physical residues/numerator coupling.

## Negative controls
- reject a nonpositive or non-S5 metric as the sensitivity witness;
- reject claiming Q sensitivity for primitive K5 alone (Iter083H forbids it);
- reject using an arbitrary non-authoritative subgraph family instead of the 10/5/1 forest blocks;
- reject treating changed Gram numbers alone as sufficient if the orthogonal complement is unchanged;
- reject treating changed polar complement as proof of nonzero physical counterterm difference;
- reject scalarizing the 32-dimensional boundary fiber;
- retain the possibility that stronger locality/factorization uniquely forces Q proportional to I;
- retain the possibility that actual residues vanish in Q-sensitive channels.

## Expected classification if PASS

`ITER083I_SM_AUTHORITATIVE_K3_K4_K5_FOREST_POLE_COMPLEMENTS_SEE_S5_INVARIANT_Q_SHAPE_SCOPED`

Verdict: `PASS_EXACT_SCOPED`.

## Research consequence if PASS
A generic S5-invariant Q-based projection is geometrically scheme-sensitive exactly on proper/nested forest poles even though the primitive overall K5 simple pole is Q-independent. The next nonredundant question becomes positive: whether locality/factorization/forest functoriality forces Q to the Euclidean ray `Q proportional I`, or whether source-faithful residues actually excite the Q-sensitive directions.

## Interpretation ceiling
No actual nonzero physical scheme dependence is claimed; no full K5 meromorphic continuation; no unique selector; no generic-spin theorem; no regulator independence; no all-strata global renormalization theorem; no G3/F9/G8/K5 promotion; no `NEW_PHYSICS_FOUND`; no complete-QG claim.