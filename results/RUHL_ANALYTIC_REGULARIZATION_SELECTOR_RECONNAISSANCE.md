# Rühl analytic-regularization reconnaissance for the corrected K5 extension problem

Date: 2026-09-14
Status: **SOURCE-MOTIVATION NOTE — NOT A SELECTOR RESULT**

## Motivation
After the right-SU(2) repair, the demonstrated local ambiguity is finite but nontrivial: Iter081R leaves at least 28 scalar `SO(3) x S5` invariant normal-jet coefficients through order 8. Researcher Iter081T independently confirms that CRQN v0.1/v0.2 contain no pre-existing rule fixing them.

A useful next mechanism must therefore be independently motivated before its coefficient consequences are calculated.

## Rühl primary authority
Werner Rühl, *Lectures on the Lorentz Group and Harmonic Analysis* (CERN Academic Training Lectures, 1967-68), Chapter 4 on harmonic analysis of polynomially bounded functions on `SL(2,C)`, explicitly treats generalized functions and representation functions of the second kind.

In the discussion following the second-kind Fourier transform, Rühl states that if one allows a polynomially bounded function rather than a regular distribution, one can obtain the final distribution from a regular one by **analytic continuation in a parameter**. He gives as one possible device multiplication by a power `|a|^(2 sigma)` followed by continuation from a sufficiently negative/regular value to `sigma=0`.

The same passage explicitly warns that this is **not necessarily the most convenient device** and discusses essentially arbitrary contour deformations / different continuation procedures when singularities and second-kind fixed poles are present.

Therefore Rühl supplies independent historical/source motivation for analytic regularization of polynomially bounded Lorentz-group functions, but does **not** supply a unique K5 renormalization/extension prescription.

## Relation to BCG
BCG `arXiv:2604.24945v1` uses Rühl's second-kind/Toller functions and proves equivalence of their one-wedge analytic definition with the spectral Feynman `i epsilon` projector. That uniqueness is a one-wedge statement for `beta>0` in the representation parameter and does not determine distributions supported only at a simultaneous K5 collision.

The Rühl continuation remark is broader in spirit but still does not specify:

- which common K5 analytic parameter(s) to introduce;
- whether the regularizer is edgewise, graphwise or transverse-radial;
- the path to the physical point;
- subtraction/minimal-part convention at poles;
- normalization scale;
- compatibility with node-wise right `SU(2)`, `S5`, true boundary covariance and source ordering;
- whether different admissible analytic families differ by the 28 repaired local jets.

## Candidate mechanism worth testing
A legitimate successor may prospectively freeze a **correlated transverse analytic family** for the already source-ordered, fully boundary-contracted K5 object, for example schematically

`u_s = R^(2s) u`

where `R^2` is a source-covariant positive quadratic normal function around `N=SU(2)^4`, or an equally explicit edgewise analytic family. The family must first be justified from the exact K5 geometry and symmetries; it may not be selected after inspecting the desired finite part.

Then the gate should determine:

1. meromorphic continuation to the physical point;
2. pole order and residue distributions;
3. whether a finite part exists;
4. dependence on analytic family / subtraction scheme / scale;
5. which of the 28 invariant scalar jets are fixed versus shifted under admissible scheme changes;
6. compatibility with the off-collision source amplitude and with causal orientation sums.

## Critical warning
Choosing one analytic family and taking its finite part would construct **an extension**, but uniqueness requires more. A different analytic family, scale, subtraction convention or continuation path can differ by distributions supported on the collision set. Those differences live precisely in the repaired extension-ambiguity space unless a theorem removes them.

Thus analytic regularization is now a scientifically motivated candidate mechanism, not a solved selector.

## Recommended prospective gate
`RUHL_MOTIVATED_CORRELATED_K5_ANALYTIC_REGULARIZATION_SCHEME_DEPENDENCE_GATE`.

Before any calculation freeze:
- exact analytic family;
- invariant transverse norm/edge functions;
- scale convention;
- subtraction rule;
- source ordering;
- symmetry requirements;
- comparison class of admissible alternative schemes;
- claim ceiling.

Primary success criterion should not be merely `finite part exists`. It should ask whether the prescription is **scheme-independent or source-uniquely normalized on the demonstrated invariant jet subspace**. If not, it is a construction, not yet a predictive selector.

## Claim ceiling
This note does not assert existence of the K5 meromorphic continuation for a particular proposed family, uniqueness of any finite part, regulator independence, causal-vertex finiteness/divergence, G3/F9/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete QG.
