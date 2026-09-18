# Prospective preregistration — K5 G8 matching-covariance composition diagnostic

Frozen before implementation/production.

## Parent authority

Terminal post-collapse diagnostic run `35404490633`, artifact `10571294546`, classification `K5_S5_POSTCOLLAPSE_DEFECT_MATCHING_COVARIANCE_COMPOSITION`.

## Frozen lane

Use exactly the same mask/ray/cycle as the parent diagnostic: mask `1`, ray `W1`, S5 cycle `(0 1 2 3 4)` represented as `[1,2,3,4,0]`. Freeze the first parent-failing retained matching:

`((0,1),(2,3),(4,5),(6,7),(8,9))`.

No other matching may be substituted after seeing output.

## Question

Localize the first exact disagreement in G8 matching-covariance composition without evaluating or consuming scientific N/B leading orders or q18 partials.

## Required independent routes

Reconstruct the frozen matching contribution by two exact-rational routes:

1. canonical matching object followed by the already-authoritative S5 edge/orientation transport and target covariance geometry;
2. direct target-frame reconstruction from permuted edge pairs, orientation cocycle/signs, and target covariance entries.

Decompose comparison into frozen stages:

H1 edge-pair permutation / canonicalization;
H2 orientation cocycle and pair sign;
H3 covariance-entry index pullback/pushforward convention;
H4 per-pair transported covariance factor equality;
H5 ordered five-pair product equality;
H6 permutation-insensitive five-factor multiset equality;
H7 final frozen matching contribution equality.

## Mandatory validity controls

- exact rational arithmetic wherever algebraic data are rational;
- parent G1-G7 checks reproduced as true without changing their formulas;
- 10-edge ordering unchanged;
- retained matching census remains 945;
- source-term census remains 100000 where provenance validation touches source data;
- q18 values unused;
- no N/B leading coefficients or orders emitted;
- deliberate omitted-orientation-sign control must be rejected;
- deliberate covariance-index transpose/pullback mutation must be rejected;
- deliberate swapped edge-pair control must be rejected;
- canonicalize-pair roundtrip must pass for all five pairs.

## Frozen classifier

If provenance/controls fail: `INVALID_IMPLEMENTATION_OR_PROVENANCE`.

Otherwise report the earliest failed stage only:

- `K5_G8_DEFECT_EDGE_PAIR_PERMUTATION`
- `K5_G8_DEFECT_ORIENTATION_COCYCLE_SIGN`
- `K5_G8_DEFECT_COVARIANCE_INDEX_CONVENTION`
- `K5_G8_DEFECT_PER_PAIR_COVARIANCE_FACTOR`
- `K5_G8_DEFECT_ORDERED_PRODUCT_ASSEMBLY`
- `K5_G8_DEFECT_FACTOR_MULTISET_ASSEMBLY`
- `K5_G8_DEFECT_FINAL_MATCHING_CONTRIBUTION`
- or `K5_G8_FROZEN_MATCHING_COMPOSITION_EXACT` if H1-H7 all pass.

Frozen criteria must not be changed after production output is viewed.

## Claim locks

Implementation diagnosis only. Resolver remains `0/64` authoritative. No heavy resolver rerun, Repair-2 promotion, N/B authority, global Stokes/IBP, K5 periods, F9/G3/G8 promotion, regulator-independence theorem, `NEW_PHYSICS_FOUND`, physical sector selection, or complete-QG claim is authorized by this diagnostic alone.