# Iter080D-SM control-only repair plan

**Date:** 2026-09-14

This note records an authorized control-only repair under the unchanged prospective preregistration `prereg/ITER080D_SM_FINITE_SCALAR_SELECTOR_OBSTRUCTION.md` (`a61780f9f84cf2ecff0e4a09993322f37e310d4c`). It does **not** change the frozen scientific object, hypotheses, criteria, classification ceiling, or selector class.

Controlling Critic review: `results/ITER080D_ADVERSARIAL_IMPLEMENTATION_REVIEW.md` / handoff `status/MSQGR_ADVERSARIAL_CRITIC_HANDOFF.md`, verdict `INVALID_IMPLEMENTATION` for the historical production Lane B because its success predicate depended only on a finite `(m,R)` witness grid.

## Authorized repair

1. Lane B PASS must depend on an executable **symbolic universal certificate** for arbitrary symbolic positive integers `m,R`: set `N=m+R-1`; verify symbolically that `dim W_N=N+1=m+R`, `rank(L|W_N)<=m`, and therefore the rank-nullity lower bound is identically `R`. The success predicate must not depend on enumerating selected `m,R` values.
2. Finite projection examples may remain only as non-authoritative controls; they cannot certify universality.
3. Lane A may be hardened to compute the actual Git blob SHA-1 of the checked-out Iter077Q derivation and compare it with the frozen source-lock SHA.
4. Historical runs/artifacts/results remain preserved and non-authoritative. The repaired run must be separately terminalized and reviewed.

## Claim ceiling unchanged

Even on PASS this excludes only selectors consisting of a fixed finite number of scalar-valued complex-linear conditions `W -> C^m`. It does not exclude function-valued/infinite condition families, differential/spectral/microlocal equations, nonlinear selectors, or prove a unique K5 extension, full-vertex divergence, regulator independence, E7/E8, G3, RG, F9/G8/K5 promotion, complete QG, or new physics.
