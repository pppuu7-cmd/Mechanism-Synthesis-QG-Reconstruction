# Iter079A-SM source snapshot — causal multi-vertex inheritance authority

**Date:** 2026-09-14

Prospective gate: `prereg/ITER079A_SM_CAUSAL_MULTIVERTEX_SOURCE_INHERITANCE.md`, commit `d489fa78cf6ee87bd4b02b5a81dc4e131e6883a7`.

This snapshot records source facts only after the gate criteria were frozen. It distinguishes a causal structure / generalized local vertex from a complete multi-vertex distributional functional.

## S1 — Bianchi–Chen–Gamonal causal vertex, arXiv:2601.23162

Current source authority used by MSQGR.

Relevant source facts:

1. The paper states that a spinfoam path integral is defined on 2-complexes with sums over face spins and edge intertwiners, and that a causal path integral additionally carries edge orientations determining a partial order.
2. Immediately after that general statement it explicitly restricts its construction: **the paper considers a single vertex dual to a 4-simplex**, with five incident edges carrying `sigma_a=+-1`.
3. Eq. (3) gives the one-wedge Toller matrix through the Feynman `i epsilon` spectral prescription.
4. Eq. (4) defines the fixed-causal single-vertex amplitude as four gauge-fixed `SL(2,C)` integrations over the product of ten Toller matrices.
5. Eq. (6) / Sec. III distinguishes the unrestricted sum over independent wedge signs, which reproduces EPRL, from the constrained factorizable causal structures `kappa_ab=sigma_a sigma_b`, whose sum does **not** reproduce EPRL.

Authority consequence: this paper defines the one-vertex causal Toller object and the causal-sign rule, but does not itself define a nontrivial multi-vertex causal state sum.

Source URL: `https://arxiv.org/abs/2601.23162`.

## S2 — Bianchi–Chen–Gamonal Toller analysis, arXiv:2604.24945

Relevant source facts:

1. The paper establishes equivalent representations and analytic properties of individual Toller matrices.
2. It describes Toller matrices as the elementary building block of the causal spinfoam **vertex** and applies the formulas to EPRL/causal vertex amplitudes.
3. It does not provide a 2-complex composition rule, face/edge causal measure, joint K5 extension prescription, or transport law for supported extension data.

Authority consequence: strengthens the one-wedge/local-vertex source lock, not multi-vertex composition.

Source URL: `https://arxiv.org/abs/2604.24945`.

## S3 — Beltrán, Causal Structure for Generalized Spinfoams, arXiv:2603.22661v2 (3 Aug 2026)

This source postdates the older Iter078A recovery and materially changes part of its blocker.

Relevant source facts:

1. The abstract and Sec. 2 explicitly define causal structure on an **arbitrary oriented 2-complex**, including orientation data on its 1- and 2-skeleta and a consistency criterion.
2. Sec. 4 replaces Wigner matrices in the generalized EPRL-KKL vertex by Toller matrices. Eq. (26) defines a generalized Bianchi–Chen–Gamonal causal vertex, and the text states that it is associated with an arbitrary 2-complex. Eq. (27) gives the coherent causal vertex on an arbitrary vertex boundary graph.
3. The construction is a generalized **vertex amplitude**. When discussing discretizations with more than one vertex, the paper phrases replacing the EPRL-KKL amplitude by the causal alternative at each vertex as a possible mechanism/proposal, not as a completed theorem establishing the full distributional state sum.
4. The conclusion explicitly lists the **finiteness of the generalized causal vertex amplitude as an open question**.
5. The paper does not address the MSQGR Iter077K/L/M/Q common-collision extension problem, does not select a joint K5 finite part, and does not provide a law transporting supported extension coefficient functions through gluing.
6. It discusses arbitrary-2-complex causal combinatorics and generalized local vertices, but does not supply an RG coarse/fine boundary embedding/projection or matching functional.

Authority consequence:

