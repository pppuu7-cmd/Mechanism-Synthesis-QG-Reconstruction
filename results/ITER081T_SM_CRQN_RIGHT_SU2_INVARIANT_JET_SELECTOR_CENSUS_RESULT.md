# Iter081T-SM — CRQN v0.1/v0.2 corrected invariant-jet selector census

## Provenance

- prereg: `ae61cee9f8c553c72bd96a5cf7647c7d2d4d505c`
- implementation: `0105f76b98cfa2f77b38b9874aa18b0078737809`
- production workflow: `ae79da736984419e1c3e96edd47230df07d12039`
- Actions run: `34883851361`, terminal `success`
- artifact: `10364396425` (`iter081t-sm-aggregate`)
- artifact ZIP digest: `sha256:336c225db60ecdef3b2162c9d054083a94c4efcdb26c8993b6f052aac8df7ce2`
- downloaded aggregate JSON SHA256: `d3d954e913db6db4c51f5b4d4c134ae5f4e20bb6868a803e2d86b0f34c2e9f48`

## Frozen classification

`ITER081T_SM_CRQN_V0_1_V0_2_HAS_NO_PREEXISTING_CORRECTED_INVARIANT_JET_SELECTOR_BLOCKED_EXACT_CENSUS_SCOPED`

Verdict: **`BLOCKED_EXISTING_CANDIDATE_SELECTOR_MISSING`**.

## Exact census outcome

Frozen corpus:

1. `candidates/CANDIDATE_A_CRQN.md`
   - SHA256 `600e24ec5b363a092dbf7d4b726a1678d8c3ff9b9aa6d9ee55dbe5be8ffdaf1c`
   - 77 exhaustive nonempty blocks.
2. `candidates/CANDIDATE_A_CRQN_V0_2.md`
   - SHA256 `beb7255f88d8f7b6b432603c9514567f03e498d22327ad2c2f72bb286f93490f`
   - 29 exhaustive nonempty blocks.

Total exhaustive corpus blocks: **106**.
Qualifying pre-existing selectors satisfying frozen Q1-Q6: **0**.

Controls:

- synthetic positive control with 28 explicit independent coefficient normalizations: PASS;
- synthetic negative control containing only `causal composition + RG stability + continuum gauge recovery`: correctly rejected;
- Iter081R corrected target lock present in `status/CURRENT.md`;
- no invalid/provenance reasons.

## Scientific interpretation

The pre-existing CRQN v0.1/v0.2 corpus does contain architectural requirements such as causal composition, gauge/refoliation recovery, RG closure and a placeholder finite relation `Phi(...) = 0`. It does **not** already contain an explicit mathematical selector that acts on the corrected source-compatible K5 ambiguity target established by Iter081R: the demonstrated 28-dimensional scalar `SO(3) x S5` invariant normal-jet coefficient subspace through order 8.

In particular, the corpus supplies neither:

- 28 independent scalar equations/normalizations with demonstrated full rank on the Iter081R scalar basis; nor
- a function-valued/differential/spectral/boundary-value rule with a uniqueness proof covering that basis; nor
- an equivalent source-ordered rule demonstrably fixing those coefficients while respecting node-wise right-SU(2), S5 and boundary covariance.

Therefore the corrected local blocker is **not secretly solved by pre-existing CRQN v0.1/v0.2 axioms**. A successor selector, if proposed, must be new, independently motivated and prospectively frozen; it cannot be represented as an already-present v0.2 rule.

## Scope / claim locks

This is a candidate-corpus census only. It does not prove that no physically motivated 28-direction selector exists, that 28 conditions suffice for the full representation-valued extension problem, or that the full extension space has dimension exactly 28. It does not promote G3/F9/G8/K5, regulator independence, RG completion, NEW_PHYSICS_FOUND or complete quantum gravity.
