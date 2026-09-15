# Iter083L source lock — causal/Toller formulas versus joint-K5 renormalization data

Date: 2026-09-15
Status: PRIMARY-SOURCE FORMULA LOCK

## Primary sources audited
1. E. Bianchi, C. Chen, M. Gamonal, “Causal spinfoam vertex for 4d Lorentzian quantum gravity”, arXiv:2601.23162, especially Eqs. (3)–(4).
2. E. Bianchi, C. Chen, M. Gamonal, “Toller matrices and the Feynman i epsilon in spinfoams”, arXiv:2604.24945, especially the one-wedge Feynman projector construction.

## Direct formula facts
The causal paper Eq. (3) defines one Toller matrix by

`T^(+-)(g) = lim_(epsilon->0+) integral d rho_tilde [one spectral pole kernel] ... D^(rho_tilde)(g)`.

Thus the published epsilon is a one-wedge spectral prescription in one integration variable `rho_tilde`.

Eq. (4) subsequently defines the K5 vertex by

`integral prod_(a=2)^5 dg_a  prod_(a<b) T_ab(g_b^-1 g_a)`.

There are ten Toller factors. The one-wedge limit in Eq. (3) is part of each Toller definition before Eq. (4) forms the product.

The companion paper develops the same one-wedge spectral projection in detail. It does not introduce a ten-variable analytic collision regulator for the K5 product.

The causal paper explicitly distinguishes Wigner D matrices, which are Lorentz-group representations, from Toller T matrices, which are polynomially bounded functions on SL(2,C). Hence no representation multiplication law is available that turns the ten-factor product into a source-defined joint extension prescription.

## Objects absent from the published K5 definition
The audited source formulas do not define any of the following as part of the causal K5 vertex:

- edgewise collision-analytic parameters `s_e=1+x_e`;
- a ten-dimensional regulator-parameter space carrying a metric Q;
- a Q-dependent polar/holomorphic projection `pi_Q`;
- a forest pole form `L_B=sum_(e internal B) x_e` as source data;
- the condition `Q*(L_B,e_external)=0`;
- a joint K3/K4/K5 finite-part/subtraction map;
- a common K5 collision regulator/limit;
- a K5 gluing/composition normalization selecting supported extension coefficients.

This conclusion follows from the direct type/content of the published formulas, not merely from a keyword search.

## Relation to repository results
Iter083E establishes that one-wedge analytic uniqueness does not lift to the joint extension selector.

Iter083F establishes that even deliberately retaining one common finite spectral epsilon across all ten wedges does not regularize the common collision.

Iter083J and Iter083K prove conditional mathematical uniqueness of the Euclidean Q ray under stronger factorization/locality assumptions, but those assumptions are not stated in the audited causal/Toller source definition.

## Scope
This audit does not prove that no physically justified forest-locality, composition, microlocal naturality or RG principle can exist. It proves only that such a bridge is additional to the presently audited published causal/Toller formula set.