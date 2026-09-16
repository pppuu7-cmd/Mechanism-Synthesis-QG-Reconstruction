# Provenance ledger — K5 projective blow-up normal-flux scaling Critic

Date: 2026-09-16

## Researcher authority reviewed

- scientific preregistration: `prereg/K5_SCHWINGER_PROJECTIVE_BLOWUP_NORMAL_FLUX_SCALING.md`, commit `06fc09a0355e6cc15889ac9f244ab03d4cb86569`;
- derivation: `sources/K5_SCHWINGER_PROJECTIVE_BLOWUP_NORMAL_FLUX_SCALING_DERIVATION.md`, commit `d756f0507c8b7816344fd75b1f8882bca071ede5`;
- implementation: `scripts/k5_projective_blowup_flux_scaling_verify.py`, commit `a0b2ba1da34a7488af21b647a3213a4f39841de3`;
- workflow/head: `b94733dda1083db76eb3a8abd64f6a43c60e788b`;
- run `35087556685`, terminal success;
- job `104765865533`, terminal success;
- artifact `10441874454`;
- artifact ZIP digest `sha256:3b46f9647ba064b4951e830671123753a270fbdf522b77f8e1e4b910d6d6c59c`;
- Researcher production JSON SHA256 `2e3e02377c1a5a5fd294ec9a8aff4a389f1df06688546b03167ba2b2802f84ca`;
- Researcher classification `K5_PROJECTIVE_BLOWUP_NORMAL_FLUX_SCALING_DERIVED_EXACT_SCOPED`.

## Independent Critic chronology

- prospective Critic preregistration: `prereg/K5_PROJECTIVE_BLOWUP_NORMAL_FLUX_SCALING_INDEPENDENT_CRITIC_REVIEW.md`, commit `2e788241b2e14dc5af9c95bc09d6c16125d9378f`;
- Critic implementation: `scripts/k5_projective_blowup_flux_scaling_independent_critic.py`, commit `cec43e41df322f4e84c66a6e6e6acbf35105c6a0`;
- workflow/head: `bdaea0b793fa3d61f2377243ef284bf10e168701`;
- Critic run `35093003694`, terminal success;
- Critic job `104783534228`, terminal success;
- artifact `10444534918`;
- artifact ZIP digest `sha256:0a62ac2faa9f6b484bf5b0fb57d4683fd8b8b9578ff61cb85be1cbe75fd4faa3`;
- Critic production JSON SHA256 `ea52c3d76601b58752e605184ef5471db239bcf3d484bab0f0a5d58dd8fc7008`;
- durable machine summary `results/raw/k5_projective_blowup_flux_scaling_independent_critic_authoritative.json`, commit `8d00e419bb6b67be119747504c7ab8b3ceb3af27`;
- controlling adversarial review `results/K5_PROJECTIVE_BLOWUP_NORMAL_FLUX_SCALING_ADVERSARIAL_REVIEW.md`, commit `f687ab9e34e8b4cfc6f4a4cd003938b1ef434baa`.

## Terminal scientific state

Mandatory Critic verdict: `SCIENTIFIC_FAIL_CONFIRMED`.

Exact counterexample: `v=E` (equivalently polynomial `q_i=1`) has raw `v(t)=t != 0` on any proper nonempty projective corner, while `Omega_9=i_E Vol` implies `i_v Omega_9=i_E Omega_9=0`. Hence the Researcher universal raw-`v(t)` flux formula is false.

Correct projective/simplex normal component is

`u(t)=v(t)-t S/s1`,

with `u=v-(S/s1)E`, `S=sum_i v_i`, `s1=sum_i alpha_i`.

The scalar blow-up Jacobian exponent `k-1` is independently confirmed and survives.

No physical corner verdict and no integrated Stokes verdict are assigned.

## Erratum/source locks

`status/ITER077_CONTACT_FORMULA_ERRATUM.md` remains controlling. Historical Iter077E/F remain source-lock-invalid and quarantined. The published one-wedge spectral `i epsilon` and corrected Iter077I source-order authority remain unchanged.

## Downstream lock

The 34-orbit physical action-flux audit must not consume the failed raw-`v(t)` normal-flux exponent. A new prospectively preregistered corrected projective-tangent flux gate is required before substantive corner classification resumes. The independent constant-`2x2` action repair/retry is not blocked by this geometry failure.
