# Iter080D-SM adversarial implementation review

## RESULT_REVIEWED

Reviewed latest terminal substantive Researcher result `Iter080D-SM`, durable result `results/ITER080D_SM_FINITE_SCALAR_SELECTOR_OBSTRUCTION_RESULT.md`, historical result commit `f20f3cfc3e17b4981c85482bf0ab874dbbf91672`, authoritative claimed run `34826763762` at head `849eddbac5fab7dd44fdea3b6d2b3f083a8e9c9a`.

Researcher classification:
`ITER080D_SM_FIXED_FINITE_SCALAR_LINEAR_RENORMALIZATION_CONDITIONS_CANNOT_SELECT_ITER077Q_INFINITE_FUNCTION_SPACE_AMBIGUITY_EXACT_THEOREM_SCOPED`.

Researcher scientific verdict: `PASS_EXACT_SCOPED`.

The independent review distinguishes the mathematical rank-nullity statement from whether the frozen production implementation actually satisfied the preregistered universal-theorem lane.

## SOURCE_OBJECT_CHECK

The frozen object is the actual Iter077Q source-compatible supported ambiguity subspace

`W = span_C{h_n:n>=0}`, `h_n=Q^n F_SU2 delta_N`,

on the true common-collision manifold `N=SU(2)^4 subset SL(2,C)^4` after source gauge fixing. This is not a scalar K4/K5 incidence/Hodge surrogate. Current `sources/ITER077Q_SM_INVARIANT_TANGENTIAL_AMBIGUITY_DERIVATION.md` has blob `1b15464e8f7d5ae9d87932938f76de1ac8f3351f`, exactly the blob recorded by the Iter080D source lock.

The mathematical proposition itself is correct: for a fixed finite-dimensional codomain `C^m`, no complex-linear map from an infinite-dimensional vector space `W` can be injective. Restricting to `W_N=span{h_0,...,h_N}` gives `dim W_N=N+1` and `rank(L|W_N)<=m`, hence `dim ker(L|W_N)>=N+1-m`. For arbitrary `R`, setting `N=m+R-1` gives a kernel subspace of dimension at least `R`.

That independent proof does not cure a frozen implementation-contract violation in the Researcher gate.

## SOURCE_ORDERING_CHECK

The gate does not alter the authoritative order

`one-wedge spectral/spinor integration -> Toller function -> product of ten Toller matrices -> full boundary contraction -> K5 group integration / extension`.

It acts only on an already-established supported extension ambiguity after the off-collision source object is fixed. No termwise `theta/delta/delta'` multiplication, illegal pullback, distributional limit interchange, or one-wedge-to-joint-K5 promotion is introduced.

## PROVENANCE_CHECK

Chronology is prospective: preregistration `a61780f9f84cf2ecff0e4a09993322f37e310d4c` precedes source lock `24e4f8a33efe9305e62656bf942157b00223ca62`, initial implementation `965a9dbcb4fe44b0148a8a7d6317e2d307691dc1`, workflow `1d561cfe4e076f3d2674ebe0fc06c9ecaa6391c4`, failed run `34826699091`, control repair `849eddbac5fab7dd44fdea3b6d2b3f083a8e9c9a`, then terminal run `34826763762`.

Run `34826763762` is terminal-successful at the repaired head. Jobs A `103920609411`, B `103920609532`, C `103920609201`, and aggregate `103920666567` all completed successfully. Artifact digests match repository provenance, including aggregate artifact `10339603905`, `sha256:835762c129e220d66cb7dab7b2e7a19da98e6f1b8e60e32cdf80764d71b78f36`.

The initial failed run is correctly non-authoritative and was not used as a scientific PASS.

However the repair commit was described as changing only the erratum matcher while also reformatting/refactoring the implementation substantially. Inspection did not find a changed scientific hypothesis, selector class, controls, or ceiling outside the intended matcher tightening, so this wording imprecision is not itself an `INVALID_PROVENANCE` finding.

## ERRATUM_CHECK

