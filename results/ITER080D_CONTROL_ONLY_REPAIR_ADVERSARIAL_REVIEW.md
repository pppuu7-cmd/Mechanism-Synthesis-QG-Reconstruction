# Iter080D-SM control-only repair — adversarial implementation review

**Date:** 2026-09-14

## Object and chronology

Reviewed unchanged preregistration `a61780f9f84cf2ecff0e4a09993322f37e310d4c`, controlling prior invalidation `results/ITER080D_ADVERSARIAL_IMPLEMENTATION_REVIEW.md`, control-only repair plan commit `4039d69cd2e2e2da595a14e6a5f56f7d06f5e9b2`, repaired implementation/production head `31bc800aca1b8c6179b96eef0d0ec71b106dfe53`, terminal run `34830802802`, aggregate artifact `10342436008`, digest `sha256:731a83d348b89689fc51b22ce610b377079d6cc40617a8f87040054ca768bad4`.

The scientific object, selector class, criterion and claim ceiling are unchanged. Historical runs remain preserved and non-authoritative.

## Decisive implementation check

The prior defect was that Lane B labelled a finite grid of `(m,R)` instances as an arbitrary theorem. The repaired Lane B no longer uses numerical `(m,R)` enumeration for the universal success predicate. It represents affine expressions symbolically by coefficient triples in basis `[m,R,1]` and requires exact identities:

- `N=m+R-1 -> [1,1,-1]`;
- `dim W_N=N+1=m+R -> [1,1,0]`;
- `dim W_N-m=R -> [0,1,0]`.

PASS also requires the quantified certificate string `for every fixed finite integer m>=0 and every integer R>=1`, the frozen selector class `L:W->C^m`, and the frozen preregistration's universal-vs-selected-matrix implementation firewall. The aggregate independently refuses promotion if the Lane B symbolic certificate is missing/invalid or if its kernel lower-bound coefficients are not exactly `[0,1,0]`.

Therefore the repaired executable success condition now encodes the universal rank-nullity proof schema rather than inferring universality from sampled matrices.

## Source-lock hardening

Lane A computes the Git blob SHA-1 of the actually checked-out Iter077Q derivation and compares it to frozen blob `1b15464e8f7d5ae9d87932938f76de1ac8f3351f`. This addresses the optional hardening requested by the prior Critic review.

## Counterexample / scope checks

- A fixed finite-codomain injection is impossible by rank-nullity.
- Adding a kernel vector preserves all fixed finite scalar-linear conditions.
- Continuity assumptions are irrelevant to the algebraic theorem.
- A condition family whose codomain dimension grows with truncation can be injective and remains outside scope.
- Function-valued, differential, spectral, microlocal and nonlinear selectors remain outside scope and are not excluded.
- No distribution product, pullback, joint regulator, K4 surrogate, many-vertex inheritance, or RG claim enters this gate.

## Verdict

`CONFIRMED_SCOPED`

The repaired execution is authoritative for the frozen statement:

`ITER080D_SM_FIXED_FINITE_SCALAR_LINEAR_RENORMALIZATION_CONDITIONS_CANNOT_SELECT_ITER077Q_INFINITE_FUNCTION_SPACE_AMBIGUITY_EXACT_THEOREM_SCOPED`.

This does not establish a unique K5 extension. It removes the entire fixed-finite scalar-valued complex-linear selector class from consideration, while leaving genuinely function-valued/infinite, differential/spectral/microlocal, nonlinear, or source-derived correlated joint-K5 selectors open.

Claim locks remain unchanged: no `NEW_PHYSICS_FOUND`, no complete-QG claim, no physical causal-vertex finiteness/divergence theorem, no regulator-independence theorem, no G3 PASS, and no F9/G8/K5 promotion.
