# Iter080E-SM source snapshot — joint-K5 function-space selector audit

**Date:** 2026-09-14

Prospective contract: `prereg/ITER080E_SM_JOINT_K5_FUNCTION_SPACE_SELECTOR_SOURCE_AUDIT.md`, prereg commit `f1a465a059f7c4da8270bed8021f920013b7f5da`.

This file records source evidence only after the scientific criteria were frozen. It does not add a selector axiom.

## Provenance / erratum lock

Controlling contact erratum blob: `status/ITER077_CONTACT_FORMULA_ERRATUM.md` SHA `63356e5099929f2b21d9d7296ab97f15ff163dba`.

Historical Iter077E/F source-dependent results using the earlier incorrect contact transcription remain quarantined and are not evidence in this audit.

## S1 — Bianchi–Chen–Gamonal, causal vertex, arXiv:2601.23162

Durable source transcription: `sources/CAUSAL_SPINFOAM_VERTEX_2026_SOURCE_SNAPSHOT.md`, blob `006001f06ec9beef56906b2e808920e1ec72b99e`.

Source facts represented there:

- Eq. (3) defines **one Toller function** by a Feynman `i epsilon` spectral integral and fixes the physical one-wedge branch convention.
- Eq. (4) writes the fixed-causal single-4-simplex vertex as four gauge-fixed `SL(2,C)` integrations of the product of ten Toller functions, with `g_1=1` and `g_ab=g_b^{-1}g_a`.
- The source formula therefore establishes the ordered local vertex expression and its ten-wedge incidence.
- The durable source record does **not** supply a separate correlated joint-K5 boundary-value limit, common finite part, joint contour, extension map on the common-collision set, or theorem that the ten individually defined Toller boundary values have a unique distributional product/extension after full boundary contraction.
- No function-valued/infinite system is identified there that acts on the later Iter077Q supported tangential extension freedom.

Frozen predicate evidence for S1:

`P1_JOINT_K5 = NOT_EXPLICIT`: Eq. (4) is a ten-wedge vertex formula, but the source record contains no distinct correlated joint-K5 extension/boundary-value prescription resolving the collision product.

`P2_SOURCE_ORDER = EXPLICIT_FOR_VERTEX_FORMULA`: the source order and direct ten-Toller product/integration formula are explicit.

`P3_FULL_OBJECT_REACH = EXPLICIT_FOR_FORMAL_VERTEX_FORMULA_ONLY`: Eq. (4) reaches the formal ten-wedge/full group integral, but not a separately defined distributional extension at the common collision.

`P4_FUNCTION_SPACE_UNIQUENESS = NOT_EXPLICIT`: no uniqueness theorem or condition fixing the full Iter077Q `W` appears in the frozen record.

`P5_REGULATOR_BRANCH_AUTHORITY = ONE_WEDGE_ONLY`: physical spectral branch is explicit per Toller factor; no theorem relating the ten one-wedge limits to a unique joint K5 extension/interchange is supplied.

## S2 — Bianchi–Chen–Gamonal, Toller matrices, arXiv:2604.24945

Durable source records:

- `sources/TOLLER_MATRICES_2026_CONJUGATION_BRANCH_FLIP_SNAPSHOT.md`, blob `2f9312b5e596dffddd348fe57c58af59e4e51671`;
- `sources/CAUSAL_VERTEX_TOLLER_ONEJET_SOURCE_SNAPSHOT.md`, blob `7fc5482bff78ea97e7a64681413257b6c8d7d359`;
- `sources/ITER079A_SM_CAUSAL_MULTIVERTEX_SOURCE_INHERITANCE_SNAPSHOT.md`, blob `2c3c5744494faef8cf070bc49e031fb446ce1180`.

Source facts represented there:

- The paper derives the Feynman-`i epsilon` Toller projector/matrices and exact analytic identities for individual Toller matrices, including reduced gamma-simple formulas and branch/conjugation identities.
- The Iter079A source audit records that this paper strengthens the one-wedge/local-vertex source lock but provides no joint K5 extension prescription or transport law for supported extension data.
- Exact one-wedge identities do not become a correlated ten-wedge boundary-value theorem merely by applying them independently to each factor.

Frozen predicate evidence for S2:

`P1_JOINT_K5 = NOT_EXPLICIT`.

`P2_SOURCE_ORDER = LOCAL_WEDGE_ONLY`: compatible one-wedge building blocks are explicit, but no joint extension stage is defined.

`P3_FULL_OBJECT_REACH = NOT_EXPLICIT_FOR_EXTENSION`: the analytic Toller identities stop at one-wedge/local-vertex ingredients for the relevant extension question.

`P4_FUNCTION_SPACE_UNIQUENESS = NOT_EXPLICIT`.

`P5_REGULATOR_BRANCH_AUTHORITY = ONE_WEDGE_ONLY`.

## S3 — Beltrán, Causal Structure for Generalized Spinfoams, arXiv:2603.22661v2 (3 Aug 2026)

Durable source transcription: `sources/ITER079A_SM_CAUSAL_MULTIVERTEX_SOURCE_INHERITANCE_SNAPSHOT.md`, blob `2c3c5744494faef8cf070bc49e031fb446ce1180`.

Source facts represented there:

- causal orientation/consistency is explicit on arbitrary oriented 2-complexes;
- Sec. 4 / Eq. (26) defines a generalized BCG causal vertex and Eq. (27) a coherent causal vertex on an arbitrary vertex boundary graph;
- generalized causal-vertex finiteness is explicitly left open;
- the paper does not address the Iter077K/L/M/Q common-collision extension problem, does not select a joint K5 finite part, and does not provide a law selecting/transporting the supported extension coefficient functions.

Frozen predicate evidence for S3:

`P1_JOINT_K5 = NOT_EXPLICIT`.

`P2_SOURCE_ORDER = GENERALIZED_LOCAL_VERTEX_ONLY`.

`P3_FULL_OBJECT_REACH = NOT_EXPLICIT_FOR_COLLISION_EXTENSION`.

`P4_FUNCTION_SPACE_UNIQUENESS = NOT_EXPLICIT`.

`P5_REGULATOR_BRANCH_AUTHORITY = NOT_EXPLICIT_FOR_JOINT_EXTENSION`.

## Existing exact blocker context

`status/CURRENT.md` records the controlling source-order firewall and the following already-authoritative facts:

- Iter077K: one-wedge spectral `i epsilon` does not define a joint K5 finite part, correlated extension, contour, conditional-convergence theorem, or interchange theorem.
- Iter077Q: source-compatible extension freedom contains the infinite-dimensional tangential subspace `W=span{Q^n F_SU2 delta_N}`.
- Iter080A: finite K5 permutation covariance does not uniquely select the extension.
- repaired Iter080D: every fixed finite scalar-valued complex-linear selector has infinite-dimensional kernel on `W`.

These are dependencies, not substitutes for the primary-source census.

## Source census conclusion to be machine-tested

All three frozen primary sources are represented. The durable evidence contains important one-wedge, formal ten-wedge/local-vertex, and generalized-vertex ingredients, but no source record above is marked `EXPLICIT` for every P1–P5 selector predicate. The workflow must derive the scientific classification from this evidence structure and must include controls showing that an actually joint/function-space-complete source record would be classified differently.

No result classification is asserted by this snapshot itself.