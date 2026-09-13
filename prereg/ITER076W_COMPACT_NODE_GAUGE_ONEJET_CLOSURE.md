# Iter076W preregistration — compact source-node gauge one-jet and root-stabilizer transport

Date: 2026-09-14

Status: `PREREGISTERED / EXACT_SOURCE_COVARIANCE_GATE`

## Purpose

Iter076V established that after the frozen leading singular-matrix extraction the **node-common pure-boost** relative one-jet is `i gamma J_n` on each incident wedge and is annihilated by an SU(2)-invariant boundary intertwiner. The remaining pure-generator question is the compact tangent to the singular SU(2) locus.

This gate tests one statement only:

> Does exact source Eq.(7) compact covariance make a common compact perturbation of an integrated source node act by the total SU(2) generator on that node's four magnetic slots, so that the boundary intertwiner annihilates it; and does the root-stabilizer relabeling transport this cancellation from node 5 to every integrated node?

It does **not** test mixed compact/boost differentiability, a global ten-wedge singular factorization, the nonlinear source-to-K4 curvature, or the nominal `epsilon^-1` coefficient.

## Frozen source inputs

Use only source-established data already recorded before this preregistration:

- `sources/TOLLER_COMPACT_NODE_GAUGE_ONEJET_SUPPLEMENT.md` at commit `47300bf71f05b5091a66babb1ef137fe9b9e970d`;
- primary-source Eq.(4): fixed-causal vertex built from `T(g_b^{-1} g_a)`, gauge root `g_1=1`, with `g_2,...,g_5` integrated and five SU(2) boundary intertwiners;
- primary-source Eq.(7): `T(U_1 exp(beta sigma_z/2) U_2)=D^j(U_1)t(beta)D^j(U_2)`;
- closed Iter076V result `results/ITER076V_MATRIX_BOOST_ONEJET_INTERTWINER_CLOSURE_RESULT.md` only as a scope/control antecedent.

No symmetry-only assumption may replace Eq.(7) compact covariance or exact intertwiner invariance.

## Lane A — source/provenance locks

PASS-A iff the committed source supplement records all of:

1. five SU(2) intertwiners;
2. Eq.(4) relative argument `g_b^{-1}g_a`;
3. gauge root `g_1=1` and integrated nodes `2,...,5`;
4. Eq.(7) compact covariance;
5. common node compact perturbation acts through the same SU(2) generator on all four node slots;
6. mixed compact/boost differentiability and `epsilon^-1` remain unestablished.

A missing lock makes the gate invalid rather than supplying a physical zero.

## Lane B — exact node-5 compact closure

At the coincident source control set neighboring group variables to identity and perturb only node 5 by

`g_5(theta)=exp(theta J_n)`.

For its four incident wedges `(a,5)`, Eq.(4)/(7) gives the common compact first correction proportional to

`-i sum_(a=1)^4 J_n^(5a)`

(up to the frozen Hermitian/anti-Hermitian generator normalization, irrelevant to the zero).

Construct exact four-valent SU(2)-invariant tensors by Clebsch-Gordan coupling for the same controls as Iter076V:

- `(1/2,1/2,1/2,1/2)`, every allowed common intermediate `k`;
- `(1/2,1,1/2,1)`, every allowed common `k`;
- `(1,1,1,1)`, every allowed common `k`.

PASS-B iff every nonzero control is annihilated exactly by total `J_z`, total raising, and total lowering operators. Hence total `J_n` vanishes for arbitrary compact direction.

No floating tolerance is allowed.

## Lane C — root-stabilizer transport

Freeze source root `1`. Enumerate all `4! = 24` permutations of integrated labels `{2,3,4,5}`.

For every permutation `p` require exactly:

- `p(1)=1`;
- the ten unordered K5 wedges are mapped bijectively to the same wedge set;
- the node-5 incident star maps to the incident star of `p(5)`;
- simultaneous relabeling transports the node magnetic slots, causal edge labels and group variables together;
- the targets `p(5)` cover each integrated node `{2,3,4,5}` exactly six times.

PASS-C establishes only relabeling-covariant transport of the already-derived node-common cancellation. It does not create a new scalar parity/sign selector.

## Lane D — negative control and scope firewall

The compact cancellation must be specific to a **common source-node** perturbation.

Take at least one nonzero frozen intertwiner control and act with `J_z` on a single magnetic leg only. PASS-D requires this single-leg action to be nonzero while the total `sum_a J_z^(a)` action is zero.

The aggregate must also record:

- `common_compact_node_onejet_killed=true`;
- `all_integrated_nodes_transport=true`;
- `independent_wedge_compact_onejet_killed=false`;
- `mixed_compact_boost_differentiability_established=false`;
- `full_source_onejet_established=false`;
- `physical_source_to_K4_curvature_selected=false`;
- `epsilon_minus1_coefficient_established=false`;
- no generic finite-spin signed P3 or G3/F9/G8/K5 promotion.

## PASS classification

All frozen lanes valid:

`ITER076W_COMMON_COMPACT_SOURCE_NODE_ONEJET_KILLED_BY_SU2_INTERTWINER_AND_S4_TRANSPORT_EXACT_SCOPED`

Scientific meaning: every integrated node has its **pure common compact source direction** removed by exact boundary gauge invariance. Together with Iter076V this closes the six separate pure generator directions only as directional statements. It does not prove a single differentiable factorized germ on a full `SL(2,C)` neighborhood.

## FAIL classification

Any exact algebra/source/relabeling predicate fails:

`ITER076W_COMPACT_NODE_GAUGE_ONEJET_CLOSURE_FAIL`

This is an algebra/source-compatibility result, not a physical finiteness/divergence theorem.

## BLOCKED classification

If Eq.(7) compact covariance cannot be connected to the Eq.(4) magnetic slots with the frozen source conventions without adding an unsourced identification:

`ITER076W_BLOCKED_SOURCE_COMPACT_SLOT_IDENTIFICATION`

No zero may be inferred in this case.

## Next admissible gate after PASS

Audit the **normal blow-up / mixed compact-boost compatibility** of the extracted leading singular matrix: determine whether the separate pure-direction cancellations assemble into a direction-independent differentiable regular germ, or whether mixed approach directions leave independent regular one-jet data.

Only after that object is defined may the regular source one-jet be classified as zero/nonzero and combined with a separately derived nonlinear source-to-K4 curvature for the nominal `epsilon^-1` channel.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no full source one-jet; no physical nonlinear source-to-K4 map; no nominal `epsilon^-1` coefficient; no physical causal-vertex finiteness/divergence theorem; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; retain the source spectral `i epsilon` prescription.
