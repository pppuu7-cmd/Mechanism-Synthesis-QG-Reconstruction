# Iter081D Critic orthogonal exact control — actual two-wedge Toller branch face vs Han bound

Status: **exact Critic control following prospective object freeze; not a Researcher-A verdict.**
Date: 2026-09-14
Prospective object freeze: `results/ITER081D_PRE_GATE_ACTUAL_TOLLER_TWO_WEDGE_FACE.md`, commit `f90129012da85854afff416c66de7d6bf5ca9819`.

## Frozen source formula
Use BCG arXiv:2604.24945v1 Eq. (46) at `j=k=1/2`, arbitrary fixed real `rho>0`, branch `+`, pure boost `g_beta=exp(-i beta K_z)`, `beta>0`.

For `m=+1/2`, the exact simplification already frozen in Iter081C gives

`t_+(beta) := t_{1/2,1/2,+1/2}^{(+,rho,1/2)}(beta)
 = -[2/D] exp[-(2-i rho) beta]/(1-exp(-2 beta))^2`,

where `D=rho^2+1/4`.

For `m=-1/2`, Eq. (46) has
`a=1`, `b=3/2-i rho`, `c=1/2-i rho`, so `b=c+1`. The exact series identity

`2F1(1,c+1;c;z)=1/(1-z)+z/[c(1-z)^2]=[c+(1-c)z]/[c(1-z)^2]`

holds for `z=exp(-2 beta) in (0,1)`. Gamma recurrence gives
`2 Gamma(1/2+i rho)/Gamma(3/2+i rho)=2/(1/2+i rho)`. Hence

`t_-(beta) := t_{1/2,1/2,-1/2}^{(+,rho,1/2)}(beta)
 = [2/D] exp[-(1-i rho) beta]
   *[(1/2-i rho)+(1/2+i rho)exp(-2 beta)]/(1-exp(-2 beta))^2`.

## Exact small-beta coefficients
Direct one-sided expansion from these exact expressions gives

`lim_{beta->0+} beta^2 t_+(beta) = -1/(2D)`,

`lim_{beta->0+} beta^2 t_-(beta) = +1/(2D)`.

Thus the leading singularities would cancel in the **linear** magnetic trace, which is precisely why the two-wedge control was prospectively frozen instead of inferring a face result from one matrix element.

## Two-wedge natural branch face term
For two identical pure-boost wedge factors and branch assignment `(+,+)`, the projected matrices are diagonal and

`tau_{++,2}(beta)=2[(t_+(beta))^2+(t_-(beta))^2]`.

Therefore

`lim_{beta->0+} beta^4 tau_{++,2}(beta)
 = 2[(1/(2D))^2+(1/(2D))^2]
 = 1/D^2
 = 16/(4 rho^2+1)^2 > 0`.

Hence

`tau_{++,2}(beta) ~ [1/(rho^2+1/4)^2] beta^(-4)`

and in particular

`|tau_{++,2}(beta)| -> infinity` as `beta->0+`.

Since `d_j=2`, Han's comparison bound is `d_j^2=4`. Consequently there exists `beta_0(rho)>0` such that every `0<beta<beta_0(rho)` satisfies

`|tau_{++,2}(beta)|>4`.

## Classification of this Critic control
`ACTUAL_TWO_WEDGE_TOLLER_FACE_BOUND_COUNTEREXAMPLE`.

This is an actual gamma-simple Toller-formula counterexample for the prospectively frozen natural branch face term. It is stronger than the Iter081B abstract additive witness and stronger than the Iter081C single-matrix-element operator-norm obstruction: magnetic-index cancellation does not restore Han's same `d^2` face bound for the frozen two-wedge `(+,+)` term.

## Scope / anti-overclaim
This does **not** promote `tau_{++,2}` to a source-authorized complete causal Han-stack amplitude. It proves that the most direct algebraic branch term obtained from Han's face formula by replacing both Wigner factors with actual BCG `T^+` factors cannot obey Han's original uniform `d^2` bound on this admissible pure-boost path. It does not prove:
- every branch assignment or face length violates every possible alternative bound;
- no cancellation can occur in a separately defined causal sum over branch assignments;
- no subtraction/renormalization/new causal face functional can be constructed;
- a complete causal multivertex stack diverges;
- a K5 distributional extension is selected or ruled out;
- regulator independence, E7/E8, G3, F9/G8/K5 promotion, GR recovery or new physics.

## Consequence for the research front
If independently reproduced by Researcher A, the original Han pole/condensation mechanism cannot be ported to this natural causal branch face term with the same single-face bound and saturation theorem. Any surviving causal Han-style stack requires genuinely new mathematics: a different causal face functional, a renormalized/subtracted quantity, a branch-summed construction with a proved bound, or new primary authority. Such a modification is new model/theorem content and must be prospectively frozen.