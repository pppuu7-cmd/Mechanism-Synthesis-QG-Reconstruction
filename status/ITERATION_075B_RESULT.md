# Iter075B — Toller wedge-order reversal source-authority audit

**Scientific classification:** `ITER075B_TOLLER_ORDER_REVERSAL_BLOCKED_SOURCE_LAW_NOT_ESTABLISHED`

## Authority

- Preregistration: `b73c6a9396715ee51629adda8403e4927ad214bc`
- Implementation: `007e2c776a078190a26b7ff09194026881aa79a4`
- Production head: `5268af0005165d3eae7186f03207ff87a42a7e70`
- Run: `34753179897`
- Job: `103713045234`
- Artifact: `10315658865` (`iter075b-source-audit`)
- Digest: `sha256:23143a335551347f5f88836f456616d911ccf87d3d83f158132fd1c08bd0ebe0`

## Frozen source audit outcome

The audited 2026 sources establish all of the following:

- Toller `T^(±)` are functions on `SL(2,C)` and are explicitly **not** representations (arXiv:2604.24945 Eq. 14);
- `T^(+) + T^(-) = D` (Eq. 15);
- the Wigner-D inverse identity is available for the unitary representation `D`;
- the causal vertex uses the wedge argument `g_b^-1 g_a` and the branch selector `kappa_ab = sigma_a sigma_b` (arXiv:2601.23162);
- global reversal of all edge orientations leaves `kappa_ab` unchanged.

The frozen audit did **not** find an explicit full-group branchwise Toller inversion / wedge-order-reversal law fixing branch map, index swap, conjugation, representation-label changes and phases. Therefore ordinary Wigner-D unitarity may not be transferred branchwise to Toller functions.

The negative control correctly rejects the unsupported inference `T^(kappa)(g^-1) = [T^(kappa)(g)]^dagger` when justified only by unitary representation properties of `D`.

## Scope

This is a source-law blocker, not a scientific failure of the causal vertex. It forbids promotion of tournament/positive-circulation geometry through edge reversal until an algebraic law is derived from the source Feynman representation or another authoritative formula. It does not imply divergence/finiteness, physical sector selection, or any K5/G3/F9/G8 promotion.
