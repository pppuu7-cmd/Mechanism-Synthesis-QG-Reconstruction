# Iter081B-SM preregistration — Han/Toller face-functional transport obstruction

Date: 2026-09-14
Status: PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION

## Question
Can the standard EPRL/KKL Han internal-face stack machinery be inherited directly after replacing Wigner matrices by causal Toller branches, using only currently cited primary authority and exact algebra, without inventing new causal face/stack dynamics?

## Frozen source corpus
1. Muxin Han, arXiv:2602.18665v1 — standard Lorentzian EPRL/KKL stack/face functional, face bound/saturation, bosonic face partition function, localization, gauge fixing and cut/gluing.
2. E. Bianchi, C. Chen, M. Gamonal, arXiv:2604.24945 — Toller functions, `T^(+)+T^(-)=D`, analyticity/i-epsilon, and the explicit statement that individual Toller matrices are functions rather than a Lorentz-group representation.
3. C. E. Beltran, arXiv:2603.22661v2 — causal EPRL-KKL vertex on arbitrary 2-complexes via Toller replacements.
4. Withdrawn arXiv:2603.17207 is quarantined and cannot supply positive authority.

## Frozen object
Han standard face functional:
`tau_k^(h)(g_h)=d_k Tr[ ordered_product_{v in boundary h} P_k D(U_v) P_k ]`, with `U_v=g_ve^{-1} g_ve'`.

BCG additive identity:
`D(U)=T^(+)(U)+T^(-)(U)`.

Natural algebraic branch expansion only:
`tau_k^(h)=sum_{epsilon: boundary h -> {+,-}} tau_{k,epsilon}^(h)`,
`tau_{k,epsilon}^(h)=d_k Tr[ ordered_product_v P_k T^(epsilon_v)(U_v) P_k ]`.

This expansion is not prospectively assumed to be a physical causal stack amplitude.

## Frozen tests
A. Source acquisition/provenance must retrieve all three frozen primary sources and record SHA256 hashes. Network/source failure is INFRASTRUCTURE/PROVENANCE failure, not scientific BLOCKED/PASS.

B. Source-positive checks must recover from actual source text/formulas: Han standard face/stack object and its bound/saturation/partition/localization chain; BCG additive branch identity and non-representation warning; Beltran arbitrary-2-complex causal vertex construction.

C. Exact distributive control must verify the branch-sum expansion for noncommuting symbolic matrix factors for face lengths 1..4. Failure is SCIENTIFIC_FAIL_ALGEBRA.

D. Exact anti-inheritance witness: the additive identity `D=T+ + T-` alone must be shown insufficient to imply Han's branch bound. Frozen witness: dimension 2, `D=I`, `T+=2I`, `T-=-I`, `P=I`, one-factor face. Then standard `tau=2 Tr(I)=4=d^2`, while selected branch `tau_+=2 Tr(2I)=8>d^2`. This is only a logical insufficiency witness; it is not asserted to be an actual Toller value.

E. Source-bridge criterion. A direct-inheritance PASS requires an explicit source theorem or derivation in the frozen corpus that supplies a causal Toller face/stack object and establishes all of: (E1) causal face bound replacing/preserving `|tau|<=d_k^2`; (E2) saturation/maximizer locus; (E3) convergence/meromorphy and dominant poles of the causal bosonic face partition function; (E4) localization/condensation theorem; (E5) causal cut/gluing compatibility; (E6) connection back to source-ordered local Toller object without silently replacing the Iter077Q K5 problem by a face surrogate.

The implementation may detect source evidence from retrieved primary text, but must not contain preassigned E1-E6 truth values.

## Frozen classifications
- Any provenance/source retrieval/hash failure: `INVALID_PROVENANCE_OR_INFRASTRUCTURE`.
- Algebraic expansion failure or anti-inheritance witness failure: `SCIENTIFIC_FAIL_ALGEBRA`.
- If all E1-E6 are source-explicit: `ITER081B_SM_HAN_TOLLER_FACE_STACK_DIRECT_INHERITANCE_SOURCE_ESTABLISHED_SCOPED`.
- Otherwise, provided A-D are valid: `ITER081B_SM_DIRECT_HAN_D_TO_SINGLE_TOLLER_BRANCH_FACE_STACK_INHERITANCE_NOT_SOURCE_PROVEN_BLOCKED_SCOPED` with verdict `BLOCKED_SOURCE_BRIDGE`.

## Claim ceiling
A BLOCKED result means only that direct inheritance is not established by the frozen corpus plus the additive identity. It does not prove that no causal Toller stack can exist. Constructing a new causal face functional, transport equation, selector or stack theorem is new model content requiring a separately named prospective gate.

No NEW_PHYSICS_FOUND, complete-QG, K5/F9/G8/G3 promotion, causal-vertex finiteness/divergence theorem, or regulator-independence claim is allowed.