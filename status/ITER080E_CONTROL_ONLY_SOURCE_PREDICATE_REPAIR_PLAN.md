# Iter080E-SM — control-only source-predicate repair plan

**Scope:** implementation/provenance repair only. This does **not** alter the scientific preregistration frozen at commit `f1a465a059f7c4da8270bed8021f920013b7f5da`.

## Defect being repaired

The historical Iter080E Lane B derived P1–P5 eligibility from `status` values already written into `analysis/iter080e_sm_joint_k5_selector_source_matrix.json` and then only checked matching Iter080E-authored snapshot anchors. That is circular and violates the frozen `INVALID` clause forbidding trust in prefilled verdict/status booleans. Historical Iter080E scientific classification therefore remains `INVALID_IMPLEMENTATION` and is not promoted by this plan.

## Frozen science that MUST NOT change

- exact source corpus: Bianchi–Chen–Gamonal `2601.23162`, Bianchi–Chen–Gamonal `2604.24945`, Beltrán `2603.22661v2`;
- exact P1–P5 definitions and all PASS / FAIL / BLOCKED / INVALID rules from the original preregistration;
- Iter077Q ambiguity space `W` and source ordering;
- selector eligibility requires all P1–P5 to be exactly `EXPLICIT`;
- positive/negative controls and interpretation ceiling;
- no new source, selector axiom, branch convention, regulator, numerical tolerance, fitted coefficient, or post-hoc subspace.

## Allowed implementation repair

Lane B shall derive source predicate statuses only from the already-frozen **source-specific evidence files** whose blob SHAs are pinned in the existing machine matrix. It must not use the matrix fields `predicates.*.status`, `eligible`, `classification`, `verdict`, or Iter080E-authored source-snapshot predicate labels as scientific evidence.

The repaired implementation must:

1. verify every source-specific evidence file against its frozen blob SHA and fail closed on mismatch/missing evidence;
2. evaluate P1–P5 from explicit source-specific evidence anchors/facts in those pinned files;
3. keep the original matrix statuses only as non-authoritative expected-control values, never as inputs to eligibility;
4. add a non-circularity adversarial control proving that mutating all prefilled matrix predicate `status` strings cannot change derived P1–P5 or selector eligibility;
5. fail closed if source-specific evidence is ambiguous or insufficient for a predicate;
6. preserve the old historical runs/results as non-authoritative invalid history.

## Frozen source-specific evidence basis

No new evidence is admitted. The repair may use only the evidence files already pinned by the frozen Iter080E matrix:

- `sources/CAUSAL_SPINFOAM_VERTEX_2026_SOURCE_SNAPSHOT.md` for `2601.23162`;
- `sources/TOLLER_MATRICES_2026_CONJUGATION_BRANCH_FLIP_SNAPSHOT.md`, `sources/CAUSAL_VERTEX_TOLLER_ONEJET_SOURCE_SNAPSHOT.md`, and `sources/ITER079A_SM_CAUSAL_MULTIVERTEX_SOURCE_INHERITANCE_SNAPSHOT.md` for `2604.24945`;
- `sources/ITER079A_SM_CAUSAL_MULTIVERTEX_SOURCE_INHERITANCE_SNAPSHOT.md` for `2603.22661v2`.

## Classification lock

Only a new terminal aggregate from the repaired implementation may restore Iter080E authority. Until then Iter080E remains `INVALID_IMPLEMENTATION`. A repaired BLOCKED result, if produced, remains only a frozen-corpus source-object-definition statement and cannot be promoted to a universal no-selector theorem.

All standing claim locks remain unchanged.