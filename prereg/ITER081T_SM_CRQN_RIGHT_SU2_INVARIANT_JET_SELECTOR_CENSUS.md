# Iter081T-SM preregistration — CRQN v0.1/v0.2 corrected invariant-jet selector census

Status: PROSPECTIVELY_FROZEN_BEFORE_IMPLEMENTATION
Date: 2026-09-14

## Motivation

Iter081R repairs the historical Iter077Q source-lock error. The controlling local ambiguity target is no longer an infinite tangential function space. The demonstrated source-compatible scalar ambiguity subspace is the SO(3) x S5 invariant normal-jet space through order 8 with dimensions by order

`[1,0,1,0,3,0,7,0,16]`, total `28`.

Historical Iter080H audited CRQN v0.1/v0.2 against the now-invalid infinite-W target and therefore cannot be reused as the decisive candidate-corpus selector gate.

## Frozen corpus

Only the pre-existing candidate documents:

- `candidates/CANDIDATE_A_CRQN.md`
- `candidates/CANDIDATE_A_CRQN_V0_2.md`

at the production checkout commit. No later result/status/prereg text may count as positive selector evidence.

## Frozen target

A qualifying pre-existing selector must act on the corrected source-compatible local ambiguity target: the demonstrated 28-dimensional scalar SO(3) x S5 invariant normal-jet coefficient subspace from Iter081R, or on a rigorously larger object in a way that proves uniqueness on this 28-dimensional subspace.

## Frozen qualifying predicates

A candidate statement qualifies only if all of Q1-Q6 are satisfied from the frozen corpus itself.

Q1 EXPLICIT_LOCAL_OBJECT: it specifies an equation, normalization, boundary-value rule, differential/spectral condition, or other mathematically explicit rule acting on the local K5 amplitude / extension data, not merely an architectural desideratum.

Q2 CORRECTED_TARGET_REACH: it explicitly acts on all invariant normal-jet coefficients through allowed order 8, or supplies a uniqueness theorem/rule whose scope rigorously includes that coefficient space.

Q3 SUFFICIENT_SELECTION_POWER: either (a) at least 28 independent scalar conditions are explicitly given with a demonstrated full-rank action on the Iter081R scalar basis, or (b) an explicit non-finite/function-valued rule is given together with a proof of uniqueness on that basis. Merely saying `finite relation`, `composition`, `RG closure`, `gauge recovery`, `causal rule`, or similar is insufficient without the actual operator/equations and rank/uniqueness content.

Q4 SYMMETRY_COMPATIBLE: the rule respects the exact node-wise right-SU(2) gauge covariance/quotient, S5 relabeling covariance, and boundary covariance relevant to the corrected K5 local problem; no preferred node/order/basis may be inserted without source justification.

Q5 SOURCE_ORDER_COMPATIBLE: the rule is compatible with the locked order `one-wedge spectral/spinor integration -> Toller function -> ten-wedge product -> full boundary contraction -> K5 group integration / extension`; it may not replace the published spectral i-epsilon by an unrelated post-hoc local regulator.

Q6 PREEXISTING_NOT_POSTHOC: the rule is genuinely present in CRQN v0.1/v0.2 corpus and is not imported from Iter081R/S or invented during this audit.

## Frozen classifications

- `ITER081T_SM_CRQN_PREEXISTING_CORRECTED_INVARIANT_JET_SELECTOR_FOUND_EXACT_SCOPED` iff at least one corpus rule satisfies Q1-Q6 and the production evidence records the exact text location plus a reproducible 28-direction rank/uniqueness certificate.
- `ITER081T_SM_CRQN_V0_1_V0_2_HAS_NO_PREEXISTING_CORRECTED_INVARIANT_JET_SELECTOR_BLOCKED_EXACT_CENSUS_SCOPED` iff the complete frozen corpus is enumerated and no rule satisfies Q1-Q6.
- `ITER081T_SM_INVALID` for incomplete corpus, provenance mismatch, parser failure, missing Iter081R target lock, or control failure.

## Controls

1. SHA256 of both frozen candidate files must be recorded.
2. Census must enumerate every nonempty prose/equation block, not keyword-hit snippets only.
3. A positive synthetic control containing 28 explicit independent coefficient normalizations must qualify.
4. A negative synthetic control containing only the phrases `causal composition + RG stability + gauge recovery` must not qualify.
5. No scientific criterion may be altered after production output is observed.

## Claim locks

Even a positive result would not prove physical correctness of the selector, generic-spin uniqueness, E3/E4/E6 composition, regulator independence, RG completion, G3 PASS, NEW_PHYSICS_FOUND, or complete quantum gravity. A blocked result says only that CRQN v0.1/v0.2 did not already contain the required corrected selector.
