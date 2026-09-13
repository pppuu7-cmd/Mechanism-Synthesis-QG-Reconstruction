# Iter076P preregistration — orientation-line descent of the homogeneous quadratic transport

Date: 2026-09-13

## Motivation

Iter076F/H established that the exact K4 cut-to-cycle isomorphism is not an ordinary S4 intertwiner: it is a unique sign-twisted Hodge/complement line, represented by `+H` or `-H`. Iter076J established the unsigned complementary-edge support from the gauge-fixed K5 source incidence. Iter076N then found no canonical exact amplitude-level S5-odd scalar that would select one global sign of this Hodge line at generic finite spin; only the non-degenerate Lorentzian Regge saddle locus has source-backed orientation selection.

However, Iter074A/076B isolate the first unresolved reduced overlap layer at homogeneous degree two. A global sign on a linear map can disappear after passing to the symmetric square. The exact question for this gate is therefore narrower than signed P3:

> Does the projective Hodge line `{+H,-H}` canonically induce an ordinary, sign-independent S4-covariant transport on homogeneous quadratic data?

If yes, the exact signed-P3 no-go does not by itself obstruct the homogeneous quadratic part of the reduced numerator/Jacobian jet. This would not define the full source-to-K4 coordinate pushforward, because a nonzero source one-jet or unknown nonlinear coordinate curvature can still feed degree two.

Iter076O remains `NOT_APPLICABLE_SOURCE_NATIVE` in the sense fixed by Iter076N; this gate is intentionally named Iter076P.

## Frozen objects

Use exactly the K4 oriented-edge conventions and exact integer/rational constructions already used in Iter076H:

- oriented edge space `E ~= Q^6`;
- incidence matrix `B`;
- cut space `C = im(B^T)`, dimension 3;
- cycle space `Z = ker(B)`, dimension 3;
- signed S4 edge action `R(pi)`;
- induced coordinate actions `C(pi)` and `Z(pi)`;
- tetrahedral complementary-edge Hodge operator
  `H e_ij = epsilon(i,j,k,l) e_kl`;
- coordinate map `X:C->Z` obtained by restricting `H` to the cut space and expressing the image in the frozen cycle basis.

No post-hoc basis fitting, metric insertion, source orientation convention, Levi-Civita projector in the physical amplitude, or semiclassical saddle input may be used.

For symmetric degree two use the frozen monomial basis

`(x0^2, x1^2, x2^2, x0*x1, x0*x2, x1*x2)`.

For a 3x3 matrix `A`, define `Sym2(A)` by exact polynomial substitution on this monomial basis.

## Frozen lanes and predicates

### Lane A — recover the Hodge line

- A0: `X` is exact and nonsingular.
- A1: for all 24 permutations `pi`,
  `Z(pi) X = sgn(pi) X C(pi)` exactly.
- A2: both representatives `+X` and `-X` are retained; no representative is declared physical.

### Lane B — sign descent on homogeneous quadratics

- B0: `Sym2(X) = Sym2(-X)` exactly.
- B1: `Sym2(X)` has rank 6.
- B2: `abs(det(Sym2(X))) = 1` in the frozen integer bases.
- B3: for a generic symbolic symmetric quadratic form `Q`,
  `X^T Q X = (-X)^T Q (-X)` identically.

### Lane C — untwisted S4 covariance after squaring

For all 24 permutations,

`Sym2(Z(pi)) Sym2(X) = Sym2(X) Sym2(C(pi))`

must hold exactly. No parity factor is allowed on the quadratic transport. A deliberately unsquared linear control must retain the parity twist on odd permutations.

### Lane D — scope firewall / odd-jet negative control

- D0: for a generic nonzero linear covector `l`, transport by `+X` and `-X` gives opposite linear forms; full first-order transport therefore does **not** descend through the Hodge line.
- D1: the absolute linear Jacobian is sign-independent: `|det X|=|det(-X)|`.
- D2: the implementation must state explicitly that an unknown nonlinear source-to-cycle map can mix a nonzero source one-jet into degree two; this gate does not resolve that contamination.
- D3: no physical source numerator/Jacobian coefficient, `epsilon^-1` value, generic finite-spin signed P3, G3, F9, G8 or K5 promotion is emitted.

## Pass classification

All lanes valid:

`ITER076P_HODGE_LINE_DESCENDS_TO_UNTWISTED_SYM2_QUADRATIC_TRANSPORT_EXACT_SCOPED`

## Fail classification

Any frozen algebraic predicate fails:

`ITER076P_ORIENTATION_LINE_QUADRATIC_DESCENT_FAIL`

## Scientific interpretation on PASS

A PASS establishes only that the global orientation sign is mathematically irrelevant for **homogeneous quadratic transport through the exact linear K4 Hodge line**. It narrows the source-to-K4 blocker: the remaining obstruction is not the sign of `H` on degree two itself, but provenance of the physical map together with possible odd/source-one-jet and nonlinear-coordinate contributions to the degree-two density.

The next admissible gate after a PASS is a prospective audit of whether the relevant source numerator/Haar-Jacobian **one-jet vanishes or is annihilated in the physical alternating/transitive channel**, sufficient to prevent nonlinear-map curvature from contaminating the quadratic coefficient. That audit must remain source-faithful and may not infer vanishing merely from the reduced denominator-skeleton cancellation of Iter074A.

## Claim lock

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no generic finite-spin signed P3; no physical causal-vertex finiteness/divergence theorem; no nominal `epsilon^-1` coefficient; no G3/F9/G8/K5 promotion. The published spectral `i epsilon` prescription is retained.