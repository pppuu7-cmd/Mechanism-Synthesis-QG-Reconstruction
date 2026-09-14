# MSQGR Researcher handoff — Iter081E

Date: 2026-09-14

## New authoritative Researcher result
Iter081E-SM independently reproduced the actual-Toller counterexamples previously present only in Critic controls.

Prospective chain:
- prereg `0f5414c9471a382527ca06c7f29ef2da6b8f8c1d`
- implementation `8ceb7cc99925bb1d2a262b304ce29731f438ffdb`
- production `5743b4e0d6f5ce247ebe207b0ad48b0f17f3f664`
- run `34877725730`
- job `104088973504`
- artifact `10361621460`
- artifact digest `sha256:f2a4c52535799fad2aa7ad94b7bb2eeedde1933dde62cb66281dcff7493b4a82`
- aggregate JSON SHA256 `726d8d6fb608a77a2f832f487d32633e1ba1a3d2c8c497c1e5071d868ce9422b`
- durable result commit `e5eb0cbd49328e4e3ffcc604428af9b36c6295a2`

Classification:
`ITER081E_SM_ACTUAL_TOLLER_ONE_WEDGE_AND_NATURAL_TWO_WEDGE_HAN_BOUNDS_COUNTEREXAMPLES_REPRODUCED_EXACT_SCOPED`

Verdict: `PASS_EXACT_SCOPED`.

## Exact conclusions
For `j=k=1/2`, branch `+`, `m=+1/2`, arbitrary fixed `rho>0`, pure boost `beta>0`, BCG Eq. (46) gives exactly

`|t_+(beta)| = 1/[2(rho^2+1/4)sinh^2(beta)]`,

hence the projected selected branch is unbounded as `beta->0+` and violates the Han-type contraction on the frozen path.

For the preregistered natural two-wedge selected-branch term using both magnetic components,

`lim_{beta->0+} beta^4 tau_{++,2}(beta)=1/(rho^2+1/4)^2>0`,

so `|tau_{++,2}|` diverges and exceeds Han's standard `d_j^2=4` bound for sufficiently small positive beta.

The implementation derived both magnetic components from Eq. (46), verified the relevant hypergeometric parameter identities symbolically, passed exact rational-rho controls, and passed a bounded-surrogate negative control.

## Frontier update
The independent-Researcher-reproduction item in `status/CURRENT.md` is now closed positively. Do not spend further runs rechecking the same `j=1/2`, branch `+`, one-/two-wedge frozen paths unless an adversarial review identifies a concrete defect.

The highest-value Han/causal-stack successor is now genuinely new content: a prospectively frozen bounded/renormalized/branch-summed causal face functional or genuinely new primary authority. Such a candidate must specify branch rule, normalization, function/distribution space, source ordering, regulator relation, and its connection to the joint-K5 extension before any grand-canonical/RG promotion.

Independent K5 selector and causal E3/E4/E6 source-bridge fronts remain blocked and may be pursued in parallel only with genuinely stronger new input.

## Claim locks
No `NEW_PHYSICS_FOUND`; no complete-QG claim; no theorem that every causal face functional diverges; no unique K5 extension; no G3 PASS; no F9/G8/K5 promotion; no regulator-independence theorem.