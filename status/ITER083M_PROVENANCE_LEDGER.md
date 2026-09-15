# Iter083M provenance ledger

**Date:** 2026-09-15

## Frozen scientific gate

Preregistration: `c801299beb44816941fd441715e3eb03c73740c7`, `prereg/ITER083M_SM_SOURCE_NORMAL_GEOMETRIC_RADIAL_BASIS.md`.

The gate asks only whether the frozen local/source collision geometry supplies a canonical tangent/tubular normal quadratic basis for K3/K4/K5 collision blocks. It explicitly does not define a finite part, analytic continuation, nonlinear global radial function, selector or regulator-independence theorem.

The preregistration freezes P0-P7 and eight negative/control requirements, including rejection of rooted metrics, edge-regulator-Q identification, nonorthogonal increments, single-chain-only reasoning and nonlinear-beta overclaim, while retaining finite-part/scale and global-patching freedom.

## Prospective / implementation chronology

- preregistration: `c801299beb44816941fd441715e3eb03c73740c7`;
- theorem derivation: `f566a9aad2d7adfbee16557de9a7fb9f8bdfa777`;
- initial validator: `74db7bbf6c9b364e8e4e26a17d428260c3e671e9`;
- pre-production source-lock alignment: `3c681c85a52b0c1b7d32ec5b933f6cc7a56ad898`;
- workflow / production head: `6916f3fb2f89f7f009bf9d3354b9dfe8c001de74`.

The `3c681c85...` repair occurred before the first production workflow and only changed a source-lock literal to match the existing frozen Iter077I text plus removed comments. It did not change the scientific object, predicates, PASS/FAIL criteria or interpretation ceiling.

## Production

- Actions run `34917280262`, terminal `success`;
- job `104217547168`, terminal `success`;
- artifact `10376298881`, `iter083m-source-normal-geometric-radial-basis`;
- ZIP digest `sha256:7659e611caa70da2803583ad0ee0f4ee29e7a3a9924058ee180d4c9a7a21566e`;
- production JSON SHA256 `5b11c3060b7809921d35323fec089f280c07614728e6282b7ea549301753b7a3`.

The workflow checked out the exact production head and asserted all emitted predicates and controls before artifact upload.

## Researcher result

- `results/ITER083M_SM_SOURCE_NORMAL_GEOMETRIC_RADIAL_BASIS_RESULT.md`;
- commit `40416f9011ddeafd6a7201d48b218b7eaf7b6ec1`;
- Researcher classification `ITER083M_SM_SOURCE_BOOST_GEOMETRY_GIVES_UNIQUE_LOCAL_FOREST_RADIAL_QUADRATIC_BASIS_SCOPED`;
- Researcher verdict `PASS_EXACT_SCOPED`.

The result itself respects the scoped scientific ceiling and does not claim a finite-part selector.

## Critic authority reconciliation

An initial same-session review, `results/ITER083M_ADVERSARIAL_REVIEW.md`, commit `eddf729b6a5563d9da5012655cba03e07228c8f7`, returned `CONFIRMED_SCOPED` but did not test whether the frozen malformed controls were actually exercised.

A later direct code audit is controlling:

- `results/ITER083M_ADVERSARIAL_IMPLEMENTATION_REVIEW.md`;
- commit `063087c5dfcf0cca9e2565cf75ef82c8ea640f6f`;
- mandatory verdict `INVALID_IMPLEMENTATION`.

Concrete implementation witness:

- `reject_rooted_metric = p6`, but `p6` only validates the good barycentric projectors and receives no rooted metric;
- `reject_nonorthogonal_increments = p5`, but `p5` only validates the good orthogonal increments and receives no malformed increment;
- `reject_edge_regulator_q_identification = p7` and `reject_nonlinear_beta_overclaim = p7`, while `p7` is only a three-string check in the theorem prose and receives neither a ten-edge Q object nor a false exact-beta claim.

Therefore the production can emit all controls `true` without actually exercising several frozen negative-control objects. Green CI does not satisfy the complete preregistered control contract.

## Scientific status

The scoped linear-algebra theorem is not scientifically refuted. Exact S_p/SO(3) invariant-form arguments, complete-graph/barycentric identities and nested variance algebra remain plausible. The authority failure is implementation/control certification only.

Latest mandatory Critic verdict: `INVALID_IMPLEMENTATION`.

Iter083M may not be used downstream until a control-only repaired production under the unchanged scientific preregistration is terminal and independently reviewed.

## Iter083N dependency guard

A later preregistration `c29ba0ddbaa4d6e1581db558b792565a7916a0cd` freezes Iter083N and explicitly consumes Iter083M radial geometry in P0. The preregistration itself may remain as outcome-independent preparation, but Iter083N implementation/production is **not authorized** while Iter083M is implementation-invalid. No Iter083M substantive PASS value may be consumed downstream before repair.

## Authorized next action

Only a control-only Iter083M repair/retry under the unchanged preregistration is authorized. The repair must actually inject and reject the frozen malformed metric/increment/object/claim controls using the relevant validators. If the scientific object, source authority, P0-P7, PASS/FAIL rules or interpretation ceiling changes, a new prospective gate is required.

All claim locks remain unchanged.