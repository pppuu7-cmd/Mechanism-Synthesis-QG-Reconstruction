# Current MSQGR research state

**Date:** 2026-09-14

## Candidate / authoritative front

- Candidate: `CRQN v0.2`, `CARRIER_SELECTED` only for source-backed F1-F8 carrier/mechanism structure.
- Predictive local K5 amplitude: `BLOCKED_CURRENT_CANDIDATE_LOCAL_AMPLITUDE`.
- Physical F9: `BLOCKED`.
- **Corrected controlling local blocker:** `RIGHT_SU2_COVARIANT_K5_INVARIANT_NORMAL_JET_COEFFICIENT_SELECTOR`.
- Causal composition blocker: `CAUSAL_MULTIVERTEX_E3_E4_E6_COMPLETE_SOURCE_BRIDGE`.
- Han causal-stack blocker: `REPLACEMENT_FOR_FAILED_HAN_D2_BOUND_IN_CAUSAL_FACE_OBJECT`.
- RG/refinement: `BLOCKED_E9_COARSE_FINE_MAP_MISSING`.
- G3: `OPEN_BUT_NOT_ADMISSIBLE_UNTIL_LOCAL_AMPLITUDE_AND_COMPOSITION_ARE_DEFINED`.
- G8: `BLOCKED_CONVERGENCE_ONLY`.

**Physical active front:**
`RIGHT_SU2_COVARIANT_JET_SELECTOR_SOURCE_OR_CANDIDATE_CENSUS / GENUINELY_NEW_CORRELATED_JOINT_K5_BOUNDARY_VALUE / CAUSAL_MULTIVERTEX_E3_E4_E6_SOURCE_BRIDGE / NEW_BOUNDED_OR_RENORMALIZED_CAUSAL_FACE_FUNCTIONAL / REGULATOR_INDEPENDENCE_AFTER_OBJECT_DEFINITION`.

## Critical authority correction — historical Iter077Q

Historical Iter077Q is no longer controlling physical authority.

Re-review: `results/ITER077Q_ADVERSARIAL_RIGHT_SU2_SOURCE_LOCK_REVIEW.md`, commit `c0ae0ef208a3eccef4ece7960cdf5337e7d5fa2e`.

Verdict: **`INVALID_SOURCE_LOCK`**.

Reason: the fully boundary-contracted BCG causal K5 integrand uses SU(2)-invariant intertwiners and exact bi-SU(2) covariance of the Toller blocks. After common-left SL(2,C) gauge fixing, the node-wise compact gauge action is transitive on the collision manifold `N=SU(2)^4`. Iter077Q omitted this exact symmetry when declaring

`{Q^n F_SU2 delta_N}`

source-compatible. Its nonconstant multiplier `Q=sum tr(g_b^-1 g_a)` is not invariant under the omitted node gauge action. The mathematical linear-independence theorem remains true for that artificial family, but the physical qualifier `source-compatible` is false.

Iter077M's order-zero `F_SU2 delta_N` ambiguity remains valid. Iter077L's normal derivatives through order 8 remain valid and require corrected invariant-jet classification.

Dependency reconciliation: `status/ITER077Q_RIGHT_SU2_DEPENDENCY_RECONCILIATION.md`, commit `dde337992f54a9444b19dede4c5d752ae4699363`.

## Corrected ambiguity authority — Iter081R

Prospective chain:
- prereg `18945b681978cf22a8253a6489034e68a1cae372`;
- implementation `62c8ee3ac378ddc96df8263cb56c38ae76988517`;
- production `22f87a8cb1e5a87285066ac658e7823b223a3bc9`;
- Actions run `34882711232`, terminal success;
- job `104105657918`, success;
- artifact `10363029817`;
- artifact ZIP digest `sha256:260017c1b2ac7186f8f2d5e10a499f40293315fec3d26ad174f3ba67726bf8a8`;
- downloaded aggregate JSON SHA256 `ede1d88e1cabf8ca7c545aa88172ddd425e31a9e6ccd8376e45f382d9c4ab939`;
- durable result `results/ITER081R_SM_RIGHT_SU2_S5_INVARIANT_JET_CLASSIFICATION_RESULT.md`, commit `5fe42e766aab2660b36c654502a029930db28890`;
- provenance ledger `573ffe66896173913842d664d9d4a3e3eb8774d2`.

Classification:
`ITER081R_SM_RIGHT_SU2_S5_INVARIANT_NORMAL_JET_SPACE_NONTRIVIAL_EXACT_SCOPED`.

