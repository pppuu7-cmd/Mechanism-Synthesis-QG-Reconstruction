# Iter076R preregistration — symmetry-allowed quadratic curvature and one-jet contamination of transitive faces

Date: 2026-09-13

## Status of this preregistration

This is a **confirmatory production preregistration after an exploratory exact-algebra derivation**. The exploratory derivation was used only to choose and freeze the predictions below. No production Iter076R implementation, workflow result, or artifact has been viewed at the time of this commit. The production code must independently reconstruct the objects from the committed Iter076H/Q and Iter073/076B definitions.

## Motivation

Iter076Q established that the unresolved global sign of the exact linear Hodge line disappears on homogeneous quadratic transport. The remaining danger is coordinate curvature: if a source-to-cycle map has

`z = X c + B(c,c) + O(c^3)`

and the source density has a nonzero one-jet `ell(c)`, then the inverse coordinate change can feed `ell` into the degree-two density.

Before computing any physical source one-jet, test whether symmetry forces this mechanism to vanish. If no symmetry-compatible `B` exists, or if every induced quadratic contamination vanishes on the exact Iter076B transitive proper-face restriction complex, a source one-jet audit can be bypassed. If the contamination survives, a source-faithful one-jet audit is genuinely required.

## Frozen objects and conventions

Use exactly the committed conventions of:

- Iter076Q: K4 cut space `C`, cycle space `Z`, signed S4 actions, Hodge coordinate map `X`, and degree-two monomial order `(x0^2,x1^2,x2^2,x0*x1,x0*x2,x1*x2)`;
- Iter073A/D: transitive causal classes `['++++','+++-','++--','+---']`, tree bases `['S0','S1','P0','P1']`, and the six proper transitive faces per class/tree;
- Iter076B: exact quadratic restriction matrix convention with pair order `[(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]`.

For a quadratic curvature matrix `B` with three output coordinates and six degree-two input monomials, impose the same twisted covariance as the linear Hodge map:

`B Sym2(C(pi)) = sgn(pi) Z(pi) B`

for all 24 permutations.

No physical `B` is selected by this gate. The unique algebraic line, if present, is only the symmetry-allowed curvature line.

## Exploratory predictions frozen for production confirmation

With primitive normalization (first nonzero integer entry positive), the predicted curvature generator is

`B0 = [[ 1, 0, 0,-1,-1, 0],
       [-1, 0, 1, 1, 0,-1],
       [ 1,-1, 0, 0,-1, 1]]`.

Using `z = X c + B0(c,c) + O(c^3)` and the quadratic inverse correction

`c = X^{-1} z - X^{-1} B0(X^{-1}z,X^{-1}z) + O(z^3)`, 

a generic source covector `ell` induces a quadratic contamination. In the Iter076B quadratic coefficient order, the predicted coefficient map `T: ell -> q_ell` is

`T0 = [[-1,-1,-1],
       [-1,-1, 0],
       [ 1, 0, 1],
       [ 0, 0, 1],
       [ 0, 1, 1],
       [ 0, 1, 0]]`.

Overall nonzero rescaling of `B0` rescales `T0` and does not change any rank or survival predicate.

## Frozen lanes

### Lane A — twisted quadratic-curvature Hom space

Reconstruct all 18 linear covariance equations over exact rationals.

PASS iff:

- the covariance system has rank 17;
- its nullspace has dimension exactly 1;
- `B0` spans the nullspace (up to a nonzero rational scalar);
- the zero-curvature matrix is retained as a separate negative/control possibility and no physical nonzero curvature is asserted.

### Lane B — inverse-map one-jet contamination

Using the primitive generator from Lane A and the exact Iter076Q `X`, derive the inverse-map quadratic correction symbolically.

PASS iff:

- the induced coefficient map has rank exactly 3;
- it agrees with `T0` up to the same overall generator scale;
- setting `B=0` gives identically zero induced quadratic contamination;
- no assumption is made about the actual physical value of the source one-jet.

### Lane C — exact transitive-face survival

For each of 4 transitive causal classes, 4 frozen tree bases, and 6 proper faces, transport `T` to the tree cycle coordinates and apply the exact Iter076B quadratic restriction matrix.

There are `4*4*6 = 96` face restrictions.

PASS iff the frozen exploratory prediction is reproduced exactly:

- `32/96` restrictions have rank 1;
- `64/96` restrictions have rank 0;
- every class/tree lane has rank multiset `[1,1,0,0,0,0]`;
- stacking all six proper-face restrictions in each class/tree gives rank exactly 2;
- stacking all transitive classes/tree bases gives rank exactly 3, so no nonzero generic one-jet direction is globally invisible across the full transitive family.

The per-class one-dimensional invisible direction may be reported, but is not promoted to a physical one-jet selection rule.

### Lane D — controls and scope firewall

PASS iff:

- the `B=0` control gives zero face contamination everywhere;
- a deliberately altered curvature matrix outside the one-dimensional covariance line fails the exact twisted covariance test;
- the aggregate explicitly records:
  - `physical_quadratic_curvature_selected = false`;
  - `physical_source_one_jet_established = false`;
  - `one_jet_can_be_bypassed_by_symmetry = false` on a successful survival result;
  - `epsilon_minus1_coefficient_established = false`;
  - `generic_finite_spin_signed_P3_promoted = false`;
  - no G3/F9/G8/K5 promotion.

## Frozen classification on confirmation

If A-D all pass with the predicted survival pattern:

`ITER076R_UNIQUE_TWISTED_QUADRATIC_CURVATURE_ALLOWS_ONEJET_CONTAMINATION_ON_TRANSITIVE_FACES_EXACT_SCOPED`

Scientific meaning: symmetry does **not** eliminate nonlinear-map contamination of the homogeneous degree-two layer. A source-faithful audit of the relevant one-jet is therefore necessary unless a stronger source mechanism annihilates it.

## Failure classification

Any frozen algebraic, basis-transport, or control predicate fails:

`ITER076R_QUADRATIC_CURVATURE_ONEJET_CONTAMINATION_CONFIRMATION_FAIL`

A failure means the exploratory derivation must be reviewed; it is not a physical finiteness/divergence statement.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no physical source-to-K4 map; no assertion that the physical curvature is nonzero; no assertion that the physical source one-jet is nonzero; no nominal `epsilon^-1` coefficient; no causal-vertex finiteness/divergence theorem; no G3/F9/G8/K5 promotion.