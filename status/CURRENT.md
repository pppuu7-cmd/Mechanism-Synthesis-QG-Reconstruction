# Current MSQGR research state

**Date:** 2026-09-15

## Authoritative front

Candidate remains `CRQN v0.2`, `CARRIER_SELECTED` only for the established source-backed F1-F8 carrier/mechanism structure.

Predictive local K5 amplitude remains `BLOCKED_CURRENT_CANDIDATE_LOCAL_AMPLITUDE`; physical F9 and G3 remain downstream-blocked.

The latest confirmed local result is the **scientifically repaired source-faithful joint K5 multivariate meromorphic bridge**.

Classification:

`BRIDGE_AUTHORITY_CONFIRMED_SCOPED`

Researcher verdict: **`PASS_EXACT_SCOPED`**.

Independent repaired Critic verdict: **`CONFIRMED_SCOPED`**.

The Iter083P object-definition blocker is therefore closed at exactly one arrow in the frozen all-`j=1/2` local sector:

`source-ordered ten-Toller/full-32 off-collision object`
`-> explicit q_B-scheme 16-parameter multivariate meromorphic polar germ`.

It remains open at the physical selector arrow:

`multivariate polar germ`
`-> physical finite part / unique K5 extension`.

No one-parameter residue, finite part, regulator-independence theorem or predictive local amplitude is implied.

**Immediate active front:**

`ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR`
`/ PHYSICAL_FINITE_PART_OR_JOINT_K5_SELECTOR`
`/ K5_GLOBAL_MULTISTRATUM_PATCHING`
`/ CAUSAL_MULTIVERTEX_E3_E4_E6_COMPLETE_SOURCE_BRIDGE`
`/ REGULATOR_INDEPENDENCE_AFTER_GLOBAL_ANALYTIC_OBJECT_DEFINITION`.

---

## Latest authoritative result — repaired joint K5 meromorphic bridge

Parent scientific preregistration:

`prereg/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_AUTHORITY_GATE.md`

commit `4151c02452edd3e5e2c49952686e42e64c6dc180`.

Nested-Jacobian scientific-repair preregistration:

`prereg/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_CRITIC_REPAIR_1.md`

commit `148dd5130c448420419a807826fdfd84bb1228ef`.

Corrected derivation:

`sources/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_NESTED_JACOBIAN_REPAIR_DERIVATION.md`

commit `b227ad0d433d89c9fe1df589535b354961e5a91b`.

Corrected machine lock:

`sources/raw/source_faithful_joint_k5_bridge_lock.json`

commit `ae43268efc7e4b7bdc46df514a8fc03b3fe2267e`.

Corrected validator/workflow:

- validator commit `2dfb4ad341bca7ebf1e41521909052e5056980cc`;
- workflow/head `6aca4249f956f5e1a05a9e214660495427ab7470`.

Authoritative repaired production:

- run `34954021547`, terminal success;
- job `104331589295`, terminal success;
- artifact `10390666862`;
- artifact ZIP digest `sha256:2989f3b4aad1c1ccb8494f2f11821a66df17e99c15b731c3d84c587ed1003abb`;
- production JSON SHA256 `079587747eb747e067400b88a3969982a495c17eee9150543cdede856d883acd`.

Durable scientific-repair result:

`results/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_NESTED_JACOBIAN_REPAIR_RESULT.md`

commit `457107f45513facf8911d3001610a362f9d924b8`.

Independent repaired adversarial confirmation:

`results/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_ADVERSARIAL_REVIEW_REPAIR2.md`

commit `9efc5d227afc3cff187d386a5574e2ae010cc7d9`.

The earlier confirmation at `d22ee017...` is not authority: it was superseded after discovery of the nested-Jacobian defect. The temporary Critic state `REJECTED_SCIENTIFIC_PENDING_REPAIR` at commit `b0a5ba418...` correctly blocked downstream promotion until the fresh production above succeeded.

---

## Exact source-derived regulator family

Source order remains

`one-wedge spectral/spinor integration`
`-> Toller function`
`-> product of ten Toller matrices`
`-> full 32-component boundary contraction`
`-> K5 group integration / distributional extension`.

For a relative Lorentz element `h`, define from the exact source Cartan rapidity

`q(h)=beta(h)^2=arcosh(Tr(h h^dagger)/2)^2`.

Writing

`s=Tr(h h^dagger)/2-1`,

exact formal inversion gives

`q=2s-(1/3)s^2+(4/45)s^3+O(s^4)`.

For every collision block `B`, define

`q_B=(1/|B|) sum_(a<b in B) beta(g_b^-1 g_a)^2`.

