# Iteration 021 — Pair exclusion and leading-pole subtraction

Status: **COMPLETED**

## 021A — nested pair exclusion

Workflow: `Pair Exclusion Epsilon Scan`

- 8/8 GitHub jobs completed successfully.
- gamma = 1.2, R = 1.0, N = 512 samples/job.
- modes: allplus, onefour, twothree, EPRL control.
- common-random-number nested cutoffs: epsilon = 0.20, 0.10, 0.05, 0.025.
- rejected proposals were retained as zero, so no conditional-normalization bias was introduced.

The scan does **not** provide a reliable epsilon->0 extrapolation.  For seed 301 the acceptance fractions were 0.9453125, 0.994140625, 1.0, 1.0; for seed 607 they were 0.923828125, 0.990234375, 1.0, 1.0.  Thus neither seed sampled a configuration with min pair beta below 0.05.  A single rare collision-shell sample could change a causal estimate by O(1) or more.  The two-seed epsilon=0.025 causal estimates remain mutually inconsistent at the present sample size.

Verdict: **IID pair exclusion is not an efficient convergence method for the causal integral.**  It is retained only as a diagnostic/control.

## 021B — leading beta^-2 subtraction

Workflow: `Leading Pole Subtraction Diagnostic`

- 6/6 GitHub jobs completed successfully.
- gamma = 0.2, 1.2, 2.0; two independent compact-orientation seeds each.
- every run returned `LEADING_POLE_SUBTRACTION_VARIANCE_CURE_LOCAL_PASS`.

For each full Cartan-reconstructed j=1/2 Toller component we fitted

`beta^2 T^s(beta) = C_s + a_s beta + b_s beta^2 + ...`

and tested the remainder

`R_s(beta) = T^s(beta) - C_s / beta^2`.

Aggregate result across all 48 causal edge rows:

- finite-variance-after-subtraction: **48/48**;
- remainder slopes: **-1.005879 ... -0.988203**.

For the direct ten-wedge causal integrand, across both gauge-pair and internal-pair collisions and all three causal classes, aggregate result across 36 rows:

- finite-variance-after-subtraction: **36/36**;
- remainder slopes: **-1.026034 ... -0.948402**.

The fitted leading coefficients of the two Toller branches obey the expected cancellation very accurately:

`C_plus + C_minus ~= 0`,

with the worst relative mismatch across the six runs about **2.1e-7** (best about 4.6e-9).

## Interpretation

Iteration 020 found a local causal singularity `I ~ beta^-2`, which is first-moment integrable under the local Haar factor `beta^2 d beta` but gives an infinite ordinary-IID second moment.  Iteration 021B shows that, along generic single-collision rays, subtracting the leading beta^-2 term leaves an approximately beta^-1 remainder.  Since q ~= -1 > -3/2, that remainder has a finite local second moment.

This is a strong numerical indication that a **singularity-aware control variate / subtraction estimator is possible**.  It is not yet a global estimator: overlapping collision strata require their own analysis and an inclusion-exclusion/partition-of-unity construction.

## Next bottleneck

**Iteration 022: multi-collision intersections.**

For a cluster of k group variables, the independent local boost dimension is `d=3(k-1)`, while the naive number of beta^-2 pair singularities is `k(k-1)/2`.  The independent-edge prediction is therefore

`|I| ~ r^{-k(k-1)}`.

For k=3 this sits exactly at the logarithmic absolute-integrability boundary (`q=-d=-6`).  k>=4 would be worse if the pair singularities simply multiplied.  The next computation tests the actual direct causal integrand on generic k=2,3,4,5 cluster rays instead of assuming that naive product power.
