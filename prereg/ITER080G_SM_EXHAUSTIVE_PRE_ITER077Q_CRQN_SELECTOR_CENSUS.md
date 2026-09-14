# Iter080G-SM — exhaustive pre-Iter077Q CRQN full-function-space selector census

**Scientific gate:** `EXHAUSTIVE_PRE_ITER077Q_CRQN_SELECTOR_ANTI_RESCUE_CENSUS`

## Prospective timing lock

This preregistration is frozen after the independent invalidation of the repaired Iter080F Lane-B completeness certificate and before any Iter080G implementation/production result is inspected.

This is a new successor gate, not a third patch of Iter080F. Frozen scientific question and A1-A5 are preserved. The defect being removed is statement-universe incompleteness.

## Frozen candidate corpus

Only the two pre-Iter077Q candidate specifications are positive scientific evidence:

1. `candidates/CANDIDATE_A_CRQN.md`, frozen blob SHA `a3023dadb75f4c53d0c44a6de1c46958f4149178`.
2. `candidates/CANDIDATE_A_CRQN_V0_2.md`, frozen blob SHA `3933c110f9bafabb6593f8301029adaa25458bb2`.

Both predate Iter077Q durable result commit `5941b3a064d93f2898d9e9a48545826e950455f1`.

No later file may be used as positive evidence that CRQN already contained a selector. Later authority is dependency/provenance control only.

## Frozen selector predicates

A pre-existing CRQN statement qualifies only if it satisfies all:

- **A1_PREEXISTING:** explicitly stated in the frozen candidate corpus, not merely a future target.
- **A2_FULL_W_ACTION:** acts on the whole admissible Iter077Q extension function space `W` or an explicitly equivalent infinite-dimensional object.
- **A3_SELECTION_POWER:** supplies enough rule/content to distinguish/select extension data, not just a property shared by an infinite family.
- **A4_OBJECT_REACH:** reaches the local causal/K5 amplitude or its extension/renormalization data, not only later continuum/RG observables.
- **A5_INDEPENDENT_MOTIVATION:** required by the pre-existing CRQN architecture rather than reconstructed from Iter077Q.

## Frozen exhaustive statement universe

The implementation must deterministically parse the exact frozen bytes of both candidate blobs into a complete ordered block universe.

Parsing rules are frozen now:

1. Normalize CRLF to LF; do not otherwise rewrite source text.
2. Split on one-or-more blank lines into raw Markdown blocks.
3. A block whose first non-space characters begin with `#` is a `HEADING_BLOCK` and may be excluded only with reason `HEADING_ONLY`.
4. Every other nonempty block is a `SCIENTIFIC_BLOCK`, including paragraphs, list blocks, tables, formula-containing blocks, status blocks, and mixed prose/formula blocks.
5. Stable block ID is `V01-BNNN-<sha256(raw_block)[:12]>` or `V02-BNNN-<sha256(raw_block)[:12]>`, where `NNN` is the 1-based raw-block ordinal in that file.
6. Every `SCIENTIFIC_BLOCK` must appear exactly once in the frozen classification manifest. No keyword-based relevance prefilter is permitted.
7. A scientific block may be excluded from A1-A5 semantic scoring only by one of these pre-frozen machine-checkable reasons:
   - `METADATA_ONLY`: block consists only of Status/Promotion/Parent metadata lines and contains no mathematical/physical prescription;
   - `EXTERNAL_ANCHORS_ONLY`: bibliography/literature-anchor prose that explicitly says it does not validate/specify CRQN;
   - `ABLATION_LIST_ONLY`: an ablation checklist that removes mechanisms but does not prescribe local amplitude/extension selection;
   - `FALSIFICATION_STATUS_TABLE_ONLY`: a status/pass-condition table with no prescription beyond status bookkeeping.
8. Any block not matching one of those four exact exclusion rules must receive A1-A5 booleans plus a short literal rationale and a text digest.
9. Production must fail `INVALID_IMPLEMENTATION` if the generated universe/hash differs from the preregistered manifest/hash, if any scientific block is missing/duplicated, or if any excluded block fails its exact exclusion predicate.

