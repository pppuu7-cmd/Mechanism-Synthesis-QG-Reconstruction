# Primary mathematical motivation for a stratified K5 diagonal/forest extension

Date: 2026-09-14
Status: **INDEPENDENT MATHEMATICAL MOTIVATION — NOT A SPINFOAM RENORMALIZATION THEOREM**

## Why this note exists
The exact K5 source-leading carrier is singular on a family of pairwise compact-collision diagonals, not only at the deepest all-five collision. The corrected local extension problem therefore requires a stratified object before any analytic finite part can be interpreted globally.

This structure is not invented ad hoc for MSQGR. It closely matches established position-space extension/renormalization mathematics.

## Bergbauer--Brunetti--Kreimer
Christoph Bergbauer, Romeo Brunetti, Dirk Kreimer, `arXiv:0908.0633`, *Renormalization and resolution of singularities*.

Their stated framework:

- ultraviolet renormalization in position space is extension of distributions onto diagonals;
- for a general graph the relevant diagonals form a nontrivial arrangement of linear subspaces;
- De Concini--Procesi wonderful models resolve the arrangement to normal crossings;
- analytic regularization can be performed on the resolved model;
- the stratification encodes the forest formula / nested subdivergences;
- one subtraction along each irreducible divisor can yield a finite renormalized distribution, with higher degrees of divergence treated by local counterterms.

This is structurally aligned with the K5 linearized normal arrangement `X_a=X_b`, its collision subsets `B subset {1,...,5}`, and nested divergent chains.

## Dütsch--Fredenhagen--Keller--Rejzner
Michael Dütsch, Klaus Fredenhagen, Kai Johannes Keller, Katarzyna Rejzner, `arXiv:1311.5424`, *Dimensional Regularization in Position Space, and a Forest Formula for Epstein-Glaser Renormalization*.

Their position-space analysis emphasizes that a regularized product develops not only an overall divergence on the thin/full diagonal but also subdivergences on partial diagonals. The Epstein--Glaser forest formula is formulated in terms of **families of subsets of the vertex set**, adding local counterterms in an order compatible with nested/disjoint singular subsets.

Again this matches the natural combinatorial language of K5 collision blocks more closely than a single deepest radial subtraction.

## Exact MSQGR correspondence and non-correspondence
The correspondence is at the level of extension geometry/combinatorics:

- graph vertices <-> five K5 tetrahedral/group nodes;
- partial configuration diagonals <-> compact relative-boost collision blocks;
- nested vertex subsets <-> collision forests;
- scaling degree/power counting <-> Toller small-boost degrees;
- local counterterms <-> distributions supported on collision strata.

The correspondence is **not** a theorem that QFT forest renormalization automatically defines the spin-foam amplitude. Differences that must be resolved prospectively include:

- the local configuration variable is a Lorentz-group/tubular normal geometry, not flat scalar-field position space globally;
- Toller kernels are matrix-valued before true boundary contraction;
- exact node-wise right SU(2), common-left gauge, S5 and boundary-intertwiner covariance must be preserved;
- causal branch assignments and source order must remain fixed;
- partial-stratum full-boundary nonvanishing is not yet proved exactly for k=3,4;
- choice of analytic regularizer, subtraction operator, scale and finite normalization may remain scheme dependent.

## Consequence for next gates
The established literature supplies **independent motivation** for a `K5_STRATIFIED_DIAGONAL_FOREST_EXTENSION` program. It does not supply its coefficient values.

A source-faithful successor should:

1. use the exact collision-subset/forest object from Iter081X;
2. define local tubular coordinates and extension maps on each divergent stratum;
3. order subtractions by nested forests/wonderful-model geometry;
4. impose right-SU2, S5, boundary covariance and source ordering;
5. compare admissible schemes and identify which local jet coefficients remain free;
6. only then test whether an analytic/minimal-subtraction prescription is predictive or merely one extension choice.

## Claim ceiling
No claim is made that the mathematical QFT theorems' hypotheses hold automatically for the Toller K5 kernel, that the causal spin-foam vertex is renormalizable by the same forest formula, that a canonical scheme exists, or that the physical amplitude is finite. This note supplies independent mathematical motivation for the object and workflow only.