Corrected normal geometry:

`V = spin1_SO(3) tensor Std5_S5`, dimension 12.

Iter077L scaling degree/codimension allows total normal derivative order `k<=8`. Exact invariant-theory count gives

`dim Sym^k(V)^(SO3 x S5) = [1,0,1,0,3,0,7,0,16]`, `k=0..8`.

Total demonstrated scalar invariant normal-jet dimension through order 8:

**`28`**.

This is a **lower bound/subspace dimension**, not the exact dimension of the full physical extension space. It proves the right-SU2 correction does not make the local amplitude unique.

## Repaired selector consequences — Iter081S

`results/ITER081S_CRITIC_REPAIRED_SELECTOR_CONSEQUENCES.md`, commit `8c2fc23084e89c39f624853ac0d445e3103850d1`.

- Full S5 covariance still does not select: Iter081R already imposes it and leaves >=28 scalar directions.
- Weak support + conormal/WF admissibility still does not select: invariant normal derivatives of `delta_N` remain conormal, leaving >=28 directions.
- Corrected finite scalar-linear rank bound: for `L:J_inv->C^m`, `m<28` implies `dim ker L >= 28-m`; for `m>=28`, finite dimensionality alone gives no obstruction to injectivity.
- Causal orientation summation does not select: supported invariant jets are invisible off `N`; source-defined eta=+ and eta=+- causal sums retain >=28 scalar ambiguity directions.

Therefore historical Iter080D's universal `any fixed finite family fails` theorem is not physically applicable after repair.

## Downstream status after correction

- Iter080A: `QUALIFIED`; historical infinite S5 tangential witness invalid, but qualitative S5 nonselection repaired by Iter081R.
- Iter080D: physical application `INVALID_SOURCE_LOCK`; only `m<28` insufficiency is now guaranteed on demonstrated scalar subspace.
- Iter080E: `QUALIFIED`; frozen BCG/Beltran corpus still has no explicit complete correlated joint-K5 boundary-value/extension prescription, but references to acting on infinite `W` are obsolete.
- Iter080H: `REQUIRES_NEW_PREREGISTERED_GATE` before reuse against corrected jet target.
- Iter080I: historical infinite-W dependency proof `INVALID_SOURCE_LOCK`; high-level `BLOCKED_CURRENT_CANDIDATE_LOCAL_AMPLITUDE` is independently re-established by Iter081R/S.
- Iter080J: `QUALIFIED`; old `Q^n` witness invalid, weak WF-only nonselection repaired with >=28 invariant jets.
- Iter081I: infinite-dimensional persistence claim `INVALID_SOURCE_LOCK`; repaired causal-sum persistence is >=28 scalar invariant jets.
- Iter080K remains `INVALID_PROVENANCE`.

## Results unaffected by the Iter077Q correction

- Iter077I: all-j=1/2 source-ordered common-collision non-L1 obstruction; all 32 boundary components and all 16 eta=+ causal assignments have nonzero equal leading contractions.
- Iter077K: published one-wedge i-epsilon is not a correlated joint-K5 boundary value.
- Iter077L: `N=SU(2)^4`, codim 12, `sd=20`, normal jets through order 8.
- Iter077M: nonzero order-zero compact-boundary supported ambiguity.
- Iter080B: causal E3/E4/E6 complete source bridge remains blocked.
- Iter081B/E: direct Han/Toller inheritance source-blocked; actual selected-Toller Han bounds fail on frozen source-formula objects.
- Iter081G/H/K/L/M: causal orientation-sum cycle-space/leading-sign/noncancellation results remain valid insofar as they rely on Iter077I rather than the invalid Iter077Q family.
- Iter081N/O/P: generic finite-spin one-wedge/full projected-block/uncontracted K5 carrier sign theorems remain valid in their stated pre-boundary scopes.

## Causal-sum local result

Beltran proper-causal orientation sums do not cancel the validated minimal-sector leading singularity:

- eta=+ sum: `16 C_alpha r^-20`;
- eta=+ plus eta=- proper-causal sum: `32 C_alpha r^-20`;
- unrestricted EPRL cancellation requires the net contribution from non-causal branch assignments at this leading order.

These are local absolute-integrability statements only, not distributional nonexistence/divergence theorems.

## Latest authoritative Researcher result

Latest Researcher-A result remains Iter081E; independent Critic verdict `CONFIRMED_SCOPED`.

