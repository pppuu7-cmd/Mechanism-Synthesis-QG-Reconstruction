# Source-faithful joint K5 meromorphic bridge — nested-Jacobian scientific repair result

Date: 2026-09-15

Status: **PASS_EXACT_SCOPED — SCIENTIFIC REPAIR PRODUCTION**

Classification:

`BRIDGE_AUTHORITY_CONFIRMED_SCOPED`

## Why this repair was necessary

The earlier bridge production correctly identified the incremental orthogonal normal ranks `(6,3,3)` but incorrectly treated their independent polar powers `(5,2,2)` as the boundary Jacobian powers of the **nested** K3-K4-K5 blow-up used in the Mellin argument.

The independent Critic caught this after the first confirmation. The initial Critic confirmation was explicitly superseded by

`results/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_ADVERSARIAL_REVIEW_REPAIR1.md`, commit `b0a5ba418189fb4e3c37f7adf9b370a7fd5aad21`,

which returned `REJECTED_SCIENTIFIC_PENDING_REPAIR` for B4/B6 only.

The scientific repair was prospectively frozen before implementation:

- `prereg/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_CRITIC_REPAIR_1.md`, commit `148dd5130c448420419a807826fdfd84bb1228ef`.

Corrected derivation:

- `sources/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_NESTED_JACOBIAN_REPAIR_DERIVATION.md`, commit `b227ad0d433d89c9fe1df589535b354961e5a91b`.

Corrected machine-readable lock:

- `sources/raw/source_faithful_joint_k5_bridge_lock.json`, commit `ae43268efc7e4b7bdc46df514a8fc03b3fe2267e`.

Corrected validator:

- `scripts/source_faithful_joint_k5_bridge_gate.py`, commit `2dfb4ad341bca7ebf1e41521909052e5056980cc`.

Final repaired workflow/head:

- `.github/workflows/source_faithful_joint_k5_bridge_gate.yml`, commit `6aca4249f956f5e1a05a9e214660495427ab7470`.

## Authoritative scientific-repair production

- GitHub Actions run `34954021547`, terminal `success`;
- job `104331589295`, terminal `success`;
- head `6aca4249f956f5e1a05a9e214660495427ab7470`;
- artifact `10390666862`, `source-faithful-joint-k5-bridge-gate`;
- artifact ZIP digest `sha256:2989f3b4aad1c1ccb8494f2f11821a66df17e99c15b731c3d84c587ed1003abb`;
- production JSON SHA256 `079587747eb747e067400b88a3969982a495c17eee9150543cdede856d883acd`.

All workflow assertions, all B1-B9 predicates and all malformed controls passed.

An intermediate run `34953991571` on the repaired scientific validator already returned B1-B9 true and the corrected geometry, but the historical workflow attempted to print the removed key `chain_rank_values` and terminated with a Python `KeyError`. It uploaded no artifact and is an implementation-interface failure only. It is not scientific production authority.

Earlier bridge runs `34952663240` and `34953022566` predate discovery of the nested-Jacobian scientific defect and are historical evidence only; neither is current bridge authority.

## Correct nested geometry

For a maximal divergent chain

`K3 subset K4 subset K5`,

authoritative orthogonal normal increments have physical real dimensions

`(6,3,3)`.

The hierarchical blow-up scales are

`u5 ~ rho5`,

`u4 ~ rho5 rho4`,

`u3 ~ rho5 rho4 rho3`.

Therefore the cumulative dimensions seen by the boundary defining functions are

`(6,9,12)`

and the pulled-back Haar/tubular density has radial powers

`(5,8,11)`:

`rho3^5 rho4^8 rho5^11 d rho3 d rho4 d rho5`

up to a smooth nonvanishing angular/tangential factor.

Production derives these values mechanically from the block projectors; they are not target literals supplied to the scientific predicates.

## Source singular exponents and recovered divergence degrees

There are edge increments

`(3,3,4)`

along K3, K4/K3 and K5/K4.

Since every frozen `j=1/2` Toller wedge has leading order `beta^-2`, the cumulative source powers are

`(-6,-12,-20)`.

Combining with the corrected Haar powers gives

`(-1,-4,-9)`.

Thus the superficial divergence degrees are exactly

`omega=(0,3,8)`.

This reproduces the earlier independently established K3/K4/K5 scaling-degree chain from the actual nested blow-up geometry rather than inserting those numbers as an assumption.

## Exact regulator incidence map

