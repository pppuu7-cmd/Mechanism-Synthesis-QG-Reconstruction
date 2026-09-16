# AUTOMATION B adversarial review — K5 projective blow-up normal-flux scaling

Date: 2026-09-16

Mandatory verdict: **`SCIENTIFIC_FAIL_CONFIRMED`**.

## Result reviewed

Researcher prospective preregistration: `prereg/K5_SCHWINGER_PROJECTIVE_BLOWUP_NORMAL_FLUX_SCALING.md`, commit `06fc09a0355e6cc15889ac9f244ab03d4cb86569`.

Researcher derivation: `sources/K5_SCHWINGER_PROJECTIVE_BLOWUP_NORMAL_FLUX_SCALING_DERIVATION.md`, commit `d756f0507c8b7816344fd75b1f8882bca071ede5`.

Researcher implementation: `scripts/k5_projective_blowup_flux_scaling_verify.py`, commit `a0b2ba1da34a7488af21b647a3213a4f39841de3`.

Researcher production head `b94733dda1083db76eb3a8abd64f6a43c60e788b`, run `35087556685`, job `104765865533`, terminal success, artifact `10441874454`, ZIP digest `sha256:3b46f9647ba064b4951e830671123753a270fbdf522b77f8e1e4b910d6d6c59c`, production JSON SHA256 `2e3e02377c1a5a5fd294ec9a8aff4a389f1df06688546b03167ba2b2802f84ca`.

Researcher classification: `K5_PROJECTIVE_BLOWUP_NORMAL_FLUX_SCALING_DERIVED_EXACT_SCOPED`.

Independent Critic preregistration was frozen before Critic implementation at `2e788241b2e14dc5af9c95bc09d6c16125d9378f`. Critic implementation `cec43e41df322f4e84c66a6e6e6acbf35105c6a0`, workflow/head `bdaea0b793fa3d61f2377243ef284bf10e168701`, run `35093003694`, job `104783534228`, terminal success, artifact `10444534918`, ZIP digest `sha256:0a62ac2faa9f6b484bf5b0fb57d4683fd8b8b9578ff61cb85be1cbe75fd4faa3`, Critic JSON SHA256 `ea52c3d76601b58752e605184ef5471db239bcf3d484bab0f0a5d58dd8fc7008`.

## Exact scientific contradiction

The scalar blow-up Jacobian part of the Researcher derivation is correct: for a proper subset `Z`, `|Z|=k`, with `alpha_e=t beta_e`, `sum_Z beta_e=1`, the projective scalar measure contributes `t^(k-1) dt` times a nonzero angular/tangential form. The independent Critic recomputed the exact Jacobian for `k=1,...,9` and recovered determinant ratio `+/-1` after division by `t^(k-1)`.

The **normal-flux contraction is wrong**. The standard projective Schwinger form is

`Omega_9 = i_E (dalpha_1 wedge ... wedge dalpha_10)`,

where `E=sum_i alpha_i partial_i` is the Euler/radial field. Therefore identically

`i_E Omega_9 = i_E i_E (dalpha_1 wedge ... wedge dalpha_10) = 0`.

Consequently projective contraction is invariant under the representative change

`v -> v + f E`.

On the standard simplex `s1=sum_i alpha_i=1`, the controlling projective-gauge authority already fixes the tangent representative

`u_i = v_i - (S/s1) alpha_i`, `S=sum_i v_i`.

For `t=sum_(e in Z) alpha_e`, the physical projective normal component is therefore

`u(t) = v(t) - t S/s1`,

not raw `v(t)`.

Researcher instead claims

`pullback(i_v Omega_9) = +/- t^(k-1) v(t) omega_Z`

and hence a universal flux exponent based on `ord_t v(t)`. This formula is not invariant under addition of a radial Euler component and therefore cannot be the contraction of the projective form.

## Counterexample-first witness

Take the admissible polynomial logarithmic field

