# Iter080D-SM — Finite scalar renormalization conditions cannot select the K5 function-space ambiguity

**Status:** PROSPECTIVELY FROZEN BEFORE SUBSTANTIVE COMPUTATION
**Date:** 2026-09-14

## HYPOTHESIS

Let

`W = span_C{ h_n : n >= 0 }`, `h_n = Q^n F_SU2 delta_N`,

be the exact source-compatible ambiguity subspace established by Iter077Q. Any proposed extension selector that acts on `W` only through a fixed finite number `m < infinity` of scalar-valued linear renormalization conditions

`L=(L_1,...,L_m): W -> C^m`

cannot uniquely select the extension: `ker L` remains infinite-dimensional. Consequently a successful selector for the already-established Iter077Q ambiguity must contain more information than a fixed finite list of scalar linear normalization/counterterm conditions; e.g. it may require a function-valued/infinite family of constraints, a differential/spectral equation, or other independently source-derived functional input.

## exact OBJECT

The true Iter077Q source-compatible K5 supported ambiguity subspace only:

`W = span_C{Q^n F_SU2 delta_N}_{n>=0}`

on the common-collision submanifold `N=SU(2)^4 subset SL(2,C)^4`.

This is not a scalar K4/K5 surrogate and does not replace the full source-ordered Toller amplitude. The gate concerns only whether a broad class of prospective **selectors** could remove an ambiguity already proven to exist for the true source object.

## DEPENDENCY

`local source-ordered amplitude -> distributional extension selector -> causal composition/E7-E8 -> G3 -> regulator removal -> RG -> continuum -> spin-2 -> Einstein -> matter/QFT -> prediction`.

A selector that cannot distinguish all directions in `W` cannot close the local-amplitude definition.

## SOURCE AUTHORITY

Repository-authoritative exact results only:

1. Iter077L-SM: collision `N=SU(2)^4`, real codimension `12`, transverse scaling degree `20`; same-scaling-degree extensions admit supported normal-jet ambiguity through order `8` with smooth tangential coefficient data.
2. Iter077Q-SM: exact theorem that `W` contains the linearly independent family `h_n=Q^n F_SU2 delta_N`, with `Q` common-left `SL(2,C)` invariant, fully `S5` invariant, and `Q(t)=12+8 cos(t)` on the frozen compact path for an actual boundary component with nonzero `F_SU2`.
3. Controlling `status/ITER077_CONTACT_FORMULA_ERRATUM.md`; historical Iter077E/F remain quarantined.

No external or new source formula is introduced in this gate.

## FROZEN INPUTS

- Field: complex scalars.
- Ambiguity basis: exactly `{h_n}_{n>=0}` from Iter077Q; no new ambiguity directions are needed.
- Selector class: a **fixed finite** number `m` of scalar-valued linear functionals `L_i:W->C`; `m` is independent of truncation size `N`.
- Finite truncations: `W_N=span{h_0,...,h_N}` for controls.
- Frozen witness pairs `(m,N)` with `N>=m`: `(1,8)`, `(2,16)`, `(4,32)`, `(8,64)`.
- Positive exact rank control matrices: first-`m` coordinate projections on `W_N`, rank exactly `m`.
- Negative control: for each finite `N`, the identity map `W_N -> C^(N+1)` has zero kernel, demonstrating that a number of independent scalar conditions growing with `N` lies outside the fixed-finite-`m` obstruction.
- No regulator limit, quadrature, floating-point tolerance, post-hoc boundary state, or surrogate pushforward enters.

## POSITIVE CONTROLS

1. Verify from the frozen Iter077Q authority that `{h_n}` is linearly independent and hence `dim W_N=N+1`.
2. For every frozen `(m,N)`, exact coordinate-projection control has rank `m` and nullity `N+1-m`.
3. General theorem lane must use only rank-nullity: for arbitrary linear `L|_{W_N}:W_N->C^m`, `rank<=m`, so `nullity>=N+1-m`.

## NEGATIVE CONTROLS

1. `GROWING_CONSTRAINT_SET`: identity `W_N->C^(N+1)` has nullity zero; the gate must therefore **not** claim that an infinite/function-valued family of independent conditions cannot select.
2. `NONLINEAR_OR_PDE`: nonlinear selectors, differential equations, spectral equations, microlocal conditions, or function-valued constraints are outside the frozen theorem unless separately reduced to a fixed finite scalar linear map.
3. `FULL_VERTEX_PROMOTION`: selector obstruction is not a causal-vertex divergence/nonexistence theorem and cannot be promoted to G3/RG/F9/G8/K5.

## PASS

`PASS_EXACT_SCOPED` iff:

- Iter077Q source lock establishes linearly independent `{h_n}`;
- exact rank-nullity proves that for every fixed finite `m` and every scalar-linear selector `L:W->C^m`, `ker L` is infinite-dimensional; and
- all frozen positive and negative controls behave as specified.

## FAIL

`SCIENTIFIC_FAIL_EXACT_SCOPED` iff an exact counterexample within the frozen class exists: a fixed finite `m` scalar-linear map `L:W->C^m` that is injective on the established infinite-dimensional `W`.

## BLOCKED

`BLOCKED_OBJECT_DEFINITION` iff the authoritative Iter077Q family cannot be source-locked or its linear independence is not available in the frozen scope.

## INVALID

- `INVALID_SOURCE_LOCK` if Iter077Q/Iter077L/erratum authority cannot be verified.
- `INVALID_IMPLEMENTATION` if the executable lanes merely test selected matrices but do not encode/check the universal rank-nullity argument and the negative-control scope.
- `INVALID_PROVENANCE` if computation/result precedes this preregistration.

## INTERPRETATION CEILING

A PASS eliminates only selectors consisting of a fixed finite number of scalar-valued linear renormalization conditions on `W`. It does **not** eliminate a source-derived function-valued constraint, an infinite family of conditions, a differential/spectral/microlocal selector, or a nonlinear selector. It does not prove that no extension selector exists.

It also does not establish a unique K5 extension, full causal-vertex finiteness/divergence, regulator independence, E7/E8 closure, G3, RG, continuum GR, or new physics.

Claim locks remain unchanged: no `NEW_PHYSICS_FOUND`; no complete-QG claim; no generic finite-spin signed P3; no exact full-amplitude cancellation/non-cancellation theorem; no causal-vertex finiteness/divergence theorem; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal `epsilon^-1`; no G3 PASS; no F9/G8/K5 promotion; retain published spectral `i epsilon`.
