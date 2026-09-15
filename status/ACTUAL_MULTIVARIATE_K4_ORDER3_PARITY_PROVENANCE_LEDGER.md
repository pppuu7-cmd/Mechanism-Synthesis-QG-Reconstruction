# Provenance ledger — actual multivariate K4 order-3 parity gate

Date: 2026-09-15

## Scientific preregistration

- `prereg/ACTUAL_MULTIVARIATE_K4_ORDER3_PARITY_GATE.md`
- commit `4f306f3eda9d5ff71a77580c9c192eb7b8a323d0`
- frozen before K4 coefficient computation.

## Upstream independent authority

K4 cubic-realization bridge Critic confirmation:

- run `34993531171`, success;
- job `104463943299`, success;
- artifact `10406716330`;
- ZIP digest `sha256:6ef541cf9190907ac776099d08a16ea3a542167afe05b11d209b9e4e0d35c736`;
- durable result commit `105d94ca6af870c11d009b65efb15a9f701ee060`;
- classification `K4_CUBIC_REALIZATION_BRIDGE_CRITIC_CONFIRMED_SCOPED`.

Historical bridge-Critic runs `34985145895`, `34993299842`, `34993403191` are `INVALID_IMPLEMENTATION` only.

## K4 parity implementation history

Parent implementation/workflow were created only after preregistration.

Historical implementation-invalid K4 parity productions:

1. run `34993972013`: brittle upstream bridge-authority text anchors; no scientific verdict.
2. run `34994071337`: bridge matcher repaired, but brittle Critic-result text anchors left P0 false; no scientific verdict.
3. run `34994172757`: Markdown normalizer applied asymmetrically to haystack vs needles; no scientific verdict.
4. run `34994282499`: all P0-P8 true, but `execution_valid` was incorrectly computed with `all({'valid':True,'reasons':[]}.values())`, making an empty correct reasons list falsy; no scientific verdict.

Prospective control-only repairs:

- repair 1 commit `31d3f7b1bf64baf9931279d71cc7cf0c01ff07c6`;
- repair 2 commit `a595d20b47437904c7867825bf953d18ab215cb6`;
- repair 3 commit `b243dcda8b4e673cfbfc15be2a168940d7c223b8`;
- repair 4 commit `bfb8e95e37599a55aa58790f71b2b807987542ac`.

The scientific contract was unchanged across all repairs.

## Authoritative production

- implementation/head `cd57b6d0a9c7c48c17ffea7ac3c978e77107c95f`;
- run `34994467079`, terminal success;
- job `104467110732`, terminal success;
- artifact `10407455156`;
- artifact ZIP digest `sha256:1021b31937956cf2ff3e84c0a98bd8d3f2abac2ce021f087fd19e8cb39d40486`;
- production JSON SHA256 `dd93d6bfe0151a3f72b2dc3bcee3ac530108e5f7966f919021e165edd2981934`.

Authoritative production facts:

- classification `K4_ACTUAL_ORDER3_POLAR_COEFFICIENT_ZERO_EXACT_BY_FULL_NORMAL_INVERSION_PARITY_SCOPED`;
- verdict `PASS_EXACT_SCOPED`;
- execution valid;
- P0-P8 all true;
- `degree_partition_count=364`;
- `full32_raw_contraction_terms=500000`;
- `edge_census_failures=0`;
- 9D K4 normal Gram determinant `64`;
- all frozen malformed controls rejected.

## Durable records

- durable aggregate summary `results/raw/actual_multivariate_polar_k4_order3_parity_gate_authoritative.json`, commit `21963a99ea4f2b1071474092ddf3400758be2df6`;
- scientific result `results/ACTUAL_MULTIVARIATE_K4_ORDER3_PARITY_RESULT.md`, commit `7df3d4d2843d46459877a0196f6b904be895a94c`.

## Claim locks

No K5 order-8 result; no physical finite-part selector; no regulator-independence theorem; no full-K5 finiteness/uniqueness theorem; no F9/G3/G8/K5 promotion; no global patching theorem; no `NEW_PHYSICS_FOUND`; no complete-QG claim.

Iter077I provenance remains controlling: failed historical run `34786550378`; authoritative corrected source-order-lock run `34786586785` from alias head `102fc7268b732bead5dfcf6d61fe4479ae1d3030`. Historical Iter077E/F remain quarantined under `status/ITER077_CONTACT_FORMULA_ERRATUM.md`.
