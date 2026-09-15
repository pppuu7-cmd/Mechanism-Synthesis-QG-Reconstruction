# K5 order-8 invariant-dual projective object / IBP reachability — terminal result

Date: 2026-09-16

## Authority

Prospective gate:

`prereg/K5_ORDER8_INVARIANT_DUAL_PROJECTIVE_PERIOD_IBP_NONCANCELLATION.md`, commit `4a92113d33addb7c00bcb294f35fa78c35e18691`.

Post-prereg derivation:

`sources/K5_ORDER8_INVARIANT_DUAL_PROJECTIVE_OBJECT_IBP_REACHABILITY_DERIVATION.md`, commit `14714804b462ae4e277e1da1162ed5079bc525ef`.

Validator:

`scripts/k5_order8_invariant_dual_projective_ibp_reachability.py`, commit `549d59013286220f834b32d2ab2c70d8214572da`.

Production:

- workflow/head: `6e21e36811131b6359a35cc80006685d477e4602`;
- run: `35036111528`, terminal `success`;
- job: `104605480618`, terminal `success`;
- artifact: `10423513476`;
- artifact ZIP digest: `sha256:e8a42e1affe58cb84ead79a001ce72b7abecf487d5f903224041edb45cd3bd69`;
- production JSON SHA256: `9a1d21e1a33a6d03349f855f963b42a0a85126426ea7e01d5004653c960a21f1`;
- status: `PASS_EXACT_SCOPED`;
- classification: `K5_INVARIANT_DUAL_PROJECTIVE_OBJECT_DEFINED_IBP_REDUCTION_INCOMPLETE_SCOPED`.

All 32 frozen implementation checks and all 16 adversarial controls passed.

## Exact object

The complete boundary S5 action was rebuilt from the authoritative stripped local node tensors rather than imported as a character literal. The local norms are

`||T_0||^2=4`, `||T_1||^2=12`, `T_0.T_1=0`.

The independently reconstructed boundary character is

`(32,0,8,2,0,0,2)`,

and the Reynolds projector has exact rank two. Because the stripped basis is not orthonormal, boundary amplitudes are projected with the dual action / `P^T`, not with `P`.

A deterministic invariant-dual RREF basis has pivots at boundary components `00001` and `00100`.

At the uniform Schwinger point, the complete all-32 order-eight contraction uses all `100000` source node-choice terms and all 945 Wick pairings before uniform sparsity. In the invariant-dual RREF basis the exact pointwise coordinates are

`(-9225216/9765625, -7175168/9765625)`.

Both are nonzero. This is only a pointwise reachability statement, not a period evaluation.

## Projective reduction

The exact K5 Kirchhoff polynomial is

`Psi_K5(alpha)=det L(alpha)`,

homogeneous degree four with exactly 125 spanning-tree monomials, each coefficient one.

For either invariant-dual scalar channel, the order-eight principal-symbol projective form can be written, up to one common nonzero source normalization, as

`Omega_9 * prod_e alpha_e^(1/2) * N_c(alpha) / Psi_K5(alpha)^(21/2)`,

with

- `deg N_c=27`;
- scalar-function homogeneity `-10`;
- projective-volume degree `+10`;
- total projective degree exactly zero.

For every edge face `alpha_e=0`, exactly 75 K5 spanning trees survive. Thus `Psi_K5` remains nonzero in the interior of each codimension-one Schwinger face, while the explicit factor `alpha_e^(1/2)` vanishes. Regular polynomial projective IBP vector fields therefore have zero codimension-one boundary contribution for the target integrand.

This does not authorize singular `1/alpha_e` fields or identify Schwinger faces with K3/K4 collision strata.

## IBP reachability result

The Euler/radial field yields only the tautological projective homogeneity identity

`sum_e d_e(alpha_e f)=0`.

No exact higher-degree projective IBP/syzygy system sufficient to decide either integrated invariant-dual period was established in this gate. Therefore the correct frozen outcome is

`K5_INVARIANT_DUAL_PROJECTIVE_OBJECT_DEFINED_IBP_REDUCTION_INCOMPLETE_SCOPED`.

The two integrated periods remain unknown. This is not a zero result and does not imply that exact reduction is impossible.

## Controls and ceiling

The validator rejects vector projection in place of dual projection, representative `00000` substitution, omitted edge, corrupted node normalization, wrong character/rank, wrong tree count, missing Schwinger half-weight, wrong denominator exponent, wrong numerator degree, non-projective degree, silent IBP boundary drop, promotion of common Schwinger scale to a physical regulator, pointwise-to-period promotion, and two-channel-to-full-tensor-zero promotion. Synthetic nonzero-period and exact-zero fixtures pass the same classifier.

No parent K5 zero/nonzero theorem, no complete 217-dimensional tensor result, no finite-part selector, no regulator-independence theorem, no G3/F9/G8 promotion, no `NEW_PHYSICS_FOUND`, and no complete-QG claim follows.

## Authorized successor

Classify the lowest-degree nontrivial regular face-tangent projective/logarithmic IBP fields for the exact K5 Kirchhoff polynomial before constructing a large numerator-specific IBP system. In particular, determine whether any S5-equivariant degree-two face-tangent logarithmic derivation exists beyond polynomial multiples of the Euler field. If none exists, same-denominator low-degree symmetric IBP is structurally exhausted and the next route must use higher degree, non-equivariant orbit systems, or explicitly audited denominator-shifting identities.