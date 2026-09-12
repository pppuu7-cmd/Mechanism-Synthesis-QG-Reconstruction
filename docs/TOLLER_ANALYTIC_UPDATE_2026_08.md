# Toller analytic update — August 2026

External anchor:

- Eugenio Bianchi, Chaosong Chen, Mauricio Gamonal, **“Toller matrices and the Feynman iε in spinfoams”**, Phys. Rev. D 114, 046014 (published 13 August 2026), arXiv:2604.24945, DOI: 10.1103/v3kc-4n3n.

The paper establishes that the causal Toller matrices admit three equivalent constructions:

1. the Feynman `i epsilon` analytic projector acting on the Lorentz Wigner matrix;
2. a boost-generator spectral representation which becomes an infinite residue sum;
3. explicit hypergeometric formulas obtained through the Wick-rotation construction.

It also keeps the exact additive identity

`T^(+) + T^(-) = D`.

## Consequence for MSQGR numerics

Iterations 016/017 used the residue-series representation as an independent numerical evaluator and found agreement with the closed hypergeometric form to roughly 1e-61--1e-64 on the tested small-spin grid.  The August 2026 paper independently establishes that these are not different causal prescriptions but equivalent representations of the same Toller object.

Therefore:

- residue summation is an admissible stable numerical backend;
- hypergeometric evaluation is an equivalent backend when numerically stable;
- the physical branch definition remains the Feynman/analytic projector, not an arbitrary pole subtraction;
- subtraction introduced in Iteration 021 is to be treated only as a variance-control identity unless it is embedded in an exactly unbiased representation of the same `i epsilon` amplitude.

This distinction is a hard guardrail for subsequent collision regularization work.
