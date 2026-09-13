# Source/derived supplement — true causal-vertex B-map transversality input

**Date:** 2026-09-14

## Primary authority
Eugenio Bianchi, Chaosong Chen, Mauricio Gamonal, **“Causal spinfoam vertex for 4d Lorentzian quantum gravity”**, arXiv:2601.23162, Phys. Rev. D 113, 126020 (2026), DOI `10.1103/fwql-t4yr`.

Primary HTML checked on 2026-09-14: https://arxiv.org/html/2601.23162

This supplement freezes only source facts and an elementary local derivative needed for the next prospective gate. It does not establish a vertex finiteness theorem.

## Source-established facts

1. Eq. (16) writes the coherent-state causal vertex as four gauge-fixed `SL(2,C)` group integrations with one Toller matrix for each of the ten wedges.
2. Eq. (17) writes each coherent Toller matrix as an integral over an auxiliary projective spinor `z in CP^1`; the exact distributional factor is

   `theta(kappa B(z,g)) + kappa delta^(rho,j)(B(z,g))`.

3. Appendix C Eq. (32) defines

   `B(z,g) = log(<g^dagger z|g^dagger z>/<z|z>)`,

   a real-valued function invariant under projective rescaling of `z`.
4. Appendix D Eqs. (35)-(39) derive the same distributional factor from the published spectral Feynman `i epsilon` prescription.
5. The ten auxiliary spinors are wedge-local integration variables. No source equation identifies them with one common normal direction.

These facts are also consistent with the existing repository snapshots `sources/CAUSAL_SPINFOAM_VERTEX_2026_SOURCE_SNAPSHOT.md` and `sources/CAUSAL_SPINFOAM_VERTEX_2026_TOLLER_RESTRICTOR_SADDLE_ORIENTATION_SNAPSHOT.md`.

## Exact local derivative at the common group collision

Gauge-fix node `0` and write the four non-root group variables along Hermitian boost coordinates

`g_a(x_a) = exp[(x_a . sigma)/2]`,  `a=1,...,4`,  `x_a in R^3`,  `x_0=0`.

For wedge `e=(ab)`, `g_ab=g_b^(-1) g_a`. Define the projective Bloch vector

`n_ab^i = <z_ab|sigma_i|z_ab>/<z_ab|z_ab>`.

At `x=0`, direct differentiation of source Eq. (32) gives

`d B_ab = n_ab . (d x_a - d x_b)`.

Hence the boost block of the true ten-component source differential is the `10 x 12` matrix

`J_(ab),(c,i) = (delta_ac - delta_bc) n_ab^i`,

with root-column contributions omitted because `x_0=0`.

At the common group collision, compact first-order directions do not change `B` because unitary `g` has `g^dagger g=1`, and spinor variations do not change `B` at `g=1` because `B(z,1)=0` identically. Therefore this boost block is the full first differential relevant to rank at that locus.

## Scope firewall

- The scalar K5 incidence matrix is recovered only in the special collinear case `n_ab=n` for every wedge; it is not source-established as the generic differential.
- A full-rank witness for `J` would establish local transversality of the ten `B_ab` only near that source point. It would not by itself prove global integrability or regulator independence.
- Rank-deficient points remain admissible and must be analyzed separately.
- No physical source-to-K4 pushforward, nominal `epsilon^-1` coefficient, finiteness/divergence theorem, G3/F9/G8/K5 promotion, complete-QG claim or new-physics claim follows from this supplement.