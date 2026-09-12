# Current MSQGR research state

**Date:** 2026-09-12

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- Physical F9 (`CAUSAL_ANALYTICITY_RG_INVARIANT`): `BLOCKED`
- G3 quantum dynamics: `OPEN`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`
- K5 distributional/vertex extension: `BLOCKED`
- Active programme front: parallel `ITERATION_052 / K4_RRR_CANONICAL_ANTISYMMETRY` + `ITERATION_051C / SIGN_CLASS_RANGE_VALIDATION`

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
12. Iter050 terminal `K4_RR_FACTOR_DEPENDENT_BEYOND_POLE_COUNT`: run `34710540567`, aggregate artifact `10303507511`. All 108/108 lanes valid; gamma, epsilon and external-flow OAT changes caused no RR transitions; causal-sign changes caused 10. Coarse upper-pole-count asymmetry is not an exact selector.
13. Independent Iter050 denominator control terminal `DENOMINATOR_POLE_TOPOLOGY_SIGN_GEOMETRY_STABLE`: run `34710672477`, artifact `10302654486`; 32/32 jobs valid and stable under frozen epsilon/k nuisance variants.
14. Iter051 terminal `K4_RR_EXACT_RESIDUE_GEOMETRY_SEPARATION` + `K4_RR_CANCELLATION_DOMINATED_SUBSET`: run `34712814029`, artifact `10304298594`, digest `sha256:68a2c96e7150950138f199219ea44fda17d7fca12f264961143586469316bcc1`. 108/108 valid; exact classes 37 identical, 31 geometry-different-but-sum-cancelling, 40 geometry-and-sum-different, 0 inconsistencies. RR is nonzero in exactly those 40 residue-sum-mismatch lanes.
15. Iter051A terminal `K4_RR_SIGN_CLASS_NUISANCE_STABLE`: run `34713025288`, artifact `10303884916`, digest `sha256:56270b122eee124d02388d246d687f4b85337c5ba5aa6307bb5d68b0f5265a0c`. All 192/192 lanes valid, all controls exactly zero, all factorized-sign checks pass, and total H1↔H2 Hamming distance across all eight 12-bit sign-class masks is exactly 0. This is scoped nuisance stability, not global sign universality.
16. Iter051B terminal `K4_RR_BEYOND_PREREG_RESIDUE_STRUCTURE`: run `34713037668`, artifact `10304474485`, digest `sha256:3c0483a01b283178193965a5dc54fe92ab19b85f7998041834336967cc27af43`. All 96/96 lanes valid; source RR is active in 48/96; none of eight prospectively frozen coarse discrete residue/cancellation booleans exactly matches RR (`exact_matching_diagnostics=[]`). No post-hoc selector fitting is authorized.

Durable results:
- `status/ITERATION_048_RESULT.md`
- `status/ITERATION_049_RESULT.md`
- `status/ITERATION_050_RESULT.md`
- `status/ITERATION_050_DENOMINATOR_CONTROL_RESULT.md`
- `status/ITERATION_051_RESULT.md`
- `status/ITERATION_051A_RESULT.md`
- `status/ITERATION_051B_RESULT.md`

## Active Iter052 — canonical triple-residue antisymmetry / inclusion-exclusion gate

Preregistered in `status/ITERATION_052.md` at commit `2ae9e81572363f4a9bc9e02637056a43a7d5a8e9`, before implementation/output.

For each of nine frozen Iter050/051 conditions and four K4 tree bases, compute all six pure triple-residue orders `T_pi = R_pi3 R_pi2 R_pi1 F` and the canonical parity-weighted antisymmetrizer

`A_RRR = sum_{pi in S3} sgn(pi) T_pi`.

Frozen matrix: **36 source lanes**, each with identical F=1 control. Primary outcomes:
- `ITER052_CONTROL_OR_RECONSTRUCTION_INVALID`;
- `K4_RRR_CANONICAL_ANTISYMMETRY_IDENTITY_EXACT` if all 36 source antisymmetrizers and controls are exactly zero with nontrivial order dependence;
- `K4_RRR_CANONICAL_ANTISYMMETRY_OBSTRUCTION_NONZERO` if any valid source lane has exact nonzero antisymmetrizer.

Implementation commits `4cd7a059211475bfbd107b55782765cbb10a4d52`, workflow `34ee42573f8355c169aea56090a35e3d88c6c79e`, PR #53 merged as `6a212175e5e2f091c841b51e05c029c9c1df4613`.

Authoritative active run: `34716166419`. Job-level production is ongoing; consume only the terminal aggregate before scientific classification.

## Active Iter051C — wider held-out sign-class range validation

Preregistered in `status/ITERATION_051C.md` at commit `1d3cd2b28d4f33cb18b89408962628254a2ed920` **before** implementation `e40189337d29efdda04c530f43242c21b8f54d3a` and workflow `9a68ab092b68cb2897d54006eab770fc7ebcf572`.

Frozen held-out points:
- H4: `gamma=31/100`, `epsilon=31/1000`, `k=(41,-37,12,-16)/100`;
- H5: `gamma=245/100`, `epsilon=163/1000`, `k=(-22,47,-31,6)/100`.

The eight complete Iter051A H1/H2 reference masks are frozen in the preregistration and implementation before production. Matrix: **192 exact lanes** = 2 points × 8 sign classes × 4 trees × 3 pairs, each with identical F=1 control.

Primary outcomes:
- `ITER051C_CONTROL_OR_RECONSTRUCTION_INVALID`;
- `K4_RR_SIGN_CLASS_RANGE_STABLE` iff every H4/H5 mask exactly equals its frozen Iter051A reference mask;
- `K4_RR_SIGN_CLASS_RANGE_DEPENDENT` otherwise.

PR #54 merged as main commit `676760962d5177b7a045f4ebfac30c0ad4ca0da8`.

Authoritative active run: `34717183041`.

## Next allowed decisions

1. Consume Iter052 only at terminal aggregate. If canonical S3 antisymmetry is exact, preregister a genuinely independent held-out validation before structural promotion. If nonzero, do not fit coefficients; move toward a source/analyticity-selected simultaneous multivariate K4 extension audit.
2. Consume Iter051C only at terminal aggregate. A PASS is only wider scoped sign-mask stability, not a global theorem. A FAIL must be retained as range dependence rather than retuned.
3. Iter051B already rules out the eight preregistered coarse discrete residue/cancellation selectors on H3; do not invent a post-hoc replacement selector.
4. A genuinely multivariate K4 prescription must still pass tree/cycle-basis/permutation/order independence plus exact EPRL control before K5 is authorized.

## Claim locks

- no `NEW_PHYSICS_FOUND`;
- no physical causal-vertex finiteness/divergence theorem;
- no universal no-go theorem for causal EPRL;
- no global causal-sign universality theorem from finite held-out scans;
- no G3 PASS from a finite-part diagnostic;
- no F9/G8 promotion from symmetry/distributional surrogates;
- no arbitrary counterterm or preferred integration order;
- fixed causal-sector claims may not borrow `T+ + T- = D` cancellation without proof;
- distinguish ordinary absolute integrability, conditional/PV finite part and a source-defined distributional amplitude.
