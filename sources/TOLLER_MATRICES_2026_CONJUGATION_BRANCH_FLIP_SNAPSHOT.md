# Primary-source snapshot — exact Toller conjugation branch-flip identities

**Acquired:** 2026-09-13  
**Purpose:** freeze the exact Toller identities relevant to the post-Iter076O question whether a parity/conjugation symmetry can act as a same-causal finite-spin orientation selector.

## Authority

Eugenio Bianchi, Chaosong Chen, Mauricio Gamonal, **“Toller matrices and the Feynman i epsilon in spinfoams”**, arXiv:`2604.24945`, *Phys. Rev. D* **114**, 046014 (2026).

Primary sources:
- https://arxiv.org/abs/2604.24945
- https://doi.org/10.1103/v3kc-4n3n

## Exact reduced Toller identities

The source derives the Toller matrices from the Feynman `i epsilon` projector and records exact conjugation/equivalence identities for real principal-series labels. In the source notation, Eq. (22) is

`conj(t^(+/- ,rho,k)_{j l m}(beta)) = (-1)^(j-l) t^(-/+ ,rho,k)_{l j,-m}(beta)`.

The same section also gives

`conj(t^(+/- ,rho,k)_{j l m}) = t^(+/- ,-rho,k)_{j l m}`

and equivalent relations involving `(-rho,-k)`.

For the gamma-simple lowest-spin block used by the causal EPRL vertex, `j=l=k` and `rho=gamma j`, so the branch-flip identity simplifies to

`conj(t^(kappa,gamma j,j)_{j j m}(beta)) = t^(-kappa,gamma j,j)_{j j,-m}(beta)`,

with `kappa=+/-1`.

Thus exact complex conjugation of a reduced gamma-simple Toller block changes the Toller causal branch sign.

## Exact causal K5 branch image

The causal vertex does not permit arbitrary independent wedge signs. Its source-defined wedge pattern is

`kappa_ab = sigma_a sigma_b`, `sigma_a in {+/-1}`,

on the ten edges of K5. Global `sigma -> -sigma` leaves all `kappa_ab` unchanged, so the 32 edge-sign assignments generate 16 distinct causal wedge patterns.

For every source-factorizable pattern and every triangle `(a,b,c)`,

`kappa_ab kappa_bc kappa_ca = +1`.

If every wedge branch is flipped, `kappa'_ab=-kappa_ab`, then on every triangle

`kappa'_ab kappa'_bc kappa'_ca = -1`.

Therefore the all-wedge branch-flipped pattern cannot equal `sigma'_a sigma'_b` for any source edge-sign assignment `sigma'`. This is an exact K5 factorization obstruction, not a numerical observation.

## Scope implication to be tested prospectively

The companion-paper conjugation identity is an exact statement about Toller blocks. Applied wedgewise, it flips every causal Toller branch. The resulting ten-wedge sign pattern lies outside the source-defined causal-edge image.

Consequently this identity does not automatically define a symmetry **within one fixed causal vertex amplitude** and cannot by itself be used to claim same-causal cancellation or projection between opposite `Omega_sigma` sectors.

This does not rule out a different exact parity transformation, a boundary-state transformation, or a nontrivial full-integral interference mechanism. Those possibilities require separate provenance.

## Claim guard

This snapshot does not establish a generic finite-spin signed P3, does not prove both `Omega` sectors survive full integration, and does not establish cancellation or non-cancellation of the exact causal vertex. It isolates only the branch-factorization obstruction for the known Toller conjugation identity.
