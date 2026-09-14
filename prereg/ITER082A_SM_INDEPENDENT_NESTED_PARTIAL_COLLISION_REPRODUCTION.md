# Iter082A-SM prereg — independent Researcher reproduction of nested K3/K4 source-ordered partial-collision boundary witnesses

Status: **PROSPECTIVE RESEARCHER REPRODUCTION GATE — frozen before any Iter082A implementation/production**
Date: 2026-09-14

## Motivation
Critic exploratory control `results/ITER081Z_CRITIC_EXPLORATORY_NESTED_PARTIAL_COLLISION_CONTROL.md` reported exact nested K4/K3 boundary-contraction witnesses but was not prospectively frozen before exploration and is therefore not authoritative scientific proof. Iter082A independently reproduces or falsifies that hypothesis from the authoritative Iter077I source-leading matrix and boundary tensors.

The Critic output values must not be imported as pass labels or data.

## Frozen source object
Use exactly the Iter077I all-`j=1/2` source-leading matrix shape

`M(v)=[[v_z,-v_x-i v_y],[-v_x+i v_y,-v_z]]`

and exactly the five-node two-dimensional SU(2)-invariant intertwiner basis used by authoritative Iter077I, including the same edge incidence/magnetic ordering and integer-stripped intertwiner coefficients.

All calculations must be exact Gaussian-integer/integer arithmetic. No numerical Toller backend is permitted for the positive classification.

## K4 nested witness
Freeze cluster `B={0,1,2,3}` with

`a_0=(0,0,0)`, `a_1=(1,2,3)`, `a_2=(2,3,5)`, `a_3=(3,5,7)`,

external direction

`b=(5,7,11)`.

For the nested limit `X_i=r a_i`, `i in B`, `X_4=s b`, `r/s->0`, construct leading numerator matrices mechanically:

- internal edges `(ij) subset B`: `M(a_i-a_j)`;
- cross edges `(i4)`: `M(-b)`.

Enumerate all 32 boundary basis components and contract the ten matrices exactly.

K4 positive predicate: at least one exact boundary contraction is nonzero. Stronger diagnostic: count how many of 32 are nonzero, but the Critic-reported `32/32` is a hypothesis to be checked, not a frozen pass value.

If nonzero, combine with exact source small-boost asymptotics to prove the fixed-external partial coefficient function is not identically zero: in the subsequent `s->0` limit its leading nested coefficient is nonzero. Then there exist sufficiently small fixed `s>0` partial-K4 configurations with nonzero fully boundary-contracted internal coefficient.

Use exact internal power `q_4=-12`, normal dimension `d_4=9`, margin `-3`.

## K3 nested witness
Freeze cluster `B={0,1,2}` with

`a_0=(0,0,0)`, `a_1=(1,2,3)`, `a_2=(2,3,5)`,

external directions

`b_3=(3,5,7)`, `b_4=(5,7,11)`.

For `X_i=r a_i`, `i in B`, `X_3=s b_3`, `X_4=s b_4`, `r/s->0`, construct mechanically:

- internal K3 edges: `M(a_i-a_j)`;
- cluster-to-3 edges: `M(-b_3)`;
- cluster-to-4 edges: `M(-b_4)`;
- edge `(3,4)`: `M(b_3-b_4)`.

Enumerate/contract all 32 boundary components exactly.

K3 positive predicate: at least one exact contraction is nonzero. Stronger diagnostic: count how many of 32 are nonzero; do not hard-code the Critic-reported count.

If nonzero, prove by the same nested-asymptotic argument that the fixed-external K3 coefficient function is not identically zero and hence is nonzero at some sufficiently small fixed external configuration.

Use exact internal power `q_3=-6`, normal dimension `d_3=6`, margin `0` (logarithmic absolute-L1 failure when the leading coefficient is nonzero).

## Causal sign control
Independently verify that at the final nested all-edge leading level every proper causal K5 assignment `epsilon_ab=eta sigma_a sigma_b` has total branch parity `+1`, so the nested leading tensor does not cancel by proper-causal orientation summation. Do not infer equality of exact finite-s partial coefficients away from the deeper collision.

## Required controls
1. Reconstruct the 32 boundary basis components from the Iter077I intertwiner definition rather than importing old output tables.
2. Verify every frozen relative direction used in a leading denominator is nonzero.
3. Verify exact integer/Gaussian-integer arithmetic throughout.
4. Include a degenerate negative control where one internal relative vector is deliberately zero and reject it as inadmissible rather than classifying a contraction.
5. Reproduce the deepest Iter077I all-plus witness nonzero on at least one boundary component as an implementation sanity check, without using its stored result as the partial-stratum pass predicate.

## Frozen classifications
- `ITER082A_SM_SOURCE_ORDERED_FULL_BOUNDARY_K3_LOG_AND_K4_POWER_PARTIAL_COLLISION_NONL1_WITNESSES_CONFIRMED_EXACT_SCOPED` iff both frozen K3 and K4 nested witnesses have at least one nonzero exact full boundary contraction and the fixed-external nonidentity argument is valid.
- `ITER082A_SM_K4_ONLY_PARTIAL_COLLISION_WITNESS_CONFIRMED_EXACT_SCOPED` if K4 succeeds but K3 does not.
- `ITER082A_SM_K3_ONLY_PARTIAL_COLLISION_WITNESS_CONFIRMED_EXACT_SCOPED` if K3 succeeds but K4 does not.
- `ITER082A_SM_NESTED_PARTIAL_COLLISION_HYPOTHESIS_FAILS_EXACT_SCOPED` if both valid exact contractions vanish.
- `INVALID_IMPLEMENTATION_OR_PROVENANCE` for source/basis/chronology/control failure.

## Claim ceiling
A positive result proves existence of source-ordered fully boundary-contracted partial K3/K4 non-L1 configurations in the frozen minimal-spin sector, not divergence on every point/state, not generic-spin behavior, and not distributional nonexistence. It would justify a real stratified forest extension requirement. It does not define subtraction coefficients, a selector, regulator independence, G3/F9/G8/K5, `NEW_PHYSICS_FOUND`, or complete QG.
