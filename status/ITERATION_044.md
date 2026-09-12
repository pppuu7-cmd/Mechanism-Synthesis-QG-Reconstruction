# Iteration 044 — Joint K3 spectral/Feynman cycle-direction audit

Date: 2026-09-12

## Motivation
Iter043A established that the published finite spectral i-epsilon antecedent of the j=1/2 wedge retains an epsilon-independent delta-prime contact term. Iter043C established regulator-path dependence for an independently mollified overconstrained all-delta K3 cycle, while the transverse tree control remains path independent. The next admissible question is therefore the source-faithful joint spectral representation before any multiplication of boundary-supported distributions.

## Frozen object
For a K3 cycle with boundary coordinates `(u,v,-u-v)`, sign sector `(sigma1,sigma2,sigma3)`, finite published spectral epsilon > 0, and j=1/2 polynomial

`F_sigma(q)=1+c1*sigma*q+(c2/2)q^2`,

use the exact joint spectral integrand

`prod_e F_sigmae(qe)/(qe-i epsilon)`

with Fourier combinations

`k1=sigma1*q1-sigma3*q3`, `k2=sigma2*q2-sigma3*q3`.

Set the common cycle spectral variable `t=q3`, so

`q1=sigma1*(k1+sigma3*t)`, `q2=sigma2*(k2+sigma3*t)`, `q3=t`.

No artificial beta+i*epsilon deformation is introduced.

## Prospective gates
For gamma in {0.2,1.2,2.0}, epsilon in {0.05,0.2}, representative sign sectors {+++ , ++- , +-+ , -++}, and fixed nonzero Fourier probes `(k1,k2)=(0.37,-0.61)`:

1. Exact symbolic polynomial division in the common cycle variable must reproduce the numerical rational integrand to relative error < 1e-11 on a fixed probe grid.
2. Record the polynomial quotient degree and all coefficients. The j=1/2 source integrand is classified as having a common-cycle ultraviolet obstruction only if a nonzero polynomial quotient remains.
3. Record the highest even quotient power. A nonzero even term prospectively implies symmetric-cutoff growth; its predicted power is `L^(p+1)` for even power p.
4. EPRL/no-contact control `F=1` must have no polynomial quotient and asymptotic degree -3.
5. No conclusion about physical vertex divergence, finiteness, G3, F9 or G8 is allowed. A positive obstruction means only that the naive joint K3 spectral integral still requires a correlated Feynman/extension prescription along the cycle direction.

Thresholds and interpretation were frozen before viewing Iter044 results.

## Terminal authority
- production commit: `7eba66613dc67a5fde15806caea022c07c72a609`
- production run: `34697936208`
- repair commit: `70d33090defea6701423ebdbcb5cf1f8e0a3a8be`
- repaired `-++` run: `34700764999`

The production run contained 24 frozen physics lanes. Eighteen completed scientifically. The six `-++` lanes failed only because the leading minus sign was parsed by the command line as an option. The dedicated repair workflow changed only argument transport (`--signs=-++`) and re-ran exactly those six frozen lanes; all six completed successfully. This is an infrastructure repair, not a changed scientific criterion.

## Terminal result
All 24 frozen lanes satisfy the exact scientific gates. The source numerator has degree 6, the denominator degree 3, and the polynomial quotient degree 3. In every frozen lane the highest nonzero even quotient power is 2, hence a symmetric real cutoff has predicted `R^3` growth. The EPRL/no-contact control has zero polynomial quotient and asymptotic degree -3.

Representative repaired lane `(gamma,epsilon,signs)=(1.2,0.05,-++)`:
- `t^3`: `-4.40565509888492869`
- `t^2`: `-14.8030011322533604 - 0.220282754944246435 i`
- exact reconstruction relative error: `0`
- classification: `JOINT_K3_COMMON_CYCLE_SPECTRAL_OBSTRUCTION`

## Scientific classification
**NEGATIVE RESULT / OPEN EXTENSION PROBLEM.** Jointly retaining the published finite spectral `i epsilon` antecedent does not by itself remove the redundant K3 common-cycle polynomial sector. This is stronger than the separate-wedge contact-product diagnosis because it is obtained before multiplying boundary-supported distributions.

It is not a physical causal-vertex divergence theorem, does not select a finite part/counterterm, and does not promote G3, F9, or G8. The next admissible gate is to test whether a correlated finite-part/Feynman extension is invariant under equivalent choices of redundant cycle coordinate and has a controlled epsilon->0 limit.
