# Toller front-face nonscalar coefficient supplement

Date: 2026-09-13

## Closed inputs

- Iter076V: the gamma-simple branch has leading singular order `beta^(-(2j+1))` with invertible magnetic leading matrix `C_z`, and radial relative boost one-jet `i gamma J_n`.
- Iter076W: all six pure Lie-generator directions at every integrated source node are killed after exact boundary-intertwiner contraction.
- Iter076X: the leading matrix family over boost normals,
  `C_n=D^j(U_n) C_z D^j(U_n)^(-1)`, has a nontrivial transverse angular connection surviving `5/7` frozen exact intertwiner controls.
- Iter076Y: a concrete mixed compact/boost source path feeds that connection at first subleading radial order with exact half-angle coefficient.

## Front-face leading coefficient after radial power extraction

For a wedge of spin `j`, extracting only the universal radial power gives

`beta^(2j+1) T(g) -> C_n`

as the boost-normal direction `n` is held fixed while `beta->0+`, up to a nonzero branch/spin scalar already irrelevant to the relative connection.

Thus the radial power strip does **not** produce one direction-independent scalar coefficient. It leaves a matrix-valued front-face function `n -> C_n`.

For a source node with four incident wedges and invariant intertwiner `i`, define the leading outgoing boundary tensor

`F_n := i [tensor_e C_{j_e,n}]`.

Using compact covariance and intertwiner invariance,

`F_n = F_z [tensor_e D^{j_e}(U_n)^(-1)]`

with

`F_z := i [tensor_e C_{j_e,z}]`.

Therefore for an infinitesimal rotation of the normal about the `y` axis,

`dot F = -i F_z [sum_e J_y^(e)]`

(up to the convention for Hermitian versus anti-Hermitian generators).

## Exact magnetic-sector obstruction to scalar flattening

Every original invariant tensor has support only at total magnetic number `M=sum_e m_e=0`. Because every `C_{j,z}` is diagonal, `F_z` also has support only in the `M=0` sector.

A scalar direction-dependent renormalization `s(n)` changes the first angular derivative by

`dot(s F)=dot s F_z + s dot F`.

The first term remains entirely in `M=0`.

By contrast, the `J_+` and `J_-` components of `dot F` lie in the disjoint total-magnetic sectors `M=+1` and `M=-1`. Hence whenever either ladder component is nonzero, **no scalar choice of `s(n)` can cancel the angular derivative**.

Iter076X's frozen exact census gives:

- two `(1/2,1/2,1/2,1/2)` controls: `J_+ F_z=J_- F_z=0`;
- the remaining five controls: both `J_+ F_z` and `J_- F_z` are nonzero.

Thus in exactly `5/7` frozen controls, the front-face direction dependence cannot be removed by any scalar normalization, even one allowed to depend on `n`.

## Matrix-valued trivialization versus scalar numerator jet

A matrix-valued frame can of course trivialize `C_n` locally, for example by retaining the `D(U_n)` factors. But such a frame carries the nontrivial connection already isolated in Iter076X-Y. Therefore replacing `C_n` by a scalar Taylor numerator discards source data.

The correct local object is at least a bundle-valued / blown-up boundary coefficient over the sphere of boost-normal directions. It is not, generically, a scalar smooth coefficient on the unblown group identity.

## Consequence for the earlier P4 language

Earlier iterations referred provisionally to a source numerator/Haar-Jacobian quadratic jet in ordinary reduced coordinates. The present chain shows that, before any source-to-K4 pushforward, the individual causal Toller branch already carries a non-scalar front-face coefficient after its universal radial power is extracted.

Therefore a scalar ordinary Taylor-jet formulation of the branch numerator is not source-faithful in generic spin/intertwiner sectors. The degree-two/`epsilon^-1` problem must first be reformulated with the relevant blown-up/polyhomogeneous boundary data, while keeping the smooth even Haar factor as a separate multiplier.

## Scope firewall

This supplement does not construct the full blow-up calculus, the full ten-wedge correlated front face, the physical source-to-K4 pushforward, or the `epsilon^-1` coefficient. It establishes only the exact obstruction to reducing the source front-face coefficient to scalar directional data in the frozen generic controls.