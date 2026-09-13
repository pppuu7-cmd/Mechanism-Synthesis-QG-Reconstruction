# Primary-source snapshot — exact off-saddle Toller spinor support

**Acquired:** 2026-09-13  
**Purpose:** freeze the exact source facts needed to test whether finite-spin Toller support globally fixes the Iter076M orientation pseudoscalar away from stationary points.

## Authority

Eugenio Bianchi, Chaosong Chen, Mauricio Gamonal, **“Causal spinfoam vertex for 4d Lorentzian quantum gravity”**, arXiv:`2601.23162`, *Phys. Rev. D* **113**, 126020 (2026).

Primary text: https://arxiv.org/html/2601.23162

## Exact coherent-spinor integration structure

For the coherent boundary-state representation, the source introduces one auxiliary projective spinor `z_ab` per wedge. Eq. (12) writes the EPRL coherent integral with

`integral prod_{a=2}^5 dg_a integral prod_{ab} dOmega_ab exp(i S)`.

Eq. (16) writes the causal vertex as a product of one coherent-basis Toller matrix per wedge, and Eq. (17) gives each such Toller matrix as its own `CP^1` spinor integral. Therefore the ten wedge spinors are independent integration variables before stationary-point conditions correlate their critical values.

## Exact Toller bulk restriction

For one wedge the exact Eq. (17) factor is

`theta(kappa * B(z,g)) + kappa * delta^(rho,j)(B(z,g))`,

where `kappa=sigma_a sigma_b` and Appendix C Eq. (32) gives

`B(z,g) = log( <g^dagger z|g^dagger z> / <z|z> )`.

The distributional term is supported at `B=0`; the open bulk selected by the Heaviside factor is `kappa * B > 0`.

## Exact linear-algebra consequence to be tested prospectively

For fixed `g in SL(2,C)`,

`exp(B(z,g)) = (z^dagger (g g^dagger) z)/(z^dagger z)`

is the Rayleigh quotient of the positive Hermitian matrix `H=g g^dagger`.

Because `det(g)=1`, `det(H)=1`. If `g` is non-unitary, `H != I` and its two positive eigenvalues are reciprocal:

`lambda_max > 1 > lambda_min > 0`, `lambda_max lambda_min = 1`.

Consequently the exact bulk contains projective spinors with `B>0` and projective spinors with `B<0` for the same non-unitary group element. For `g in SU(2)`, `H=I` and `B=0` for every spinor, so only the boundary distribution can contribute.

This consequence is elementary linear algebra applied to the exact source formula; it is not asserted by the source as a new physical theorem. It is frozen here as the mathematical basis of the next prospective gate.

## Multi-wedge implication under test

Since the ten `z_ab` are independent integration variables, if every relative element `g_b^-1 g_a` is non-unitary then, wedge by wedge, one can in principle choose the sign of `B_ab` required by any fixed source-factorizable causal pattern `kappa_ab=sigma_a sigma_b`.

The next gate must explicitly verify that this remains true for all ten wedges in group configurations with opposite nonzero values of the Iter076M `Omega_sigma`, using the same fixed causal assignment. Only then may one conclude that the **bulk support alone** does not globally fix orientation off saddle.

## Scope guard

A support-overlap result does not prove that the full integrated amplitudes of the two orientation sectors are equal or both nonzero after phases, damping factors, intertwiner contractions and integration. It proves only that the Heaviside support restriction by itself is not a global `Omega_sigma` projector.

No generic finite-spin signed P3, numerator/Jacobian coefficient, finiteness/divergence theorem, F9/G3/G8/K5 promotion, complete-QG claim, or new-physics claim follows from this snapshot.
