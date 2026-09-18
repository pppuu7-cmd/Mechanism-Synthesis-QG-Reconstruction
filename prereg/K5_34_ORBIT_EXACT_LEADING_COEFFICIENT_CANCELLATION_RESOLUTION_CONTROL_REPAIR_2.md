# Prospective control-only repair 2 — K5 34-orbit exact leading-coefficient cancellation resolver

Date: 2026-09-19

## Parent scientific contract

Immutable parent scientific preregistration:

`prereg/K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION.md`

commit `d6b0e805101c8590eafac71398cc2b1466691752`.

Repair-1 preregistration remains historical and immutable:

`2193692c90d8ee1fa097200dbbac6ab70fd3a159`.

Repair-1 production run `35271187040` is terminal `INVALID_IMPLEMENTATION`; it supplies zero authoritative N/B values.

## Independent defect authority

The repaired component-1 implementation diagnostic was independently reconstructed and terminally confirmed:

`CONFIRMED_SCOPED_COMPONENT1_SUPPORT_SET_MISMATCH`.

Critic authority:
- prereg `bc7a63a50a2fff36f931e03b5f26d4563ca29607`;
- implementation `6b140a14bcd679ad5594f29b7d50e83d6b6d88e8`;
- run `35402998823`;
- artifact `10571337475`;
- artifact ZIP SHA256 `4d0cd5dd8c8ec42787d5bd6b22b006655ec237924d6241c96ecbabb10260e5b2`.

The Critic independently reconstructed the full 32-component source, exact target component-1 projection, 16 nonzero contributors, dropped-contributor rejection and exact unequal support sets. q18 partials were not used.

## Exact repair-2 diagnosis

Repair-1 constructs its S5 source coefficient object from

`s5.transport_target_key_to_old(types, CYCLE)`

and collapses that pullback/old-label support directly into perfect-matching indices. The shard then supplies that matching object to `route_a` evaluated on the permuted mask and permuted weights, whose covariance object is indexed in the **target edge frame**.

This mixes support index frames.

The only allowed repair is to express the transported source support in the same target edge frame as the permuted route before Wick matching collapse.

For each canonical old edge index `i`, let

`j = ep(CYCLE, i)`.

For an old-frame source type tuple `types`, the repaired target-frame tuple is frozen as:

- `out[j] = types[i]` if the oriented edge is preserved;
- `out[j] = transpose(types[i])` if `edge_sign(CYCLE,i)=-1`.

Multiply by the already-required source reversal orientation character exactly once. Do **not** pre-multiply the covariance orientation character: the target-frame covariance route supplies its own orientation transport.

Then perform the unchanged invariant-dual projection and unchanged 945-perfect-matching collapse on this target-indexed tuple.

No fitted sign, phase, channel matrix, support filter or result-dependent remapping is allowed.

## Mandatory repair-2 controls

Before heavy scientific use, the implementation must establish exactly:

1. parent prereg, repair-1 prereg and this repair-2 prereg locks;
2. independent component-1 Critic classification is `CONFIRMED_SCOPED_COMPONENT1_SUPPORT_SET_MISMATCH`;
3. Critic reports q18 unused and authorizes prospective heavy-resolver repair-2;
4. corrected Iter077I source blob remains unchanged;
5. full source has 32 components and exactly 100000 source terms;
6. forward old-to-target edge map is a bijection and inverse-roundtrips exactly on all 32 source dictionaries;
7. target-frame component-1 transported dictionary reproduces the independent Critic route-2 dictionary/support hashes and support cardinality 1536;
8. repaired target-frame matching object is exact rational, nonempty, has exactly 945 perfect-matching support keys, and every key covers edge indices 0..9 exactly once;
9. historical pullback-frame repair-1 matching object is rejected as a distinct malformed object;
10. structural polynomial equality controls from repair-1 remain passing;
11. independent Boundary-S5 Critic authority and mask511/projective-normal locks remain unchanged;
12. no q18 partial, historical invalid resolver coefficient/order, interpolation fit or floating tolerance is consumed.

## Immutable scientific inputs

Repair-2 MUST NOT alter:

- CRQN v0.2 or claim ceiling;
- 32 proper S5 orbit representatives;
- both invariant-dual physical channels;
- W1/W2 or their frozen permuted weights;
- canonical ten-edge ordering;
- all-32/100000-term source contraction;
- 945 retained matchings;
- degree ceilings N<=27, B<=31, U<=5;
- degree-27 DAG and Q source radius;
- projective-normal authority;
- mask511 r_N=19, r_B=21 authority;
- exact Fraction arithmetic;
- independent interpolation route;
- parent PASS/PARTIAL/INVALID meanings;
- published spectral i epsilon.

## Production rule

Only after the repair-2 preflight controls are terminal PASS may exactly one heavy eight-shard resolver production be launched.

No partial shard coefficient/order may be consumed. Only the complete aggregate may classify the heavy production.

## Terminal taxonomy

Unchanged from repair-1/parent:

- `PASS_EXACT_SCOPED` only if every frozen implementation/source/S5/coverage/independent-route/U/mask511 control passes and all 64 channel-orbit rows are certified under the unchanged parent contract.
- `PASS_EXACT_PARTIAL_BLOCKED_SCOPED` only if implementation is valid but at least one frozen component remains uncertified.
- `INVALID_IMPLEMENTATION` for any mandatory implementation/provenance/S5/frame/support/control failure. INVALID carries no scientific N/B verdict.

## Interpretation ceiling

Even a valid resolver closes only the frozen 64-component local N/B leading-order table. It does not itself prove global Stokes/IBP, K5 periods, a physical finite-part selector, reduce dim_C F_8=377, prove regulator independence, promote F9/G3/G8/K5, establish NEW_PHYSICS_FOUND, or complete quantum gravity.
