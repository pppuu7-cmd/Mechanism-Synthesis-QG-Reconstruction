# Iter078C-RG adversarial qualification — BF15j vertex identification is exact; CRQN refinement stability is conditional on a BF measure/map

**Date:** 2026-09-14

## Reviewed authority

- preregistration `prereg/ITER078C_RG_SUPPORTED_AMBIGUITY_BF15J_CHANNEL.md`, commit `bef22c39989905373c95bf49c666584dc898176e`;
- derivation `sources/ITER078C_RG_SUPPORTED_AMBIGUITY_BF15J_DERIVATION.md`, commit `b531e3d9a2f5e0c9422b170cc220ae9890c0f71e`;
- result `results/ITER078C_RG_SUPPORTED_AMBIGUITY_BF15J_CHANNEL_RESULT.md`, commit `1eb593fdc97b46e3a2cc41e4ac568274e1c3b1c8`.

## Independent source-object check

The local compact supported tensor is source-faithful to the Iter077 ambiguity: it uses the same K5 graph, ten SU(2) spins and five four-valent invariant boundary intertwiners. On the collision submanifold the compact relative holonomies are pure gauge; node gauge invariance reduces the closed spin-network evaluation to the identity-edge K5 contraction.

That closed K5 invariant in a four-valent recoupling basis is the SU(2) 4-simplex `15j` tensor. The repository's exact independent complete-boundary control, `results/ITER077M_ADVERSARIAL_COMPACT_BOUNDARY_CONTROL.json`, checks all 32 all-`j=1/2` basis components and gives the same compact tensor up to the already frozen nonzero node-basis normalizations/signs.

Therefore the **local tensor identification**

`F_SU2  <->  SU(2) BF/Ooguri 15j vertex tensor`

is accepted in its basis-normalization scope.

## Adversarial refinement-map check

The stronger phrase “refinement-stable BF channel” requires a second ingredient beyond local tensor identity: the multi-vertex contraction must use the BF internal face/intertwiner resolution weights and BF gauge-volume prescription.

Iter078C explicitly obtains its pure-`L` BF state sum only **when** the internal SU(2) spins/intertwiners are summed with the standard BF resolution/representation-dimension weights. Those weights are not yet the source-defined causal-Toller refinement map.

This distinction is not optional. Iter078A already established:

`ITER078A_RG_CAUSAL_TOLLER_REFINEMENT_MAP_NOT_YET_DEFINED_FRAMEWORK_EXISTS_BUT_SELECTOR_NOT_COMPUTABLE`.

The causal-Toller source supplies a single-vertex Eq. (4) but not a same-boundary coarse/fine map, fine-complex face/edge measure, boundary embedding/projection map, or fixed-point equation. Iter078B removed only the causal-orientation combinatorial obstruction; its own next-step prescription explicitly treats Lorentzian EPRL-like face/edge convolution weights as **new** multi-vertex structure rather than source authority already present in CRQN v0.2.

Hence a BF-weighted pure-`L` state sum is a mathematically legitimate **conditional comparator/subsector construction**, but it is not yet the actual RG image of the causal-Toller model.

## Counterexample to an unconditional RG reading

Keep the same local `15j` tensor `L` but change the internal face/edge weights away from Ooguri BF weights, as is permitted while the causal-Toller refinement measure is undefined. Then the Pachner/BF identity used to write

`Fine[L^5] = K_BF L`

need not hold. Local tensor identity alone therefore cannot imply CRQN refinement stability.

This counterexample changes no Iter077 local source object; it changes precisely the missing multi-vertex measure/map identified by Iter078A. Therefore it is a scope counterexample, not a competing physical model claim.

## Normalization qualification

The repository correctly refuses to set `K_BF=1`: the non-q-deformed `1<->5` BF relation carries redundant-flatness/gauge-volume normalization issues. Until a regulator/gauge fixing and actual causal refinement measure are frozen, `K_BF` is not a CRQN coupling-flow coefficient.

## Verdict

`QUALIFIED`

Accepted scientific core:

`ITER078C_LOCAL_SUPPORTED_K5_TENSOR_IS_SU2_BF_15J_UP_TO_NONZERO_BASIS_NORMALIZATION_EXACT_SCOPED`.

Conditional statement only:

`PURE_L_REFINEMENT_IS_BF_TOPOLOGICAL_IF_THE_MULTI_VERTEX_MEASURE_AND_INTERNAL_SUMS_ARE_THE_OOGURI_BF_ONES`.

Not authorized:

- “the supported ambiguity is already a refinement-stable direction of CRQN v0.2” without a causal-Toller-to-BF refinement-map theorem;
- using `c=K_BF c^5` as the CRQN RG equation;
- setting `K_BF=1`;
- inferring a nonzero or discrete CRQN fixed point;
- reducing the full Iter077L normal-jet ambiguity space to the single BF-like coefficient `c`.

## Next scientific consequence

The next decisive gate remains the **source-faithful mixed-sector causal refinement map/closure test**, not a pure-BF fixed-point calculation. It must freeze the actual multi-vertex measure, boundary embedding/projection, causal-label propagation and regulator, then test whether mixed `A_0^{5-r}L^r` sectors close on the proposed coupling space. If those map data remain undefined, the correct classification is `BLOCKED_MAP_DEFINITION`.