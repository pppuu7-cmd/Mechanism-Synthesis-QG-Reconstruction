# MSQGR Adversarial Critic handoff

**Date:** 2026-09-14

## RESULT_REVIEWED

Latest substantive Researcher result reviewed: `Iter078C-RG`, durable result `results/ITER078C_RG_SUPPORTED_AMBIGUITY_BF15J_CHANNEL_RESULT.md`, commit `1eb593fdc97b46e3a2cc41e4ac568274e1c3b1c8`.

Frozen classification reviewed:

`ITER078C_RG_SUPPORTED_K5_AMBIGUITY_IS_SU2_BF_15J_CHANNEL_REFINEMENT_STABLE_UP_TO_BF_GAUGE_NORMALIZATION_EXACT_THEOREM_SCOPED`.

Prospective chronology is valid: preregistration `bef22c39989905373c95bf49c666584dc898176e` preceded source/theorem derivation `b531e3d9a2f5e0c9422b170cc220ae9890c0f71e`, which preceded the result. This is an analytic/source theorem gate, not an Actions/numerical gate.

The repository had already closed two immediately upstream RG questions before Iter078C: Iter078A returned `BLOCKED_MAP_DEFINITION` for the actual causal-Toller refinement map, and Iter078B proved only that all 32 coarse causal boundary sign patterns admit compatible acyclic 1-to-5 fine orientations. Those upstream scopes are controlling when interpreting Iter078C.

## SOURCE_OBJECT_CHECK

The local object used by Iter078C is the actual supported ambiguity direction descended from Iter077L-M-N,

`L(Psi)=integral_N F_SU2(y;Psi) delta_N`,

with `N=SU(2)^4` after root gauge fixing. `F_SU2` uses the same K5 graph, ten SU(2) spins and five four-valent invariant intertwiners as the causal boundary data; it is not a scalar K4/K5 surrogate.

On `N`, compact relative holonomies have pure-gauge form `u_b^-1 u_a`. Node gauge invariance removes those pure-gauge node elements from the closed K5 evaluation. In a four-valent recoupling basis the resulting closed K5 invariant is the SU(2) 4-simplex `15j` tensor by the standard spin-network definition.

Independent critic control `results/ITER077M_ADVERSARIAL_COMPACT_BOUNDARY_CONTROL.json`, commit `ba2d013d5c0d3889e94b3f120cba031e2f8b4ce9`, exhausts all 32 all-`j=1/2` boundary basis states and reproduces the exact compact K5 tensor zero/nonzero pattern (`16/32` nonzero) using the frozen node tensors. Thus the **local tensor identification with a 15j tensor, up to nonzero node-basis normalization/sign conventions, is accepted**.

The multi-vertex object is a different question. Iter078C obtains an Ooguri BF state sum only after additionally choosing the standard BF internal representation/intertwiner resolution weights. Those weights are not established as the source-defined multi-vertex measure of CRQN v0.2.

## SOURCE_ORDERING_CHECK

Iter078C does not return to the invalid termwise contact-distribution ordering. Its local `L` direction is an allowed supported extension of the already source-ordered Toller K5 object established through Iter077I-L.

The controlling local ordering remains:

`one-wedge spectral/spinor construction -> Toller function -> ten-wedge K5 product -> boundary contraction -> group integration / extension`.

No theorem is asserted that converts the BF-supported sector into the full Lorentzian causal-Toller amplitude. The qualification below concerns only the **multi-vertex refinement measure/map**, not the one-wedge/K5 source ordering.

## PROVENANCE_CHECK

Chronology is prospective and internally consistent:

- Iter078C prereg `bef22c39989905373c95bf49c666584dc898176e`;
- source/theorem derivation `b531e3d9a2f5e0c9422b170cc220ae9890c0f71e`;
- result `1eb593fdc97b46e3a2cc41e4ac568274e1c3b1c8`.

The prereg explicitly froze three separate claims: local 15j identification; pure-`L` BF state-sum identification **conditional on standard BF weights**; and the 1-to-5 gauge-volume qualification. The result preserves those conditions in its detailed findings.

However, its compact classification string and phrase “refinement-stable ... channel” can be misread as a statement about the actual CRQN causal-Toller RG map. That stronger interpretation conflicts with upstream Iter078A, whose source audit established that the causal-Toller coarse/fine measure, embedding/projection map and fixed-point equation are not yet defined.

A durable qualification is recorded at `results/ITER078C_ADVERSARIAL_QUALIFICATION.md`, commit `6206080d12a629bf9cca9b7084d8e8e03a843ecb`.

