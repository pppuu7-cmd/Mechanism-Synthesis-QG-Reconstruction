# Iteration 045 — correlated K3 finite-part covariance and epsilon-limit audit

Date: 2026-09-12

## Motivation
Iter044 established a nonzero polynomial quotient of degree 3 in the source-faithful joint K3 common-cycle spectral integrand, with a nonzero even t^2 term and predicted symmetric-cutoff R^3 growth. The next question is not whether another raw cutoff diverges, but whether subtracting exactly the polynomial quotient produces a mathematically canonical correlated finite part.

A development-only pilot at the already-consumed Iter044 point `(gamma,epsilon,signs,k1,k2)=(1.2,0.05,++-,0.37,-0.61)` indicated that a residue-defined finite part may agree when the redundant cycle is parameterized by q1, q2, or q3. That point is therefore excluded from the production acceptance set below. Production values are held out from that pilot.

## Frozen finite-part definition
For each equivalent cycle coordinate `u in {q1,q2,q3}`:

1. Express the same joint K3 rational spectral density in `u`, including the absolute Jacobian of the real-line reparameterization.
2. Perform exact polynomial division `K_u(u)=Q_u(u)+r_u(u)` with `r_u=O(1/u)`.
3. Define the symmetric Hadamard/PV finite part of the remainder by the exact upper-half-plane identity

   `FP_u = 2*pi*i*sum Res(r_u, upper poles) - i*pi*a_minus1`,

   where `a_minus1 = lim_{u->infinity} u*r_u(u)`.

This definition subtracts only the polynomial quotient forced by exact division; no fitted coefficient, arbitrary counterterm, or post-result tolerance is allowed.

## Stream A — held-out cycle-coordinate covariance
Production matrix:
- gamma `{0.35, 0.9, 1.7}`
- epsilon `{0.03, 0.11}`
- sign sectors `{+++, ++-, +-+, -++}`
- Fourier probes `(k1,k2)=(0.23,-0.47)`

Prospective PASS requires exact symbolic equality `FP_q1 == FP_q2 == FP_q3` after simplification and numerical relative spread `<1e-11`. A mismatch is a scientific negative result for this finite-part candidate, not an infrastructure failure.

## Stream B — independent kinematic holdout
Repeat the same exact covariance gate at `(k1,k2)=(-0.41,0.58)` for gamma `{0.55,1.35}`, epsilon `{0.04,0.13}`, and the same four sign classes. No retuning is allowed.

## Stream C — epsilon->0 diagnostic
For held-out `(k1,k2)=(0.23,-0.47)`, evaluate the coordinate-invariant candidate finite part at epsilon `{0.2,0.05,0.01,0.002}` for gamma `{0.35,0.9,1.7}` and sign classes `{+++,++-,+-+,-++}`. Record successive differences and the last-step change. This stream is diagnostic: it may establish convergence evidence or a negative trend, but does not by itself prove the distributional epsilon->0 theorem.

## Affine-contour guard
Record the polynomial quotient degree before subtraction. Because any nondegenerate affine reparameterization preserves the numerator-minus-denominator degree, a degree-3 polynomial sector cannot acquire absolute decay merely by shifting or tilting an otherwise rational contour. This is a structural guard, not a claim about more general non-affine or oscillatory prescriptions.

## Claim locks
Even a full PASS establishes only a promising mathematically canonical K3 finite-part candidate under the tested source-faithful j=1/2 spectral representation. It does not prove equality to the physical causal spinfoam vertex, forest consistency on K4/K5, RG closure, G3, F9, G8, or a new quantum-gravity theory. A PASS must be followed by forest/inclusion-exclusion compatibility and ordinary-EPRL recombination controls before any physical promotion.
