# Iter083Q control-only repair 1 — supersession-candidate ingestion

Date: 2026-09-15
Status: **PROSPECTIVELY FROZEN BEFORE INSPECTING THE DETECTED CANDIDATE CONTENT AND BEFORE REPAIR IMPLEMENTATION**

Parent scientific contract: `prereg/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_AUTHORITY_GATE.md`, commit `4151c02452edd3e5e2c49952686e42e64c6dc180`.
Initial implementation: `019704d0566f0c055961c9a4ccd3b5097fe42b92`.
Initial workflow/head: `3889de168d1705ac57bdd8c022c49548cad26417`.
Historical run: `34952709428`, implementation-invalid because the supersession guard detected newer source/result authority candidates and correctly refused classification.

## Detected candidates

The pre-classification delta guard reported two source-side candidates not included in the initial manifest:

- `sources/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_DERIVATION.md`;
- `sources/raw/source_faithful_joint_k5_bridge_lock.json`.

Their substantive content has not been used to assign a scientific verdict before this repair freeze.

## Control-only repair obligation

The repaired validator must ingest these files, verify their provenance/ancestry and exact source citations, and treat them as possible **new positive authority** rather than automatically whitelisting them or allowing older absence records to override them.

The same parent B1-B9 predicates and classifications remain frozen. For each detected candidate, the validator must determine whether it is:

1. genuine source/mathematical bridge authority satisfying one or more B predicates with exact auditable formulas/theorems and source matching;
2. a conditional/preparatory derivation that explicitly preserves the blocker;
3. invalid or unresolved evidence.

A newer valid positive bridge must supersede older scoped absence statements without creating a false contradiction. A conditional/preparatory file may be consumed only at its stated interpretation ceiling.

## Repair controls

The repaired implementation must additionally demonstrate:

- a synthetic newer positive authority candidate can supersede an older absence record and produce positive predicate status rather than `FAIL`;
- a synthetic newer conditional candidate does not promote a B predicate;
- an unresolved candidate forces `INVALID_IMPLEMENTATION`/unresolved evidence rather than `BLOCKED_OBJECT_DEFINITION`;
- the nine malformed bridge controls from the parent implementation remain rejected by the same bridge validator.

## Scientific-contract lock

No B1-B9 wording, source ordering, negative controls, PASS/BLOCKED/FAIL/INVALID taxonomy or interpretation ceiling changes. This repair only closes an implementation/evidence-ingestion defect exposed by the supersession guard.
