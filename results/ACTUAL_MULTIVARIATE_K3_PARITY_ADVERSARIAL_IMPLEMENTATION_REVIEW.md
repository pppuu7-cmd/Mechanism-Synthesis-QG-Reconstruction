# Adversarial implementation review — actual multivariate K3 polar parity lane

**Date:** 2026-09-15

## Reviewed terminal production

Gate: `ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR_K3_LANE`.

Parent preregistration:

- `prereg/ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR.md`, scientific prereg commit `4c4478db20e08387fb7067a55d773fce31d3fc34`.

K3 derivation:

- `sources/ACTUAL_MULTIVARIATE_POLAR_K3_PARITY_DERIVATION.md`, commit `78e63844a8fe0a70af9ac8dc574d358e7ecab927`.

Initial implementation / workflow:

- implementation `c8ddedab0530cb08b17aea08299c1e45a1897d30`;
- workflow/head `7f15c4f4188990f2bd7b0c08329fb46345da43cd`;
- initial run `34955091523`, job `104335105619`, terminal failure with no artifact because of a bridge-provenance literal mismatch.

Control-only repair 1:

- repair prereg `6a048a91eb668787d1227331025888d86f8fb3ed`;
- repaired head `4d45991d381930d84da2d5bf33c02d7d7050aa74`.

Fresh repaired production:

- run `34955160116`, terminal success;
- job `104335856061`, terminal success;
- artifact `10390188871`;
- artifact ZIP digest `sha256:e519d0b2c01327532ba5ad4024cd4791efe390b447f1ad5f705ca0af31794b83`;
- aggregate JSON SHA256 `537c477b1bf2207a2935814dca6cffa532a0581dc539247653b4fe47176cddf9`.

The artifact was independently downloaded. Its ZIP SHA256 is exactly `e519d0b2c01327532ba5ad4024cd4791efe390b447f1ad5f705ca0af31794b83`; both the uploaded stdout JSON and `results/raw/actual_multivariate_polar_k3_parity_gate.json` hash to `537c477b1bf2207a2935814dca6cffa532a0581dc539247653b4fe47176cddf9`.

Production classification:

`K3_PHYSICAL_ORIGIN_POLAR_COEFFICIENT_ZERO_EXACT_BY_NORMAL_INVERSION_PARITY`

Production verdict:

`PASS_EXACT_SCOPED`.

## Frozen-contract comparison

The parent preregistration requires the K3 zero certificate to act on the **full actual pole coefficient**, including the internal singular Toller factors, all external smooth Toller factors, compact/angular matrix factors, full 32-component boundary contraction, pulled-back Haar density and the relevant defining-function factors. A zero by parity is permitted only if the inversion symmetry is established on that complete coefficient. The same preregistration also states explicitly: **hard-coded acceptance booleans invalidate the implementation**.

The production script does not satisfy that requirement.

## Implementation witness 1 — decisive premises are hard-coded acceptance booleans

The candidate object in `scripts/actual_multivariate_polar_k3_parity_gate.py` assigns these fields directly:

```python
"external_order0_direction_independent": True,
"front_measure_even": True,
"q_radius_even": True,
"angular_domain_inversion_symmetric": True,
"k3_residue_extracted_before_outer_residues": True,
"defining_function_gauge_holomorphic": True,
```

Those booleans feed the scientific predicates

- `K3_6_external_order0_direction_independent`;
- `K3_7_even_measure_radius`;
- `K3_9_angular_pairing_zero`;
- `K3_11_nested_multiresidue_zero`;
- `K3_12_scheme_invariant_zero`.

No source/Toller/Haar/regulator expression is passed through a validator to derive these facts. The negative controls merely flip the same flags and verify that a Boolean predicate changes. Thus the code can return the production PASS even though the decisive external-factor, Haar and nested-residue statements were never computed.

This is a direct frozen-contract violation, not a matter of interpretation.

## Implementation witness 2 — `exact_full32()` is a fixed-ray witness, not the K3 front coefficient

The imported Iter077I engine freezes explicit node vectors

`X_0=(0,0,0)`, `X_1=(1,2,3)`, `X_2=(2,3,5)`, `X_3=(3,5,7)`, `X_4=(5,7,11)`

and constructs ten fixed leading matrices `EDGE_MATRICES` at that one common-collision angular witness.

`exact_full32()` then contracts those fixed matrices against the 32 all-`j=1/2` boundary basis components. This is authoritative for the historical nonzero frozen-ray certificate and for checking that all 32 components are represented.

The K3 production calls `exact_full32()` only to obtain `full_boundary_components == 32` and a checksum. It does **not** construct the 32 contracted K3 front-face functions as functions of the six-dimensional K3 angular variable, and it does not apply the K3 inversion to those full contracted functions.

Therefore `full32_components_executed == 32` does not mechanically prove the preregistered full-boundary parity theorem.

## Implementation witness 3 — external smooth factors and Haar density are never expanded

