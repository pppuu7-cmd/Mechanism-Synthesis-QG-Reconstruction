# Iter083M provenance ledger

**Date:** 2026-09-15

## Frozen scientific gate

Parent preregistration: `prereg/ITER083M_SM_SOURCE_NORMAL_GEOMETRIC_RADIAL_BASIS.md`, commit `c801299beb44816941fd441715e3eb03c73740c7`.

The gate asks only whether the frozen local/source collision geometry supplies a canonical tangent/tubular normal quadratic basis for K3/K4/K5 collision blocks. It explicitly does not define a finite part, analytic continuation, nonlinear global radial function, selector or regulator-independence theorem.

## Original production chronology — historical / non-authoritative

- preregistration `c801299beb44816941fd441715e3eb03c73740c7`;
- theorem derivation `f566a9aad2d7adfbee16557de9a7fb9f8bdfa777`;
- initial validator `74db7bbf6c9b364e8e4e26a17d428260c3e671e9`;
- pre-production source-lock alignment `3c681c85a52b0c1b7d32ec5b933f6cc7a56ad898`;
- production head `6916f3fb2f89f7f009bf9d3354b9dfe8c001de74`;
- run `34917280262`, job `104217547168`, terminal success;
- artifact `10376298881`, ZIP digest `sha256:7659e611caa70da2803583ad0ee0f4ee29e7a3a9924058ee180d4c9a7a21566e`;
- production JSON SHA256 `5b11c3060b7809921d35323fec089f280c07614728e6282b7ea549301753b7a3`;
- Researcher result commit `40416f9011ddeafd6a7201d48b218b7eaf7b6ec1`.

The controlling historical review is `results/ITER083M_ADVERSARIAL_IMPLEMENTATION_REVIEW.md`, commit `063087c5dfcf0cca9e2565cf75ef82c8ea640f6f`, verdict `INVALID_IMPLEMENTATION`. The original run remains non-authoritative permanently because multiple frozen malformed controls were aliases instead of executed injections.

## Prospective control-only repair 1

Repair preregistration:

- `prereg/ITER083M_CONTROL_ONLY_REPAIR_1.md`;
- commit `9da79bd7cf1e78c546017340e234eeffdaef52dc`.

It preserves the parent hypothesis, object, source authority, P0-P7, PASS classification and interpretation ceiling. It changes only execution/wiring needed to make the already-frozen negative controls outcome-sensitive.

Repair implementation / production head:

- `scripts/iter083m_source_normal_geometric_radial_basis.py`;
- commit `463ba012c4b3f8d465ab7df99995f5f40f3e7e44`.

## Repaired production

- run `34921183332`, terminal success;
- job `104229460141`, terminal success;
- exact checkout head `463ba012c4b3f8d465ab7df99995f5f40f3e7e44`;
- artifact `10378026902`, `iter083m-source-normal-geometric-radial-basis`;
- artifact ZIP digest `sha256:06d6c560942a73bd78c31557f9fb3f4714a17b495857ed17071d271409700f11`;
- production JSON SHA256 `6572765b7a760a7505d6dc1c23d9239d5ede80cd37e1174c171951635f26c3e2`;
- raw copy `results/raw/iter083m_sm_control_repair_1.json`, commit `41a62c9b6d3f1728ff3c1bb927a7ff33ebd742a0`;
- repaired Researcher result `results/ITER083M_CONTROL_REPAIR_1_RESULT.md`, commit `6f886ce799a17cde6ad35c7686f4ea96396acb7e`.

All P0-P7 passed. The repaired artifact emits explicit witnesses for every frozen malformed control.

## Executed malformed-control witnesses

1. rooted metric `diag(1,2,3,4,5)` fails exact S5 permutation-conjugation invariance;
2. auxiliary ten-edge `Q` and physical normal metric have incompatible kind/domain/dimension metadata and identity is rejected;
3. `J|Std_p=0` for p=3,4,5;
4. good chain passes while `B_bad=B+A` fails the same chain validator;
5. a one-chain truncation fails the same 20-chain coverage validator;
6. tangent beta claim is accepted while exact-global beta claim is rejected;
7. finite-part/subtraction-scale promotion is rejected;
8. global nonlinear/all-strata patching promotion is rejected.

## Independent Critic review

Prospective Critic-only preregistration:

- `prereg/ITER083M_REPAIRED_INDEPENDENT_CRITIC_REVIEW.md`;
- commit `065870cd2aba398e48f126e7e116823589f3ca08`.

Controlling review:

- `results/ITER083M_REPAIRED_ADVERSARIAL_REVIEW.md`;
- commit `e7623cb5303ea49894e480e2fc4a884df44e7713`;
- mandatory verdict `CONFIRMED_SCOPED`;
- Critic-gate classification `ITER083M_REPAIRED_CRITIC_CONFIRMED_SCOPED`.

The Critic independently verified production provenance, exact source-tangent normalization, all 20 nested projector chains, exact ranks `(2,1,1)` / physical `(6,3,3)`, all 120 S5 relabellings, and the repaired malformed-control sensitivity. No scientific counterexample was found within the frozen tangent/tubular scope.

The rooted-metric control uses direct ambient S5 metric conjugation rather than the literal positive-projector P6 helper, but it tests the same frozen permutation action and is sufficient to reject the malformed rooted geometry. This is recorded as an implementation qualification, not an authority defect.

## Authoritative scientific status

Repaired Iter083M is now usable authority **only** for:

`ITER083M_SM_SOURCE_BOOST_GEOMETRY_GIVES_UNIQUE_LOCAL_FOREST_RADIAL_QUADRATIC_BASIS_SCOPED`.

Meaning: in the frozen local all-`j=1/2` common-collision scope, the source small-boost relation plus authoritative barycentric projectors determines a unique invariant tangent/tubular radial quadratic basis on each K3/K4/K5 normal fiber, with exact nested physical ranks `(6,3,3)` over all 20 maximal chains.

It is not a finite-part selector or global nonlinear radial theorem.

## Dependency effect

- historical original Iter083M remains `INVALID_IMPLEMENTATION` provenance;
- repaired Iter083M is `CONFIRMED_SCOPED` and may be consumed only within its frozen scope;
- old Iter083N remains `INVALID_PROVENANCE` and is not rehabilitated;
- a **fresh Iter083N retry under its unchanged frozen scientific contract is now authorized**;
- the retry must make P0 consult controlling repository authority, including `e7623cb5...`, and must record actual source-lock/theorem commits `cf9d17cc8dae087f2c59ff0adb9f8aeff8ef7533` and `70a756c9c7c66f822d0e5933e9522b2d359dafe8`;
- Iter083O remains preparation-only until a valid Iter083N retry is terminal and independently reviewed.

## Source / erratum locks

`status/ITER077_CONTACT_FORMULA_ERRATUM.md`, blob `63356e5099929f2b21d9d7296ab97f15ff163dba`, remains controlling. Historical source-lock-invalid Iter077E/F siblings remain quarantined.

Iter077I source-order authority remains the repaired run `34786586785`, artifact `10326812769`, digest `sha256:b9e7d617598acaeb60ee7018e3ee4f78a232b32be86b112da4713352d9797887`.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no unique physical K5 extension; no source-authorized finite-part selector; no actual nonzero physical finite-part scheme-dependence theorem; no generic finite-spin theorem; no causal-vertex finiteness/divergence theorem; no physical regulator dependence/independence theorem; no G3/F9/G8/K5 promotion; no fitted subtraction constants/scales or preferred finite parts.