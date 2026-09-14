# Iter080A-SM adversarial review — finite K5 permutation covariance

**Date:** 2026-09-14

## Reviewed result

Researcher result: `results/ITER080A_SM_K5_FINITE_PERMUTATION_SELECTOR_RESULT.md`, commit `4b5ed558225819e8eaf36798d15de7a007f39964`.

Researcher classification:
`ITER080A_SM_FINITE_K5_PERMUTATION_COVARIANCE_LEAVES_INFINITE_DIMENSIONAL_TANGENTIAL_EXTENSION_AMBIGUITY_EXACT_SCOPED`.

Researcher scientific verdict: `PASS_EXACT_SCOPED`.

Critic verdict: `CONFIRMED_SCOPED`.

## Frozen-contract audit

The prospective preregistration is commit `19f03d40929c7f7fc7aa9c82eed6485646028876`, followed by implementation `eaef2c647c338767622187b293b0b3f476b60103` and workflow/production head `431e3cc4056c06885cf0ba4c468ff886ba2bb9a3`. The authoritative run `34820372854` executed exactly at head `431e3cc4056c06885cf0ba4c468ff886ba2bb9a3`, completed successfully, and only afterward were the raw aggregate and durable result committed.

The frozen object is not the full causal vertex. It is the already-authorized Iter077Q tangential supported-extension ambiguity over the true common-collision manifold `N=SU(2)^4` after one K5 gauge fixing. The gate asks only whether finite K5 vertex relabeling covariance can by itself make that ambiguity unique or finite-dimensional.

The exact frozen witness is

`F(g_1,...,g_5)=sum_(a<b)|Tr(g_a^-1 g_b)|^2`.

On the frozen path `g_1=g_3=g_4=g_5=I`, `g_2=diag(e^{it},e^{-it})`, one obtains

`F(t)=24+16 cos^2(t)`.

The lane-C exact rational evaluation matrix for `1,F,...,F^12` at thirteen distinct frozen values has rank `13` over `Q`. This finite rank control is not extrapolated to infinity by itself: the analytic argument uses the fact that `F` takes the interval `[24,40]`, so a polynomial relation `P(F)=0` would force `P` to vanish identically.

The preregistration did not separately name a negative-control lane. That omission does not change the present verdict because the scientific conclusion is an exact algebraic/analytic implication, not an empirical sensitivity claim, and the decisive invariance/rank conditions were prospectively frozen. No post-hoc threshold, boundary state, regulator path, or PASS criterion was introduced.

## Implementation and Actions audit

Run `34820372854` is terminal `success`; all required jobs are terminal-successful: lane A `103900365276`, lane B `103900365214`, lane C `103900365168`, lane D `103900364995`, aggregate `103900533687`.

Aggregate artifact `10337479168` has digest `sha256:981c7a994ee481fbe3663c66054cfb1ea7a956933f4f5452f480c8cd1eb5dcce` and is tied to head `431e3cc4056c06885cf0ba4c468ff886ba2bb9a3`.

The aggregate Python script records `lane_B=True` structurally rather than enumerating permutations itself. This is not an execution defect because the workflow has a distinct required lane-B job that explicitly enumerates all `120` permutations of the ten unordered K5 pairs; the aggregate is gated by `needs: [lane-a,lane-b,lane-c,lane-d]`. Green CI alone is not used as the scientific proof.

Lane D checks the frozen interpretation-ceiling text rather than a physical observable. That is appropriate because D is an overclaim guard, not a physics computation.

## True-object and source-order audit

The witness is a smooth scalar function on the true tangential collision manifold, not a scalar K4/K5 incidence or Hodge surrogate. It is used only as a tangential multiplier of the already-established source-compatible Iter077Q supported ambiguity.

No reduction from the source Jacobian to a scalar graph surrogate occurs. No termwise `theta/delta/delta'` product or pullback is introduced. The source ordering remains

`one-wedge spectral/spinor integration -> Toller function -> ten-wedge product -> full boundary contraction -> K5 group integration / extension`.

The supported ambiguity is added only at the extension stage, after the off-collision source object is fixed.

