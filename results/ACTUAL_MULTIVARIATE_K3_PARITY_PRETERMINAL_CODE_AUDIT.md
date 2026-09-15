# Preterminal adversarial code audit — actual multivariate K3 polar parity lane

**Date:** 2026-09-15

**Status:** PRETERMINAL / NO SCIENTIFIC VERDICT.

At the time of this audit, the fresh repair-1 production run `34955160116` for `.github/workflows/actual_multivariate_polar_k3_parity_gate.yml` is non-terminal (`queued`) on head `4d45991d381930d84da2d5bf33c02d7d7050aa74`. Under the MSQGR Critic contract, no competing verdict and no substantive use of partial production values is authorized before terminal completion.

The last validated scientific authority therefore remains the independently confirmed repaired joint-K5 bridge in `status/CURRENT.md`.

## Frozen contract recovered

Parent preregistration: `prereg/ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR.md`.

The K3 lane is allowed to prove a zero residue by exact parity only if the symmetry acts on the **full K3 pole coefficient**, including the external smooth Toller factors, full 32-component boundary contraction, pulled-back Haar density and the relevant defining-function factors. The preregistration explicitly requires mechanical rejection of ten malformed constructions and states that hard-coded acceptance booleans invalidate the implementation.

The K3 theorem note `sources/ACTUAL_MULTIVARIATE_POLAR_K3_PARITY_DERIVATION.md` supplies a plausible analytic parity argument, but the production validator must still execute the frozen contract rather than merely encode its desired premises.

## Preterminal implementation findings

### 1. Several decisive scientific premises are hard-coded booleans

In `scripts/actual_multivariate_polar_k3_parity_gate.py`, the candidate is constructed with these acceptance values set directly to `True` rather than derived from the actual source coefficient:

- `external_order0_direction_independent=True`;
- `front_measure_even=True`;
- `q_radius_even=True`;
- `angular_domain_inversion_symmetric=True`;
- `k3_residue_extracted_before_outer_residues=True`;
- `defining_function_gauge_holomorphic=True`.

These values feed K3 predicates `K3_6`, `K3_7`, `K3_9`, `K3_11` and `K3_12`. Flipping such flags in a negative control only proves that the Boolean validator notices a changed flag; it does not mechanically establish the source/Haar/regulator statement represented by the flag.

This is directly relevant to the preregistered rule that hard-coded acceptance booleans invalidate the implementation.

### 2. The executed `exact_full32()` engine is a frozen-ray nonzero contraction, not the K3 front-face angular coefficient

The imported Iter077I engine `distributional/iter077i_sm_source_ordered_jhalf_k5_l1.py` freezes five explicit vectors `X[a]`, constructs ten fixed leading matrices `EDGE_MATRICES`, and evaluates the 32 boundary contractions at that single common-collision angular witness.

The K3 validator calls `mod.exact_full32()` only to obtain `full_boundary_components == 32` and a checksum. It does **not** construct the 32 contracted K3 front-face functions as functions of the six-dimensional K3 angular variable, nor does it apply the K3 inversion to those contracted functions.

Therefore `full32_components_executed == 32` is a valid boundary-count/provenance control, but it is not by itself the preregistered proof that the complete full-boundary K3 pole coefficient is odd.

### 3. External-factor and Haar parity are not actually computed

The theorem note argues that all seven external wedges have direction-independent zeroth K3-normal coefficient and that the leading pulled-back Haar density is even. The validator does not expand any external Toller factor in K3 normal coordinates, does not construct the pulled-back Haar/Jacobian coefficient, and does not verify either transformation under the inversion.

Those are exactly the ingredients the frozen Lane B/C contract requires for an exact zero certificate.

### 4. The ten implemented mutations are not the ten frozen negative controls

The parent preregistration requires mechanical rejection of at least:

