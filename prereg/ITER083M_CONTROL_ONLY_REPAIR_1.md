# Iter083M control-only repair 1 — frozen negative-control execution

Date: 2026-09-15
Status: **PROSPECTIVELY FROZEN BEFORE REPAIR IMPLEMENTATION / REPAIRED PRODUCTION OUTPUT**

Parent scientific preregistration: `prereg/ITER083M_SM_SOURCE_NORMAL_GEOMETRIC_RADIAL_BASIS.md`, commit `c801299beb44816941fd441715e3eb03c73740c7`.
Controlling invalidation: `results/ITER083M_ADVERSARIAL_IMPLEMENTATION_REVIEW.md`, commit `063087c5dfcf0cca9e2565cf75ef82c8ea640f6f`.
Historical production run `34917280262` and Researcher result `40416f9011ddeafd6a7201d48b218b7eaf7b6ec1` remain provenance-only and scientifically non-authoritative because the frozen malformed controls were not actually injected.

## Repair scope

This is a **control-only** repair. The parent hypothesis, exact object, source authority, P0-P7, frozen positive calculations, PASS classification, interpretation ceiling and all scientific inputs remain unchanged. No new radial geometry, regulator, boundary state, finite-part prescription, normalization law or physical selector is introduced.

The repaired validator must make PASS depend on actual execution of the eight frozen negative controls rather than aliases to positive predicates or prose-string presence.

## Frozen malformed-control injections

### C1 — rooted / label-weighted normal metric

Construct an explicit positive diagonal label metric with unequal label weights on the five-node ambient label space, e.g. `diag(1,2,3,4,5)`. Restrict/use it in the same block/transport context as the canonical barycentric geometry and feed it through an S5 covariance validator. At least one S5 permutation must fail covariance. The control passes only when the malformed rooted metric is mechanically rejected.

### C2 — ten-edge regulator Q identification firewall

Represent the Iter083G-J-K auxiliary edge-regulator object and the physical normal-fiber object with structured type/domain metadata. The auxiliary object lives on the ten-edge regulator space; the physical object lives on `R^3 tensor Std_p` with physical dimensions `6,9,12` for K3/K4/K5. An attempted identity/alias map between these domains must be rejected by a validator that checks object kind/domain/dimension and does not rely on disclaimer text.

### C3 — nontrivial J component on Std_p

Retain the exact parent check that the two-dimensional ambient S_p-invariant form family restricts to a one-dimensional form space on `Std_p`; explicitly verify that the all-ones matrix J restricts to zero for p=3,4,5. A purported physically distinct J deformation must therefore be rejected.

### C4 — non-orthogonal forest increment

Take at least one valid maximal chain and deliberately corrupt one increment by adding a nonzero multiple of another increment, e.g. `B_bad = B + A`. Feed `(A,B_bad,C)` through the same idempotence/orthogonality/decomposition validator used for the good chain. The control passes only when the malformed chain fails.

### C5 — single-chain-only coverage

Run the same all-chain coverage validator on a deliberately truncated list containing only one maximal chain. It must fail the exact requirement of 20 maximal K3-K4-K5 chains. The good path must still validate all 20.

### C6 — exact nonlinear beta overclaim

Use a structured source-authority object in which the only authorized relation is the tangent statement `beta_ab(r)=r|x_a-x_b|+O(r^2)`. Inject a claim object asserting an exact nonlinear equality with the remainder removed. The source-authority validator must reject that claim mechanically.

### C7 — finite-part / subtraction-scale promotion

Use a structured interpretation-claim validator. Inject a claim that the tangent radial basis uniquely fixes a finite part and subtraction scale. It must be rejected because the parent P7 explicitly forbids such promotion.

### C8 — global nonlinear / patching promotion

Using the same structured interpretation firewall, inject a claim that the local tangent/tubular radial basis supplies a unique global nonlinear defining function / all-strata global patching. It must be rejected mechanically.

## Positive calculations retained unchanged

The repaired implementation must preserve the exact parent computations:

- P0 authority locks;
- P1 exact S_p invariant-form dimensions on R^p and `Std_p` for p=3,4,5;
- P2 exact boost-vector invariant symmetric-form dimension;
- P3 `L_Kp=pP_p` for p=3,4,5;
- P4 every nested K3->K4 and K4->K5 variance/projector identity;
- P5 all 20 maximal chains with label ranks `(2,1,1)` and physical ranks `(6,3,3)`;
- P6 all 120 S5 covariance transports;
- P7 the unchanged interpretation ceiling.

## Terminal classification lock

A repaired `PASS_EXACT_SCOPED` is permitted only if all P0-P7 pass **and** C1-C8 are executed and rejected as frozen above.

If a malformed control is not actually injected or the validator is insensitive to its mutation, classify `INVALID_IMPLEMENTATION`.

If the exact positive mathematics fails under the unchanged scientific object/source authority, do not disguise that as a control failure; classify according to the parent scientific contract and preserve the failure witness.

Expected PASS classification remains exactly:

`ITER083M_SM_SOURCE_BOOST_GEOMETRY_GIVES_UNIQUE_LOCAL_FOREST_RADIAL_QUADRATIC_BASIS_SCOPED`

Interpretation ceiling remains exactly the parent ceiling: no physical finite-part selector, no source-authorized analytic continuation, no full nonlinear group-manifold radial theorem, no all-strata global renormalization, no regulator independence, no generic-spin theorem, no G3/F9/G8/K5 promotion, no `NEW_PHYSICS_FOUND`, no complete-QG claim.
