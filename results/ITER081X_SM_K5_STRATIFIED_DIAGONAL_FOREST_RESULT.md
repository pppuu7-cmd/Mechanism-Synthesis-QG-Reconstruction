# Iter081X-SM — exact K5 stratified diagonal/forest extension object

**Date:** 2026-09-14  
**Status:** `PASS_EXACT_SCOPED`

## Prospective chain
- preregistration: `3c306fdc4581bc5d1fdd2cb6c3500a4e49a2e676`;
- implementation: `a9e3d818bab5de441c1e6bd17507d58708e2fc49`;
- production head: `d93b99bacf455e8873775cc0f4a54f338d5e7843`;
- Actions run: `34885725498`, terminal success;
- job: `104115781734`, terminal success;
- artifact: `10364074314`, `iter081x-sm-k5-stratified-forest`;
- artifact ZIP digest: `sha256:cccfcd65d86ffddaef5a53a162327e92410629e2a8a1859819c12080a332af8d`;
- downloaded aggregate JSON SHA256: `a3a8a9bf9e1b403e57e6b9f0f6a6219ade3d33174772cffb172deda61062b1ad`;
- durable raw aggregate: `results/raw/iter081x_sm_k5_stratified_forest.json`, commit `327d34ffb25b028f8259ad05c840150b17f38cc5`.

## Classification
`ITER081X_SM_K5_STRATIFIED_DIAGONAL_FOREST_OBJECT_DEFINED_EXACT_SCOPED`

Verdict: **`PASS_EXACT_SCOPED`**.

## Exact partition geometry
The linearized common-collision normal configuration space is

`V5=(R^3)^5/R^3_diag`, `dim V5=12`.

For a collision block `B`, `Delta_B` imposes equality of all `X_a` in `B` and has codimension `3(|B|-1)`.

The exact enumeration contains Bell number `B_5=52` set partitions, with block-size counts

- `1+1+1+1+1`: 1;
- `2+1+1+1`: 10;
- `2+2+1`: 15;
- `3+1+1`: 10;
- `3+2`: 10;
- `4+1`: 5;
- `5`: 1.

For all-`j=1/2` source-leading edge degree `-2`, a partition `pi` has

`q_pi=-2 sum_B C(|B|,2)`,
`m_pi=q_pi+codim(Delta_pi)`,
`omega_pi=-m_pi`.

Exact type table:

| type | codim | internal edges | q | L1 margin | omega |
|---|---:|---:|---:|---:|---:|
| `5` | 12 | 10 | -20 | -8 | 8 |
| `4+1` | 9 | 6 | -12 | -3 | 3 |
| `3+1+1` | 6 | 3 | -6 | 0 | 0 |
| `3+2` | 9 | 4 | -8 | +1 | -1 |
| `2+2+1` | 6 | 2 | -4 | +2 | -2 |
| `2+1+1+1` | 3 | 1 | -2 | +1 | -1 |
| singletons | 0 | 0 | 0 | 0 | 0 |

Thus the connected superficially divergent collision blocks are exactly:

- 10 triples `K3`, logarithmic (`omega=0`);
- 5 quadruples `K4`, excess 3;
- 1 quintuple `K5`, excess 8.

Total: **16** connected divergent blocks.

The deepest excess `8` exactly matches the Iter077L maximum normal derivative order.

## Exact forest combinatorics
A forest is a collection of divergent blocks that are pairwise nested or disjoint. For the five-vertex K5 case, two distinct blocks of sizes >=3 cannot be nonempty disjoint, so admissible forests reduce to nested chains.

Exact enumeration:

- total forests: **72**;
- size 0: 1;
- size 1: 16;
- size 2: 35;
- size 3: 20.

Maximum forest size is 3. All 20 maximal forests are exactly chains

`K3 subset K4 subset K5`.

Under `S5` relabeling there are **8 forest orbit types**, corresponding exactly to the eight rows recorded in the aggregate.

## Scientific meaning
The local K5 extension problem is intrinsically stratified. A global distributional extension cannot in general be defined solely by choosing coefficients at the deepest `K5` collision while ignoring partial diagonals: the source-leading product has logarithmic/power singular substructures associated with `K3` and `K4` blocks.

Iter081X is an exact **object-definition/power-counting** theorem. It does not by itself prove that the fully boundary-contracted physical source amplitude is nonzero on every K3 or K4 stratum. Exact boundary-complete non-L1 survival was previously authoritative only at K5; Iter082A is prospectively frozen to independently test explicit K3/K4 nested source-boundary witnesses.

## Renormalization consequence
Any Rühl/Epstein-Glaser/BPHZ/wonderful-model style extension proposed for the K5 object must specify how subtractions/extensions are assigned to the 16 connected blocks and combined over the 72 allowed forests, while preserving source ordering, node-wise compact gauge covariance, S5 relabeling and true boundary covariance.

A single radial analytic continuation about the deepest K5 stratum is therefore not a complete global extension object unless its treatment of partial diagonals is separately defined and proved equivalent to a stratified prescription.

## Claim ceiling
No K3/K4 full-boundary divergence theorem is claimed solely from this result; no subtraction values, counterterms, renormalization scale, forest formula, extension uniqueness, regulator independence or causal-vertex existence/nonexistence is established. No G3/F9/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete-QG claim follows.
