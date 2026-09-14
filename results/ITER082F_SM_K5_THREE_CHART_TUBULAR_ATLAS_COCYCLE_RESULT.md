# Iter082F-SM — K5 three-chart tubular atlas / finite-jet cocycle result

Date: 2026-09-15

## Authoritative classification

`K5_THREE_CHART_TUBULAR_ATLAS_FINITE_JET_COCYCLE_CLOSED_EXACT_SCOPED`

Verdict: **`PASS_EXACT_SCOPED`**.

This is a local finite-jet atlas-consistency result only. It is not a global distributional patching theorem, not a Toller forest-extension theorem, and not a selector.

## Prospective / production chain

Scientific preregistration before implementation:

- commit `f4d524df3bbac8590953226b751bac660b58911c`;
- `prereg/ITER082F_SM_K5_THREE_CHART_TUBULAR_ATLAS_COCYCLE.md`.

Implementation / production:

- implementation `179ef1a5fe7e433bd8a327db87ce560f42f82d77`;
- production `3b439a6b0d5bfdd3ec5a19dfde3ddfcc10325763`;
- Action run `34896547503`, job `104151975917`, terminal success;
- artifact `10369102456`;
- artifact ZIP digest `sha256:352f8a4d8d49aee12a6f65e76c160408c7e3aeb66c539165ec421bf8048025e7`;
- extracted aggregate JSON SHA256 `0a997a439129d66ee11af3dc48227a320cb5b03dd587652c6bb36f1097c644a0`;
- implementation payload SHA256 `a7242c582c011d4201fe901891a099600a5c58bbcb73d51b2392ef398d802637`;
- prereg payload SHA256 `24a285e6f3b190d79765047c1f24ef5096274d7d99883a3659d14c7746c2346b`.

No frozen scientific criterion was changed after production inspection.

## Frozen atlas

Three node-wise normal coordinates were used:

1. rapidity/exponential coordinate `x`;
2. hyperbolic velocity `v=(sinh r/r)x`;
3. bounded-ball coordinate `w=(tanh r/r)x`, with `r=|x|`.

All six directed overlap maps were represented by exact rational radial Taylor series through vector degree 9, one order above the deepest K5 jet order 8.

## Exact audit

The authoritative artifact records:

- all six forward/backward pair compositions equal identity through degree 9;
- all six orientation-equivalent triple-overlap cocycle identities hold exactly through degree 9;
- all six directed overlaps pass all 120 S5 permutations;
- 288 exact signed-permutation SO(3) subgroup checks pass with zero failures;
- 16 K3/K4/K5 divergent blocks and 20 maximal K3 subset K4 subset K5 chains are retained;
- each directed overlap passes 210 diagonal-ideal generator checks with zero failures;
- 234 relevant ideal-power checks pass;
- 26,400 nested-order check classes pass;
- all collision tests have zero failures;
- all six frozen malformed controls are rejected.

The preferred-label cubic negative control passes only 24/120 permutations and is correctly rejected. Corrupting the X→W degree-5 coefficient is detected by the cocycle check; a singular linear chart, order-lowering map, numeric finite-part insertion, and use of the cocycle as a selector are also rejected.

## Scoped mathematical conclusion

For this explicit three-chart local tubular atlas, the finite-jet transports preserve the K3/K4/K5 diagonal ideals and the frozen jet filtration `(omega_3,omega_4,omega_5)=(0,3,8)`, and the transports close under an exact triple-overlap cocycle through degree 9.

Therefore the Iter082D/Iter082E supported-jet extension class admits a coherent nontrivial three-chart finite-jet atlas in this scoped construction.

This closes the specific local finite-jet cocycle concern. It does **not** imply arbitrary-chart/global atlas independence or existence of a globally patched distributional extension. Partition-of-unity compatibility, actual distributional descent on overlaps, finite-part/scale selection, and regulator independence remain open.

## Next blocker

Promote the analytic frontier to:

`K5_DISTRIBUTIONAL_CECH_PATCHING_AND_PARTITION_OF_UNITY_COMPATIBILITY`

A valid next gate must distinguish finite-jet coordinate descent from actual distributional patching, keep all finite coefficients/scales symbolic, and treat patching compatibility only as admissibility rather than a selector.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no unique K5 extension; no physical selector; no arbitrary-chart/global Toller forest-extension theorem; no regulator independence; no G3/F9/G8/K5 promotion; no fitted subtraction constants, scales, or preferred finite parts.