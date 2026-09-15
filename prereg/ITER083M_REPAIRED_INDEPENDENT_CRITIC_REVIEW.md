# Iter083M repaired result — independent Critic review preregistration

## Status
Prospective Critic-only gate. This file is committed before any independent review implementation or production result is inspected.

## Parent authority
Controlling `status/CURRENT.md` requires independent Critic review of the terminal control-repaired Iter083M Researcher result before downstream promotion.

Repaired Researcher production is frozen as:
- production head `463ba012c4b3f8d465ab7df99995f5f40f3e7e44`
- run `34921183332`
- job `104229460141`
- artifact `10378026902`
- ZIP digest `sha256:06d6c560942a73bd78c31557f9fb3f4714a17b495857ed17071d271409700f11`
- production JSON SHA256 `6572765b7a760a7505d6dc1c23d9239d5ede80cd37e1174c171951635f26c3e2`
- raw copy commit `41a62c9b6d3f1728ff3c1bb927a7ff33ebd742a0`
- repaired result commit `6f886ce799a17cde6ad35c7686f4ea96396acb7e`
- provenance ledger commit `77dba76247c22de212b03ba731c2cde246bec676`

Historical original Iter083M remains `INVALID_IMPLEMENTATION`; this gate reviews only the repaired production and must not rehabilitate the historical run.

## Frozen review questions
P0. Verify all above provenance identifiers against repository/run/artifact data and verify preregistration preceded repair implementation/production.

P1. Verify the repair changed only malformed-control execution/wiring and did not alter the frozen scientific object, positive predicates, interpretation ceiling, or fit parameters after outcome inspection.

P2. Independently inspect all eight malformed controls and require that each is actually injected into the tested mathematical object and rejected by the same validator logic, not merely represented by an alias/boolean/string.

P3. Independently recompute the source small-boost tangent quadratic form used by the Researcher from the frozen source formulas/derivation and verify no auxiliary ten-edge Q is identified with the physical normal metric without proof.

P4. Independently reconstruct the barycentric nested K3/K4/K5 normal projectors and verify exact physical ranks `(6,3,3)` on all 20 maximal chains, including orthogonality/nesting identities used by the result.

P5. Verify permutation covariance over the complete frozen relabelling set and reject preferred-label or single-chain-only implementations.

P6. Verify that the conclusion is limited to a unique invariant tangent/tubular radial *quadratic basis* in the frozen scope. It must not imply an exact nonlinear global radius, finite-part selector, subtraction scale, unique distributional extension, regulator independence, global patching, or physical F9/G3 promotion.

P7. Verify no arbitrary fitted coefficient, counterterm, preferred sequential order, or replacement of the published spectral `i epsilon` was introduced.

## Frozen classifications
Return exactly one of:

- `ITER083M_REPAIRED_CRITIC_CONFIRMED_SCOPED` if P0-P7 all pass.
- `ITER083M_REPAIRED_CRITIC_SCIENTIFIC_FAIL_SCOPED` if provenance/implementation are valid but an independently recomputed scientific predicate fails.
- `ITER083M_REPAIRED_CRITIC_INVALID_IMPLEMENTATION` if the repair or review object does not actually implement the frozen tests.
- `ITER083M_REPAIRED_CRITIC_INVALID_PROVENANCE` if the frozen authority/provenance chain is false or incomplete.
- `ITER083M_REPAIRED_CRITIC_BLOCKED` only if a required source/object cannot be obtained without adding a new assumption.

Infrastructure/numerical execution failure is not a scientific classification and must be repaired/retried without changing P0-P7.

## Dependency firewall
Iter083N must not be retried and Iter083O must not be promoted until this Critic gate is terminal `CONFIRMED_SCOPED`. No downstream scientific gate may consume repaired Iter083M before then.

## Claim locks
No `NEW_PHYSICS_FOUND`; no complete-QG claim; no unique physical K5 extension; no source-authorized finite-part selector; no physical regulator-independence/dependence theorem; no G3 PASS; no F9/G8/K5 promotion.