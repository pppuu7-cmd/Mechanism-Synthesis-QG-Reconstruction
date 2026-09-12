# Iteration 022 — Multi-collision cluster power counting

Status: **COMPLETED / MAJOR FINITENESS WARNING**

Workflow: `Multi-Collision Cluster Power Counting`

- 6/6 GitHub jobs completed successfully.
- gamma = 0.2, 1.2, 2.0.
- two independent generic cluster rays per gamma (seeds 17 and 41).
- each job tested k = 2,3,4,5 clusters and the fixed causal classes allplus, onefour, twothree plus EPRL control.
- scaling grid: r = 0.20, 0.10, 0.05, 0.025, 0.0125, 0.00625, 0.003125.

For a k-group collision cluster the independent local boost dimension is

`d = 3(k-1)`.

Absolute local integrability of `|I| ~ r^q` requires `q > -d`; a finite ordinary-IID second moment requires `q > -d/2`.

## Aggregate causal results

### k = 2

- measured q range: **-2.097345 ... -1.966546**
- first-moment margin q+d: **+0.902655 ... +1.033454**
- first moment: **18/18 PASS**
- second moment: **18/18 FAIL**

This reproduces Iteration 020.

### k = 3

- measured q range: **-6.074077 ... -6.010093**
- local dimension d = 6
- first-moment margin q+d: **-0.074077 ... -0.010093**
- first moment: **18/18 BORDERLINE_LOG**
- second moment: **18/18 FAIL**

The measured direct-vertex singularity is essentially the naive three-edge product `r^-6`, exactly at the logarithmic absolute-integrability boundary.

### k = 4

- measured q range: **-11.989092 ... -11.935979**
- local dimension d = 9
- first-moment margin q+d: **-2.989092 ... -2.935979**
- first moment: **18/18 FAIL**
- second moment: **18/18 FAIL**

The actual direct integrand follows the naive six-edge product `r^-12` to high accuracy.

### k = 5

- measured q range: **-19.999724 ... -19.937345**
- local dimension d = 12
- first-moment margin q+d: **-7.999724 ... -7.937345**
- first moment: **18/18 FAIL**
- second moment: **18/18 FAIL**

The actual direct integrand follows the naive ten-edge product `r^-20` to high accuracy.

## EPRL control

Across k=2,3,4,5 and all six gamma/seed runs the EPRL control remained regular, with measured slopes near zero (approximately -0.020 ... +0.020) and both first- and second-moment classifications PASS.

## Interpretation

There is no evidence that fixed-causal-class multiplication internally softens simultaneous Toller poles.  Generic common-scale collision rays reproduce the independent-edge pole count almost exactly.

Therefore a fixed causal class is not absolutely integrable on the tested k>=3 collision intersections: k=3 is logarithmically borderline, while k=4 and k=5 are power-counting failures.  This is a **finiteness warning**, not yet a proof that the physical distributional/Feynman-i-epsilon causal vertex is undefined.  Conditional/distributional cancellations and sums over causal sectors must be tested before a final conclusion.

## Next target

Iteration 023 tests the physically motivated sums over causal structures.  In particular it compares

- `C+`: sum over the 16 inequivalent factorized wedge-sign structures `kappa_ab=sigma_a sigma_b`,
- `C-`: the corresponding co-causal sector with all wedge signs reversed,
- `C+ + C-`,
- EPRL control.

Because Iteration 021 found `C_edge^- ~= -C_edge^+` for the leading beta^-2 residues, parity predicts that the leading singularities cannot cancel within C+ for odd collision-cluster sizes k=3 and k=5.  Iteration 023 tests that prediction on the full ten-wedge magnetic-basis carrier.
