# Exact causal-vertex orientation provenance supplement

**Date:** 2026-09-13

**Purpose:** freeze the primary-source facts needed for Iter076N. This note does not promote physical signed P3 and does not alter the terminal classifications of Iter076K-M.

## Primary sources

1. E. Bianchi, C. Chen, M. Gamonal, *Causal spinfoam vertex for 4d Lorentzian quantum gravity*, arXiv:2601.23162, Phys. Rev. D 113, 126020 (2026).
   - https://arxiv.org/abs/2601.23162
2. E. Bianchi, C. Chen, M. Gamonal, *Toller matrices and the Feynman i epsilon in spinfoams*, arXiv:2604.24945 (2026).
   - https://arxiv.org/abs/2604.24945
3. J. Engle, A. Zipfel, *The Lorentzian proper vertex amplitude: Classical analysis and quantum derivation*, arXiv:1502.04640.
   - https://arxiv.org/abs/1502.04640
4. C. E. Beltran, *Causal Structure for Generalized Spinfoams*, arXiv:2603.22661v2 (2026).
   - https://arxiv.org/abs/2603.22661

## Frozen exact facts from the causal vertex

For five vertex edges/tetrahedra labelled `a=1,...,5`, the source causal data are `sigma_a=+-1`, while the wedge branch entering the causal amplitude is only

`kappa_ab = sigma_a sigma_b`.

Global source reversal `sigma_a -> -sigma_a` therefore leaves every exact wedge branch unchanged.

The fixed-causal vertex, source Eq. (4), is

`A_sigma[Psi] = int prod_(a=2)^5 dg_a prod_(a<b) T^(kappa_ab,gamma j_ab,j_ab)_(j_ab m_ba,j_ab m_ab)(g_b^-1 g_a)`

with `g_1=1`. The exact displayed kernel contains:

- four Haar measures on `SL(2,C)`;
- ten relative group elements `g_b^-1 g_a`;
- ten Toller functions;
- boundary spin/intertwiner magnetic contractions through the spin-network state.

It contains no displayed Levi-Civita tensor on the five tetrahedron labels, no determinant of five normal columns, no oriented 4-volume factor and no explicit alternating `S5` character.

Source Eq. (7) is a Cartan decomposition of the same Toller function,

`T(g)=sum_p D(U_1) t(beta) D(U_2)`.

It introduces no new simplex-label orientation object; it is a computational representation of the same exact group function.

## Semiclassical orientation is a different layer

The same causal-vertex paper explicitly distinguishes combinatorial causal data `sigma_a` from Regge causal data `s_a`; their relation arises only at the semiclassical level. On non-degenerate Lorentzian Regge boundary data, causal rigidity selects the compatible saddle and a single Regge exponential.

Iter076L already established that oriented Regge four-volume has the required pseudoscalar character. Iter076M established that the exact integration-variable set admits the non-degenerate candidate

`Omega_sigma(g) = sgn det([1; sigma_a F_a])`, `F_a = ghat_a T`.

Those results prove availability/semiclassical compatibility, not occurrence in source Eq. (4)/(7).

## Proper-vertex comparison guardrail

The Lorentzian proper vertex uses an additional orientation/sector-selection construction (including orientation-sensitive epsilon/determinant data in its classical analysis) to eliminate unwanted sectors. This is evidence that an orientation selector can be added/derived in a related spin-foam construction; it is not evidence that the Bianchi-Chen-Gamonal Eq. (4) contains that selector.

## Generalized-spinfoam guardrail

For a five-valent causal graph, arXiv:2603.22661 discusses reconstruction of edge time orientations from wedge orientations up to global information. In particular, products of edge orientations can distinguish certain reconstruction choices. Such a product is permutation-even and is not by itself the alternating `S5` pseudoscalar required by the Iter076H Hodge sign line.

## Iter076N question

The only admissible promotion criterion is source provenance:

> Does the exact Eq. (4)/(7) amplitude, including its boundary intertwiner/magnetic contractions and allowed source ordering/orientation data, contain or uniquely force an `S5`-odd, proper-Lorentz-gauge-invariant, global-causal-reversal-invariant selector equivalent to `Omega_sigma(g)` on the non-degenerate locus?

Mere constructibility from `(g_a,sigma_a)` is insufficient.
