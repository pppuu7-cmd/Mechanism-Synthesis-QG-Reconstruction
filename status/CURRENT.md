# Current MSQGR research state

**Date:** 2026-09-13

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- Physical F9 (`CAUSAL_ANALYTICITY_RG_INVARIANT`): `BLOCKED`
- G3 quantum dynamics: `OPEN`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`
- K5 distributional/vertex extension: `BLOCKED_CORRELATED_EXTENSION_OBJECT_MISSING`
- Active front: `SOURCE_ANALYTICITY_SELECTOR / JOINT_BOUNDARY_VALUE_UNIQUENESS`

## Newly controlling source/direct chain

- Iter063B authoritative retry run `34731891190`, job `103656077408`, artifact `10310265245`, digest `sha256:dc0a3f250949b780ebe758af82f1b4ef3f27eeb1370fe7bc46b5fb1c42b064ba`: `ITER063B_SOURCE_CONTROL_BLOCKED_MISSING_EXPLICIT_RELATION`. The earlier green run `34729216381` was implementation-invalid self-reference and is non-authoritative.
- Primary source snapshot commit `7df82d28dd6426aa7aaac353a1e0abf795e6fdee`: Bianchi-Chen-Gamonal arXiv `2601.23162`, DOI `10.1103/fwql-t4yr`; pins Eq.(3) spectral Feynman `i epsilon`, Eq.(4) direct ten-wedge fixed-causal vertex, Eq.(5) `T+ + T-=D`, Eq.(6) unconstrained independent-wedge EPRL sum, Eq.(7) Cartan/magnetic representation.
- Iter063C authoritative run `34732046499`, job `103656528583`, artifact `10309351521`, digest `sha256:a8fad3edd3e820b849fa0be8fcf0939571fdc65b4919b2369d46efb2f2aa4eac`: 4/4 `ITER063C_PRIMARY_SOURCE_VERTEX_CONTROL_PINNED`.
- Iter064A authoritative run `34732198011`, aggregate job `103656960238`, artifact `10309427622`, digest `sha256:2cb05aa6b626f23256a0ba1fcd3502404ecc3387a8521baece660ab238a9f161`: 6/6 `ITER064A_DIRECT_CAUSAL_POINTWISE_EPRL_CONTROL_PASS`. Initial run `34732114933` was runtime-invalid before science and is non-authoritative. Worst controls: KAK `1.9462e-15`, edge additive `5.2303e-64`, independent-wedge EPRL sum `5.6631e-64`, global sigma-flip duplication `1.1054e-80`; min pair boost `0.44134`.
- Historical Iter038 run `34694739107` was re-consumed rather than repeated: 6/6 raw carrier-S5 lanes PASS. Worst causal even/odd errors `3.39e-14 / 2.38e-14`, EPRL `6.95e-12`, KAK `2.34e-15`, all within its frozen gates.
- Iter064B authoritative run `34732360103`, aggregate job `103657391209`, artifact `10310016825`, digest `sha256:8012eb7aedfcb1765509a7e86e94ff3816da3f349ca2524e208236c29d665a8a`: 4/4 `ITER064B_K4_SOURCE_PREREQUISITES_CLOSED_FOR_K5_QUALIFICATION`. This closed the prerequisite blocker only; it did not pass K5.
- Iter065A prereg `987b0b27aaccc9e75ceed5fe209e9944a17f5e94`, authoritative head `fd93c7e968df49f0b1df9468117cf6795afed701`, run `34732545131`, aggregate job `103657905982`, artifact `10310465490`, digest `sha256:3d171139e80274074924065acdc12fdba265de78238f1cf2a859b62820dad5ba`: 0/4, `ITER065A_K5_BLOCKED_CORRELATED_EXTENSION_OBJECT_MISSING`.
- Iter066A prereg `b6846ee0515853cd9981dc0d6688c021174922be`, authoritative head `9cfc3cc3f94e9246f103d6f50628621726cd9967`, run `34734333416`, aggregate job `103662960682`, artifact `10309673723`, digest `sha256:05fd9933952a634158d4cee4a5f680ba0e48182b748a0d15053f7aab4f85082b`: `ITER066A_GENERIC_MULTIVARIATE_FRAMEWORK_AVAILABLE_SOURCE_SELECTOR_STILL_MISSING`. `BBK2009_WONDERFUL_EG` supplies a genuine multivariate framework, but no audited source supplies a unique physical Toller/EPRL selector. Durable result: `status/ITERATION_066A_RESULT.md`.

## Exact K5 blocker after Iter066A

The project no longer lacks generic multivariate extension machinery in the abstract: BBK-style wonderful/analytic-regularization machinery exists for nontrivial singular arrangements. What remains missing is the **source-faithful selector/bridge** proving that the physical Toller finite-spectral-`i epsilon` family itself has the required unique correlated K5 distributional boundary value.

The unresolved requirements are:

1. a source-defined *joint* multivariate analytic/distributional family corresponding to the physical causal vertex, not a support-native or Euclidean subtraction surrogate;
2. a theorem-level selector establishing uniqueness of the boundary value/extension without arbitrary local counterterms or preferred sequential order;
3. hypotheses sufficient for tree/cycle/permutation/order independence and controlled regulator removal in the intersecting K5 singular arrangement;
4. inheritance of Eq.(5)/(6) independent-wedge EPRL control at the resulting **distributional K5 level**.

This is `BLOCKED`, not a theorem of vertex divergence/nonexistence.

## Historical distributional localization retained

- Iter039: `S5_SYMMETRY_ONLY_EXTENSION_UNIQUE_THROUGH_16 = FALSE`; first non-unique invariant degree 4.
- Iter040: `QUADRATIC_ISOTROPIZATION_GENERATES_ALL_S5_INVARIANTS_THROUGH_16 = FALSE`; primitive S5 extension directions start at degree 4.
- Iter041: `HIGHER_ORDER_SOURCE_EXTENSION_BUDGET_PRESENT = TRUE`; complete K5 all-delta sector already has superficial extension degree `omega=6`.
- Iter042: Appendix-D edge-local source span strongly reduces but does not uniquely select the primitive extension ambiguity.
- Iter044: source-faithful joint finite-spectral-`i epsilon` K3 kernel still has a common-cycle polynomial obstruction.
- Iter045: the exact correlated finite part is coordinate-covariant on held-out K3 data and is a viable K3 candidate extension only.
- Iter046: applying that sequential one-dimensional rule to K4 gives `K4_FINITE_PART_ORDER_OR_FOREST_DEPENDENT` with valid EPRL/no-contact control, so preferred order/tree is forbidden.

## Next admissible step

Prospectively qualify boundary-value / microlocal uniqueness routes for the physical finite-spectral-`i epsilon` family. A route is scientifically useful only if it states checkable hypotheses for a joint multivariate boundary value (holomorphy/tube or wavefront/cone conditions, growth/temperedness, uniqueness) and can in principle be tied to the BCG2026 Toller prescription and distributional Eq.(5)/(6). Generic subtraction or finite-part machinery without such a source bridge is insufficient.

## Claim locks

- no `NEW_PHYSICS_FOUND` or complete-QG claim;
- no physical causal-vertex finiteness/divergence theorem;
- no universal causal-EPRL or contour no-go theorem;
- no physical causal-sector selection from tournament results;
- no G3 PASS or F9/G8 promotion;
- no arbitrary counterterm, fitted cancellation coefficient, or preferred sequential order;
- do not replace the published spectral `i epsilon` prescription with `beta+i epsilon`;
- keep absolute integrability, conditional/PV finite part, and source-defined distributional amplitude distinct.
