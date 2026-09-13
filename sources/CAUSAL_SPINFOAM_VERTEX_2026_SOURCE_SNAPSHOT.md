# Primary-source snapshot — causal spinfoam vertex (2026)

**Acquired:** 2026-09-13  
**Purpose:** resolve the source-object blocker exposed by terminal Iter063B; this file is a new source input and does not retroactively change Iter063B.

## Immutable bibliographic authority

Eugenio Bianchi, Chaosong Chen, Mauricio Gamonal, **“Causal spinfoam vertex for 4d Lorentzian quantum gravity”**, arXiv:`2601.23162` (submitted 30 Jan 2026; arXiv text dated 22 Mar 2026), published as *Phys. Rev. D* **113**, 126020 (15 Jun 2026), DOI `10.1103/fwql-t4yr`.

Primary source:
- https://arxiv.org/abs/2601.23162
- https://doi.org/10.1103/fwql-t4yr

The statements below are a compact equation-level provenance snapshot, not a new MSQGR assumption.

## Source-defined causal data and ordered wedges

The source labels the five oriented edges of a single 4-simplex vertex by `a=1,...,5` and assigns edge orientations `sigma_a = ±1` (Eq. 2). For a wedge `(ab)`, the causal branch sign is

`kappa_ab = sigma_a sigma_b`.

For the EPRL kinematics the Lorentz representation is gamma-simple,

`(rho,k) = (gamma j_ab, j_ab)`,

and the relative group element attached to the ordered wedge is

`g_ab = g_b^{-1} g_a`.

These conventions are stated in Sec. II immediately before the source definition of the causal vertex.

## Source Toller object — Eq. (3)

The source defines the Toller functions by a Feynman `i epsilon` spectral integral,

`T^(±,rho,k)_{jm,ln}(g) = lim_{epsilon->0+} integral d(rho_tilde)/(2 pi i) [±1/(rho_tilde-rho ∓ i epsilon)] * [Gamma-ratio] * D^(rho_tilde,k)_{jm,ln}(g)`.

This fixes the physical spectral branch convention. It is not the MSQGR surrogate `beta+i*epsilon` and does not authorize arbitrary pole subtraction.

## Fixed-causal vertex — Eq. (4)

For a spin-network boundary state with ten spins `j_ab`, five intertwiners, and magnetic labels, the source defines

`<A_v^(sigma_a sigma_b) | Psi_{j_ab,m_ab}> = integral prod_{a=2}^5 dg_a prod_{1<=a<b<=5} T^(sigma_a sigma_b, gamma j_ab, j_ab)_{j_ab m_ba j_ab m_ab}(g_b^{-1} g_a)`.

The source gauge-fixes `g_1 = 1`. This is a direct four-`SL(2,C)` group integral with a ten-wedge product. Its definition contains no spanning-tree choice, no cycle-basis choice, and no sequential finite-part order.

## Exact EPRL control relation — Eqs. (5) and (6)

The source gives the exact additive identity

`T^(+,rho,k) + T^(-,rho,k) = D^(rho,k)`  (Eq. 5).

Consequently the ordinary EPRL vertex is the **unconstrained sum over independent wedge signs**,

`<A_v^EPRL| = sum_{kappa_ab=±1} <A_v^(kappa_ab)|`  (Eq. 6),

where the wedge signs in this control sum are independent. The source explicitly distinguishes this from the constrained sum induced by causal edge data `kappa_ab=sigma_a sigma_b`; summing causal structures does **not** reproduce the EPRL vertex.

This distinction is a hard guardrail for MSQGR: EPRL control is the 2^10 independent-wedge-sign sum, not the 16 causal classes modulo global reversal.

## Cartan / magnetic decomposition — Eq. (7)

For `g = U_1 exp(beta sigma_z/2) U_2`, the source writes

`T^(±,rho,k)_{jm,ln}(g) = sum_p D^j_{mp}(U_1) t^(±,rho,k)_{jlp}(beta) D^l_{pn}(U_2)`  (Eq. 7).

This is the source-backed bridge from the full group object to reduced Toller matrices used by numerical implementations.

## Scope guard

This snapshot establishes a source-defined object and its EPRL control relation. It does **not** establish finiteness, absolute integrability, a physical sector selected by K4 tournament geometry, F9, G3, G8, K5, a continuum limit, or new physics. Any computational use must be separately prospectively preregistered.
