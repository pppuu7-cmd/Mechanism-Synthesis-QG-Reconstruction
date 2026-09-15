# Iter083E public-source lock — Ruhl/Toller one-wedge uniqueness versus joint K5 product

Date audited: 2026-09-15

Purpose: freeze only public-source statements needed by prospective Iter083E. This file does not itself assert the Iter083E scientific conclusion.

## Source A — Bianchi, Chen, Gamonal, `arXiv:2604.24945`

Title: *Toller matrices and the Feynman i epsilon in spinfoams*.

Audited current arXiv HTML, submitted 2026-04-27, paper date shown as 2026-05-10.

### A1. Ruhl one-wedge existence/uniqueness object

Section II, around Eqs. (5)-(12), states that for `beta>0` Ruhl proves existence and uniqueness of functions of the second kind, identified by the authors with the reduced Toller matrices `t^(+/- ,rho,k)_(jlm)(beta)`.

The uniqueness data are explicitly one-variable analytic data in the **complex rho plane**:

- asymptotic decay in the upper/lower rho half-plane, Eqs. (7)-(8);
- matching to the reduced Wigner `d^(rho,k)_(jlm)(beta)` in the opposite half-plane, Eqs. (9)-(10);
- meromorphy in rho with a finite set of simple Toller poles, Eq. (11);
- the one-wedge sum rule

  `t^+ + t^- = d`, Eq. (12).

The paper then states that those analytic properties together with the sum rule determine the reduced Toller branches uniquely.

### A2. Full Toller matrices are not an SL(2,C) representation

The Cartan reconstruction is Eq. (13).

Immediately after it the paper explicitly says that, unlike the Wigner D-matrix, the Toller T-matrices are functions over `SL(2,C)` and **do not provide a representation**.

Eq. (14) states

`T^(+/-)(g1 g2) != sum T^(+/-)(g1) T^(+/-)(g2)`.

The paper then records the additive property only,

`T^+ + T^- = D`, Eq. (15).

This source lock prohibits importing the Wigner-D representation law into the Toller T-matrices.

### A3. Feynman i epsilon is a one-spectral-variable projector

Section III.1 defines the functional `I_epsilon^(+/-)` in Eq. (17) as an integral over the single spectral variable `tilde rho`, with denominator

`tilde rho - rho -/+ i epsilon`.

Eqs. (18)-(20) show that the upper/lower contour projects the reduced Wigner d-matrix onto the corresponding Toller branch.

The uniqueness paragraph after Eq. (20) considers trial functions

`u_+(rho,beta), u_-(rho,beta)`

that are meromorphic in `rho`, satisfy the one-variable asymptotic decay and pole structure, and obey

`u_+ + u_- = d`.

Applying the same `I_epsilon` contour proves

`u_+/- = t^+/-`.

The source therefore establishes uniqueness of the **one-wedge Toller splitting**. No statement in this audited argument introduces ten correlated spectral variables or a common-collision K5 distributional extension.

### A4. Harmonic-analysis role does not supply a product law

The paper notes that Toller matrices play a role in the inverse Fourier transform of distributions on `SL(2,C)`. This source statement is retained. It is not to be rewritten as a theorem that arbitrary products of ten Toller functions possess a unique extension across a simultaneous singular submanifold; the same paragraph explicitly contains the non-representation Eq. (14).

## Source B — Bianchi, Chen, Gamonal, `arXiv:2601.23162v1`

Title: *Causal spinfoam vertex for 4d Lorentzian quantum gravity*.

Submitted 2026-01-30.

### B1. Source ordering of the K5 vertex

The paper first defines the elementary Toller matrices, including their Feynman `i epsilon` representation, and then defines a fixed-causal 4-simplex vertex by multiplying the ten wedge factors.

For the K5/4-simplex boundary the fixed-sector amplitude has the source form

`integral prod_(a=2)^5 dg_a  product_(a<b) T^(sigma_a sigma_b)(g_b^-1 g_a)`

with boundary indices/contractions understood and one `SL(2,C)` element gauge-fixed by the common-left redundancy.

Thus each elementary Toller branch is already defined before the ten-factor group-space product and the four remaining `SL(2,C)` integrations are formed.

### B2. No source-locked joint prescription recorded here

The audited causal-vertex source gives the one-wedge Feynman/Toller prescription and the ten-factor vertex formula. This audit did not locate a theorem defining a **single correlated multivariable boundary value/common regulator for the simultaneous ten-wedge K5 collision**, nor a composition/gluing condition that selects supported common-collision extension coefficients.

This is an absence statement limited to the audited source text. It is not an impossibility theorem and must be falsified if such a source-authorized joint prescription is later located.

## Frozen distinction for Iter083E

Public-source object 1:

`ONE_WEDGE = unique t^(+/-)(rho,beta) under one-rho-plane analytic/asymptotic/pole data + t+ + t-=d`, equivalently extracted by one-variable `I_epsilon^(+/-)`.

Public-source object 2:

`K5_PRODUCT = product of ten already-defined T^(sigma_a sigma_b)(g_b^-1 g_a), followed by boundary contraction/group integration`.

No source statement in this manifest identifies `rho` with a common-collision normal coordinate or states that the one-wedge uniqueness theorem is a uniqueness theorem for extensions of `K5_PRODUCT` across the simultaneous compact collision.

## Falsifier lock

If a primary source is found that proves any of the following for the exact ten-wedge K5 object, this manifest must be amended before Iter083E can remain authoritative:

- a correlated multivariable boundary-value theorem fixing the simultaneous product;
- a common K5 regulator with a unique distributional limit;
- a multiplication theorem controlling the ten Toller singular factors at the shared collision;
- a composition/gluing law selecting common-collision supported coefficients;
- another source-authorized condition proved to act on the full supported ambiguity space.

Until such authority is found, this manifest records only the narrower one-wedge source theorem and the ten-factor construction.
