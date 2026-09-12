# Iteration 036 — source causal-orbit symmetry gate

Status: **PREREGISTERED / RUNNABLE**

Date: 2026-09-12

## Recovered frontier

The hourly auto-research advanced the repository beyond the older Iter029 `CURRENT.md` snapshot through Iter030–Iter035. The authoritative latest terminal run before this gate is Iter035 run `34692215902` at commit `adc1c6bc60243dcefc361f72e92cdfc69e06ebe1`: 32/32 jobs are SUCCESS after an infrastructure-only NumPy-boolean JSON fix. Because the Iter035 script exits nonzero if any preregistered gate fails, all 32 profiles satisfy its gates: exact S5 isotropy at zero bias, residual S4 invariance, positive approximately linear small-bias response, and return of finite shape anisotropy under explicit vertex-selecting bias.

Iter034 had shown that a uniform S5 average collapses a generic six-dimensional K5 cycle metric to the unique isotropic form. Iter035 therefore establishes that the ambiguity-removal mechanism is symmetry-protected rather than generically robust to arbitrary microscopic bias.

## Why Iter036 is different

The causal vertex does not introduce an arbitrary distinguished-vertex bias as its primitive data. Its source combinatorics use five signs `sigma_a=+-1` modulo the global reversal, hence 16 inequivalent causal classes with factorized wedge signs `kappa_ab=sigma_a sigma_b`.

Under S5 these classes must split by the future/past partition sizes:

- `5+0`: expected orbit size 1, stabilizer S5;
- `4+1`: expected orbit size 5, stabilizer S4;
- `3+2`: expected orbit size 10, stabilizer S3 x S2.

Iteration 036 asks whether *source-induced causal orbit covariance*, rather than an arbitrary full-group average, is enough to remove the cycle-metric finite-part shape ambiguity.

## Frozen lanes

### 036A — exact rational representation theorem

Use an integer fundamental-cycle basis of K5 and exact SymPy arithmetic. For each causal type compute:

1. orbit size and stabilizer order;
2. dimension of stabilizer-invariant symmetric bilinear forms on the 6D cycle space;
3. shape-parameter count after removing one overall scale;
4. whether the S5 orbit average of **every** stabilizer-invariant basis tensor is proportional to the unique S5-invariant cycle metric.

No numerical rank thresholds are allowed in this lane.

### 036B — 32-profile numerical stress test

For random SPD cycle metrics over condition targets `3..10000`:

1. project onto the fixed-sector stabilizer invariant space;
2. average all S5 transforms;
3. allow arbitrary positive relative weights between the `5+0`, `4+1`, `3+2` orbit sums;
4. verify determinant-normalized isotropy remains;
5. weakly bias one member **inside** a nontrivial orbit as a control and require shape anisotropy to return.

### 036C — exact source sign covariance

Enumerate all `16 x 120` sector/permutation pairs and verify that `kappa_ab=sigma_a sigma_b` transforms covariantly, the orbit split is exactly `1+5+10`, and any scalar weight depending only on causal orbit type is S5 invariant.

## Interpretation lock

A PASS would establish an exact finite-K5 symmetry mechanism: if the physical multi-wedge finite part is covariant under the source causal-sector action and weights are constant inside each S5 orbit, then orbit summation removes cycle-metric shape even if fixed sectors admit several invariant tensors. It would **not** establish that the Toller/Feynman distribution actually generates those covariant finite parts or orbit-constant weights.

The next physical gate after a PASS is therefore a same-realization permutation-covariance test of the **actual Toller matrix + boundary/intertwiner carrier**, not a promotion of F9/G8.