This is source-derived, nonnegative, relabel/reversal covariant, vanishes exactly on the corresponding compact block collision, and has the repaired Iter083M source-normal quadratic form.

The 16 regulator parameters are attached to the 10 K3, 5 K4 and 1 K5 divergent blocks:

`U(lambda)=[product_(B in D) q_B^(lambda_B/2)] A_source`.

`A_source` is the actual already-constructed ten-Toller/full-32-boundary local object with the original product Haar density. The published one-wedge spectral prescription is not modified and no `beta+i epsilon` substitution is used.

---

## Correct nested blow-up geometry

The complete compact collision arrangement contains

- 10 K2 blocks;
- 10 K3 blocks;
- 5 K4 blocks;
- 1 K5 block;

for 26 nontrivial blocks. K2 faces are included in the resolution although they are individually locally integrable.

For every maximal divergent chain

`K3 subset K4 subset K5`,

the orthogonal incremental normal dimensions are

`(6,3,3)`.

The nested boundary scales act on cumulative dimensions

`(6,9,12)`.

Therefore the **correct** pulled-back Haar/tubular radial powers are

`(5,8,11)`,

not the historical `(5,2,2)` incremental-polar tuple.

Equivalently,

`dmu ~ rho3^5 rho4^8 rho5^11 d rho3 d rho4 d rho5 * smooth_nonzero_density`.

At frozen `j=1/2`, the three K3-internal, three additional K4-internal and four additional K5-internal wedges give cumulative source powers

`(-6,-12,-20)`.

Combining source and Haar powers gives

`(-1,-4,-9)`

and therefore the independently known superficial divergence degrees

`omega=(0,3,8)`.

This agreement is now derived from the actual nested geometry and source edge count.

---

## Exact regulator incidence / convergence geometry

For every divergent face `C`, the boundary-scale regulator form is

`L_C(lambda)=sum_(B subseteq C, |B|>=3) lambda_B`.

The 16-by-16 block-to-face incidence matrix is exactly

- rank 16;
- lower triangular by increasing block size;
- unit diagonal;
- determinant 1.

Thus the face forms `L_C` are equivalent regulator coordinates.

At a maximal corner,

`U(lambda) ~ rho3^(L_K3-1) rho4^(L_K4-4) rho5^(L_K5-9) A`.

A sufficient convergence chamber is

`Re L_K3>0`, `Re L_K4>3`, `Re L_K5>8`.

Production supplies the explicit simultaneous witness `lambda_B=1`, for which

`L_K3=1`, `L_K4=5`, `L_K5=16`.

Hence the full local convergence chamber is nonempty.

The pole-producing Taylor orders at the physical regulator origin are exactly

- K3: `0`;
- K4: `3`;
- K5: `8`.

These orders are now source/geometry-derived candidates for the next actual polar-normal-jet calculation; their allowed values are not yet a proof that every corresponding source polar tensor is nonzero.

---

## Production controls

All B1-B9 passed in fresh production.

The validator also rejected all 14 malformed constructions:

1. representative boundary component;
2. auxiliary regulator-space `Q`;
3. `beta+i epsilon` substitution;
4. omitted Haar density;
5. post-hoc holomorphic projection / finite part;
6. preferred sequential specialization;
7. preferred label;
8. K5-only incidence replacing the 16-block family;
9. wrong source order;
10. historical `(5,2,2)` promoted as nested Jacobian;
11. singular regulator incidence map;
12. empty convergence chamber;
13. wrong nested source exponents;
14. false regulator-independence claim.

An intermediate run `34953991571` already produced scientific PASS with the corrected geometry but failed afterward because the old workflow attempted to print a removed JSON key. It uploaded no artifact and is implementation-only history, not authority.

---

## Defining-function scheme firewall

The confirmed bridge is scoped to the explicit source-derived `q_B` family.

Under an allowed smooth positive rescaling

`q'_B=exp(phi_B)q_B`,

the families obey

`U'(lambda)=exp[(1/2)sum_B lambda_B phi_B]U(lambda)`.

The factor is holomorphic and invertible in the regulator parameters. Therefore existence of the meromorphic continuation and the polar divisor are stable, while lower Laurent coefficients can mix when higher-order poles occur.

Consequently:

- **meromorphic bridge existence is confirmed**;
- **regulator independence is not confirmed**;
- no individual lower Laurent coefficient may be called physically canonical without an additional theorem or prospectively frozen scheme.

No one-parameter slice is authorized by the bridge result.

---

## Retained exact local authority

