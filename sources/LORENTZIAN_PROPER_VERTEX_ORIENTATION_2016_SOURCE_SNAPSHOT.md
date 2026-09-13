# Primary-source snapshot — Lorentzian proper vertex orientation structure (2016)

**Acquired:** 2026-09-13  
**Purpose:** provide equation-level provenance for the orientation/pseudoscalar object explicitly requested by the Iter076K blocker. This source is used only as an additional EPRL/proper-vertex authority and does not retroactively alter earlier frozen iterations.

## Immutable bibliographic authority

Jonathan Engle and Antonia Zipfel, **“The Lorentzian proper vertex amplitude: Classical analysis and quantum derivation”**, *Phys. Rev. D* **94**, 064024 (2016), arXiv:`1502.04640`.

Primary source:
- https://arxiv.org/abs/1502.04640
- https://doi.org/10.1103/PhysRevD.94.064024

The 2026 causal-spinfoam paper of Bianchi, Chen and Gamonal explicitly cites the proper-vertex line and states that clarifying the relation to the proper vertex, where a 4-volume-orientation constraint selects a single critical point, is an open direction. This snapshot records only source equations relevant to that orientation structure.

## SL(2,C) action and canonical time normal — Eqs. (2.3)–(2.4)

The source uses the standard double-cover map `X -> Xhat in SO+(3,1)` and the canonical future unit timelike vector

`T = (1,0,0,0)`.

For boundary areas `A_ab`, tetrahedral face normals `n_ab`, and group elements `X_a in SL(2,C)`, the reconstructed bivectors are

`B_ab = - A_ab Xhat_a ▷ [ T ∧ (0,n_ab) ]`.

Thus the vectors

`F_a := Xhat_a T`

are source-defined future-pointing 4-vectors in the common 4-simplex frame.

## Geometric tetrahedron normals — Eq. (2.8)

For a reconstructed non-degenerate 4-simplex, the outward tetrahedron normal satisfies

`N_a = ± F_a = ± Xhat_a T`,

with the sign chosen separately for each tetrahedron so that `N_a` is outward pointing. The paper later denotes these relative signs by `epsilon_a` in the proof of Lemma 4.

The source also notes the common-left equivalence `X_a -> Y X_a`: this only performs an overall proper Lorentz transformation. Since `Yhat in SO+(3,1)` has determinant `+1`, oriented 4-vector contractions with the spacetime Levi-Civita tensor are invariant under this common gauge action.

## Dynamical orientation — Eq. (2.21)

The source defines the dynamical orientation of the reconstructed continuum Plebanski 2-form by

`omega(B) = sgn( epsilon^{alpha beta gamma delta} epsilon_{IJKL} B^{IJ}_{alpha beta} B^{KL}_{gamma delta} )`.

It is explicitly orientation-sensitive: under parity reversal of the numbered 4-simplex, the paper derives `omega -> -omega`. The Plebanski-sector sign `nu` also flips, while their product is the sector variable relevant to the Einstein–Hilbert restriction.

## Proper-vertex pair sign beta_ab — Lemma 4

For Regge-like non-degenerate data, the paper introduces

`beta_ab = sgn[ epsilon_ijk (Xhat_ac T)^i (Xhat_ad T)^j (Xhat_ae T)^k * epsilon_lmn (Xhat_bc T)^l (Xhat_bd T)^m (Xhat_be T)^n ]`,

where `{c,d,e}` are the three labels complementary to `{a,b}`. The ordering of `{c,d,e}` is arbitrary because both triple products acquire the same sign under a reorder.

In the proof, `beta_ab` is related to a **product of two four-dimensional oriented contractions**,

`epsilon(Xhat_b T, Xhat_c T, Xhat_d T, Xhat_e T) * epsilon(Xhat_a T, Xhat_c T, Xhat_d T, Xhat_e T)`,

and the paper obtains `beta_ab = -epsilon_a epsilon_b` (with its conventions).

This is important for MSQGR provenance: the source contains explicit single Levi-Civita contractions of four `Xhat_a T` vectors, while the published `beta_ab` uses them only through an orientation-even product. Therefore `beta_ab` by itself need not retain the global orientation bit carried by one unsquared contraction.

## Einstein–Hilbert restriction and quantum projector — Eqs. (2.29), (4.1)

The source derives the Einstein–Hilbert-sector condition

`beta_ab * tr( sigma_i X_ab X_ab^dagger ) * n_ab^i > 0`,

and quantizes it with the positive-spectrum projector

`Pi_ab = Pi_(0,infinity)( beta_ab * tr(sigma_i X_ab X_ab^dagger) * Lhat^i )`.

This is the proper-vertex mechanism that removes the unwanted semiclassical branch. It is not being imported into the causal vertex as an assumption here; it is used only as source evidence for which orientation-sensitive contractions are legitimate EPRL/proper-vertex objects.

## Scope guard

This snapshot does **not** establish that the 2026 causal vertex contains the proper-vertex projector, that a candidate orientation sign is nonzero on the full integration domain, or that physical MSQGR P3 is established. It does not establish the source numerator/Jacobian, the nominal `epsilon^-1` coefficient, finiteness/divergence, F9, G3, G8, K5, a continuum limit, or new physics. Any derived orientation selector must be prospectively tested for source-variable dependence, relabeling covariance, common-gauge/root covariance, degeneracy controls, and compatibility with the Iter076H–K Hodge line before any promotion.
