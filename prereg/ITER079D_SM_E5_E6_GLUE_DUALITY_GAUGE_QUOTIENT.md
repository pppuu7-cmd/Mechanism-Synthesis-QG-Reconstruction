# Iter079D-SM preregistration — E5/E6 boundary duality and gauge quotient inheritance

## Prospective status
Frozen **before** implementation/production and before observing any Iter079D numerical result.

## Scientific question
After Iter079C establishes that E3/E4 are not uniquely fixed by source-defined one-vertex causal data plus the parent combinatorial skeleton, isolate the remaining pre-distributional composition data:

- **E5:** boundary gluing / dual-orientation identification;
- **E6:** gauge quotient/fixing and its normalization for the composed causal object.

Do the currently frozen causal/source and parent-skeleton data uniquely determine these objects, or do exact inequivalent choices survive until an explicit causal inheritance rule is supplied?

This gate does **not** test E7/E8 distributional extension transport and does not define a physical multi-vertex amplitude.

## Frozen exact witness space
Use `H = Q^2` only as a minimal algebraic witness space. Frozen local vectors and pairing:

- `VL = (1,2)`
- `VR = (3,-1)`
- `B0 = diag(2,1)`

No coefficient fitting after results.

## Lane A — prerequisite/provenance lock
Require durable authoritative records:

1. Iter079B classification that E5/E6 are missing required causal inheritance objects;
2. Iter079C authoritative BLOCKED classification for E3/E4;
3. no claim that the parent EPRL-KKL skeleton may be silently promoted to causal inheritance authority.

Failure of this provenance contract => `INVALID`, not scientific FAIL.

## Lane B — E5 exact duality-identification nonuniqueness witness
Freeze two boundary orientation-reversal/duality involutions

`D1 = [[1,0],[0,-1]]`,
`D2 = [[0,1],[1,0]]`.

Both must satisfy exactly:

- `D_i^2 = I`;
- `det(D_i) = -1`;
- invertibility.

Define composed witness amplitudes

`Z_i = VL^T B0 D_i VR`.

Frozen expected underdetermination criterion:

- both duality maps satisfy the same minimal algebraic involutive orientation-reversal contract;
- `Z_1 != Z_2` exactly.

If true, the present data do not uniquely fix E5. This does not claim both are physical choices; it proves an additional source-derived E5 selector/identification is required to distinguish them.

## Lane C — E6 exact gauge-quotient normalization witness
Model only the normalization freedom of a free one-dimensional noncompact gauge orbit after the reduced integrand has been fixed. Freeze a nonzero reduced witness `Zred = 5` and two invariant quotient/Haar normalizations `c=1` and `c=2`.

Frozen exact amplitudes:

`Q1 = 1 * Zred`,
`Q2 = 2 * Zred`.

Frozen criterion:

- both constants preserve gauge invariance of the quotient measure convention;
- `Q1 != Q2` exactly;
- current frozen source authority contains no E6 normalization theorem selecting one.

This is scoped only to gauge-quotient normalization underdetermination. It is not a statement that a properly normalized causal theory cannot fix E6.

## Lane D — scope/source audit
Require exact controlling claim locks and verify that E7/E8 are not imported into this gate. The current source/durable authority must still record E5/E6 as missing objects rather than established formulas.

## Frozen classification
If A and D provenance are valid and both exact witnesses B/C show nonuniqueness, classify:

`ITER079D_SM_E5_E6_BOUNDARY_DUALITY_AND_GAUGE_QUOTIENT_NOT_UNIQUELY_FIXED_BY_CURRENT_CAUSAL_INHERITANCE_DATA_EXACT_SCOPED`

with verdict `BLOCKED`.

If a frozen witness fails algebraically, classify a scoped scientific FAIL for that proposed nonuniqueness mechanism. If provenance/implementation contract fails, classify `INVALID`.

## Claim locks
No full causal multi-vertex theorem; no unique K5 extension; no regulator independence; no E7/E8 result; no RG/G3/F9/G8/K5 promotion; no complete-QG claim; no `NEW_PHYSICS_FOUND`.

## Next admissible decision
If BLOCKED, E3-E6 are now separately shown to require bridge data. Do **not** manufacture such bridge data. The next high-value physical task is to search/derive a source-faithful causal composition prescription that simultaneously specifies E3-E6. E7/E8 may be tested only against an actually defined composed functional.
