# Iter082B-SM K5 source-covariant forest extension architecture — RESULT

Date: 2026-09-14

## Prospective chain

- prereg: `b263efeeeb052a8d5cf082334d350b5a4967d82b`
- implementation: `061c7fa9bb52b8e0157a2980959caa6ef0a40e3c`
- production: `9ea87d05fdf2e17f6dbe7ef7e46bbc10b202953c`
- run: `34890231748`, job `104130787436`, terminal `success`
- artifact: `10366686776`, `iter082b-sm-aggregate`
- artifact ZIP digest: `sha256:7c37478c2f352d8cd8ab9248a7ef7735d4ad69e16c5b59f36b052064eaf78be2`
- extracted aggregate JSON SHA256: `93a714e2df7762282e82d0f63a082a62a699f46c812d15ee5fff839c18509511`

## Classification

`ITER082B_SM_K5_FOREST_EXTENSION_ARCHITECTURE_COMBINATORIALLY_SOURCE_COVARIANT_EXACT_SCOPED`

Verdict: **PASS_EXACT_SCOPED**.

## Exact results

The implementation independently reconstructed the divergent-block arrangement instead of importing the Iter081X table:

- 16 divergent blocks total: 10 K3, 5 K4, 1 K5;
- 72 compatible forests;
- forest sizes `{0:1, 1:16, 2:35, 3:20}`;
- 20 maximal `K3 subset K4 subset K5` chains;
- all 120 S5 permutations checked exactly;
- forest set closed under S5;
- 8 exact S5 forest orbits, sizes `[1,1,5,5,10,10,20,20]`;
- all 20 maximal nested chains pass the quotient/partition consistency test.

There are no two disjoint divergent blocks among K3/K4/K5 on five vertices, so the disjoint-commutativity axiom is vacuous for this particular K5 divergent arrangement (`0` disjoint divergent pairs). It remains part of the architecture for larger complexes.

Negative controls all passed:

- a vertex-label-dependent coefficient tag breaks S5 covariance and is rejected;
- an overlapping nonnested K3/K4 pair is rejected as a forest;
- a termwise-contact source-order violation is rejected by the source firewall.

## Scientific meaning

A source-firewalled, S5-covariant, nested-consistent **combinatorial architecture** for a stratified K5 forest extension exists without choosing preferred vertex labels or a preferred nested order. Thus the Iter082A physical partial strata can be organized coherently at the forest/combinatorial level.

This removes a purely combinatorial obstruction but does **not** solve the physical extension problem. The aggregate explicitly has:

- `analytic_R_B_constructed = false`;
- `finite_parts_selected = false`.

The next high-value gate must construct actual analytic/distributional block-extension operators on K3/K4/K5 and test compatibility across the 20 nested chains, while leaving finite coefficients/scales prospectively controlled rather than fitted post hoc.

## Claim ceiling

No analytic forest-extension theorem for the Toller amplitude; no subtraction constants, scales, K3/K4 tangential coefficient selector, deepest 28/16 invariant-jet selector, regulator independence, causal E3/E4/E6, G3/F9/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete-QG claim.
