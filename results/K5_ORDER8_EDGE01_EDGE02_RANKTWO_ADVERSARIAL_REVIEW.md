# AUTOMATION B adversarial review — K5 edge01/edge02 rank-two sign-change lane

Date: 2026-09-16

Independent Critic preregistration: `prereg/K5_ORDER8_EDGE01_EDGE02_RANKTWO_INDEPENDENT_CRITIC_REVIEW.md`, commit `40a3f78b2a85ef1750d8c6006438c0b1d2044398`.

Reviewed Researcher result: `results/K5_ORDER8_EDGE01_EDGE02_RANKTWO_SIGN_CHANGE_RESULT.md`.

Reviewed production:
- run `35035152999`, terminal success;
- job `104602503455`, terminal success;
- head `6fb57d915cbb20c80674ec2a97121b35ffedd396`;
- artifact `10422859073`;
- ZIP digest `sha256:b409c5dfb8c1182da8bcab903a800955c8a34462a179c841f08d511d55625867`;
- production JSON SHA256 `c3abbcaf61bafc13eea2677ce71537d5899e375b3571e513abc1e94a0287a31f`.

Mandatory Critic verdict: **`REQUIRES_NEW_PREREGISTERED_GATE`**.

## Decisive wrong-object witness

The Researcher scientific preregistration `prereg/K5_ORDER8_EDGE01_EDGE02_RANKTWO_POSITIVITY_LANE.md` prospectively freezes the construction as starting from the same authoritative **`all-32/full-source K5 order-eight principal-symbol object`**. It does not prospectively freeze a representative boundary component `k=(0,0,0,0,0)` as the scientific object.

The production implementation does not retain the all-32 boundary fiber. Its shared general engine defines

`selected_patterns(mod, edges)`

by iterating

`itertools.product(mod.NODE_OPTIONS[0], repeat=5)`.

Thus every node is fixed to boundary intertwiner label `k=0`, producing exactly `4^5=1024` source terms for the single boundary component

`k=(0,0,0,0,0)`.

It never iterates the 32 boundary labels `ks in {0,1}^5`. By contrast, an all-32 source contraction must range over every boundary component; the repository's full-32 K5 diagnostics contain `100000=(4+6)^5` raw node-choice terms across that full fiber.

The rank-two script then explicitly treats `len(pats)==1024` as the required source count and classifies the sign witnesses only for that selected component.

The post-prereg derivation confirms the narrowing after the scientific contract was frozen:

> `The boundary component used in the rank-one predecessor and here is the stripped component k=(0,0,0,0,0), retaining all 4^5=1024 source node-tensor choice terms.`

It further describes the result as a `component-level noncancellation lane` and states that it is not a replacement for the full boundary tensor.

This is a material scientific-object change, not a control-only implementation repair.

## Why this cannot be repaired in place

The preregistered sign question is scalar (`retain a fixed positive sign`) while the frozen construction simultaneously says `all-32/full-source object`. A 32-component tensor/vector has no unique scalar sign until a component, covector, norm, invariant-dual projection or other scalar functional is prospectively specified.

The implementation resolves that ambiguity by choosing `00000` after preregistration. That representative-state selection is precisely the kind of post-hoc narrowing forbidden by the standing review contract.

A control-only repair cannot turn the all-32 tensor into the `00000` scalar without changing the scientific object. Therefore the old gate cannot be rewritten as if it had prospectively asked the `00000` question.

## Exact witness audit inside the narrower produced object

The narrower component-level calculation appears internally coherent and is not being rejected as false mathematics:

- authoritative edge order is retained;
- determinant is exact: `det L(t,u)=5*(3tu+7t+7u+8)>0` for `t,u>0`;
- the exact positive witness `R(1,2)=1254383808/9191328125` and negative witness `R(1,3)=-14327118848/13839609375` are interior to the positive Schwinger cone;
- the specialized edge02 slice and full general-L engine reproduce the same witness values;
- the post-prereg derivation correctly limits the consequence to the `00000` component and does not claim a full projective-period theorem.

Thus this review does not issue `SCIENTIFIC_FAIL_CONFIRMED` and does not claim the two rational witness values are wrong. The problem is that the result is attached to a scientific contract that froze a different / insufficiently scalarized object.

## Boundary completeness

The production's `1024` source-choice count is a complete source-term census **only for `00000`**. It is not full-32 boundary completeness. No theorem is supplied reducing the all-32 tensor or the two invariant-dual K5 channels to `00000`.

The current K5 authority elsewhere explicitly identifies a two-dimensional invariant dual/covector space and states that physically informative scalar periods must use the dual action / transposed Reynolds projector because the stripped node basis is not orthonormal. That makes a representative-component sign theorem even less suitable as an all-32 scalar replacement.

## Source ordering / surrogate firewall

The produced component-level lane still uses the authoritative ten-edge K5 incidence, exact weighted Laplacian/Schwinger construction, source node tensors and exact rational arithmetic. No termwise contact-distribution product, scalar K4/Hodge surrogate, one-parameter physical regulator or modified spectral prescription is promoted.

The published one-wedge spectral `i epsilon` remains locked. `status/ITER077_CONTACT_FORMULA_ERRATUM.md` remains controlling and historical Iter077E/F remain quarantined.

## Interpretation ceiling

The Researcher result itself correctly avoids promoting the sign change to full 9D projective-period zero/nonzero. This review retains that ceiling. No K5 full tensor theorem, finite-part selector, regulator-independence theorem, global patching, E3/E4/E6, G3/F9/G8/K5 promotion, `NEW_PHYSICS_FOUND` or complete-QG claim follows.

## Verdict

**`REQUIRES_NEW_PREREGISTERED_GATE`**

The produced exact `00000` sign-change witness may be retained as non-authoritative exploratory evidence, but it cannot be cited as the terminal result of the existing all-32/full-source scientific gate.

## Required successor

Do not repair the old result by editing its object after the fact.

Prospectively preregister one of the following explicit scalar objects before any new terminal classification:

1. a **component-specific** `K5_ORDER8_EDGE01_EDGE02_RANKTWO_00000_SIGN_LANE`, freezing `k=(0,0,0,0,0)` and the 1024 source terms from the outset; or, preferably because it unlocks the physical front,
2. the already higher-information **two invariant-dual K5 projective channels**, using the exact 32D boundary action and transposed Reynolds projector, with full all-32 source contraction and projective integration/noncancellation.

The second option has higher information gain and downstream relevance. Further mechanical rank-three/rank-four representative-component positivity lanes are not authorized as the main front.
