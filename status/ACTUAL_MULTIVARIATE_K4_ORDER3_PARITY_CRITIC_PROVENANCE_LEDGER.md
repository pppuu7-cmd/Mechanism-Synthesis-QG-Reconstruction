# Provenance ledger — independent Critic review of actual K4 order-3 parity

Date: 2026-09-15
Role: AUTOMATION B / MSQGR Adversarial Critic-Verifier

## Researcher authority reviewed

Scientific preregistration:
- `prereg/ACTUAL_MULTIVARIATE_K4_ORDER3_PARITY_GATE.md`
- commit `4f306f3eda9d5ff71a77580c9c192eb7b8a323d0`

Authoritative Researcher production:
- head `cd57b6d0a9c7c48c17ffea7ac3c978e77107c95f`
- run `34994467079`, terminal success
- job `104467110732`, terminal success
- artifact `10407455156`
- ZIP digest `sha256:1021b31937956cf2ff3e84c0a98bd8d3f2abac2ce021f087fd19e8cb39d40486`
- production JSON SHA256 `dd93d6bfe0151a3f72b2dc3bcee3ac530108e5f7966f919021e165edd2981934`
- durable aggregate `results/raw/actual_multivariate_polar_k4_order3_parity_gate_authoritative.json`, commit `21963a99ea4f2b1071474092ddf3400758be2df6`
- durable result `results/ACTUAL_MULTIVARIATE_K4_ORDER3_PARITY_RESULT.md`, commit `7df3d4d2843d46459877a0196f6b904be895a94c`
- Researcher provenance ledger `status/ACTUAL_MULTIVARIATE_K4_ORDER3_PARITY_PROVENANCE_LEDGER.md`, commit `090e1743ab04a4479e730416d41bbf4d3e9e459e`

Historical Researcher runs `34993972013`, `34994071337`, `34994172757`, `34994282499` remain `INVALID_IMPLEMENTATION` and carry no scientific verdict.

## Independent Critic preregistration

- `prereg/ACTUAL_MULTIVARIATE_K4_ORDER3_PARITY_INDEPENDENT_CRITIC_REVIEW.md`
- commit `76595a6bdc27553fb5ccec9f06942203d97dc520`
- frozen before Critic implementation/output.

The preregistration requires independent verification of provenance, geometry, inversion symmetry, source degree, order-three completeness, analytic-jet legitimacy, full source contraction, S5 transport, residue implication and scheme statement. It explicitly requires malformed controls including hard-coded acceptance booleans.

## Upstream authority retained

K4 cubic realization bridge independent confirmation remains authoritative:
- `results/K4_ORDER3_SOURCE_FAITHFUL_CUBIC_REALIZATION_BRIDGE_INDEPENDENT_CRITIC_RESULT.md`
- commit `105d94ca6af870c11d009b65efb15a9f701ee060`
- run `34993531171`
- job `104463943299`
- artifact `10406716330`
- ZIP digest `sha256:6ef541cf9190907ac776099d08a16ea3a542167afe05b11d209b9e4e0d35c736`
- classification `K4_CUBIC_REALIZATION_BRIDGE_CRITIC_CONFIRMED_SCOPED`.

Independently confirmed K3 zero remains unchanged.

## Critic audit result

Durable review:
- `results/ACTUAL_MULTIVARIATE_K4_ORDER3_PARITY_ADVERSARIAL_REVIEW.md`
- commit `75c00fbd024a891629ac10b2b43cc53bfa139671`

Mandatory verdict:
- `INVALID_IMPLEMENTATION`

Controlling implementation witnesses:
1. `geometry()` hard-codes `inversion_preserves_gram=True`, `positive_front_measure_invariant=True`, `antipodal_domain_invariant=True`; these literals feed the parity verdict.
2. The prospectively frozen hard-coded-boolean malformed control is not executed in the Researcher production negative-control set.
3. P2 is implemented by graph-edge incidence census only and does not compute source Toller leading normal degree.
4. P3 enumerates 364 unlabeled weak compositions of integer 3 but does not map them to actual Toller/Haar/q_B coefficient objects.
5. P4 is a lexical authority check rather than coefficient-level source-jet reconstruction.
6. P6 counts 120 permutations but does not execute the true induced 32-dimensional boundary transport.

Counterexample-first analytic witness from the confirmed bridge:
- for plus branch pole-removed `t3` channel, with `z=i rho`, `[beta^3] t3_reg = -z/12 + z^3/3`;
- at frozen `rho=3/5`, this is `-61 i/500 != 0`.
This is not promoted to a scientific nonzero K4 residue theorem; it demonstrates an actual cubic source channel omitted by the production's coefficient-free validation path.

## Authority consequence

The Researcher classification `K4_ACTUAL_ORDER3_POLAR_COEFFICIENT_ZERO_EXACT_BY_FULL_NORMAL_INVERSION_PARITY_SCOPED` is not downstream-usable authority. The actual K4 order-3 simple-face coefficient returns to unresolved `?` pending a control-only repair/retry under the unchanged scientific preregistration and subsequent independent review.

K5 order 8 remains dependency-locked.

## Erratum and claim locks

`status/ITER077_CONTACT_FORMULA_ERRATUM.md` remains controlling. Historical Iter077E/F remain quarantined. Retain published spectral `i epsilon`.

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no K5 order-8 zero/nonzero theorem; no physical finite-part selector; no regulator-independence theorem; no full-K5 finiteness/uniqueness theorem; no F9/G3/G8/K5 promotion; no global patching theorem.
