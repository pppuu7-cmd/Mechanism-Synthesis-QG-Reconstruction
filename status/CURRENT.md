# Current MSQGR research state

**Date:** 2026-09-13

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- Physical F9 (`CAUSAL_ANALYTICITY_RG_INVARIANT`): `BLOCKED`
- G3 quantum dynamics: `OPEN`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`
- K5 distributional/vertex extension: `BLOCKED_CORRELATED_EXTENSION_OBJECT_MISSING`
- Active front: `SOURCE_ANALYTICITY_SELECTOR / MICROLOCAL_COLLISION_HYPOTHESES`

## Newly controlling source/direct chain

- Iter063B authoritative retry run `34731891190`, job `103656077408`, artifact `10310265245`, digest `sha256:dc0a3f250949b780ebe758af82f1b4ef3f27eeb1370fe7bc46b5fb1c42b064ba`: `ITER063B_SOURCE_CONTROL_BLOCKED_MISSING_EXPLICIT_RELATION`. The earlier green run `34729216381` was implementation-invalid self-reference and is non-authoritative.
- Primary source snapshot commit `7df82d28dd6426aa7aaac353a1e0abf795e6fdee`: Bianchi-Chen-Gamonal arXiv `2601.23162`, DOI `10.1103/fwql-t4yr`; pins Eq.(3) spectral Feynman `i epsilon`, Eq.(4) direct ten-wedge fixed-causal vertex, Eq.(5) `T+ + T-=D`, Eq.(6) unconstrained independent-wedge EPRL sum, Eq.(7) Cartan/magnetic representation.
- Iter063C authoritative run `34732046499`, job `103656528583`, artifact `10309351521`, digest `sha256:a8fad3edd3e820b849fa0be8fcf0939571fdc65b4919b2369d46efb2f2aa4eac`: 4/4 `ITER063C_PRIMARY_SOURCE_VERTEX_CONTROL_PINNED`.
- Iter064A authoritative run `34732198011`, aggregate job `103656960238`, artifact `10309427622`, digest `sha256:2cb05aa6b626f23256a0ba1fcd3502404ecc3387a8521baece660ab238a9f161`: 6/6 `ITER064A_DIRECT_CAUSAL_POINTWISE_EPRL_CONTROL_PASS`. Initial run `34732114933` was runtime-invalid before science and is non-authoritative. Worst controls: KAK `1.9462e-15`, edge additive `5.2303e-64`, independent-wedge EPRL sum `5.6631e-64`, global sigma-flip duplication `1.1054e-80`; min pair boost `0.44134`.
- Historical Iter038 run `34694739107` was re-consumed rather than repeated: 6/6 raw carrier-S5 lanes PASS. Worst causal even/odd errors `3.39e-14 / 2.38e-14`, EPRL `6.95e-12`, KAK `2.34e-15`, all within its frozen gates.
- Iter064B authoritative run `34732360103`, aggregate job `103657391209`, artifact `10310016825`, digest `sha256:8012eb7aedfcb1765509a7e86e94ff3816da3f349ca2524e208236c29d665a8a`: 4/4 `ITER064B_K4_SOURCE_PREREQUISITES_CLOSED_FOR_K5_QUALIFICATION`. This closed the prerequisite blocker only; it did not pass K5.
- Iter065A prereg `987b0b27aaccc9e75ceed5fe209e9944a17f5e94`, authoritative head `fd93c7e968df49f0b1df9468117cf6795afed701`, run `34732545131`, aggregate job `103657905982`, artifact `10310465490`, digest `sha256:3d171139e80274074924065acdc12fdba265de78238f1cf2a859b62820dad5ba`: 0/4, `ITER065A_K5_BLOCKED_CORRELATED_EXTENSION_OBJECT_MISSING`.
- Iter066A prereg `b6846ee0515853cd9981dc0d6688c021174922be`, authoritative head `9cfc3cc3f94e9246f103d6f50628621726cd9967`, run `34734333416`, aggregate job `103662960682`, artifact `10309673723`, digest `sha256:05fd9933952a634158d4cee4a5f680ba0e48182b748a0d15053f7aab4f85082b`: `ITER066A_GENERIC_MULTIVARIATE_FRAMEWORK_AVAILABLE_SOURCE_SELECTOR_STILL_MISSING`. `BBK2009_WONDERFUL_EG` supplies a genuine multivariate framework, but no audited source supplies a unique physical Toller/EPRL selector. Durable result: `status/ITERATION_066A_RESULT.md`.
- Iter067A prereg `dd3c05d334271d986c427d26a632db01d804efea`, authoritative head `73d08d884293d1f789cc3347ce7181fa09aacd46`, run `34736725079`, aggregate job `103669423844`, artifact `10310499751`, digest `sha256:7287dfb43f83722cf9112bdd784da8d06c453260fbecf34735e74ddc837bd9f1`: `ITER067A_THEOREM_ROUTE_EXISTS_PHYSICAL_HYPOTHESES_UNPROVEN`. Hormander analytic-boundary-value and wavefront-product theorems provide conditional canonical routes, but the physical joint-family hypotheses and distributional Eq.(5)/(6) bridge remain unproved. Durable result: `status/ITERATION_067A_RESULT.md`.

## Exact K5 blocker after Iter067A

The project has both generic multivariate extension machinery and conditional theorem-level uniqueness routes. What remains missing is verification that the **physical Toller finite-spectral-`i epsilon` family** satisfies the hypotheses of one of those canonical routes and that Eq.(5)/(6) survives the resulting correlated boundary value.

The unresolved requirements are:

1. a source-defined or source-derived joint multivariate analytic/distributional family corresponding to the physical causal vertex;
2. verified holomorphy/tube/growth or wavefront-cone hypotheses sufficient for a canonical boundary value/product at the correlated K5 collision arrangement;
3. uniqueness without arbitrary local counterterms or preferred tree/cycle/integration order;
4. inheritance of Eq.(5)/(6) independent-wedge EPRL control at the distributional K5 level.

This is `BLOCKED`, not a theorem of vertex divergence/nonexistence.

## Historical distributional localization retained

- Iter039: `S5_SYMMETRY_ONLY_EXTENSION_UNIQUE_THROUGH_16 = FALSE`; first non-unique invariant degree 4.
- Iter040: `QUADRATIC_ISOTROPIZATION_GENERATES_ALL_S5_INVARIANTS_THROUGH_16 = FALSE`; primitive S5 extension directions start at degree 4.
- Iter041: `HIGHER_ORDER_SOURCE_EXTENSION_BUDGET_PRESENT = TRUE`; complete K5 all-delta sector already has superficial extension degree `omega=6`.
- Iter042: Appendix-D edge-local source span strongly reduces but does not uniquely select the primitive extension ambiguity.
- Iter044: source-faithful joint finite-spectral-`i epsilon` K3 kernel still has a common-cycle polynomial obstruction.
- Iter045: the exact correlated finite part is coordinate-covariant on held-out K3 data and is a viable K3 candidate extension only.
- Iter046: applying that sequential one-dimensional rule to K4 gives `K4_FINITE_PART_ORDER_OR_FOREST_DEPENDENT` with valid EPRL/no-contact control, so preferred order/tree is forbidden.
- Iter058: exact K4 strict-chamber feasibility iff strong tournament connectivity.
- Iter059: source-backed equal-spin Toller wedge reversal gives branch swap under group inversion.
- Iter060: the K4 tournament/positive-circulation analyticity surrogate is covariant under the source-backed reversal law.
- Iter061: orientation-blind identification of physical `kappa` with ordered spectral sign is obstructed.
- Iter062: minimal ordered bridge `s(a,b)=c eta(a,b) kappa_ab` is covariant but retains an unfixed global convention.

## Next admissible step

Prospectively test the Hormander wavefront collision condition on the source-backed K4 spectral-denominator skeleton using the Iter059/062 reversal/orientation bridge. This gate may only establish a necessary microlocal compatibility/obstruction for the denominator skeleton; it must not be promoted to the full Toller wavefront set or a physical sector selector. If a canonical product route survives the skeleton test, the next task is a full Toller wavefront/growth proof; if it fails on part of the domain, the remaining extension locus must be localized before any K5 construction.

## Claim locks

- no `NEW_PHYSICS_FOUND` or complete-QG claim;
- no physical causal-vertex finiteness/divergence theorem;
- no universal causal-EPRL or contour no-go theorem;
- no physical causal-sector selection from tournament results;
- no G3 PASS or F9/G8 promotion;
- no arbitrary counterterm, fitted cancellation coefficient, or preferred sequential order;
- do not replace the published spectral `i epsilon` prescription with `beta+i epsilon`;
- keep absolute integrability, conditional/PV finite part, source-defined distributional amplitude, and microlocal product existence distinct.
