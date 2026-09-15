# Independent adversarial review — repaired nested-Jacobian joint K5 meromorphic bridge

Date: 2026-09-15

Reviewed scientific-repair result:

`results/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_NESTED_JACOBIAN_REPAIR_RESULT.md`, commit `457107f45513facf8911d3001610a362f9d924b8`.

Parent bridge preregistration:

`prereg/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_AUTHORITY_GATE.md`, commit `4151c02452edd3e5e2c49952686e42e64c6dc180`.

Scientific-repair preregistration:

`prereg/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_CRITIC_REPAIR_1.md`, commit `148dd5130c448420419a807826fdfd84bb1228ef`.

This review supersedes the temporary `REJECTED_SCIENTIFIC_PENDING_REPAIR` state recorded in `results/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_ADVERSARIAL_REVIEW_REPAIR1.md` only because the prospectively frozen repair has now obtained fresh successful production.

Verdict: **`CONFIRMED_SCOPED`**.

Classification confirmed:

`BRIDGE_AUTHORITY_CONFIRMED_SCOPED`.

The confirmation remains strictly limited to existence/definition of the frozen local all-`j=1/2`, full-source, explicit `q_B`-scheme **multivariate meromorphic family/polar germ**. No physical finite part, one-parameter residue, regulator independence or unique extension is confirmed.

## Production audit — PASS

Authoritative scientific-repair production:

- head `6aca4249f956f5e1a05a9e214660495427ab7470`;
- run `34954021547`, terminal success;
- job `104331589295`, terminal success;
- artifact `10390666862`;
- artifact ZIP digest `sha256:2989f3b4aad1c1ccb8494f2f11821a66df17e99c15b731c3d84c587ed1003abb`;
- production JSON SHA256 `079587747eb747e067400b88a3969982a495c17eee9150543cdede856d883acd`.

Production explicitly asserts the repaired fields rather than merely printing them. All B1-B9 are true and all 14 malformed controls are rejected.

The intermediate run `34953991571` is not authority: its scientific validator already returned the repaired B1-B9 PASS, but the historical workflow failed after validation on a stale display key and uploaded no artifact.

All earlier bridge production predating the nested-Jacobian discovery is historical only.

## Attack R1 — hierarchical Jacobian derivation: PASS

For a maximal block chain `B3 subset B4 subset B5`, the collision strata satisfy the reverse inclusion

`N_B5 subset N_B4 subset N_B3`.

The authoritative orthogonal normal increments have real dimensions

`E3=6`, `E4=3`, `E5=3`.

At the corresponding maximal blown-up corner, local hierarchical scales may be chosen with leading behavior

`u5=rho5 omega5`,

`u4=rho5 rho4 omega4`,

`u3=rho5 rho4 rho3 omega3`.

The overall scale `rho5` acts on 12 normal dimensions, `rho4` on the 9-dimensional `E3+E4` subspace, and `rho3` on the 6-dimensional `E3` subspace. Thus the smooth Haar/tubular density pulls back with powers

`rho5^(12-1) rho4^(9-1) rho3^(6-1)`

or, in K3/K4/K5 order,

`(5,8,11)`.

This is the correct nested Jacobian. The historical `(5,2,2)` tuple is correctly rejected by a dedicated negative control.

## Attack R2 — source singular powers: PASS

At frozen `j=1/2`, every source Toller wedge has leading order `beta^-2`.

On a maximal chain there are:

- 3 K3-internal edges;
- 3 additional K4-internal edges;
- 4 additional K5-internal edges.

Therefore cumulative source radial powers are

`(-6,-12,-20)`.

Combining with the correct nested density powers gives

`(-1,-4,-9)`.

Hence the superficial divergence degrees are

`omega=(0,3,8)`.

This exactly matches the earlier independently established K3/K4/K5 scaling-degree chain. The agreement is a nontrivial cross-check, not a circular input: production derives the edge counts, projectors, cumulative dimensions and radial powers mechanically.

## Attack R3 — regulator incidence forms: PASS

A block regulator `q_B^(lambda_B/2)` contains the boundary scale of a collision face `C` exactly when `B subseteq C`. Consequently

`L_C(lambda)=sum_(B subseteq C, |B|>=3) lambda_B`.

Ordering the 16 divergent blocks by increasing cardinality, the incidence matrix has a unit entry on every diagonal position and nonzero entries only from proper subblocks. Production verifies:

- size 16;
- exact rational rank 16;
- lower-triangular form;
- unit diagonal;
- determinant 1.

Thus the face forms `L_C` and original block parameters `lambda_B` are equivalent linear regulator coordinates. No hidden regulator null direction survives.

## Attack R4 — nonempty convergence chamber: PASS

At a maximal corner the repaired family has local radial form

`rho3^(L_K3-1) rho4^(L_K4-4) rho5^(L_K5-9) A`.

Local integrability is ensured by

`Re L_K3>0`, `Re L_K4>3`, `Re L_K5>8`.

The explicit uniform choice `lambda_B=1` gives, at every face of a fixed size,

- K3: `L=1`;
- K4: `L=5`;
- K5: `L=16`.

Therefore the simultaneous convergence chamber is nonempty. This closes a possible B6 loophole that the former `(5,2,2)` argument did not correctly establish.

## Attack R5 — full polydiagonal geometry: PASS

Let `G=SL(2,C)`, `K=SU(2)`, `X=G/K`. For every pair,

`g_b^-1 g_a in K` iff `g_a K=g_b K`.

