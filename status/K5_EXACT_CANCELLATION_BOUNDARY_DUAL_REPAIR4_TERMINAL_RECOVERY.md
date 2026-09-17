# K5 exact-cancellation boundary-dual diagnostic — repair-4 terminal recovery

Date: 2026-09-17

This note is controlling where newer than `status/K5_EXACT_CANCELLATION_S5_RECOVERY_20260917.md` and `status/CURRENT.md`. It records only terminal GitHub/Actions authority and does not alter any scientific claim ceiling.

## Recovered authority

Parent scientific gate remains prospectively frozen at `d6b0e805101c8590eafac71398cc2b1466691752`, `K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION`.

Parent boundary-dual diagnostic remains prospectively frozen at `41f26f8e314f4ab1213fe6a681b69d2c87e00d68`.

Execution repair 4 preregistration is `06049f0a575a07d1e35afcea143fbb800101071e`; repair-4 shard implementation commit `29d14e6b5b4fa907c43cf543eedc6fa6e2a4c698`; aggregate implementation commit `57ddff47d55086065fc752693ce11b565c5127b1`; workflow/head `46f2b46d827758c42c24df8afd23a8fb6e617ad6`.

## Terminal Actions authority

Repair-4 production run `35189938242` is terminal `completed`, conclusion `failure`.

Jobs:

- `105100069213`, `shard (W1_base)`: terminal `failure`;
- `105100069238`, `shard (W2_inverse)`: terminal `failure`;
- `105100068986`, `shard (W1_inverse)`: terminal `cancelled` at the job budget;
- `105100069152`, `shard (W1_cycle)`: terminal `cancelled` at the job budget;
- `105100069203`, `shard (W2_cycle)`: terminal `cancelled` at the job budget;
- `105100069267`, `shard (W2_base)`: terminal `cancelled` at the job budget;
- aggregate job `105111060239`: `skipped` because required shards were not successful.

Run `35189938242` produced no Actions artifacts. There is no aggregate result JSON, classifier, artifact ID, artifact digest, or substantive boundary-vector authority from repair 4.

## Exact implementation failure

The completed `W1_base` log proves a control/execution failure before any shard payload was written. The workflow correctly invoked

`python scripts/k5_exact_cancellation_unprojected_boundary_dual_s5_shard_repair4.py --label W1_base --output ...`

but the repair-4 shard imported the parent diagnostic before reaching its own parser. The parent diagnostic imports `scripts/k5_deg4_annihilator_actual_dual_action.py`. That historical action script has an unguarded production block beginning at `results={};checks={}` and an unguarded terminal `argparse` accepting only `--output`. Therefore the import executes unrelated pointwise-action production and ultimately rejects the shard argument:

`error: unrecognized arguments: --label W1_base`.

The historical action production suffix is unrelated to the frozen boundary-dual diagnostic and must never execute as an import dependency. This explains both the long per-shard runtime before failure and the CLI mismatch.

Classification of repair 4: **`INVALID_IMPLEMENTATION`**. This is not a scientific K5, S5, boundary-dual, corner, integrability, period, or finite-part result.

No partial substantive values from any repair-4 job are authority.

## Prospective repair 5 already frozen without repair-4 substantive output

Before repair 4 terminalized, only after the completed `W1_base` implementation-failure log and static source audit, an outcome-independent control-only repair was prospectively frozen:

- repair-5 preregistration commit `f472eb29ded6a04ab1ae8a5f367d378f64beee4f`;
- import-safe shard implementation commit `f6fb4e6d2c747d6b6a704982347d81ba324a50d7`;
- import-safe aggregate implementation commit `5a7359d8b4124f24ed5f5e4b59f6990c7e9b598d`.

Repair 5 keeps the exact same six alpha tuples, all 32 boundary components, all 100000 source terms, four frozen representation laws, `P^T` pivot-coordinate authority, exact arithmetic and parent classifier. The sole execution change is that it verifies the frozen action-source blob and executes only the source prefix before the unique historical marker `results={};checks={}`. The historical action production/CLI suffix is excluded and a negative control rejects its inclusion.

Repair 5 must not be launched until repair 4 is terminal. That condition is now satisfied.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no physical-corner classification from the invalid run; no global Stokes/IBP theorem; no invariant-dual period theorem; no reduction of `dim_C F_8=377`; no unique physical finite part; no regulator-independence theorem; no G3/F9/G8/K5 promotion. Historical Iter077E/F remain quarantined; Iter077I authority remains corrected run `34786586785`; retain published spectral `i epsilon`.
