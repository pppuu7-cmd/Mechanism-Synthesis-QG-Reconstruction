# Iter076W result — compact node gauge one-jet vanishes and relabeling extends pure-direction closure to all integrated nodes

**Date:** 2026-09-13

## Authority

- source supplement: `47300bf71f05b5091a66babb1ef137fe9b9e970d`
- prospective preregistration: `6cc3771899206f7d78fb3642270792588ba220d6`
- implementation: `50bc77c0e872a1c1e43444493ae831b386cf8eca`
- production/workflow head: `61f8b4c81863ce1529c2323f180157680080204a`
- authoritative run: `34783642774`
- jobs: A `103795051618`, B `103795051537`, C `103795051563`, D `103795051448`, aggregate `103795100089`

Artifacts:

- A `10325189139`, `sha256:d4ad8e25c48630904cffa6cd99d7b5e41756a878bc575eb3c7947c304af9c567`
- B `10325687286`, `sha256:ebcba94610bbd266fb4950b558076c30df974482fcd8cae739d6f4b329624445`
- C `10326170936`, `sha256:b4af5a61941641ad0af0ebfbec3fbbe95fbdde69071c49e7a47cb2cdab1efc5b`
- D `10325851666`, `sha256:f0ddf897e8115222668fa56eaa9e23f9496ecd24e68f49e545c8b5c7c193ee8e`
- aggregate `10326260213`, `sha256:53c5f2ffa5bc3c9002049dad2f13af4dd1fef5d49ae9eb1f8ed257b31527d800`

All frozen lanes A/B/C/D and aggregate completed successfully.

## Frozen classification

`ITER076W_COMPACT_NODE_GAUGE_ONEJET_ZERO_AND_RELABEL_EXTENDS_PURE_DIRECTION_CLOSURE_ALL_INTEGRATED_NODES_EXACT_SCOPED`

## Lane A — provenance

The source supplement locks the Eq.(4) magnetic relative-group structure, the gauge root `g_1=1`, Eq.(7) compact covariance, node-5 common compact action, the gauge-root stabilizer `S4`, and the mixed-direction/full-curvature firewalls. The authoritative Iter076V boost result and the exact Iter076N Eq.(4) 120-permutation scalar-character audit are also locked.

## Lane B — exact compact node-5 closure

The same seven exact 4-valent SU(2) invariant tensors used in Iter076V were reconstructed. For every tensor:

- total `J_z` annihilates it;
- total `J_+` annihilates it;
- total `J_-` annihilates it;
- hence a common compact generator in any spatial direction annihilates it.

At least one deliberately single-leg `J_z` control is nonzero. Therefore the cancellation is genuinely collective diagonal-SU(2) intertwiner closure; it is not caused by every magnetic leg being individually trivial.

No Toller pole-strip input is needed for this compact cancellation.

## Lane C — exact transport to all integrated nodes

The gauge-root stabilizer contains exactly `24` permutations fixing the root and permuting the four integrated nodes. Every integrated node maps to the clean source-node-5 position exactly `6` times. Each permutation maps all ten K5 wedge slots bijectively to themselves and preserves the root/integrated decomposition.

Combined with the Iter076N exact source audit that simultaneous Eq.(4) product/measure relabeling carries scalar coefficient `+1`, this transports the structural node-5 zero to any integrated node when group variables, causal data, spins, magnetic slots and intertwiners are relabeled together.

## Lane D — 24 pure generator directions

The exact ledger contains

`4 integrated nodes * (3 compact + 3 boost) directions = 24`

structural cancellations.

- compact node-common one-jets vanish by exact SU(2) boundary-intertwiner invariance;
- boost-normal node-common one-jets vanish by Iter076V plus the same closure;
- the statement is relabeling-covariant over all integrated nodes.

Therefore all six **pure Lie-generator directions** are closed at each integrated source node after boundary-intertwiner contraction.

## Scientific consequence

The surviving source one-jet blocker is now much narrower. It is no longer an isolated compact or boost generator derivative. The unresolved issue is compatibility of the matrix-valued leading singular extraction when compact and boost directions mix: the leading boost singular matrix depends on the normal direction, and a path whose normal direction changes at first order can generate a connection term not probed by the 24 pure-direction zeros.

Separate directional zeros do not by themselves establish a single direction-independent `C^1` factorized germ on a full six-dimensional neighborhood of the singular identity locus.

## Independent frozen confirmation

A second prospective implementation tested the same scientific step with an explicit single-wedge negative control and an exact root-stabilizer star-transport census.

- preregistration: `fd58cc2856062eccee9c5b01af2bd6ee6d96d8ac`
- implementation: `bb8577615b114192d186a4c8f2d26112363549ef`
- workflow head: `07d1249375532572c3f85cfe7588a0170ab18b35`
- run: `34783679839`
- jobs: A `103795156426`, B `103795156384`, C `103795156284`, D `103795156417`, aggregate `103795207316`

Artifacts:

- A `10326185888`, `sha256:227eeba5683408c80e0fc23328d497512947dcba4221ec9fad4120947deb5062`
- B `10324564945`, `sha256:f92090b8be3868eab3a4ebfa7d991d7b74ddf2f10dc682517474cb7bf83b9a63`
- C `10326200945`, `sha256:46ce68030e48aa95e3e9a4e04dd824c64374f6e1ec010ab7ee97a1c697a5bd35`
- D `10325752003`, `sha256:b16a6429afc14fe5845559bed01a4104b15154da7b97b673123da578b3021fcf`
- aggregate `10324989307`, `sha256:9f9393d4c061e03f862450f43709b3683b02db19c59e52c670084890149d10f0`

All four lanes and aggregate passed. The companion frozen classification was

`ITER076W_COMMON_COMPACT_SOURCE_NODE_ONEJET_KILLED_BY_SU2_INTERTWINER_AND_S4_TRANSPORT_EXACT_SCOPED`.

The additional negative control confirms that a single magnetic-leg `J_z` action is generically nonzero while the node-total generator vanishes. Thus the zero is specifically a common source-node gauge/intertwiner cancellation, not an independent-wedge zero. The 24 root-stabilizer permutations also map the node-5 star bijectively to each integrated-node star, with each target reached exactly six times.

This confirmation does not enlarge the scientific scope of the authoritative result.

## Next admissible gate

Construct the normal-direction family of leading matrices `C_n = D(U_n) C_z D(U_n)^{-1}` and its exact angular connection. Test whether the induced mixed-direction connection term reduces to a common SU(2) gauge generator after boundary contraction, or whether a non-generator operator survives. Use exact low-spin intertwiner controls and freeze the prediction before implementation.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no full source one-jet; no physical nonlinear source-to-K4 map; no nominal `epsilon^-1` coefficient; no physical causal-vertex finiteness/divergence theorem; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; retain the source spectral `i epsilon` prescription.