- old Iter078A missing item “causal orientation compatibility on arbitrary 2-complex” is now **resolved**;
- old Iter078A missing item “causal Toller vertex for arbitrary vertex boundary graph / valence” is now **resolved**;
- this does not by itself close the complete multi-vertex functional, regulator/extension problem, or refinement map.

Source URL: `https://arxiv.org/abs/2603.22661v2`.

## S4 — parent EPRL/EPRL-KKL generalized state-sum framework

Relevant authority:

- Kamiński–Kisielowski–Lewandowski, `Spin-Foams for All Loop Quantum Gravity`, arXiv:0909.0939: generalizes the EPRL framework to arbitrary 2-cell spin foams and arbitrary valence.
- Ding–Han–Rovelli, `Generalized Spinfoams`, arXiv:1011.2149: constrained-BF derivation on a general oriented 2-cell complex and generalized vertex construction.
- Donà–Frisoni, `How-To compute EPRL spin foam amplitudes`, arXiv:2202.04360: standard EPRL-FK transition amplitudes from a specified 2-complex to numerical implementation.

These sources establish that the **parent noncausal model** has a multi-vertex/state-sum framework. They do not by themselves prove that every face/edge weight, gauge regularization, boundary contraction and distributional prescription survives unchanged after the BCG Toller replacement and constrained causal orientation rule. Such inheritance requires an explicit causal statement or theorem under the Iter079A contract.

## Frozen E1–E9 authority matrix

| ID | Required object | Frozen status | Basis |
|---|---|---|---|
| E1 | arbitrary-2-complex causal orientation + shared-cell consistency | `SOURCE_EXPLICIT` | Beltrán v2 Sec. 2 and consistency analysis |
| E2 | generalized causal Toller vertex at arbitrary required valence | `SOURCE_EXPLICIT` | Beltrán v2 Eq. (26)-(31), generalized BCG vertex |
| E3 | complete multi-vertex causal product/contraction rule | `MISSING_REQUIRED_OBJECT` | parent EPRL-KKL has a state sum, but frozen causal sources do not establish a complete source-faithful distributional composition rule |
| E4 | causal face/edge weights + internal spin/intertwiner sums + normalization | `MISSING_REQUIRED_OBJECT` | parent weights exist; no explicit theorem in frozen causal source shows unchanged inheritance is the unique causal prescription |
| E5 | boundary gluing / dual-orientation convention for composed causal object | `MISSING_REQUIRED_OBJECT` | standard framework available, explicit causal inheritance bridge not supplied |
| E6 | gauge fixing / redundant noncompact integration treatment for composed causal object | `MISSING_REQUIRED_OBJECT` | local removal of a redundant integral is discussed; generalized causal finiteness remains explicitly open |
| E7 | joint distributional/regulator prescription making local and composed causal object well-defined at collision | `MISSING_REQUIRED_OBJECT` | Iter077K/L/Q plus Beltrán's explicit finiteness open issue |
| E8 | transport/projection/selection of supported extension function space under composition | `MISSING_REQUIRED_OBJECT` | none of S1-S4 acts on Iter077Q `{Q^n F_SU2 delta_N}` freedom |
| E9 | coarse/fine boundary embedding/projection + RG matching functional | `NOT_REQUIRED_AT_THIS_LAYER` for fixed multi-vertex amplitude; `MISSING_REQUIRED_OBJECT` for refinement/RG | no causal RG map supplied |

## Frozen scientific classification implied if matrix survives adversarial lanes

`BLOCKED_MULTI_VERTEX_CAUSAL_OBJECT_DEFINITION_PARTIAL_SOURCE_BRIDGE_E1_E2_CLOSED_E3_E8_OPEN`

This is not a claim that parent EPRL composition cannot be adopted. It says adopting it as CRQN causal-Toller dynamics is an additional bridge choice unless frozen causal authority proves the inheritance, and even such an adoption would not solve the local distributional extension/regulator freedom established in Iter077Q.