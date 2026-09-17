# Prospective preregistration — full-source boundary S5 transport object definition

Date: 2026-09-17

Status: **PROSPECTIVELY FROZEN BEFORE SUBSTANTIVE OUTPUT**.

Parent scientific gate: `K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION`, prereg commit `d6b0e805101c8590eafac71398cc2b1466691752`.

Immediate blocker authority: terminal source-fixed boundary-dual diagnostic repair 5, run `35193589556`, classification `BOUNDARY_S5_REPRESENTATION_UNRESOLVED_EXACT`, reconciled in `results/K5_EXACT_CANCELLATION_UNPROJECTED_BOUNDARY_DUAL_S5_DIAGNOSTIC_REPAIR5_RESULT.md`.

## HYPOTHESIS

The repair-5 mismatch is an object-definition mismatch rather than a physical S5 obstruction: the complete source-ordered all-`j=1/2` order-zero boundary Wick functional becomes exactly S5 covariant when a vertex permutation acts **simultaneously** on (i) Schwinger edge variables, (ii) the source wedge endpoint/orientation data, and (iii) the complete 32-state boundary basis.

The source-derived covector law to test is

`a_p(p alpha) = chi(p) A_p^(-T) a(alpha)`,

where `A_p` is the already-authoritative 32-dimensional boundary-vector action and `chi(p)` is frozen to one of exactly two source-derived one-dimensional characters before output:

1. trivial character `chi_0(p)=+1`;
2. orientation character `chi_sgn(p)=sgn(p)=(-1)^(number of canonically reversed K5 edges)`.

No fitted phase, matrix, character, channel mixing or post-output convention change is allowed.

## exact OBJECT

For a frozen positive generic Schwinger vector `alpha`, define the complete unprojected order-zero boundary Wick covector

`a(alpha) in C^32`

by the source-ordered all-`j=1/2` K5 object, retaining all 32 boundary basis components and all original `100000` node-choice terms.

For a vertex permutation `p`, define the **transported source object** before contraction as follows.

- Edge `(a,b)`, `a<b`, maps to canonical target edge `(min(p(a),p(b)),max(p(a),p(b)))`.
- Schwinger weight follows that edge exactly.
- If canonical edge orientation is preserved, endpoint magnetic entry `(row,col)` is transported unchanged.
- If canonical edge orientation is reversed, endpoint roles are exchanged, hence `(row,col)->(col,row)` before compression, exactly as independently established by `ORIENTATION_TRANSPOSE_SOURCE_S5_EXACT`.
- Any source-common sign forced by the exact off-axis leading matrix under reversal is tracked explicitly and may contribute only through the two prospectively frozen characters above; it is not fitted.
- The boundary vector basis is transported by the independently reconstructed exact `A_p`; the amplitude is compared as a covector through `A_p^(-T)`.

The gate must construct the target by **two independent exact routes**:

A. a direct source-entry route which applies the edge map and orientation-sensitive endpoint transport to every source term before Wick pairing and evaluates the full target vector at `p alpha`;

B. an independently organized transported-pattern route which maps source-term edge-entry patterns first, reconstructs the target complete vector, and agrees componentwise with route A before any representation-law verdict.

No invariant-dual projection is allowed until the full 32-vector equality has been decided.

## DEPENDENCY

`correct source ordering + full all-32 boundary contraction + exact source-entry orientation transport + exact boundary S5 action -> full simultaneous source/boundary transport law -> authorization of coefficient-level S5 covariance in K5 exact-cancellation resolver`.

If this object does not close, the parent exact-cancellation resolver remains physically uninterpretable under S5 transport and must not issue corner exponents.

## SOURCE AUTHORITY

- Source ordering remains `one-wedge spectral/spinor integration -> Toller function -> product of ten Toller matrices -> full boundary contraction -> K5 group/distributional object`.
- Corrected Iter077I authority remains run `34786586785`, alias head `102fc7268b732bead5dfcf6d61fe4479ae1d3030`; historical run `34786550378` remains failure/non-authority.
- Source derivation `sources/ITER077I_SM_SOURCE_ORDERED_TOLLER_FUNCTION_K5_L1_DERIVATION.md`, blob `f4c536b3fc70b866edeb7a397b457c47fd07d60a`, fixes the full `j=1/2` leading matrix and edge orientation: for canonical wedge `(a,b)`, `a<b`, row is target half-edge `(b,a)`, column is source half-edge `(a,b)`.
- Source leading matrix is linear: `M(v)=[[v_z,-v_x-i v_y],[-v_x+i v_y,-v_z]]`, so reversal is checked exactly rather than assumed.
- Full invariant-dual K5 object commit `e9ed372a91ac1bd219dc7671a916c70405e9cd43`; canonical numerator DAG commit `666aa6e61f62bbfff456f6be7995ce3a65f2b633`.
- Exact source invariant-vector transport result commit `dbd03184774a027f6e735138742295dfa211214e`: `A_cycle W=W I_2`.
- Exact orientation-transpose source-entry transport result commit `e9a0472da5e55216789f1d6c20118da9f9d59061`: source-type and recompressed matching dictionaries are exactly covariant when reversed canonical edges transpose `(row,col)` before compression.
- Source-fixed diagnostic repair-5 authority remains run `35193589556`; it is a negative/object-definition control, not the full-source object.
- Published one-wedge spectral `i epsilon` is retained unchanged.

## FROZEN INPUTS

- candidate `CRQN v0.2` unchanged;
- all source spins `j=1/2`;
- all 32 boundary components;
- all original `100000` source node-choice terms per complete vector;
- exact rational / Gaussian-rational arithmetic only;
- Reynolds projector rank two and pivots `[1,4]` only as a downstream coordinate control, never as replacement for the full vector;
- two generic positive Schwinger witnesses exactly:
  - `W1=(2,3,5,7,11,13,17,19,23,29)`;
  - `W2=(31,37,41,43,47,53,59,61,67,71)`;
