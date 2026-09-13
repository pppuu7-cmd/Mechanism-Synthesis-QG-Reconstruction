# Iter077M-SM preregistration — can published source symmetries select the K5 extension?

**Date:** 2026-09-14

## Scientific question

After Iter077L-SM establishes local extendibility but finite order-8 normal-jet freedom at the common K5 collision, do the symmetries/constraints actually stated in the published causal-vertex construction uniquely fix that freedom without adding a new prescription?

This is a counterexample-first uniqueness gate. A single nonzero local extension term that preserves all frozen source-backed constraints is sufficient to show that those constraints do not select a unique extension.

## Source authority

Freeze:

1. Bianchi, Chen, Gamonal, *Causal spinfoam vertex for 4d Lorentzian quantum gravity*, arXiv:2601.23162, especially Eqs. (3)-(7), the boundary-state definition around Eq. (4), global `SL(2,C)` gauge fixing, and the fixed causal data `sigma_a`.
2. Bianchi, Chen, Gamonal, *Toller matrices and the Feynman i epsilon in spinfoams*, arXiv:2604.24945, only for the one-wedge Toller transformation/analytic structure already source-locked by Iter077I/K.
3. Iter077L theorem authority for the allowed local extension freedom supported on the common-collision submanifold.

No unstated gluing axiom, Ward identity, renormalization condition, or normalization condition may be imported and called source-backed.

## Frozen geometry

Before gauge fixing, let the five group variables be `g_a in SL(2,C)`. The common compact-collision set is

`S = { (g_1,...,g_5) : g_b^{-1} g_a in SU(2) for every a,b }`.

The vertex integrand depends on the relative elements `g_b^{-1}g_a` and is invariant under common left multiplication `g_a -> h g_a`. Gauge fixing `g_1=1` sends `S` locally to

`N = SU(2)^4 subset SL(2,C)^4`.

Freeze the invariant normal delta distribution `delta_N` defined with respect to the Haar-induced tubular density. Its transverse scaling degree is `12`, so adding a nonzero `delta_N` term does not raise the Iter077L scaling degree `20`.

## Frozen boundary coefficient

For fixed spins/intertwiners, define `F_SU2(y;Psi)` to be the ordinary SU(2) spin-network boundary functional obtained on `N` by contracting the spin-`j_ab` SU(2) Wigner matrices of the relative compact elements with exactly the same five boundary intertwiners as the source vertex.

This is not proposed as a physical counterterm. It is a source-compatible smooth coefficient used only to test uniqueness under the published symmetries.

Candidate ambiguity:

`Delta A_c = c * F_SU2(y;Psi) * delta_N(x)`

with constant `c` and normal coordinates `x`, tangential compact coordinates `y`.

## Frozen checks

1. **Support:** `Delta A_c` vanishes off the common-collision set and therefore leaves the published off-collision Toller function unchanged.
2. **Scaling:** `sd_N(delta_N)=12 <= 20`; the modified extension has the same maximal transverse scaling degree 20.
3. **Global gauge:** formulate the term on the pre-gauge set `S` and verify invariance under common left `SL(2,C)` multiplication; gauge fixing must reproduce `delta_N`.
4. **Boundary gauge/intertwiner structure:** `F_SU2` uses the same boundary spins and invariant intertwiners; no representative boundary state may be selected post hoc.
5. **Causal data:** fixed `sigma_a sigma_b` remain labels of the vertex; the local term neither sums nor changes causal sectors.
6. **One-wedge source ordering:** no Toller/contact limit is reordered; the term is an extension ambiguity after the off-`N` source object has already been constructed.
7. **Published constraint audit:** search the frozen primary sources for an explicit local normalization, gluing/composition identity, subtraction condition, joint regulator, or other condition that fixes `c`.

## Positive control

If the source explicitly states a normalization/identity whose application gives one unique value of `c` and forbids every nonzero symmetry-compatible supported term, this gate must not claim residual freedom.

## Negative control

A term with support away from `N`, a term that changes the fixed causal labels, or a boundary coefficient not built from the source boundary representation/intertwiners is invalid as a uniqueness counterexample.

## PASS

PASS iff `Delta A_c` is a valid nonzero one-parameter family preserving all frozen source-backed constraints and no published condition fixes `c`.

Classification:

`ITER077M_SM_PUBLISHED_GAUGE_BOUNDARY_CAUSAL_CONSTRAINTS_DO_NOT_SELECT_K5_EXTENSION_NONZERO_DELTA_N_AMBIGUITY_SURVIVES_EXACT_THEOREM_SCOPED`

Scientific consequence: the published constraints are insufficient to turn Iter077L extension existence into a unique causal vertex. A new selector/normalization/composition principle would be required.

## FAIL

FAIL iff a frozen published source condition uniquely fixes `c` and rules out the candidate ambiguity without adding a new assumption.

## BLOCKED

BLOCKED iff the transformation law/support/invariance of the candidate ambiguity cannot be established for the actual boundary functional.

## INVALID

INVALID if the argument uses an arbitrary scalar surrogate, changes the source ordering, changes the boundary space, assumes a gluing law absent from the source, or promotes local extension freedom into a full-vertex nonexistence theorem.

## Interpretation ceiling

Even PASS proves only that the **currently published** gauge/boundary/causal constraints do not uniquely select the local extension. It does not prove that no additional physically motivated condition can do so, and it does not disprove the CRQN programme in principle.

No full causal-vertex divergence/nonexistence theorem; no regulator-independence theorem; no G3/F9/G8/K5 promotion; no new-physics or complete-QG claim.