## Independent analytic cross-check

The finite-permutation claim survives the main adversarial attacks:

1. **Gauge refixing after relabeling.** A relabeling that moves the gauge-fixed vertex is followed by a common-left refixing. Since `(h g_a)^-1(h g_b)=g_a^-1 g_b`, `F` is unchanged by the refixing.
2. **Alternative permutation character/sign assignment.** Multiplication by an invariant scalar preserves any already-existing covariant transformation law of the base ambiguity. A nontrivial finite-group character therefore does not make the invariant multiplier algebra finite-dimensional by itself.
3. **Exceptional support where `F` is constant.** The authorized Iter077Q ambiguity has a nonzero smooth tangential coefficient on an open set. `F` is real analytic and nonconstant on connected `SU(2)^4`; hence it cannot be constant on any nonempty open set. Therefore the powers remain linearly independent when applied to a nonzero authorized base ambiguity.
4. **Special-path artifact.** The one-parameter path is used only to prove global nonconstancy and interval-valued image. Global permutation/common-left invariance is an exact identity independent of that path.
5. **Special-spin or representative-boundary artifact.** Iter080A does not infer a new physical amplitude from one boundary component. The multiplier is boundary-state independent and acts on the already-authorized true-boundary-linear Iter077Q ambiguity sector.
6. **Regulator rescue.** No regulator is introduced, so no regulator path can be inferred to select the extension. A genuinely stronger source-derived regulator/analytic principle remains outside this gate and is not excluded.

No counterexample was found to the scoped proposition that finite K5 permutation covariance alone leaves an infinite-dimensional invariant tangential multiplier freedom.

## Distributional and normalization audit

`F^n` is smooth and bounded on compact `N`. Multiplying an order-zero supported ambiguity by such a tangential function preserves support on `N` and does not increase the transverse scaling degree. It therefore does not create a new illegal product/pullback operation.

The gate does not fix normalization, does not define a joint K5 boundary value, and does not select a unique extension. The published one-wedge spectral `i epsilon` remains a one-wedge prescription only.

## Boundary completeness audit

Read standalone, linear independence of the scalar functions `F^n` would only be a function-algebra statement. The physical relevance here depends on the already-authoritative Iter077Q base supported ambiguity and its true-boundary linearity. Under that dependency, multiplying by boundary-independent invariant `F^n` preserves the same boundary transformation law and yields the intended infinite family. The Researcher result explicitly keeps this dependency and does not promote the scalar witness into a full vertex by itself.

## Scope and novelty

The scientific conclusion is correct but intentionally narrow. Iter077Q had already proved the controlling stronger fact using the fully `S5`-invariant family generated by `Q^n`. Iter080A is therefore a second exact invariant-multiplier witness and robustness check, not a stronger dimensional theorem and not a new physical blocker.

No claim follows about stronger analyticity, positivity, causality, locality, composition, infinite-family consistency, source-derived normalization, regulator removal, E7/E8, G3, F9/G8/K5 promotion, physical RG, new physics, or complete quantum gravity.

## Critic verdict

`CONFIRMED_SCOPED`

The exact finite-permutation non-selection result is scientifically correct under its frozen Iter077Q dependency and interpretation ceiling. The result must continue to be read only as a statement about finite K5 relabeling covariance acting on the already-authorized tangential extension ambiguity.

## Authorized next gate

Do not spend another main gate on finite permutation symmetry or neighboring invariant-polynomial witnesses.

Highest information gain per cost is a single prospectively frozen generalized-causal primary-source bridge audit that jointly tests E3/E4/E6 inheritance as a complete many-vertex causal prescription using the already validated KKL/BCG/Beltrán source corpus. This gate may clarify composition authority but must preserve the independent local K5 extension-selector blocker and may not promote E7/E8 or G3 unless an actual composed source-faithful functional exists.

A K5 selector successor is admissible only if a genuinely stronger, independently motivated, source-compatible selection principle is identified prospectively and acts on the full Iter077Q function space; another finite-symmetry restatement is not authorized.
