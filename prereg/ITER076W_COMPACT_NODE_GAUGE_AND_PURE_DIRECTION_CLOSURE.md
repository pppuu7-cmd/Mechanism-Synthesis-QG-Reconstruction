# Iter076W preregistration — compact node gauge one-jet and pure-direction closure on all integrated nodes

Date: 2026-09-13

## Purpose

Iter076V closed the boost-normal part of the factorized source one-jet: after leading singular matrix extraction the relative Toller one-jet is `i gamma J_n`, and a common boost of source node 5 is annihilated by the exact SU(2) boundary intertwiner.

This gate tests the complementary **compact/tangential pure generator directions** directly from source Eq. (7), then transports both compact and boost-normal node-common cancellations from node 5 to all four integrated source nodes using the gauge-root stabilizer and exact source relabeling covariance.

It deliberately does **not** infer a differentiable mixed compact/boost germ from separate pure-direction cancellations.

## Frozen source input

Use `sources/TOLLER_COMPACT_NODE_GAUGE_ONEJET_SUPPLEMENT.md`, committed before implementation, the authoritative Iter076V result, and the exact Iter076N Eq.(4) relabeling audit.

Source labels are represented in code as `0,1,2,3,4`, with gauge root `0` and integrated nodes `1,2,3,4`; code node `4` corresponds to source node `5`.

## Frozen lanes

### Lane A — source/provenance locks

PASS iff the committed source supplement records:

- five SU(2) boundary intertwiners;
- Eq. (4) relative arguments `g_b^{-1}g_a` and magnetic wedge slots;
- gauge root `g_1=1` with four integrated nodes;
- Eq. (7) compact covariance;
- the node-5 common compact action on the four node-5 magnetic slots;
- the root-stabilizer `S4` transport statement;
- the explicit firewall that mixed-direction differentiability and the physical nonlinear source-to-K4 curvature remain open.

The authoritative Iter076V result must contain the frozen PASS classification. The Iter076N exact-amplitude provenance result must contain the exact 120-permutation Eq.(4) scalar-character audit and explicit `+1` product/measure coefficient.

### Lane B — exact node-5 compact intertwiner closure

Construct the same exact 4-valent SU(2) invariant tensors as Iter076V for the frozen spin controls

- `(1/2,1/2,1/2,1/2)`, all allowed common intermediate `k`;
- `(1/2,1,1/2,1)`, all allowed common intermediate `k`;
- `(1,1,1,1)`, all allowed common intermediate `k`.

PASS iff all seven invariant tensors are nonzero and, for every tensor,

- total `J_z` annihilates it exactly;
- total `J_+` annihilates it exactly;
- total `J_-` annihilates it exactly;
- hence the common compact generator in any spatial direction is annihilated exactly;
- at least one deliberately **single-leg** generator control is nonzero, proving that cancellation is collective intertwiner closure rather than every leg being individually trivial.

No Toller pole-strip input is used in this compact lane.

### Lane C — gauge-root stabilizer and source relabeling transport

Enumerate exactly all permutations of five source labels that fix the gauge root `0` and permute the four integrated labels.

PASS iff:

- there are exactly `24` root-stabilizer permutations;
- each of the four integrated nodes is mapped to code node `4` exactly `6` times;
- every permutation bijectively maps the ten unordered K5 wedge slots to themselves;
- every permutation preserves the decomposition into one gauge root plus four integrated nodes;
- the committed Iter076N source audit records scalar Eq.(4) product/measure character `+1`, so no alternating scalar obstruction is inserted during simultaneous relabeling.

This lane transports a structural zero only under simultaneous relabeling of group variables, causal data, spins, magnetic slots and boundary intertwiners. It does not assert equality at fixed unpermuted boundary data.

### Lane D — combined pure-direction closure and firewall

Combine:

- three compact generator directions per integrated node from Lane B/C;
- three boost-normal generator directions per integrated node from authoritative Iter076V plus Lane C.

PASS iff the exact ledger contains `4 * 6 = 24` node/direction structural cancellations and records:

- `compact_node_common_onejet_killed_by_intertwiner=true`;
- `boost_node_common_onejet_killed_by_intertwiner=true`;
- `pure_generator_direction_cancellation_all_integrated_nodes=true`;
- `mixed_compact_boost_C1_germ_established=false`;
- `direction_independent_leading_factorization_established=false`;
- `full_source_onejet_established=false`;
- `physical_source_to_K4_curvature_selected=false`;
- `epsilon_minus1_coefficient_established=false`;
- no generic finite-spin signed P3 or G3/F9/G8/K5 promotion.

## PASS classification

`ITER076W_COMPACT_NODE_GAUGE_ONEJET_ZERO_AND_RELABEL_EXTENDS_PURE_DIRECTION_CLOSURE_ALL_INTEGRATED_NODES_EXACT_SCOPED`

## Scientific meaning on PASS

Every integrated source node has exact cancellation of all six **pure Lie-generator directions** after boundary-intertwiner contraction: three compact directions by SU(2) gauge invariance and three boost-normal directions by the Iter076V relative operator `i gamma J_n` plus the same intertwiner closure.

This materially narrows the source one-jet blocker but does not yet prove a full differentiable one-jet at the singular identity locus. The leading Toller singular matrix depends on the normal boost direction, so mixed compact/boost paths may carry compatibility data not visible in the six separate generator directions.

## Next admissible gate

Audit the normal blow-up / mixed-direction compatibility of the extracted leading singular matrix. Determine whether the family `C_n` defines a covariant bundle-valued leading object with a connection whose first mixed compact/boost correction is pure SU(2) gauge and therefore killed by the boundary intertwiners, or whether an independent connection/curvature datum survives. This must be frozen before implementation.

## FAIL classification

`ITER076W_COMPACT_NODE_GAUGE_PURE_DIRECTION_CLOSURE_CONFIRMATION_FAIL`

A failure is an algebra/source-covariance result, not a physical finiteness/divergence theorem.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no full source one-jet; no physical nonlinear source-to-K4 map; no nominal `epsilon^-1` coefficient; no physical causal-vertex finiteness/divergence theorem; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; retain the source spectral `i epsilon` prescription.