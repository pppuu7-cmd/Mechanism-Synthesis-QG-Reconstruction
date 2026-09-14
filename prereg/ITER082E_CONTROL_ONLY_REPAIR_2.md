# Iter082E control-only repair 2

Status: **PROSPECTIVELY FROZEN BEFORE REPAIR IMPLEMENTATION**
Date: 2026-09-14

Parent scientific preregistration commit: `15105f6326f652db44809336579060a46403ca8d`.
Repair-1 preregistration commit: `eab36d2b70b911a54440f05f43eb0beb89fce571`.
Repair-1 implementation commit: `bf5bae441a6e9d37c7e96b68355a56a7a0c8d32b`.
Repair-1 run: `34896145784`, artifact `10368621471`.

## Observed control defect

The repaired production artifact mechanically passed parent P0–P5, including exact inverse series, actual block-diagonal tests, 420 diagonal-ideal generator checks, 78 ideal-power checks, 120 nested-chain generator checks, 8800 nested-order checks, 234 tangent-normal basis checks, and 120 positive S5 permutations.

However P6 failed only because the *negative* label-dependent cubic control was implemented incorrectly: its node-dependent coefficient was permuted together with the node data. That construction transports the preferred-label defect covariantly and therefore is not the preregistered malformed chart with a coefficient fixed to one absolute label.

This is an implementation/control failure, not a scientific failure of the frozen chart-overlap gate.

## Frozen repair

Change only the S5 negative-control evaluator:

- positive chart: one common cubic coefficient at all labels, unchanged;
- malformed control: coefficient 2 is tied permanently to absolute label 0 and coefficient 1 to labels 1–4;
- under an input label permutation, the malformed coefficient array remains tied to output labels `[0,1,2,3,4]` and is **not** permuted with the data;
- compare `bad_chart(P x)` with `P bad_chart(x)` using the same exact rational node samples and all 120 permutations;
- the frozen control passes only if at least one permutation is rejected (identity may pass).

No parent scientific predicate, chart formula, order bound `(0,3,8)`, PASS/FAIL label, or claim ceiling may change. No other production logic may be altered except what is strictly necessary to correct this negative-control wiring.
