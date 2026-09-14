# Iter079B-SM frozen source snapshot

Frozen after prereg commit `45121d1b772057c61a861169ae93902c0b42e725` and before implementation.

## S1 — KKL generalized EPRL parent
Kaminski, Kisielowski, Lewandowski, *Spin-Foams for All Loop Quantum Gravity*, arXiv:0909.0939v5.

Verified source facts:
- the simplicial EPRL framework is generalized to arbitrary linear 2-cell spin foams;
- generic LQG spin-network boundaries are admitted;
- vertex structure and vertex amplitude are generalized to arbitrary valency;
- boundary spin-network orientation reversal is represented by dualizing the representation on the reversed edge;
- the paper is parent EPRL/EPRL-KKL structure, not a causal-Toller composition theorem.

This source therefore supplies `PARENT_COMPOSITION_SKELETON_AUTHORITY` but not by itself `CAUSAL_INHERITANCE_AUTHORITY`.

## S2 — generalized causal vertex
Carlos E. Beltran, *Causal Structure for Generalized Spinfoams*, arXiv:2603.22661v2 (3 Aug 2026).

Verified source facts already frozen by Iter079A:
- causal orientation is defined on arbitrary oriented 2-complexes;
- the generalized Bianchi-Chen-Gamonal/Toller causal vertex extends to arbitrary vertex boundary graph/valence;
- finiteness of the generalized causal vertex is left open;
- no explicit complete multi-vertex causal distributional functional is supplied in Iter079A's source audit.

Therefore E1-E2 are source explicit, while E3-E8 were classified missing required objects in Iter079A.

## S3 — local Toller vertex
Bianchi, Chen, Gamonal, *Causal spinfoam vertex for 4d Lorentzian quantum gravity*, arXiv:2601.23162.

Verified source facts:
- causal data are carried by Toller functions/matrices with `T^(+)+T^(-)=D`;
- a one-wedge Feynman spectral `i epsilon` representation is supplied;
- this local prescription is not authority for a joint K5 or multi-vertex regulator/extension.

## S4 — repository-authoritative distributional results
- Iter077K: joint K5 boundary value / correlated extension object is not source-defined.
- Iter077Q: source-compatible local extension ambiguity contains a countably infinite-dimensional tangential subspace `{Q^n F_SU2 delta_N}`.
- Iter079A: E1/E2 closed; E3-E8 remain `MISSING_REQUIRED_OBJECT`.

## Frozen inheritance matrix
| element | parent EPRL-KKL | causal source | status for causal composition |
|---|---|---|---|
| E1 arbitrary-2-complex causal orientation | not causal | explicit in Beltran | SOURCE_EXPLICIT |
| E2 generalized local causal vertex | parent local vertex only | explicit in Beltran/BCG | SOURCE_EXPLICIT |
| E3 multi-vertex causal product/contraction | parent algebraic skeleton exists | no explicit causal inheritance theorem identified | MISSING_REQUIRED_OBJECT |
| E4 face/edge weights, internal sums, normalization | parent model has model-specific structure | no explicit unchanged-inheritance theorem identified | MISSING_REQUIRED_OBJECT |
| E5 boundary gluing / dual orientation | parent spin-network duality exists | no complete causal bridge identified | MISSING_REQUIRED_OBJECT |
| E6 noncompact gauge quotient / redundant integrations | parent/local prescriptions are not enough | no composed causal prescription identified | MISSING_REQUIRED_OBJECT |
| E7 joint distributional/regulator prescription | not resolved by parent structure | absent; Iter077K blocker | MISSING_REQUIRED_OBJECT |
| E8 transport/selection of Iter077Q supported ambiguity | parent linear gluing cannot select by itself | no selector/annihilation theorem identified | MISSING_REQUIRED_OBJECT |

## Frozen algebraic control for E8
Let `G` denote any ordinary linear gluing/contraction map on boundary amplitudes. For an extension family `A_ext + h`, with `h` in supported ambiguity subspace `H`, linearity gives

`G(A_ext + h) = G(A_ext) + G(h)`.

Thus ordinary gluing selects a unique extension only if `G|_H = 0` or if an independent selector fixes `h`. Neither condition may be assumed from parent composition alone. Iter077Q gives an infinite-dimensional `H` already at normal-derivative order zero.

## Scope lock
This snapshot supports only a source/provenance inheritance audit. It does not claim that the full EPRL-KKL state sum is absent, inconsistent, or unusable; it tests whether unchanged inheritance into the causal-Toller model follows without adding a new physical choice.
