# Boundary-S5 independent Critic — repair2 authority reconciliation

Date: 2026-09-18
Status: **PRE-RESULT PROVENANCE; NO SCIENTIFIC VERDICT**

## Controlling authority

Current repository authority predates and supersedes the redundant local classifier-repair attempt created on 2026-09-18:

- parent Critic scientific contract: `cf8576acb7237b751c26d5b5942aa60874bcd00e`;
- frozen classifier/execution repair1: `2d510ae4ef0dab2e15a763a520864869eff2d71b`;
- frozen classifier repair2 q18-boolean semantics: `1440e07b8a3d6295020cba50d0ac73f44d4be641`;
- frozen independent base implementation: commit `64a4f4935d0238d67e2d60e0b202f81f1195330a`, blob `948f32653872e0920b4450d60d56d48a2a0cc24d`;
- classifier wrapper: `scripts/critic_k5_full_source_boundary_s5_classifier_repair.py`, current blob `a6922bc72459132ab92e559b6213d4c863e8266a`.

The repository repair2 contract requires the independent base implementation to remain byte-for-byte at the frozen blob while classifier separation is applied externally by the wrapper.

## Non-authoritative accidental run

Commit `60b09d346dc8ec261dd366a2da000db98b022c27` modified the frozen base file before this older repair2 authority was recovered. Workflow run `35364197119` was triggered from that commit.

Because repair2 requires base blob `948f32653872e0920b4450d60d56d48a2a0cc24d`, that run is provenance-invalid for scientific authority regardless of its eventual output. No substantive value from that run has been read or used.

The redundant prereg `5576f1d8453dfec541767697304978082e14b4d5` is retained only as provenance and does not supersede repair2.

## Restored frozen base

Commit `e4448943e776621b97287881bc6d19ee3bebb040` restores the independent base script exactly to blob

`948f32653872e0920b4450d60d56d48a2a0cc24d`.

The next workflow execution triggered from the restored file is the only admissible scientific execution in this session, subject to terminal run/job/artifact validation.

## Scientific classifier separation

Repair2 remains controlling:

A. implementation/provenance validity excludes substantive theorem truth and includes locked source/hash/coverage/exact-arithmetic machinery, all-120 generation machinery, 945-matching completeness, malformed controls, and forbidden-method absence with `q18_values_used=false` checked separately.

B. substantive theorem conditions include C/T source-boundary contragredient identities, C/T covariance transport, complete-Wick orientation cancellation, inverse/roundtrip consistency, and exact representation/edge composition sufficient for all 120 S5 elements.

With A valid:
- all B true => `CONFIRMED_EXACT_SCOPED`;
- any B false with sufficient exact machine-readable witness => `REFUTED_EXACT_SCOPED`;
- missing primitive => `BLOCKED`;
- implementation/control/provenance defect => `INVALID_IMPLEMENTATION`.

The frozen scientific classification field is terminal authority.

## q18 firewall

No q18 partial value from run `35259123078` has been inspected or consumed. No competing q18 verdict is created.

## Interpretation ceiling

Even a confirmed result is limited to coefficient-level full-source Boundary-S5 transport for the frozen complete unprojected order-zero all-`j=1/2` object. It does not establish q18, all-orbit cancellation, K5 integrability, global Stokes/IBP, periods, physical finite-part selection, regulator independence, downstream CRQN promotion, new physics, or complete quantum gravity.
