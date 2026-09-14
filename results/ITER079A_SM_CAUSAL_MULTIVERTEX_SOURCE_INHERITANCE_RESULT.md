# Iter079A-SM result — partial source bridge for causal multi-vertex object

**Date:** 2026-09-14

## Provenance

- Prospective preregistration: `prereg/ITER079A_SM_CAUSAL_MULTIVERTEX_SOURCE_INHERITANCE.md`, commit `d489fa78cf6ee87bd4b02b5a81dc4e131e6883a7`.
- Frozen source snapshot / authority matrix: `sources/ITER079A_SM_CAUSAL_MULTIVERTEX_SOURCE_INHERITANCE_SNAPSHOT.md`, commit `ec642f9d5ad919ae2d75c5d33f5da758621f898b`.
- Implementation: `distributional/iter079a_sm_causal_multivertex_source_inheritance.py`, commit `19e00e7acbc7c6407b9841735f8f59404296ab04`.
- Workflow / production head: `.github/workflows/iter079a_sm_causal_multivertex_source_inheritance.yml`, commit `7627cf8303c4184940962b260118e0cd5420f833`.
- Authoritative terminal run: `34793089002`.
- Aggregate artifact: `10328048914`, digest `sha256:5172301070c89bc01e16ecf34ff5ecb547e9e78a9e50f5f0c706fd277ee9bb2b`.
- Lane artifacts:
  - A `10328554530`, digest `sha256:6e8dbb31f1f7d8ab4dbe0975dc33e378290385380e0cdeb52ec62c35e28e1be4`;
  - B `10327749262`, digest `sha256:3bfa7c5653d310e25797b0f04f4adb53a18ee75fcc230dee0b2dcc1fcb59a708`;
  - C `10327794298`, digest `sha256:1236355d92cfdfabadedb2c30406d027facf3f50ec92d8f602805a694f2a48a2`;
  - D `10327993954`, digest `sha256:9f08fa6a4de633e76f5dd36a47bf9a9b36dd2fe61c331b18e54c98047d4ec13a`.

All four raw lane outputs and the aggregate were consumed before classification. Green CI is not treated as scientific PASS.

## Classification

`ITER079A_SM_CAUSAL_MULTIVERTEX_PARTIAL_SOURCE_BRIDGE_E1_E2_CLOSED_E3_E8_OBJECT_DEFINITION_BLOCKED_EXACT_SOURCE_AUDIT`

Scientific verdict: **BLOCKED**.

This is not a FAIL: no contradiction or nonexistence theorem for a causal multi-vertex theory has been established.

## Frozen required-element matrix

| ID | Required physical object | Terminal status |
|---|---|---|
| E1 | arbitrary-2-complex causal orientation / shared-cell consistency | `SOURCE_EXPLICIT` |
| E2 | generalized causal Toller / BCG local vertex at arbitrary required valence | `SOURCE_EXPLICIT` |
| E3 | complete multi-vertex causal product / contraction rule | `MISSING_REQUIRED_OBJECT` |
| E4 | causal face/edge weights, internal spin/intertwiner sums, normalization | `MISSING_REQUIRED_OBJECT` |
| E5 | boundary gluing / dual-orientation convention for the composed causal object | `MISSING_REQUIRED_OBJECT` |
| E6 | gauge fixing / redundant noncompact integration treatment for the composed causal object | `MISSING_REQUIRED_OBJECT` |
| E7 | joint distributional / regulator prescription for local and composed collision singularities | `MISSING_REQUIRED_OBJECT` |
| E8 | transport / projection / selection rule for local supported extension freedom under composition | `MISSING_REQUIRED_OBJECT` |
| E9 | coarse/fine embedding/projection + RG matching functional | `NOT_REQUIRED_AT_THIS_LAYER` for a fixed multi-vertex amplitude; `MISSING_REQUIRED_OBJECT` for refinement/RG |

## Source advance relative to Iter078A

The old Iter078A blocker was too broad after the August 2026 source update.

Beltrán, `Causal Structure for Generalized Spinfoams`, arXiv:2603.22661v2 (3 Aug 2026), now supplies two pieces that were previously missing:

