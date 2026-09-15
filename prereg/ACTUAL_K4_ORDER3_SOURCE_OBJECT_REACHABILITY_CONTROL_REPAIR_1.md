# K4 order-3 source-object reachability — control-only repair 1

Date: 2026-09-15
Status: **PROSPECTIVELY FROZEN BEFORE REPAIR IMPLEMENTATION / REPAIRED OUTPUT**

Parent scientific preregistration: `prereg/ACTUAL_MULTIVARIATE_K4_ORDER3_OBJECT_DEFINITION_REACHABILITY.md`, commit `a6983a4d7379bf73f48752a4de357450996d8572`.
Historical run: `34963831115` on head `e82fb6d2496cd063a8f512dd8dd3ec182b9e9cd2`, terminal failure and **`INVALID_IMPLEMENTATION`**.

## Repair reason

The historical validator correctly loaded the frozen requirement-status manifest and all scientific controls, but its evidence verifier used brittle case-sensitive literal substring matching. Three evidence anchors in `sources/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_DERIVATION.md` failed only because the Markdown source inserts line breaks / indentation and uses lowercase `define` in prose:

- the displayed `q_B = r^2 ... + O(r^3)` formula spans normalized whitespace rather than the exact raw literal;
- the prose says `define the exact block radius` with lowercase `define`.

This is an implementation/provenance-control defect only. The historical run emits no authoritative scientific verdict and no artifact.

## Frozen control-only repair

Change only the evidence-anchor matcher so that both source text and frozen anchor are compared after:

1. Unicode-preserving lowercase normalization;
2. collapsing every run of whitespace to a single ASCII space.

Do **not** change:

- any R1-R10 status in `sources/raw/k4_order3_source_object_authority_audit.json`;
- any evidence path or commit anchor;
- HYPOTHESIS, exact OBJECT, DEPENDENCY, SOURCE AUTHORITY, frozen inputs;
- positive or negative controls;
- PASS/BLOCKED/INVALID taxonomy;
- interpretation ceiling;
- K4 coefficient values (none are allowed to be emitted).

The repaired run is authoritative only if normalized evidence verification, the synthetic complete positive control, and all 12 frozen malformed controls pass. Otherwise it remains `INVALID_IMPLEMENTATION`.
