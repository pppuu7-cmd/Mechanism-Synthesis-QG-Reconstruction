# Control-only repair 1 — independent Critic for actual K4 order-3 parity

Date: 2026-09-15
Status: PROSPECTIVELY FROZEN BEFORE REPAIR IMPLEMENTATION

Parent scientific contract: `prereg/ACTUAL_MULTIVARIATE_K4_ORDER3_PARITY_INDEPENDENT_CRITIC_REVIEW.md`, commit `76595a6bdc27553fb5ccec9f06942203d97dc520`.
Initial Critic implementation: `3d637eb144ce2e979b419b807bfb6c02af18a6e9`.
Initial workflow/head: `de3f01118c482f9a37f37eab113f2cd2d5975f3f`.
Historical run: `35004252640`, terminal success at the workflow level but classified here as `INVALID_IMPLEMENTATION` for scientific authority.

## Defect discovered before repair

The initial Critic does not independently establish several frozen acceptance criteria. It populates a `base` dictionary with the target values themselves (`normal_dim=9`, `front_dim=8`, `gram_det=64`, `internal_wedges=6`, `external_wedges=4`, `baseline_degree=6`, `all32=True`, `all5=True`, `s5_transport=True`, `analytic_common_chart=True`, etc.) and then validates those literals against the same expected literals.

Only the weak-composition count is independently recomputed. The implementation also states that provenance/digest is a separate requirement but does not verify the frozen run/artifact/digest chain before allowing `K4_ACTUAL_ORDER3_PARITY_CRITIC_CONFIRMED_SCOPED`.

The workflow performs no extra independent recomputation beyond this script.

Therefore the green historical run is implementation evidence only and has no terminal scientific Critic authority.

## Frozen repair obligations

The repaired Critic must keep the original scientific criteria and terminal taxonomy unchanged and must derive/check, rather than literal-initialize, at least:

1. authoritative Researcher prereg/run/artifact/JSON digest provenance and quarantine of historical invalid runs;
2. K4 block census and exact normal dimension/front dimension from K5/K4 combinatorics;
3. barycentric Gram matrix/determinant from exact rational matrices;
4. inversion invariance of the Gram form and evenness/antipodal status of the resolved front measure from the actual local geometry authority;
5. six internal/four external K4 edge census for each of all five K4 blocks;
6. baseline degree six from six independently verified degree-one pole-removed internal leading factors, not from a stored total;
7. the 12 frozen analytic jet slots and all 364 weak degree-3 partitions by exact enumeration;
8. all-32 boundary coverage and all-five-K4 coverage from actual production/repository records;
9. S5 transport/covariance from an explicit permutation computation or an authoritative exact table that is itself checked;
10. source-faithful common-chart/cubic-realization authority and published spectral `i epsilon` retention by anchored source/result inspection;
11. scheme/interpretation firewall: simple residue only, no finite-part/physical-amplitude/K5 inference.

## Repair controls

The repaired validator must run the same decision path on malformed mutations and reject all controls frozen in the parent preregistration. It must additionally reject a synthetic input in which all target booleans are supplied as literals but the underlying recomputed evidence is absent or inconsistent.

A positive fixture must still be able to pass, but it may not bypass recomputation/provenance by setting expected values directly.

## Scientific-contract lock

No scientific acceptance criterion, K4 parity target, source convention, residue convention, control meaning, or terminal classification is changed by this repair. This repair closes only circular/self-confirming implementation and missing provenance verification.

K5 order eight remains dependency-locked until repaired Critic production is terminal and valid.