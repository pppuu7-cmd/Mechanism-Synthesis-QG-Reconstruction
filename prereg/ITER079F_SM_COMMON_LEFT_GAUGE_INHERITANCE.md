# Iter079F-SM — common-left gauge redundancy inheritance under local causal vertex replacement

Status: PROSPECTIVELY PREREGISTERED BEFORE IMPLEMENTATION
Date: 2026-09-14

## Question
Under the same restricted inheritance class that passed Iter079E, does the **one-vertex common-left group redundancy** of the parent EPRL/KKL vertex survive replacement of local wedge/vertex factors by the generalized causal Toller factors `T^(kappa_ab)(g_b^-1 g_a)`?

This gate is intentionally narrower than full E6. It asks only whether the local common-left gauge orbit and the associated need to quotient/fix one redundant noncompact group integration are algebraically inherited. It does not assume a complete multi-vertex gauge-fixing theorem or a finite quotient normalization.

## Frozen source/algebra facts
1. The causal generalized vertex is built from wedge factors depending on relative group elements `g_b^-1 g_a` with fixed causal labels `kappa_ab`; no ordinary representation composition law is assumed for the Toller functions.
2. Parent Lorentzian EPRL/KKL vertex integrands share the standard simultaneous common-left redundancy because their local group dependence is through relative products.
3. Iter079E has already established conditional inheritance of the parent KKL E5 gluing algebra when the causal change is only a local vertex-factor replacement and the parent boundary normalization is fixed.
4. Beltran leaves finiteness of the generalized causal vertex open. Therefore this gate cannot establish quotient finiteness, regulator independence, or a complete E6 prescription.

## Frozen lanes
### Lane A — source/provenance contract
PASS only if the recorded contract contains the causal relative-element dependence `g_b^-1 g_a`, the parent common-left redundancy premise, Iter079E conditional inheritance scope, and the finiteness lock.

### Lane B — exact common-left invariance
Represent each relative word as `inv(g_b) * g_a`. Under the simultaneous replacement `g_a -> h*g_a` for every local group variable, reduce the transformed free-group word exactly and verify

`inv(h*g_b) * (h*g_a) = inv(g_b) * g_a`

for all ten K5 wedges. No numerical sampling and no fitted coefficients.

### Lane C — orbit/gauge-fixing consequence
For a local integrand that depends only on the ten invariant relative words, verify symbolically that adding one common-left orbit variable changes no local factor. Record the exact consequence as **redundant orbit survives**, hence an ungauge-fixed integration contains a common group-volume factor and a source-faithful definition still needs a quotient/fixing convention. This is an algebraic redundancy statement, not a claim that a particular normalization is uniquely selected.

### Lane D — scope lock / adversarial control
PASS only if the result explicitly does **not** promote:
- unique E6 quotient normalization;
- multi-vertex gauge-orbit counting after gluing;
- finiteness of the causal vertex;
- E3/E4 or E7/E8;
- G3/F9/G8/K5 or RG.
Also verify a negative control: independent left multiplications `g_a -> h_a g_a` do not cancel generically, so the inherited redundancy is the single simultaneous common-left action rather than arbitrary independent local actions.

## Frozen classifications
If A–D pass:
`ITER079F_SM_CAUSAL_TOLLER_VERTEX_COMMON_LEFT_GAUGE_REDUNDANCY_CONDITIONALLY_INHERITS_EXACT_SCOPED_E6_PARTIAL`

If exact common-left invariance fails:
`ITER079F_SM_CAUSAL_TOLLER_COMMON_LEFT_GAUGE_INHERITANCE_FAILS_EXACT_SCOPED`

If the source/provenance premise is missing:
`ITER079F_SM_COMMON_LEFT_GAUGE_INHERITANCE_BLOCKED_SOURCE_PREMISE_MISSING`

## Claim locks
No complete E6 theorem; no unique quotient measure/normalization; no causal-vertex finiteness/divergence theorem; no E7/E8 selection; no G3/F9/G8/K5 promotion; no complete-QG claim; no `NEW_PHYSICS_FOUND`.

## Dependency rule
Do not open a composed multi-vertex E6 orbit-counting/normalization gate until Iter079F is terminal and consumed. E7/E8 remain separate until E3/E4/E6 define a composed functional.
