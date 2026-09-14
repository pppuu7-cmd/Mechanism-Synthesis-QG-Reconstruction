# Iter080K-SM source matrix — arXiv:2604.24945

Source: Eugenio Bianchi, Chaosong Chen, Mauricio Gamonal, **Toller matrices and the Feynman i-epsilon in spinfoams**, arXiv:2604.24945 (2026).

Checked current arXiv full text on 2026-09-14. The web rendering identifies the paper date as May 10, 2026.

## Positive source anchors

### A. One-wedge/reduced-Toller uniqueness

In Sec. II, around Eqs. (7)–(12), the paper states that the reduced Toller matrices are uniquely characterized by:

- half-plane asymptotic decay;
- matching to the Wigner reduced matrix in the opposite half-plane;
- a finite simple Toller-pole structure;
- the additive decomposition `t^(+) + t^(-) = d`.

The text immediately following Eq. (12) says these analytic properties plus the sum rule determine the two branches uniquely.

In Sec. III.1, Eqs. (17)–(20), the paper constructs the Feynman i-epsilon functional/projector and then gives an explicit `Uniqueness` argument: if `u_+ + u_- = d` and the candidate branches have the same frozen asymptotic/pole properties, applying the projectors returns the Toller branches. Thus the one-wedge/reduced-branch split is source-explicit and unique in that scope.

### B. Toller matrices are not representations

Around Eqs. (13)–(15), the paper explicitly states that Toller `T`-matrices are functions on `SL(2,C)` and do **not** provide a representation. It writes explicitly that, for generic `g_1,g_2`, the ordinary representation-composition identity does not hold for `T^(±)(g_1 g_2)`.

This is a frozen anti-promotion lock: joint-K5 structure cannot be inferred by ordinary representation multiplication/composition.

## Systematic audit for a joint-K5 collision-extension selector

The source was checked for explicit full-object prescriptions using the following concept/term families:

- `K5`;
- ten-wedge / `ten` in the relevant full-vertex sense;
- `multi-wedge`;
- simultaneous collision;
- correlated multi-wedge prescription;
- distributional `extension` / renormalization at the common collision;
- wavefront/microlocal extension rule;
- group-integration extension prescription;
- boundary-functional rule selecting tangential coefficient functions.

No explicit theorem/equation/prescription was identified in arXiv:2604.24945 that defines the simultaneous ten-wedge K5 collision extension or selects smooth tangential extension data on the Iter077Q common-collision manifold.

The paper's positive result is instead a uniqueness theorem for the individual/reduced Toller branch splitting and equivalent representations of those Toller matrices.

## Frozen predicate matrix

- P1 `ONE_WEDGE_UNIQUENESS_EXPLICIT` = **true**.
- P2 `JOINT_K5_OBJECT_EXPLICIT` = **false** in the frozen sense required by Iter080K: no explicit full ten-wedge simultaneous-collision distributional object/extension theorem is supplied by this paper.
- P3 `CORRELATED_JOINT_K5_EXTENSION_RULE_EXPLICIT` = **false**.
- P4 `ITER077Q_TANGENTIAL_SELECTION_POWER_EXPLICIT` = **false**.
- P5 `NO_REPRESENTATION_COMPOSITION_ASSUMPTION` = **true**.

## Scope

This matrix does not say the Toller paper is incomplete for its stated purpose. It says only that its one-wedge analytic uniqueness theorem is not itself an explicit theorem selecting the separate joint-K5 distributional extension encountered in MSQGR Iter077Q.

No claim is made that no stronger consequence could ever be derived from the source together with additional independently justified mathematics. Such a derivation would require a separately prospectively frozen theorem gate.
