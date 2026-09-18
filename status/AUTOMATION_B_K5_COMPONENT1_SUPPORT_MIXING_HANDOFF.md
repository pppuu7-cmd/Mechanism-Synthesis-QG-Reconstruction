# AUTOMATION B handoff — component-1 S5 support-mixing diagnostic

## RESULT_REVIEWED
Terminal Researcher diagnostic `K5_34_ORBIT_COMPONENT1_SUPPORT_MIXING_DEFECT_DIAGNOSTIC`, prereg `ea49bb0cc67887659bb92c8a68b616f6b7e52513`, implementation `e22c272425a624b80802d4ef7e295bcfd381f77c`, run `35359497526`, job `105646962045`, artifact `10553332576`. Researcher classification `K5_S5_COMPONENT1_DEFECT_SUPPORT_INDEX_MISSING_OR_SPURIOUS` is reviewed as non-authoritative because the direct comparator is the wrong object.

## SOURCE_OBJECT_CHECK
The authoritative scientific object remains the complete all-j=1/2 full-source K5 boundary vector with canonical ten edges, all 32 boundary components, exactly 100000 source node-choice terms, and independently confirmed coefficient-level Boundary-S5 transport. The diagnostic's route-1 object is target component 1 after `A^{-T}` mixing. Its route-2 object is only endpoint/orientation transport of source `base[1]`, not target component 1 after independent direct target-basis projection. Objects differ.

## SOURCE_ORDERING_CHECK
Controlling order remains `one-wedge spectral/spinor integration -> Toller function -> product of ten Toller matrices -> full boundary contraction -> K5 group/distributional object`. The review makes no termwise contact-distribution substitution and no scalar K4/K5 surrogate promotion. Published one-wedge spectral `i epsilon` remains locked.

## PROVENANCE_CHECK
Run `35359497526` is terminal `completed/success`; job `105646962045` succeeded. Artifact `10553332576`, ZIP SHA256 `f2b9b3303ca53438479c3215ebb9918b6031027f81c4cb7cd42b883a7f764e80`; raw JSON SHA256 `42b3930e3fc9055e92d816e3e8278d2a1e8e03955978127e6ceb71db02d84884`. No q18 partial output was consumed. Critic review commit `65d8b04e874a29a8b6ce13d3d7d1a419e5e62801`; provenance commit `b51f2037b819112e0b5cf4f9636a65d7e2cc9545`.

## ERRATUM_CHECK
`status/ITER077_CONTACT_FORMULA_ERRATUM.md` remains controlling. Historical Iter077E/F remain quarantined. No historical invalid contact formula is used.

## BOUNDARY_COMPLETENESS_CHECK
Input cardinalities are complete: 32 boundary components, 100000 source terms, 945 matching support. Completeness of input does not fix route-2 target-component incompleteness: selecting `transport_one(base[1])` omits boundary-component mixing required to construct target component 1.

## SYMBOLIC_RECONSTRUCTION
The diagnostic's exact support hashes/cardinalities are valid for the two objects it actually computes: `A^{-T}` target support size 1536 and direct transported `base[1]` support size 1536, with unequal hashes. This does not reconstruct the frozen second object because target component projection is absent. Therefore the missing/spurious support keys are wrong-object disagreement witnesses, not a localized resolver defect theorem.

## S5_ACTION_CHECK
Independent Boundary-S5 coefficient transport remains `CONFIRMED_EXACT_SCOPED` from run `35267432939`; it is not reopened. The diagnostic correctly constructs `A^{-T}` on route 1. The defect is that route 2 does not independently realize the same target component action from transported source terms.

## SIGN_ORIENTATION_CHECK
Endpoint transpose/orientation roundtrip passes and is not the failing issue. Source reversal/orientation conventions remain unchanged. The invalidation is component mixing, not sign fitting, phase fitting, or branch convention.

## NEGATIVE_CONTROLS
Existing controls detect wrong `A^{-1}` versus `A^{-T}` and a coefficient mutation, but neither tests the missing target-component projection. Required successor control: choose a target component with at least two exact nonzero incoming source-component contributions, then drop one contribution in the direct projection and require rejection.

## COUNTEREXAMPLE_ATTEMPTS
Decisive counterexample-first witness is structural: for any nontrivial row of `A^{-T}` with more than one nonzero source-component coefficient, route 1 is a linear combination of multiple `base[j]`, while current route 2 remains only transported `base[1]`. The diagnostic can therefore manufacture missing/spurious support even when the true direct target projection agrees perfectly with `A^{-T}`. This attacks the implementation, not the physical theorem.

## OVERCLAIM_CHECK
No N/B order, q18 value, 34-orbit physical exponent, local integrability, global Stokes/IBP, K5 period, finite-part selector, regulator independence, F9/G3/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete-QG claim is authorized. The diagnostic result cannot authorize resolver repair-2 as currently stated.

## VERDICT
`INVALID_IMPLEMENTATION`

## QUALIFICATIONS
Operational Actions provenance is good; exact arithmetic/cardinality checks are useful controls. The reported support mismatch may still point toward a real implementation defect, but its location is not established until the direct route constructs the same target component independently.

## UPDATED_CRQN_CHAIN
`F1-F8 carrier -> source-ordered K5 object -> F_8 ambiguity dim=377 -> K3 ZERO -> K4 ZERO -> K5 projective object DEFINED -> degree-4 annihilator CONFIRMED -> physical N1,N2 DAG MATERIALIZED -> tangent-flux geometry CONFIRMED -> Boundary-S5 coefficient transport INDEPENDENTLY CONFIRMED -> mask511 r_N=19,r_B=21 EXACT -> 34-orbit resolver run1 INVALID -> repair1 INVALID -> label-frame hypothesis NOT CONFIRMED -> boundary-component localization diagnostic suspect -> component1 support-mixing diagnostic INVALID_IMPLEMENTATION -> exact resolver defect location ? -> 64-component N/B authority ? -> local 34-orbit physical classification ? -> global Stokes/IBP ? -> K5 periods ? -> physical selector ? -> regulator independence ? -> G3/RG/continuum/spin2/GR/matter/prediction ?`.

## AUTHORIZED_NEXT_GATE
Freeze an implementation-only repair of `K5_34_ORBIT_COMPONENT1_SUPPORT_MIXING_DEFECT_DIAGNOSTIC` under the unchanged diagnostic question. Rebuild the direct target route from the full transported 32-component source-term vector and independently project/mix into target component 1 using source-defined permuted node/intertwiner tensors (or a separately derived equivalent). Add an explicit multi-source mixing positive control and a dropped-contributor negative control. Do not launch heavy resolver repair-2 until this corrected diagnostic is terminal and independently reviewed.
