# Iter083F provenance ledger

Date: 2026-09-15

## Authority chain

- Scientific preregistration: `prereg/ITER083F_SM_COMMON_SPECTRAL_EPSILON_NOT_K5_COLLISION_REGULATOR.md`, commit `18fbeca191aa05fe09e3e38ed60abec53e09a8c9`.
- Public source lock: `sources/ITER083F_PUBLIC_SOURCE_LOCK.md`, commit `d69eb1b5c187be257c507cdc3527ec4f9e824c97`.
- Machine-readable source lock: `sources/raw/iter083f_finite_epsilon_source_lock.json`, commit `66c9a80ca6cecc59131deccca5d6e37a7ef57011`.
- Exact derivation: `sources/ITER083F_SM_COMMON_SPECTRAL_EPSILON_COLLISION_SCALING_DERIVATION.md`, commit `464e54abfb63aa123ff9a6614fc033d98274b733`.
- Validator: `scripts/iter083f_common_spectral_epsilon_collision_test.py`, commit `8094d15e62e285da0733852c80386c380fb7451a`.
- Production workflow/head: `d5778a6bc93e5b3b6e129f579299be5a1f0a1b28`.
- Authoritative Actions run: `34912148095`, terminal `success`.
- Job: `104201783021`, terminal `success`.
- Artifact: `10374589062`, name `iter083f-common-spectral-epsilon-collision-test`.
- Artifact ZIP digest: `sha256:7f64b3a817ea89cdef21bf75ef001f8afc1699c77fdcb661164e889f0cca45e0`.
- Production JSON SHA256: `9242bfeea498e8634bec469ca52907eb1852ec60d9e56c200af4dee2d6e55fa6`.
- Durable Researcher result: `results/ITER083F_SM_COMMON_SPECTRAL_EPSILON_COLLISION_RESULT.md`, commit `950611372f7b5898d5822f3dafd5f875e6007183`.
- Independent Critic review: `results/ITER083F_ADVERSARIAL_REVIEW.md`, commit `f55f2704acd687deb6f14955f3b190799e81d954`, verdict `CONFIRMED_SCOPED`.

## Frozen classification

`ITER083F_SM_COMMON_FINITE_SPECTRAL_EPSILON_DOES_NOT_REGULARIZE_K5_COMMON_COLLISION_EXACT_SCOPED`

Researcher verdict: `PASS_EXACT_SCOPED`.

Critic verdict: `CONFIRMED_SCOPED`.

## Exact terminal facts

For the frozen all-`j=1/2` common-K5 collision sector, a common fixed finite one-wedge spectral Feynman parameter `epsilon>0` across all ten wedges does not change the leading collision order.

- exact shifted Toller denominator cancellation: pass;
- all four branch leading signs: `(-,+,+,-)` in the frozen ordering;
- leading coefficient independent of `epsilon`;
- gamma-simple magnitude: `2/(1+gamma^2)`;
- one-wedge order: `beta^-2`;
- ten-wedge common-collision order: `r^-20`;
- normal codimension: `12`;
- radial measure times leading integrand: `r^-9 dr`;
- ordinary local integrability at the common collision: false.

Thus the existing spectral epsilon, even held finite and common while the ten-wedge product is formed first, does not by itself regularize the K5 collision or eliminate the Iter083B `dim_C F_8=377` extension problem.

## Scope lock

This result does not rule out genuinely joint regulators or selectors that act on collision-normal variables or on the supported kernel, including multivariable boundary values, analytic regularization of scaling powers, microlocal/renormalized multiplication plus normalization, composition/gluing laws, differential/positivity/RG constraints, or other joint prescriptions.

No causal-vertex nonexistence theorem, generic-spin completeness, global all-strata patching theorem, regulator independence, E3/E4/E6 closure, G3/F9/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete-QG claim follows.

## Recovery note — Iter083A classifier repair

During recovery of this run, a pre-terminal audit of an already-launched Iter083A rerun found two classifier defects: outcome-biased P6 and collapse of scientific FAIL into `INVALID_IMPLEMENTATION`. A control-only repair was frozen before terminal-output inspection in `prereg/ITER083A_CONTROL_ONLY_REPAIR_1.md`; repaired run `34912167894` on head `8af7f1667a8cd2de4cc60f2d34560b88dda650d8` terminated success and reproduced the already-authoritative Iter083A values while restoring outcome-neutral verdict taxonomy. This is provenance reconciliation only, not a second scientific gate and does not alter Iter083A/B/C/D/E/F scientific content.
