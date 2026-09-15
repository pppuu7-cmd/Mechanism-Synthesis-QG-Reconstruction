# Prospective preregistration — K4 order-3 source-faithful cubic realization bridge

Date: 2026-09-15
Role: AUTOMATION A / MSQGR Researcher-Constructor

Status: **FROZEN BEFORE BRIDGE DERIVATION / IMPLEMENTATION / PRODUCTION OUTPUT**

## HYPOTHESIS

Current independently confirmed source authority may already contain enough exact ingredients to construct, without a scalar surrogate or post-hoc choice, a single mutually compatible cubic jet realization of the frozen all-`j=1/2` source-ordered multivariate meromorphic K5 germ near every K4 face. The decisive question is whether the missing K4 reachability requirements `R3_TOLLER_ORDER3`, `R4_EXTERNAL_TOLLER_JETS`, and `R6_Q_DEFINING_FUNCTION_ORDER3` can be derived from exact source functions and the already-authoritative K4 normal/BCH/Haar/front geometry rather than inserted as new phenomenological data.

No PASS or BLOCKED outcome is assumed.

## exact OBJECT

The object is **not** the K4 residue coefficient itself. It is the source-faithful cubic realization map needed before that coefficient can be computed:

`J_K4^3 := J^3 [ {T_e^(kappa_e)(g_b^-1 g_a)}_(10 wedges), {q_B(g)}_(16 divergent blocks), dmu_Haar, full32 contraction ]`

in one authoritative local K4 normal chart and all its exact `S5` transports, where:

- every one-wedge Toller matrix is first the published source object with the published spectral `i epsilon` prescription already taken in the source order;
- all ten K5 wedges are retained;
- the boundary contraction is the complete frozen 32-component all-spin-half contraction;
- the joint meromorphic family remains

`U(lambda)=[product_(B in D) q_B^(lambda_B/2)] A_source`, `|D|=16`;

- the exact source-derived block defining functions remain

`q_B=(1/|B|) sum_(a<b in B) beta(g_b^-1 g_a)^2`;

- only formal/source Taylor jets through total K4 normal degree 3 are constructed.

The gate may introduce an exact algebraic re-expression of an already-published `j=1/2` Toller matrix if and only if it is mechanically proved identical to the source Cartan formula. Such a re-expression is a coordinate bridge, not a new physical mechanism.

## DEPENDENCY

This gate tests only

`independently confirmed K4 object-definition blocker -> source-faithful cubic realization defined?`.

A PASS would authorize a later prospective gate to evaluate the actual all-32 K4 order-3 polar coefficient/tensor and its annihilator. A PASS does **not** classify that coefficient as zero or nonzero.

A BLOCKED result leaves K4 coefficient evaluation and K5 order 8 locked.

## SOURCE AUTHORITY

Frozen repository authority at preregistration:

- `main` recovered through commit `800e9878f18eac2c805b1d51aa90e1bfaab6abec`;
- `status/CURRENT.md` at that authority: K4 reachability independently confirmed `BLOCKED_OBJECT_DEFINITION`, with next authorized Researcher gate exactly this cubic-realization bridge;
- independent Critic result `results/ACTUAL_K4_ORDER3_SOURCE_OBJECT_REACHABILITY_CRITIC_RESULT.md` and provenance ledger `status/ACTUAL_K4_ORDER3_REACHABILITY_CRITIC_PROVENANCE_LEDGER.md`;
- source-faithful multivariate bridge `sources/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_DERIVATION.md`, blob `b8cb7dc72570132c0d4b1c7e10944681f02e7674`;
- nested Jacobian/Mellin repair `sources/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_NESTED_JACOBIAN_REPAIR_DERIVATION.md`, blob `4db334fb3c12e4ce5caea3d000d01e6012ee2a1c`;
- exact `j=1/2` public Toller source lock `sources/ITER083F_PUBLIC_SOURCE_LOCK.md`, blob `e499e741c85502c1b2fe5abd6e83b1b532de0b3e`;
- repaired source-ordered full-32 leading authority `sources/ITER077I_SM_SOURCE_ORDERED_TOLLER_FUNCTION_K5_L1_DERIVATION.md`, blob `f4c536b3fc70b866edeb7a397b457c47fd07d60a`;
- K3 exact full-coefficient parity derivation `sources/ACTUAL_MULTIVARIATE_POLAR_K3_PARITY_DERIVATION.md`, blob `860d310add243fc30e49c11840e5d51f5a320f72`;
- mixed compact/boost KAK one-jet control `sources/TOLLER_MIXED_POLAR_KAK_JET_SUPPLEMENT.md`, blob `d64c07e720f1d174a29cc2002ebb0fc4ae77dc11`;
- exact nonlinear tubular chart/overlap authority `scripts/iter082e_nonlinear_tubular_chart_overlap.py` and three-chart authority `scripts/iter082f_three_chart_tubular_atlas.py`;
- exact BCH evidence identified by the independent Critic in `status/ITER077_PROVENANCE_LEDGER_V2.md`;
- exact front/pairing evidence identified by the independent Critic in `status/ITERATION_028.md`;
- source erratum `status/ITER077_CONTACT_FORMULA_ERRATUM.md` remains controlling.

Primary source convention remains the repository-frozen Bianchi-Chen-Gamonal causal vertex and Toller formulas. No new external source authority is introduced by this gate.

