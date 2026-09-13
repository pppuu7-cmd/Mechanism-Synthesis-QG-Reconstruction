# Iter078D-RG adversarial qualification — BF `c^5` gauge-volume theorem is conditional, not the undefined causal-Toller RG map

**Date:** 2026-09-14

## Reviewed authority

- preregistration `prereg/ITER078D_RG_BF_CHANNEL_1TO5_GAUGE_VOLUME.md`, commit `71a8c52bbc2b46a83ebb3f57908e1a4e028261a8`;
- source/theorem derivation `sources/ITER078D_RG_BF_1TO5_GAUGE_VOLUME_DERIVATION.md`, commit `2a3f4f05e04c27cad58e76d11460c7334e0d2d42`;
- result `results/ITER078D_RG_BF_CHANNEL_1TO5_GAUGE_VOLUME_RESULT.md`, commit `2046e38df32431967b16297dbb3f33d2967bad19`.

## Accepted theorem-scoped core

For a **fixed multilinear five-vertex contraction** and formal universal coupling

`A_c=A_0+cL`,

the coefficient of `c^5` is exactly

`R_5=Contract[L_1 L_2 L_3 L_4 L_5]`.

No mixed term containing `A_0` contributes to that formal coefficient. This algebraic separation is exact.

Under the additional frozen Iter078C condition that the internal contractions/weights are the Ooguri SU(2) BF ones, each `L_v` is the BF 15j vertex and `R_5` is the BF `1->5` amplitude. In the cited BF theorem scope the unregularized `1->5` identity contains four redundant bulk flatness constraints and a `delta(I)^4`-type gauge-volume factor. Thus the **BF-weighted pure-supported coefficient** requires gauge fixing/regulation before it is a finite normalized Pachner coefficient.

## Critical source-map qualification

Iter078A remains controlling for the actual CRQN refinement object:

`ITER078A_RG_CAUSAL_TOLLER_REFINEMENT_MAP_NOT_YET_DEFINED_FRAMEWORK_EXISTS_BUT_SELECTOR_NOT_COMPUTABLE`.

CRQN v0.2 has no source-defined fine face/edge measure, internal representation/intertwiner weights, boundary embedding/projection, or same-boundary coarse/fine amplitude for the 1-to-5 move. Iter078B supplied only compatible causal orientations. Iter078C was already adversarially qualified: its BF multi-vertex statement is conditional on choosing BF weights.

Therefore the phrase

`the naive coefficientwise causal refinement map is gauge-volume divergent`

is too strong unless “causal refinement map” is explicitly read as the **conditional BF-weighted pure-supported control contraction**. The actual causal-Toller map does not yet exist, so no theorem can establish its `c^5` coefficient or its divergence.

## Explicit scope counterexample

Keep the same local supported tensor `L` but choose a non-BF fine face/edge measure or projection rule. Such a choice is not excluded because the CRQN refinement map is currently undefined. Then `Contract[L^5]` need not equal the Ooguri BF `1->5` Pachner amplitude, and the particular `delta(I)^4` theorem need not apply.

This does not propose the non-BF measure as correct physics. It proves only that the BF gauge-volume result cannot be promoted from a conditional BF control to a source-defined CRQN refinement obstruction without a measure/map bridge theorem.

## Consequence for gate ordering

BF gauge fixing is logically prior to computing a **BF-weighted pure-`L` coefficient**, but it is not logically prior to defining the actual causal-Toller refinement map. The higher upstream obligation remains:

`fine causal measure + embedding/projection + regulator + extension transport`.

If the future causal prescription deliberately adopts BF weights on the pure-supported sector, then the Iter078D theorem becomes an applicable required regulator control. If it adopts different source-motivated weights, applicability must be re-established prospectively.

## Verdict

`QUALIFIED`

Authoritative core:

`ITER078D_BF_WEIGHTED_PURE_C5_1TO5_CHANNEL_HAS_DELTAI4_GAUGE_VOLUME_AND_REQUIRES_BF_GAUGE_FIXING_THEOREM_SCOPED`.

Not authorized:

- an unconditional statement that the undefined CRQN causal-Toller 1-to-5 map is divergent;
- treating the BF gauge fixing as the CRQN regulator before the causal multi-vertex measure is defined;
- using the regularized BF coefficient as the CRQN beta function;
- concluding `c=0`, nonrenormalizability, or an RG fixed point.

## Next admissible gate

Return to the upstream missing physical object: freeze one explicit causal 1-to-5 amplitude/measure/embedding/projection prescription, independently motivated by continuum/regulator requirements. Then audit which pure and mixed `A_0/L` sectors are mathematically defined and whether the BF gauge-volume theorem actually applies to its pure-supported sector. Only after that should a coefficientwise closure/fixed-point calculation be authoritative.