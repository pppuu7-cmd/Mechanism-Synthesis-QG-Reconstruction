# Provenance ledger — independent Critic review of K5 edge01/edge02 rank-two lane

Date: 2026-09-16
Role: AUTOMATION B / MSQGR Adversarial Critic-Verifier

## Researcher authority reviewed

Prospective Researcher preregistration:
- `prereg/K5_ORDER8_EDGE01_EDGE02_RANKTWO_POSITIVITY_LANE.md`
- commit `ef26d063354d0def5af3fdba4fe0d8b537a038d1`

Post-prereg derivation:
- `sources/K5_ORDER8_EDGE01_EDGE02_RANKTWO_SIGN_CHANGE_DERIVATION.md`
- commit `b427ddaf39636359898d498d90277dc89c593f06`

Researcher validator:
- `scripts/k5_order8_edge01_edge02_ranktwo_sign_change.py`
- commit `c14b8fe2148be20d5bcd62f45065cc909bd302ff`

Authoritative production:
- workflow/head `6fb57d915cbb20c80674ec2a97121b35ffedd396`
- run `35035152999`, terminal success
- job `104602503455`, terminal success
- artifact `10422859073`
- artifact ZIP digest `sha256:b409c5dfb8c1182da8bcab903a800955c8a34462a179c841f08d511d55625867`
- production JSON SHA256 `c3abbcaf61bafc13eea2677ce71537d5899e375b3571e513abc1e94a0287a31f`

Researcher durable result:
- `results/K5_ORDER8_EDGE01_EDGE02_RANKTWO_SIGN_CHANGE_RESULT.md`
- commit `d01790ed11881c31ca5d7c6119fa40d90bff1368`
- classification `K5_EDGE01_EDGE02_RANKTWO_SIGN_CHANGE_EXACT_SCOPED`

Operational Actions provenance is internally consistent; this review does not classify `INVALID_PROVENANCE`.

## Independent Critic preregistration

- `prereg/K5_ORDER8_EDGE01_EDGE02_RANKTWO_INDEPENDENT_CRITIC_REVIEW.md`
- commit `40a3f78b2a85ef1750d8c6006438c0b1d2044398`
- frozen before durable Critic verdict file.

## Decisive object mismatch

Researcher preregistration freezes construction from the authoritative `all-32/full-source K5 order-eight principal-symbol object`.

The production general engine `selected_patterns()` iterates only

`itertools.product(mod.NODE_OPTIONS[0], repeat=5)`

which fixes every node to `k=0` and produces exactly `4^5=1024` source terms for the single boundary component `k=(0,0,0,0,0)`.

The post-prereg derivation explicitly states that the rank-two lane uses this `00000` component and calls it a component-level lane.

Therefore the terminal Researcher calculation is a representative-component result, not an all-32 tensor result. No prospectively frozen covector/projection converts the all-32 object into this scalar component.

## Mathematical status of the produced component witnesses

The Critic does not find evidence that the exact `00000` witness arithmetic itself is false. The determinant polynomial is positive in the open quadrant and the produced exact witness signs are consistent with the post-prereg derivation:

- `R(1,2)=1254383808/9191328125 > 0`
- `R(1,3)=-14327118848/13839609375 < 0`

These values remain non-authoritative exploratory evidence for a future prospectively frozen `00000` component gate.

## Critic verdict

`REQUIRES_NEW_PREREGISTERED_GATE`

Durable review:
- `results/K5_ORDER8_EDGE01_EDGE02_RANKTWO_ADVERSARIAL_REVIEW.md`
- commit `6d5da2372e62eed4327a2eb568e4ac974189c36c`

The old gate must not be rewritten post hoc to say it froze `00000`. A new component-specific gate could prospectively freeze that object, but the higher-information authorized front is the full all-32 / invariant-dual projective period.

## Claim locks

No K5 full order-eight zero/nonzero theorem; no physical finite part or selector; no regulator independence; no global patching; no causal multivertex closure; no G3/F9/G8/K5 promotion; no `NEW_PHYSICS_FOUND`; no complete-QG claim. Retain published spectral `i epsilon`. Historical Iter077E/F remain quarantined under `status/ITER077_CONTACT_FORMULA_ERRATUM.md`.