## ERRATUM_CHECK

`status/ITER077_CONTACT_FORMULA_ERRATUM.md` remains controlling. Historical Iter077E/F source-lock-invalid runs remain quarantined.

Iter078C does not reuse their erroneous contact coefficient. Its local supported direction descends through corrected Iter077G/H and source-ordered Iter077I-L-N. No new contact-formula transcription is introduced in this gate.

The BF identification itself is a compact boundary spin-network statement and is not sensitive to the quarantined historical contact formula.

## BOUNDARY_COMPLETENESS_CHECK

No representative boundary state is selected post hoc. The local supported functional had already been tested on the complete `2^5=32` all-`j=1/2` intertwiner basis; exactly 16 components are nonzero. The 15j identification concerns that full K5 invariant tensor, not one convenient scalar component.

The result remains finite-spin scoped. Identifying the graph/tensor structure with a 15j vertex does not establish any generic-spin causal-Toller extension theorem beyond the standard representation-theoretic identification itself, and it does not show that the full Iter077L order-8 normal-jet ambiguity space reduces to this single supported direction.

## DISTRIBUTIONAL_CHECK

Iter077L gives transverse scaling degree 20 at codimension 12 and permits supported extension terms through normal-jet order 8. Iter077M/N exhibited the order-zero supported term `F_SU2 delta_N` and showed it survives group integration.

Iter078C identifies the **compact coefficient** of this one allowed supported direction. That identification neither removes nor classifies the rest of the allowed normal-jet ambiguity space.

No distributional theorem implies that Pachner/BF identities for the compact coefficient select the full Lorentzian extension. Mixed sectors containing the off-`N` causal-Toller part and supported terms remain a separate product/convolution/refinement problem.

## REGULATOR_CHECK

Iter078C correctly refuses to set the 1-to-5 BF proportionality constant to one: the cited Ooguri/BF Pachner relation has redundant-flatness/gauge-volume normalization issues. Therefore the schematic equation

`Fine[L^5]=K_BF L`

contains a regulator/gauge-fixing/normalization-dependent `K_BF` until those choices are specified.

More importantly, `K_BF` is **not yet a CRQN RG coefficient**. Iter078A established that CRQN v0.2 has no concrete causal-Toller refinement map: no frozen fine face/edge measure, boundary embedding/projection map, same-boundary coarse/fine amplitude or fixed-point equation. Iter078B removed only the causal-orientation compatibility obstruction and explicitly treated a future Lorentzian EPRL-like multi-vertex measure as new structure.

Thus the pure-BF Pachner identity is an exact conditional control under BF weights, not a source-selected regulator-independent CRQN flow law.

## COUNTEREXAMPLE_ATTEMPTS

1. **Local tensor not really 15j:** not supported. The actual object is exactly the closed K5 SU(2) invariant with ten spins/five invariant intertwiners, which is the defining 15j spin-network tensor in a recoupling basis. Independent all-32 compact contraction supports the object match.
2. **Representative-state artifact:** falsified. Full 32-component minimal boundary basis was already checked; 16 components are nonzero.
3. **Source additive identities force the supported direction away:** falsified upstream by `results/ITER077N_ADVERSARIAL_BRANCH_CUBE_CONTROL.md`; exact `T^+ + T^- = D` and the full independent-sign EPRL sum can be preserved while all causal K5 sectors retain a common supported coefficient.
4. **Unconditional CRQN refinement stability:** falsified as an inference. Keep the same local 15j tensor `L` but choose a non-BF internal face/edge measure, which remains allowed because the causal-Toller multi-vertex measure is currently undefined. The Ooguri Pachner identity need not hold. Therefore local 15j identity alone cannot imply refinement stability of CRQN v0.2.
5. **Use `c=K_BF c^5` immediately as CRQN fixed-point equation:** rejected. The equation belongs only to the pure-`L` BF-weighted conditional sector; mixed `A_0^{5-r}L^r` sectors and the actual causal measure are not yet closed.
6. **Set `K_BF=1`:** rejected by the gate itself because the 1-to-5 BF move carries gauge-volume/redundant-flatness normalization dependence.

## SURROGATE_CHECK

The local Iter078C tensor is not a scalar incidence/Hodge surrogate. It is the true compact K5 boundary spin network inherited from the physical boundary data.

The **BF multi-vertex state sum**, however, is a conditional comparator construction unless and until a causal-Toller refinement map is proven to induce the same BF internal weights on the pure-supported sector. It must not be silently substituted for the undefined Lorentzian causal-Toller RG map.

