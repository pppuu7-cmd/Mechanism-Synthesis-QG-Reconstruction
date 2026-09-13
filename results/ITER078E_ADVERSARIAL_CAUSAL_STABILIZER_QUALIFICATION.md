# Iter078E-RG adversarial qualification — full 32-dimensional componentwise extension space is reduced by fixed-causal relabeling stabilizers

**Date:** 2026-09-14

## Reviewed authority

- preregistration: `prereg/ITER078E_RG_MINIMAL_EXTENSION_COUPLING_SPACE.md`, commit `1a5cbc1704f3e9b28539d46f974f4aa815924d78`;
- source/theorem derivation: `sources/ITER078E_RG_MINIMAL_EXTENSION_COUPLING_SPACE_DERIVATION.md`, commit `d6e0b31d9bc32b4a04eb060d4f314de7a7780e92`;
- result: `results/ITER078E_RG_MINIMAL_EXTENSION_COUPLING_SPACE_RESULT.md`, commit `f9a7e264a0747e3fbb809a2130b6729361b6ec31`.

Research classification reviewed:

`ITER078E_RG_INTEGRATED_EXTENSION_THEORY_SPACE_HAS_AT_LEAST_FULL32_ORDERZERO_BOUNDARY_DUAL_DIRECTIONS_EXACT_THEOREM_SCOPED`.

## What survives review exactly

Iter077L's extension theorem is linear and applies componentwise to the 32 scalar boundary components. Before imposing additional source symmetries, the construction

`Delta A_ell(Psi) = ell(Psi) delta_N`, `ell in H_B^*`,

indeed supplies a 32-dimensional order-zero **unconstrained componentwise extension space** in the all-`j=1/2` boundary sector. `delta_N` has transverse scaling degree 12, below the source object's maximal degree 20, so these terms do not increase the frozen maximal scaling degree.

Global common-left `SL(2,C)` gauge invariance also does not by itself identify the boundary-dual coefficients.

## Missing source-covariance condition in the Researcher result

The stronger step from the unconstrained 32-dimensional extension space to a 32-dimensional **source-compatible fixed-causal theory space** omitted the automorphism stabilizer of the causal-labelled 4-simplex.

The source Eq. (4), as frozen in `sources/CAUSAL_SPINFOAM_VERTEX_2026_SOURCE_SNAPSHOT.md`, has five dummy simplex-node labels, ten all-pairs wedges, relative elements `g_b^-1 g_a`, causal wedge signs `kappa_ab=sigma_a sigma_b`, and the full boundary spin-network data. Undoing the root gauge fixing, simultaneously permuting node labels, group variables, spins/intertwiners and `sigma_a`, and then re-fixing a root is a relabelling of the same source object.

In the frozen all-equal-spin sector, any node permutation that preserves the causal sign partition leaves the fixed causal pattern itself unchanged. For `p` nodes carrying one sign and `5-p` the other, the stabilizer contains

`G_p = S_p x S_(5-p)`.

For such a stabilizer element, relabeling covariance is no longer merely a map between differently labelled causal data: it is an automorphism of the same fixed-causal boundary problem. A supported coefficient functional compatible with that source automorphism must therefore lie in the invariant subspace of the induced boundary-dual representation.

This is the case that Iter078E Lane C did not distinguish from a generic simultaneous relabeling.

## Independent exact boundary-representation control

A retrospective deterministic critic control was implemented in

`distributional/iter078e_critic_boundary_stabilizer.py`, commit `69090a034f883f4c4d08fbf5c422ba3ca63e63a8`,

and run in six independent matrix lanes by

`.github/workflows/iter078e_critic_boundary_stabilizer.yml`, production head `4be41872dba8c39930f500b9b54e322547cd1cd3`.

Terminal run: `34790682104`, completed success. CI success is used only as execution provenance; the scientific interpretation is here.

The control uses exactly the stripped `j=1/2` invariant node tensors frozen in Iter077I/J/N. It reconstructs, over exact rational arithmetic, the 2x2 recoupling action induced by each node-leg permutation and then the exact 32x32 action on the five-node boundary basis. Adjacent transposition generators are independently checked to square to the identity.

For each causal partition the exact stacked rank of `(P-I)` gives the invariant-space dimension. Since the dual representation has the same multiplicity of the trivial representation over characteristic zero, these dimensions also apply to invariant boundary covectors.

Exact terminal results:

