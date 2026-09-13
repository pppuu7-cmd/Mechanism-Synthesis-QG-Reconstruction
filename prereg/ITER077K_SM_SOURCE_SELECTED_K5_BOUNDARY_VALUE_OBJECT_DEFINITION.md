# Iter077K-SM preregistration — source-selected K5 boundary-value object-definition audit

Date: 2026-09-14
Status: prospective / frozen before terminal source classification

## Hypothesis

The primary causal-vertex/Toller sources either (A) explicitly define a joint K5-level correlated/conditional boundary-value or regulator prescription sufficient to assign the non-L1 common-collision group integral after the ten one-wedge Toller functions are constructed, or (B) they do not. This is an object-definition gate, not a numerical convergence gate.

## Exact object

`SOURCE_SELECTED_CORRELATED_OR_CONDITIONAL_COMMON_COLLISION_BOUNDARY_VALUE_WITH_FULL_BOUNDARY_CONTRACTION_AND_SUBLEADING_SOURCE_DATA`

The audited chain is strictly:

`one-wedge spectral/Feynman construction -> Toller function -> product of ten Toller functions -> full boundary contraction -> four gauge-fixed SL(2,C) group integrations`.

No termwise product of contact distributions is substituted for this chain.

## Source authority

Primary authority only for PASS:

1. E. Bianchi, C. Chen, M. Gamonal, `Causal spinfoam vertex for 4d Lorentzian quantum gravity`, arXiv:2601.23162 / Phys. Rev. D 113, 126020 (2026).
2. E. Bianchi, C. Chen, M. Gamonal, `Toller matrices and the Feynman i epsilon in spinfoams`, arXiv:2604.24945.

Secondary/index sources may be used only to locate primary text, never to establish PASS.

## Frozen inputs

- Authoritative Iter077I-SM result: source-ordered all-j=1/2 K5 leading product is not locally L1 in all 32 boundary components.
- Authoritative CURRENT active missing object: source-selected correlated/conditional common-collision boundary value with full boundary contraction and subleading source data.
- Published spectral `i epsilon` is retained exactly as defined at the one-wedge level.
- No new regulator, finite part, contour deformation, subtraction, boundary state, or extension is introduced.

## Positive control

The source must explicitly define the one-wedge Toller object and the K5 vertex ordering. Finding Eq. (3)-type one-wedge Feynman prescription and Eq. (4)-type ten-Toller group integral is required for a valid audit.

## Negative controls

The following do NOT count as a K5 boundary-value prescription:

- a one-wedge `epsilon -> 0+` prescription whose limit is taken before K5 multiplication;
- the identity `T+ + T- = D` or cancellation only after an unconstrained sum over wedge signs;
- large-spin saddle/asymptotic finiteness;
- a statement that Toller matrices are polynomially bounded functions;
- termwise contact-distribution extensions;
- ordinary EPRL finiteness theorems unless the source proves their applicability to each fixed-causal Toller product;
- an implicit appeal to formal group integration without an extension/convergence theorem at the identified common collision.

## PASS

PASS iff primary source text supplies an explicit joint prescription/theorem that fixes the common-collision K5 boundary value for the fixed-causal ten-Toller product, with enough ordering information to distinguish it from arbitrary correlated extensions.

Classification:
`ITER077K_SM_PRIMARY_SOURCE_DEFINES_JOINT_K5_BOUNDARY_VALUE_PRESCRIPTION_EXACT_SCOPED`.

## FAIL

FAIL iff the sources explicitly state that no such prescription exists or demonstrate inconsistency/nonexistence of the fixed-causal object under their own definition.

Classification:
`ITER077K_SM_PRIMARY_SOURCE_FIXED_CAUSAL_K5_OBJECT_NONEXISTENT_OR_INCONSISTENT_SOURCE_EXPLICIT`.

## BLOCKED

BLOCKED iff the primary sources define the one-wedge Toller matrices and write the formal K5 group integral but do not provide a joint common-collision boundary-value/regulator/extension prescription or theorem sufficient to define the non-L1 object identified by Iter077I-SM.

Classification:
`ITER077K_SM_SOURCE_SELECTED_K5_COMMON_COLLISION_BOUNDARY_VALUE_NOT_DEFINED_IN_PRIMARY_SOURCE_OBJECT_DEFINITION_BLOCKED`.

## INVALID

INVALID iff the primary source cannot be inspected at sufficient detail, the source ordering cannot be recovered, or the audit accidentally relies on secondary summaries for the decisive claim.

## Interpretation ceiling

A BLOCKED result is not a proof that no mathematical extension exists. It means CRQN cannot currently promote the fixed-causal K5 vertex to a defined physical amplitude using the published source prescription alone, and no post-hoc extension may be treated as source-selected without a new independently motivated, prospectively testable mechanism.

No full causal-vertex divergence/nonexistence theorem; no regulator-independence theorem; no G3/F9/G8/K5 promotion; no complete-QG claim.