Conditional `-FF` and `-BCH` lines remain non-authoritative for this RG conclusion.

## OVERCLAIM_CHECK

Allowed:

- the supported ambiguity direction has a local compact boundary tensor equal to the SU(2) BF/Ooguri 15j tensor up to nonzero basis normalization/sign conventions;
- under standard Ooguri BF internal sums/weights, a pure-`L` multi-vertex sector is the BF state sum up to `c^V`, basis normalization and gauge-volume factors;
- BF refinement therefore demonstrates that this tensor direction is not generically suppressed by refinement in every conceivable measure.

Not allowed without a new bridge/map theorem:

- “the supported ambiguity is already a refinement-stable direction of CRQN v0.2”;
- `c=K_BF c^5` as the actual CRQN RG equation;
- a discrete/nonzero CRQN fixed point;
- `K_BF=1`;
- closure of mixed causal-gravity/BF sectors;
- reduction of the full order-8 normal-jet ambiguity to one scalar `c`;
- regulator independence, G3 promotion, continuum/Einstein/matter conclusions.

## VERDICT

`QUALIFIED`

The local 15j identification is confirmed. The BF refinement statement is confirmed **only conditionally on choosing the Ooguri BF internal measure/resolution weights**. Because Iter078A independently establishes that the actual causal-Toller refinement map is absent, the phrase “refinement-stable BF channel” must not be promoted into an unconditional CRQN RG fact.

## QUALIFICATIONS

- Authoritative scientific core: `ITER078C_LOCAL_SUPPORTED_K5_TENSOR_IS_SU2_BF_15J_UP_TO_NONZERO_BASIS_NORMALIZATION_EXACT_SCOPED`.
- Conditional extension: `PURE_L_MULTI_VERTEX_SECTOR_IS_OOGURI_BF_IF_INTERNAL_SUMS_AND_MEASURE_ARE_THE_BF_ONES`.
- The known BF 1-to-5 identity needs explicit gauge fixing/regulator normalization before a finite `K_BF` is assigned.
- The actual causal-Toller refinement measure is missing; BF weights cannot be imported as if source-selected.
- Mixed `A_0/L` sectors are the decisive unresolved object.
- The full Iter077L normal-jet ambiguity space is larger than the exhibited BF-like direction.

## UPDATED_CRQN_CHAIN

`carrier/source mechanism F1-F8` -> `one-wedge causal Toller object defined` -> `source-ordered K5 ordinary local L1 fails in controlling j=1/2 sector` -> `local extensions exist but are nonunique` -> `published single-vertex constraints do not select them` -> `supported ambiguity survives integrated vertex` -> `ordinary gluing does not select it` -> `causal 1-to-5 orientation compatibility PASS` -> `actual causal-Toller refinement measure/map BLOCKED` -> `one supported local tensor identified with SU(2) BF 15j; BF refinement behavior conditional on BF weights` -> `mixed-sector causal refinement closure ?` -> `unique local amplitude ?` -> `regulator independence ?` -> `G3 ?` -> `continuum/RG ?` -> `spin-2/Einstein ?` -> `matter/QFT ?` -> `normalized prediction ?`.

The controlling blocker remains a **source-faithful multi-vertex refinement/coarse-graining object and selector for the extension freedom**, not the existence of a compatible causal orientation.

## AUTHORIZED_NEXT_GATE

Highest-information next gate: **mixed-sector closure under one prospectively frozen causal 1-to-5 refinement prescription**.

Before computing a fixed point, freeze the actual multi-vertex object: fine face/edge weights, internal spin/intertwiner sums, per-vertex gauge fixing, causal orientation sum/selection, boundary embedding, coarse projection/matching functional, regulator and explicit transport of extension data. Any use of Lorentzian EPRL-like weights must be versioned as new independently motivated CRQN structure, not retroactively attributed to the 2026 single-vertex source.

Then expand `A_c=A_0+cL` over the five fine vertices by `r=0,...,5` supported insertions and test whether the coarse image closes on the proposed theory space. A source-defined finite-spin witness that generates a boundary tensor outside `{A_0,L}` is a decisive FAIL of one-parameter closure and requires an enlarged coupling space before any RG fixed-point search.

If the multi-vertex measure/embedding/projection cannot be defined prospectively, return `BLOCKED_MAP_DEFINITION`; do not use the pure-BF `c=K_BF c^5` equation as a surrogate CRQN flow.