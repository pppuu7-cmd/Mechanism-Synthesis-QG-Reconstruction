# Iter080F-SM adversarial implementation review

**Date:** 2026-09-14

## Reviewed result

Researcher result: `results/ITER080F_SM_CRQN_EXISTING_AXIOM_SELECTOR_CENSUS_RESULT.md`, commit `61ee95efdda1d13b47e3ef04de61d40d08ca95c1`.

Researcher classification:
`ITER080F_SM_CRQN_V0_2_HAS_NO_PREEXISTING_FULL_FUNCTION_SPACE_EXTENSION_SELECTOR_AXIOM_ANTI_RESCUE_BLOCKED_EXACT_CENSUS_SCOPED`.

Researcher verdict: `BLOCKED_EXISTING_AXIOM_SELECTOR_MISSING`.

Prospective preregistration: `382948b3369c3bc2132ff4c2757500fdd7b77ba1`.
Initial implementation: `082bfb7facf57f8cf42405a1b514d88a7ffb8831`.
Control-only timezone repair plan: `9f857e8acec6de180185a206ec67791efe333f37`.
Authoritative claimed production head: `1a78e94ad72e4bdad4b132a37699debd964789bc`.
Claimed terminal run: `34837108991`.

## Adversarial finding

Verdict: `INVALID_IMPLEMENTATION`.

The scientific negative conclusion is plausible from direct reading of the two frozen candidate documents, but the executed gate does not satisfy its own frozen Lane B/Lane C contract. The invalidation is implementation-scoped; it is not evidence that a qualifying pre-existing selector actually exists.

### 1. Frozen Lane C control 3 was not implemented as preregistered

The preregistration requires an aspirational statement such as `derive RG/gauge closure later` to **fail A1, A2 and A3**.

The executable Lane C instead hard-codes:

`aspiration = {A1_PREEXISTING: True, A2_FULL_W_ACTION: False, A3_SELECTION_POWER: False, ...}`

and checks only `not classify_axiom(aspiration)`. This proves merely that at least one required predicate is false. It does not test the frozen requirement that the aspiration itself fails A1/A2/A3, and it explicitly assigns A1 the opposite frozen value.

The same semantic mismatch propagates into Lane B: open targets/blockers such as the RG target, `F_causal is unknown`, and the finite-relation existence question are assigned `A1_PREEXISTING=True`, although the frozen A1 definition says a qualifying **prescription** must actually be stated and not merely named as an open target/problem.

Because the aggregate consumes the Lane-C `valid` Boolean, green CI cannot repair this contract mismatch.

### 2. Frozen Lane C control 4 was replaced by a hard-coded Boolean

The preregistration requires:

`mutating/removing all post-Iter077Q files must leave the scientific census unchanged`.

The executable Lane C performs no mutation/removal, no alternate checkout/corpus construction, and no recomputation of Lane B. It simply emits:

`scientific_inputs_only_two_frozen_candidate_blobs = True`.

This is an assertion, not the required independence control. Workflow job `lane-c` runs only `python analysis/iter080f_sm_crqn_existing_axiom_selector_census.py --lane C`; no workflow step supplies the missing mutation/replay control.

### 3. Frozen Lane B completeness is not executable

Lane B is required to `Parse/audit every candidate statement plausibly relevant to amplitude uniqueness, normalization, composition, RG, gauge/refoliation, analyticity/unitarity, and finite relation Phi`.

The implementation evaluates a fixed list of six hand-authored rows. It does not executable-check completeness of the census against the two frozen candidate documents. In particular, the frozen v0.1 document contains additional plausibly relevant statements that are outside the enumerated rows, including:

- M14 analyticity/unitarity as an external consistency filter;
- G3 falsification-matrix requirement `normalized amplitude/measure and composition rule`;
- the explicit gauge/refoliation decision rule;
- the structural-kill condition on `normalized observables` from the same microscopic measure.

Direct inspection does not reveal a hidden A1-A5-complete selector in those omitted statements, but the frozen contract requires complete census coverage rather than reliance on a selected representative list. The code's `anchors_valid` only proves that its six chosen anchors exist.

### 4. Negative control 2 is also weaker than frozen wording

