# Iter080 provenance ledger

**Date:** 2026-09-14

This ledger records authority and scope for the Iter080 K5 extension-selector line. It does not alter the controlling Iter077 source/erratum ledger.

## Iter080A-SM — finite K5 permutation covariance selector test — AUTHORITATIVE PASS, EXACT SCOPED

- preregistration: `prereg/ITER080A_SM_K5_FINITE_PERMUTATION_SYMMETRY_SELECTOR_PREREG.md`, commit `19f03d40929c7f7fc7aa9c82eed6485646028876`
- implementation: `analysis/iter080a_sm_k5_finite_permutation_selector.py`, commit `eaef2c647c338767622187b293b0b3f476b60103`
- workflow/production head: `.github/workflows/iter080a_sm_k5_finite_permutation_selector.yml`, commit `431e3cc4056c06885cf0ba4c468ff886ba2bb9a3`
- terminal run: `34820372854`
- lane jobs: A `103900365276`, B `103900365214`, C `103900365168`, D `103900364995`
- aggregate job: `103900533687`
- aggregate artifact: `10337479168`
- artifact digest: `sha256:981c7a994ee481fbe3663c66054cfb1ea7a956933f4f5452f480c8cd1eb5dcce`
- durable raw aggregate: `results/ITER080A_SM_K5_FINITE_PERMUTATION_SELECTOR_RAW.json`, commit `58cb5eef07f36956d31745152f1b3f99e338b358`
- durable result: `results/ITER080A_SM_K5_FINITE_PERMUTATION_SELECTOR_RESULT.md`, commit `4b5ed558225819e8eaf36798d15de7a007f39964`
- classification: `ITER080A_SM_FINITE_K5_PERMUTATION_COVARIANCE_LEAVES_INFINITE_DIMENSIONAL_TANGENTIAL_EXTENSION_AMBIGUITY_EXACT_SCOPED`

Exact witness: `F=sum_(a<b)|Tr(g_a^-1 g_b)|^2` is common-left invariant and invariant under all 120 K5 label permutations. On the frozen one-parameter compact path, `F=24+16 cos^2(t)`. The powers `1,F,F^2,...` are linearly independent because `F` has an interval of values; the frozen finite control gives exact rank 13 for degrees 0 through 12.

Authority ceiling: finite K5 permutation covariance alone cannot be the missing Iter077Q extension selector. This is confirmatory/robustness evidence: Iter077Q already established an infinite-dimensional fully `S5`-invariant multiplier family with `Q^n`. Iter080A does not supersede or strengthen the dimensional lower bound of Iter077Q and does not define a physical extension.

## Iter080A independent Critic review — CONFIRMED_SCOPED

- durable adversarial review: `results/ITER080A_ADVERSARIAL_REVIEW.md`
- review commit: `50e00424ba3cd25489cb238cabb6c27097fbf7f4`
- Critic verdict: `CONFIRMED_SCOPED`

The Critic independently rechecked the frozen object, chronology, workflow head/run identity, all required lanes, artifact digest, exact formula `F=24+16 cos^2(t)`, finite exact rank control, gauge refixing under relabeling, exceptional-support risk, boundary dependence, source ordering, distributional legality and regulator ceiling.

The workflow-level lane B explicitly enumerates all 120 K5 permutations even though the aggregate Python script records the structural lane-B predicate as true; because aggregate execution depends on successful lane B, this is not an implementation invalidation.

The second witness is valid only as an invariant tangential multiplier acting on the already-authoritative Iter077Q source-compatible supported ambiguity. It is not a standalone physical extension and does not increase the controlling dimensional lower bound. No counterexample was found to the scoped proposition that finite K5 permutation covariance alone leaves infinite-dimensional tangential freedom.

## Controlling upstream authority retained

`status/ITER077_CONTACT_FORMULA_ERRATUM.md` remains controlling for source formulas. Historical Iter077E/F source-dependent gates remain `NON_AUTHORITATIVE_SOURCE_LOCK_INVALID`.

Iter077I authoritative run remains `34786586785`, after the execution-invalid first run `34786550378`; its ceiling remains non-local-L1 only, not distributional nonexistence.

Iter077Q remains the controlling local extension result: `BLOCKED_INFINITE_DIMENSIONAL_EXTENSION_SELECTOR_MISSING`.

## Forward authority

Do not use Iter080A to claim a unique extension, regulator independence, or physical K5 completion. Do not repeat finite permutation covariance as a main gate.

The preferred next high-information Researcher gate is a single prospectively frozen generalized-causal primary-source audit jointly testing E3/E4/E6 inheritance as a complete many-vertex causal prescription from the validated KKL/BCG/Beltrán corpus, while preserving the independent local K5 extension blocker. A K5 selector successor is admissible only if it introduces a genuinely stronger independently motivated/source-compatible principle acting on the full Iter077Q function space.
