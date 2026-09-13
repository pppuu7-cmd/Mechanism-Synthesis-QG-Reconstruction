# Causal-vertex Toller one-jet source snapshot

**Date:** 2026-09-13

**Purpose:** freeze the exact published formulas used by Iter076T. This note distinguishes a local/source wedge one-jet witness from the still-unproved one-jet of the fully contracted/integrated causal vertex.

## Primary sources

1. E. Bianchi, C. Chen, M. Gamonal, *Causal spinfoam vertex for 4d Lorentzian quantum gravity*, arXiv:2601.23162, Phys. Rev. D 113, 126020 (2026).
   - https://arxiv.org/abs/2601.23162
2. E. Bianchi, C. Chen, M. Gamonal, *Toller matrices and the Feynman i epsilon in spinfoams*, arXiv:2604.24945, Phys. Rev. D 114, 046014 (2026).
   - https://arxiv.org/abs/2604.24945

## Exact causal vertex

For fixed causal edge data `sigma_a`, source Eq. (4) is a four-group integral of ten Toller functions with wedge branch

`kappa_ab = sigma_a sigma_b`.

In the coherent-spinor representation, source Eq. (17) writes a causal Toller matrix element as

`T^(sigma,rho,j)(g) = const * int_CP1 dOmega(z,g) * Theta_(sigma,rho,j)[B(z,g)] * exp(i rho B(z,g)) * exp(i j Phi(z,xi,zeta,g)) * exp(-j Q(z,xi,zeta,g))`,

where

`Theta_(sigma,rho,j)[B] = theta(sigma B) + sigma delta^(rho,j)(B)`.

The contact distribution is supported at `B=0`; away from contact, inside the appropriate open causal region, the branch factor is simply the Heaviside value multiplied by the regular phase/amplitude factors.

The source definitions are

`B(z,g) = log(<g^dagger z|g^dagger z>/<z|z>)`,

with `Phi` real phase and `Q >= 0` real.

Appendix D isolates `exp(i rho B)` as the only rho-dependent part of the coherent Wigner integrand before application of the Feynman/Toller projector.

## Exact reduced gamma-simple formula

Source Eq. (9) gives, for the lowest-spin block `k=j=l`,

`t^(+/- , gamma j,j)_(j j m)(beta)`

as an exponential times a Gamma-function coefficient and a Gauss hypergeometric function at `exp(-2 beta)`.

For the exact specializations

- plus branch: `j=1/2`, `m=+1/2`, `rho=gamma/2`;
- minus branch: `j=1/2`, `m=-1/2`, `rho=gamma/2`;

the hypergeometric identity `2F1(2,b;b,z)=(1-z)^(-2)` and Gamma recurrence reduce the published formula exactly to

`t_plus(beta) = - exp(+i rho beta) / [2 (rho^2+1/4) sinh(beta)^2]`,

`t_minus(beta) = - exp(-i rho beta) / [2 (rho^2+1/4) sinh(beta)^2]`.

Therefore the pole-removed quantities

`u_plus(beta) = sinh(beta)^2 t_plus(beta)`,

`u_minus(beta) = sinh(beta)^2 t_minus(beta)`

obey

`u_plus'(0) = - i rho / [2 (rho^2+1/4)]`,

`u_minus'(0) = + i rho / [2 (rho^2+1/4)]`.

For real `rho != 0` these one-jets are exactly nonzero.

## Haar relation

The source-domain radial Haar/KAK factor was independently frozen in Iter076D. Its normalized local factor is even,

`(sinh beta / beta)^2 = 1 + beta^2/3 + 2 beta^4/45 + ...`,

so its one-jet vanishes. Equivalently, the raw radial `sinh(beta)^2` factor cancels the displayed `1/sinh(beta)^2` singularity in the exact extremal `j=1/2` branch above and exposes the nonzero phase one-jet rather than cancelling it.

## Scope guard

This exact low-spin wedge witness establishes that neither the causal Toller branch nor the Haar radial factor provides a universal zero-one-jet theorem.

It does **not** establish:

- the one-jet of the full ten-wedge product after correlated collision geometry;
- cancellation/non-cancellation after magnetic sums and the five intertwiner contractions;
- the one-jet after the four `SL(2,C)` group integrations;
- the actual nonlinear source-to-K4 pushforward curvature;
- the physical degree-two coefficient or nominal `epsilon^-1` coefficient.

Those remain separate provenance questions.
