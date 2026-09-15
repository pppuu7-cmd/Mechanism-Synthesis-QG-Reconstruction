# Iter083M provenance ledger

**Date:** 2026-09-15

## Frozen scientific gate

Preregistration: `c801299beb44816941fd441715e3eb03c73740c7`, `prereg/ITER083M_SM_SOURCE_NORMAL_GEOMETRIC_RADIAL_BASIS.md`.

The gate asks only whether the frozen local/source collision geometry supplies a canonical tangent/tubular normal quadratic basis for K3/K4/K5 collision blocks. It explicitly does not define a finite part, analytic continuation, nonlinear global radial function, selector or regulator-independence theorem.

The preregistration freezes P0-P7 and eight negative/control requirements, including rejection of rooted metrics, edge-regulator-Q identification, nonorthogonal increments, single-chain-only reasoning and nonlinear-beta overclaim, while retaining finite-part/scale and global-patching freedom.

## Original production chronology — historical / non-authoritative

- preregistration: `c801299beb44816941fd441715e3eb03c73740c7`;
- theorem derivation: `f566a9aad2d7adfbee16557de9a7fb9f8bdfa777`;
- initial validator: `74db7bbf6c9b364e8e4e26a17d428260c3e671e9`;
- pre-production source-lock alignment: `3c681c85a52b0c1b7d32ec5b933f6cc7a56ad898`;
- workflow / production head: `6916f3fb2f89f7f009bf9d3354b9dfe8c001de74`;
- Actions run `34917280262`, job `104217547168`, terminal success;
- artifact `10376298881`, ZIP digest `sha256:7659e611caa70da2803583ad0ee0f4ee29e7a3a9924058ee180d4c9a7a21566e`;
- production JSON SHA256 `5b11c3060b7809921d35323fec089f280c07614728e6282b7ea549301753b7a3`;
- Researcher result `results/ITER083M_SM_SOURCE_NORMAL_GEOMETRIC_RADIAL_BASIS_RESULT.md`, commit `40416f9011ddeafd6a7201d48b218b7eaf7b6ec1`.

A first Critic review `eddf729b6a5563d9da5012655cba03e07228c8f7` returned `CONFIRMED_SCOPED`, but a later direct implementation audit is controlling for this historical run:

- `results/ITER083M_ADVERSARIAL_IMPLEMENTATION_REVIEW.md`;
- commit `063087c5dfcf0cca9e2565cf75ef82c8ea640f6f`;
- verdict `INVALID_IMPLEMENTATION`.

The concrete defect was that several frozen malformed controls were never injected: `reject_rooted_metric` aliased P6 on the good projectors, `reject_nonorthogonal_increments` aliased P5 on the good increments, and multiple object/claim controls aliased a theorem-text boolean P7. Historical run `34917280262` therefore remains non-authoritative despite green CI.

## Prospective control-only repair 1

The repair contract was frozen before implementation/output:

- `prereg/ITER083M_CONTROL_ONLY_REPAIR_1.md`;
- commit `9da79bd7cf1e78c546017340e234eeffdaef52dc`.

The repair preserves the parent hypothesis, exact object, source authority, P0-P7, scientific PASS classification and interpretation ceiling. It changes only execution of the already-frozen negative controls.

Repair implementation / production head:

- `scripts/iter083m_source_normal_geometric_radial_basis.py`;
- commit `463ba012c4b3f8d465ab7df99995f5f40f3e7e44`.

Because the existing workflow is triggered by changes to the validator path, this commit launched the repaired production without a competing gate.

## Repaired production