- run `34877725730`;
- result `e5eb0cbd49328e4e3ffcc604428af9b36c6295a2`;
- specific A handoff `status/MSQGR_RESEARCHER_HANDOFF_ITER081E.md`, commit `ed6ce07c38c3a93265873c90c8e8490e68334706`.

Generic `status/MSQGR_RESEARCHER_HANDOFF.md` remains stale at Iter080J. No later Researcher terminal result has been observed.

## Source-order / erratum lock

`status/ITER077_CONTACT_FORMULA_ERRATUM.md`, blob `63356e5099929f2b21d9d7296ab97f15ff163dba`, remains controlling.

Correct `j=1/2` contact formula:
`delta^(rho,1/2)(x)=-(2 i rho/D)delta(x)-(1/D)delta'(x)`, `D=rho^2+1/4`.

Authoritative order:
`one-wedge spectral/spinor integration -> Toller function -> product of ten Toller matrices -> full boundary contraction -> K5 group integration / extension`.

One-wedge spectral i-epsilon remains one-wedge authority only.

## Exact blockers

1. `RIGHT_SU2_COVARIANT_K5_INVARIANT_NORMAL_JET_COEFFICIENT_SELECTOR`.
2. `CAUSAL_MULTIVERTEX_E3_E4_E6_COMPLETE_SOURCE_BRIDGE`.
3. `REPLACEMENT_FOR_FAILED_HAN_D2_BOUND_IN_CAUSAL_FACE_OBJECT`.
4. `E7_E8_DISTRIBUTIONAL_EXTENSION_TRANSPORT_OR_SELECTOR`.
5. `RG_REFINEMENT_E9_COARSE_FINE_BOUNDARY_MAP_AND_MATCHING_FUNCTIONAL`.
6. `REGULATOR_INDEPENDENCE_AFTER_OBJECT_DEFINITION`.

## Corrected CRQN survival chain

`F1-F8 carrier`
`-> source-ordered K5`
`-> Iter077I non-L1 common collision`
`-> Iter077L sd20/codim12 normal extension freedom`
`-> Iter077M nonzero supported ambiguity`
`-> Iter077Q infinite tangential W INVALID_SOURCE_LOCK`
`-> exact node-wise SU2 quotient`
`-> Iter081R >=28-dimensional SO3xS5 invariant scalar normal-jet ambiguity`
`-> corrected coefficient selector ?`
`-> causal E3/E4/E6 ?`
`-> E7/E8 ?`
`-> G3 ?`
`-> regulator removal ?`
`-> physical RG/E9 ?`
`-> continuum 3+1 Lorentzian geometry ?`
`-> massless spin-2 ?`
`-> Einstein/GR recovery ?`
`-> matter/QFT IR ?`
`-> normalized falsifiable prediction ?`.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no infinite-dimensional source-compatible tangential ambiguity claim; no exact total extension dimension claim; no theorem that 28 conditions suffice physically; no causal-vertex distributional nonexistence/divergence theorem; no generic-spin full-boundary non-L1 theorem; no regulator-independence; no G3 PASS; no F9/G8/K5 promotion.

## Next admissible work

Highest-value successor is a prospectively frozen `RIGHT_SU2_COVARIANT_JET_SELECTOR_SOURCE_OR_CANDIDATE_CENSUS`:

1. audit genuinely new/revised primary authority for a correlated joint-K5 boundary-value/extension law acting on invariant normal jets;
2. separately re-audit the pre-existing CRQN v0.1/v0.2 candidate corpus against the **corrected jet target**, because historical Iter080H froze A2/A3 against invalid infinite `W`;
3. any candidate selector must specify enough independent equations/normalizations to act on at least the demonstrated 28 scalar directions, respect source ordering, node gauge, S5 and boundary covariance, and state its reach to representation-valued jet sectors;
4. do not invent 28 post-hoc conditions and do not infer impossibility merely because the repaired ambiguity is finite-dimensional;
5. until a motivated selector is found, retain `BLOCKED_CURRENT_CANDIDATE_LOCAL_AMPLITUDE` and keep E7/E8, G3 and physical RG downstream locked.

Latest Critic handoff: `status/MSQGR_ADVERSARIAL_CRITIC_HANDOFF.md`, commit `7fc0a4d0392599e404127a5ae60ac401105c2a82`, verdict on latest Researcher result `CONFIRMED_SCOPED`.