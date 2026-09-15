# K3 polar parity gate — control-only repair 1

Date: 2026-09-15
Status: **PROSPECTIVELY FROZEN BEFORE VALIDATOR REPAIR**

Parent gate preregistration: `prereg/ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR.md`, commit `4c4478db20e08387fb7067a55d773fce31d3fc34`.
K3 theorem derivation: `sources/ACTUAL_MULTIVARIATE_POLAR_K3_PARITY_DERIVATION.md`, commit `78e63844a8fe0a70af9ac8dc574d358e7ecab927`.
Initial validator: `scripts/actual_multivariate_polar_k3_parity_gate.py`, commit `c8ddedab0530cb08b17aea08299c1e45a1897d30`.
Initial workflow/head: `7f15c4f4188990f2bd7b0c08329fb46345da43cd`.
Initial run: `34955091523`, job `104335105619`.

## Defect

The initial production executed the complete scientific validator and returned all K3 predicates `K3_1..K3_13=true`, all ten malformed controls `true`, exact full-32 execution, three internal / seven external edge census, K2 front exponent `0`, and 20 maximal K3-K4-K5 chains.

It classified `INVALID_IMPLEMENTATION` solely because a provenance substring check against the repaired bridge result required the exact literal

`full 32-component boundary contraction`

while the durable repaired bridge records the same scientific fact with different wording.

No mathematical predicate or control failed.

## Frozen repair scope

The repair may alter only that provenance text needle to an exact phrase already present in the authoritative repaired bridge result. It must not alter:

- the K3 parity theorem;
- any K3_1..K3_13 scientific predicate;
- any malformed negative control;
- edge/block/chain counts;
- exact leading-matrix oddness checks;
- full-32 execution;
- K2 integrability criterion;
- PASS/FAIL/INVALID taxonomy;
- interpretation ceiling or K4/K5 non-overreach.

Fresh terminal production is required before scientific promotion.