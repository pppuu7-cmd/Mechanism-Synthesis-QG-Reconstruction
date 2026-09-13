# Iter076S result — unique twisted quadratic curvature allows one-jet contamination on transitive faces

**Date:** 2026-09-13

## Administrative provenance

The scientific predictions were originally frozen in colliding prereg commit `62bdff74931814d2fbf598b6d0898bcb0140b271` under the name Iter076R, after the earlier authoritative R preregistration `3c6c179aeea5bafa02c986b0cd6a197b65f4e24e` already existed. They were administratively renumbered as Iter076S in `382dc5424d9a5f7eaa2d6c6772c01ada56541014` with no mathematical threshold, lane, control, or interpretation change.

The colliding R follow-up run `34782381742` independently passed and is retained as a reproducibility cross-check only. The Iter076S rerun below is authoritative for this follow-up.

## Authority

- frozen scientific predictions: `62bdff74931814d2fbf598b6d0898bcb0140b271`
- renumbered preregistration: `382dc5424d9a5f7eaa2d6c6772c01ada56541014`
- renumbered implementation: `893222700291c3f39f877b3f481512443234a206`
- production/workflow head: `f6de9eb571a5ef05154ebd7b04d206cc2e6afa1b`
- authoritative run: `34782561421`
- lane jobs: A `103792113268`, B `103792113096`, C `103792113258`, D `103792113297`
- aggregate job: `103792160990`

Artifacts:

- A: `10325342803`, digest `sha256:433700e4dc0eee9a025b4400937faf993c9c23e0856d3e1285e679320e25c532`
- B: `10324788366`, digest `sha256:e3f0d4d1b9c0a59b42788443f6c7ea9b457715bbfe11ba69ef4f047cf5ed939d`
- C: `10324798364`, digest `sha256:0c7cf6485bdfee4d7e2754df35bed2e07c97225ca7505c69c70fc9aca81736e0`
- D: `10325382788`, digest `sha256:90e57a2f8b69b20f9d47cd538fc697d260b2dbd9753044cf1ec3839cac7c7778`
- aggregate: `10325780492`, digest `sha256:025282186fa349b5bbb47af87ff135886ca54af39182800f3bf84227ac4f3fac`

All frozen lanes A/B/C/D and aggregate completed successfully.

## Frozen classification

`ITER076S_UNIQUE_TWISTED_QUADRATIC_CURVATURE_ALLOWS_ONEJET_CONTAMINATION_ON_TRANSITIVE_FACES_EXACT_SCOPED`

## Lane A — exact curvature Hom space

The exact rational covariance system for a quadratic map `B: Sym2(Cut) -> Cycle` with the same sign twist as the linear Hodge map has 18 unknown coefficients, constraint rank `17`, and nullity exactly `1`.

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

## Lane C — transitive proper-face survival

The contamination map was transported through the frozen Iter073/076B transitive-face complex:

- total proper-face restrictions: `96`;
- rank-1 nonzero restrictions: `32/96`;
- rank-0 restrictions: `64/96`;
- every causal-class/tree lane has rank multiset `[0,0,0,0,1,1]`;
- stacking all six proper faces in each class/tree gives rank `2`;
- stacking the full transitive family gives rank `3`.

Therefore there is **no nonzero generic source one-jet direction that is globally invisible across the full frozen transitive family**.

## Lane D — controls and scope

- zero-curvature control gives zero face contamination on all `96` checks;
- an altered curvature matrix outside the unique covariance line fails exact twisted covariance;
- no physical curvature is selected;
- no physical source one-jet is established;
- the one-jet cannot be bypassed by symmetry;
- the nominal `epsilon^-1` coefficient remains unestablished;
- generic finite-spin signed P3 remains blocked;
- no G3/F9/G8/K5 promotion follows.

## Scientific consequence

Iter076Q removed the global `+H/-H` ambiguity from homogeneous quadratic linear transport. Iter076R showed that symmetry permits a nonlinear curvature contamination channel. Iter076S strengthens this: the generic one-jet contamination actually survives the exact transitive proper-face restriction structure relevant to the degree-two layer.

The next admissible work is therefore source-faithful and must distinguish the singular Toller/contact structure from a regular numerator jet. In particular, a naive derivative of an individual Toller branch at the group identity is not automatically a valid source one-jet object; the regular numerator/Jacobian factorization must first be defined from the published Toller representation.

Only after the relevant regular source one-jet and actual nonlinear source-to-K4 curvature are source-defined may the physical degree-two coefficient and nominal `epsilon^-1` term be formed.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no physical nonlinear source-to-K4 map; no assertion that physical curvature or physical one-jet is nonzero; no nominal `epsilon^-1` coefficient; no causal-vertex finiteness/divergence theorem; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; retain the published spectral `i epsilon`.