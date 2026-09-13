# Iter077N-SM preregistration — does the supported ambiguity survive the vertex integral, and can standard gluing select it?

**Date:** 2026-09-14

## Scientific question

Iter077M exhibited a local same-scaling-degree ambiguity

`Delta A_c = c F_SU2(y;Psi) delta_N(x)`

on the common-collision submanifold `N=SU(2)^4`. Two logically separate questions remain before using it as an obstruction to the **integrated** vertex:

1. Does this source-built supported term survive integration over `N` as a nonzero linear functional on the frozen all-`j=1/2` boundary space?
2. If it does, does the standard spin-foam gluing/convolution law fix its coefficient `c`, or does gluing simply propagate an arbitrary local vertex choice?

## Source authority

1. Bianchi-Chen-Gamonal causal vertex, arXiv:2601.23162, Eq. (4): vertex is a linear functional on the spin-network boundary state; one group integration is gauge fixed.
2. Donà-Frisoni, *How-to Compute EPRL Spin Foam Amplitudes*, arXiv:2202.04360: on a general 2-complex the amplitude is a state sum

`Z_Delta = sum_{j_f,i_e} prod_f A_f(j_f) prod_e A_e(i_e) prod_v A_v(j_f,i_e)`,

and resolution of the identity in intertwiner space decomposes a multi-vertex amplitude into contractions/products of vertex amplitudes. The correct convolution property fixes face/edge weights; it does not state a separate equation selecting a local modification of `A_v`.
3. Iter077L/M theorem/source authority for the allowed `delta_N` ambiguity.

## Frozen minimal sector

- all ten boundary spins `j_ab=1/2`;
- complete 32-component basis `(k_0,...,k_4) in {0,1}^5` with exactly the same stripped invariant node tensors as Iter077I;
- no boundary component chosen post hoc;
- fixed causal sector; no causal-sector sum.

## Lane A — exact compact K5 survival census

On `N`, relative elements are pure compact gauge holonomies `u_b^-1 u_a`. The coefficient `F_SU2(y;Psi)` is the closed K5 SU(2) spin-network functional made from the same five invariant node tensors.

Because the node tensors are invariant, pure-gauge edge holonomies can be gauged to the identity. Therefore the integral of this coefficient over normalized Haar measure on `SU(2)^4` equals its exact K5 spin-network evaluation with every edge matrix set to the 2x2 identity.

Compute that exact stripped contraction for **all 32** boundary basis tuples using the Iter077I node tensors and edge orientation convention.

Record every exact integer value and a deterministic checksum.

- `SURVIVES` iff at least one of the 32 values is nonzero.
- `KERNEL` iff all 32 are exactly zero.

No floating threshold is allowed.

## Lane B — source gluing algebra

Freeze an arbitrary two-vertex contraction across a common internal boundary basis `alpha` with the standard source-backed state-sum weight `mu_alpha`:

`G_c = sum_alpha mu_alpha A_c^(1)(...,alpha) A_c^(2)(alpha,...)`,

where the **same universal** local coefficient `c` is used at every vertex and

`A_c = A_0 + c L`.

Expand exactly:

`G_c = G_00 + c (G_L0+G_0L) + c^2 G_LL`.

This lane is structural, not numerical. Verify from the general state-sum formula that standard gluing is the contraction operation itself. It is satisfied for every input vertex tensor `A_c`; absent an additional c-independent equation, it does not algebraically solve for `c`.

Positive control: if a frozen source-backed composition identity equates `G_c` to a separately defined c-independent target amplitude for the same complex, derive the resulting equation for `c` rather than declaring freedom.

## Lane C — source selector audit

Audit the frozen sources for an equation that constrains the local vertex beyond insertion into the state sum:

- a projector/idempotency relation for the causal vertex;
- a cylindrical-consistency equation relating one- and two-vertex refinements;
- a gluing normalization that fixes a vertex-supported collision term;
- a causal composition law with a c-independent right-hand side;
- a renormalization/fixed-point condition already stated for this causal vertex.

The causal-vertex paper explicitly says it focuses on a single vertex and that many-vertex construction is future work. Preserve that distinction.

## Aggregate classifications

### PASS — ambiguity survives and standard gluing does not select it

If Lane A has at least one exact nonzero compact K5 value and Lanes B/C find no existing selector:

`ITER077N_SM_K5_SUPPORTED_AMBIGUITY_SURVIVES_VERTEX_INTEGRATION_STANDARD_STATE_SUM_GLUING_DOES_NOT_FIX_COEFFICIENT_EXACT_SOURCE_SCOPED`

### FAIL — frozen ambiguity lies in the integrated kernel

If all 32 Lane-A values vanish exactly:

`ITER077N_SM_FROZEN_DELTA_N_FSU2_AMBIGUITY_INTEGRATES_TO_ZERO_ALL32_EXACT_SCOPED`

This would qualify Iter077M: its local distributional nonuniqueness would not yet establish ambiguity of the integrated minimal-sector vertex.

### BLOCKED

If compact gauge reduction or the source gluing measure cannot be fixed without adding assumptions:

`ITER077N_SM_AMBIGUITY_SURVIVAL_OR_GLUING_BLOCKED_OBJECT_DEFINITION`.

### INVALID

Any post-hoc boundary selection, scalar surrogate, invented composition identity, or equation that silently compares amplitudes on different 2-complexes is invalid.

## Interpretation ceiling

Even PASS establishes only that the standard state-sum contraction operation does not determine the local extension coefficient. It does not show that coarse-graining, cylindrical consistency, an RG fixed point, reflection positivity, a transfer-matrix/causal law, or another independently motivated stronger requirement cannot select it.

No G3 PASS, no regulator independence, no generic-spin theorem, no full vertex nonexistence/divergence theorem, no complete-QG claim.