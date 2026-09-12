# Iteration 039 — S5-invariant distributional-extension jet audit

Status: **PREREGISTERED / RUNNABLE**

Date: 2026-09-12

## Closed prerequisite

Iter038 authoritative run `34694739107`, commit `fff6514000d0620b1617af8711e28172795ce216`, completed six gamma/seed lanes successfully. Raw artifacts report max even/odd causal S5 covariance errors ~`2e-14`, EPRL control errors ~`2e-14`, and KAK reconstruction errors ~`2e-15`, all far inside the frozen Iter038 thresholds. Scientific classification: `FULL_SMALL_SPIN_CAUSAL_CARRIER_S5_COVARIANT` for the tested regular pointwise j=1/2 carrier.

This does **not** establish uniqueness/covariance of a singular multiwedge distributional extension.

## Question

If a correlated Feynman/distributional extension exists at the complete K5 collision, is full S5 covariance by itself enough to fix the local extension ambiguity?

The six-dimensional K5 cycle representation from Iter034-037 is used. For every total polynomial/jet degree `d=0..16`, compute the exact-integer invariant multiplicity

`dim Sym^d(Cycle_K5)^G`

for `G=S5` and oriented control `G=A5` using the character of the symmetric power. Also compute fixed-causal-sector stabilizer controls for representatives `5+0`, `4+1`, `3+2`.

The range through degree 16 is frozen prospectively from the j=1/2 Appendix-D singular content: each of ten wedge factors contains delta and delta-prime pieces; under common collision scaling a delta contributes nominal degree 1 and delta-prime degree 2. Thus the all-delta-prime superficial common-scaling degree is 20 in four independent vertex-relative directions, corresponding to a nominal local extension derivative budget up to 16. This is a power-counting audit only; it does not assume the naive product exists.

## Frozen scientific discriminator

For each degree record:

- `s5_invariant_dimension`;
- `a5_invariant_dimension`;
- causal-stabilizer invariant dimensions;
- numerical integrality residual of the character average.

Define `S5_UNIQUE_AT_DEGREE_d` iff the S5 invariant dimension is <=1. Define `S5_SYMMETRY_ONLY_EXTENSION_UNIQUE_THROUGH_16` iff this holds for **every** `d=0..16`.

No threshold or degree range may be changed after results are seen.

## Interpretation lock

- If the through-16 uniqueness discriminator fails, classify this as a **scientific negative result for symmetry-only uniqueness**, not as a failure of S5 covariance and not as physical divergence.
- A failure means additional source-backed analytic/Feynman information is required to fix higher-order local extension data.
- If it passes, this still does not construct the extension or prove the integrated causal vertex finite.
- No manual counterterm may be promoted to physical F9/G3/G8 evidence.
