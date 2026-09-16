# K5 invariant-dual degree-27 numerator materialization audit

Date: 2026-09-16

Status: OUTCOME-INDEPENDENT OBJECT AUDIT for the successor to the degree-four Kirchhoff-annihilator gate. This file does not assume or assign the degree-four production outcome.

## Question

Are the two exact invariant-dual projective numerator polynomials `N_1(alpha), N_2(alpha)` of degree 27 already materialized in the repository in coefficient form, so that a future logarithmic/annihilator derivation can act on them exactly?

## Existing exact authority

The all-32 invariant-dual reachability validator `scripts/k5_order8_invariant_dual_projective_ibp_reachability.py` establishes the exact projective form

`Omega_9 * prod_e alpha_e^(1/2) * N_c(alpha) / Psi_K5(alpha)^(21/2)`

with `deg N_c=27`, reconstructs the 32D boundary S5 action, and obtains the exact two-dimensional invariant dual/covector projection.

However, its actual full-32 Wick computation `uniform_full32_radial` first constructs the **uniform numerical covariance matrix** from the inverse unweighted reduced K5 Laplacian and then performs exact rational Wick contractions at that one Schwinger point. The output contains the two exact uniform projected coordinates, not sparse coefficient tables for `N_1(alpha)` and `N_2(alpha)`.

The structural reduction `scripts/k5_order8_schwinger_projective_reduction.py` independently establishes the K5 Kirchhoff denominator, 125 spanning trees, degree counting, Wick order nine, and common-scale exponent. It likewise does not emit the two degree-27 numerator coefficient maps.

Thus the current repository authority determines the two numerator channels algorithmically and structurally, but does not yet expose them as reusable exact polynomial objects.

## Consequence for the next admissible projective-IBP gate

A future action of a Kirchhoff logarithmic derivation or annihilator on the **actual** invariant-dual channels may not substitute a representative boundary component, a uniform point, or an arbitrary degree-27 polynomial.

The next gate must first materialize the two exact numerator objects from the same authoritative ingredients:

1. exact source leading edge-entry coefficients from `distributional/iter077i_sm_source_ordered_jhalf_k5_l1.py`;
2. exact reduced weighted K5 Laplacian `L(alpha)`;
3. exact `Psi_K5(alpha)=det L(alpha)` and polynomial adjugate entries;
4. all nine Wick contractions of the total degree-18 Gaussian numerator/probe object;
5. all 32 boundary components and all source node choices;
6. the exact dual/covector Reynolds projection, not the vector projection.

The materialization must emit deterministic sparse degree-27 coefficient maps (or an exactly equivalent canonical DAG with coefficient identity/hashes), together with independent evaluation controls at the uniform point reproducing

`(-9225216/9765625, -7175168/9765625)`

in the frozen RREF dual basis.

## Projective-form caution

Even after an exact `v(Psi_K5)=0` annihilator is available, a valid projective integration-by-parts identity still requires a correctly projective `(n-2)`-form and explicit Schwinger-simplex boundary analysis. The explicit factor `prod_e alpha_e^(1/2)` is part of the actual integrand and cannot be dropped when differentiating the numerator/measure factor.

## Interpretation ceiling

This audit identifies a missing reusable coefficient representation, not a missing scientific source object. It does not make either invariant-dual period zero/nonzero, does not assign the degree-four annihilator outcome, and does not select a physical finite part.
