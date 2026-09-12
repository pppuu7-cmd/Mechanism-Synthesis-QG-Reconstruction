# Iteration 062 preregistration — ordered-wedge orientation-sensitive kappa→spectral bridge

Preregistered prospectively after terminal Iter061 and before any Iter062 implementation or production result.

## Motivation
Iter061 exactly obstructs every orientation-blind edge-local identification between the unordered physical causal sign `kappa_ab=sigma_a sigma_b` and the Toller spectral branch sign, because source-backed wedge-order reversal leaves `kappa` unchanged but flips the spectral branch. The minimal non-fitted repair is to include only the orientation datum already present in the ordered group argument `g_b^-1 g_a`.

This gate asks whether the canonical ordered-edge sign supplies a fully covariant bookkeeping bridge compatible simultaneously with Iter056 S4 orientation cocycle, Iter059 source-backed branch swap, Iter058 strong-tournament/positive-circulation theorem, and the physical K4 sigma classes. It does not assume the bridge is a physical sector selector.

## Frozen objects
Vertices are `{0,1,2,3}`. For an ordered wedge `(a,b)`, define the canonical orientation sign

`eta(a,b)=+1` if `a<b`, and `eta(a,b)=-1` if `a>b`.

The only bridge family tested is

`s(a,b)=c * eta(a,b) * kappa_{ab}`,

with global convention `c in {+1,-1}` and `kappa_{ab}=sigma_a sigma_b`. The global sigma redundancy is fixed by `sigma_0=+1`, giving exactly eight physical sigma classes. No edge-dependent coefficient, fitted sign, amplitude weight, counterterm, or post-hoc selector is allowed.

## Frozen exact tests
For every one of the 8 physical sigma classes, both global conventions `c`, all 24 S4 relabelings, and both wedge-order states:

1. **Reversal law:** verify `eta(b,a)=-eta(a,b)` and therefore `s(b,a)=-s(a,b)` while unordered `kappa_ab` is unchanged, exactly matching the Iter059 branch-swap requirement.
2. **S4 covariance:** recompute the canonical-orientation cocycle under each permutation and verify that direct relabeling of the ordered bridge equals the Iter056 orientation-cocycle action on spectral signs.
3. **Convention control:** verify that changing global `c` reverses every tournament edge and preserves strong-connectivity / Iter058 strict-chamber feasibility status. No convention may be preferred by this gate.
4. **Positive-circulation transport:** for every strong image, reconstruct the deterministic Iter058 positive circulation and verify exact kernel/sign conditions; for every non-strong image, reconstruct a one-way directed cut and verify the exact conservation obstruction.
5. **Physical-class census:** report, but do not interpret as a sector probability, the number of the 8 sigma classes mapping to strong vs non-strong tournaments. The count must be invariant under `c`, S4 relabeling, and wedge reversal.
6. **Orbit consistency:** every resulting spectral sign vector must lie in the Iter057 orientation-aware orbit atlas and retain its orbit feasibility label under all allowed transformations.

## Frozen classifiers
- `ITER062_SOURCE_OR_IMPLEMENTATION_INVALID`
- `K4_ORDERED_ORIENTATION_BRIDGE_COVARIANCE_FAIL`
- `K4_ORDERED_ORIENTATION_BRIDGE_COVARIANT_CONVENTION_UNFIXED`

## Interpretation rule
A PASS establishes only that the minimal ordered-wedge orientation factor is an exact covariance-compatible bridge between physical `kappa` data and the spectral-sign geometry, up to an unfixed global branch convention. It may authorize a subsequent prospective direct-causal-vertex analyticity gate using the bridged signs, with tree/cycle-basis/permutation/order independence and exact EPRL controls.

A PASS does **not** select a physical causal sector, does not choose the global convention `c`, does not prove that strong-connectivity alone is sufficient for the full source-defined amplitude, and does not establish a contour, absolute integrability, a distributional finite part, vertex finiteness/divergence, K5, G3, F9, G8, complete quantum gravity, or new physics.
