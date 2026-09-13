# Iter075E result — exact Appendix-D branch-flip kernel identity

Date: 2026-09-13

## Authority

- preregistration commit: `5e6899e9a35043f24c48fdfdbaa2b1f436314a13`
- implementation commit: `2f9d7212e626a6c148b993b4f99b129a13e50c5b`
- authoritative workflow/head: `1905295fb7e96cc6652fc4edb48bd142748fd52a`
- workflow run: `34755819190`
- job: `103719893727`
- artifact: `10317735773` (`iter075e-exact-branchflip`)
- digest: `sha256:e9994dae30d1d2d12c1b3905e8370e0871dbafa15f276e116a835c89c7c751c3`

## Frozen classification

`ITER075E_APPENDIXD_BRANCHFLIP_KERNEL_IDENTITY_EXACT_SCOPED`

The terminal raw job log and artifact satisfy every frozen obligation in `status/ITERATION_075E_PREREG.md`.

## Exact result

For every admissible nonnegative half-integer pair with `2j,2l<=16` and `j+l` integer, the symbolic audit verifies the index-set reflection, factorwise conjugation and the exact identities

`P_jl(x;rho) = conjugate(P_lj(x;rho))`

and

`K_s(j,l) = -conjugate(K_-s(l,j))`

for real `x,rho` and fixed `epsilon>0` in the published Feynman-pole convention used by the frozen kernel. All exact residuals are zero. Inadmissible parity pairs are excluded rather than coerced. The deliberately wrong same-branch conjugation fails on unequal-spin controls, so the result is not an accidental equal-spin collapse.

## Scope guard

This promotes Iter075C/075D from numerical recurrence evidence to an exact Appendix-D polynomial/Feynman-kernel identity. It does **not** establish a full unequal-spin Toller-function inversion/order-reversal law on `SL(2,C)`, does not select a physical causal sector, and does not prove a source-defined correlated boundary value or causal-vertex finiteness/divergence. K5, G3, F9 and G8 remain unpromoted; no complete-QG or new-physics claim follows.

## Next admissible work

Do not repeat the kernel identity numerically. Return compute priority to the unresolved coefficient/boundary-value front: degree-two / nominal `epsilon^-1` overlap subtraction on the transitive K4 strata, actual proper-stratum coefficients with numerator/Jacobian bookkeeping, and separately any source-derived unequal-spin full-group Toller transformation if such an object can be pinned without assuming representation identities branchwise.
