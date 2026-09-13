# Iter078C-RG source/theorem derivation — supported ambiguity as SU(2) BF 15j channel

**Date:** 2026-09-14

Prospective contract: `prereg/ITER078C_RG_SUPPORTED_AMBIGUITY_BF15J_CHANNEL.md`, commit `bef22c39989905373c95bf49c666584dc898176e`.

## Vertex identification

Iter077M/N define the supported coefficient `F_SU2(y;Psi)` by restricting the actual boundary spin-network data to the compact common-collision locus `N=SU(2)^4` and contracting the ten spin-`j_ab` SU(2) matrices with the same five four-valent invariant intertwiners as the causal vertex.

On `N`, all relative compact holonomies have pure-gauge form `u_b^-1 u_a`. Gauge invariance of each four-valent node tensor removes the five node group elements (one already fixed), so the closed K5 evaluation equals the contraction obtained with all edge matrices equal to the identity.

In an orthonormal recoupling basis this contraction is, by the standard spin-network definition, the SU(2) `15j` 4-simplex vertex used in the Ooguri model of four-dimensional BF theory.

The Iter077I/N implementation used stripped integer node tensors only to obtain exact zero/nonzero certificates. Restoring the frozen nonzero node normalizations (`k=0` and `k=1` recoupling tensors) multiplies each 32-component boundary basis value by a nonzero basis normalization and, depending on graphical orientation, a nonzero phase/sign. Such changes do not alter the identification of the K5 invariant tensor or its zero/nonzero pattern.

Thus the exact Iter077N compact tensor is the all-`j=1/2` Ooguri/BF 15j tensor expressed in the repository's stripped recoupling convention.

## Multi-vertex pure-L sector

For each spin-foam vertex let `L_v` denote the supported compact ambiguity tensor after integration over the local common-collision submanifold. If a term in a multi-vertex expansion picks `L_v` at every vertex, then contracting shared tetrahedron intertwiner indices and summing internal SU(2) face spins/intertwiners with the standard BF resolution-of-identity/representation-dimension weights gives exactly the SU(2) Ooguri BF state sum on that subcomplex, up to:

- the overall local extension coefficient `c^V` for `V` vertices;
- basis-normalization conventions;
- the usual BF gauge-volume/flatness regularization factors.

This statement concerns the pure supported sector only. Mixed terms containing one or more Lorentzian causal-Toller gravitational vertices are not BF amplitudes.

## Pachner/refinement authority

Ooguri's four-dimensional SU(2) BF model uses the 15j vertex and is topological: its amplitudes satisfy the appropriate simplicial move identities after the standard treatment of gauge redundancy.

Bonzom-Livine-Speziale (arXiv:0911.2204) explicitly use Pachner invariance of the SU(2) 15j/Ooguri model to derive recurrence relations. They also emphasize the qualification relevant here: the naive four-dimensional `1->5` move contains redundant flatness delta functions and diverges by a gauge-volume factor (described as a `delta(I)^4`-type redundancy). A regularized/gauge-fixed version is required before assigning a finite numerical proportionality factor.

Therefore it is invalid to assert, without a regulator convention,

`Fine[L^5] = L`

with unit coefficient. The source-supported statement is instead schematically

`Fine[L^5] = K_BF(regulator,normalization) L`

in the pure BF channel, where the existence/topological character of the relation is known but the finite value of `K_BF` depends on handling the redundant gauge volume.

## Consequence for the extension coupling

A pure-sector one-parameter refinement equation would have the schematic form

`c L = c^5 K_BF L`,

or

`c = K_BF c^5`.

This demonstrates two points simultaneously:

1. refinement does not generically suppress the supported ambiguity tensor: it lies on a known topological BF channel;
2. once a regulator/normalization and the full coarse/fine equation are fixed, refinement may constrain/quantize its normalization rather than leaving it arbitrary.

No claim is made that this pure-sector equation is the RG equation of the full CRQN causal vertex. Mixed `A_0/L` terms, the Lorentzian causal sector, internal-spin convergence and projection back to a chosen theory space remain to be derived.