1. a one-parameter `rho^z u` replacement of the 16-parameter family;
2. representative boundary component only;
3. omission of external smooth wedge factors;
4. historical nested-density tuple `(5,2,2)`;
5. a nonzero claim from one angular point without angular pairing;
6. promotion of positive representation multiplicity to source nonzero;
7. declaration that all Laurent coefficients are scheme invariant;
8. sequential finite-part ordering called the source residue;
9. omission of Haar/Jacobian factors;
10. import of the invalid Iter077Q tangential family.

The current script instead mutates:

- even internal-edge count;
- representative boundary only;
- nonintegrable K2 front;
- nonsymmetric angular domain;
- direction-dependent external order-zero flag;
- odd measure flag;
- non-even radius flag;
- wrong K3 order;
- K4/K5 overclaim flag;
- non-holomorphic scheme-change flag.

Only the representative-boundary control directly matches a frozen malformed construction. Some others are useful additional controls, but they do not execute the missing frozen controls. In particular there is no same-validator test of the one-parameter surrogate, `(5,2,2)` nested density, representation-multiplicity promotion, sequential finite part, or Iter077Q tangential import.

### 5. S5/all-K3 transport is only combinatorial

`all_k3_blocks_same_combinatorics` checks only that every K3 block has three internal edges. It does not transport the full source polar coefficient through all 120 S5 relabelings as required by Lane E. A full coefficient-level parity theorem may make this transport analytically trivial, but the current implementation does not mechanically establish it.

### 6. Initial failed run does not cure these issues

Completed run `34955091523` failed because of a bridge-provenance literal mismatch. Its log shows all K3 Boolean predicates and all ten implemented mutation controls as `true`, but the code audit above is independent of those printed values: several predicates are true because the candidate fields were assigned `True` directly, and several frozen negative controls were never instantiated.

### 7. Repair-1 scope is too narrow to fix the independent code issues

`prereg/ACTUAL_MULTIVARIATE_POLAR_K3_PARITY_CONTROL_ONLY_REPAIR_1.md`, commit `6a048a91eb668787d1227331025888d86f8fb3ed`, prospectively restricts repair 1 to changing only the bridge provenance text needle. The head `4d45991d...` obeys that narrow repair scope.

Consequently, even if the queued run becomes green, repair 1 has not prospectively authorized changes that would cure the independent frozen-contract gaps identified above. A substantive Critic verdict must wait for terminal production, but a green run alone cannot erase these pre-existing code facts.

## Scientific status of the parity idea

This preterminal audit does **not** refute the mathematical K3 parity hypothesis. The source note gives a coherent candidate proof: each of the three internal `j=1/2` leading matrices is odd under simultaneous inversion of the K3 incremental normal variables; zeroth-order external factors should be independent of that inner angular direction; K2 subfaces are locally integrable; and an even Haar/front measure would then force the angular pairing to zero.

The issue is certification. To satisfy the frozen gate, a successor implementation should construct or symbolically prove the full coefficient transformation, not encode its decisive premises as acceptance flags.

## Required repair if terminal production later claims PASS

Without changing the scientific hypothesis/object/ceiling, a prospectively frozen control-only successor should at minimum:

1. derive the zeroth K3-normal external Toller coefficient from the actual source expressions and verify inversion independence;
2. derive the pulled-back Haar/front density transformation and verify evenness;
3. evaluate the full 32-component contracted leading K3 coefficient symbolically or via an exact algebraic representation on the K3 normal variables, and verify oddness under inversion before angular pairing;
4. execute coefficient-level S5 transport, not only edge-count transport;
5. instantiate all ten frozen malformed controls through the same object/coefficient validator, including one-parameter surrogate, `(5,2,2)` density, representation-multiplicity promotion, sequential finite part, omitted Haar/Jacobian and Iter077Q tangential import;
6. keep K4/K5 conclusions unset unless separately prospectively frozen and computed.

No physical finite part, regulator-independence theorem, predictive local amplitude or downstream promotion is authorized by this note.