The 16 regulator parameters remain attached to the physical divergent blocks: 10 K3, 5 K4, 1 K5.

For every divergent collision face `C`, define

`L_C(lambda)=sum_(B subseteq C, |B|>=3) lambda_B`.

The 16-by-16 incidence matrix from block parameters `lambda_B` to face parameters `L_C` is lower triangular when blocks are ordered by increasing cardinality, with unit diagonal.

Production verifies exactly:

- matrix size `16`;
- rank `16`;
- lower triangular with unit diagonal;
- determinant `1`.

Thus no regulator direction is lost and the face-linear forms are equivalent coordinates on the regulator parameter space.

For the explicit uniform witness `lambda_B=1`, production obtains

- K3: `L=1`;
- K4: `L=5`;
- K5: `L=16`.

These satisfy the sufficient convergence conditions

`Re L_K3>0`, `Re L_K4>3`, `Re L_K5>8`.

Hence the corrected full convergence chamber is demonstrably nonempty.

## Corrected Mellin local model

At a maximal nested corner the actual full source family has local radial form

`U(lambda) ~ rho3^(L_K3-1) rho4^(L_K4-4) rho5^(L_K5-9) A(rho,angles,lambda)`,

where `A` is polyhomogeneous conormal and holomorphic in the initial convergence chamber.

The pole-producing Taylor orders at the physical regulator origin are exactly

- K3: `0`;
- K4: `3`;
- K5: `8`.

Production verifies `(0,3,8)` independently from the source edge counts and nested Jacobian.

The standard Mellin theorem for polyhomogeneous conormal objects on manifolds with corners therefore supplies the multivariate meromorphic continuation in the face forms `L_C`, equivalently in the original block parameters because the incidence map is invertible.

## Repaired B1-B9 outcome

All frozen predicates are true in production:

- B1 true K5 simultaneous multivariate family;
- B2 exact post-Toller source ordering, no spectral substitution;
- B3 all 32 boundary components retained;
- B4 original Haar density retained and **correct nested Jacobian `(5,8,11)` explicitly derived**;
- B5 source branch/sign/reversal conventions preserved;
- B6 full resolution plus corrected Mellin exponents, invertible incidence map and nonempty convergence chamber;
- B7 no arbitrary regulator-space metric, finite part, fitted subtraction or sequential specialization; regulator independence is explicitly not claimed;
- B8 S5 covariance with no preferred label/chain;
- B9 actual multivariate polar germ sufficient to authorize only a downstream multivariate polar-normal-jet analysis after independent Critic review.

## Mechanical negative controls

The same validator rejects all of the following:

1. representative boundary component;
2. auxiliary regulator-space `Q`;
3. `beta+i epsilon` substitution;
4. omitted Haar density;
5. post-hoc holomorphic projection / finite part;
6. preferred sequential specialization;
7. preferred label;
8. K5-only incidence replacing the 16-block family;
9. wrong source order;
10. historical `(5,2,2)` incremental powers promoted as nested Jacobian;
11. singular regulator incidence map;
12. empty convergence chamber;
13. wrong nested source exponents;
14. false regulator-independence claim.

All 14 controls passed.

## Scheme firewall

The bridge remains scoped to the explicit source-derived block defining functions

`q_B=(1/|B|) sum_(a<b in B) beta(g_b^-1 g_a)^2`.

Under

`q'_B=exp(phi_B) q_B`,

one has

`U'(lambda)=exp[(1/2)sum_B lambda_B phi_B] U(lambda)`.

Thus existence of the meromorphic continuation and its polar divisor are robust under such a holomorphic gauge transformation, but lower Laurent coefficients can mix in the presence of higher-order poles. No regulator-independence theorem follows.

## Scientific conclusion

The previously reopened B4/B6 blocker is repaired at Researcher level. The frozen local all-`j=1/2` full-source K5 object admits the explicit `q_B`-scheme multivariate meromorphic continuation with correct nested Haar geometry and true K3/K4/K5 incidence.

This result is **not yet downstream authority until an independent repaired Critic review confirms the scientific repair**.

## Interpretation ceiling

No unique physical finite part; no unique K5 extension; no one-parameter `A_-1`; no regulator independence; no causal-vertex finiteness/divergence theorem; no generic-spin completeness; no global all-strata patching; no E3/E4/E6 closure; no G3/F9/G8/K5 promotion; no RG/continuum/spin-2/GR/matter/prediction result; no `NEW_PHYSICS_FOUND`; no complete quantum gravity.