| `p` | stabilizer | stacked rank | invariant dimension |
|---:|---|---:|---:|
| 0 | `S_0 x S_5` | 30 | 2 |
| 1 | `S_1 x S_4` | 29 | 3 |
| 2 | `S_2 x S_3` | 27 | 5 |
| 3 | `S_3 x S_2` | 27 | 5 |
| 4 | `S_4 x S_1` | 29 | 3 |
| 5 | `S_5 x S_0` | 30 | 2 |

Artifacts:

- `p=0`: `10328735363`, `sha256:0b16cb009e1b59c8ed1dda7bbbeac49e8ff3cbb98244f300122c67cc908fae5b`;
- `p=1`: `10327787892`, `sha256:4528cbcdfe9af7cbe730c1bad02a737cee5dcfd68fe9a148f549a1a42ed5d1b5`;
- `p=2`: `10327687033`, `sha256:4fd4be85955dc8dfdcdc8af1bfd428ed8ba260fc5af078df1d2ffc5812c1c6cd`;
- `p=3`: `10328476353`, `sha256:81ae05c678861affc29a5f57b927c4caf05c7658526ce65a70840362e979111b`;
- `p=4`: `10328386614`, `sha256:43777b85dff131a7c50a0a60232f66c6af11c85b239cdb5a03fde642cbf2a029`;
- `p=5`: `10328600977`, `sha256:048e03ce666c760c7e119f08ae908af9f2626d6c2c0437a56761cc7dbf647350`.

Global reversal `sigma_a -> -sigma_a` leaves `kappa_ab` unchanged, so the physical causal classes pair `p <-> 5-p`; the corresponding dimensions agree exactly as required: `2,3,5` for the three partition types.

## Adversarial consequence

The Researcher statement

`dim_C source-compatible ambiguity_image >= 32`

is not established and is false once the manifest fixed-causal relabeling stabilizer covariance of Eq. (4) is imposed in the same frozen boundary convention.

The correct scoped statement is two-level:

1. before source relabeling constraints, the componentwise order-zero extension space contains `H_B^*` and has dimension 32;
2. within the exact constant-in-`N`, all-`j=1/2` boundary-dual sector, imposing the fixed-causal stabilizer reduces the invariant subspace to dimension `2`, `3`, or `5` depending on the causal partition type.

Thus the one-scalar witness `A_0+cL` is **still not a complete symmetry-compatible truncation**: even after this source covariance is imposed, the currently allowed constant order-zero sector has more than one independent direction for every causal class. But the required lower bound is not 32.

## Scope ceiling

This control does **not** determine the full physical extension space.

- Additional source conditions could reduce the invariant order-zero subspace further.
- Normal derivatives through order 8 and nonconstant/distributional coefficient data along `N` can enlarge the total ambiguity beyond these finite-dimensional constant order-zero sectors.
- The exact dimensions above are for the frozen all-`j=1/2` recoupling basis and the causal-label stabilizer action induced by the repository's exact node tensors.
- They are not generic-spin coupling counts.
- No RG fixed point, unique extension, regulator independence, G3, continuum or complete-QG claim follows.

## Verdict

`QUALIFIED`

Accepted: `ITER078E_UNCONSTRAINED_COMPONENTWISE_ORDERZERO_EXTENSION_SPACE_CONTAINS_FULL32_BOUNDARY_DUAL_EXACT_SCOPED`.

Rejected as over-broad: a source-compatible fixed-causal lower bound of 32 independent order-zero couplings.

New exact source-covariant finite-spin fact: the fixed-causal stabilizer-invariant constant order-zero boundary-dual sector has dimensions `2/3/5` by causal partition class, so a one-coupling truncation remains insufficient but a 32-coupling lower bound is not justified.

## Next admissible gate

Before any refinement beta function, freeze the symmetry-compatible extension theory space, beginning with the exact `2/3/5` stabilizer-invariant order-zero sectors and then testing which normal-jet/tangential coefficient directions survive the same source automorphisms. In parallel, the higher upstream blocker remains the missing source-faithful causal 1-to-5 measure/embedding/projection/regulator map from Iter078A.

A future RG truncation must therefore solve **both** obligations prospectively:

- define the causal refinement map;
- define a symmetry-compatible projection/transport law for the actual residual extension space.

Do not use either one scalar `c` or an unreduced 32-vector as the physical coupling space without the corresponding reduction/closure theorem.