# Iter081F causal-admissibility scope note

Date: 2026-09-14
Status: **CRITIC SOURCE-SCOPE FIREWALL — NOT AN ITER081F OUTCOME**

## Purpose
Iter081F prospectively freezes an exact algebraic two-wedge branch-subset boundedness atlas over the four local branch assignments `{++,+-,-+,--}`. This note fixes the source-supported interpretation ceiling before any Researcher result exists.

## Frozen primary authority
Carlos E. Beltran, `arXiv:2603.22661v2`, *Causal Structure for Generalized Spinfoams*.

Relevant exact source statements:

1. For a wedge `w=(v,f)` bounded by two edges `e1,e2`, Beltran Eq. (8) gives
   `epsilon_v(f) = eta epsilon_v(e1) epsilon_v(e2)`.

2. Wedge orientations at a vertex define a proper causal structure only if the cycle constraints hold. Beltran Eq. (9): for every cycle of length `s` in the causal graph,
   `prod_{f in cycle} epsilon_v(f) = eta^s`.
   Equivalently the signs arise from a globally consistent edge-orientation assignment, up to the stated global ambiguity.

3. Beltran Eq. (23) decomposes the ordinary EPRL-KKL vertex into three sums: causal assignments with `eta=+1`, causal assignments with `eta=-1`, and non-causal assignments.

4. Beltran Eqs. (24)-(26) define orientation-dependent vertex amplitudes and state that the ordinary EPRL-KKL amplitude is recovered only after summing over **all** `2^M` wedge-orientation assignments. The exact Toller realization is a product over all wedges of `T^{epsilon_ab}` for one complete assignment.

5. Beltran Eq. (36) defines the proposed positive-signature causal vertex
   `A^+_{gamma_v} = sum_{[epsilon_ab], eta=+1} A_v^{epsilon_ab}`,
   i.e. a sum over globally admissible full-vertex assignments, not a freely chosen subset of local branch words.

## Scope consequence for Iter081F
The 15 nonempty subsets of the local two-wedge word set `{++,+-,-+,--}` are an exact **algebraic cancellation atlas**. They are not, by themselves, 15 source-defined physical causal amplitudes.

A proper local subset `S` can be promoted to a causal-sector statement only if a separate embedding/counting theorem establishes how globally admissible Beltran assignments project onto the two frozen wedges, including multiplicities/weights and correlations with all other wedges. No such projection theorem is assumed in Iter081F.

In particular:
- if only the full four-word set is bounded, this proves that unrestricted local branch completion restores the standard `D=T^+ + T^-` cancellation on the frozen object; it does **not** by itself prove that every globally causal `eta=+1` sum is unbounded;
- if a proper subset is bounded, it is only a candidate cancellation pattern until shown to be induced by the source-defined global causal assignment sum;
- no two-wedge result may be promoted to the full vertex, multivertex stack, Han face functional, joint-K5 distributional extension, or RG mechanism without the corresponding embedding/composition theorem.

## Relation to historical Iteration 023
The historical `research/iteration-023-causal-sector-sums` branch already encoded correlated 4-simplex signs as `kappa_ab=sigma_a sigma_b` and numerically scanned the full ten-wedge carrier over 16 factorized classes. Its own guardrail states that this is power counting on generic cluster rays and does not replace exact distributional `i epsilon` integration or boundary contraction.

Therefore Iter081F is not a repeat: it is an exact local Eq. (46) cancellation atlas. Conversely, historical Iteration 023 prevents interpreting arbitrary local subsets as already-established physical causal sector sums.

## Claim lock
This note makes no boundedness prediction for any of the 15 Iter081F subsets and must not be used to infer the gate outcome. It only freezes the distinction
`local algebraic subset != source-defined globally causal assignment sum`
unless an embedding theorem is supplied.