1. a causal orientation / consistency construction on an arbitrary oriented 2-complex (`E1`);
2. a generalized Bianchi–Chen–Gamonal / Toller causal vertex on arbitrary vertex boundary graphs / valence (`E2`).

Thus future work must **not** repeat orientation-combinatorics or generalized-valence existence as unresolved blockers.

## What remains missing

The same source does not turn the generalized local vertex into a complete finite-spin multi-vertex distributional functional. Its discussion of discretizations with more than one vertex is a proposed/application direction, while finiteness of the generalized causal vertex is itself left as an open issue.

The parent EPRL/EPRL-KKL state-sum framework provides multi-vertex composition machinery for the parent noncausal model, but the Iter079A contract forbids silently assuming that all face/edge weights, normalizations, boundary contractions, gauge regularization and distributional prescriptions are uniquely inherited after replacing the local vertex by the constrained causal Toller object. No frozen causal source theorem establishing that full inheritance was found.

Most importantly, no source in the frozen authority acts on the physical local extension freedom established by Iter077L/M/Q. In particular, there is no source-defined composition law selecting, transporting or quotienting the infinite family

`{ Q^n F_SU2 delta_N : n>=0 }`.

Therefore even an adopted parent-state-sum contraction would not, by itself, close the local-amplitude ambiguity.

## Independent lane results

- Lane A — `PASS`: exact BCG/Toller local source scope verified: one-wedge `i epsilon`, fixed-causal one-vertex Eq. (4), single-4-simplex restriction, and the fact that the constrained causal sign sum is not the unrestricted EPRL sign sum.
- Lane B — `PASS`: Beltrán v2 closes `E1/E2`; the generalized vertex is explicit, but generalized-vertex finiteness remains open and no extension-transport rule is supplied.
- Lane C — `BLOCKED`: `E3-E6` are not source-faithfully inherited by theorem; importing parent EPRL/BF composition data without a causal bridge would change the model definition.
- Lane D — `BLOCKED`: `E7-E8` remain absent when checked against authoritative Iter077K and Iter077Q. No hidden joint K5 prescription or function-space extension transport was found.

## New scientific fact

CRQN's causal multi-vertex problem is now **narrower but still fundamental**:

- causal structure on an arbitrary 2-complex is source-defined;
- generalized local causal Toller vertices are source-defined;
- the complete multi-vertex physical functional is not yet source-defined because the composition/measure/gluing/gauge/distributional/extension-transport layer (`E3-E8`) remains missing.

This is meaningful progress because it removes two old object-definition uncertainties while isolating the exact remaining bridge.

## CRQN chain effect

`carrier -> one-wedge causal Toller -> generalized local causal vertex`

is source-backed in the relevant scopes.

The next arrow

`generalized local causal vertices -> unique well-defined multi-vertex causal functional`

remains `BLOCKED`.

Consequently `composition -> G3 dynamics -> physical RG -> continuum -> spin-2 -> GR -> matter/QFT -> predictions` cannot yet be promoted.

## Interpretation ceiling / claim locks

No full causal multi-vertex amplitude theorem; no unique K5 extension theorem; no regulator-independence theorem; no physical CRQN RG map/fixed point; no G3/F9/G8/K5 promotion; no generic-spin signed-P3 theorem; no new physics and no complete quantum gravity.

The result does not prove that E3-E8 cannot be supplied by a future independently motivated bridge. It proves only that they are not supplied by the frozen source authority strongly enough to make the current CRQN v0.2 composition object unique and mathematically defined.

## Exact next admissible step

Do not repeat `E1/E2` work and do not return to fixed-spin control ranks.

Highest-information successor: prospectively test one **explicit causal composition inheritance theorem** for `E3-E6` from the parent EPRL-KKL state sum under the BCG/Beltrán causal replacement, including orientation/duality and normalization. In parallel as an independent theorem lane, determine whether any such inherited composition can even be defined on the Iter077Q supported extension family without a new `E7/E8` prescription.

If no exact inheritance bridge exists, retain `BLOCKED_MULTI_VERTEX_CAUSAL_OBJECT_DEFINITION`. If a bridge is proved, the next physical gate is whether composition reduces the Iter077Q infinite-dimensional ambiguity or merely propagates it.