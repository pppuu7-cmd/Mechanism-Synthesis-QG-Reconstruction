# Gamma-simple Toller pole lattice — exact naive-composition obstruction

**Status:** `EXACT_NEGATIVE_CONTROL / FULL_RG_OPEN`  
**Iteration:** 005

## External input

For the `gamma`-simple Lorentzian representations used in EPRL-type spinfoams,

`rho = gamma j`, `k=j`,

and the Toller boost-spectrum poles are

`omega_n^± = ∓ gamma j - i(2 n + |j ± m| + 1)`.

Since `m=-j,...,j`, `j±m >= 0`, hence

`omega_n^± = ∓ gamma j - i(2 n + j ± m + 1)`.

Reference: Bianchi, Chen, Gamonal, *Toller matrices and the Feynman i epsilon in spinfoams* (2026), arXiv:2604.24945 / Phys. Rev. D 114, 046014.

## Naive same-branch product test

Take two modes in the same causal branch at the same boost variable `beta`:

`exp(-i omega_1 beta) exp(-i omega_2 beta) = exp[-i(omega_1+omega_2) beta]`.

Ask whether the summed frequency can itself be a single `gamma`-simple pole with coarse labels `(J,M,N)` at the same fixed nonzero `gamma`.

Matching real parts gives

`J = j1 + j2`.

For the maximal coupled magnetic label,

`M = m1 + m2`.

Matching imaginary parts would require

`2N + J ± M + 1 = (2n1+j1±m1+1) + (2n2+j2±m2+1)`.

Substituting `J=j1+j2`, `M=m1+m2` gives

`N = n1 + n2 + 1/2`.

But `N` is a nonnegative integer. Therefore no exact single-pole gamma-simple mode can represent the raw product.

## Meaning

This is an exact obstruction to the **naive mode-multiplication coarse-graining ansatz**. It says that a physical RG step cannot be implemented by merely multiplying same-branch residue modes and relabeling the result as one gamma-simple pole.

It does **not** show that causal EPRL/Toller coarse graining is impossible. The true blocked amplitude includes gluing, sums/integrals over internal labels, boundary embedding maps, recoupling, truncation and possibly same-sector superpositions. Those operations can produce an effective state/amplitude not describable by one pole label.

## Relation to CCI

CCI only requires preservation of the causal subspace,

`P_b'^± iota_b'b = iota_b'b P_b^±`.

It does not require

`one pole mode -> one pole mode`.

Therefore:

- single-pole closure implies a very special realization of CCI;
- failure of single-pole closure does not imply failure of CCI;
- a same-sector superposition remains admissible under CCI.

`code/toller_embedding_taxonomy.py` makes this distinction executable.

## Research consequence

Iteration 005 must replace raw multiplication with a boundary-map calculation. The decisive object is the projected effective embedding/amplitude after internal sums:

`P_b'^∓ iota_b'b P_b^±`.

The physical F9 question remains whether these cross-sector blocks vanish (or flow to zero) in a dynamically justified Lorentzian realization while the effective Toller analytic class remains controlled.
