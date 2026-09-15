# Independent Critic — K4 order-3 source-object reachability

Date: 2026-09-15

Status: **CONFIRMED BLOCKED OBJECT DEFINITION, SCOPED**

## Authority reviewed

Researcher production run `34964010302`, job `104364057703`, artifact `10394990199`, artifact ZIP digest `sha256:22cc7680b651802c96f5ce4ca0de8d358df6d790f6b61deccf198510d01c6c47`, production JSON SHA256 `60a4787f73d1b0908222ba85ae11eb3f55434465f1d1d5dcc386a090ec22957c`.

Researcher classification reviewed:

`ACTUAL_K4_ORDER3_SOURCE_COEFFICIENT_OBJECT_DEFINITION_BLOCKED_SCOPED` / `BLOCKED_OBJECT_DEFINITION`.

Independent Critic preregistration:

`prereg/ACTUAL_MULTIVARIATE_K4_ORDER3_OBJECT_DEFINITION_REACHABILITY_INDEPENDENT_CRITIC_REVIEW.md`, commit `8a1dd0cb57c9d895ebf1b2a56bf04af7d4428194`.

Critic implementation commit: `6a80f0becc39de5a4a51d8d019389dcaafc5df10`.

## Historical invalid attempt

Critic run `34971934034` on head `d308cf543b8bd1b6c6dae51aef743b6e5d44f0b6` terminated failure with `K4_ORDER3_REACHABILITY_CRITIC_INVALID_PROVENANCE` because the durable Researcher raw JSON had been reserialized and no longer had the exact production byte hash. No scientific conclusion is taken from that run.

Control-only provenance repair was prospectively frozen at commit `927b5f489c85a116936d8b208df618f3befa4cba`; exact production bytes were restored at `4b4f6504f5474ce7e49fe8c9ad28c37f45e513b4`; the workflow trigger was extended without changing Critic scientific logic at `43fd33507b1360f48bbbb31453411ba713f96c6b`.

## Authoritative Critic production

Run `34975020879` on head `43fd33507b1360f48bbbb31453411ba713f96c6b` completed success.

- job `104400456761`, success;
- artifact `10399550019`, `critic-k4-order3-reachability`;
- artifact ZIP digest `sha256:04472e48edcf2ce393459db998a5fe855408d9723cf31e4f3ed5b8b5c09a9964`;
- Critic JSON SHA256 `7638d51595372a4df9420db42a67761be13eecc97fa947d60316c9703f481345`;
- provenance valid: restored Researcher JSON hash exactly matched `60a4787...`;
- synthetic complete fixture accepted;
- all 12 malformed controls rejected by the same validator.

## Independent result

The Critic independently found retained positive authority for:

- `R7_FULL32_CONTRACTION_MAP`;
- `R9_BRANCH_NORMALIZATION` including published spectral `i epsilon`;
- `R10_S5_TRANSPORT`.

Its conservative corpus scan found constructive evidence for R1, R2, R5 and R8 in pre-existing files, but did **not** find complete source-faithful cubic constructions for:

- `R3_TOLLER_ORDER3`;
- `R4_EXTERNAL_TOLLER_JETS`;
- `R6_Q_DEFINING_FUNCTION_ORDER3`.

Therefore the complete all-32 K4 simple-pole coefficient at total K4 normal order 3 remains not explicitly extractable from current authority without adding unverified cubic source data.

## Verdict

`K4_ORDER3_REACHABILITY_CRITIC_CONFIRMED_BLOCKED_OBJECT_DEFINITION_SCOPED`.

The Researcher object-definition blocker is independently confirmed.

## Interpretation ceiling

This is not a theorem that the abstract K4 polar distribution does not exist. It does not classify the K4 coefficient as zero or nonzero, does not establish physical divergence or finiteness, does not choose a finite part, and does not imply regulator dependence or independence.

The next admissible Researcher work is a prospectively frozen `K4_ORDER3_SOURCE_FAITHFUL_CUBIC_REALIZATION_BRIDGE` targeting the missing source-faithful cubic Toller/internal-external jets and nested `q_B` cubic pullback/cross-couplings while retaining the already authoritative full-32 contraction, branch normalization, S5 action, original Haar structure and multivariate regulator family.