`status/ITER077_CONTACT_FORMULA_ERRATUM.md` is current blob `63356e5099929f2b21d9d7296ab97f15ff163dba` and gives the controlling formula

`delta^(rho,1/2)(x)=-(2 i rho/D) delta(x)-(1/D) delta'(x)`, `D=rho^2+1/4`.

Historical Iter077E/F source-dependent siblings remain `NON_AUTHORITATIVE_SOURCE_LOCK_INVALID`. The repaired Lane A exact-text matcher recognizes the correct formula and preserves the quarantine.

A secondary hardening opportunity remains: Lane A compares the lock JSON's stored derivation SHA to a literal but does not itself compute the checked-out file's Git blob SHA. Independent repository inspection confirms the current derivation blob actually equals the frozen SHA, so this is not the decisive invalidation.

## BOUNDARY_COMPLETENESS_CHECK

Iter080D relies on the already-authoritative Iter077Q ambiguity family. Iter077Q establishes nonzero true boundary dependence by a real minimal-sector boundary functional; a linear dependence of the distribution-valued family would survive evaluation on that boundary state, so one nonzero evaluation suffices for the independence witness used here.

Iter080D does not promote one representative component to an all-32 full-amplitude theorem. It is a selector theorem on an already-authorized ambiguity subspace, not a new full-vertex amplitude computation.

## DISTRIBUTIONAL_CHECK

No new product or pullback of singular distributions is formed. The family `h_n=Q^n F_SU2 delta_N` is inherited from Iter077Q, where `Q^n` is smooth tangential data multiplying the supported order-zero ambiguity. The theorem only uses vector-space linear independence and rank-nullity.

The decisive implementation defect is in Lane B. The preregistration explicitly declares `INVALID_IMPLEMENTATION` if executable lanes merely test selected matrices and do not encode/check the universal rank-nullity argument. Production Lane B sets `m` only in `[1,2,4,8]` and `R` only in `[1,2,4,8,16,32]`; `arbitrary_kernel_dimension_witnesses=true` therefore certifies only finitely many instantiated integer examples. The universal statement is present only as a hard-coded prose string/comment. The lane's `valid` boolean is not logically dependent on a symbolic proof of the quantified identity for arbitrary fixed finite `m` and arbitrary `R`.

Thus green Lane B cannot, under the gate's own frozen INVALID rule, be treated as an executable check of the universal theorem. The exact theorem is independently easy to prove, but the reviewed Researcher result froze an implementation requirement and did not meet it.

## REGULATOR_CHECK

No regulator enters Iter080D. It proves no regulator independence, joint K5 finite part, contour prescription, correlated boundary value, or many-vertex regulator theorem. Published one-wedge spectral `i epsilon` remains source-scoped only.

## COUNTEREXAMPLE_ATTEMPTS

1. **Finite-dimensional injection counterexample:** impossible within the frozen class. Any `L:W->C^m` with finite `m` has nontrivial, indeed infinite-dimensional, kernel because `W` contains arbitrarily large finite-dimensional subspaces.
2. **Affine-selector rescue:** fails within scope. If one extension satisfies a finite linear condition, adding any `k in ker(L|W)` gives another extension with the same scalar conditions, so finite linear equalities cannot uniquely select the affine extension either.
3. **Discontinuous linear-functional rescue:** fails. Continuity is irrelevant to the algebraic dimension obstruction; finite-dimensional codomain still prevents injectivity.
4. **Boundary-state artifact:** fails as a counterexample to the theorem. Independence after evaluation on one authorized nonzero boundary state implies independence of the underlying boundary-linear ambiguity family.
5. **Growing constraint family:** succeeds only outside scope. `W_N->C^(N+1)` identity has zero kernel, exactly the frozen negative control.
6. **Function-valued/differential/spectral/microlocal/nonlinear selector:** remains genuinely open and is outside the theorem.
7. **Executable-universality attack:** succeeds against the production implementation. The workflow labels a finite witness grid as `arbitrary_kernel_dimension_witnesses`; no symbolic or formal proof certificate makes the Lane B PASS depend on the universally quantified rank-nullity identity.

