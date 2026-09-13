# Iter078C-RG preregistration — is the surviving supported ambiguity an SU(2) BF / 15j refinement channel?

**Date:** 2026-09-14

## Scientific question

Iter077N proves that the supported local ambiguity

`L(Psi) = integral_N F_SU2(y;Psi) delta_N`

survives as a nonzero integrated vertex functional. Is its boundary tensor, after restoring standard intertwiner normalizations, exactly the SU(2) Ooguri/BF 4-simplex vertex (`15j`), so that the pure-`L` multi-vertex sector is a known BF refinement channel rather than an arbitrary counterterm?

## Frozen authority

1. Iter077M/N definition of `F_SU2`: the compact K5 spin-network functional built from the same ten SU(2) spins and five invariant intertwiners, evaluated on pure-gauge compact relative holonomies.
2. Ooguri 4D SU(2) BF model / standard reviews: the SU(2) BF 4-simplex vertex is the evaluation of the K5 boundary spin network, i.e. the `15j` symbol in a chosen recoupling basis.
3. Standard Ooguri/BF state sum and Pachner/refinement literature: products of 15j vertices with the corresponding representation/intertwiner sums define 4D SU(2) BF theory; Pachner invariance/topological behavior is subject to the known gauge-volume/redundant-flatness regularization subtleties, especially for the `1<->5` move.

No q-deformation, cosmological constant, or gravity simplicity constraint may be imported into the verdict.

## Frozen object match

The gate must compare the **actual** Iter077 compact boundary tensor with the BF vertex definition:

- same K5 graph;
- same ten spins;
- same five four-valent invariant intertwiners;
- compact edge matrices / relative SU(2) holonomies;
- same orientation/duality convention up to an explicitly nonzero basis phase/normalization.

A mere similarity of diagrams is insufficient.

## Lane A — exact vertex identification

Show that gauge invariance of the compact K5 network makes evaluation on pure-gauge relative holonomies equal to evaluation with all node group elements set to the identity. In an orthonormal four-valent intertwiner basis this is exactly the SU(2) BF/Ooguri 15j vertex tensor.

For the all-`j=1/2` basis, cross-check the exact 32-component tensor against the Iter077N compact census after applying only known nonzero node-normalization factors. Zero/nonzero pattern must be preserved.

## Lane B — refinement/state-sum identification

Show that a multi-vertex term in which every causal vertex contributes only the supported compact tensor `L`, and internal SU(2) spins/intertwiners are contracted with the standard BF/state-sum weights, is the SU(2) Ooguri BF state sum on that subcomplex up to the overall local coefficient `c^V` and explicitly tracked normalization/gauge factors.

## Lane C — 1-to-5 adversarial normalization check

Audit the 4D BF Pachner literature for the `1<->5` move.

PASS requires preserving both facts if supported by the authority:

1. the BF model is topological/Pachner invariant after the appropriate gauge-volume/normalization treatment;
2. the non-q-deformed `1<->5` expression can contain redundant-flatness / gauge-volume divergences, so one may not set the proportionality constant to `1` without specifying the regularization convention.

If the move is only formal/divergent in the relevant normalization, classify that qualification explicitly.

## PASS

PASS iff A-C establish that the surviving ambiguity contains an exact SU(2) BF 15j channel and that its refinement behavior is controlled by the known BF Pachner identities/regularization rather than by generic suppression.

Classification:

`ITER078C_RG_SUPPORTED_K5_AMBIGUITY_IS_SU2_BF_15J_CHANNEL_REFINEMENT_STABLE_UP_TO_BF_GAUGE_NORMALIZATION_EXACT_THEOREM_SCOPED`

## FAIL

FAIL iff the actual compact K5 tensor is not the BF 15j vertex after allowed basis normalization/phase changes, or if the pure-L glued sector fails to reproduce the BF state-sum contraction structure.

## BLOCKED

BLOCKED iff basis normalization/orientation or Pachner regularization cannot be fixed sufficiently to establish the identification.

## Interpretation ceiling

PASS does **not** show that the full Lorentzian causal vertex is topological, that `c` is arbitrary at an RG fixed point, or that refinement consistency cannot constrain `c`.

If the normalized pure BF channel obeys schematically

`Fine[L^5] = K_BF L`,

then a one-parameter pure-sector fixed-point equation would be

`c = K_BF c^5`,

so refinement may quantize/fix the normalization of a nonzero BF-like channel once `K_BF` and the regulator are specified. Cross terms with the gravitational causal sector remain a separate problem.

No RG fixed point for CRQN, no regulator independence, no G3 promotion, no continuum/Einstein/matter claim follows from this gate.