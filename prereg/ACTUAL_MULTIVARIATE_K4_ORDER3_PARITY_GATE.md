# Preregistration — actual multivariate K4 order-3 full-coefficient parity gate

Date: 2026-09-15
Status: **PROSPECTIVELY FROZEN BEFORE K4 COEFFICIENT COMPUTATION**

## HYPOTHESIS

For the independently confirmed source-faithful K4 cubic realization, the actual normal-order-3 coefficient multiplying the simple K4 face pole is identically zero in every one of the five K4 blocks and all 32 frozen all-`j=1/2` boundary components, because every complete contribution to that coefficient is homogeneous of odd total K4 normal degree 9 and the resolved K4 front pairing is invariant under simultaneous normal inversion.

This is a prospectively falsifiable zero prediction. Any exact surviving even contribution or any source-authoritative failure of the inversion argument is a scientific FAIL/BLOCKED outcome under the taxonomy below; the target will not be changed post-result.

## EXACT OBJECT

The object is the K4-face coefficient of the confirmed 16-parameter source family

`U(lambda)=[product_(B in D) q_B^(lambda_B/2)] A_source`

at the physical regulator origin, with the K4 face form `L_C(lambda)=0`, extracted in the normal-crossing sense frozen by `prereg/ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR.md`.

For each K4 block `C`:

- retain all six internal source Toller factors;
- retain all four external smooth Toller factors as full `2x2` matrix jets;
- retain the complete 32-component boundary contraction;
- retain the exact source Haar/Jacobian pullback;
- retain all 16 `q_B` defining-function jets and the confirmed source branch/sign normalization with published one-wedge spectral `i epsilon`;
- use the one common source-faithful cubic normal chart confirmed by the K4 bridge.

No scalar K4 surrogate, frozen angular ray, representative boundary component, commuting-BCH replacement, or one-parameter regulator is admissible.

## DEPENDENCY

Required upstream authority:

1. independently confirmed joint 16-parameter source-faithful K5 meromorphic bridge;
2. independently confirmed K3 actual residue zero, used only as provenance/control and **not** as a proof for K4;
3. Researcher K4 cubic-realization bridge result from run `34976334040`;
4. independent Critic repair-3 confirmation run `34993531171`, job `104463943299`, artifact `10406716330`, ZIP digest `sha256:6ef541cf9190907ac776099d08a16ea3a542167afe05b11d209b9e4e0d35c736`, classification `K4_CUBIC_REALIZATION_BRIDGE_CRITIC_CONFIRMED_SCOPED`.

Historical Critic runs `34985145895`, `34993299842`, `34993403191` remain `INVALID_IMPLEMENTATION` and have no scientific authority.

## SOURCE AUTHORITY

- exact source order: one-wedge spectral/spinor integration -> Toller function -> ten-factor source product -> full 32-component boundary contraction -> K5 group/distributional object;
- `distributional/iter077i_sm_source_ordered_jhalf_k5_l1.py` and corrected Iter077I authority for the full boundary contraction and source incidence;
- `sources/K4_ORDER3_SOURCE_FAITHFUL_CUBIC_REALIZATION_BRIDGE_DERIVATION.md` for the exact full-matrix reconstruction and common cubic chart;
- exact full spin-half reconstruction
  `T=t0(h+h^{-dagger})/[2 cosh(beta/2)] + t3(h-h^{-dagger})/[2 sinh(beta/2)]`;
- exact block defining functions `q_B` with `q=2s-s^2/3+4s^3/45+O(s^4)`;
- original Haar measure, source causal branch/sign conventions, and published spectral `i epsilon`.

## FROZEN INPUTS

- sector: all source spins `j=1/2`;
- boundary basis: all 32 frozen intertwiner components, no post-hoc state choice;
- K4 blocks: all five 4-subsets of `{0,1,2,3,4}`;
- K4 cumulative real normal dimension: 9;
- K4 pole-producing normal Taylor order: `omega_4=3`;
- six internal and four external source wedges per K4 block;
- all 16 divergent-block regulator variables retained;
- exact branch/sign normalization and published one-wedge spectral `i epsilon` retained;
- exact arithmetic/symbolic combinatorics only for the promoted verdict; no floating-point fit;
- no new regulator, quadrature, finite part, subtraction scale, or fitted coefficient.

## ANALYTIC OBLIGATIONS

P0. Verify the authoritative bridge and Critic hashes/classifications before coefficient work.

P1. For each K4 block, construct the 9-dimensional barycentric normal linear space and verify simultaneous inversion `X -> -X` preserves the leading front Gram form and orientation measure.

