# Iter083M adversarial implementation review

**Date:** 2026-09-15

## Reviewed Researcher result

Researcher result: `results/ITER083M_SM_SOURCE_NORMAL_GEOMETRIC_RADIAL_BASIS_RESULT.md`, commit `40416f9011ddeafd6a7201d48b218b7eaf7b6ec1`.

Frozen / production chain:

- preregistration `c801299beb44816941fd441715e3eb03c73740c7`;
- theorem derivation `f566a9aad2d7adfbee16557de9a7fb9f8bdfa777`;
- initial validator `74db7bbf6c9b364e8e4e26a17d428260c3e671e9`;
- pre-production source-lock alignment `3c681c85a52b0c1b7d32ec5b933f6cc7a56ad898`;
- production workflow/head `6916f3fb2f89f7f009bf9d3354b9dfe8c001de74`;
- Actions run `34917280262`, terminal `success`;
- job `104217547168`, terminal `success`;
- artifact `10376298881`;
- artifact ZIP digest `sha256:7659e611caa70da2803583ad0ee0f4ee29e7a3a9924058ee180d4c9a7a21566e`;
- production JSON SHA256 `5b11c3060b7809921d35323fec089f280c07614728e6282b7ea549301753b7a3`.

Researcher classification: `ITER083M_SM_SOURCE_BOOST_GEOMETRY_GIVES_UNIQUE_LOCAL_FOREST_RADIAL_QUADRATIC_BASIS_SCOPED`, Researcher verdict `PASS_EXACT_SCOPED`.

A prior same-session review `results/ITER083M_ADVERSARIAL_REVIEW.md` classified the result `CONFIRMED_SCOPED`. The implementation audit below identifies a frozen-control defect not addressed in that review. The earlier review is therefore insufficient as scientific authority for the production PASS.

## Frozen-contract check

The scientific preregistration freezes P0-P7 **and eight negative controls**. The production workflow explicitly treats those controls as part of the PASS contract by asserting

`assert all(d['controls'].values())`.

The relevant frozen controls include:

- reject a label-dependent/rooted normal metric;
- reject identifying the ten-edge regulator `Q` with the physical normal metric;
- reject non-orthogonal forest increments;
- reject use of only one maximal chain;
- reject promotion of the tangent relation `beta_ab=r|x_a-x_b|+O(r^2)` to an exact nonlinear distance law;
- retain finite-part/scale freedom and the nonlinear/global patching blocker.

These are not optional prose after the fact: the executable emits a `controls` object and the workflow requires every entry to be true before declaring `PASS_EXACT_SCOPED`.

## Concrete implementation witness

The validator does **not** construct and reject several of the frozen malformed controls. Instead it aliases their verdicts to positive-predicate booleans or to a literal-text firewall:

```python
controls={
    'reject_rooted_metric':p6,
    'reject_edge_regulator_q_identification':p7,
    'reject_J_as_distinct_on_std':...,
    'reject_nonorthogonal_increments':p5,
    'reject_single_chain_only':len(chains)==20,
    'reject_nonlinear_beta_overclaim':p7,
    'retain_finite_part_scale_freedom':p7,
    'retain_global_patching_blocker':p7,
}
```

Here `p6` only verifies covariance of the **good barycentric projectors**. No rooted/label-weighted metric is ever constructed and passed through the covariance validator. Therefore `reject_rooted_metric=true` does not certify rejection of the frozen negative control.

Likewise `p5` verifies that the **good** forest increments are orthogonal; no deliberately non-orthogonal increment is injected. Therefore `reject_nonorthogonal_increments=true` is a positive-control restatement, not the frozen negative-control test.

The entries `reject_edge_regulator_q_identification`, `reject_nonlinear_beta_overclaim`, `retain_finite_part_scale_freedom`, and `retain_global_patching_blocker` are all assigned the single boolean `p7`. But `p7` is only

```python
require(args.theorem,[
  'does not yet define a renormalized extension',
  'No exact nonlinear identity',
  'finite parts can depend'
])
```

so those four controls pass when three strings occur in the theorem note. No ten-edge `Q` object is type-checked against the physical normal fiber, no false nonlinear beta identity is injected into an authority validator, and no attempted finite-part/global-patching promotion is mechanically rejected.

This is exactly the failure mode the repository has repeatedly treated as implementation-invalid: a green control field is not scientific evidence when the malformed object was never exercised by the claimed validator.

## Counterexample-first mutation test

