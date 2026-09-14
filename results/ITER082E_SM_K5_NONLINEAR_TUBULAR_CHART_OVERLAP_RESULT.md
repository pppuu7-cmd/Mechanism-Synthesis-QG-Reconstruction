# Iter082E-SM — K5 nonlinear tubular chart-overlap / extension-class result

Date: 2026-09-14

## Authoritative classification

`K5_NONLINEAR_TUBULAR_CHART_OVERLAP_PRESERVES_ALLOWED_SUPPORTED_JET_CLASS_EXACT_SCOPED`

Verdict: **`PASS_EXACT_SCOPED`**.

This is a local finite-jet/tubular result only. It is not a global `SL(2,C)^4` extension theorem and does not select finite parts.

## Prospective / production chain

Scientific preregistration, before implementation:

- `15105f6326f652db44809336579060a46403ca8d`
- `prereg/ITER082E_SM_K5_NONLINEAR_TUBULAR_CHART_OVERLAP_EXTENSION_CLASS_INDEPENDENCE.md`

Initial implementation / production:

- implementation `fefcfdd01d3afe58bcbf63227c2904e18e0d4e3a`;
- workflow production `27d726762f795326d905f09e340556aa3fae3d22`;
- run `34895924300`, artifact `10368810908`, ZIP digest `sha256:62352195c05d1bcd58738cf7ca7d58785b533bfe4cd208208e2e9c06bc354cf2`.

That green run is **quarantined as `INVALID_IMPLEMENTATION`** by `results/ITER082E_ADVERSARIAL_IMPLEMENTATION_REVIEW.md`: P2/P3/P4/P5 were not all mechanically computed.

Control-only repair 1 was frozen before repair implementation:

- prereg `eab36d2b70b911a54440f05f43eb0beb89fce571`;
- implementation `bf5bae441a6e9d37c7e96b68355a56a7a0c8d32b`;
- run `34896145784`, artifact `10368621471`, ZIP digest `sha256:28648c0fcc6320446340988e073c09636554573dd5f96502a77557bd344839bb`.

Repair-1 mechanically passed parent P0–P5 but exposed an incorrectly wired label-dependent negative control. The resulting CI failure is an **implementation/control failure, not scientific FAIL**.

Control-only repair 2 was frozen before its implementation:

- prereg `287003ffd9d76e712351805afab7fe4eeb4ac46d`;
- repair driver implementation `480aa0e65fdae87fb2b5dabb3e83d2bc2e9c3696`;
- authoritative production `c1ed0877fa47b3b72f760650b4537b487207855e`;
- run **`34896247290`**, job `104150906384`, terminal success;
- artifact **`10368652613`**;
- artifact ZIP digest **`sha256:02ca64d497a7c28c7cba9b881ecdf290f34f9bc9e88875f65c99f062534e5e5e`**;
- extracted aggregate JSON SHA256 **`21383c9dfe1b85e14dba9560a6454f8d455360ac8cc62138637c6294ee5f03e5`**;
- repaired implementation payload SHA256 `555eff4adcf25e21d8373ee44da9fb3bc63137cb9eb002159c7d23159a7ccaa1`.

No frozen scientific criterion was changed in either repair.

## Frozen nonlinear charts

At each node, compare the rapidity/exponential boost-normal coordinate `x` with the hyperbolic-velocity coordinate

`v = (sinh(|x|)/|x|) x`,

with inverse

`x = (asinh(|v|)/|v|) v`.

Exact rational Taylor coefficients were retained through vector degree 9, one order above the deepest allowed K5 jet order 8.

Both truncated compositions were exactly identity through degree 9:

- `G(F(x)) = x + O(|x|^10)`;
- `F(G(v)) = v + O(|v|^10)`.

## Exact mechanical audit

The authoritative artifact records:

- 16 divergent blocks;
- 20 maximal `K3 subset K4 subset K5` chains;
- all 120 positive S5 permutations passed under the actual chart evaluator;
- 16+16 explicit block-collision tests passed in both chart directions;
- 117+117 tangent-normal barycentric basis checks passed;
- 210+210 exact diagonal-ideal generator checks passed;
- 78 ideal-power checks passed for the frozen K3/K4/K5 bounds;
- 120 nested-chain generator checks passed;
- 220 degree triples of total degree <=9 were represented;
- 8800 exact nested-order checks passed in both directions with zero leakage;
- 96 exact signed-permutation radial covariance controls passed;
- all six frozen malformed controls were mechanically rejected.

The corrected preferred-label cubic control passes only 24/120 permutations and is therefore correctly rejected as non-S5-covariant; its first recorded failure is permutation `[1,0,2,3,4]`.

## Mathematical scoped conclusion

For this explicit pair of nonlinear tubular boost charts, the node-wise overlap is a local analytic diffeomorphism tangent to identity. The exact audit verifies that it preserves each K3/K4/K5 diagonal ideal and its relevant powers. Consequently the nested finite-jet filtration used by Iter082D is transported into itself through the frozen orders

`(omega_3, omega_4, omega_5) = (0,3,8)`.

Thus chart transport changes an admissible local forest representative only within the already-authorized supported-jet extension class in this scoped finite-jet setting. Representative equality is neither required nor used.

This is an **extension-class covariance statement, not a selector**. All finite coefficients and analytic scales remain symbolic.

## What this closes / does not close

Closed in scoped form:

- the specific Iter082D nonlinear rapidity ↔ hyperbolic-velocity tubular overlap;
- preservation of the K3/K4/K5 normal-ideal jet filtration through degree 9;
- local supported-jet extension-class compatibility for this overlap.

Still open:

- a global tubular atlas and cocycle/patching theorem on the relevant `SL(2,C)^4` neighborhood;
- a global Toller forest extension;
- source-derived finite-part / scale / invariant-jet selector;
- exact total physical ambiguity dimension;
- causal E3/E4/E6 bridge;
- replacement for the failed selected-Toller Han `d^2` bound;
- regulator independence and RG/refinement closure.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no unique K5 extension; no physical selector; no theorem that 28/16 conditions suffice; no global forest-extension theorem; no regulator independence; no G3/F9/G8/K5 promotion; no arbitrary fitted subtraction constants, scales or preferred finite parts.
