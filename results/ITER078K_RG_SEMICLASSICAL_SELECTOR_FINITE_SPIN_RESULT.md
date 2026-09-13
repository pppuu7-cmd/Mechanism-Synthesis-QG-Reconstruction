# Iter078K-RG result — published large-spin causal rigidity does not select the exact finite-spin K5 extension

**Date:** 2026-09-14

## Provenance

- Prospective preregistration: `prereg/ITER078K_RG_SEMICLASSICAL_SELECTOR_FINITE_SPIN_EXTENSION.md`, commit `9fc2e38be7593ed3923aad06aab47fdc7232b35a`.
- Source derivation: `sources/ITER078K_RG_SEMICLASSICAL_SELECTOR_DERIVATION.md`, commit `a1851dbc6d110be1ace8db81d2503f1f4f159108`.
- Primary authority: Bianchi-Chen-Gamonal large-spin causal-vertex asymptotics.
- Finite-spin ambiguity authority: Iter078G-RG.

## Classification

`ITER078K_RG_PUBLISHED_LARGE_SPIN_CAUSAL_RIGIDITY_DOES_NOT_SELECT_EXACT_FINITE_SPIN_K5_EXTENSION_COUNTEREXAMPLE_SCOPED`

Scientific verdict: **PASS**.

## Exact counterexample

Choose any nonzero all-`j=1/2` integrated extension shift `ell in H_B^*`, realized locally by `ell(Psi) delta_N`, and set that shift to zero in every other spin sector.

This changes the exact finite-spin causal vertex on at least one all-`j=1/2` boundary state while preserving the off-collision Toller source object.

The published semiclassical theorem studies uniform scaling

`j_ab -> lambda j_ab`, `lambda -> infinity`

of a fixed nondegenerate Lorentzian Regge boundary geometry. Along every such large-spin ray the finite-support low-spin modification is exactly absent for all sufficiently large `lambda`.

Therefore the modified and unmodified amplitudes coincide identically on the full asymptotic tail. The published compatible-causal single Regge exponential, incompatible-causal suppression, power law, phase and causal-rigidity conclusion are unchanged.

## Source audit

No exact cross-spin recurrence, analyticity condition in the discrete spin labels, or normalization theorem was found in the frozen source that would reconstruct the all-`j=1/2` amplitude uniquely from the `lambda -> infinity` asymptotic data.

The fixed-spin identity `T+ + T-=D` does not relate different spin magnitudes, and Iter078I already shows that its EPRL sum consequence does not uniquely select one causal-sector extension.

## New scientific fact

The correct semiclassical causal behavior is **not sufficient** to fix the exact finite-spin causal vertex. Large-spin causal rigidity remains a necessary downstream consistency condition, but it leaves the established minimal finite-spin ambiguity untouched unless supplemented by an exact cross-spin law.

This closes another natural shortcut: one cannot choose a convenient finite part at low spin and justify it solely because the known Regge asymptotics is recovered.

## Interpretation ceiling

This result does not prove that arbitrary spin-by-spin extension choices are compatible with a complete theory. Refinement/RG, exact recurrences, continuum consistency, unitarity/transfer conditions or another independently motivated cross-spin law may correlate sectors and remove the finite-support freedom.

No generic-spin ambiguity theorem, RG fixed point, continuum limit, G3, Einstein/matter recovery or complete-QG conclusion follows.

## Exact next admissible step

The selector problem is now concentrated on **exact cross-scale/cross-spin structure**, not semiclassical asymptotics. Highest-information options are:

1. derive/test an exact refinement/cylindrical map that correlates finite-spin sectors;
2. search for a source-backed exact spin recurrence satisfied by the causal Toller vertex and test whether supported extension shifts lie in its kernel;
3. if neither exists, keep the exact finite-spin vertex `BLOCKED_NONUNIQUE_EXTENSION_SELECTOR_MISSING` even though its semiclassical saddle structure is known.