## FROZEN INPUTS

- candidate: `CRQN v0.2`, unchanged;
- spin sector: all ten wedges `j=l=k=1/2`;
- physical spectral value `rho=gamma/2` with symbolic finite real `gamma`;
- both source causal Toller branches and all `m=+-1/2` reduced entries;
- published one-wedge spectral `i epsilon`; **no** `beta+i epsilon` replacement;
- ten true K5 incidences `(a,b)`, `0<=a<b<=4`;
- all five K4 blocks and their `S5` transports;
- all 32 all-spin-half boundary intertwiner components; no post-hoc boundary-state choice;
- the confirmed 16 divergent-block parameters `lambda_B` and exact source-derived `q_B` family;
- original product Haar measure/source ordering;
- total K4 normal Taylor degree cutoff exactly `3`;
- K3 result may be used only as already-confirmed authority and may not be extrapolated to K4;
- K5 order 8 remains out of scope.

## POSITIVE CONTROLS

P0. Exact source reduced-branch recovery: any full-matrix re-expression must reduce in the `z` Cartan frame to all four Table-II `j=1/2` branch/magnetic formulas frozen in `ITER083F_PUBLIC_SOURCE_LOCK.md`.

P1. Leading matrix recovery: its small-boost leading term must reproduce repaired Iter077I, including branch sign and full angular matrix shape, without using a representative scalar component.

P2. Mixed-path one-jet compatibility: specialization to the already-frozen mixed compact/boost path must reproduce the source-controlled first-subleading structure of `TOLLER_MIXED_POLAR_KAK_JET_SUPPLEMENT.md` within that supplement's stated scope.

P3. Exact source-radius recovery: the defining function must remain `q(h)=beta(h)^2=arcosh((1/2)Tr(hh^dagger))^2` and the block average `q_B`; the source-normal quadratic Hessian must agree with the confirmed tangent radial metric.

P4. Cubic-jet closure: the proposed construction must define every internal and external Toller matrix jet and every nested `q_B` pullback through total K4 normal degree 3 from exact source/chart composition, with no free fitted coefficients.

P5. Full-object retention: the construction must retain all ten wedges, the full 32-component contraction map, original Haar density, true K5 incidence, source branch data and all 16 regulator parameters.

P6. Covariance: relabeling by every `S5` permutation must transport the cubic realization by relabeling source vertices/blocks only; no preferred root, chain or boundary state may enter the definition.

## NEGATIVE CONTROLS

The validator/review must reject each of the following as an implementation of this bridge:

1. scalar K4/Hodge surrogate in place of source Toller matrices;
2. representative boundary component or post-hoc boundary state;
3. frozen angular ray used as a substitute for the full front coefficient;
4. commuting-coordinate replacement of required noncommutative group composition;
5. omission of the four external-to-K4 wedge jets;
6. flat/constant Haar replacement when cubic Haar/Jacobian data are required;
7. one-parameter `rho^z u` or a preferred regulator ray replacing the 16-parameter family;
8. `beta -> beta+i epsilon` or any group-normal reinterpretation of the spectral prescription;
9. termwise contact-distribution multiplication/pullback replacing the source-ordered Toller object;
10. a fitted cubic coefficient, subtraction constant, preferred finite part or regulator metric;
11. inference `K3 residue zero => K4 residue zero`;
12. use of a KAK angular gauge choice that changes the full Toller matrix rather than an algebraically proved gauge-free re-expression of it.

## PASS

`PASS_EXACT_SCOPED` only if the gate constructs a single source-faithful mutually compatible cubic realization satisfying P0-P6 and all negative controls, with no undefined/fitted cubic source datum remaining in R3/R4/R6.

PASS classification:

`K4_ORDER3_SOURCE_FAITHFUL_CUBIC_REALIZATION_BRIDGE_DEFINED_EXACT_SCOPED`.

## FAIL

`FAIL_EXACT_SCOPED` only if exact authoritative source ingredients are mutually incompatible at cubic order (for example, two exact source-defined constructions force contradictory coefficients/covariance/orderings). Failure of a surrogate does not count.

## BLOCKED

`BLOCKED_OBJECT_DEFINITION` if any required R3/R4/R6 datum still needs an extra angular gauge, unproved source-to-chart map, unspecified external jet, unproved nested `q_B` pullback, missing normalization or other non-authoritative choice. Do not invent the missing object.

BLOCKED classification:

`K4_ORDER3_SOURCE_FAITHFUL_CUBIC_REALIZATION_BRIDGE_REMAINS_UNDEFINED_SCOPED`.

## INVALID

`INVALID_IMPLEMENTATION` for broken provenance, incomplete source manifest, a validator/control defect, malformed symbolic algebra, or a workflow that cannot distinguish PASS/BLOCKED/FAIL under the frozen contract.

## INTERPRETATION CEILING

Even a PASS defines only the K4 cubic source realization required to make the **next** coefficient-extraction gate meaningful. It does not compute or classify the K4 polar coefficient, does not determine its annihilator, does not define a physical finite part, does not remove the exact 377-dimensional extension-selection freedom, does not establish regulator independence, and does not authorize K5 order 8 before K4 coefficient extraction and independent review.

No causal-vertex finiteness/divergence theorem, no G3/F9/G8/K5 promotion, no `NEW_PHYSICS_FOUND`, and no complete-QG claim follows.
