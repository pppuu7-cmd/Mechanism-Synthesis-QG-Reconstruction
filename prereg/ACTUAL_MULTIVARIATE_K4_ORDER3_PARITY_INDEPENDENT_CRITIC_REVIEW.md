# Prospective preregistration — independent Critic review of actual K4 order-3 parity

Date: 2026-09-15

## Scope and dependency

This Critic gate is frozen before any Critic implementation/production and reviews only the Researcher result `K4_ACTUAL_ORDER3_POLAR_COEFFICIENT_ZERO_EXACT_BY_FULL_NORMAL_INVERSION_PARITY_SCOPED` from authoritative run `34994467079`, artifact `10407455156`.

It does not compute K5 order 8, does not infer K4 from K3, and does not select a finite part or physical extension.

## Frozen acceptance criteria

The Critic must independently establish all of the following from repository authority and/or exact recomputation rather than trusting Researcher verdict booleans:

1. Provenance: authoritative Researcher run/artifact/digests and preregistration precede implementation/production; historical invalid runs are quarantined.
2. Geometry: each K4 collision has real normal dimension 9, resolved front dimension 8, and exact barycentric Gram determinant 64 in the confirmed Cartesian chart.
3. Inversion symmetry: simultaneous normal inversion `X -> -X` preserves the Gram form, positive front measure, and the complete antipodal front domain; no hidden orientation/sign convention breaks the pairing.
4. Source degree: the six K4-internal pole-removed leading source Toller matrix factors contribute exactly baseline Cartesian normal degree 6, with no omitted degree-zero or nonanalytic leading term that invalidates the parity count.
5. Order-three completeness: independently enumerate all weak degree-3 partitions over the frozen analytic jet slots and obtain exactly 364; every complete contribution has total homogeneous normal degree 9.
6. Analytic-jet legitimacy: all remaining internal/external Toller, Haar/Jacobian, q_B pullback, contraction and branch-normalization factors used by the coefficient are analytic jets in the one independently confirmed source-faithful cubic realization; no commuting-BCH, frozen-ray, scalar/Hodge or representative-component surrogate is substituted.
7. Full source contraction: all five K4 blocks and all 32 frozen boundary components are retained using the authoritative Iter077I source-order contraction algebra; edge census must be six internal plus four external wedges for every K4 block.
8. Transport: exact S5 transport across all five K4 blocks is compatible with the parity statement and does not introduce an orientation-dependent exception.
9. Residue implication: under the frozen normal-crossing convention, odd full front integrand implies exact zero of the simple K4 face residue. The Critic must distinguish this from a statement about finite parts, other Laurent coefficients, conditional/PV values, or a physical amplitude.
10. Scheme statement: zero of the simple residue is stable under allowed holomorphic defining-function changes `q'_B=exp(phi_B) q_B`; this must not be promoted to a unique finite-part/extension theorem.

## Frozen adversarial controls

The same validator/recomputation path must reject or flag at least these malformed variants: wrong normal dimension; non-antipodal front domain; inversion-odd measure insertion; one internal leading factor changed to degree zero; omitted internal wedge; incomplete degree-3 partition family; representative boundary component only; one K4 block only; commuting-BCH/scalar surrogate; post-hoc finite-part subtraction; preferred sequential continuation; replacement of published spectral `i epsilon` by `beta+i*epsilon`.

A synthetic internally consistent positive fixture must pass the same structural validator so that a blocked/fail verdict cannot be produced by literal false initialization or an impossible validator.

## Frozen terminal classifications

- `K4_ACTUAL_ORDER3_PARITY_CRITIC_CONFIRMED_SCOPED`: all acceptance criteria pass and all controls behave as frozen.
- `SCIENTIFIC_FAIL_SCOPED`: valid implementation demonstrates a substantive failure of the Researcher parity theorem.
- `INVALID_IMPLEMENTATION`: validator/recomputation/control logic is circular, incomplete, brittle, or otherwise invalid.
- `INVALID_PROVENANCE`: authority/order/digest requirements fail.
- `BLOCKED`: required authoritative material cannot be accessed or independently evaluated.

No criteria may be changed after viewing Critic production results. K5 order eight remains dependency-locked until a terminal valid Critic classification.