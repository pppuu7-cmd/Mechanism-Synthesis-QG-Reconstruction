# Repaired independent Critic — actual multivariate K4 order-3 parity

Date: 2026-09-15
Status: **CONFIRMED_SCOPED**

## Authority and repair chronology

Parent Critic preregistration: `76595a6bdc27553fb5ccec9f06942203d97dc520`.

The initial Critic implementation `3d637eb144ce2e979b419b807bfb6c02af18a6e9` and workflow head `de3f01118c482f9a37f37eab113f2cd2d5975f3f` produced run `35004252640`. That workflow was green, but the implementation populated several target facts as literals and then validated those same literals. It therefore did not satisfy the frozen independence requirement and is permanently reclassified here as **`INVALID_IMPLEMENTATION`**. Its scientific conclusion happened to agree with the repaired calculation, but it is not authority.

Control-only repairs were frozen before their implementations:

- repair 1 prereg `f24290d18a246d8ba1c6938e04d66b8769a8bd8e`;
- repair 2 prereg `3a3516f799dd70c6a41b6ec84790d27683d64c40`;
- repair 3 prereg `a4c735f1c6d1f5323b9b88e2026aa779a57639f5`.

Repair-1 run `35011898749` exposed two implementation-only evidence-matcher defects. Repair-2 run `35012028134` already had `scientific_ok=true`, `provenance_ok=true`, exact 364 partitions, 500000 source terms and zero S5 failures, but one malformed mutation was not rejected because duplicated baseline-degree fields were not cross-checked. These runs carry no terminal scientific Critic verdict.

Authoritative repair-3 implementation/workflow:

- repair-3 script commit `ee2ed7045e21cde10e442b42c6053ce3e0302c3c`;
- workflow/head `9063081ac93d9134807c8d39dcc4d83a0eea4322`;
- production run `35012269378`, terminal success;
- job `104526899873`, terminal success;
- artifact `10414077581`, `critic-actual-multivariate-k4-order3-parity`;
- artifact ZIP digest `sha256:30eebde38acb3465850470e0af11d98ba61acc863335899714303cac63c4fb10`;
- extracted production JSON SHA256 `a03b97f86c70a6dca9adb4e2cd07bc74d752f6db75938cf02011fd92c2941a44`.

## Verdict

`K4_ACTUAL_ORDER3_PARITY_CRITIC_CONFIRMED_SCOPED`

The repaired independent Critic confirms the Researcher theorem

`K4_ACTUAL_ORDER3_POLAR_COEFFICIENT_ZERO_EXACT_BY_FULL_NORMAL_INVERSION_PARITY_SCOPED`.

## Independent recomputation

The repaired Critic no longer accepts expected facts as self-confirming literals. It independently recomputes/checks:

- K4 normal dimension `9`, front dimension `8`, one-axis barycentric Gram determinant `4`, full Gram determinant `64`;
- full-normal inversion preserves the Gram form, antipodal front and positive measure;
- the Iter077I leading source matrix is linear and odd under `v -> -v`, and agrees with the authoritative source module;
- each K4 block has exactly six internal and four external K5 edges;
- all five K4 blocks and all 32 boundary components are traversed;
- the full source traversal contains exactly `500000` raw contraction terms with `0` source/edge-census failures;
- all `120` S5 transports have `0` failures;
- scaling degree `12`, normal dimension `9`, hence `omega_K4=3`;
- independently recomputed baseline Cartesian degree is `6` and is cross-checked against the scaling summary;
- the frozen grouping `6+4+1+1` gives exactly `12` analytic jet slots;
- all `364` weak degree-three partitions are enumerated, unique and complete, and every contribution has total degree `6+3=9`;
- regrouping the smooth q-family into 16 separate factors changes the partition count to `3654` but leaves total degree `9`, so the odd-parity conclusion is not an artifact of the 12-slot grouping;
- byte locks to the independently confirmed source-faithful K4 cubic bridge all match;
- Researcher preregistration/head/run/artifact/ZIP/production-JSON provenance and git ancestry are consistent.

Therefore the complete simple-K4 order-three coefficient is odd under full normal inversion while the front pairing is invariant, and the residue vanishes exactly.

## Adversarial controls

All fourteen malformed cases are rejected by the same repaired decision path:

1. literal-only evidence without recomputation;
2. wrong normal dimension;
3. non-antipodal front;
4. inversion-odd measure;
5. internal source-factor degree corruption;
6. omitted internal wedge;
7. incomplete partition family;
8. representative boundary component only;
9. one K4 block only;
10. commuting/BCH scalar surrogate;
11. post-hoc finite part;
12. preferred sequential continuation;
13. `beta+i*epsilon` substitution;
14. broken Researcher provenance.

No malformed control passes.

## Downstream authorization

The independent K4 Critic dependency is now genuinely closed. K5 order-eight production may proceed under the already-frozen scientific contract

`prereg/ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR_K5_LANE.md`, commit `7466325187f22043d1794379fd6e6dcf62e05abd`.

That K5 preregistration was frozen before any K5 implementation or K5 production result. Although it was historically opened during the interval in which the initial K4 Critic was incorrectly treated as authoritative, no K5 outcome had been inspected; the repaired K4 Critic now satisfies the dependency before K5 production begins. The K5 scientific criteria remain unchanged.

## Interpretation ceiling

This is a local simple-K4 residue theorem only. No K5 order-eight zero/nonzero result follows automatically; no finite part, unique physical extension, regulator independence, physical causal-vertex theorem, F9/G3 promotion, new physics or complete-QG claim follows.
