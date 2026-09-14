# Iter080K-SM preregistration — new Toller analyticity authority vs joint-K5 extension selector

Date: 2026-09-14

## Trigger / admissibility

A primary source not represented in the frozen Iter080E BCG/Beltran selector census has been identified:

E. Bianchi, C. Chen, M. Gamonal, **Toller matrices and the Feynman i-epsilon in spinfoams**, arXiv:2604.24945 (2026).

This is a genuinely additional primary authority and therefore satisfies the `NEW_PRIMARY_AUTHORITY` route allowed by `status/CURRENT.md`.

A preliminary identification pass established only that this paper proves uniqueness of the **one-wedge Toller branch splitting** from analytic/asymptotic/pole data. The scientific gate below is frozen before repository source-matrix implementation and before any claim about whether that uniqueness lifts to the full K5 collision-extension problem.

## Frozen question

Does arXiv:2604.24945 provide an explicit source-defined principle strong enough to select the **joint ten-wedge K5 distributional extension** and thereby act on the Iter077Q infinite-dimensional tangential ambiguity?

The paper's uniqueness theorem for individual Toller functions must not be silently promoted to a uniqueness theorem for their source-ordered K5 product/group integral.

## Frozen predicates

P1 `ONE_WEDGE_UNIQUENESS_EXPLICIT`:
The source explicitly proves that the two Toller branches are uniquely fixed by the stated analytic/asymptotic/pole/sum-rule conditions (equivalently by the Feynman i-epsilon projector).

P2 `JOINT_K5_OBJECT_EXPLICIT`:
The source explicitly defines the full ten-wedge K5 source-ordered distributional object at simultaneous collision, beyond merely defining individual Toller functions/matrices.

P3 `CORRELATED_JOINT_K5_EXTENSION_RULE_EXPLICIT`:
The source explicitly gives a correlated multi-wedge boundary-value/extension prescription that fixes the K5 simultaneous-collision distribution rather than ten independent one-wedge prescriptions.

P4 `ITER077Q_TANGENTIAL_SELECTION_POWER_EXPLICIT`:
The source provides a condition with actual selection power over smooth tangential coefficient functions on the common-collision manifold (or an equivalent full-function-space uniqueness theorem), sufficient in scope to eliminate the Iter077Q `Q^n F delta_N` freedom.

P5 `NO_REPRESENTATION_COMPOSITION_ASSUMPTION`:
The audit must retain the source statement that Toller T-matrices are functions rather than Lorentz-group representations and cannot use ordinary representation composition to manufacture P2-P4.

## Frozen source evidence policy

- Positive P2-P4 require an explicit equation/theorem/prescription in arXiv:2604.24945, not an inference from one-wedge uniqueness.
- Absence claims must be based on a systematic term/section audit of the source for full vertex/K5/product/distribution/extension/collision/multi-wedge/correlated prescriptions, with relevant positive one-wedge sections anchored.
- The BCG causal-vertex paper may be used only as context for what K5 vertex is being discussed, not to fill a missing prescription in the new Toller paper.

## Frozen classifications

If P1=true, P5=true, but any of P2-P4=false:

`ITER080K_SM_NEW_TOLLER_ANALYTICITY_AUTHORITY_UNIQUELY_FIXES_ONE_WEDGE_BRANCHES_BUT_DOES_NOT_EXPLICITLY_SELECT_JOINT_K5_EXTENSION_SOURCE_BRIDGE_BLOCKED_SCOPED`

Verdict: `BLOCKED_SOURCE_BRIDGE_SCOPED`.

If P1-P5 all true:

`ITER080K_SM_NEW_TOLLER_ANALYTICITY_AUTHORITY_SUPPLIES_EXPLICIT_JOINT_K5_EXTENSION_SELECTOR_SOURCE_CANDIDATE_SCOPED`

Verdict: `SOURCE_CANDIDATE_FOUND_SCOPED`, which only authorizes a later separately preregistered implementation/test against Iter077Q; it does not itself establish uniqueness.

If P1 or P5 fails because the source was misread, classify `SCIENTIFIC_FAIL_SOURCE_CHARACTERIZATION_SCOPED`.

Infrastructure/provenance failure remains separate.

## Claim ceiling

No `NEW_PHYSICS_FOUND`; no CRQN v0.3; no unique K5 extension unless a later gate actually proves it; no G3 PASS; no F9/G8/K5 promotion; no causal-vertex finiteness/divergence theorem. One-wedge analytic uniqueness and joint-K5 distributional-extension uniqueness are distinct objects.
