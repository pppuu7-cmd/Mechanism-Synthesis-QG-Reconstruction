# Iter082G-SM — K5 supported-jet Čech descent result

Date: 2026-09-15

## Authoritative classification

`K5_SUPPORTED_JET_CECH_DESCENT_EXACTLY_SOLVABLE_WITH_GLOBAL_JET_GAUGE_FREEDOM_SCOPED`

Verdict: **`PASS_EXACT_SCOPED`**.

This result is deliberately scoped to the prospectively frozen abstract scalar normal-order jet modules `J_k` of dimensions `omega_k+1` for `(omega_3,omega_4,omega_5)=(0,3,8)`. It is not a theorem for the full tensor normal-jet space and not a global distributional patching theorem.

## Prospective / production chain

Scientific preregistration before implementation:

- prereg commit `2cfc7ec27905fc60eb3fe133d827dbf9e579232d`;
- `prereg/ITER082G_SM_K5_SUPPORTED_JET_CECH_DESCENT.md`.

Implementation / production:

- implementation commit `0dbded5bb0cc463dca726af2477f2c38fca5dbd4`;
- production workflow commit `fd108d7c6d0ffee8681ef7cbfb20ef261cec3a45`;
- Action run `34901591129`, terminal success;
- artifact `10370872893`;
- artifact ZIP digest `sha256:e9e71e981554f3c4c24da26f12dc8e609d8fda2df80fc3219ba7b0b616189853`;
- extracted aggregate JSON SHA256 `135b8c6c6a0ba37a2d32a352cbfcc885459b294f0711f765cfaa0aa269fc69bf`;
- implementation payload SHA256 `5b24bab70bbaf6ae47efd6792b53e55f5a471800cdc7f90b3d41b4e59791afbf`;
- prereg payload SHA256 `06aa69e87f5aa6d2f1fe21f6def8ed0b4f90c69aa2260c581fb55ccbb04bd4e6`.

No frozen scientific criterion was changed after production inspection.

## Exact scoped audit

For each abstract normal-order jet module:

- K3: `omega=0`, dimension 1, 2 deterministic basis 1-cocycles;
- K4: `omega=3`, dimension 4, 8 deterministic basis 1-cocycles;
- K5: `omega=8`, dimension 9, 18 deterministic basis 1-cocycles.

The exact pullback matrices induced by the frozen Iter082F one-dimensional radial restrictions are invertible, pairwise inverse-consistent and satisfy the X/V/W triple-overlap cocycle in every module.

For every deterministic basis 1-cocycle, the solver constructs a 0-cochain `(b_X,b_V,b_W)` whose Čech coboundary reproduces all three overlap data exactly. All residuals are zero over `Q`, including independent triple-overlap reconstruction.

All 120 S5 block-label permutations preserve the 16 divergent-block set. All transition matrices preserve the degree filtration without lowering normal order.

Crucially, the reconstruction remains non-unique: adding one globally transported supported-jet vector to all three chart corrections leaves every overlap coboundary unchanged. This global supported-jet gauge freedom was mechanically verified for every basis 1-cocycle.

All six frozen negative controls are rejected: non-cocyclic overlap data, corrupted X→W transition, singular transition, absolute-label-dependent correction, order-lowering correction, and declaring the free global Čech mode to be a physical selector. The preferred-label control survives only 24/120 permutations.

## Scoped conclusion

Within the explicit three-chart atlas and the frozen abstract scalar normal-order coefficient modules, there is no additional algebraic Čech-H1 obstruction: compatible supported-jet overlap differences are exact coboundaries.

This means the local extension-class ambiguity can be reconciled algebraically across the three-chart nerve **without choosing physical finite parts**. The surviving global supported-jet mode confirms that Čech solvability is an admissibility statement, not a selector.

## What remains open

Iter082G does not prove:

- the corresponding theorem for the full tensor/right-SU2 invariant normal-jet module;
- existence of globally patched distributions on the physical `SL(2,C)^4` configuration space;
- partition-of-unity independence for singular Toller amplitudes;
- continuity/topological completeness of the required distribution space;
- physical finite-part or scale selection;
- regulator independence, causal closure, RG closure, G3/F9/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete QG.

## Next analytic blocker

The next admissible step is a **full-module / actual distribution-space descent test**, not another scalar Čech repetition. A useful successor must either lift the twisted Čech construction to the corrected right-SU2 invariant tensor normal-jet module, or define an actual distributional partition-of-unity patching construction with source-compatible overlap transports.

All finite coefficients and subtraction scales must remain symbolic.