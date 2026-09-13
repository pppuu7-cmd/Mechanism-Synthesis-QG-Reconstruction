# Iter077D-SM result — nonlinear excess `B` jet on the frozen rank-9 source stratum

**Date:** 2026-09-14  
**Status:** terminal scientific PASS, exact/scoped

## Authority

- Frozen preregistration: `prereg/ITER077D_SM_NONLINEAR_EXCESS_B_JET.md`
- Frozen witness: `xxxxxyyyzz` in edge order `01,02,03,04,12,13,14,23,24,34`
- Frozen self-stress: `lambda=(1,-1,0,0,1,0,0,0,0,0)`
- Initial production run: `34785141237` at head `9c4bc5ac4f3201fdd37416c0c338b656b61fbf1c`
  - all four scientific lanes completed successfully;
  - aggregate was infrastructure-only failure because the aggregate job omitted the SymPy dependency;
  - this run is non-authoritative for terminal classification.
- Control-only repair commit: `79fd7ccabd41adc0b039994855da919645881a40`
  - only installs `sympy==1.13.3` in the aggregate job;
  - frozen scientific object, witness, Taylor order, controls and interpretation rule unchanged.
- Authoritative retry run: `34785181275`
- Authoritative retry head: `79fd7ccabd41adc0b039994855da919645881a40`
- Aggregate job: `103799287885`
- Aggregate artifact: `10326213053`
- Aggregate digest: `sha256:5d74fbbe1fd149bf82780510161d65d435cf9f5f4afdaf547bf4ea79b995dd9c`
- Raw retry artifacts:
  - A `10325873721`, digest `sha256:e8addb8b0eb2b24d7c479583bf8e46438f072aa3bba55c9b111589dcb26eb76b`
  - B `10325714398`, digest `sha256:e896d4db874a2bdb86b2879490d341a1b5bca5eb552a0437ebf3631f04fcb963`
  - C `10326302783`, digest `sha256:ea87c64bef7a9c8f2b79b1ca04ac85ec965c8476e9e679658b990c17360c6cf1`
  - D `10326218070`, digest `sha256:baffa0bcf172abc6b9c7de8be9949b6dc01cf903d220a1dd8585813e1dd85a6d`

## Frozen classification

`ITER077D_SM_RANK9_EXCESS_CONSTRAINT_HAS_INDEFINITE_RANK2_QUADRATIC_JET_EXACT_DIAGONAL_FLAT_PLANE_AND_QUARTIC_LIFTED_SECOND_ISOTROPIC_BRANCH_EXACT_SCOPED`

Aggregate verdict: `PASS`.

## Scientific result

For the exact source-derived excess combination

`Phi(t;a,b,c)=B_01(t)-B_02(t)+B_12(t)`

on the frozen right-kernel coordinates of the rank-9 witness, the exact source matrix expansion satisfies the preregistered jet.

The quadratic Hessian in convention `Phi_2=(1/2) u^T H u`, `u=(a,b,c)`, has

- exact rank `2`;
- inertia `(positive,negative,zero)=(1,1,1)`;
- therefore an indefinite, non-Morse quadratic singularity.

Two distinct quadratic-zero structures behave differently:

1. **Exact diagonal flat plane:** `a=c` implies `g_1=g_2`, hence `B_12=0` and `B_01=B_02` exactly, so `Phi=0` identically rather than only to finite Taylor order.
2. **Second isotropic branch:** on `a=0`, the quadratic term vanishes but the source-faithful expansion is generically lifted at quartic order with coefficient

   `b^2 c^2 / 3`.

The pure Hessian-kernel axis `a=c=0` lies inside the exact diagonal flat plane and remains exactly flat for arbitrary `b`.

## Interpretation

This closes the nonlinear normal-form question only for the frozen first tested full-span rank-9 exceptional source stratum. The result is stronger than a second-jet rank statement because it separates an exact flat family from a distinct quartically lifted isotropic branch.

It is **not** a theorem for all rank-deficient source points. It is **not** a proof that the ten source contact distributions admit a unique pullback, are locally integrable, or yield a regulator-independent full causal vertex.

The next admissible source-amplitude step is a prospectively frozen local contact-pullback/scaling analysis that explicitly retains both the exact flat plane and the quartically lifted branch. Any such gate must distinguish a source-defined distributional object from an auxiliary regularization model.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no generic finite-spin signed P3; no exact full-amplitude cancellation/non-cancellation theorem; no physical causal-vertex finiteness/divergence theorem; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal `epsilon^-1` coefficient; no G3 PASS or F9/G8/K5 promotion; retain the published spectral `i epsilon`.