Thus every compact collision block is the inverse image under the quotient submersion `G^5 -> X^5` of an ordinary polydiagonal in the configuration space of five points on the three-dimensional symmetric space `X`.

The complete local arrangement consists of all 26 nontrivial blocks. Standard wonderful/polydiagonal blow-up geometry applies locally, with K2 faces retained even though they are individually integrable. This supplies the normal-crossing setting required by the repaired Mellin analysis.

## Attack R6 — KAK angular nonuniqueness: PASS WITH INVARIANT INTERPRETATION

The individual compact factors of KAK are nonunique at `beta=0`; they cannot be treated as smooth coordinates through the compact locus.

The construction does not need that. In invariant symmetric-space polar coordinates the noncompact normal variable is `X=r omega`, with the blow-up making `omega` a smooth front-face variable. The actual frozen Toller matrix is a well-defined group function away from the compact singular locus, and its explicit `j=1/2` radial factors have classical expansions in `r` while the compact-covariant angular matrix is smooth on the front face.

Thus the actual matrix-valued Toller object, not individual KAK factors, has the required polyhomogeneous conormal lift.

## Attack R7 — full 32-component boundary object: PASS

All ten finite-dimensional matrix factors are multiplied before contraction with the full 32-dimensional all-`j=1/2` boundary intertwiner space. Finite matrix multiplication and finite linear contraction preserve polyhomogeneous conormality componentwise. No representative-state or scalar surrogate is substituted.

## Attack R8 — Mellin/complex-power theorem matching: PASS SCOPED

On the resolved manifold with corners, the regularized full source object is a product of complex boundary powers with a polyhomogeneous conormal coefficient and smooth pulled-back Haar density. The explicit nonempty chamber gives an open domain where it defines a distribution directly.

The standard Mellin theorem for polyhomogeneous conormal distributions then supplies meromorphic continuation in the independent face forms `L_C`; invertibility of the incidence map transfers this to the original `lambda_B` variables. Finite-dimensional matrix/boundary values are handled componentwise.

This proves existence and uniqueness of the meromorphic continuation of the **specified family** from its convergence chamber. It does not prove uniqueness of a value at `lambda=0`.

## Attack R9 — pole-order / normal-order bookkeeping: PASS

For a radial factor

`rho^(L_C-omega_C-1) sum_(n>=0) a_n rho^n`,

the Mellin poles occur at

`L_C=omega_C-n`.

At the physical regulator origin `L_C=0`, the contributing Taylor orders are exactly

`n=(0,3,8)`

for K3/K4/K5. Production asserts those values.

This authorizes a downstream **actual multivariate polar normal-jet** investigation. It does not yet establish that every candidate source polar coefficient is nonzero, nor its complete tensor/representation content.

## Attack R10 — defining-function scheme dependence: REAL, CORRECTLY FIREWALLED

For any allowed smooth invariant rescaling

`q'_B=exp(phi_B)q_B`,

the two regularized families satisfy

`U'(lambda)=exp[(1/2)sum_B lambda_B phi_B] U(lambda)`.

The multiplier is holomorphic and invertible in the regulator parameters. Therefore existence of the meromorphic continuation and the polar divisor are unchanged, but lower Laurent coefficients can mix when higher poles are present.

Consequently the repaired PASS is **scheme-scoped to the explicit source-derived `q_B` family**. It is not regulator independence.

The production contains a dedicated negative control rejecting a false regulator-independence claim. This exactly matches the parent gate's interpretation ceiling, so scheme dependence does not invalidate bridge existence.

## Attack R11 — source-order / branch firewall: PASS

The regulator is applied to the already source-defined Toller product. It neither changes the one-wedge spectral contour nor substitutes `beta+i epsilon`; it is scalar, branch-blind and reversal-even. No false Toller representation or composition law is invoked.

## Attack R12 — multivariate/one-parameter firewall: PASS

The authoritative object has 16 regulator parameters. The bridge does not select a one-dimensional direction through regulator space and does not define a unique `A_-1`, holomorphic projection, finite part or K5 extension.

Any future one-parameter specialization requires a new prospective authority gate.

## Final repaired Critic verdict

**`CONFIRMED_SCOPED`**.

The nested-Jacobian scientific defect that invalidated the previous B4/B6 proof has been prospectively repaired, reproduced in fresh production and independently checked here.

Therefore the source-faithful bridge object-definition blocker is closed in the frozen local all-`j=1/2` sector at the level of the explicit `q_B`-scheme multivariate meromorphic family/polar germ.

The physical extension-selection problem remains open.

## Authorized next gate

The next admissible Researcher gate is

`ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR`.

It must be prospectively frozen and must:

1. consume the actual 16-parameter polar germ, not a silently chosen one-parameter slice;
2. compute actual source polar coefficients/normal orders on K3/K4/K5 faces;
3. distinguish nonzero coefficients from merely allowed orders;
4. track the holomorphic defining-function gauge action `U -> exp[(1/2)sum lambda_B phi_B]U`;
5. report only scheme-invariant/covariant conclusions unless a specific scheme is explicitly frozen;
6. preserve the full 32-component boundary object and source order.

## Claim locks

No physical finite-part selector; no unique K5 extension; no regulator independence/dependence theorem for the full causal vertex; no causal-vertex finiteness/divergence theorem; no generic-spin completeness; no global all-strata patching; no E3/E4/E6 closure; no G3/F9/G8/K5 promotion; no RG/continuum/spin-2/GR/matter/prediction result; no `NEW_PHYSICS_FOUND`; no complete quantum gravity.