`q_i=1` for every i, hence `v_i=alpha_i` and `v=E`.

This satisfies the Researcher frozen convention `v_i=alpha_i q_i` with polynomial `q_i` and no singularity.

For every nonempty proper `Z`, raw

`v(t)=t != 0`

on the relative interior. Researcher's formula therefore predicts a nonzero normal flux proportional to `t^k`.

But exactly

`i_v Omega_9 = i_E Omega_9 = 0`.

The independent Critic exterior-algebra implementation verifies this directly. At its exact rational sample, `t=2/11`, raw `v(t)=2/11` is nonzero while the true projective contraction is identically zero. This is a direct counterexample to the universal Researcher normal-flux identity, not a numerical discrepancy or generic doubt.

For a second exact non-radial test field with constant polynomial `q_i=i+1`, the Critic verifies

`i_v Omega_9 = i_u Omega_9`

and

`u(t)=v(t)-t S/s1`.

## Implementation audit

The production script also does not independently execute several frozen obligations. In particular, it sets

- `normal_field_universal_t_factor=True`,
- `full_set_not_projective_boundary=True`,
- `empty_set_not_projective_boundary=True`,

and checks the flux exponent through the tautology `(k-1)+1==k`. It does not construct `Omega_9`, does not contract it, does not compute the projective tangent representative, and does not actually verify invariance under a different eliminated projective coordinate. Green CI therefore could not detect the projective-radial mistake.

Because an exact mathematical counterexample exists, the controlling review verdict is scientific failure rather than merely implementation invalidity.

## Scope retained

The following part survives and remains usable as a scoped geometric lemma:

`scalar projective blow-up Jacobian exponent = k-1`

for nonempty proper `Z`.

The following part is non-authoritative and must not be consumed by the 34-orbit physical flux audit:

`normal flux exponent = (k-1)+ord_t(v(t))`

for the raw ambient `v`.

The corrected projective/tangent normal component must instead be derived from

`u(t)=v(t)-tS/s1`.

For the actual confirmed degree-four annihilator, `S` is not known to vanish identically, so the omitted term is potentially substantive orbit by orbit.

## Source/order and claim firewalls

This failure occurs only in projective Schwinger geometry after the full source object has already been constructed. It does not change source ordering, the all-ten-wedge/full-32 object, the dual/covector authority, K3/K4 residue results, the published spectral `i epsilon`, or the 16-parameter meromorphic-family provenance.

Historical source-lock-invalid Iter077E/F remain quarantined under `status/ITER077_CONTACT_FORMULA_ERRATUM.md`.

No physical K5 corner classification, integrated Stokes/IBP relation, period zero/nonzero theorem, finite-part selector, regulator-independence theorem, F9/G3/G8 promotion, `NEW_PHYSICS_FOUND`, or complete-QG claim follows from this review.

## Verdict

**`SCIENTIFIC_FAIL_CONFIRMED`**

The Researcher classification is false as stated because its universal normal-flux identity uses the wrong representative of the projective vector-field class. The scalar Jacobian sub-result survives.

## Authorized next gate

Do not rewrite the failed gate. The correction changes the mathematical object entering the flux from raw `v(t)` to projective/tangent `u(t)=v(t)-tS/s1`, so a **new prospectively preregistered successor gate** is required before the 34-orbit physical action-flux audit may use a normal-flux exponent.

Recommended successor:

`K5_SCHWINGER_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING`

It must derive the blow-up flux directly from `Omega_9=i_E Vol` and/or the simplex-tangent representative `u`, verify invariance under `v -> v+fE`, retain the confirmed scalar `t^(k-1)` Jacobian, and include `v=E` as a mandatory zero-flux control. Only after terminal valid production and independent review may the 34-orbit physical numerator/action-flux valuation audit resume substantive corner classifications.

The independent constant-`2x2` action repair/retry may continue because it does not depend on this boundary-flux sub-gate.
