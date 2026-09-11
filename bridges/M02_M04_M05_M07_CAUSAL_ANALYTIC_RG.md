# M02 × M04 × M05 × M07 — Causal Analyticity–RG bridge

**Status:** `SYNTHESIS_DERIVED_CONSTRAINT / PHYSICAL_REALIZATION_OPEN`  
**Iteration:** 003

## Why the previous scalar branch is not the main route

A naive local factor satisfying `F(x+y)=F(x)F(y)` collapses to an exponential character (with a free phase under unit modulus), but this is too restrictive as a model of modern causal spinfoam dynamics. Toller causal matrices are not representations of the Lorentz group and do not satisfy ordinary group multiplication. The scalar-character calculation is therefore retained only as a negative control.

## External causal analytic input

The 2026 causal-spinfoam programme identifies causal branches `T^(+)` and `T^(-)` with the additive relation

`T^(+) + T^(-) = D`,

where `D` is the Wigner matrix. The branches are uniquely characterized by analytic/asymptotic properties and their Toller pole structure; the Feynman `i epsilon` prescription acts as a projector onto the branches.

References:

- Bianchi, Chen, Gamonal, *Causal spinfoam vertex for 4D Lorentzian quantum gravity*, Phys. Rev. D 113, 126020 (2026), DOI `10.1103/fwql-t4yr`.
- Bianchi, Chen, Gamonal, *Toller matrices and the Feynman i epsilon in spinfoams*, Phys. Rev. D 114, 046014 (2026), DOI `10.1103/v3kc-4n3n`, arXiv `2604.24945`.

These results are source-framework evidence, not MSQGR novelty.

## New synthesis question

MSQGR combines the causal analytic mechanism with the independent RG/coarse-graining requirement. The relevant question is no longer whether a local causal factor is multiplicative. It is whether **coarse graining preserves the causal analytic decomposition**.

Let `P_+` and `P_-` denote the causal analytic projectors (Toller/Feynman branches), and let `R_b` be a coarse-graining map including the required boundary embedding/identification at scale factor `b`.

The proposed **Causal Analyticity–RG Commutator (CARC)** condition is

`C_±(b) = P_±^(b) R_b - R_b P_± = 0`

on the physical/effective amplitude space, modulo declared representation/coupling renormalization.

At linearized level this is equivalent to eliminating cross-sector blocks,

`P_+ R_b P_- = 0`,

`P_- R_b P_+ = 0`.

Thus RG flow may mix modes inside a causal branch but must not generate an independent positive/negative-frequency mixing datum if causality is to be stable under scale change.

## Why this is useful

The relation is not inserted as a decorative new interaction. It is forced by combining:

- M02: causal orientation / Lorentzian admissibility;
- M04: Lorentzian quantum-geometric representation data;
- M05: causal quantum history amplitudes;
- M07: RG/coarse-graining closure.

It therefore has the right form for the Iteration-003 target `Phi(...)=0`: it constrains an allowed RG map rather than adding a new free coupling.

## Current evidence level

`code/causal_rg_commutator.py` verifies the linear algebra in a finite positive/negative-frequency surrogate. Sign-preserving kernels commute with the causal projector; cross-sign/parity mixing does not.

This is **not** evidence that an EPRL/Toller or TGFT coarse-graining map satisfies CARC. The physical gate remains open until the same microscopic realization supplies `R_b` and the commutator is evaluated.

## Strong physical gate F9

Promote F9 only if all are satisfied in one realization:

1. define the causal projectors on the actual boundary/amplitude space;
2. define the coarse-graining/embedding map without fitting to the desired answer;
3. evaluate the projected effective amplitude;
4. demonstrate closure of the causal analytic/pole class after internal sums/integrals;
5. show that no new independent pole/residue/cross-branch coupling is required;
6. repeat over more than one blocking/refinement step.

If the condition fails generically, CRQN v0.2 is rejected or must explicitly enlarge its mechanism set. If it holds nontrivially, it becomes the first candidate MSQGR-derived dynamical/RG relation.
