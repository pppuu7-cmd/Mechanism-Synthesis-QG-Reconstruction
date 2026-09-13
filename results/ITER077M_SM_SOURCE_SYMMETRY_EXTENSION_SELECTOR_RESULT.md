# Iter077M-SM result — published source symmetries do not select the K5 extension

**Date:** 2026-09-14

## Provenance

- Prospective preregistration: `prereg/ITER077M_SM_SOURCE_SYMMETRY_EXTENSION_SELECTOR.md`, commit `b9af6704336a357dba0b2287b2d7d1320fc020a7`.
- Source derivation: `sources/ITER077M_SM_SOURCE_SYMMETRY_SELECTOR_DERIVATION.md`, commit `3bd388c143030e8947ca1a206e907027e0dd2362`.
- Extension-theorem authority: `results/ITER077L_SM_TRANSVERSE_SCALING_DEGREE_EXTENSION_THEOREM_RESULT.md`.
- Primary source authority: Bianchi-Chen-Gamonal causal vertex Eq. (3)-(7) and Discussion.

## Classification

`ITER077M_SM_PUBLISHED_GAUGE_BOUNDARY_CAUSAL_CONSTRAINTS_DO_NOT_SELECT_K5_EXTENSION_NONZERO_DELTA_N_AMBIGUITY_SURVIVES_EXACT_THEOREM_SCOPED`

Scientific verdict: **PASS** for the preregistered nonuniqueness-under-published-constraints hypothesis.

## Frozen checks

1. **Support PASS.** The common-collision set is invariantly defined by `g_b^-1 g_a in SU(2)` for all wedges. After the source global gauge fixing it is `N=SU(2)^4`. A term proportional to `delta_N` changes only the extension on that set and leaves every off-collision Toller function unchanged.
2. **Scaling PASS.** `delta_N` has transverse scaling degree `12`, while the exact source-ordered K5 object has `sd_N=20`. Therefore adding a smooth tangential coefficient times `delta_N` preserves the overall scaling degree 20.
3. **Global gauge PASS.** Before gauge fixing, the supported set and coefficient can be written only in terms of relative group elements, so common left `SL(2,C)` multiplication leaves them invariant.
4. **True boundary object PASS.** The smooth coefficient `F_SU2(y;Psi)` is the ordinary compact spin-network functional built from the same ten spins and five SU(2)-invariant boundary intertwiners. No scalar K4/K5 surrogate and no post-hoc representative boundary component are used.
5. **Causal-data PASS.** The ambiguity is constructed separately inside one fixed causal sector and does not alter or sum the `sigma_a sigma_b` labels.
6. **Source-order PASS.** The ambiguity is an extension term added only after the exact one-wedge Toller construction and ten-wedge off-collision product have been fixed. No spinor/contact limit is reordered.
7. **Published-selector audit PASS.** The primary paper explicitly leaves causal-vertex finiteness for future investigation and treats the many-vertex theory as a future step. It does not state a K5 subtraction/normalization, finite-part rule, common joint regulator, collision boundary-value condition, or gluing/composition identity fixing the supported coefficient.

## Explicit nonuniqueness witness

If `A_ext` is any Iter077L same-scaling-degree local extension, then for any constant `c`

`A_ext,c(Psi) = A_ext(Psi) + c F_SU2(y;Psi) delta_N(x)`

has the same off-`N` source object, the same maximal transverse scaling degree, the same common global gauge symmetry, the same true boundary spin/intertwiner structure, and the same frozen causal labels.

At least the coefficient `c` therefore remains undetermined by the constraints actually stated in the published single-vertex construction.

## New scientific fact

The Iter077K/L object-definition blocker is not merely an abstract renormalization freedom. A concrete nonzero source-compatible supported ambiguity survives the published gauge, boundary and causal structure. Thus those published constraints cannot, by themselves, promote the formal Eq. (4) expression to a unique finite-spin local distributional functional at the common collision.

## Interpretation ceiling

This does **not** prove that no additional physical principle can select `c`. In particular, multi-vertex gluing/composition, cylindrical consistency, coarse-graining/RG, a derived normalization condition, or another independently motivated law might constrain or remove the ambiguity. The primary source has not yet supplied such a selector, so introducing one now is a new scientific gate, not a reinterpretation of the existing one-wedge `i epsilon` prescription.

No full causal-vertex divergence/nonexistence theorem; no proof that every order-8 local coefficient survives stronger future constraints; no regulator-independence theorem; no generic-spin theorem; no G3/F9/G8/K5 promotion; no new-physics or complete-QG claim.

## Exact next admissible step

Move one layer outward instead of accumulating more local singularity lemmas: prospectively test **multi-vertex gluing/composition consistency as a selector of the local extension freedom**. Construct the smallest two-vertex causal complex for which the supported `delta_N` ambiguity enters an internal boundary contraction, freeze the gluing measure and causal orientations from source-backed spinfoam rules, and determine whether composition forces `c=0`, fixes a unique nonzero `c`, leaves a family, or is itself undefined. This directly couples the local-amplitude blocker to G3/composition without assuming the blocker solved.