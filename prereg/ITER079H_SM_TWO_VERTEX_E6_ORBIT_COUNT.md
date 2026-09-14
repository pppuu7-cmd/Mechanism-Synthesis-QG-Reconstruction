# Iter079H-SM — minimal two-vertex E6 common-left orbit count under KKL gluing

Status: PROSPECTIVELY PREREGISTERED BEFORE IMPLEMENTATION
Date: 2026-09-14

## Dependency
Iter079E is terminal PASS conditional for KKL E5 gluing under fixed parent boundary normalization. Iter079F is terminal PASS conditional for one common-left redundancy of each local causal/Toller vertex. This gate depends on both and was opened only after both terminal artifacts were consumed.

## Question
For the minimal two-vertex composition obtained by KKL boundary gluing of two local causal vertex amplitudes, do the two one-vertex common-left redundancies remain independent, or does gluing reduce them to a single diagonal redundancy?

This gate counts exact algebraic redundancies only. It does not choose a quotient measure, Faddeev-Popov factor, Haar normalization, or a physical finite gauge volume.

## Frozen premise
1. Each local vertex integrand depends on its own local group variables only through relative products `g_b^-1 g_a`, hence has one simultaneous common-left redundancy (Iter079F).
2. The KKL gluing identity contracts boundary state data and preserves the parent boundary normalization (Iter079E).
3. In the frozen minimal composition model, boundary gluing does **not** identify the Lorentz-group integration variables belonging to distinct local vertex integrals; it contracts the shared boundary spin-network data.
4. No full source-faithful E3/E4/E6 state-sum theorem is assumed.

## Frozen lanes
### Lane A — provenance/dependency lock
PASS only if Iter079E/F authority and the frozen distinction between boundary-state contraction and local group-variable identification are recorded.

### Lane B — exact independent-action invariance
Construct two disjoint K5 local variable sets `g1_a`, `g2_a`. Verify all ten wedges of vertex 1 are invariant under `g1_a -> h1 g1_a` and all ten wedges of vertex 2 under `g2_a -> h2 g2_a`, with `h1,h2` independent. The glued boundary scalar contraction is declared independent of these redundant left-orbit coordinates under the frozen KKL gluing premise. PASS iff the full minimal product/contraction is invariant under `G x G` exactly.

### Lane C — diagonal-only quotient negative control
Quotient only the diagonal subgroup `h1=h2=h`. Verify algebraically that the relative orbit parameter `r=h2^-1 h1` remains as one unfixed group degree of freedom. Equivalently, `dim(G x G)-dim(diag G)=dim(G)` at the group-manifold level. For `SL(2,C)`, record real dimensions `12-6=6` as a dimension-count control, not as a measure theorem.

### Lane D — scope locks
PASS only if the conclusion is limited to the frozen factorized local-integration + KKL boundary-contraction model. Explicitly leave unresolved: unique E6 quotient normalization, possible additional redundancies/constraints in a full multi-vertex state-sum representation, E3/E4 source bridge, E7/E8 distributional extension transport, and all downstream physics claims.

## Frozen classifications
If A–D pass:
`ITER079H_SM_MINIMAL_TWO_VERTEX_KKL_GLUE_RETAINS_TWO_INDEPENDENT_COMMON_LEFT_REDUNDANCIES_DIAGONAL_QUOTIENT_INSUFFICIENT_EXACT_SCOPED_E6_PARTIAL`

If the independent `G x G` action is not invariant under the frozen gluing model:
`ITER079H_SM_TWO_VERTEX_COMMON_LEFT_REDUNDANCIES_COUPLE_UNDER_KKL_GLUE_EXACT_SCOPED`

If the gluing/group-variable premise cannot be justified:
`ITER079H_SM_TWO_VERTEX_E6_ORBIT_COUNT_BLOCKED_SOURCE_PREMISE_MISSING`

## Claim locks
No unique gauge-fixing prescription; no finite gauge-volume claim; no Faddeev-Popov theorem; no complete E6; no E7/E8 selection; no G3/F9/G8/K5/RG promotion; no complete QG; no `NEW_PHYSICS_FOUND`.
