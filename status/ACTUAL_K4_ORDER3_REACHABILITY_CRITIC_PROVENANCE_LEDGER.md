# K4 order-3 reachability independent Critic provenance ledger

Date: 2026-09-15

## Researcher authority reviewed

- scientific preregistration: `prereg/ACTUAL_MULTIVARIATE_K4_ORDER3_OBJECT_DEFINITION_REACHABILITY.md`, commit `a6983a4d7379bf73f48752a4de357450996d8572`;
- authoritative Researcher head: `0bcd68093ab19afb1d6643c3c876b4f0c2e261c4`;
- run `34964010302`, job `104364057703`, success;
- artifact `10394990199`, ZIP digest `sha256:22cc7680b651802c96f5ce4ca0de8d358df6d790f6b61deccf198510d01c6c47`;
- production JSON SHA256 `60a4787f73d1b0908222ba85ae11eb3f55434465f1d1d5dcc386a090ec22957c`;
- classification `ACTUAL_K4_ORDER3_SOURCE_COEFFICIENT_OBJECT_DEFINITION_BLOCKED_SCOPED` / `BLOCKED_OBJECT_DEFINITION`.

## Independent Critic freeze

- Critic preregistration: `prereg/ACTUAL_MULTIVARIATE_K4_ORDER3_OBJECT_DEFINITION_REACHABILITY_INDEPENDENT_CRITIC_REVIEW.md`;
- prereg commit `8a1dd0cb57c9d895ebf1b2a56bf04af7d4428194`;
- Critic implementation commit `6a80f0becc39de5a4a51d8d019389dcaafc5df10`.

## Historical invalid Critic attempt

Run `34971934034`, head `d308cf543b8bd1b6c6dae51aef743b6e5d44f0b6`, job `104390056615`, terminal failure.

Classification: `K4_ORDER3_REACHABILITY_CRITIC_INVALID_PROVENANCE`.

Cause: the durable Researcher raw JSON had been reserialized after production, so its byte SHA256 was `d89153fcfd54d7b2498ff4e3581170392f53de99f52473d4888393708d4e6bbe` rather than the authoritative production digest `60a4787...`. No scientific verdict is taken from this run.

## Prospectively frozen control-only provenance repair

- repair preregistration commit `927b5f489c85a116936d8b208df618f3befa4cba`;
- exact authoritative production bytes restored in `results/raw/actual_k4_order3_source_object_reachability.json`, commit `4b4f6504f5474ce7e49fe8c9ad28c37f45e513b4`;
- Critic workflow trigger extended to react to the repaired durable raw file, commit `43fd33507b1360f48bbbb31453411ba713f96c6b`;
- Critic scientific script/criteria unchanged.

## Authoritative Critic production

Run `34975020879`, head `43fd33507b1360f48bbbb31453411ba713f96c6b`, terminal success.

- job `104400456761`, success;
- artifact `10399550019`, `critic-k4-order3-reachability`;
- artifact ZIP digest `sha256:04472e48edcf2ce393459db998a5fe855408d9723cf31e4f3ed5b8b5c09a9964`;
- Critic JSON SHA256 `7638d51595372a4df9420db42a67761be13eecc97fa947d60316c9703f481345`;
- durable raw `results/raw/critic_k4_order3_reachability.json`;
- durable review `results/ACTUAL_K4_ORDER3_SOURCE_OBJECT_REACHABILITY_CRITIC_RESULT.md`.

## Terminal Critic result

`K4_ORDER3_REACHABILITY_CRITIC_CONFIRMED_BLOCKED_OBJECT_DEFINITION_SCOPED`.

The independent Critic confirms that the complete all-32 K4 normal-order-3 coefficient is not yet source-faithfully extractable from current authority.

It independently retains positive authority for R7 full-32 contraction, R9 branch/source normalization and R10 S5 transport. Its conservative repository scan additionally finds constructive evidence for R1 chart material, R2 BCH material, R5 Haar/Jacobian material and R8 front/pairing material, but still finds no complete mutually compatible cubic source realization for the decisive missing subset:

- `R3_TOLLER_ORDER3`;
- `R4_EXTERNAL_TOLLER_JETS`;
- `R6_Q_DEFINING_FUNCTION_ORDER3`.

Thus the next Researcher construction must target these source-faithful cubic jets/cross-couplings in a single compatible realization before any K4 zero/nonzero or annihilator computation.

## Claim ceiling

No K4 zero/nonzero theorem, no K5 order-8 inference, no finite-part selector, no regulator-independence theorem, no causal-vertex finiteness/divergence theorem, no G3/F9/G8/K5 promotion, no `NEW_PHYSICS_FOUND`, and no complete-QG claim follows.