- three frozen nontrivial permutation lanes:
  - even five-cycle `C=(1,2,3,4,0)`;
  - inverse five-cycle `Cinv=(4,0,1,2,3)`;
  - odd transposition `T=(1,0,2,3,4)`;
- order-zero Wick object only; this gate defines transport and does not inspect physical corner coefficients;
- exactly two candidate source characters: `chi_0=+1` and `chi_sgn=sgn(p)`;
- exact boundary action reconstructed from the existing local tensor action, never fitted;
- no float, tolerance, adaptive witness, post-hoc boundary state, regulator choice, fitted two-channel map, or new character after output.

## POSITIVE CONTROLS

P1. Verify exact source blobs / lineage and that the source-fixed repair-5 result is already terminal before this gate.

P2. Verify 10 K5 edges, all 32 boundary components and exactly `100000` source terms per complete vector.

P3. Reconstruct `A_C`, `A_Cinv`, `A_T` independently from local tensor actions and verify exact group inverses/composition, including `A_C A_Cinv=I`, `A_T^2=I`.

P4. Verify Reynolds rank two and pivots `[1,4]`, and reproduce `A_C P=P=P A_C` as a provenance control.

P5. Mechanically count canonical-edge orientation reversals for each permutation and verify parity equals permutation sign. In particular the odd transposition must expose a nontrivial sign character while the five-cycle cannot hide it.

P6. Verify directly from the source leading matrix that `M(-v)=-M(v)` on three exact linearly independent integer vectors.

P7. Route A and route B target 32-vectors must agree exactly for every W1/W2 and C/Cinv/T lane before law classification.

P8. Every direct and transported route uses full source support; no representative boundary state or projected channel may decide equality.

P9. After a full-vector law is identified, `P^T` pivot coordinates and the historical weighted compressed coordinate extraction must agree exactly for both base and transported targets.

P10. Round-trip source transport `p` followed by `p^-1` must reproduce the complete source pattern object exactly.

P11. The known source-fixed alpha-only comparison is retained as a negative provenance control and must remain distinct from the full-source transported object; its mismatch may not be overwritten.

## NEGATIVE CONTROLS

N1. Omitting row/column transpose on reversed canonical edges must be detected as a different transported source object and must fail exact source-pattern round-trip and/or at least one frozen full-vector law lane.

N2. Applying a fitted nontrivial constant `2x2` channel matrix is forbidden and rejected before evaluation.

N3. Replacing the full 32-vector verdict by invariant-dual projected equality is rejected.

N4. A 31-component target, any source-term count other than `100000`, changed W1/W2 tuple, changed generator, or float conversion is `INVALID_IMPLEMENTATION`.

N5. Swapping trivial/orientation character after seeing output, introducing an arbitrary phase, or changing endpoint orientation convention post hoc is rejected.

N6. Reusing the source-fixed repair-5 target as if it were the transported-source target is rejected by the route-A/route-B object identity controls.

## PASS

Return exactly one of:

- `K5_FULL_SOURCE_BOUNDARY_S5_CONTRAGREDIENT_TRIVIAL_CHARACTER_EXACT_SCOPED` if routes A/B agree, all controls pass, and `a_p(p alpha)=A_p^(-T)a(alpha)` exactly for all six W1/W2 x C/Cinv/T lanes;
- `K5_FULL_SOURCE_BOUNDARY_S5_CONTRAGREDIENT_ORIENTATION_CHARACTER_EXACT_SCOPED` if routes A/B agree, all controls pass, and `a_p(p alpha)=sgn(p) A_p^(-T)a(alpha)` exactly for all six lanes.

Exactly one character must pass globally. If both are indistinguishable on even lanes, the frozen odd transposition decides them.

A PASS only defines the full-source transport law and authorizes a separately controlled resume of the parent exact-cancellation resolver. It is not a physical-corner or Stokes result.

## FAIL

`K5_FULL_SOURCE_BOUNDARY_S5_TRANSPORT_OBSTRUCTION_EXACT_SCOPED` if routes A/B agree exactly, all source/object controls pass, but neither prospectively frozen source-derived character gives the contragredient law on all frozen generators and witnesses.

This is a concrete obstruction of the current source/boundary transport implementation/object in scope. It is not permission to add a new mechanism post hoc.

## BLOCKED

`BLOCKED_OBJECT_DEFINITION` if the repository/source authority does not determine one of the mandatory maps needed for the exact full object — in particular the endpoint/orientation action, boundary basis action, source sign under canonical reversal, or the simultaneous source-plus-Schwinger map — without adding a convention not already fixed by source authority.

If blocked, do not invent a scalar, projected or fitted surrogate.

## INVALID

`INVALID_IMPLEMENTATION` for source/blob mismatch, incomplete source/boundary coverage, failed route-A/route-B equality due to coding inconsistency, failed group-action/round-trip controls, altered frozen inputs, failed negative controls, use of floating arithmetic, or promotion of partial/nonterminal values.

## INTERPRETATION CEILING

This gate can define or obstruct only the exact full-source S5 transport law of the frozen order-zero all-`j=1/2` boundary Wick object. It cannot classify a Schwinger corner as finite/divergent, prove global Stokes/IBP, evaluate an invariant-dual K5 period, prove the full 217-dimensional tensor zero/nonzero, reduce `dim_C F_8=377`, select a physical finite part, prove regulator independence, promote F9/G3/G8/K5, establish `NEW_PHYSICS_FOUND`, or complete quantum gravity.
