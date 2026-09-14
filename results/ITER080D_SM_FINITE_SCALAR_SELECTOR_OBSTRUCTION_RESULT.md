# Iter080D-SM — finite scalar selector obstruction

**Date:** 2026-09-14

## Frozen contract

Prospective preregistration: `prereg/ITER080D_SM_FINITE_SCALAR_SELECTOR_OBSTRUCTION.md`, commit `a61780f9f84cf2ecff0e4a09993322f37e310d4c`.

The frozen object is the actual Iter077Q source-compatible ambiguity subspace

`W = span_C{h_n : n>=0}`, `h_n = Q^n F_SU2 delta_N`,

and the frozen selector class is any fixed finite list of scalar-valued complex-linear conditions

`L=(L_1,...,L_m): W -> C^m`, `m<infinity` fixed independently of truncation dimension.

Function-valued/infinite condition families, differential/spectral/microlocal equations and nonlinear selectors were prospectively excluded from the theorem's scope.

## Source lock

Frozen source-lock matrix: `analysis/iter080d_sm_source_lock.json`, commit `24e4f8a33efe9305e62656bf942157b00223ca62`.

The gate uses the authoritative Iter077Q theorem only: `Q(g)=sum_(a<b) tr_1/2(g_b^-1 g_a)`, exact compact path `Q(t)=12+8 cos(t)`, and for an actual minimal-sector boundary state with nonzero compact boundary functional the family `{Q^n F_SU2 delta_N}_{n>=0}` is linearly independent. Iter077Q terminal authority remains run `34792482045`, aggregate artifact `10328598487`, digest `sha256:58e3cb389a985838942a4d0181e6e680cdd75480cfc24e0ec7bb07d73b199a96`, result commit `5941b3a064d93f2898d9e9a48545826e950455f1`.

The controlling contact erratum remains `status/ITER077_CONTACT_FORMULA_ERRATUM.md`, blob `63356e5099929f2b21d9d7296ab97f15ff163dba`; historical Iter077E/F remain quarantined.

## Execution provenance

Implementation was first committed as `965a9dbcb4fe44b0148a8a7d6317e2d307691dc1`; workflow added at `1d561cfe4e076f3d2674ebe0fc06c9ecaa6391c4`.

Initial run `34826699091` terminated `failure` because Lane A used an overly brittle string matcher for the already-correct erratum formula. Its own output explicitly marked `erratum_correct_formula=false` and `INVALID_SOURCE_LOCK`; no scientific verdict is taken from that run.

A control-only implementation repair changed only that source-lock matcher, without changing the preregistered object, selector class, theorem, controls or interpretation ceiling. Repair commit: `849eddbac5fab7dd44fdea3b6d2b3f083a8e9c9a`.

Authoritative terminal run: `34826763762`, conclusion `success`.

Jobs:

- Lane A source lock: job `103920609411`, success, `PASS_SOURCE_LOCK`.
- Lane B exact theorem: job `103920609532`, success, `PASS_EXACT_THEOREM`.
- Lane C scope control: job `103920609201`, success, `PASS_SCOPE_CONTROL`.
- Aggregate: job `103920666567`, success.

Artifacts:

- `iter080d-sm-A`: ID `10339814856`, digest `sha256:0391417bfd226f41adb28cc67ea2ca5004169296a6556d5b68daa815d4fd4aaa`.
- `iter080d-sm-B`: ID `10340518518`, digest `sha256:de5ce82b150dfcb64b90ff696047e9d5d897ddd93949f0868d5aa3b4652ca7bf`.
- `iter080d-sm-C`: ID `10339583938`, digest `sha256:654061a9c7df98cf99573c4058b69d36fcd1eae70059f7464ce499916c3d5102`.
- `iter080d-sm-aggregate`: ID `10339603905`, digest `sha256:835762c129e220d66cb7dab7b2e7a19da98e6f1b8e60e32cdf80764d71b78f36`.

Durable aggregate: `results/raw/ITER080D_SM_AGGREGATE.json`, commit `4c26dd49531be05195881c7c5c8a8ccfac363c5c`.

Green CI is execution evidence only; the scientific result is the frozen exact theorem below.

## Exact theorem

For any fixed finite `m` and any complex-linear `L:W->C^m`, restrict `L` to

`W_N = span{h_0,...,h_N}`.

Iter077Q linear independence gives exactly `dim W_N=N+1`. Rank-nullity gives

`rank(L|W_N) <= m`,

so

`dim ker(L|W_N) >= N+1-m`.

For any requested finite kernel dimension `R>=1`, choose `N=m+R-1`. Then

`dim ker L >= dim ker(L|W_N) >= R`.

Since `R` is arbitrary, `ker L` is infinite-dimensional. Therefore no map in the frozen selector class can be injective on `W`, and no fixed finite list of scalar-valued linear renormalization/normalization conditions can uniquely select the K5 extension inside the already-established Iter077Q ambiguity family.

Frozen projection controls give exact nullities:

- `(m,N)=(1,8)`: rank `1`, nullity `8`;
- `(2,16)`: rank `2`, nullity `15`;
- `(4,32)`: rank `4`, nullity `29`;
- `(8,64)`: rank `8`, nullity `57`.

Negative control: the identity `W_N -> C^(N+1)` has rank `N+1` and nullity `0`. Thus the theorem does not forbid a number of independent conditions growing without bound with the ambiguity dimension; that class was deliberately outside the frozen hypothesis.

## Verdict

`PASS_EXACT_SCOPED`

Classification:

`ITER080D_SM_FIXED_FINITE_SCALAR_LINEAR_RENORMALIZATION_CONDITIONS_CANNOT_SELECT_ITER077Q_INFINITE_FUNCTION_SPACE_AMBIGUITY_EXACT_THEOREM_SCOPED`

## New scientific fact

The source-compatible K5 extension ambiguity is not only too large for a single scalar finite part or finite permutation-covariance condition. The exact Iter077Q infinite-dimensional subspace cannot be uniquely removed by **any fixed finite number of scalar-valued linear renormalization conditions**. A successful selector, if one exists, must therefore contain genuinely more information: for example a source-derived function-valued/infinite family of constraints, a differential/spectral/microlocal condition, or another independently motivated structure outside this theorem's class.

## Interpretation ceiling

This theorem does **not** prove that no extension selector exists. It does not exclude function-valued or infinite condition families, differential/spectral/microlocal equations, or nonlinear selectors. It does not establish a unique K5 extension, full causal-vertex divergence/nonexistence, regulator independence, E7/E8 closure, G3, RG, continuum GR, F9/G8/K5 promotion, or new physics.

The local CRQN amplitude therefore remains `BLOCKED_INFINITE_DIMENSIONAL_EXTENSION_SELECTOR_MISSING`.

## Next admissible gate

Do not repeat finite-group symmetry variants or finite scalar normalization/counterterm controls. The highest-information successor is a source-authority audit for a **genuinely function-valued, differential, spectral or microlocal joint-K5 extension condition** derivable from the primary causal/Toller construction. If the exact sources do not supply such a condition or an independently motivated CRQN axiom does not prospectively define one, retain `BLOCKED_OBJECT_DEFINITION`; do not invent a post-hoc selector.

Claim locks remain unchanged: no `NEW_PHYSICS_FOUND`; no complete-QG claim; no generic finite-spin signed P3; no exact full-amplitude cancellation/non-cancellation theorem; no causal-vertex finiteness/divergence theorem; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal `epsilon^-1`; no G3 PASS; no F9/G8/K5 promotion; retain published spectral `i epsilon`.
