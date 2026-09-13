# Iter077I-SM result — source-ordered all-j=1/2 K5 leading local L1

Date: 2026-09-14

## Authoritative provenance

- Workflow run: `34786586785`
- Production head: `102fc7268b732bead5dfcf6d61fe4479ae1d3030`
- Lane A job: `103803070767`, artifact `10326866875`, digest `sha256:3c25ece3c76ecc84a3214fe71b1659fc65a7415cf56d5edfca624ad8b674f22d`
- Lane B job: `103803070817`, artifact `10326627184`, digest `sha256:de78c9d92dedf8f130417e252c80cfa2504990a83e69d091e03a2a3ac6f2a7ff`
- Lane C job: `103803070819`, artifact `10327155717`, digest `sha256:484b32b9cae14a51797b556e18f80c240fab3b259339ffb56b8cfedd94bf3008`
- Lane D job: `103803070859`, artifact `10327210575`, digest `sha256:ca947468f164f64fb6b51704f9ce36ff9fb3584f83666a03f52e779b5ad99e19`
- Aggregate job: `103803109954`, artifact `10326812769`, digest `sha256:b9e7d617598acaeb60ee7018e3ee4f78a232b32be86b112da4713352d9797887`

All four raw lane artifacts and the aggregate artifact were consumed before classification.

## Frozen classification

`ITER077I_SM_SOURCE_ORDERED_JHALF_TOLLER_FUNCTION_K5_LEADING_TERM_NONZERO_ALL_32_BOUNDARY_COMPONENTS_NOT_LOCALLY_L1_EXACT_SCOPED`

Scientific verdict: `PASS` for the preregistered scoped hypothesis.

## Exact findings

1. The source ordering is the one-wedge Toller construction followed by the ten-wedge K5 product and group integration; the gate does not multiply the ten spinor-contact distributions termwise.
2. For `j=1/2`, each wedge has leading small-boost radial power `beta^-2` with nonzero common scalar `2/(1+gamma^2)`; at frozen `gamma=6/5` this scalar is `50/61`.
3. On the frozen nondegenerate common-collision ray, all 32 five-node boundary-intertwiner components have nonzero exact Gaussian-integer leading contractions. Lane B exact-row digest: `2fd44a481c5ca7a87744727678f211b17be048c173a9cf79fe10ff3a7b1decfd`.
4. Across all 16 factorized causal assignments and all 32 boundary components, `512/512` leading contractions are nonzero and equal to the all-plus leading coefficient in the frozen convention. Lane C exact-row digest: `6d4249958c1dc878e2d2bfabd88427db7bc7d2ecdde011437e6f3314c45fa1d7`.
5. Ten wedges give total homogeneous power `q=-20`. The four gauge-fixed boost variables give transverse dimension `d=12`, so the radial absolute-integrability exponent is `d-1+q=-9`, with first-moment margin `q+d=-8`.
6. Therefore every one of the 32 frozen leading boundary components is not locally absolutely integrable on an open angular neighborhood of the exact nonzero witness.

## Scope

This is a local `L1` obstruction only. It does **not** prove that the fully contracted causal vertex fails to exist as a conditional, oscillatory, Hadamard-finite-part, or source-selected correlated distributional boundary value. It does not establish regulator dependence, generic-spin behavior, a source-to-K4 pushforward, or a physical `epsilon^-1` coefficient.

## Next admissible gate

Test whether the complete 32-component leading angular coefficient spans the full boundary space over exact collision directions. If it does, no nonzero angle-independent boundary-state superposition can cancel the leading `r^-20` coefficient identically. This remains logically prior to any full causal-vertex divergence claim.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no physical causal-vertex finiteness/divergence theorem; no regulator-independence theorem; no generic finite-spin result; no physical source-to-K4 pushforward; no nominal `epsilon^-1` coefficient; no G3/F9/G8/K5 promotion.