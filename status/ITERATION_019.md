# Iteration 019 — regulated Haar-matched four-group Monte Carlo pilot

Status: **COMPUTATION PASS / IID CONVERGENCE FAIL-OPEN**

## Scope
Gauge-fix `g1=1` and sample `g2..g5` from the truncated polar domain

`g = B(n,beta) h`, `0 <= beta <= R`,

with `n` uniform on `S^2`, `h` Haar on `SU(2)`, and radial proposal proportional to `sinh(beta)^2`.  The finite rapidity `R` is an explicit regulator; only the `R`-dependent radial Haar factor is retained, so no absolute normalization is claimed.

The pilot evaluates one `j=1/2` magnetic-basis component for three representative causal classes (`0<->5`, `1<->4`, `2<->3`) and the EPRL control.

## GitHub campaign
- gamma = 1.2
- modes = `allplus`, `onefour`, `twothree`, `eprl`
- cutoffs `R = 0.6, 1.0, 1.4`
- seeds = `101, 202`
- `N=32` samples/job
- total = **24 jobs**

Result: **24/24 jobs SUCCESS**, all 768 sampled integrand values finite.

## Variance diagnosis
For the causal classes, the sample distributions are extremely heavy-tailed:

- `stderr/|mean|`: **0.710 .. 1.145**
- `q90(|I|) / median(|I|)`: **86.3 .. 391.7**
- `max(|I|) / median(|I|)`: **2.15e3 .. 3.75e4**
- smallest encountered relative Cartan rapidity: **beta_ab = 0.04436**

The two independent seeds typically give complex estimates in nearly opposite directions.  Their separation is about `1.75 .. 2.00` times the average estimate magnitude for the causal sectors, while still only about `1.0 .. 1.6` combined nominal standard errors because the estimated variance is itself enormous.

The EPRL control is far less heavy-tailed (`max/median ~ 21.8 .. 67.8`) because `T+ + T- = D` cancels the branch singular structure, although phase cancellation still makes `stderr/|mean|` large (`0.59 .. 2.90`) at `N=32`.

## Interpretation
The pilot does **not** support brute-force IID sample-size scaling yet. Rare configurations with one or more relative elements `g_b^-1 g_a` close to the zero-boost (`beta_ab -> 0`) stratum dominate the causal sample distribution.

A plausible mechanism is a finite first moment but divergent/very large second moment.  In Cartan/polar coordinates the Lorentz Haar measure contributes locally `sinh(beta)^2 d beta ~ beta^2 d beta`.  If a full branch matrix element behaves as `|T| ~ beta^{-p}`, then:

- absolute first-moment radial power is `beta^(2-p)` and is locally integrable for `p < 3`;
- second-moment radial power is `beta^(2-2p)` and is locally integrable only for `p < 3/2`.

Thus a branch scaling near `p ~ 2` would produce exactly the observed pattern: a potentially finite vertex contribution but infinite ordinary Monte Carlo variance.

This is only a hypothesis at this stage.  The causal-vertex paper itself notes that finiteness of the new causal model must be investigated again because the Toller poles may introduce new divergences; it also notes that naive pole power counting can be misleading in the Livine-Oriti/Barrett-Crane limit, where more detailed calculations give a finite vertex.

## Verdict
`IID_HAAR_MONTE_CARLO_HEAVY_TAIL_FAIL_OPEN`

Do not infer cutoff convergence from Iteration 019.  The next task is local collision power counting of the **full** Cartan-reconstructed `T(g)` and the 10-wedge integrand.  Only after classifying first- and second-moment integrability should the integration algorithm be chosen (singularity subtraction, stratification, pair-adapted importance sampling, distributional/Feynman treatment, or ordinary MC if unexpectedly safe).
