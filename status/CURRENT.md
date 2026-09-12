# Current MSQGR research state

**Date:** 2026-09-12

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- Physical F9 (`CAUSAL_ANALYTICITY_RG_INVARIANT`): `BLOCKED`
- G3 quantum dynamics: `OPEN`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`
- K5 distributional/vertex extension: `BLOCKED`
- Active programme front: `ITERATION_052 / K4_RRR_CANONICAL_ANTISYMMETRY`

## Closed results controlling the current front

1. Source-backed Lorentzian EPRL/Toller carrier, exact `T+ + T- = D` control, native general Toller kernel, residue-series pure-boost kernel and direct ten-wedge topology have been independently validated.
2. Ordinary-function causal collision layers show strong Toller poles; magnetic sums, 16 causal-sector wiring and full j=1/2 boundary-intertwiner contraction do not remove the dangerous higher multi-collision powers. This is not a physical divergence theorem.
3. Appendix-D distributional primitives are reproduced; j=1/2 contains `delta` and `delta_prime`, with an epsilon-independent `delta_prime` contact coefficient.
4. Standard Christensen positive absolute spanning-tree proof does not close for the `beta^-2` Toller carrier. Naive complete-graph products also fail the standard transversality/Hormander criterion. A correlated/source-backed extension is required.
5. The regular pointwise j=1/2 boundary-contracted carrier is genuinely S5 covariant, but S5/source-support audits leave higher extension ambiguity.
6. Iter044: joint K3 pre-contact spectral integrand has a nonzero polynomial quotient; symmetric cutoff has an `R^3` obstruction. This is not a physical divergence theorem.
7. Iter045: exact quotient subtraction plus residue/PV finite part is coordinate-covariant on 40 held-out K3 points: `FP_q1=FP_q2=FP_q3` exactly. This is a viable structural K3 extension candidate only.
8. Iter046 terminal `K4_FINITE_PART_ORDER_OR_FOREST_DEPENDENT`: the same sequential 1D FP is not a covariant K4 extension; EPRL/no-contact control is invariant. K5 blocked.
9. Iter047 terminal `K4_PAIRWISE_FP_COMMUTATOR_OBSTRUCTION_LOCALIZED`: run `34708051922`; 24/24 source pairwise FP commutators nonzero, 24/24 controls exactly zero.
10. Iter048 terminal `K4_FP_OBSTRUCTION_MIXED_CHANNELS`: run `34708541480`; 24/24 valid; controls exactly zero; source channel counts `RR=8/24`, `RA=24/24`, `AR=24/24`, `AA=24/24`; 16 `INFINITY_ONLY`, 8 `MIXED`.
11. Iter049 terminal `K4_RR_SELECTOR_NONCOVARIANT`: repaired run `34709710387`, artifact `10302939028`; 48/48 valid and all controls exact zero. No universal graph/tree/pair-only RR selector exists on the frozen held-out cases.
12. Iter050 terminal `K4_RR_FACTOR_DEPENDENT_BEYOND_POLE_COUNT`: run `34710540567`, head `410ab8e2c1f2bb1f3f13f3129ee9eeaec730a0eb`, aggregate artifact `10303507511`. All 108/108 lanes valid; gamma, epsilon and external-flow changes caused no RR transitions; causal-sign changes caused 10. Coarse upper-pole-count asymmetry is not an exact selector.
13. Independent Iter050 denominator control terminal `DENOMINATOR_POLE_TOPOLOGY_SIGN_GEOMETRY_STABLE`: run `34710672477`, head `ddd002785482be959190f160482fbc235ce575b4`, aggregate artifact `10302654486`; 32/32 jobs valid and stable under frozen epsilon/k nuisance variants.
14. Iter051 terminal `K4_RR_EXACT_RESIDUE_GEOMETRY_SEPARATION` with structural flag `K4_RR_CANCELLATION_DOMINATED_SUBSET`: run `34712814029`, implementation head `e668862616cf898ad269d49a55b0c40a83efe720`, aggregate artifact `10304298594`, digest `sha256:68a2c96e7150950138f199219ea44fda17d7fca12f264961143586469316bcc1`. All 108/108 lanes valid. Exact classes: 37 `ORDERED_RESIDUE_DATA_IDENTICAL`, 31 `GEOMETRY_DIFFERS_BUT_SUM_CANCELS`, 40 `GEOMETRY_DIFFERS_AND_SUM_DIFFERS`, 0 inconsistencies. RR is nonzero in exactly those 40 sum-mismatch lanes. Thus exact ordered residue-sum mismatch localizes the sequential RR obstruction on the frozen grid more sharply than pole counts do.

Durable results:
- `status/ITERATION_048_RESULT.md`
- `status/ITERATION_049_RESULT.md`
- `status/ITERATION_050_RESULT.md`
- `status/ITERATION_050_DENOMINATOR_CONTROL_RESULT.md`
- `status/ITERATION_051_RESULT.md`

## Running independent held-out validation streams

### Iter051A — exhaustive factorized causal-sign census

- run: `34713025288`
- merged implementation: PR #51 / main commit `910db9ea333f88db55c47bcbca297ac98e7fa964`
- prereg commit before implementation: `fd0086e0fe75663834ebc0fe665cf3bde7521896`
- frozen matrix: 2 new nuisance points × 8 factorized causal-sign classes × 4 trees × 3 pairs = **192 lanes**
- target: whether each sign class has an identical 12-bit RR mask at H1 and H2.
- current status: not terminal; do not classify yet.

### Iter051B — held-out discrete residue/cancellation audit

- run: `34713037668`
- merged implementation: PR #52 / main commit `1483a71dc2eaf3cc72e915453c6891d3f1daa595`
- prereg commit before implementation: `596b431d5d4173f6d8674a774f4ffec03d0ab1f0`
- frozen matrix: 8 factorized causal-sign classes × 4 trees × 3 pairs = **96 lanes** at independent H3.
- tests eight prospectively frozen discrete residue/cancellation booleans; exact match requires equality with RR on all 96 lanes.
- current status: `in_progress`; do not classify yet.

## Active Iter052 — canonical triple-residue antisymmetry / inclusion-exclusion gate

Preregistered in `status/ITERATION_052.md` at commit `2ae9e81572363f4a9bc9e02637056a43a7d5a8e9`, before implementation/output.

For each of the nine frozen Iter050/051 conditions and four K4 tree bases, compute all six pure triple-residue orders `T_pi = R_pi3 R_pi2 R_pi1 F` and the canonical parity-weighted antisymmetrizer

`A_RRR = sum_{pi in S3} sgn(pi) T_pi`.

Frozen matrix: **36 source lanes**, each with identical F=1 control. Primary outcomes:
- `ITER052_CONTROL_OR_RECONSTRUCTION_INVALID`;
- `K4_RRR_CANONICAL_ANTISYMMETRY_IDENTITY_EXACT` if all 36 source antisymmetrizers and all controls are exactly zero with a nontrivial order-dependence guard;
- `K4_RRR_CANONICAL_ANTISYMMETRY_OBSTRUCTION_NONZERO` if any valid source lane has exact nonzero antisymmetrizer.

Implementation commits: `4cd7a059211475bfbd107b55782765cbb10a4d52`, workflow `34ee42573f8355c169aea56090a35e3d88c6c79e`; PR #53 merged as main commit `6a212175e5e2f091c841b51e05c029c9c1df4613`.

Authoritative active run: `34716166419`.

## Next allowed decisions

1. Consume Iter051A and Iter051B only when their aggregate artifacts are terminal; do not infer their classifiers from partial jobs.
2. Consume Iter052 against its frozen gate. If the canonical antisymmetrizer identity is exact, validate it on a new independent held-out grid before structural promotion.
3. If Iter052 is nonzero, do not fit coefficients: move toward a source/analyticity-selected simultaneous multivariate K4 extension audit.
4. A genuinely multivariate K4 prescription must still pass tree/cycle-basis/permutation/order independence and exact EPRL control before K5 can be authorized.

## Claim locks

- no `NEW_PHYSICS_FOUND`;
- no physical causal-vertex finiteness/divergence theorem;
- no universal no-go theorem for causal EPRL;
- no G3 PASS from a finite-part diagnostic;
- no F9/G8 promotion from symmetry/distributional surrogates;
- no arbitrary counterterm or preferred integration order;
- fixed causal-sector claims may not borrow `T+ + T- = D` cancellation without proof;
- distinguish ordinary absolute integrability, conditional/PV finite part and a source-defined distributional amplitude.
