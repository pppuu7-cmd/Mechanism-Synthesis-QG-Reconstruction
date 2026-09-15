# Control-only repair 2 — repaired K4 parity Critic evidence matcher

Date: 2026-09-15
Status: PROSPECTIVELY FROZEN BEFORE REPAIR-2 IMPLEMENTATION

Parent scientific contract: `prereg/ACTUAL_MULTIVARIATE_K4_ORDER3_PARITY_INDEPENDENT_CRITIC_REVIEW.md`.
Control-only repair 1: `prereg/ACTUAL_MULTIVARIATE_K4_ORDER3_PARITY_CRITIC_CONTROL_ONLY_REPAIR_1.md`, commit `f24290d18a246d8ba1c6938e04d66b8769a8bd8e`.
Repair-1 implementation/workflow: commits `5b8f6d09a49bad6454e08eeb0c03a915f429f36a` and `1643a3a89403acf764cd8277fe41233f85987f1f`.
Repair-1 run `35011898749` produced `INVALID_PROVENANCE`/failure after the independently recomputed scientific geometry/source/full-contraction/S5 checks had passed.

## Implementation-only defects exposed by repair-1 production

1. The 12-slot order-3 partition computation was gated by one brittle literal comment-string anchor in the Researcher implementation. The actual authoritative Researcher aggregate already records the complete order-3 partition count and the source decomposition is independently derivable as 6 internal Toller factors + 4 external Toller factors + Haar + the smooth joint q-family factor. The repair must derive the slot census structurally and use the Researcher aggregate only as a cross-check, not require an exact comment phrase.

2. Provenance incorrectly required every historical invalid Researcher run ID to remain literally listed in the current `status/CURRENT.md`. Durable provenance is the authoritative aggregate/result ledger plus git ancestry; later status compaction may omit old invalid IDs. Repair-2 must verify the authoritative aggregate values and quarantine metadata there, plus ancestry of the Researcher preregistration/head, without treating a status-summary wording omission as invalid provenance.

## Frozen repair-2 obligations

- Scientific K4 acceptance criteria, parity statement, residue/scheme interpretation and terminal taxonomy remain unchanged.
- Recompute exact geometry, source leading parity, 5-block/32-component/500000-term census, S5 transport, scaling degree and `omega_K4=3` exactly as repair 1.
- Derive `jet_slots=12` from the actual structural census `6+4+1+1`, enumerate all 364 weak order-3 partitions, and retain the regrouping robustness control.
- Verify Researcher run/head/artifact/ZIP/production-JSON metadata from the authoritative durable aggregate and git ancestry; historical invalid runs must be quarantined by that durable aggregate, not by an optional CURRENT prose string.
- Retain byte locks to the independently confirmed cubic bridge.
- All malformed controls from repair 1 remain required.

No outcome-dependent K4 or K5 criterion changes are permitted.