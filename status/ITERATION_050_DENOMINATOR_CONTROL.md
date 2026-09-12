# Iteration 050 independent control — denominator-only K4 pole topology

**Date:** 2026-09-12

This is an independent, response-blind control running in parallel with Iter050. It does **not** use any Iter050 RR labels and cannot modify the Iter050 classifier.

## Question
For the ordinary no-contact `F=1` K4 rational kernel, is the ordered upper/lower Feynman pole-count topology determined only by the factorized causal sign class and cycle basis/pair, or can it change when only positive epsilon magnitude or real external K4 flow are varied?

## Frozen grid
Enumerate all eight K4 factorized causal sign classes modulo the global sigma flip by fixing `sigma0=+1` and taking `sigma1,sigma2,sigma3=+/-1`. Convert to edge signs `kappa_ab=sigma_a*sigma_b` in edge order `01,02,03,12,13,23`.

Trees: `S0,S1,P0,P1`.
Pairs: `01,02,12`.

For each sign class/tree/pair evaluate the no-contact `F=1` kernel at four nuisance variants:
- epsilon=0.04, k=(0.23,-0.34,0.18,-0.07)
- epsilon=0.14, same k
- epsilon=0.04, k=(-0.17,0.29,-0.33,0.21)
- epsilon=0.14, same alternate k

Use gamma=1 only as inert metadata; `F=1` has no gamma-dependent numerator.

For ordered paths `i->j` and `j->i`, record
`(upper_count(first R), upper_count(second R-after-R))`, total pole counts, and all exact `R+A` reconstruction checks.

Matrix implementation: 8 sign classes × 4 trees = 32 independent jobs; each job evaluates all 3 pairs × 4 nuisance variants locally.

## Frozen classifier
- `DENOMINATOR_POLE_TOPOLOGY_CONTROL_INVALID` if any exact reconstruction/control calculation fails.
- `DENOMINATOR_POLE_TOPOLOGY_EPS_OR_K_DEPENDENT` if any sign/tree/pair signature changes across the four nuisance variants.
- `DENOMINATOR_POLE_TOPOLOGY_SIGN_GEOMETRY_STABLE` if all signatures are invariant to positive epsilon magnitude and real external k on the frozen grid.

No relationship to source RR activation is fitted in this control. Its only purpose is to establish the denominator-only baseline against which Iter050 source numerator/cancellation effects can later be interpreted.
