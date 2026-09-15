# Preregistration — actual source-ordered multivariate polar normal-jet / annihilator gate

Date: 2026-09-15
Status: **PROSPECTIVELY FROZEN BEFORE POLAR-COEFFICIENT COMPUTATION**

## Authoritative dependency

This gate is downstream of the scientifically repaired and independently confirmed source-faithful joint K5 bridge:

- parent bridge preregistration `4151c02452edd3e5e2c49952686e42e64c6dc180`;
- nested-Jacobian repair preregistration `148dd5130c448420419a807826fdfd84bb1228ef`;
- repaired Researcher result `results/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_NESTED_JACOBIAN_REPAIR_RESULT.md`, commit `457107f45513facf8911d3001610a362f9d924b8`;
- repaired independent Critic `results/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_ADVERSARIAL_REVIEW_REPAIR2.md`, commit `9efc5d227afc3cff187d386a5574e2ae010cc7d9`;
- authoritative production run `34954021547`, job `104331589295`, artifact `10390666862`, JSON SHA256 `079587747eb747e067400b88a3969982a495c17eee9150543cdede856d883acd`.

The bridge supplies the actual frozen local all-`j=1/2`, full-32-boundary, source-ordered family

`U(lambda)=[product_(B in D) q_B^(lambda_B/2)] A_source`,

with 16 divergent-block parameters and face forms

`L_C(lambda)=sum_(B subseteq C, |B|>=3) lambda_B`.

It does not supply a finite part or one-parameter specialization.

## Scientific question

For the actual source family, which polar coefficients at the physical regulator origin are nonzero, what supported normal-jet orders/tensor channels do they occupy, what test-function ideals do they annihilate, and which conclusions are invariant under allowed changes of the nonlinear collision defining functions?

The gate must distinguish **allowed pole order** from an **actual nonzero source polar coefficient**.

## Frozen geometry

On a maximal chain `K3 subset K4 subset K5`, the corrected local form is

`U(lambda) ~ rho3^(L_K3-1) rho4^(L_K4-4) rho5^(L_K5-9) A(rho,Omega,lambda)`.

Thus the only Taylor orders that can generate poles through the physical point are

- K3: `omega_3=0`;
- K4: `omega_4=3`;
- K5: `omega_5=8`.

These are candidate source polar normal orders, not frozen nonzero outcomes.

## Polar-coordinate convention

The primary regulator variables for this gate are the 16 face forms `L_C`, not an arbitrary one-parameter direction.

The face-residue operation is defined as coefficient extraction in the normal-crossing Laurent expansion with respect to these independent linear forms.

For a compatible nested set `F={C1,...,Cr}`, define the **top multi-residue**

`Res_F U := coefficient of product_(C in F) L_C^(-1)`

with all remaining regulator variables retained symbolically/meromorphically until the specified extraction is complete.

No sequential finite part or chosen one-dimensional ray through regulator space is part of the object.

## Lane A — provenance/object lock

A1. Consume the repaired bridge family and corrected nested Haar powers `(5,8,11)`, source powers `(-6,-12,-20)`, combined exponents `(-1,-4,-9)` and invertible 16-by-16 incidence map.

A2. Retain the source order

`one-wedge construction -> Toller functions -> ten-factor product -> full 32-component boundary contraction -> group/distributional object`.

A3. Reuse the exact Iter077I full-32 boundary contraction algebra where applicable; no representative boundary component is accepted.

## Lane B — actual front-face coefficient extraction

For one canonical representative of each S5 orbit of divergent faces/chains, construct local symmetric-space normal coordinates and expand the **actual source object**, including:

- all singular internal Toller factors;
- all external smooth Toller factors;
- compact/angular matrix factors;
- full boundary contraction;
- exact pulled-back Haar density;
- smooth positive factors from the chosen `q_B` defining functions.

Extract exactly the coefficient that multiplies the pole at the physical point:

- K3 face: normal Taylor order 0;
- K4 face: normal Taylor order 3;
- K5 face: normal Taylor order 8.

For a maximal chain, also extract the coefficient of the highest product pole

`1/(L_K3 L_K4 L_K5)`.

A mere nonzero angular witness at one point is insufficient to prove a nonzero residue: the required front-face angular pairing/integration or an exact equivalent symmetry/representation calculation must be performed.

## Lane C — nonzero/zero certification

For every tested face/channel, classify the actual polar coefficient as one of:

- `NONZERO_EXACT` — exact symbolic/representation-theoretic certificate;
- `ZERO_EXACT` — exact symmetry/cancellation certificate;
- `NUMERIC_EVIDENCE_ONLY` — exploratory, never promotable to an exact PASS;
- `BLOCKED_COEFFICIENT_EXTRACTION` — source/tensor/angular data insufficient.

