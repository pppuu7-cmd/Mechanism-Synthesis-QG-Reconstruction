# Prospective preregistration — K5 Schwinger projective blow-up normal-flux scaling

Status: FROZEN BEFORE DERIVATION/IMPLEMENTATION.

## Question
Fix a nonempty proper edge subset Z of K5, k=|Z|, in the positive projective Schwinger simplex. Under the simultaneous boundary blow-up alpha_e=t beta_e for e in Z, derive from the projective form itself (not by inserting a guessed Jacobian power) the exact t-power contributed by the projective normal measure and by contraction with a face-tangent logarithmic vector field v_e=alpha_e q_e(alpha).

This is a geometry sub-gate required by the already-frozen 34-orbit physical numerator/action-flux audit at prereg commit b6580a731c88027dc568672840c4c77333ff7c16. It does not classify any physical K5 corner.

## Frozen conventions
- Work on the positive projective simplex sum_e alpha_e=1, dimension 9.
- Z is nonempty and proper; Z=empty and Z=E(K5) are controls, not physical projective boundary faces.
- Let t=sum_{e in Z} alpha_e and beta_e=alpha_e/t, so sum_{e in Z} beta_e=1.
- Use the standard projective Schwinger form Omega_9 restricted to sum alpha=1, equivalently the induced Lebesgue form in any affine chart, and show chart-equivalent valuation.
- v_e=alpha_e q_e with polynomial q_e; no singular vector fields are allowed in this sub-gate.

## Frozen checks
1. Derive the Jacobian of the change from the k coordinates alpha_Z to (t,beta_1,...,beta_{k-1}) exactly.
2. Prove the scalar projective measure contributes t^(k-1) dt times a nonzero angular form on the relative interior of the blown-up face.
3. Let t=sum_Z alpha_e. Derive v(t)=sum_{e in Z} alpha_e q_e and prove its valuation is at least t^1 for polynomial q_e.
4. Pull back i_v Omega_9 to t=epsilon and derive the normal-flux measure power, explicitly separating the t^(k-1) geometric Jacobian from the valuation of v(t).
5. Verify k=1 directly in an affine chart.
6. Verify invariance under choosing a different eliminated projective coordinate outside Z.
7. Malformed controls inserting k instead of k-1 for the scalar Jacobian, or treating Z=E(K5) as a projective boundary, must be rejected.

## Frozen classifications
Only one of:
- K5_PROJECTIVE_BLOWUP_NORMAL_FLUX_SCALING_DERIVED_EXACT_SCOPED
- INVALID_GATE

## Claim firewall
No numerator valuation, no corner-vanishing theorem, no integrated Stokes/IBP relation, no K5 period value, no finite-part selector, and no F9/G3/G8 or NEW_PHYSICS_FOUND claim follows from this geometry sub-gate alone.