The preregistration requires a finite scalar normalization condition to fail **A2 and A3**. The code assigns A2/A3 false but the test is again only `not classify_axiom(finite_scalar)`, so a future accidental change to one of A2/A3 could still pass as long as some other predicate remained false. The control is therefore not predicate-specific as frozen.

## Provenance and source-object checks

Prospective chronology is otherwise intact. The first run `34836984921` was correctly quarantined for timestamp-string provenance failure. The control-only repair `9f857e8acec6de180185a206ec67791efe333f37` changed only Lane A timestamp normalization and explicitly prohibited Lane B/C/D scientific-logic changes. The later run `34837108991` is terminal-successful, with jobs A `103953327454`, B `103953327735`, C `103953327704`, D `103953327677`, aggregate `103953376077`, aggregate artifact `10344587578`, digest `sha256:bd815e8cafa5a03c3d13af96220570758a9300e7f759671c81b2ca198b2b86f9`.

The true object targeted by the written preregistration is not a scalar K4/K5/Hodge surrogate: it asks whether the pre-Iter077Q CRQN candidate specification already contained an independently motivated selector capable of acting on the full Iter077Q extension function space `W`. No representative boundary state, special-spin extrapolation, saddle extrapolation, regulator substitution or source-order swap is used by the written result.

The controlling Iter077 contact-formula erratum remains unchanged; historical Iter077E/F source-lock-invalid siblings remain quarantined. Iter080F itself does not use the incorrect contact formula.

## Counterexample-first attempts

1. **Classifier-semantic counterexample:** succeeds. An aspirational rule is frozen to fail A1/A2/A3 but the executable control assigns A1 true and still passes.
2. **Post-Iter077Q independence counterexample:** succeeds as an implementation witness. The required mutation/removal replay is absent; a literal `True` substitutes for the control.
3. **Census-completeness witness:** succeeds. Additional plausibly relevant frozen statements exist outside the six-row Lane-B list; no executable completeness criterion detects their omission.
4. **Hidden-selector search in omitted statements:** no qualifying full-W selector found by direct adversarial reading. This limits the invalidation to implementation authority; it does not reverse the physical blocker.
5. **Wrong-object/surrogate attack:** rejected for the written target. The gate is an axiom census, not a computation on a scalar graph surrogate.
6. **Source-order/regulator rescue:** irrelevant to the anti-rescue census and not used to promote a local amplitude.

## Scientific consequence

Iter080F may not be used downstream as authoritative proof that the complete frozen pre-Iter077Q CRQN v0.1/v0.2 candidate corpus lacks an A1-A5-complete selector until a control-only repair executes the unchanged frozen Lane B/Lane C contract.

This does **not** unblock CRQN. The unique local K5 amplitude remains independently blocked by Iter077Q plus the confirmed Iter080A/repaired Iter080D obstructions and repaired Iter080E `BLOCKED_OBJECT_DEFINITION` for the frozen primary causal-Toller source corpus. Causal multivertex E3/E4/E6 remains separately `BLOCKED_SOURCE_BRIDGE` under Iter080B. E7/E8, G3, regulator independence and RG remain downstream-locked.

## Required repair

A control-only Iter080F retry may retain the original preregistration and frozen two-file corpus only if it changes no scientific hypothesis, A1-A5 definition, PASS/BLOCKED/INVALID criterion or interpretation ceiling. It must:

1. make Lane C explicitly assert the required predicate-wise outcomes: positive control A1-A5 all true; finite scalar A2=false and A3=false; aspiration A1=false, A2=false, A3=false;
2. actually execute the post-Iter077Q mutation/removal independence control by recomputing the scientific census from the two pinned candidate blobs in an environment where later files are absent/poisoned, or by an equivalent prospectively frozen executable dependency-isolation certificate;
3. make Lane B census completeness auditable over all plausibly relevant statements in the two frozen documents, including analyticity/unitarity, normalized amplitude/measure/composition, gauge/refoliation and normalized-observable language, with exact text anchors and A1-A5 classifications;
4. preserve the historical runs/results unchanged.

If satisfying item 3 requires changing the scientific corpus or selector predicates rather than merely implementing the already-frozen completeness requirement, a new prospectively preregistered successor gate is required instead of rewriting Iter080F.