- Actions run `34921183332`, terminal `success`;
- job `104229460141`, terminal `success`;
- artifact `10378026902`, `iter083m-source-normal-geometric-radial-basis`;
- artifact ZIP digest `sha256:06d6c560942a73bd78c31557f9fb3f4714a17b495857ed17071d271409700f11`;
- production JSON SHA256 `6572765b7a760a7505d6dc1c23d9239d5ede80cd37e1174c171951635f26c3e2`;
- durable copied raw output `results/raw/iter083m_sm_control_repair_1.json`, commit `41a62c9b6d3f1728ff3c1bb927a7ff33ebd742a0`;
- repaired Researcher result `results/ITER083M_CONTROL_REPAIR_1_RESULT.md`, commit `6f886ce799a17cde6ad35c7686f4ea96396acb7e`.

The workflow checked out exact head `463ba012...`, all P0-P7 passed, and every repaired control boolean passed.

## Executed malformed-control witnesses

The repaired production emits the actual malformed objects/claims used by the validators:

1. rooted metric candidate `diag(1,2,3,4,5)` is not S5 invariant;
2. auxiliary ten-edge `Q` object has kind/domain/dimension `(edge_regulator_metric, R10_edge_regulator_space, 10)` while the physical deepest normal object has `(normal_fiber_metric, R3_tensor_Std5, 12)`; attempted identity is rejected;
3. J restricts to zero on `Std_p` for p=3,4,5;
4. good chain validates while mutated `B_bad=B+A` fails the same chain validator;
5. a one-chain truncated forest fails the same 20-chain coverage validator;
6. source authority authorizes only tangent `O(r^2)` beta relation and rejects an injected exact-global beta claim;
7. a finite-part/subtraction-scale promotion claim is rejected by the structured interpretation firewall;
8. a global nonlinear/all-strata patching promotion claim is rejected by the same structured firewall.

Therefore the specific implementation witness identified by Critic `063087c5...` is repaired at the Researcher execution level.

## Repaired Researcher scientific status

Researcher classification remains exactly:

`ITER083M_SM_SOURCE_BOOST_GEOMETRY_GIVES_UNIQUE_LOCAL_FOREST_RADIAL_QUADRATIC_BASIS_SCOPED`.

Researcher verdict: `PASS_EXACT_SCOPED`.

The scientific content is unchanged: in the frozen local all-`j=1/2` common-collision scope, source small-boost geometry plus authoritative barycentric projectors determines a unique invariant tangent/tubular radial quadratic basis on each K3/K4/K5 normal fiber, with exact nested orthogonal ranks `(6,3,3)` over all 20 maximal chains.

This is radial geometry only; it is not a physical finite-part selector.

## Authority status after repair

The controlling Critic handoff `status/MSQGR_ADVERSARIAL_CRITIC_HANDOFF.md` requires **terminal repaired Iter083M plus independent Critic review** before Iter083N can be retried.

Accordingly:

- repaired Iter083M is now terminal Researcher `PASS_EXACT_SCOPED`, **pending independent Critic review**;
- historical Iter083M run `34917280262` remains `INVALID_IMPLEMENTATION` provenance;
- Iter083N remains `INVALID_PROVENANCE` and must not be promoted or rerun in this Researcher gate;
- Iter083O remains preparation-only/downstream-quarantined.

## Source / erratum locks

`status/ITER077_CONTACT_FORMULA_ERRATUM.md`, blob `63356e5099929f2b21d9d7296ab97f15ff163dba`, remains controlling. Historical source-lock-invalid Iter077E/F siblings remain quarantined.

Iter077I source-ordered authority remains: historical run `34786550378` failed its machine-readable source-order lock; control-only alias head `102fc7268b732bead5dfcf6d61fe4479ae1d3030` produced authoritative run `34786586785`, all four lanes plus aggregate success, artifact `10326812769`, digest `sha256:b9e7d617598acaeb60ee7018e3ee4f78a232b32be86b112da4713352d9797887`.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no unique physical K5 extension; no source-authorized finite-part selector; no actual nonzero physical finite-part scheme-dependence theorem; no generic finite-spin theorem; no causal-vertex finiteness/divergence theorem; no regulator dependence/independence theorem for the physical amplitude; no G3/F9/G8/K5 promotion; no fitted subtraction constants/scales or preferred finite parts.
