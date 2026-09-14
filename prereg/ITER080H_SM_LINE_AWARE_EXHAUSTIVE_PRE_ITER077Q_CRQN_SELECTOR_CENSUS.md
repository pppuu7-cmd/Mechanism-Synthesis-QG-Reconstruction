# Iter080H-SM — line-aware exhaustive pre-Iter077Q CRQN selector census

**Scientific gate:** `LINE_AWARE_EXHAUSTIVE_PRE_ITER077Q_CRQN_SELECTOR_ANTI_RESCUE_CENSUS`

## Prospective timing / predecessor lock

Frozen after Iter080G universe-build-only run exposed a pre-production parser defect and before any Iter080H implementation or production scientific result.

Iter080G is not scientific authority: its frozen parser would classify any blank-line block beginning with `#` as heading-only even when the same block contains substantive lines after the heading. The observed examples include v0.1 near-term programme subsections. No Iter080G A1-A5 census was executed.

Iter080H preserves the scientific question and A1-A5 unchanged while replacing only the defective statement-universe segmentation prospectively.

## Frozen positive-evidence corpus

- `candidates/CANDIDATE_A_CRQN.md`, blob `a3023dadb75f4c53d0c44a6de1c46958f4149178`.
- `candidates/CANDIDATE_A_CRQN_V0_2.md`, blob `3933c110f9bafabb6593f8301029adaa25458bb2`.

Both predate Iter077Q result `5941b3a064d93f2898d9e9a48545826e950455f1`. Later files are controls only.

## Frozen A1-A5

- `A1_PREEXISTING`: explicit in frozen corpus, not merely future target.
- `A2_FULL_W_ACTION`: acts on whole Iter077Q extension space `W` or explicitly equivalent infinite-dimensional object.
- `A3_SELECTION_POWER`: distinguishes/selects extension data rather than only imposing a broadly shared property.
- `A4_OBJECT_REACH`: reaches local causal/K5 amplitude or extension/renormalization data.
- `A5_INDEPENDENT_MOTIVATION`: pre-existing CRQN motivation, not retrofitted from Iter077Q.

## Frozen line-aware universe algorithm

For each exact frozen UTF-8 file after CRLF->LF only:

1. Scan lines in order.
2. Every Markdown heading line matching `^\s*#{1,6}\s+` is emitted as its own `HEADING_LINE` record, even if no blank line follows it.
3. Heading lines terminate any current scientific segment and are never allowed to absorb following non-heading lines.
4. Non-heading lines accumulate into a scientific segment until a blank line or the next heading line.
5. Consecutive non-heading lines separated by no blank line remain one segment, preserving lists/tables/formula-plus-prose units.
6. Empty segments are discarded.
7. Stable record ID: `<V01|V02>-L<start:03d>-<end:03d>-<sha256(exact_segment)[:12]>`.
8. Every non-heading segment must occur exactly once in the frozen manifest. There is no keyword/relevance prefilter.
9. Machine exclusions allowed only for exact predicates:
   - `METADATA_ONLY`: all nonblank lines begin with `**Status:**`, `**Promotion:**`, or `**Parent:**`;
   - `EXTERNAL_ANCHORS_ONLY`: segment is in section 14 of v0.1 and contains the literal statement that those sources do not validate CRQN synthesis;
   - `FALSIFICATION_STATUS_TABLE_ONLY`: segment is a Markdown table in section 9 and contains `Current status` plus only gate status bookkeeping;
   - `ABLATION_LIST_ONLY`: segment is inside section 10 and is solely the listed `CRQN - M..` ablation questions.
10. All remaining segments receive A1-A5 booleans, rationale, exact SHA256 and text anchor.
11. Universe/manifest coverage is exact-set equality. Missing/duplicate/extra IDs => `INVALID_IMPLEMENTATION`.
12. Freeze the complete universe manifest and its digest in-repo before production execution. Production may read but not rewrite it.

## Mandatory witness visibility

The report must contain classifications for: v0.1 history amplitude; alternate `Z`; `Gamma_k`/UV critical surface; RG-flow/fixed-point equations; near-term local amplitude boundary-composition/gauge/causal-orientation prescription; early-success microstate/amplitude pair; v0.2 product amplitude; unknown `F_causal` placeholder; six local-factor requirements; finite `Phi(...)` research equation and motivating four-term requirement.

## Frozen lanes

### A — provenance + exact universe/manifest coverage
Check frozen blob SHAs, timing, regenerated line-aware IDs/digests, exact-set equality to frozen manifest, and exclusion predicates.

### B — exhaustive A1-A5 census
Classify every non-excluded segment. A selector is found only if one manifest entry, or a manifest-frozen explicitly linked set of entries, satisfies all A1-A5. No post-run synthesis of scattered statements is allowed.

### C — adversarial controls
Positive full-W synthetic selector => A1-A5 true; finite scalar normalization => A2/A3 false; aspirational RG/gauge future target => not selector; all Critic-identified Iter080F omissions must be present; injected extra paragraph, deleted manifest entry, heading/body coalescence, or false exclusion must each force invalidation.

### D — dependencies/claim locks
Verify Iter077Q, Iter080A, repaired Iter080D/E, Iter080B, Iter080F invalidation, and Iter080G pre-production parser invalidation. No downstream promotion.

## Frozen outcomes

Invalid provenance/universe/manifest/controls:
`INVALID_IMPLEMENTATION_OR_PROVENANCE`.

At least one qualifying pre-existing selector:
`ITER080H_SM_CRQN_PREEXISTING_FULL_FUNCTION_SPACE_SELECTOR_AXIOM_FOUND_REQUIRES_DIRECT_K5_TEST_SCOPED`.

None:
`ITER080H_SM_LINE_AWARE_EXHAUSTIVE_PRE_ITER077Q_CRQN_CORPUS_HAS_NO_FULL_FUNCTION_SPACE_EXTENSION_SELECTOR_AXIOM_ANTI_RESCUE_BLOCKED_EXACT_CENSUS_SCOPED`.
Verdict `BLOCKED_EXISTING_AXIOM_SELECTOR_MISSING`.

## Claim ceiling
No `NEW_PHYSICS_FOUND`; no complete-QG; no unique K5 extension; no G3/F9/G8/K5 promotion; no causal-vertex finiteness/divergence theorem; no universal causal-EPRL/contour no-go theorem; no fitted/post-hoc selector; keep one-wedge spectral `i epsilon` in source scope only.
