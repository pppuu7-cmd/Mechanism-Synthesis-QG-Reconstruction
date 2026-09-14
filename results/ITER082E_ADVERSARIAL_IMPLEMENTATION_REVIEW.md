# Iter082E adversarial implementation review

Date: 2026-09-14
Run reviewed: `34895924300`
Artifact: `10368810908`
Artifact ZIP digest: `sha256:62352195c05d1bcd58738cf7ca7d58785b533bfe4cd208208e2e9c06bc354cf2`
Production commit: `27d726762f795326d905f09e340556aa3fae3d22`

## Verdict

**INVALID_IMPLEMENTATION** — green CI is quarantined and must not be cited as a scientific PASS or FAIL.

The preregistered scientific criteria remain frozen and unchanged.

## Defects found before any durable scientific classification

The raw artifact was consumed after terminal success. Inspection of the production implementation shows that several frozen predicates were not mechanically demonstrated:

1. `P2_collision_strata_preserved` was effectively reduced to the already-known counts `len(blocks)==16` and `len(chains)==20`, rather than evaluating the nonlinear chart map on block-diagonal and normal perturbations.
2. `P3_normal_ideal_filtration_preserved` relied on `filtration_violations=0` initialized by construction, not an independent computation of transformed normal-order series.
3. `P4_nested_chain_filtration_preserved_both_directions` counted intended checks but did not actually transport nested normal perturbations through the nonlinear node-wise map.
4. `P5_supported_jet_class_quotient_automorphism_degree9` inherited the same uncomputed filtration flag; inverse radial series alone is insufficient to certify the full nested filtration predicate.
5. Several negative controls were represented as metadata booleans and rejected by a validator reading those booleans, rather than by the same algebraic machinery used for the positive case.

The exact radial series inversion and raw S5 block/chain closure counts are useful controls, but they do not by themselves close the preregistered nonlinear chart-overlap gate.

## Required control-only repair

Without changing any scientific formula, frozen order, classification label or claim ceiling from the original preregistration, a successor implementation must:

- explicitly construct truncated polynomial node maps in formal variables;
- compute barycentric normal outputs for representative/all block sizes and verify zero constant normal term plus identity/invertible linear normal part;
- mechanically track powers/vanishing orders of the K3/K4/K5 normal ideals through both X→V and V→X to degree 9;
- mechanically audit all 20 nested chains, not merely count them;
- inject malformed chart maps into the same algebraic validators for the frozen negative controls;
- keep all finite coefficients/scales symbolic and never turn same-graph reassociation into a selector.

Until a repaired terminal artifact is consumed, Iter082E has **no scientific classification**.
