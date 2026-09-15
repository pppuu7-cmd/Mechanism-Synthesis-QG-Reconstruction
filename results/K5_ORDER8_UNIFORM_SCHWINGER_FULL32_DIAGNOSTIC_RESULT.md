# K5 order-8 uniform-Schwinger full-32 diagnostic — production result

Date: 2026-09-15
Status: **DIAGNOSTIC_EXACT**

This result is subordinate to the frozen scientific gate
`ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR_K5_LANE`.
It does **not** assign a K5 zero/nonzero residue verdict.

## Provenance

- implementation: `scripts/k5_order8_uniform_schwinger_full32_diagnostic.py`, commit `6540f6eb7e8a6ed96a5ce7ee1f77afa1a7a0156f`;
- workflow/head: `.github/workflows/k5_order8_uniform_schwinger_full32_diagnostic.yml`, commit `ed1ddd8ec1795c41d4f6e7f08e6327f47eec3626`;
- production run `35016971583`, terminal `success`;
- job `104542736600`, terminal `success`;
- artifact `10415972092`, `k5-order8-uniform-schwinger-full32-diagnostic`;
- artifact ZIP digest `sha256:e7143b217800f6a647d50fb4f7a20c5a8d6b51ca77fa55b8d6d82af688959fd1`;
- production JSON SHA256 `3aa0174973ed75ce53ee654bde73de16c3b48089d416d369ef9184228627c863`.

## Exact sparse Gaussian structure

At the symmetric positive Schwinger point `alpha_e=1` for all ten K5 edges, the gauge-fixed edge-vector covariance is recomputed exactly from the inverse reduced K5 Laplacian.

Production finds:

- diagonal edge covariance: `2/5`;
- adjacent distinct edge covariance magnitude: `1/5`, with orientation-dependent sign;
- disjoint-edge covariance: exactly `0`.

For ten distinct linear edge factors there are `9!!=945` perfect Wick matchings. Because every disjoint-edge covariance vanishes, only **144** matchings survive.

This count is generated mechanically; it is not inserted as a verdict literal.

## Full source contraction

The diagnostic imports the authoritative source half-edge conventions and exact stripped four-spin node tensors from
`distributional/iter077i_sm_source_ordered_jhalf_k5_l1.py`.

It evaluates all `2^5=32` boundary components and all node-state terms. The exact number of source node-choice terms summed across the full boundary basis is

`(4+6)^5 = 100000`.

Production verifies all `100000` terms were included.

For each source state term, the ten exact matrix entries are reduced to their Gaussian-integer linear coefficient vectors and contracted with the 144 surviving Wick matchings.

## Exact result at the symmetric projective point

The Gaussian moment of the complete degree-ten leading numerator is nonzero in

**30 of 32 boundary components**.

Exactly two stripped boundary basis components vanish at this symmetric point:

- `(0,1,0,1,0)`;
- `(1,0,0,0,1)`.

All other 30 are exact nonzero rationals in the chosen stripped source basis. The imaginary parts vanish exactly at this symmetric point.

Examples:

- `(0,0,0,0,0) -> 128/625`;
- `(0,0,0,1,1) -> -384/625`;
- `(1,1,1,1,1) -> -3712/3125`.

## Order-eight source-radial probe

For the source K5 quadratic radius,

`S = sum_e |v_e|^2 = 5 R_K5^2`

at the symmetric Schwinger point.

For homogeneous numerator degree ten in normal dimension twelve,

`integral N_10 S^4 exp(-S) = (11)_4 integral N_10 exp(-S)`.

Therefore the order-eight radial probe `(R_K5^2)^4` differs here by the exact nonzero factor

`(11*12*13*14)/5^4 = 24024/625`.

It has the same 30/2 nonzero/zero pattern.

## Scientific consequence

The projective Schwinger integrand of the actual full-source K5 order-eight radial-probe lane is **not identically zero**: it has an explicit exact nonzero value at an interior positive projective point and is nonzero in 30 full boundary components there.

This is stronger than the earlier pointwise collision-ray reachability result because the present statement is after exact Gaussian/Wick contraction in the Schwinger representation of the order-eight probe.

However an interior nonzero value does **not** prove that the full nine-dimensional projective simplex integral is nonzero. Exact cancellations over the simplex remain logically possible.

Therefore no `K5_ACTUAL_ORDER8_POLAR_NORMAL_JET_NONZERO_EXACT_SCOPED` verdict is assigned yet.

## Next highest-information gate

Derive the actual projective invariant-dual integrand away from the symmetric point and seek one of:

1. an exact sign-definite representation for a nonzero boundary functional;
2. an integration-by-parts / graphical-function reduction to a manifestly nonzero positive period;
3. an exact analytic evaluation;
4. if sign changes occur, a rigorous noncancellation certificate.

High-precision numerical integration may be used only to choose among proof strategies, not as the scientific verdict.

## Interpretation ceiling

No K5 residue nonzero theorem yet; no physical finite part; no unique extension; no regulator-independence theorem; no global patching; no F9/G3 promotion; no new physics or complete-QG claim.
