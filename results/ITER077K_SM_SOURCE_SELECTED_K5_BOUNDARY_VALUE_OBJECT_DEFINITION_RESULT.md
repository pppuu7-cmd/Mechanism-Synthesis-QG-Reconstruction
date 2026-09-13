# Iter077K-SM result — source-selected K5 boundary-value object-definition audit

Date: 2026-09-14

## Prospective authority

Preregistration: `prereg/ITER077K_SM_SOURCE_SELECTED_K5_BOUNDARY_VALUE_OBJECT_DEFINITION.md`, commit `97f0114f80edee3a42f67490f81cb1eb8f497304`.

This source audit was frozen before the terminal classification below. It introduces no new regulator, finite part, contour deformation, boundary state, subtraction, or correlated extension.

## Primary sources audited

1. E. Bianchi, C. Chen, M. Gamonal, `Causal spinfoam vertex for 4d Lorentzian quantum gravity`, arXiv:2601.23162 / Phys. Rev. D 113, 126020 (2026), especially Eqs. (3)-(6) and the exact causal-vertex ordering.
2. E. Bianchi, C. Chen, M. Gamonal, `Toller matrices and the Feynman i epsilon in spinfoams`, arXiv:2604.24945, especially Secs. II-III and the Feynman representation/uniqueness discussion.

## Positive controls

PASS.

The primary source explicitly defines each individual Toller matrix by a one-wedge spectral Feynman prescription with `epsilon -> 0+`, and then Eq. (4) inserts ten already-defined Toller matrices into the four gauge-fixed `SL(2,C)` group integrations. The companion paper proves uniqueness of the individual Toller splitting/projector and gives equivalent one-wedge representations.

Thus the source ordering itself is clear:

`one-wedge spectral/Feynman construction -> Toller function -> ten-wedge K5 product -> full boundary contraction -> group integration`.

## Decisive object-definition audit

The two frozen primary sources do **not** provide an additional joint K5-level prescription that resolves the non-locally-L1 common collision established by authoritative Iter077I-SM.

In particular, within the frozen source authority no explicit theorem/prescription was found that specifies any of the following for the fixed-causal ten-Toller product at the common group collision:

- a common ten-wedge regulator retained through the K5 group integrations and only then removed;
- a correlated distributional extension;
- a Hadamard finite part/subtraction rule;
- a group-variable contour deformation selecting a unique boundary value;
- a theorem of conditional/oscillatory convergence applicable to the identified finite-spin common collision;
- an equivalence theorem allowing the one-wedge limits in Eq. (3) to be moved outside/after the ten-wedge product and group integrations.

The statement that Eq. (4) "defines the vertex amplitude" is therefore a formal source definition of the intended expression, but it does not by itself supply the missing mathematical prescription required once Iter077I-SM establishes failure of ordinary local `L1` integrability in the complete frozen all-`j=1/2` sector.

## Adversarial negative controls

1. `T+ + T- = D` does not rescue a fixed causal sector. The source states that the EPRL amplitude is the **unconstrained** sum over all wedge signs, whereas the sum over causal structures is constrained and does not reproduce EPRL.
2. Cancellation of Toller poles in the EPRL sum is therefore not a fixed-causal K5 boundary-value theorem.
3. Polynomial boundedness of individual Toller functions does not imply local integrability of their ten-fold K5 product at the common collision.
4. Uniqueness of the one-wedge Toller splitting does not imply uniqueness of a correlated distributional extension of the ten-wedge product.
5. Convergence of one-wedge Lorentzian series for nonzero boost does not control the simultaneous `beta_ab -> 0` K5 collision.
6. Large-spin saddle selection is semiclassical and does not define the exact finite-spin common-collision boundary value.

## Terminal classification

`ITER077K_SM_SOURCE_SELECTED_K5_COMMON_COLLISION_BOUNDARY_VALUE_NOT_DEFINED_IN_PRIMARY_SOURCE_OBJECT_DEFINITION_BLOCKED`

Scientific verdict: **BLOCKED**.

## New scientific fact

The active K5 obstruction is not merely that a difficult integral has not yet been evaluated. Given Iter077I-SM's exact non-`L1` result, the published source prescription presently stops one logical level too early: it uniquely defines the one-wedge causal Toller factors and formally writes the fixed-causal K5 integral, but it does not select the correlated/conditional common-collision boundary value needed to turn that formal expression into a unique finite-spin local amplitude in the obstructed sector.

## Interpretation ceiling

`BLOCKED` is not `FAIL` and is not a theorem that no mathematical extension exists. It means the current CRQN implementation cannot claim a source-selected fixed-causal K5 amplitude from these primary prescriptions alone.

Any common-`epsilon` K5 limit, correlated extension, finite part, contour deformation, or subtraction introduced from this point is a **new mechanism/definition**. It must have independent physical/mathematical motivation and a new prospective falsifiable gate; it may not be back-labelled as already selected by the published one-wedge Feynman prescription.

No full causal-vertex divergence/nonexistence theorem; no regulator-independence theorem; no generic-spin theorem; no physical source-to-K4 pushforward; no G3/F9/G8/K5 promotion; no complete-QG claim.

## Exact next admissible step

First consume any already-running authoritative Iter077J-SM terminal result without duplicating it. Regardless of its outcome, do not continue accumulating leading-angle lemmas as a substitute for the missing amplitude definition.

Then perform one of only two admissible moves:

1. find and prospectively verify an external mathematical theorem that makes the exact fixed-causal Eq. (4) a unique distributional/conditional functional under its published ordering and hypotheses; or
2. keep K5 at `BLOCKED_OBJECT_DEFINITION`. A new common-regulator/correlated-extension mechanism is admissible only if independently motivated before testing, with source ordering, full 32-component boundary contraction, regulator path and regulator-independence criteria frozen prospectively.