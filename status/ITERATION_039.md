# Iteration 039 — S5-invariant distributional-extension jet audit

Status: **TERMINAL / SCIENTIFIC FAIL FOR SYMMETRY-ONLY UNIQUENESS**

Date: 2026-09-12

## Closed prerequisite

Iter038 authoritative run `34694739107`, commit `fff6514000d0620b1617af8711e28172795ce216`: six gamma/seed lanes terminal SUCCESS. Raw artifacts put all regular-carrier S5 covariance errors at ~1e-14, far inside frozen thresholds. Scientific classification: `FULL_SMALL_SPIN_CAUSAL_CARRIER_S5_COVARIANT` for the tested regular pointwise j=1/2 carrier.

## Preregistered question

If a correlated Feynman/distributional extension exists at the complete K5 collision, is full S5 covariance by itself enough to fix the local extension ambiguity?

For every total jet degree `d=0..16` the exact K5 cycle representation was used to compute `dim Sym^d(Cycle_K5)^G` for `G=S5`, `A5`, and fixed causal-sector stabilizers. The degree range was frozen prospectively from the j=1/2 Appendix-D delta/delta-prime singular content and nominal common-collision scaling.

Frozen discriminator: `S5_SYMMETRY_ONLY_EXTENSION_UNIQUE_THROUGH_16` iff the S5 invariant dimension is <=1 at every degree `0..16`.

## Authoritative run

Run `34695173734`, workflow commit `bea6e15fdc9a4204deadb1435fae8d0e37f4a13d`, computation commit `df02a2a49cc3912256cc99fb71a4e80b88037847`, preregistration commit `805eb2f2ae69ddc27a62859d61bef12772240238`.

All **17/17** degree lanes completed successfully. Every numerical orthogonality/integrality gate passed; maximum character-integrality residual over the complete run was `1.59e-12`.

S5 invariant dimensions by degree:

`d=0..16: [1,0,1,0,4,0,9,2,20,9,38,23,74,51,125,101,211]`.

A5 control dimensions:

`[1,0,2,0,6,0,17,4,36,18,74,46,141,102,246,202,412]`.

Selected fixed-sector stabilizer dimensions (`5+0`, `4+1`, `3+2`):

- d=2: `(1,2,4)`;
- d=4: `(4,9,16)`;
- d=8: `(20,65,126)`;
- d=16: `(211,896,1782)`.

Artifact provenance includes degree-4 artifact `10298860020`, degree-16 artifact `10298098246`, and one artifact for every intermediate degree in run `34695173734`; all raw JSON artifacts were consumed before classification.

## Scientific classification

`S5_SYMMETRY_ONLY_EXTENSION_UNIQUE_THROUGH_16 = FALSE`.

The first failure occurs already at degree 4, where `dim Sym^4(Cycle_K5)^S5 = 4`. Therefore full S5 covariance, although sufficient to collapse the quadratic cycle metric to one invariant, is **not sufficient** to select a unique higher-order local distributional extension.

This is a substantive negative result. It preserves the Iter038 carrier-level S5 PASS and sharply localizes what remains missing: additional source-backed analytic/Feynman information must select among higher-order S5-covariant local structures.

## Interpretation lock

- This is **not** a proof of physical divergence or nonexistence of the causal vertex.
- It is **not** permission to add arbitrary counterterms.
- It does not promote F9/G3/G8.
- The next permitted diagnostic is to quotient the S5 invariant jet space by descendants generated from the unique quadratic invariant, identifying genuinely new primitive S5-invariant extension shapes before any source-level i-epsilon selection is attempted.
