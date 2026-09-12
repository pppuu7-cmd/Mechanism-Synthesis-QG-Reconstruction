# Iteration 027 — parallel conditional-finiteness and distributional-authority campaign

Status: **RUNNING / THREE INDEPENDENT FRONTS**

Date: 2026-09-12

## Motivation

Iterations 022-024 established a serious multi-collision finiteness warning for the causal Toller carrier: fixed causal classes, causal-sector sums, and the tested boundary-intertwiner contraction retain the naive multi-pole radial power counting.  Iteration 025A supplied an explicit tested j=1/2 Appendix-D distributional primitive.  Iteration 026 is testing the cheapest remaining conditional-convergence mechanism: antipodal cancellation of the leading homogeneous coefficient.

The present iteration deliberately opens two additional independent fronts without waiting for Iter026, because neither depends scientifically on its outcome.

## Front A — full-sphere leading-residue mean

Workflow: `Full Sphere Residue Mean`

Matrix:
- gamma = 0.2, 1.2, 2.0;
- seeds = 131, 173;
- 6 independent jobs;
- clusters k = 3,4,5;
- boundary states i00000, i22222, i02020, i20202;
- 64 generic tangent-sphere directions per row.

Observable:

`|<C(Omega)>_Omega| / sqrt(<|C(Omega)|^2>_Omega)`

for the leading homogeneous coefficient of the fully boundary-contracted `Cboth32` causal+co-causal sector.

Purpose: test non-antipodal global angular cancellation.  A small mean is only support for a possible conditional/PV mechanism; an O(1) mean/RMS ratio rules out that mechanism on the tested carrier.  This is not the exact distributional i-epsilon integral.

Run launched by commit `2c54298ec327e807fc617fa3708159aff5fc18d0`.

## Front B — Appendix-D distributional primitive beyond j=1/2

Workflow: `General-j Appendix-D Distribution Validation`

Matrix:
- rho = 0.1, 0.6, 1.0;
- j = 1, 3/2;
- 6 independent jobs.

The implementation builds the exact product polynomial

`F_j(rho+y,rho)=prod_{m=-j}^j [i(rho+y)+m]/[i rho+m]`

and uses its coefficients to construct

`delta^(rho,j)=sum_n a_(n+1)(-i)^(n+1) delta^(n)`.

Checks:
1. exact product-vs-expanded polynomial identity;
2. exact complementary `Theta_+ + Theta_- = 1` action on Schwartz tests;
3. Gaussian-derivative mollifier convergence through the higher delta derivatives.

Purpose: ensure that the published distributional causal primitive is not an artifact of the minimal j=1/2 representation before multi-wedge distribution products are studied.

Run launched by commit `08e7233498eca5ae7bb8dab33fd79a414d55d64f`.

## Concurrent inherited front — Iter026

Workflow `Angular Leading Residue Scan`, run `34666284649`, has 6 gamma/seed jobs testing antipodal cancellation on the fully boundary-contracted `Cboth32` carrier.

## Decision discipline

- A workflow success is not by itself a scientific PASS; raw artifacts must be consumed.
- Failure of antipodal cancellation does not exclude non-antipodal full-sphere cancellation.
- Failure of both angular mechanisms still does not by itself prove the published distributional i-epsilon causal vertex undefined; products/intersections of boundary distributions remain a separate authority problem.
- No result in this iteration promotes F9 or G8 novelty automatically.
- `BLOCKED` remains distinct from `FAIL`.
