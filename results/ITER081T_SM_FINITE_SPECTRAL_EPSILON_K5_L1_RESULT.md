# Iter081T-SM — finite BCG spectral epsilon does not regularize the frozen K5 common-collision L1 obstruction

**Date:** 2026-09-14  
**Status:** `PASS_EXACT_SCOPED`

## Prospective chain
- preregistration: `52313c08f39855bf18e3b56fce268e9cd262a074`;
- implementation: `0b1427c4f75434471888b930aced24dc2989ff29`;
- production head: `2935163250e31d267e6f398fae48aea8fd76817b`;
- Actions run: `34883957614`, terminal `success`;
- job: `104109829347`, terminal `success`;
- artifact: `10364226885`;
- artifact ZIP digest: `sha256:ad19c20f916b4b9de67344327ab11b29d0eb15ebb17051f5605c72e3cc8bea1f`;
- downloaded artifact JSON SHA256: `744e7e2a2a5cdef0b01692f74bf6635d5cdd70971d408b52b8a8e9e0ca4847ed`;
- durable raw copy: `results/raw/iter081t_sm_finite_spectral_epsilon.json`, commit `b91c551301f653f1bc7b6ae7a69fce769e70e5b0`.

## Frozen classification
`FINITE_SPECTRAL_EPSILON_DOES_NOT_REGULARIZE_K5_L1_COLLISION_EXACT_SCOPED`

Verdict: **`PASS_EXACT_SCOPED`**.

## Source/diagnostic distinction
BCG Eq. (20) defines the Toller branch only after `epsilon->0+`; companion Eq. (4) then inserts already-defined Toller functions into the K5 group integral. Retaining finite spectral epsilon through K5 integration is therefore not published source ordering. Iter081T tests it only as a hypothetical regulator diagnostic.

The BCG contour proof has, before the final epsilon limit, the exact residue object

`I_epsilon^sigma[d] = P_jl(rho+i sigma epsilon;rho) t^(sigma,rho+i sigma epsilon,k)`

for the projected branch, with the opposite branch excluded by contour closure.

## Exact j=1/2 cancellation in the spectral prefactor
For `j=l=k=1/2`,

`P_(1/2,1/2)(R;rho)`
`= [(iR+1/2)(iR-1/2)] / [(i rho+1/2)(i rho-1/2)]`
`= (R^2+1/4)/(rho^2+1/4)`.

The exact small-boost Toller leading coefficients at complex representation label `R` are proportional to

`1/(R^2+1/4)`.

Therefore at the finite-epsilon residue `R=rho+i sigma epsilon`, the spectral prefactor cancels the shifted denominator exactly.

For branch `+`, ordering magnetic components as `m=(-1/2,+1/2)`,

`Leading[I_epsilon^+[d]]`
`= [ +1/(2(rho^2+1/4)), -1/(2(rho^2+1/4)) ] beta^-2`,

independent of epsilon.

For branch `-`,

`Leading[I_epsilon^-[d]]`
`= [ -1/(2(rho^2+1/4)), +1/(2(rho^2+1/4)) ] beta^-2`,

also independent of epsilon.

Thus the finite-epsilon projected leading matrix is **exactly the authoritative Iter077I leading Toller matrix**, including the branch sign.

## K5 consequence
Because the equality holds wedge by wedge, both a common fixed epsilon and independent fixed positive `epsilon_ab` leave the entire ten-wedge leading tensor unchanged.

Hence every authoritative Iter077I full boundary contraction remains unchanged for all 32 minimal boundary components.

The local powers remain

- one wedge: `beta^-2`;
- ten wedges: `q=-20`;
- transverse dimension: `d=12`;
- radial absolute exponent: `d-1+q=-9`;
- L1 margin: `q+d=-8`.

Therefore finite BCG spectral epsilon does **not** make the frozen K5 common-collision object locally absolutely integrable.

## Scientific meaning
The natural rescue

`keep the published one-wedge spectral epsilon finite during K5 integration and remove it later`

fails already as an ordinary local L1 regulator in the authoritative all-`j=1/2` collision sector. The reason is exact: epsilon shifts the representation parameter, but the Toller kernel prefactor cancels the shifted leading denominator, leaving the boost singularity unchanged.

This strengthens Iter077K. Iter077K showed that published source ordering does not define a correlated K5 boundary value. Iter081T adds that the most direct finite-epsilon rearrangement does not even soften the validated local power divergence.

## Claim ceiling
This does **not** rule out a genuinely correlated group-variable analytic regularization, dimensional/analytic continuation, Epstein-Glaser/Hadamard extension, subtraction scheme, or another independently motivated boundary-value prescription. It is not a regulator-independence theorem and not a causal-vertex divergence/nonexistence theorem.

The corrected local extension blocker remains the right-SU2/S5 invariant normal-jet coefficient selector established by Iter081R/S.

No `NEW_PHYSICS_FOUND`; no G3/F9/G8/K5 promotion; no complete-QG claim.
