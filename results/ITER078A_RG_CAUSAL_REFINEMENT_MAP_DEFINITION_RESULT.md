# Iter078A-RG result — causal refinement/RG framework exists but the causal-Toller map is not yet defined

**Date:** 2026-09-14

## Provenance

- Prospective preregistration: `prereg/ITER078A_RG_CAUSAL_REFINEMENT_MAP_DEFINITION.md`, commit `97257d6830f1a386f9df3a854391e4e86e340884`.
- Source audit: `sources/ITER078A_RG_CAUSAL_REFINEMENT_MAP_AUDIT.md`, commit `377e78d6b954003354f2a73ecf95b34f70e97109`.
- Upstream integrated-ambiguity authority: `results/ITER077N_SM_SUPPORTED_AMBIGUITY_SURVIVAL_AND_GLUING_RESULT.md`.

## Classification

`ITER078A_RG_CAUSAL_TOLLER_REFINEMENT_MAP_NOT_YET_DEFINED_FRAMEWORK_EXISTS_BUT_SELECTOR_NOT_COMPUTABLE`

Scientific verdict: **BLOCKED_MAP_DEFINITION**.

## Findings

1. Background-independent spin-foam renormalization has an established conceptual framework: cylindrical/consistent-boundary conditions compare path-integral amplitudes across refinements and provide the analogue of RG flow without a background length scale.
2. Concrete spin-foam RG calculations in the literature require additional model choices: a refinement/discretization family, boundary embedding/coarse-graining maps, restricted or truncated theory space, matching observables/amplitudes, and projection back to that theory space.
3. The 2026 causal-Toller paper defines a fixed-causal **single vertex** Eq. (4), with causal edge orientations and one-wedge Toller functions, but it does not define a concrete coarse/fine causal refinement map.
4. For the current CRQN object the following selector data are missing: a chosen same-boundary coarse/fine complex pair, causal orientation propagation on shared internal tetrahedra, causal fine-complex face/edge measure, boundary embedding/refinement map, projection/truncation map, fixed-point/cylindrical equation, and a rule transporting the Iter077 supported extension freedom.
5. Existing Euclidean/restricted/hypercuboidal EPRL/FK RG maps are not source-faithful substitutes for this Lorentzian causal-Toller object.

## New scientific fact

The next CRQN blocker is no longer merely “need RG eventually”. There is presently **no defined RG map on the causal-Toller theory space on which the extension coefficient can even be evolved or tested for a fixed point**.

This prevents an RG/cylindrical condition from being invoked as if it already selected the K5 extension. However, developing such a map is independently motivated by regulator independence and the continuum limit of spin foams, so it is scientifically admissible as new mechanism development rather than a post-hoc rescue — provided it is versioned and prospectively falsifiable.

## Interpretation ceiling

This result does not show that a causal RG map cannot be constructed or that no fixed point exists. It establishes only that CRQN v0.2 / the frozen causal-Toller source does not yet define the map required to ask that question quantitatively.

No RG fixed point; no regulator independence; no continuum limit; no G3 PASS; no K5 promotion; no Einstein/matter/observable claim.

## Exact next admissible step

Define one **minimal source-faithful causal refinement experiment** prospectively as new RG structure. The preferred highest-information choice is a same-boundary 4D simplicial refinement (e.g. a Pachner/refinement cluster) built from the causal-Toller vertex, with:

- explicit internal causal-orientation compatibility;
- standard spin/intertwiner sums and face/edge measure frozen;
- boundary embedding map frozen;
- the local supported extension coefficient(s) carried as explicit couplings;
- a coarse/fine observable or amplitude matching condition;
- PASS/FAIL/BLOCKED criteria for whether the map closes on the chosen coupling family.

Before numerical RG flow, first test whether the **multi-vertex causal data and measure are themselves well-defined** on that minimal refinement. If not, return `BLOCKED_MULTI_VERTEX_CAUSAL_OBJECT_DEFINITION` rather than inventing missing dynamics.