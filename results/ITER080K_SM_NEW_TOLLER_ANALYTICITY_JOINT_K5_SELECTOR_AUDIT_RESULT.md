# Iter080K-SM result — new Toller analyticity authority does not explicitly select the joint K5 extension

Date: 2026-09-14

## New primary authority

E. Bianchi, C. Chen, M. Gamonal, **Toller matrices and the Feynman i-epsilon in spinfoams**, arXiv:2604.24945 (2026).

This source was not represented in the frozen Iter080E BCG/Beltran selector census and therefore opened the `NEW_PRIMARY_AUTHORITY` route authorized by `status/CURRENT.md`.

## Prospective provenance

- preregistration: `prereg/ITER080K_SM_NEW_TOLLER_ANALYTICITY_JOINT_K5_SELECTOR_AUDIT.md`, commit `363d15318a7747671111e1a8f2f79793f87ce2f6`;
- frozen source matrix: `sources/ITER080K_SM_TOLLER_ANALYTICITY_JOINT_K5_SOURCE_MATRIX.md`, commit `2885f70533331bdb0b13555d360f48848b43b47b`;
- implementation: `distributional/iter080k_sm_toller_joint_k5_source_audit.py`, commit `36bc70b1033aa9defeb09bb8b171914cf7046501`;
- workflow / production head: `.github/workflows/iter080k_sm_toller_joint_k5_source_audit.yml`, commit `cc9a8aa036c6a52782da76e2ea215ce379fc415c`;
- authoritative run: `34860144694`, terminal `success`.

Artifacts consumed:

- A `10354492701`, digest `sha256:980657b592837369d5036a4c19092aba687415fbb8367d7124c59be2d2674f36`;
- B `10354472611`, digest `sha256:c6317c20615d84ca31d825d66516c7a92c15de04103fc9402aea2af261e24bfc`;
- C `10354642434`, digest `sha256:c1a476b51607eb171245d1e86ec4862e18d5514499a6bed771af92472db0cbc9`;
- D `10354927171`, digest `sha256:914a48edadd9b5407f439ace84c3445d8ce3b44c6642c38345433251b05bebee`;
- aggregate `10354063246`, digest `sha256:40ced95997238b98c617ba5dd77a71c46f6d42ccc655e03a83a0d6536da1105e`.

All four lanes and aggregate are execution-valid.

## Source facts retained

The new Toller paper does materially strengthen the one-wedge analytic authority. In its reduced-Toller analysis it states uniqueness under the combination of half-plane asymptotics, matching, pole structure and the sum rule `t^(+)+t^(-)=d`. Its Feynman i-epsilon contour functional is then shown to act as a projector onto the two admissible branches.

The paper also explicitly states that Toller `T`-matrices are functions on `SL(2,C)`, not Lorentz-group representations: ordinary representation composition cannot be used to infer a full multi-wedge law.

Frozen source predicates:

- P1 `ONE_WEDGE_UNIQUENESS_EXPLICIT` = true;
- P2 `JOINT_K5_OBJECT_EXPLICIT` = false in the Iter080K simultaneous-collision-extension sense;
- P3 `CORRELATED_JOINT_K5_EXTENSION_RULE_EXPLICIT` = false;
- P4 `ITER077Q_TANGENTIAL_SELECTION_POWER_EXPLICIT` = false;
- P5 `NO_REPRESENTATION_COMPOSITION_ASSUMPTION` = true.

## Authoritative classification

`ITER080K_SM_NEW_TOLLER_ANALYTICITY_AUTHORITY_UNIQUELY_FIXES_ONE_WEDGE_BRANCHES_BUT_DOES_NOT_EXPLICITLY_SELECT_JOINT_K5_EXTENSION_SOURCE_BRIDGE_BLOCKED_SCOPED`

Verdict: **`BLOCKED_SOURCE_BRIDGE_SCOPED`**.

## Scientific meaning

The distinction between one-wedge and joint-K5 uniqueness is now source-sharper:

1. each individual Toller branch is not arbitrary — the new source gives a real analytic uniqueness theorem in its proper one-wedge/reduced-matrix scope;
2. this does not by itself define the source-ordered simultaneous ten-wedge K5 distributional extension at the common collision;
3. the source does not provide an explicit correlated joint-K5 boundary-value/extension law acting on the Iter077Q smooth tangential coefficient functions;
4. ordinary representation composition is explicitly unavailable as a bridge because Toller matrices are not representations.

Thus the Iter077Q function-space blocker is not removed by merely citing one-wedge Toller analyticity/uniqueness.

## Interpretation ceiling

This is not a theorem that the new Toller analytic data can never participate in a stronger derived joint-K5 theorem. A future separately preregistered derivation could combine its analytic projector structure with additional independently justified mathematics and test whether that stronger construction constrains the Iter077Q ambiguity.

No CRQN v0.3 is defined here; no unique K5 extension, G3 PASS, F9/G8/K5 promotion, causal-vertex finiteness/divergence theorem, regulator independence, `NEW_PHYSICS_FOUND`, or complete-QG claim follows.

## Next admissible step

The highest-value local route is no longer another source census. A new gate should require an independently motivated **actual joint-function-space law** — for example a rigorously derived correlated boundary-value condition, differential/transport equation, spectral condition, composition/RG constraint, or another new primary source that explicitly acts at the ten-wedge K5 level. One-wedge Toller uniqueness alone is insufficient.