P2. Verify every internal source Toller matrix entry has pole-removed leading normal degree exactly 1 in the physical full-matrix source expansion. Six internal factors therefore contribute baseline degree 6.

P3. Enumerate every degree partition of the additional order 3 among:
- six internal Toller regular jets;
- four external Toller jets;
- Haar/Jacobian jet;
- smooth `q_B` factors / defining-function pullbacks;
- full boundary contraction algebra.
For every contribution verify the total Cartesian K4 normal degree is exactly `6+3=9`.

P4. Verify all factors entering the coefficient are analytic Cartesian jets in the same confirmed K4 chart, so simultaneous inversion multiplies every homogeneous degree-9 term by `-1`; no absolute-value, branch, frozen-ray, or nonanalytic surrogate may enter.

P5. Verify the resolved K4 front angular domain and leading pairing measure are invariant under simultaneous inversion. Then integrate/pair the full degree-9 coefficient exactly by inversion and obtain zero.

P6. Execute P1-P5 for all 5 K4 blocks and all 32 boundary components, and verify all 120 S5 transports.

P7. Establish the K4 supported residue itself is zero. Consequently the actual K4 annihilator is the full test-function space for this residue (stronger than the generic ceiling `I_K4^4`) and every compatible multi-residue containing this K4 face factor vanishes, subject only to the simple-face normal-crossing convention already frozen.

P8. Scheme statement: zero of a simple K4 face residue is invariant under allowed holomorphic defining-function changes `q'_B=exp(phi_B)q_B` because the residue transforms only by the nonzero zeroth-order factor at the face. Do not claim all Laurent coefficients or finite parts scheme invariant.

## POSITIVE CONTROLS

1. A synthetic six-internal-factor analytic jet with baseline degree 6 and a generic homogeneous degree-3 correction must be classified odd and integrate to zero on an inversion-symmetric 8-sphere/front.
2. Exact 9D normal inversion must preserve the K4 leading Gram form.
3. Exact enumeration must return five K4 blocks, six internal/four external wedges each, 32 boundary components and 120 S5 transports.

## NEGATIVE CONTROLS

The same validator must reject at least:

1. representative boundary component only;
2. scalar K4 surrogate;
3. frozen angular ray;
4. commuting BCH replacement;
5. omission of external jets;
6. flat-Haar replacement;
7. omission of `q_B` jets;
8. one-parameter regulator specialization;
9. `beta -> beta+i epsilon` group-normal surrogate;
10. inference `K4=0` merely from the already-known K3 zero;
11. a deliberately inserted degree-8 even contamination mislabelled as order 3;
12. an inversion-asymmetric angular domain;
13. hard-coded acceptance booleans in place of computed degree/parity certificates.

## PASS

If P0-P8 and all controls pass exactly:

Classification:
`K4_ACTUAL_ORDER3_POLAR_COEFFICIENT_ZERO_EXACT_BY_FULL_NORMAL_INVERSION_PARITY_SCOPED`

Verdict: `PASS_EXACT_SCOPED`.

## FAIL

If the source-faithful full coefficient contains an exact nonzero inversion-even contribution at the pole-producing order, or an exact full angular pairing is nonzero:

Classification:
`K4_ACTUAL_ORDER3_PARITY_ZERO_PREDICTION_FALSE_EXACT_SCOPED`

Verdict: `FAIL_EXACT_SCOPED`.

The nonzero coefficient/tensor must then be retained for a subsequent annihilator computation; no rescue or coefficient deletion is permitted.

## BLOCKED

If the independently confirmed cubic bridge still does not mechanically determine a required full coefficient factor/pairing operation without adding new source data:

Classification:
`K4_ACTUAL_ORDER3_FULL_COEFFICIENT_EXTRACTION_BLOCKED_SCOPED`

Verdict: `BLOCKED_OBJECT_DEFINITION` or `BLOCKED_EXACT_COMPUTATION`, according to the demonstrated obstruction.

## INVALID

Broken provenance, incomplete full-32 enumeration, hard-coded verdict booleans, malformed-control nonexecution, source-order violation, or implementation failure => `INVALID_IMPLEMENTATION`; no scientific verdict.

## INTERPRETATION CEILING

A PASS establishes only the zero of the actual K4 order-3 simple-face polar coefficient in the frozen all-`j=1/2` local common-collision sector and its immediate scheme-stable residue consequences. It does not compute K5 order 8, choose a finite part, remove the full 377-dimensional extension-selection freedom, prove the complete K5 amplitude finite/unique, establish regulator independence, global patching, E3/E4/E6, G3/F9/G8/K5, RG/continuum/spin-2/Einstein/matter/prediction, `NEW_PHYSICS_FOUND`, or complete quantum gravity.