If a coefficient is claimed nonzero, at least one exact test tensor/polynomial pairing must be nonzero after the required angular operation.

If zero is claimed by parity or representation symmetry, the symmetry must act on the **full coefficient including external smooth factors and Haar density at the relevant Taylor order**, not just on the leading internal wedge product.

## Lane D — supported normal-jet / annihilator classification

For every exact nonzero face residue of normal order `omega_C`, identify the corresponding supported distributional order and prove its test-function annihilator contains

`I_C^(omega_C+1)`.

Determine whether the annihilator is exactly that ideal or strictly larger due symmetry/tensor cancellation.

Candidate ceilings are therefore

- K3: `I_K3^1`;
- K4: `I_K4^4`;
- K5: `I_K5^9`.

These are ceilings only; exact annihilators must be computed from the actual polar tensors.

## Lane E — S5 / boundary covariance

E1. Transport canonical face results through all 120 S5 relabelings and verify exact class consistency.

E2. Keep the true 32-dimensional boundary intertwiner fiber. Any reduction must be proved as an exact intertwiner/restriction theorem.

E3. Compare actual polar channels with the authoritative boundary-covariant graded multiplicities where the corresponding stratum representation is available. Do not infer nonzero source coefficients from positive representation multiplicity alone.

## Lane F — defining-function scheme covariance

Allowed local changes have the form

`q'_B=exp(phi_B)q_B`,

so

`U'(lambda)=H(lambda)U(lambda)`,

`H(lambda)=exp[(1/2)sum_B lambda_B phi_B]`, `H(0)=1`.

F1. Prove mechanically/algebraically that the coefficient of the **maximal product pole** for a fixed compatible nested set is invariant under multiplication by such a holomorphic `H` when all participating face poles are simple.

F2. Explicitly demonstrate that lower-codimension/lower Laurent coefficients can mix under the same transformation whenever a higher product pole is present.

F3. Label every reported polar datum as `SCHEME_INVARIANT`, `SCHEME_COVARIANT`, or `Q_B_SCHEME_ONLY`.

No regulator-independence claim may be made for data failing F1.

## Lane G — negative controls

The implementation must mechanically reject at least:

1. replacing the 16-parameter family by a one-parameter `rho^z u` family;
2. using only a representative boundary component;
3. omitting external smooth wedge factors from the residue coefficient;
4. using the old nested-density tuple `(5,2,2)`;
5. declaring a nonzero residue from one angular point without angular pairing;
6. promoting a positive representation multiplicity to source nonzero without coefficient extraction;
7. declaring all Laurent coefficients scheme invariant;
8. choosing a sequential finite-part order and calling it the source residue;
9. dropping Haar/Jacobian factors;
10. importing the old invalid Iter077Q tangential function family.

Hard-coded acceptance booleans invalidate the implementation.

## Frozen scientific outcomes

### Outcome P — actual polar data classified

If the actual source polar coefficients are exactly extracted for all required K3/K4/K5 face orbits, transported covariantly, and their scheme status/annihilators are established:

Classification:

`ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR_CLASSIFIED_SCOPED`

Verdict: `PASS_EXACT_SCOPED`.

The result may contain exact zero coefficients. PASS means classification is complete, not that every candidate residue is nonzero.

### Outcome B — coefficient extraction remains incomplete

If the bridge exists but exact angular/tensor coefficient extraction cannot be completed from the authoritative object:

Classification:

`ACTUAL_MULTIVARIATE_POLAR_COEFFICIENT_EXTRACTION_BLOCKED_SCOPED`

Verdict: `BLOCKED_OBJECT_DEFINITION` or `BLOCKED_EXACT_COMPUTATION`, whichever is appropriate to the identified failure.

### Outcome F — frozen source prediction falsified

If a prospectively frozen nonzero/zero prediction is contradicted by an exact implementation, return `FAIL_EXACT_SCOPED` rather than changing the target.

Implementation defects remain `INVALID_IMPLEMENTATION` and are not scientific outcomes.

## Interpretation ceiling

Even a PASS does not choose a holomorphic finite part, subtraction constants or a physical extension. It does not prove regulator independence of the causal vertex, global multistratum patching, generic-spin completeness, causal multivertex closure, G3/F9/G8/K5 promotion, RG/continuum/spin-2/GR/matter/prediction results, `NEW_PHYSICS_FOUND`, or complete quantum gravity.

The purpose of this gate is to replace formal `A_-1` language by actual source polar tensors and exact scheme-aware normal-jet information.