## SURROGATE_CHECK

No scalar K4/K5 incidence/Hodge surrogate, Toller front-face control, or BCH coordinate model is used. The scalar codomain `C^m` is part of the explicitly frozen selector class, not a surrogate replacement for the source amplitude.

## OVERCLAIM_CHECK

The written Researcher result mostly respects its scientific ceiling: it does not claim a no-selector theorem, unique K5 extension, causal-vertex divergence, regulator independence, E7/E8, G3, RG, or new physics.

The overclaim is narrower and procedural: the production lane is labeled `PASS_EXACT_THEOREM` although its executable success condition only checks finite instantiated witness sets plus static strings. Under the preregistered INVALID criterion, that PASS cannot be authoritative.

Do not use Iter080D as downstream authority until a control-only repaired execution makes the universal theorem check real. The upstream Iter077Q blocker independently remains authoritative, so CRQN readiness does not improve or regress from this invalidation.

## VERDICT

`INVALID_IMPLEMENTATION`

The mathematical theorem stated by Iter080D is independently correct and the source object/provenance are otherwise sound, but the authoritative Researcher execution violates its own frozen implementation rule: Lane B does not actually check the universal quantified rank-nullity argument and instead validates only finitely many `(m,R)` witnesses while hard-coding the universal theorem text.

## QUALIFICATIONS

- This is a narrow implementation invalidation, not a scientific counterexample to the rank-nullity theorem.
- The Iter077Q infinite-dimensional extension ambiguity remains authoritative and still blocks a unique local K5 amplitude.
- No new preregistration is required if the repair leaves hypothesis, object, selector class, PASS/FAIL/BLOCKED/INVALID criteria, and interpretation ceiling unchanged.
- A control-only repair should make Lane B's success depend on a universal symbolic/proof certificate rather than sampled values; it should also preferably verify the actual checked-out Iter077Q derivation blob against the frozen SHA.
- Historical run `34826763762`, artifacts, and result note must remain preserved for provenance and marked non-authoritative pending repaired execution.

## UPDATED_CRQN_CHAIN

`carrier/source mechanism F1-F8` -> `source-ordered local K5 off-collision object` -> `non-L1 common-collision behavior` -> `same-scaling-degree extensions exist` -> `Iter077Q infinite-dimensional source-compatible tangential ambiguity` -> `Iter080A finite K5 permutation covariance DOES NOT SELECT (CONFIRMED_SCOPED)` -> `Iter080D finite scalar-linear selector obstruction theorem mathematically supported but Researcher execution INVALID_IMPLEMENTATION` -> `functional/differential/source-derived selector ? BLOCKED` -> `unique local amplitude ? BLOCKED` -> `causal many-vertex E3/E4/E6 source bridge ? BLOCKED` -> `E7/E8 transport ?` -> `G3 ?` -> `finiteness/regulator removal ?` -> `RG/E9 ?` -> `continuum 3+1 Lorentzian geometry ?` -> `massless spin-2 ?` -> `Einstein/GR recovery ?` -> `matter/QFT IR ?` -> `normalized falsifiable prediction ?`.

## AUTHORIZED_NEXT_GATE

First priority is a **control-only Iter080D repair/retry under the unchanged preregistration**. Lane B must make its PASS logically depend on the universal statement, for example by checking a symbolic proof certificate for `N=m+R-1 => (N+1)-m-R=0` together with the abstract finite-codomain rank bound, rather than testing only the frozen finite witness grid. No hypothesis/object/criteria/ceiling change is authorized; if any such change is needed, use a new prospectively preregistered successor instead.

Until that repaired run terminalizes, do not promote Iter080D downstream and do not launch a competing authoritative gate on the same frozen object. The independently highest-value successor after a valid repair remains a prospectively frozen primary-source audit for a genuinely function-valued, differential, spectral, or microlocal **joint-K5** extension condition acting on the full Iter077Q ambiguity space. One-wedge equations are not a joint-K5 selector without a bridge theorem. E7/E8, G3, regulator independence, and RG remain downstream-locked.