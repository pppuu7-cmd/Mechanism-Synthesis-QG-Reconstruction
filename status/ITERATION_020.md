# Iteration 020 — local collision power counting of the direct causal vertex

Status: **PASS / FINITE LOCAL FIRST MOMENT + INFINITE IID SECOND MOMENT SIGNATURE**

## Question
Is the heavy tail observed in Iteration 019 caused by the zero-boost stratum of a relative Lorentz element, and if so does the singularity threaten the vertex mean itself or only ordinary Monte Carlo variance?

For a local asymptotic behavior `|F| ~ beta^q` and Lorentz Haar radial factor `sinh(beta)^2 d beta ~ beta^2 d beta`:

- absolute first moment is locally integrable if `q > -3`;
- the ordinary IID second moment is locally finite only if `q > -3/2`.

## GitHub campaign
Six independent jobs:
- gamma = `0.2, 1.2, 2.0`
- two independent compact/SU(2) orientation seeds = `11, 29`

Each job scanned `beta = 0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002` and measured:
1. all `j=l=1/2` magnetic components of full Cartan-reconstructed `T+` and `T-` approaching the `beta=0` SU(2) stratum;
2. the direct ten-wedge integrand for representative causal classes under both a gauge-fixed-pair collision and an internal-pair collision;
3. additive/EPRL controls.

Result: **6/6 jobs SUCCESS** and every job returned `FINITE_MEAN_INFINITE_VARIANCE_SIGNATURE`.

## Full-T edge result
Across all branch/magnetic/orientation/gamma cases:

- causal branch slopes: **-2.00490 .. -1.99021**
- equivalently, `|T+|,|T-| ~ beta^-2` to the resolution of the scan;
- additive `T+ + T- = D` slopes remain near zero, approximately **-0.00346 .. +0.00152**.

Per job:
- causal branch rows with locally integrable first moment: **8/8**;
- causal branch rows with finite ordinary-MC second moment: **0/8**.

The leading singular pieces of the two branches therefore cancel in the EPRL sum but remain separately in a fixed-causal wedge.

## Ten-wedge direct-integrand result
Across the two collision geometries and three causal classes:

- causal integrand slopes: **-2.04626 .. -1.97613**;
- EPRL-control slopes: approximately **-0.0264 .. +0.0146**.

Per job:
- causal collision rows with locally integrable first moment: **6/6**;
- causal collision rows with finite ordinary-MC second moment: **0/6**.

Across all six jobs this is **36/36 finite-first-moment causal collision cases and 0/36 finite-second-moment cases**.

## Interpretation
The local mechanism behind Iteration 019 is now directly identified:

`T^(±)(g_b^-1 g_a) ~ C^(±)/beta_ab^2` as `beta_ab -> 0`.

With Haar measure `beta_ab^2 d beta_ab`, a single generic collision layer contributes a finite `O(d beta)` amount to the absolute first moment, but its square produces `beta^-2 d beta`, so an ordinary Haar-IID Monte Carlo estimator has divergent local variance.

This explains why Iteration 019 produced finite samples but `max/median ~ 10^3-10^4`, `stderr/|mean| ~ O(1)`, and unstable seed means.

It does **not** yet prove global finiteness of the full causal vertex.  Intersections of multiple collision strata, boundary intertwiner sums, and the distributional/Feynman-i-epsilon interpretation still require separate treatment.  The causal-vertex paper itself explicitly identifies finiteness in the presence of Toller poles as an open question and cautions, through the Livine-Oriti limit, that naive pole power counting need not settle the full integral.

## Verdict
`LOCAL_CAUSAL_MEAN_INTEGRABLE__IID_VARIANCE_DIVERGENT`

Brute-force IID sample-size scaling is rejected as the primary integration strategy.  Next tasks:
1. explicit pair-exclusion regulator `min(beta_ab) > epsilon` with `epsilon -> 0` scaling;
2. isolate the universal `beta^-2` coefficient and test singular subtraction / pair-adapted importance sampling;
3. only then return to large-N vertex integration.
