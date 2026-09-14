# Iter082B-SM prereg — K5 source-covariant stratified forest extension prescription gate

Status: **PROSPECTIVE GATE — frozen before Iter082B implementation/production**
Date: 2026-09-14

## Motivation
Iter081X defines the exact divergent K5 diagonal arrangement and its 72 forests. Authoritative Iter082A now proves that K3 and K4 partial strata are physically active in the frozen source-ordered fully boundary-contracted minimal-spin sector. Therefore a deepest-K5-only extension is insufficient.

This gate does **not** choose subtraction constants or claim a published spin-foam forest theorem. It tests whether a mathematically explicit candidate forest extension architecture can be defined without hidden preferred labels/orders and while respecting the source-order and symmetry locks already established.

## Frozen input object
Use exactly:

- K3 divergent blocks: all 10 three-node subsets, `q=-6`, codim 6, `omega=0`;
- K4 divergent blocks: all 5 four-node subsets, `q=-12`, codim 9, `omega=3`;
- K5 block: the full five-node subset, `q=-20`, codim 12, `omega=8`;
- forest compatibility: blocks are compatible iff nested or disjoint;
- exact Iter081X forest census: 72 forests with sizes `{0:1,1:16,2:35,3:20}` and 20 maximal `K3 subset K4 subset K5` chains.

The implementation must reconstruct these objects independently from subsets; stored Iter081X output may be used only as a control checksum, not as generated input.

## Candidate prescription architecture to test
For each divergent block `B`, introduce an abstract local extension/subtraction operator `R_B` acting only in the normal variables of the collision block and leaving the contracted co-graph/source external variables as coefficients.

The gate is restricted to structural consistency. It must **not** assign finite coefficient values.

Freeze the following axioms for the candidate architecture:

1. **Block locality:** `R_B` is indexed only by the unlabeled induced complete subgraph on `B`, its source ordering, and its invariant normal degree `omega_B`; no vertex-number-dependent constants are permitted.
2. **S5 covariance:** for every permutation `pi`, `pi R_B pi^-1 = R_{pi(B)}`.
3. **Disjoint commutativity:** if `B` and `C` are disjoint, `R_B R_C = R_C R_B`.
4. **Nested forest admissibility:** if `B subset C`, both orders must be represented by the same contracted forest datum after quotient/co-graph identification. The implementation must explicitly test the combinatorial quotient maps rather than assume this.
5. **Source-order firewall:** the object extended is the already-contracted product of Toller functions in the authoritative order `one-wedge spectral/spinor integration -> Toller function -> ten-wedge product -> full boundary contraction -> K5 extension`; no termwise spinor-contact multiplication is permitted.
6. **No finite-part choice:** scales, subtraction constants, invariant-jet coefficients, and renormalization conditions remain symbolic/unselected.

## Exact implementation tasks

A. Reconstruct the 16 divergent blocks and all 72 forests from subset compatibility.

B. Enumerate the full S5 action on blocks and forests. Verify closure, orbit counts, and that the candidate operator labels transform covariantly without preferred node labels.

C. For every maximal chain `K3 subset K4 subset K5`, construct exact set-theoretic quotient/co-graph maps for the two nested contractions:

`K5 -> K5/K3 -> (K5/K3)/(K4/K3)`

and

`K5 -> K5/K4 -> (K5/K4)` with the embedded K3 contraction recorded inside K4.

Test whether both descriptions produce the same final partition/incidence data. This is only a combinatorial nesting-consistency test, not an equality theorem for analytic subtraction operators.

D. Verify all disjoint compatible pairs commute at the quotient-partition level.

E. Negative controls:
- inject a vertex-label-dependent coefficient tag and require S5 covariance to fail;
- treat an overlapping nonnested K3/K4 pair as a forest and require rejection;
- reverse the authoritative source firewall by tagging termwise contacts and require rejection.

## Frozen classifications

- `ITER082B_SM_K5_FOREST_EXTENSION_ARCHITECTURE_COMBINATORIALLY_SOURCE_COVARIANT_EXACT_SCOPED` iff A-E pass exactly.
- `ITER082B_SM_K5_FOREST_EXTENSION_ARCHITECTURE_COMBINATORIAL_COVARIANCE_FAILS_EXACT_SCOPED` if a valid exact S5/forest/quotient test fails.
- `INVALID_IMPLEMENTATION_OR_PROVENANCE` for chronology, reconstruction, or negative-control failure.

## Interpretation ceiling
A PASS would establish only that a source-firewalled, S5-covariant, nested/disjoint-consistent **architecture** for a forest extension can be formulated on the exact K5 stratification without preferred labels or orders at the combinatorial level. It would not define analytic `R_B`, finite parts, scales, K3/K4 coefficient functions, deepest 28/16 jet coefficients, regulator independence, E3/E4/E6, G3/F9/G8/K5, `NEW_PHYSICS_FOUND`, or complete QG. A later gate would still have to construct and test actual analytic extension operators and a physical selector.