The scientific derivation argues that, at K3 normal order zero, all seven external wedges are independent of the inner K3 angular direction and the pulled-back Haar/front density is even under inversion. Those statements are plausible, but the implementation does not derive them.

There is no construction of:

- the zeroth K3-normal Taylor coefficient of the seven external Toller factors;
- the pulled-back Haar/Jacobian leading coefficient on the K3 front;
- their exact transformation under `Omega_B -> -Omega_B`.

The production `PASS` therefore promotes prose premises to mechanical predicates without executing the frozen Lane B/C object.

## Implementation witness 4 — the ten production mutations do not implement the ten frozen negative controls

The parent preregistration requires the same implementation machinery to reject at least:

1. one-parameter `rho^z u` replacement of the 16-parameter family;
2. representative boundary component only;
3. omission of external smooth wedge factors;
4. historical nested-density tuple `(5,2,2)`;
5. nonzero residue from one angular point without angular pairing;
6. promotion of positive representation multiplicity to source nonzero;
7. declaration that all Laurent coefficients are scheme invariant;
8. sequential finite-part ordering called the source residue;
9. omission of Haar/Jacobian factors;
10. import of the invalid Iter077Q tangential family.

The production instead mutates:

- even internal-edge count;
- representative boundary only;
- nonintegrable K2 front;
- nonsymmetric angular domain;
- direction-dependent external-order-zero flag;
- odd-measure flag;
- non-even-radius flag;
- wrong K3 order;
- K4/K5 overclaim flag;
- non-holomorphic scheme-change flag.

The representative-boundary mutation directly matches one frozen malformed construction. Several other mutations are useful additional controls, but they do not instantiate the missing frozen cases. In particular there is no executed malformed object for the one-parameter surrogate, `(5,2,2)` nested density, representation-multiplicity promotion, sequential finite part, or Iter077Q tangential import.

Production's statement `all ten malformed controls true` therefore does not mean the ten **frozen** malformed controls were executed.

## Implementation witness 5 — S5 transport is reduced to edge-count combinatorics

`all_k3_blocks_same_combinatorics` checks only that each K3 block contains exactly three internal K5 edges. It does not transport the actual polar tensor/coefficient through all 120 S5 relabelings as required by Lane E.

If the full analytic parity theorem is proved, the S5 extension may indeed follow. But the current machine check does not establish it at coefficient level.

## Provenance audit

The repair chronology itself is valid. The original scientific preregistration predates theorem/implementation. Repair-1 preregistration `6a048a91...` predates the one-line provenance repair `4d45991...`. The fresh production checks out exactly `4d45991...`, terminates successfully and uploads a matching artifact.

No `INVALID_PROVENANCE` finding is made.

However repair-1's frozen scope explicitly permits changing **only** the bridge provenance text needle. It does not authorize alteration of the scientific predicates or malformed controls. Thus the fresh run can cure the literal provenance mismatch but cannot prospectively cure the independent implementation deficiencies above.

## Scientific counterexample status

No exact counterexample to the underlying K3 parity hypothesis was found in this review.

The analytic idea remains plausible in the frozen all-`j=1/2` local sector:

- each of the three internal leading Toller matrices is odd under simultaneous inversion of the incremental K3 normal variables;
- the K3 candidate pole uses order-zero normal Taylor data;
- external factors should collapse to direction-independent zeroth coefficients;
- the symmetric-space/Haar leading density should be even;
- internal K2 subfaces have radial exponent 0 and are locally integrable.

If all those facts are established on the **full contracted coefficient**, the parity cancellation would be a valid exact zero certificate. The present review rejects the implementation, not that mathematical possibility.

## Verdict

`INVALID_IMPLEMENTATION`

The terminal green workflow is not scientific authority for the claimed K3 zero because decisive source/Haar/parity premises are hard-coded and several prospectively frozen controls are unexecuted.

The production result must not be used downstream as proof that `Res_(L_K3=0) U = 0`, that every multiresidue containing K3 vanishes, or that the K3 annihilator is the whole test-function space.

## Required prospectively frozen control-only successor

Because repair 1 prospectively allowed only the provenance-needle change, any broader implementation correction requires a new control-only repair preregistration before code changes.

Without changing the parent scientific hypothesis/object/PASS-FAIL ceiling, that successor should:

1. symbolically construct or independently prove the complete K3 order-zero coefficient, including the seven external Toller factors and pulled-back Haar/front density;
2. verify the full 32-component contracted coefficient is odd under K3 inversion, not merely count 32 fixed-ray components;
3. execute coefficient-level transport over the S5 orbit;
4. derive the nested-residue and defining-function-gauge claims algebraically rather than by acceptance flags;
5. instantiate all ten frozen malformed controls through the same object/coefficient validator;
6. retain K4/K5 as unresolved unless separately prospectively computed.

Until that repair obtains terminal production and independent review, the authoritative CRQN chain remains at the confirmed joint-K5 meromorphic bridge, with actual K3/K4/K5 polar normal-jet coefficients unresolved.
