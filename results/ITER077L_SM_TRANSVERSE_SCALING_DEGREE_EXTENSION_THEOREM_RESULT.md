# Iter077L-SM result — transverse scaling-degree extension theorem at the K5 common collision

**Date:** 2026-09-14

## Provenance

- Prospective preregistration: `prereg/ITER077L_SM_TRANSVERSE_SCALING_DEGREE_EXTENSION_THEOREM.md`, commit `565a36453cf781b1af366da6960ab7f55e6605f1`.
- Source/theorem derivation: `sources/ITER077L_SM_TRANSVERSE_EXTENSION_THEOREM_DERIVATION.md`, commit `1a6cb5331098287823e55c7db5452a976b8501a5`.
- Upstream source-ordered K5 authority: `results/ITER077I_SM_SOURCE_ORDERED_JHALF_K5_L1_RESULT.md`.
- Published-source object-definition authority: `results/ITER077K_SM_SOURCE_SELECTED_K5_BOUNDARY_VALUE_OBJECT_DEFINITION_RESULT.md`.

## Frozen classification

`ITER077L_SM_TRANSVERSE_SD20_CODIM12_EXTENSION_EXISTS_BUT_SCALING_ALONE_NONUNIQUE_ORDER8_LOCAL_FREEDOM_THEOREM_SCOPED`

Scientific verdict: **PASS** for the preregistered theorem-scoped hypothesis.

## Exact/theorem findings

1. The simultaneous common-collision singular locus is locally the smooth embedded submanifold
   `N = SU(2)^4 subset SL(2,C)^4`
   after gauge fixing the root group variable.
2. Its real codimension is exactly `12`: four independent three-dimensional boost directions are normal to the compact `SU(2)^4` locus.
3. On a conic normal patch around an Iter077I exact nonzero witness, all ten relative boost directions remain nonzero away from `N`, so no extra partial-edge collision stratum is encountered for sufficiently small nonzero radius.
4. Iter077I gives a nonzero source-ordered leading term `r^-20 a(omega)` on such a patch for each of the 32 all-`j=1/2` boundary basis components. Therefore the transverse scaling degree is exactly `sd_N=20`.
5. Brunetti-Fredenhagen Theorem 6.9 is in the regime `codim(N) <= sd_N < infinity`: same-scaling-degree local extensions exist, but scaling degree alone does not select a unique extension.
6. The transverse degree above threshold is `20-12=8`. Accordingly, the theorem leaves finite normal-jet freedom through order 8; differences between local extensions are supported on `N` and may involve normal derivatives through that order, with coefficient data along `N` subject to any additional conditions imposed separately.
7. The positive control `sd=11<12` lies in the unique-extension regime. The threshold control `sd=12` already admits delta-supported freedom.

## New scientific fact

The Iter077K blocker is now sharpened. The missing fixed-causal K5 object is **not** blocked by a theorem of extension nonexistence: standard finite-scaling-degree distribution theory supplies local extensions. The obstruction is uniqueness/physical selection. The published one-wedge causal prescription does not, by itself, choose among the order-8 local extension freedom exposed by the exact source-ordered K5 singularity.

Thus a future unique CRQN vertex must derive additional source-selected conditions strong enough to fix this finite local freedom and must prove compatibility with the full boundary contraction, gluing/composition and regulator independence. Merely choosing a finite part or common regulator would be a new prescription unless independently derived.

## Adversarial scope check

This result does not claim that every order-8 local term is physically allowed. Covariance, causal composition, gluing, analyticity, Ward-like constraints, normalization, or another independently derived condition may reduce or eliminate the freedom. No such uniqueness theorem is supplied by scaling-degree extension theory itself, and Iter077K found no joint K5 selector in the frozen primary causal-Toller sources.

## Claim ceiling

No full causal-vertex divergence or nonexistence theorem; no proof that no unique physically preferred extension exists; no regulator-independence theorem; no generic-spin result; no causal-sector-sum theorem; no physical source-to-K4 pushforward; no nominal `epsilon^-1` coefficient; no G3/F9/G8/K5 promotion; no new-physics or complete-QG claim.

## Exact next admissible gate

Prospectively test whether the **already published** symmetries/composition/covariance constraints of the causal vertex uniquely annihilate the order-8 extension freedom. This must be formulated as a finite local-jet selector problem on the actual K5 common-collision submanifold. If residual freedom survives all source-backed constraints, retain `BLOCKED_OBJECT_DEFINITION`; do not choose coefficients post hoc.