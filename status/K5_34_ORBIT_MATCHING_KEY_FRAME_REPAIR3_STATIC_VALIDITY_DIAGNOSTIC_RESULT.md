# K5 matching-key repair3 static validity diagnostic — terminal

Date: 2026-09-19

Diagnostic run `35414672193`, job `105820825500`, head `43f4d7e8bdde7c32b8a991758e7f14d0763bdba9`, completed successfully. Artifact `10574968155`, ZIP SHA256 `ec94627c6a35d0cc655ff3b060918ecb9d1b36356211990a595f6fd40d45fc66`.

The diagnostic had no scientific verdict and only serialized the already-frozen repaired-core `static_checks()` map.

After excluding the intentionally false data/firewall fields `q18_values_used=false` and `N_B_orders_or_coefficients_used=false`, the remaining false static predicates are exactly:

- `label_frame_critic_raw_blob_locked=false`;
- `label_frame_critic_run_locked=false`;
- `label_frame_critic_N_B_unused=false`.

All inherited parent static controls, all matching-key census/relations, formal Boundary-S5 controls, source coverage, mask511/projective-normal locks, exact arithmetic controls and table hashes are true.

## Root cause

The repair3 core defines dedicated G8 Critic authority globals before importing/re-exporting the repair1 core. It then performs a broad inherited-surface loop:

`for _name in dir(repair1): globals()[_name] = getattr(repair1, _name)`.

That loop overwrites generic names such as `CRITIC_AUTH`, `CRITIC_RUN` and `CRITIC_CLASS` with the repair1/Boundary-S5 authority globals. Consequently the later repair3 static checks accidentally read the already-confirmed Boundary-S5 Critic JSON instead of the G8 matching-label Critic JSON. This explains all three remaining false predicates simultaneously:

- the G8 raw-blob lock is tested against the Boundary-S5 authority file;
- the G8 run is tested with the overwritten Boundary-S5 run constant;
- the Boundary-S5 JSON has no G8 `N_B_orders_or_coefficients_used` datum.

This is a namespace/provenance binding defect only. It does not alter the already-terminal exact all-945 target-key relation or repaired G8 H7 result.

No q18 or N/B payload was consumed; no heavy resolver was launched. Resolver scientific authority remains `0/64`.