1. Iter083A — complete 32-dimensional all-`j=1/2` boundary-fiber/S5 graded normal-symbol classification.
2. Iter083B — intrinsic supported ambiguity `F_8` with exact `dim_C F_8=377`.
3. Iter083C — all additive descendants of `T+ + T-=D` retain a joint-K5 nullmode.
4. Iter083D — source-defined causal orientation sums retain exact dimension 377; historical Iter081I infinity superseded.
5. Iter083E — one-wedge Ruhl/Toller analytic uniqueness does not lift to a joint-K5 selector.
6. Iter083F — common finite spectral epsilon does not regularize the common collision.
7. Iter083G-L — auxiliary regulator geometry / source-authority controls do not themselves select the extension.
8. repaired Iter083M — unique source-normal tangent radial quadratic basis.
9. provenance-correct Iter083N — formal local finite-part/jet theorem only.
10. Iter083P repair3 — joint bridge was still missing at that recovery point; Critic `QUALIFIED`.
11. repaired source-faithful joint K5 bridge — actual local 16-parameter multivariate meromorphic polar germ now **Researcher PASS + Critic CONFIRMED_SCOPED**.

The exact 377-dimensional physical extension-selection freedom has **not** been removed by item 11.

---

## Current survival chain

`F1-F8 carrier`
`-> source-ordered K5 off-collision object`
`-> exact boundary-covariant supported ambiguity F_8, dim=377`
`-> additive / causal / one-wedge analytic / spectral-epsilon mechanisms fail as selectors`
`-> source-faithful q_B-scheme 16-parameter meromorphic polar germ CONFIRMED`
`-> actual multivariate polar normal-jet coefficients / annihilator ?`
`-> physical finite-part / joint-K5 selector ?`
`-> global multistratum distributional patching ?`
`-> causal E3/E4/E6 ?`
`-> quantum dynamics G3 ?`
`-> regulator removal / independence ?`
`-> RG/refinement ?`
`-> continuum Lorentzian geometry ?`
`-> massless spin-2 ?`
`-> Einstein/GR ?`
`-> matter/QFT IR ?`
`-> normalized falsifiable prediction ?`.

---

## Exact remaining blockers

1. **`ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR`** — compute actual source polar coefficients/orders on K3/K4/K5 faces, distinguish allowed from nonzero channels, and track the defining-function holomorphic-gauge action.
2. **`PHYSICAL_FINITE_PART_OR_JOINT_K5_SELECTOR`** — select a physical extension/finite part; the bridge supplies a meromorphic family, not a renormalization condition.
3. **`K5_ACTUAL_DISTRIBUTIONAL_PARTITION_OF_UNITY_PATCHING_AND_INTER_STRATUM_TRANSPORT`**.
4. **`CAUSAL_MULTIVERTEX_E3_E4_E6_COMPLETE_SOURCE_BRIDGE`**.
5. **`REPLACEMENT_FOR_FAILED_HAN_D2_BOUND_IN_CAUSAL_FACE_OBJECT`**.
6. **`E7_E8_DISTRIBUTIONAL_EXTENSION_TRANSPORT_OR_SELECTOR`**.
7. **`RG_REFINEMENT_E9_COARSE_FINE_BOUNDARY_MAP_AND_MATCHING_FUNCTIONAL`**.
8. **`REGULATOR_INDEPENDENCE_AFTER_GLOBAL_ANALYTIC_OBJECT_DEFINITION`**.

---

## Authorized next work

Prospectively freeze `ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR`.

The gate must:

- consume the actual 16-parameter `q_B` meromorphic germ, not a one-parameter surrogate;
- retain all 32 boundary components and exact source order;
- derive face polar coefficients at K3/K4/K5 and test whether the candidate orders `(0,3,8)` are actually nonzero;
- compute the corresponding supported normal-jet tensors / annihilator ideals;
- track the holomorphic defining-function gauge action `U -> exp[(1/2)sum lambda_B phi_B]U`;
- distinguish scheme-invariant highest polar data from lower Laurent coefficients that can mix;
- avoid claiming a physical finite part unless a new independent selector is prospectively authorized.

In parallel, continue the independent global multistratum patching and causal E3/E4/E6 source bridges; do not infer them from the local meromorphic result.

---

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no unique physical K5 extension; no physical finite-part selector; no one-parameter physical `A_-1` without a new prospective specialization gate; no regulator independence; no generic-spin complete extension theorem; no global all-strata patching; no causal-vertex finiteness/divergence theorem; no G3/F9/G8/K5 promotion; no fitted subtraction constants/scales or preferred finite parts without independent authority.
