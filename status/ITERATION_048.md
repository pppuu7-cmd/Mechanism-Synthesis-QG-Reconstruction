# Iteration 048 — exact K4 finite-part channel decomposition

**Date:** 2026-09-12
**Prerequisite:** Iter047 terminal `K4_PAIRWISE_FP_COMMUTATOR_OBSTRUCTION_LOCALIZED` with 24/24 source commutators nonzero and 24/24 EPRL/no-contact controls exactly zero.

## Scientific question

Which internal channel of the unchanged Iter045 one-dimensional finite-part operator generates the K4 pairwise noncommutativity?

Write the frozen one-dimensional operator as

`FP_u = R_u + A_u`,

where after the same exact polynomial quotient subtraction used in Iter045–047:

- `R_u[K] = 2*pi*i * sum Res(r, upper-half-plane poles)` is the retained Feynman residue contribution of the proper rational remainder `r`;
- `A_u[K] = -i*pi*a_minus1`, with `a_minus1 = lim_{u->infinity} u*r(u)`, is the retained symmetric-PV / infinity contribution.

The discarded polynomial quotient is recorded as metadata only. It is **not** reintroduced as an additive finite-part contribution and no counterterm is added.

## Frozen source grid

Exactly the same 24 K4 lanes as Iter047:

- Case A: `gamma=0.83`, `epsilon=0.06`, signs `++++++`, `k=(0.19,-0.31,0.27,-0.15)`.
- Case B: `gamma=1.43`, `epsilon=0.12`, signs `-++-++`, `k=(-0.22,0.37,-0.28,0.13)`.
- trees / fundamental-cycle bases: `S0,S1,P0,P1`.
- unordered coordinate pairs: `01,02,12`.

The ordinary EPRL/no-contact `F=1` control is computed in every lane.

No source parameter, pole prescription, subtraction rule, branch sign or acceptance threshold may be changed after this preregistration.

## Exact two-step channel decomposition

For ordered application `i -> j`, decompose

`FP_j(FP_i(K))`

into four exact channels:

- `RR_ij = R_j(R_i(K))`
- `RA_ij = A_j(R_i(K))`
- `AR_ij = R_j(A_i(K))`
- `AA_ij = A_j(A_i(K))`

and analogously for `j -> i`.

Define exact channel commutators

- `Delta_RR = RR_ij - RR_ji`
- `Delta_RA = RA_ij - RA_ji`
- `Delta_AR = AR_ij - AR_ji`
- `Delta_AA = AA_ij - AA_ji`.

The exact reconstruction identity must hold:

`C_ij = Delta_RR + Delta_RA + Delta_AR + Delta_AA`,

where `C_ij` is the unchanged Iter047 full commutator

`FP_j(FP_i(K)) - FP_i(FP_j(K))`.

In addition, at every one-dimensional application the independently recombined `R+A` result must be symbolically identical to the frozen `finite_part_1d` helper.

## Frozen validity gates

A lane is valid only if all of the following hold for source and control:

1. every `R+A` one-step recombination equals `finite_part_1d` exactly;
2. the four two-step channels exactly reconstruct both ordered full results;
3. the four channel deltas exactly reconstruct the total commutator;
4. the control total commutator is exactly zero.

Any violation is `K4_FP_CHANNEL_DECOMPOSITION_INVALID` and blocks physical interpretation.

Individual EPRL-control channel deltas are allowed to be nonzero if and only if they cancel exactly in the frozen total control commutator; such cancellations must be reported rather than hidden.

## Frozen scientific classifier

After all 24 valid lanes:

- `K4_FP_OBSTRUCTION_RESIDUE_CHANNEL` iff every nonzero source total commutator has `Delta_RR != 0` and all A-containing deltas (`RA, AR, AA`) are exactly zero.
- `K4_FP_OBSTRUCTION_INFINITY_CHANNEL` iff every nonzero source total commutator has `Delta_RR == 0` and at least one A-containing delta nonzero.
- `K4_FP_OBSTRUCTION_MIXED_CHANNELS` iff at least one valid source lane has both `Delta_RR != 0` and at least one A-containing delta nonzero.
- `K4_FP_CHANNEL_DIAGNOSTIC_REVIEW` for any heterogeneous pattern not covered above, including unexpected exact-zero source commutators.

The aggregate must report, separately for Cases A and B, counts of nonzero `RR`, `RA`, `AR`, `AA` deltas, exact reconstruction status, and whether any control channel cancellation occurs.

## Interpretation lock

This is a localization test inside the already-frozen sequential FP functional. It does not define a new amplitude and does not prove physical causal-vertex divergence or finiteness.

If the obstruction is confined to A/infinity-containing channels, the next admissible construction is a preregistered genuinely multivariate Hadamard / Epstein-Glaser / BPHZ-style forest or inclusion-exclusion extension selected by source/analyticity constraints, not a post-hoc finite counterterm. If `Delta_RR` is intrinsically nonzero, a more fundamental correlated spectral/contour prescription must be investigated before any multivariate subtraction construction.

`K5`, G3 promotion, F9 and G8 remain BLOCKED throughout Iter048.
