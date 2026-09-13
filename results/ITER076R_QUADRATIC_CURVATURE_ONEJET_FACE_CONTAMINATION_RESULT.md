# Iter076R result — unique twisted quadratic curvature allows one-jet contamination on transitive faces

**Date:** 2026-09-13

## Authority

- confirmatory preregistration: `62bdff74931814d2fbf598b6d0898bcb0140b271`
- confirmatory implementation: `073a91f4492c0cbdd12080c4b14f13bae0b2466e`
- production/workflow head: `2cf08e1e9801605b1231db3a9942f579beea4f23`
- authoritative run: `34782381742`
- aggregate job: `103791713022`

Artifacts:

- A: `10325528643`, digest `sha256:a66e52eb9e5a4ea5be7f97d00bc5df18d6c8852965947cf25cba99cb271e6a1a`
- B: `10324763251`, digest `sha256:f633d4f4c45cb43a834711fd8c86bb39d3bed920fc3a78a0e8fef4bff8d04a82`
- C: `10325498756`, digest `sha256:ba2f76c818dcdbe05144b87fe349f0314e1a6457cf28d18f54638890d2a62d3a`
- D: `10325254321`, digest `sha256:f4c07e27fe9a5e1eb7a109aee2bf7985c4c1b8a7f1ecf18f3831b26f234f52f5`
- aggregate: `10325835040`, digest `sha256:a85f6e03b9c0b49006f571af2d5e8afbe36581e86e031c7d1baaa6d3572cd4f6`

All frozen lanes A/B/C/D and the aggregate completed successfully.

## Frozen classification

`ITER076R_UNIQUE_TWISTED_QUADRATIC_CURVATURE_ALLOWS_ONEJET_CONTAMINATION_ON_TRANSITIVE_FACES_EXACT_SCOPED`

## Lane A — exact curvature Hom space

The exact rational covariance system for a quadratic map `B: Sym2(Cut) -> Cycle` with the same sign twist as the linear Hodge map has:

- 18 unknown coefficients;
- constraint rank `17`;
- nullity exactly `1`.

With the frozen primitive normalization the generator is

`B0 = [[ 1, 0, 0,-1,-1, 0],
       [-1, 0, 1, 1, 0,-1],
       [ 1,-1, 0, 0,-1, 1]]`.

This is a unique **symmetry-allowed** curvature line. It is not evidence that the physical source-to-K4 pushforward realizes nonzero curvature.

## Lane B — inverse-map one-jet contamination

For the frozen exact Hodge coordinate map and `B0`, the inverse-coordinate correction maps a source one-jet `ell` to degree-two coefficients with rank exactly `3`.

The frozen coefficient map is

`T0 = [[-1,-1,-1],
       [-1,-1, 0],
       [ 1, 0, 1],
       [ 0, 0, 1],
       [ 0, 1, 1],
       [ 0, 1, 0]]`.

The `B=0` control gives identically zero contamination.

Thus symmetry does not annihilate generic one-jet contamination once nonlinear curvature is allowed.

## Lane C — transitive proper-face survival

The contamination map was transported through the frozen Iter073/076B transitive-face complex:

- total proper-face restrictions: `96`;
- rank-1 nonzero restrictions: `32/96`;
- rank-0 restrictions: `64/96`;
- every causal-class/tree lane has rank multiset `[0,0,0,0,1,1]`;
- stacking all six proper faces in each class/tree gives rank `2`;
- stacking the full transitive family gives rank `3`.

Therefore there is **no nonzero generic source one-jet direction that is globally invisible across the full frozen transitive family**.

This is stronger than merely exhibiting a nonzero quadratic curvature channel: the contamination survives the exact face-restriction structure relevant to the degree-two layer.

## Lane D — controls and scope

- zero-curvature control gives zero face contamination on all `96` checks;
- an altered curvature matrix outside the unique covariance line fails the exact twisted-covariance test;
- no physical curvature is selected;
- no physical source one-jet is established;
- the one-jet cannot be bypassed by symmetry;
- the nominal `epsilon^-1` coefficient remains unestablished;
- generic finite-spin signed P3 remains blocked;
- no G3/F9/G8/K5 promotion follows.

## Scientific consequence

Iter076Q removed the global `+H/-H` ambiguity from homogeneous quadratic linear transport. Iter076R now proves that this does **not** remove the need for source one-jet provenance: a unique symmetry-compatible nonlinear curvature channel exists and a generic one-jet can feed the physical degree-two face coefficients through it.

The next admissible gate is therefore source-faithful:

1. derive or audit the **full Toller/intertwiner numerator one-jet**, separately from the exactly even Haar/KAK radial density;
2. derive the actual nonlinear source-to-K4 curvature if the one-jet is nonzero;
3. only after both are source-defined may the physical degree-two coefficient and nominal `epsilon^-1` term be formed.

No denominator-only symmetry argument can replace this step.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no physical nonlinear source-to-K4 map; no assertion that physical curvature or physical one-jet is nonzero; no nominal `epsilon^-1` coefficient; no causal-vertex finiteness/divergence theorem; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; retain the published spectral `i epsilon`.
