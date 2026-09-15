# Control-only repair 3 — K4 parity Critic duplicate-evidence consistency

Date: 2026-09-15
Status: PROSPECTIVELY FROZEN BEFORE REPAIR-3 IMPLEMENTATION

Parent Critic contract and scientific criteria remain unchanged.
Repair-2 run `35012028134` returned `scientific_ok=true`, `provenance_ok=true`, exact 364 partitions, exact 500000-term full-source census and zero S5 failures, but correctly withheld confirmation because one malformed control was not rejected.

The sole unrejected control was `internal_factor_degree_zero`. The mutation changed the independently recomputed `source_degree.baseline_degree` from six to five while leaving the derived/cached `scaling.baseline_degree` at six. The validator checked the latter but did not require the two evidence paths to agree.

## Frozen repair

Add an explicit consistency requirement that the independently recomputed source baseline degree and the scaling-summary baseline degree agree and equal six. No scientific target, parity theorem, geometry, partition count, provenance rule, source convention, residue statement or interpretation ceiling changes.

All fourteen malformed controls remain required, including `internal_factor_degree_zero`; the repaired same-path validator must reject all of them.
