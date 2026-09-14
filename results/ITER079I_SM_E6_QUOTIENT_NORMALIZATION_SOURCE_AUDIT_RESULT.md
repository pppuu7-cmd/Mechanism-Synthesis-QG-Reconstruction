# Iter079I-SM — E6 quotient normalization source audit

## Authoritative production provenance

- Prospective preregistration: `c08341037dce72022351fd93b060300fb322d634`
- Implementation: `fe52943e31bda7c667379d535e8bd9f2fe089a5d`
- Production head: `141fc3a113a91676ad67b4772c8881224d49b66d`
- Workflow run: `34808310776`
- Raw artifacts: A `10334036764`, B `10333907428`, C `10333518403`, D `10333194752`
- Aggregate artifact: `10333912424`
- Aggregate digest: `sha256:df611a8c0d2abe3ee8ac9abd4288118648a928c70170107d980c1c846a465421`

## Frozen classification

`ITER079I_SM_E6_ORBIT_STRUCTURE_KNOWN_BUT_QUOTIENT_FIXING_NORMALIZATION_SOURCE_BRIDGE_MISSING_OBJECT_DEFINITION_BLOCKED_EXACT_SCOPED`

This is a scientific/object-definition blocker, not an infrastructure or numerical failure.

## Exact findings

1. The Iter079F one-vertex common-left redundancy and Iter079H minimal two-vertex orbit structure are terminal prerequisites and remain intact.
2. The frozen source matrix does **not** supply the full E6 bridge required for the composed causal object:
   - no explicit statement of which local `SL(2,C)` integration is removed or fixed;
   - no explicit quotient/fixing measure;
   - no explicit normalization convention;
   - no proof that a proposed E6 quotient is compatible with KKL gluing;
   - no generalized causal-Toller validity proof for such an E6 prescription;
   - no causal-vertex finiteness theorem that could silently determine the normalization.
3. The exact normalization control remains nontrivial: constant rescaling of an otherwise gauge-invariant reduced measure changes the frozen witness amplitude (`7 -> 14`) while preserving gauge invariance. Gauge invariance therefore does not select normalization by itself.

## Scope locks

- Do not divide informally by an infinite group volume.
- Do not insert an arbitrary Haar, Faddeev-Popov, or other quotient normalization.
- Do not promote E7/E8, finiteness, G3, F9, G8, or K5.
- This result does not invalidate the established orbit structure; it identifies the still-missing source-defined E6 quotient/fixing object.

## Consequence

The E6 frontier is now separated cleanly into two layers: the redundant orbit structure is known, while the physical quotient/fixing measure and normalization remain undefined by the current authority set. A subsequent gate may sharpen multi-vertex orbit counting algebraically, but a physical E6 closure still requires a source-derived quotient prescription.