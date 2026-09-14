# Iter082A-SM independent nested partial-collision reproduction — RESULT

Date: 2026-09-14

## Prospective chain

- scientific prereg: `53cd6cea982192b80fe0e23434866dda97f46002`
- implementation: `52ac5fb9e4db1637305a2d2959273410bc03ffb6`
- initial production: `13efc08795fccda7d3ed7165d083cfa5d5cca476`
- historical run `34889953575`: **INFRASTRUCTURE/PROVENANCE FAILURE ONLY** before science, because shallow checkout could not resolve prereg ancestry
- control-only repair prereg: `6ce66ba01a6f8d91053cfb45ceea85be3d47114c`
- repaired production: `713c56360c8c83212758106d2bae88d787f04d06`
- authoritative repaired run: `34890026239`, job `104130077377`, terminal `success`
- artifact: `10366287380`, name `iter082a-sm-aggregate`
- artifact ZIP digest: `sha256:cc2ebbd62f85fe64dd74d687dd263b33e5fa6963a7713bc90fcb118ae0cd38bb`
- extracted aggregate JSON SHA256: `16af00dadd1ab991d8424689612fc7ef5afd5ed420d61b6cae5d67cc80660fa7`

Frozen scientific criteria were unchanged by the control-only repair.

## Classification

`ITER082A_SM_SOURCE_ORDERED_FULL_BOUNDARY_K3_LOG_AND_K4_POWER_PARTIAL_COLLISION_NONL1_WITNESSES_CONFIRMED_EXACT_SCOPED`

Verdict: **PASS_EXACT_SCOPED**.

## Exact results

Using the frozen Iter077I five-node two-dimensional SU(2)-invariant intertwiner basis and exact Gaussian-integer arithmetic:

- K4 nested partial collision: **32/32** boundary basis contractions are nonzero.
- K3 nested partial collision: **24/32** boundary basis contractions are nonzero.
- deepest all-plus sanity reproduction: **32/32** nonzero.
- K4 internal power `q_4=-12`, normal dimension `d_4=9`, absolute-L1 margin `q_4+d_4=-3`.
- K3 internal power `q_3=-6`, normal dimension `d_3=6`, absolute-L1 margin `q_3+d_3=0`, hence logarithmic absolute-L1 failure where the leading coefficient is nonzero.

The frozen fixed-external nonidentity argument is valid: a nonzero nested leading coefficient implies that the corresponding source-ordered fixed-external partial coefficient function is not identically zero, so sufficiently small fixed external configurations exist with nonzero fully boundary-contracted partial-stratum coefficient.

## Controls

All required controls passed:

- exact Gaussian-integer/integer arithmetic throughout;
- every frozen relative direction entering a leading denominator is nonzero;
- deliberately degenerate zero internal direction is rejected as inadmissible;
- deepest Iter077I all-plus witness is independently reproduced nonzero;
- for every proper-causal K5 assignment `epsilon_ab=eta sigma_a sigma_b`, total ten-edge branch parity is `+1` at the final nested all-edge leading level.

The causal parity control does **not** assert equality of exact finite-external-scale partial coefficients away from the deeper collision.

## Scientific consequence

The K3/K4 pieces of the Iter081X 72-forest object are not merely formal geometry. In the frozen minimal-spin source-ordered fully boundary-contracted sector there exist physical partial-collision configurations with non-L1 leading behavior:

- K4 requires a genuine power-divergent partial-stratum extension/subtraction treatment;
- K3 requires a genuine logarithmic partial-stratum extension/subtraction treatment.

Therefore a deepest-K5-only radial prescription cannot define the full local K5 object. The next admissible gate is `K5_SOURCE_COVARIANT_FOREST_EXTENSION_PRESCRIPTION_GATE`, with all K3/K4/K5 strata and nesting/order consistency treated prospectively.

## Claim ceiling

This does not prove divergence at every boundary state or every point, does not establish generic-spin behavior, and is not a distributional-nonexistence theorem. It does not choose subtraction coefficients, scales, forest order, invariant-jet selector, regulator-independent amplitude, G3/F9/G8/K5, `NEW_PHYSICS_FOUND`, or complete quantum gravity.
