# Iter078L-RG source audit — no published exact cross-spin causal-vertex recurrence

**Date:** 2026-09-14

Prospective contract: `prereg/ITER078L_RG_SOURCE_BACKED_CROSS_SPIN_RECURRENCE.md`, commit `087470d6717c49065fcf5c5f83cc95048b1d5549`.

## Frozen source audit

### Causal-vertex paper

Bianchi-Chen-Gamonal define the physical gamma-simple fixed-causal vertex

`A_v^(sigma)[j_ab,i_a]`

with ten representation labels `(rho,k)=(gamma j_ab,j_ab)` and ten Toller matrices. The paper proves/uses:

- the fixed-spin additive identity `T+ + T- = D`;
- coherent-state/source formulas;
- uniform large-spin asymptotics `j_ab -> lambda j_ab`.

The paper does not state an exact recurrence, recursion, finite-difference equation, or contiguous relation connecting the full causal vertex at different boundary-spin assignments.

### Companion Toller paper

The companion paper proves uniqueness of the Toller splitting at fixed matrix/representation data from analyticity, asymptotic decay, pole structure and the Feynman projector. It gives explicit hypergeometric formulas for the reduced Toller matrices, including the gamma-simple branch.

The source does not state a recurrence/difference law relating the **physical gamma-simple K5 vertex** across different boundary spins.

The hypergeometric parameters in the gamma-simple formula depend on `j`, and standard special-function theory supplies many contiguous identities. However, shifting `j` in the physical spinfoam simultaneously changes:

- the SU(2) matrix index;
- the Lorentz representation parameter `rho=gamma j`;
- the representation label `k=j`;
- the boundary intertwiner spaces;
- the full ten-wedge contraction.

No theorem in the frozen source is given that promotes a one-function contiguous identity to an exact source-ordered full-K5 recurrence, still less one that fixes supported distributional extension terms at the common collision.

## Search controls

The source text was checked for the explicit notions:

- recurrence;
- recursion;
- difference equation;
- contiguous relation.

No physical cross-spin causal-vertex law of the required scope was found.

## Consequence

The published one-wedge uniqueness theorem and the published large-spin theorem constrain different aspects of the causal construction but leave the exact finite-spin K5 extension unselected.

A future cross-spin recurrence could be new mathematically derived structure. To become a selector it would need a prospective proof that it acts on the full gamma-simple source-ordered K5 amplitude, including boundary intertwiners and the distributional extension, and that it survives gluing/refinement consistently.