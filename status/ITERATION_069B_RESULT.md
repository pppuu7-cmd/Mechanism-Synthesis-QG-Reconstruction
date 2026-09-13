# Iteration 069B result — held-out K4 joint-spectral radial validation

Date: 2026-09-13

## Authoritative provenance

- Preregistration: `cdcbf58d59f9d610b38a1ed1996b54c175fe9897`
- Implementation: `ec9e8ba7a727f1b83c858ad93a9b067ffdf6adb8`
- Launch/head: `a38c41c10d8f5747d31389546183c39af2ff4699`
- Workflow run: `34741408690`
- Aggregate job: `103681654751`
- Aggregate artifact: `10313135598`
- Digest: `sha256:034d4438e84a963252e71a722292ee79ed00cbc8c37cbf795d182b5baf04ef59`

## Frozen held-out matrix

- source cases: H6 and H7;
- all eight physical factorized K4 causal sigma classes;
- tree/cycle bases: S0, S1, P0, P1;
- primitive radial directions: V1=(1,2,3), V2=(2,-1,3), V3=(3,1,-2).

Eight GitHub jobs evaluated 24 exact subcases each, for **192/192 exact held-out cases**.

## Frozen result

Terminal classification:

`ITER069B_K4_JOINT_SPECTRAL_HELDOUT_GENERIC_GROWTH_PLUS6_CAUSAL_SIGN_INDEPENDENT`

All 192 cases passed:

- all six exact edge slopes nonzero;
- source net radial degree exactly `+6`;
- no-contact control net radial degree exactly `-6`;
- source/control leading coefficients nonzero.

Across all 24 fixed `(case,tree,direction)` groups, the exact source leading coefficient was identical for all eight physical causal sigma classes.

## Scientific interpretation

This independently validates the Iter069A homogeneous result away from its symbolic setup: the generic `+6` source growth is stable on two new source parameter points, four K4 bases, three new radial directions, and all eight physical causal sign classes.

The result does **not** establish a multivariate boundary value and does not imply a full causal-vertex divergence theorem. It shows that causal denominator signs do not remove the highest homogeneous growth of this reduced source-backed joint-spectral rational family.

Therefore the remaining physical route must use a source/analyticity-selected multivariate distributional boundary-value construction rather than an ordinary improper real-cycle integral or a fitted sequential finite part.

No K5/G3/F9/G8 promotion is authorized.
