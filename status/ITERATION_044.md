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

Thresholds and interpretation are frozen before viewing Iter044 results.
