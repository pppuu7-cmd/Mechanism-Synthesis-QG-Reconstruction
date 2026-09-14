# Iter079C-SM — minimal two-vertex causal composition uniqueness

## Prospective status
Frozen before implementation/production.

## Scientific question
Do the source-defined one-vertex causal Toller amplitude data (E1-E2) together with the parent EPRL-KKL **combinatorial** composition skeleton uniquely determine a minimal two-vertex causal functional without adding a new inheritance axiom or normalization/pairing choice?

## Frozen authority
Only the following may be used:
1. authoritative Iter079A/079B results;
2. parent EPRL-KKL existence of a multi-vertex algebraic/state-sum skeleton;
3. Beltran/BCG causal one-vertex data already frozen as E1-E2;
4. elementary exact linear algebra.

The parent numerical weights/pairing/gauge normalization may be used as a **candidate bridge**, but may not be silently declared physically inherited by the causal replacement.

## Minimal abstract foam
Take two nonzero local causal vertex functionals `V_L, V_R` sharing one internal boundary carrier `H`. A composed amplitude requires a bilinear/dual pairing `B` (plus internal weight/normalization data). For fixed boundary insertions `u,v`, write

`Z_B(u,v) = B(V_L(u), V_R(v))`.

The gate tests uniqueness of `Z` from local data + combinatorial gluing alone.

## Frozen lanes

### Lane A — candidate parent bridge exists
Construct an exact finite-dimensional representative with nonzero local vectors and a nondegenerate parent-style pairing `B0`. Verify the composed amplitude is nonzero. This lane establishes existence of a candidate composition, not its causal authority.

### Lane B — pairing normalization underdetermination
Define `B_lambda = lambda B0` with frozen `lambda=2`. Verify exactly that `B_lambda` preserves bilinearity, nondegeneracy and the same orientation/duality type as `B0`, leaves `V_L,V_R` unchanged, but gives `Z_lambda = 2 Z_0 != Z_0` on the frozen nonzero witness. If true, local one-vertex data + topology do not determine the two-vertex normalization.

### Lane C — internal weight underdetermination
Introduce one internal-label weight `w`. Compare frozen choices `w=1` and `w=3` with identical local vertices and pairing. Verify `Z_{w=3}=3 Z_{w=1} != Z_{w=1}` on the same witness. This is a structural E4 freedom unless a causal inheritance rule fixes the weight.

### Lane D — scope/provenance test
Require the authoritative Iter079B classification and explicitly verify that no frozen source/model theorem in the current ledger promotes parent E3-E6 numerical data to causal authority. If such a theorem is present, this lane must invalidate the gate rather than override it.

## Frozen classification
- `ITER079C_SM_MINIMAL_TWO_VERTEX_CAUSAL_FUNCTIONAL_NOT_UNIQUELY_FIXED_BY_LOCAL_VERTEX_DATA_AND_COMBINATORIAL_SKELETON_E3_E4_BRIDGE_REQUIRED_EXACT_SCOPED` if A-D validate and B/C exhibit exact inequivalent compositions.
- `ITER079C_SM_CAUSAL_COMPOSITION_UNIQUENESS_ESTABLISHED_SCOPED` only if the frozen authority uniquely fixes the pairing/weight and the B/C alternatives are disallowed by a previously frozen theorem.
- `ITER079C_SM_INVALID_SOURCE_OR_IMPLEMENTATION` for provenance/implementation failure.

## Interpretation ceiling
A BLOCKED/nonuniqueness result is **not** a theorem that causal multi-vertex amplitudes cannot be defined. It only proves that one-vertex causal data plus combinatorial gluing do not uniquely fix E3/E4 without an inheritance/normalization rule. It does not yet decide E5-E8 or the Iter077Q extension transport problem.

## Claim locks
No `NEW_PHYSICS_FOUND`; no complete-QG claim; no full causal multi-vertex theorem; no unique K5 extension; no regulator independence; no RG/G3/F9/G8/K5 promotion; no reinterpretation of one-wedge spectral `i epsilon` as a joint regulator.
