# DSIR 100% completion roadmap

**Date:** 2026-09-13

**Purpose:** define an objective finish line for the DSIR research funnel before downstream polygon construction.

## Meaning of 100%

`DSIR_READY = 100%` does **not** mean that quantum gravity, the CRQN candidate, the continuum limit, or all G1-G8 gates are solved.

It means that every field in the DSIR -> polygon interface has a terminal, reproducible status and there are no anonymous `OPEN_BLOCKED` dependencies hidden inside the handoff.

A terminal field may be:

- `PASS_SOURCE_NATIVE`;
- `PASS_DERIVED_MSQGR`;
- `NO_GO_SOURCE_NATIVE`;
- `CONVERGENCE_ONLY`;
- `BLOCKED_TRANSFER_TO_POLYGON` with an explicit missing object, test and falsification criterion;
- `NOT_APPLICABLE` when an upstream no-go makes a downstream object undefined.

A failed/no-go gate can therefore complete the funnel if the no-go is itself reproducible and its downstream consequences are explicit.

## Frozen upstream state

Already available:

- provisional carrier: oriented causal labelled 2-complex `Q=(K,o,j,i,x)`;
- source-backed causal/Toller vertex definition and spectral `i epsilon` convention;
- K4 cut/cycle and Hodge-line structure through Iter076H;
- gauge-fixed K5 complement support through Iter076J;
- exact causal `sigma/kappa` global-sign obstruction through Iter076K;
- semiclassical Regge 4-volume pseudoscalar through Iter076L;
- exact-variable non-degenerate candidate `Omega_sigma(g)` through Iter076M.

None of these facts by itself promotes physical signed P3, G3, F9, G8 or K5.

## Critical path

### N — exact amplitude orientation provenance

Determine whether source Eq. (4)/(7), including generic boundary contractions, contains or uniquely forces an alternating `S5` orientation selector.

Terminal outcomes:

- source-native selector -> signed-P3 lane may continue;
- exact source no-go/unresolved -> source-native signed-P3 lane terminates and polygon extension lane must be explicitly separated.

### O — signed P3 assembly (conditional)

Run only if N authorizes it. Couple the source-provenanced orientation selector to the unique Iter076H Hodge line and test:

- all root choices;
- `S5/S4` relabeling covariance;
- proper Lorentz gauge changes;
- global causal reversal;
- degeneracy firewall.

If N blocks, O receives terminal `NOT_APPLICABLE_SOURCE_NATIVE` rather than a convention-fitted sign.

### P/Q — source numerator and Haar/Jacobian jet (conditional)

Only after a physical source-native P3 exists, derive the actual local source numerator, measure/Jacobian expansion and degree-two jet. Only then may the nominal `epsilon^-1` coefficient receive a value/classification.

If P3 is absent, the signed-P3-dependent coefficient remains terminally undefined in the source-native lane; it is not called zero or divergent.

### R — correlated K5 boundary-value object

Establish, or terminally exclude, the full correlated source-backed Toller/group boundary value. Required separation:

- finite spectral `i epsilon` object;
- absolute integrability;
- canonical distributional boundary value;
- extension/finite-part freedom;
- correlated versus sequential limits.

### S — finite-scale amplitude/composition contract

Freeze the smallest exact finite-scale dynamics package required by the polygon:

- local amplitude kernel/family;
- measure normalization convention;
- gluing/composition rule;
- physical boundary-space interface;
- exact causal projectors or a terminal missing-object definition.

This is the DSIR-side minimum for G3; full continuum dynamics remains downstream.

### T — RG/CCI handoff contract

Freeze the interface needed to test F9 and continuum behavior downstream:

- boundary spaces `H_b`;
- causal projectors `P_b^+-` if defined;
- allowed embedding/coarse-graining map class `iota_b'b`;
- cylindrical-consistency residual;
- CCI residual `P_b'^+- iota - iota P_b^+-`;
- closure test for Toller pole/analytic class.

DSIR does not need to prove a continuum fixed point to finish; it must make the downstream test executable and unambiguous.

## Mandatory DSIR exit package

The handoff is complete only when one authoritative manifest records:

1. carrier and equivalence/gauge relations;
2. source amplitude and spectral prescription;
3. causal/orientation data and exact/semiclassical distinction;
4. signed-P3 status and provenance;
5. distributional/K5 status;
6. numerator/Jacobian/`epsilon^-1` status with dependency graph;
7. boundary/composition interface;
8. RG/CCI interface;
9. terminal F9/G3/G8/K5 classifications at DSIR scope;
10. frozen claim locks;
11. authoritative preregistration/result/run/artifact hashes;
12. polygon branches and the extra assumptions each branch is allowed to add.

## Polygon responsibility

The polygon receives a constrained model space and tests the same-realization chain

`microstate -> dynamics/measure -> coarse graining -> continuum effective action -> normalized observables -> IR gravity/matter`.

Primary polygon responsibilities are therefore full G4-G7 closure, plus any downstream F9/G3/G8 tests whose exact inputs have been frozen by DSIR.

## Anti-retrofit rule

After `DSIR_EXIT_MANIFEST_V1` is frozen, the polygon may reject a DSIR object or open a clearly named extension branch, but it may not silently alter DSIR definitions to make a downstream gate pass.
