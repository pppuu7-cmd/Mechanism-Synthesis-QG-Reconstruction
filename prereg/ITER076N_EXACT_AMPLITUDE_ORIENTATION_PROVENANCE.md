# Iter076N preregistration — exact amplitude orientation provenance

**Date:** 2026-09-14
**Scope:** SOURCE_NATIVE / EXACT_AMPLITUDE_ONLY

## Question

Does the exact causal-spinfoam source object, at the level of Eq. (4), Eq. (7), magnetic/intertwiner contractions and source-defined label/orientation data, exhibit or uniquely force an orientation-odd pseudoscalar capable of selecting the `+H/-H` Hodge lift?

The previously constructed `Omega_sigma(g)` is admissible as a diagnostic because it is a function of exact source variables, but **mere constructibility is not provenance**. Iter076N passes the physical signed-P3 prerequisite only if the source amplitude itself supplies an equivalent alternating selector or a derivation that uniquely forces it.

## Frozen source facts

1. Fixed-causal vertex Eq. (4) uses ten Toller factors with branch labels `kappa_ab=sigma_a sigma_b` and arguments `g_b^{-1}g_a`.
2. Global `sigma_a -> -sigma_a` leaves every `kappa_ab` unchanged.
3. Eq. (7) is a wedge-local Cartan/magnetic decomposition of each Toller matrix.
4. The source states that the combinatorial/Regge relation arises at semiclassical level; the large-spin analysis selects compatible Lorentzian Regge saddles.
5. The source explicitly says that the relation to the proper vertex, where a 4-volume-orientation constraint selects one critical point, remains to be clarified.

## Lanes

### Lane A — causal-data factorization audit
Enumerate all `sigma in {+1,-1}^5`, compute the ten `kappa_ab`, and verify:
- exactly 16 branch patterns modulo global reversal;
- Eq. (4)'s causal branch data are functions of `kappa` only;
- no vertex-global sign bit survives in the source branch labels.

### Lane B — exact relabeling-character audit
Represent Eq. (4)'s source-visible structure as the commutative product over the ten unordered wedges plus Haar factors. Exhaust all 120 `S5` permutations and test whether odd permutations generate an intrinsic alternating sign. A successful source-native orientation selector requires an orientation-odd character not attributable solely to an externally chosen ordering convention.

### Lane C — Eq. (7) dependency-graph audit
Audit the exact source-visible ingredients of the Cartan/magnetic representation. Record whether the source formula contains a five-normal determinant, Levi-Civita contraction, proper-vertex `beta_ab` projector, 4-volume orientation operator, or any equivalent cross-wedge antisymmetric vertex factor.

### Lane D — semiclassical firewall
Verify that source statements about causal rigidity / single `exp(+i S_Regge)` arise in the large-spin saddle analysis and that importing the proper-vertex 4-volume-orientation selector into Eq. (4) would add structure not present in the published exact definition.

## Frozen classifications

If A-D validate the source audit and no exact alternating selector is source-exhibited:

`ITER076N_EQ4_EQ7_EXACT_AMPLITUDE_HAS_NO_SOURCE_EXHIBITED_GLOBAL_ORIENTATION_SELECTOR_PROVENANCE_BLOCKED_SOURCE_NATIVE_SCOPED`

If an exact source-defined orientation-odd factor is found and survives all relabeling/gauge checks:

`ITER076N_EXACT_AMPLITUDE_ORIENTATION_SELECTOR_SOURCE_PROVENANCED_REVIEW_SIGNED_P3_SCOPED`

Otherwise:

`ITER076N_SOURCE_AUDIT_INCONCLUSIVE_REVIEW_REQUIRED_SCOPED`

## Claim locks

- Absence from the audited source formula is not a theorem that no mathematically equivalent reformulation can ever expose such a factor.
- No semiclassical selector is promoted to an exact Eq. (4) selector.
- No signed P3, F9, G3, G8 or K5 promotion is authorized by this iteration alone.
- No new physics claim.
