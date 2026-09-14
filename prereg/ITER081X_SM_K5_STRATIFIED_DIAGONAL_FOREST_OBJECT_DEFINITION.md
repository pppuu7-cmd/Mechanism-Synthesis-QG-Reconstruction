# Iter081X-SM prereg — exact K5 stratified diagonal/forest extension object definition

Status: **PROSPECTIVE CRITIC OBJECT-DEFINITION GATE — frozen before implementation/result**
Date: 2026-09-14

## Motivation
The corrected deepest common-collision problem leaves a finite but nontrivial invariant normal-jet ambiguity (Iter081R). Rühl-motivated analytic regularization cannot yet be promoted globally because the authoritative Iter077I leading factor on each wedge is proportional to

`M(X_a-X_b)/|X_a-X_b|^3`,

which is singular on partial diagonals `X_a=X_b`. Historical Iteration 022 numerically observed the expected multi-cluster powers but was not an exact source-ordered forest theorem.

Before any correlated analytic/subtraction selector, define the exact local K5 collision stratification and power-counting forest.

## Frozen linearized normal configuration space
Near the compact collision manifold, after quotienting the common boost by global left `SL(2,C)` gauge, use

`V5 := { (X_1,...,X_5) in (R^3)^5 } / R^3_diag`,

`dim V5=12`.

For every nonempty subset `B subset {1,...,5}` with `|B|>=2`, define the partial diagonal

`Delta_B := { X_a=X_b for all a,b in B }`.

Its codimension in `V5` is

`codim Delta_B = 3(|B|-1)`.

For a set partition `pi={B_1,...,B_r}` define

`Delta_pi := intersection_i Delta_(B_i)`

with singleton blocks imposing no equation. Then

`codim Delta_pi = 3(5-r)=3 sum_i(|B_i|-1)`.

## Frozen j=1/2 leading carrier
For each internal edge `(ab)` contained in the same collision block, the authoritative source-leading Toller factor has transverse degree `-2`. Thus for partition `pi` the simultaneous common-radial degree contributed by edges internal to blocks is

`q_pi = -2 sum_i C(|B_i|,2)`.

The common-radial absolute-integrability margin is

`m_pi = q_pi + codim(Delta_pi)`
`= sum_i (|B_i|-1)(3-|B_i|)`.

Define superficial divergence degree

`omega_pi := -m_pi = sum_i (|B_i|-1)(|B_i|-3)`.

For a single connected collision block of size `k`,

`omega_k=(k-1)(k-3)`.

## Exact combinatorial questions
1. Enumerate all 52 set partitions of 5 and classify by integer block-size type.
2. Verify counts by type:
   - `1+1+1+1+1`: 1;
   - `2+1+1+1`: 10;
   - `2+2+1`: 15;
   - `3+1+1`: 10;
   - `3+2`: 10;
   - `4+1`: 5;
   - `5`: 1.
3. Compute `codim`, `q`, `m`, `omega` for every type.
4. Distinguish **connected divergent subgraphs/blocks** from merely simultaneous partition strata. A connected block requires local extension by power counting iff `|B|>=3`:
   - 10 triples `K3`, `omega=0`;
   - 5 quadruples `K4`, `omega=3`;
   - 1 quintuple `K5`, `omega=8`.
5. Enumerate inclusion/nesting relations among these 16 connected divergent blocks.
6. Define a Zimmermann/wonderful-model style forest combinatorially as a collection of divergent blocks that are pairwise nested or disjoint. Overlapping blocks with nonempty intersection but neither containing the other cannot appear simultaneously in one forest.
7. Count forests by size and S5 orbit type if feasible exactly; at minimum verify the forest condition mechanically and record all maximal forests.

## Source/physics scope
This gate defines the **renormalization object**, not counterterm values. It uses only exact source-leading edge powers and K5 incidence. It does not assume that every carrier divergence survives every full boundary contraction.

Physical promotion rules:
- k=5 non-L1 survival after full 32-component boundary contraction is already exact (Iter077I).
- k=3/k=4 historical evidence is numerical only; until a source-ordered full-boundary exact/nonzero theorem is supplied, their power count is a forest requirement/diagnostic, not a physical divergence theorem.
- a global extension scheme may nevertheless need partial-stratum prescriptions because the product singular support is stratified even before full physical promotion.

## Required controls
- Bell number `B_5=52` partition enumeration.
- total pair diagonals `C(5,2)=10`.
- exact connected divergent block count `10+5+1=16`.
- single-block margins: k=2 `+1`, k=3 `0`, k=4 `-3`, k=5 `-8`.
- deepest k=5 excess `8` must match Iter077L maximum normal derivative order 8.
- k=3 logarithmic prediction and k=4/k=5 power predictions must agree in sign with historical Iteration 022 numerical cluster classifications, without using those numerics to define the exact result.

## Frozen classifications
- `ITER081X_SM_K5_STRATIFIED_DIAGONAL_FOREST_OBJECT_DEFINED_EXACT_SCOPED` if partition/divergent-block/nesting/forest combinatorics and source-leading power counts are internally consistent.
- `INVALID_OBJECT_DEFINITION` if codimensions, incidence, power counting or forest structure fail controls.

## Claim ceiling
This gate does not prove k=3/k=4 full-boundary divergence, choose a subtraction scheme, assign counterterms, prove forest-formula equivalence to a source amplitude, or establish regulator independence. It is the exact local object definition required before any Rühl/Epstein-Glaser/BPHZ-style K5 extension can be tested. No G3/F9/G8/K5, `NEW_PHYSICS_FOUND`, or complete-QG claim follows.