## Mandatory explicitly visible witnesses

Regardless of other classifications, the manifest/report must visibly classify these statements if their block IDs are present:

- v0.1 history amplitude `A[B_f,B_i] = Sum_H ...`;
- v0.1 alternate history expression `Z = Sum_H integral dmu(lambda) exp(i S_micro...) Chi_causal(H)`;
- v0.1 `Gamma_k` effective-functional / finite-dimensional UV critical-surface target;
- v0.1 schematic RG flow `k dGamma_k/dk = B[Gamma_k]` and fixed-point condition;
- v0.1 near-term local-amplitude requirement: boundary composition + gauge covariance + causal orientation rule;
- v0.1 early-success microstate/amplitude-pair criterion;
- v0.2 history amplitude product `A_CRQN = Prod_f A_f Prod_e A_e Prod_v A_v^CRQN`;
- v0.2 placeholder `A_v^CRQN = A_v^geom F_causal` with `F_causal` unknown;
- v0.2 six required causal-amplitude properties;
- v0.2 finite relation `Phi(A_v,o,j,i,beta,gauge)=0` and its four motivating requirements.

## Frozen lanes

### Lane A — provenance + universe integrity

Verify exact candidate blob SHAs and pre-Iter077Q timing. Generate the complete block universe with the frozen parser, compare all stable IDs/digests to the frozen manifest, and prove coverage counts: every raw block is heading, machine-excluded, or A1-A5-classified exactly once.

### Lane B — exhaustive A1-A5 census

For every non-excluded scientific block, report A1-A5 and rationale. A qualifying pre-existing selector exists iff at least one block (or an explicitly cross-referenced set of blocks identified prospectively in the frozen manifest) satisfies all five predicates. No post-production addition/removal of blocks or criteria is allowed.

### Lane C — classifier/adversarial controls

Required controls:

1. synthetic explicit function-space prescription scores A1-A5 true;
2. finite scalar normalization scores A2/A3 false;
3. aspirational future RG/gauge target fails selector qualification;
4. every Critic-identified omitted Iter080F witness is present and classified;
5. inject one extra scientific paragraph into a temporary candidate copy: universe/hash mismatch must force invalidation;
6. delete one manifest entry: coverage check must force invalidation;
7. falsely exclude a scientific formula block as `HEADING_ONLY`: exclusion predicate must force invalidation.

### Lane D — dependency and claim locks

Verify Iter077Q, Iter080A, repaired Iter080D, repaired Iter080E, Iter080B, and the Iter080F invalidation state from durable authority. Do not promote K5/G3/F9/G8 or downstream E7/E8.

## Frozen outcomes

If provenance, universe, manifest, coverage, or controls fail:

`INVALID_IMPLEMENTATION_OR_PROVENANCE`.

If at least one pre-existing block/set satisfies A1-A5:

`ITER080G_SM_CRQN_PREEXISTING_FULL_FUNCTION_SPACE_SELECTOR_AXIOM_FOUND_REQUIRES_DIRECT_K5_TEST_SCOPED`.

If none satisfies A1-A5:

`ITER080G_SM_EXHAUSTIVE_PRE_ITER077Q_CRQN_CORPUS_HAS_NO_FULL_FUNCTION_SPACE_EXTENSION_SELECTOR_AXIOM_ANTI_RESCUE_BLOCKED_EXACT_CENSUS_SCOPED`.

Verdict: `BLOCKED_EXISTING_AXIOM_SELECTOR_MISSING`.

## Interpretation ceiling / claim locks

A blocked result is only a statement about the frozen pre-Iter077Q CRQN v0.1/v0.2 corpus. It does not forbid a new independently motivated selector in a future CRQN version and is not a no-go theorem for causal spin foams or quantum gravity.

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no unique K5 extension; no physical causal-vertex finiteness/divergence theorem; no universal causal-EPRL/contour no-go theorem; no G3/F9/G8/K5 promotion; no fitted/post-hoc selector; no replacement of published spectral `i epsilon` by an invented regulator.
