# K5 degree-4 annihilator projective constant-2x2 closure — provenance/front ledger

Date: 2026-09-16

## STATE_READ

Controlling pre-gate state: `status/CURRENT.md` at blob `d0cb5df161a6335d673165b4986114172fbc8679`, which records independent Critic verdict `REQUIRES_NEW_PREREGISTERED_GATE` for the historical raw `B=M N` closure test and authorizes a corrected projective `P=B/s1^4` closure gate.

MSQGR Adversarial Critic automation is enabled; MSQGR Researcher automation is paused. This ledger records the manual Researcher execution performed after reading that auto-research state.

## TARGET_GATE

`K5_DEG4_ANNIHILATOR_PROJECTIVE_CONSTANT2X2_CLOSURE`

Exact object:

`P_v[N](alpha)=B_v[N](alpha)/s1(alpha)^4`, `deg P=deg N=27`.

Scientific question: whether the two full-all-32 invariant-dual projective channels close through one constant rational `2x2` matrix on the four prospectively frozen representatives inherited from the parent action gate.

## PREREG

`prereg/K5_DEG4_ANNIHILATOR_PROJECTIVE_CONSTANT2X2_CLOSURE.md`, commit `4f1e49f9d850fa7834dd189228d0787f84406f84`.

Frozen before inspecting projective fit/validation outcome.

## INPUT_PROVENANCE

Parent repaired action production:

- run `35130545821`;
- job `104910177408`;
- artifact `10461780450`;
- artifact ZIP digest `sha256:d1b2bbd109aa0a3969e37e97aa3e572fc4cba368c42fdc145f94689afbc032dd`;
- production JSON SHA256 `909b2afc8474b317a424ba59f108756441bdd8cdf8888cb85763d6c368fe95b8`;
- implementation head `4e70e991ff0c5e312feac4556082e9be01afe598`;
- full all-32 / `100000` source terms;
- invariant-dual projection retained.

Artifact exact point values were extracted after preregistration and persisted in

`sources/raw/k5_deg4_projective_closure_parent_point_lock.json`, commit `14b7926ada4e4dab64c542bbd7b243035f362ff4`.

## IMPLEMENTATION

Validator:

`scripts/k5_deg4_projective_constant2x2_closure.py`, commit `63538524d53aa0888effb9a5741572a9dc86150f`.

Workflow/head:

`.github/workflows/k5_deg4_projective_constant2x2_closure.yml`, head `d508fd145973a2ad4a8772368e00c5e599c5f908`.

## PRODUCTION

- run `35140030858`, terminal success;
- job `104941953222`, terminal success;
- artifact `10464124390`;
- artifact ZIP digest `sha256:cbe6f218de38f816b30637e48198edf6f4c72a8ffdc3b18931e0f0f733ccf92d`;
- production JSON SHA256 `d9a86723b7baa5e947e0d21998d7468b61b5e26e90fce272bd8db07d677c05b4`.

All frozen checks and controls passed.

## RESULT

`K5_PROJECTIVE_CONSTANT2X2_CLOSURE_FALSIFIED_EXACT_SCOPED`.

Fit determinant is exact nonzero:

`29427625893405583852377851198976000000000000`.

The unique fit matrix gives exact zero residuals on `fit_A` and `fit_B` and four exact nonzero residual components on the two prospectively frozen validation representatives `validation_U` and `validation_G`.

Exact scale controls verify under `alpha -> 2 alpha`:

- `N -> 2^27 N`;
- `B -> 2^31 B`;
- `P=B/s1^4 -> 2^27 P`;
- each closure residual -> `2^27` times itself.

Hence failure is projectively well-defined and is not the historical raw grading mismatch.

Durable scientific result:

`results/K5_DEG4_ANNIHILATOR_PROJECTIVE_CONSTANT2X2_CLOSURE_RESULT.md`, commit `5fc64e1bf971923e7a85f42bc21e72a89af31512`.

## FRONT_CHANGE

Replace the stale survival-chain item

`projective degree-27 P=B/s1^4 closure ?`

with

`projective degree-27 constant-2x2 closure FALSIFIED_EXACT_SCOPED (Researcher; pending independent Critic review)`.

The historical raw `B=M N` failure remains non-authoritative for physical projective closure; this new gate is its prospectively corrected successor.

## CLAIM_CEILING

This excludes only one constant rational two-channel projective closure ansatz. It does not establish failure of polynomial/rational coefficient-module closure, does not provide a global Stokes identity or integrated K5 period, and does not affect the `dim_C F_8=377` selector freedom.

No finite-part selector, regulator independence, F9/G3/G8 promotion, `NEW_PHYSICS_FOUND`, or complete-QG claim.

## NEXT_RECOMMENDED_GATE

First allow the enabled independent MSQGR Critic to attack this corrected projective-closure result.

If confirmed/qualified without invalidating the object, the next algebraic high-information gate should prospectively define the **minimal degree-consistent polynomial/rational coefficient module** for the two projective channels rather than retry another constant matrix.

The independent Stokes route remains gated by corrected projective-tangent flux/corner authority and must not be conflated with pointwise algebraic closure.