The implementation defect can be stated without using any production substantive value. Consider replacing the supposed rooted-metric negative-control candidate by an arbitrary rooted metric, or omitting that candidate entirely. The executable output `controls['reject_rooted_metric']` is unchanged because it depends only on `p6`, which evaluates the canonical barycentric projector family and receives no rooted metric input.

Similarly, changing an imagined edge-regulator `Q` negative-control object cannot change `controls['reject_edge_regulator_q_identification']`, because no `Q` is an input to that predicate. The value is controlled solely by whether the theorem prose contains three required strings.

Thus the implementation is observationally insensitive to the frozen malformed objects it claims to reject. This is a direct implementation witness, not a generic concern.

## Independent theorem check

This review does **not** find a scientific counterexample to the core scoped mathematics:

- on `R^p`, an `S_p`-invariant symmetric form has diagonal/off-diagonal orbit data, and its restriction to `Std_p` is one-dimensional up to scale;
- the 24-element orientation-preserving signed-permutation subgroup already forces a symmetric form on the boost-vector factor to be scalar, consistent with the unique `SO(3)`-invariant Euclidean form;
- `L_Kp=pP_p` and the nested variance identity are exact linear-algebra identities;
- the source lock supplies only the tangent statement `beta_ab(r)=r|x_a-x_b|+O(r^2)`, and the Researcher result correctly keeps the nonlinear/global and finite-part ceilings open.

Therefore this is **not** `SCIENTIFIC_FAIL_CONFIRMED`. The mathematical theorem may well survive a valid repair. The current terminal production simply does not satisfy its own frozen negative-control contract.

## Source-object / ordering firewall

The reviewed theorem concerns only the local/tubular boost-normal quadratic geometry inherited from the already source-ordered K5 collision analysis. It does not multiply contact distributions, exchange the order of spectral/spinor integration with K5 multiplication, alter the published one-wedge spectral `i epsilon`, or derive a full physical finite part. The Iter077 contact-formula erratum and historical Iter077E/F quarantine remain controlling.

The ten-edge regulator metric `Q` from Iter083G-J-K is a different auxiliary regulator-space object and must not be identified with this physical normal-fiber quadratic geometry without a separate bridge. The frozen preregistration itself states that distinction; the defect here is that the executable negative control does not mechanically test it.

## Boundary / regulator / distributional scope

No new boundary representative is selected. The theorem imports the frozen all-`j=1/2` common-collision geometry and does not prove a generic-spin or all-strata statement. It constructs no distributional extension and no meromorphic finite part. Multiplicative radial scale, nonlinear defining-function continuation, forest weights/order, subtraction convention and global patching remain unselected. No regulator-independence theorem follows.

## Verdict

`INVALID_IMPLEMENTATION`

The terminal run and Researcher result must not be used downstream as authoritative closure of Iter083M until the frozen negative controls are actually executed. The earlier `CONFIRMED_SCOPED` review is superseded for authority by this later concrete implementation witness; the Researcher result file itself remains unchanged for provenance.

## Authorized repair

A **control-only repair/retry under the unchanged Iter083M preregistration** is authorized. It should preserve the hypothesis, object, source inputs, P0-P7, classification rules and interpretation ceiling, while making PASS depend on actual malformed-control rejection. At minimum:

1. construct a rooted/label-weighted candidate metric/projector and feed it through the same S5 covariance machinery; it must fail;
2. construct a non-orthogonal forest increment and feed it through the same idempotence/orthogonality/decomposition validator; it must fail;
3. add a structured object/type firewall that distinguishes the ten-edge regulator `Q` space from the physical `R^3 tensor Std_p` normal fiber and rejects an attempted identification;
4. inject an exact-nonlinear beta claim into the same source-authority validator and require rejection because the frozen authority contains only the tangent `O(r^2)` relation;
5. represent finite-part selection and global-patching promotion as structured claim flags/objects and require the interpretation firewall to reject them, rather than proving only that disclaimer strings occur in a theorem note;
6. retain all exact positive P1-P6 calculations and artifact/provenance checks unchanged.

If the repair changes the scientific object, source authority, hypothesis, PASS/FAIL criteria or interpretation ceiling, it requires a newly named prospectively preregistered successor gate instead.

Until a valid repaired terminal Iter083M exists, `AUTHORIZED_NEXT_GATE` is this control-only repair. Do not yet promote the proposed radial meromorphic finite-part successor from Iter083M.