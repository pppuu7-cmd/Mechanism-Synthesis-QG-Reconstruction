# Toller causal split -> sl2cfoam-next reduced-Wigner / booster path

**Status:** `IMPLEMENTATION_TARGET_IDENTIFIED / NUMERICAL_CAUSAL_VERTEX_PENDING`

## External analytic input

For the causal Lorentzian spinfoam split, the reduced Wigner matrix is decomposed as

`d = t^(+) + t^(-)`.

The 2026 Toller-matrix construction shows that the two terms are the unique Feynman `i epsilon` analytic projections / positive- and negative-boost-frequency parts. For gamma-simple EPRL representations one sets

`k = j`, `rho = gamma*j`.

The closed gamma-simple expressions are given in Eqs. (45)-(46) of Bianchi, Chen & Gamonal, Phys. Rev. D 114, 046014 (2026), arXiv:2604.24945.

## sl2cfoam-next insertion point

The upstream `sl2cfoam-next` code computes reduced Lorentzian Wigner matrices through

`sl2cfoam_dsmall(...)`

in `src/dsmall.c`. The booster integrations call this function directly, including the paths in `src/b4.c` and `src/b4_qagp.c`.

Therefore the first causal implementation should **not** post-project a completed scalar vertex. It should introduce a branch-aware reduced-matrix routine, schematically

`sl2cfoam_tsmall(branch, ...) -> t^(branch)`

with the same kinematic arguments as `sl2cfoam_dsmall`, and propagate the branch choice through the booster integrand before contraction into the vertex.

## Validation ladder

1. Python/mpmath reference: verify `t+ + t- = d` for gamma-simple samples to high precision.
2. C pointwise implementation: compare C `t+`, `t-` against the Python oracle over a beta/rho/j/m grid.
3. Booster additive test: with identical quadrature, check `B4[d] = B4[t+ + t-]` at integrand and integrated levels.
4. Single causal booster: compute `B4+` and `B4-` separately and verify numerical stability with integration precision.
5. Causal vertex: propagate branch data through the vertex tensor.
6. Only then define a same-realization refinement/boundary map and evaluate CCI cross blocks.

## Scientific guardrail

A causal vertex alone is not F9. F9 concerns compatibility of the causal analytic split with a dynamically justified coarse-graining / embedding map. This file merely identifies the correct microscopic insertion point needed to make that future calculation physical.
