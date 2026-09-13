# DSIR orientation-provenance reconciliation — exact displayed factor, saddle selection, off-saddle support and quadratic descent

**Date:** 2026-09-13

## Purpose

Two independently developed Iter076N-labelled audits answer different questions. They are compatible once their scopes are stated explicitly. This note freezes that scope grammar for the DSIR -> Polygon handoff and prevents either result from being overextended.

## Layer 1 — universal displayed scalar factor: negative

`results/ITER076N_EXACT_AMPLITUDE_ORIENTATION_SELECTOR_PROVENANCE_RESULT.md` establishes a narrow exact statement about the displayed Eq.(4)/(7) product/measure skeleton, causal `sigma/kappa` data and generic boundary-state representation:

- simultaneous label relabeling of the displayed wedge-product/Haar scalar coefficient carries the trivial character;
- `sigma/kappa` alone cannot provide an alternating scalar because every causal orbit has odd stabilizers;
- the generic boundary space is not restricted to the one-dimensional sign representation;
- `Omega_sigma(g)` is constructible from exact variables but constructibility is not the same as an explicit universal amplitude prefactor.

Therefore there is **no universal source-native explicit alternating scalar factor of that narrow form**.

This result does not rule out amplitude selection through support restrictions, stationary phase, phases, magnetic/intertwiner contractions, correlated boundary data or full-integral interference.

## Layer 2 — non-degenerate Lorentzian Regge saddle locus: positive

`results/ITER076N_TOLLER_RESTRICTOR_OMEGA_SADDLE_SELECTION_RESULT.md` establishes

`ITER076N_EXACT_TOLLER_RESTRICTOR_SELECTS_ONE_OMEGA_SECTOR_ON_NONDEGENERATE_LORENTZIAN_REGGE_SADDLE_LOCUS_SCOPED`.

The exact Toller restrictor admits the causal-compatible `+` Lorentzian critical branch and rejects the parity-related `-` branch over the frozen exhaustive causal-saddle census. The two critical branches carry opposite `Omega_sigma` signs.

Hence the Hodge-line sign is **source-selected on this saddle locus**, and a signed P3/Hodge representative is meaningful there.

This is an amplitude-selection result, not an explicit universal scalar-prefactor result, so it does not contradict Layer 1.

## Layer 3 — exact off-saddle bulk support: both signs present

`results/ITER076O_EXACT_TOLLER_OFF_SADDLE_OMEGA_SUPPORT_RESULT.md` establishes

`ITER076O_EXACT_TOLLER_BULK_SUPPORT_CONTAINS_BOTH_OMEGA_SECTORS_OFF_SADDLE_NO_GLOBAL_FINITE_SPIN_SELECTOR_SCOPED`.

For fixed causal data, open exact Toller bulk-support configurations exist with both nonzero signs of `Omega_sigma`. Therefore Heaviside/support information alone does not extend the saddle selector to generic finite spin.

This does not prove that both sectors survive the complete integration; full-integrand weighting/interference remains a distinct question.

## Layer 4 — known exact Toller conjugation: not an internal causal pairing

`results/ITER076P_TOLLER_CONJUGATION_CAUSAL_FACTOR_OBSTRUCTION_RESULT.md` establishes

`ITER076P_EXACT_TOLLER_CONJUGATION_FLIPS_OUTSIDE_SOURCE_CAUSAL_K5_IMAGE_NO_SAME_CAUSAL_SELECTOR_SCOPED`.

The exact gamma-simple conjugation identity flips every wedge branch. The globally flipped ten-wedge pattern violates the source-factorizable K5 triangle constraints: `0/16` flipped patterns lie in the causal image. Thus this conjugation cannot pair/cancel opposite `Omega` sectors **within the same fixed causal vertex**.

Other parity/boundary/full-integral mechanisms are not excluded.

## Layer 5 — homogeneous quadratic Hodge transport: global sign disappears

`results/ITER076Q_HODGE_LINE_SYM2_QUADRATIC_DESCENT_RESULT.md` establishes

`ITER076Q_HODGE_LINE_DESCENDS_TO_UNTWISTED_SYM2_QUADRATIC_TRANSPORT_EXACT_SCOPED`.

Although the linear Hodge map remains sign-twisted, its symmetric square satisfies

`Sym2(+X)=Sym2(-X)`

and transforms with ordinary untwisted S4 covariance. Therefore the unresolved generic finite-spin sign does not by itself obstruct **homogeneous degree-two transport through the exact linear Hodge line**.

This does not define the physical nonlinear source-to-K4 pushforward: a source one-jet can still feed degree two through nonlinear coordinate curvature.

## Frozen scope matrix

| Question | Status |
|---|---|
| Is there a universal explicit Eq.(4)/(7) alternating scalar prefactor from product/Haar + `sigma/kappa` + generic boundary representation? | `NO_GO_SOURCE_NATIVE` in this narrow sense |
| Is one orientation selected on the non-degenerate Lorentzian Regge stationary locus? | `PASS_SOURCE_NATIVE_SCOPED` |
| Does exact off-saddle Toller bulk support alone select one orientation? | `NO` |
| Does known exact Toller conjugation provide a same-causal opposite-orientation pairing/cancellation? | `NO` |
| Is generic finite-spin signed P3 established? | `BLOCKED` |
| Does the `+H/-H` ambiguity obstruct homogeneous quadratic linear transport? | `NO`; `Sym2` descends exactly |
| Is the physical degree-two numerator/Jacobian jet established? | `BLOCKED_OBJECT_DEFINITION` |
| Is the nominal `epsilon^-1` coefficient established? | `NO` |

## Polygon handoff rule

The conservative P0 branch must export both facts simultaneously:

1. `SADDLE_EFFECTIVE_SIGNED_P3 = PASS` on the explicitly frozen non-degenerate Lorentzian Regge saddle locus;
2. `GENERIC_FINITE_SPIN_SIGNED_P3 = BLOCKED` off saddle.

P0 may nevertheless use the exact sign-independent `Sym2` Hodge transport for homogeneous quadratic algebra, subject to the remaining source-one-jet/nonlinear-curvature provenance gate.

Any stronger generic orientation rule remains an explicit extension/result and cannot be inferred by silently extrapolating the saddle classification.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no generic finite-spin signed P3; no exact full-amplitude cancellation/non-cancellation theorem; no physical causal-vertex finiteness/divergence theorem; no nominal `epsilon^-1` coefficient; no G3/F9/G8/K5 promotion.
