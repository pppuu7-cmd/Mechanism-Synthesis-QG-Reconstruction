# Iter081U-SM — finite BCG spectral epsilon does not regularize the frozen K5 common-collision L1 obstruction

**Date:** 2026-09-14  
**Status:** `PASS_EXACT_SCOPED`

## Prospective chain
- controlling duplicate-label erratum: `status/ITER081T_DUPLICATE_LABEL_PROVENANCE_ERRATUM.md`, commit `4e0ecf2b66c36359a66d0818d8b8e45ab7a21c31`;
- fresh preregistration: `084c65dbb5f89531fc1885fbdd64316b60423417`;
- implementation: `c2417a4db7b0fdfb2191f10210722e21ad199aee`;
- production head: `87e9f2a663df0b2d5f612a3404dbb69dc7b3b83b`;
- Actions run: `34884550558`, terminal success;
- job: `104111828010`, terminal success;
- artifact: `10363943202`;
- artifact ZIP digest: `sha256:fa1e15bf7548bf2cef2411aef42f530e0abec211055b56feed650e4ac439c59c`;
- downloaded aggregate JSON SHA256: `08fd6b4e8b1ade75aff5600eed59bed8bf5464102b6cc7cd06748a23f952e427`;
- durable raw aggregate: `results/raw/iter081u_sm_finite_spectral_epsilon.json`, commit `27be989009d6081fb3067cc71c994c798eb58204`.

## Classification
`ITER081U_SM_FINITE_SPECTRAL_EPSILON_DOES_NOT_REGULARIZE_K5_L1_COLLISION_EXACT_SCOPED`

Verdict: **`PASS_EXACT_SCOPED`**.

## Source/ordering scope
Published BCG source ordering defines each Toller branch after `epsilon->0+`; keeping a finite spectral epsilon through the K5 group integration is therefore not the source-defined amplitude. Iter081U tests this only as a hypothetical regulator rearrangement.

The finite-epsilon residue object supplied by the BCG contour argument is

`I_epsilon^sigma[d] = P_jl(rho+i sigma epsilon;rho) t^(sigma,rho+i sigma epsilon,k)`.

## Exact j=1/2 identity
For `j=l=k=1/2`, mechanical evaluation of BCG's finite product gives

`P_(1/2,1/2)(R;rho)=(4R^2+1)/(4rho^2+1)`

`=(R^2+1/4)/(rho^2+1/4)`.

The shifted Toller leading coefficient is proportional to `1/(R^2+1/4)`. At

`R=rho+i sigma epsilon`,

the spectral polynomial cancels the shifted denominator exactly.

Thus the finite-epsilon leading matrices are epsilon-independent:

branch `+`, `m=(-1/2,+1/2)`:
`[+2/(4rho^2+1), -2/(4rho^2+1)] beta^-2`;

branch `-`:
`[-2/(4rho^2+1), +2/(4rho^2+1)] beta^-2`.

They are exactly the authoritative Iter077I leading matrices.

## K5 consequence
Because the identity holds independently wedge by wedge, both

- one common fixed positive epsilon, and
- independent fixed positive `epsilon_ab`

leave the ten-wedge leading tensor and all 32 authoritative Iter077I boundary contractions unchanged.

Therefore

`q=-20`, `d=12`, `d-1+q=-9`, `q+d=-8`.

The frozen minimal-sector common-collision object remains not locally absolutely `L1` at every fixed positive spectral epsilon in this diagnostic ordering.

## Scientific meaning
The most direct rescue

`retain the published one-wedge spectral epsilon until after K5 integration`

does not even soften the validated local power singularity. Spectral epsilon shifts the representation parameter but does not regulate the group-variable common-collision power.

This strengthens Iter077K: published source ordering does not define a correlated K5 boundary value, and even the simple finite-epsilon reordering fails as an ordinary local L1 regulator.

## Claim ceiling
This is not a theorem against correlated group-variable analytic regularization, stratified Epstein-Glaser/Hadamard/BPHZ extension, dimensional/analytic continuation, subtraction or another future joint-K5 boundary-value prescription. It is not regulator independence and not a causal-vertex divergence/nonexistence theorem.

No generic-spin fully contracted theorem, G3/F9/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete-QG claim follows.
