# Iter077N-SM result — supported ambiguity survives vertex integration and standard gluing does not select it

**Date:** 2026-09-14

## Provenance

- Prospective preregistration: `prereg/ITER077N_SM_SUPPORTED_AMBIGUITY_SURVIVAL_AND_GLUING.md`, commit `ee08121c94fd802f9111313d6f089fbf2ab10181`.
- Source lock: `sources/ITER077N_SM_GLUING_SOURCE_LOCK.md`, commit `3543b523595b9b4d239866423ff279ae28f7236c`.
- Implementation: `distributional/iter077n_sm_supported_ambiguity_gluing.py`, commit `aa7440a939941b5bdde4e6f5c07f8f63ddfe8562`.
- Workflow/production head: `.github/workflows/iter077n_sm_supported_ambiguity_gluing.yml`, commit `7b12b0f8207d129ffd9b79bda158db77e265f8f6`.
- Authoritative run: `34789869127`.
- Lane A artifact `10328305627`, digest `sha256:eaa6d39eda0fc732007a5cb2637a3eab4b13947b009262603942620f21da7d31`.
- Lane B artifact `10328066074`, digest `sha256:8530ea7ea38850cd6cd742d8e0bb7d9722ad6932e5ccb61fea41e0af94551824`.
- Lane C artifact `10327504463`, digest `sha256:454886636344e0831cdaf7438c1ae917f961c283fac7563ac8e964e94fbe10a9`.
- Aggregate artifact `10328420436`, digest `sha256:04fecbabcdf0db984665da0220bf2e1499b9ccaf911e721e721471a4284bddd3`.

## Classification

`ITER077N_SM_K5_SUPPORTED_AMBIGUITY_SURVIVES_VERTEX_INTEGRATION_STANDARD_STATE_SUM_GLUING_DOES_NOT_FIX_COEFFICIENT_EXACT_SOURCE_SCOPED`

Scientific verdict: **PASS** for the preregistered scoped statement.

## Exact findings

### Lane A — integrated survival

The compact common-collision coefficient was evaluated exactly for all 32 all-`j=1/2` boundary-intertwiner basis states by using the same invariant node tensors and replacing all compact pure-gauge edge holonomies by the identity. This is exactly equivalent to normalized Haar integration over `SU(2)^4` for the supported `F_SU2 delta_N` term.

- boundary components checked: `32`;
- exactly nonzero compact boundary functionals: `16`;
- zero compact boundary functionals: `16`;
- exact-row checksum: `8923ae7f43fa83b9da1e9095d3ef195e6d208031ff6824a6a1a15a2d9912b936`.

Therefore the Iter077M ambiguity is not merely a local distributional freedom in the kernel of the group integration. It changes the integrated fixed-causal vertex on at least half of the frozen minimal boundary basis.

### Lane B — standard gluing algebra

For one universal local coefficient `c`,

`A_c = A_0 + c L`.

The standard two-vertex state-sum contraction across an internal basis gives identically

`G_c = G_00 + c(G_L0+G_0L) + c^2 G_LL`.

This is the ordinary bilinear composition operation on the supplied vertex tensors. Without a separate c-independent refinement/cylindrical/composition equation, it is satisfied for every input value of `c`; standard gluing itself does not solve for `c`.

### Lane C — source selector audit

The frozen causal-vertex source focuses on one vertex and explicitly leaves the many-vertex theory as future work. No projector/idempotency equation, cylindrical-consistency equation, refinement identity, joint K5 normalization, or c-independent causal composition law was found that fixes the supported coefficient.

## New scientific fact

The extension ambiguity exposed by Iter077L/M survives the actual vertex integration and therefore affects the physical single-vertex boundary functional in the controlling all-`j=1/2` sector. Ordinary spin-foam state-sum gluing does not remove the ambiguity; it propagates it into multi-vertex amplitudes.

Consequently the local-amplitude blocker can no longer be characterized merely as an off-shell/local-integrand ambiguity. A genuinely stronger selector — e.g. a source-derived refinement/cylindrical condition, an RG fixed-point condition, a transfer/composition law with an independently defined target, or another physical normalization principle — is required before the causal vertex is unique.

## Claim ceiling

This result does not establish that no stronger consistency principle can select the extension. It does not provide G3, regulator independence, generic-spin control, full causal-vertex divergence/nonexistence, a causal-sector-sum theorem, a physical source-to-K4 pushforward, or a complete quantum-gravity model.

## Exact next admissible step

Do not repeat ordinary gluing. Prospectively test the strongest independently motivated **refinement/cylindrical/RG selector** that can be formulated for this causal vertex. The gate must distinguish:

1. an existing source-backed selector that uniquely fixes the supported local freedom;
2. a new but independently motivated RG/refinement law that defines a new CRQN mechanism/version and is falsifiable;
3. no applicable selector, leaving `BLOCKED_NONUNIQUE_EXTENSION_SELECTOR_MISSING`.
