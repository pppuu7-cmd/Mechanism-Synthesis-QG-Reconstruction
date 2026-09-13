# Source/derived supplement — causal contact terms and true B-map pullback criterion

**Date:** 2026-09-14

## Primary source facts

Primary authority: E. Bianchi, C. Chen, M. Gamonal, **“Causal spinfoam vertex for 4d Lorentzian quantum gravity”**, arXiv:2601.23162 / Phys. Rev. D 113, 126020 (2026).

In the coherent representation, each of the ten wedge Toller factors contains the source distributional factor

`theta(kappa B) + kappa delta^(rho,j)(B)`

with

`B(z,g)=log(<g^dagger z|g^dagger z>/<z|z>)`.

The distribution supported at `B=0` is a finite linear combination of delta derivatives,

`delta^(rho,j)(x) = sum_{n=0}^{2j} [c_n^(rho,j)/(n+1)!] (-1)^(n+1) d^n/dx^n delta(x)`.

At `n=0`, the defining gamma-ratio coefficient is evaluated at equal spectral parameters and is exactly

`c_0^(rho,j)=1`.

Therefore every `delta^(rho,j)` contains the nonzero ordinary point-contact component

`-delta(x)`.

Across all ten wedges, the product of the ten source factors consequently contains a nonzero pure point-contact monomial proportional to

`delta(B_01) delta(B_02) ... delta(B_34)`.

This statement concerns the exact source decomposition before any attempt to pull the ten-variable distribution back through the nonlinear source map.

## Point-contact wavefront fact

For the one-dimensional point distribution, with any standard Fourier convention,

`F[d^n delta/dx^n](xi)`

is a nonzero constant multiple of `(i xi)^n`.

Hence a nonzero finite point-supported distribution has polynomial Fourier transform and is not rapidly decreasing in either cotangent direction. In particular,

`WF(delta) = {(0,xi): xi != 0}`.

Likewise the ten-dimensional point distribution

`Delta_10(B)=prod_e delta(B_e)`

has the full nonzero cotangent fibre at `B=0` in its wavefront set.

This is a standard distribution-theory fact and is used only as a microlocal admissibility test; it is not a statement about the value of the full causal vertex.

## Pullback criterion

For a smooth map `f:X->Y`, the standard Hörmander pullback theorem canonically defines `f^*u` when the wavefront set of `u` avoids the normal set

`N_f = {(f(x),eta): (df_x)^T eta = 0}`

away from the zero covector.

In particular, if `f` is a submersion, `(df_x)^T` is injective and `N_f` has no nonzero target covector, so the standard pullback exists locally for every distribution on `Y`.

Failure of the wavefront/normal-set disjointness condition is **not** a theorem that no pullback can exist by any source-selected boundary-value prescription. It means only that the standard canonical Hörmander pullback theorem does not authorize that pullback there.

## Application to the true causal-vertex source map

The relevant map at the common group collision is the true ten-component coherent-spinor map

`B : SL(2,C)^4 x (CP^1)^10 -> R^10`,

whose boost differential is

`J_(ab),(c,i)=(delta_ac-delta_bc)n_ab^i`.

`Iter077A-SM` proves an exact rank-10 witness, so the true map is a submersion on an open neighborhood of that witness. The generic full-rank region therefore has no first-order Hörmander pullback obstruction.

`Iter077C-SM` freezes a full-span rank-9 witness

`xxxxxyyyzz`

with nonzero left-null/self-stress covector

`lambda=(1,-1,0,0,1,0,0,0,0,0)`,

so

`J^T lambda = 0`.

Because the pure ten-contact source monomial `Delta_10(B)` has every nonzero target covector in its wavefront set at the origin, this exact `lambda` belongs simultaneously to the target wavefront fibre and the normal set of the rank-9 source map. Thus the standard Hörmander pullback criterion fails for that source contact monomial at the frozen exceptional point.

## Role of the exact second jet

`Iter077D-SM` proves that this rank-9 point is not higher-order flat in the full source-variable space: the self-stress contraction has a nondegenerate mixed six-dimensional quadratic normal form with determinant `-1` and inertia `(3+,3-)`.

That second-jet result is the correct input for a subsequent **source-selected boundary-value/scaling** analysis, but it does not repair the hypotheses of the first-order canonical pullback theorem. A nonlinear critical pullback must therefore be treated as a separate distributional extension/boundary-value problem.

## Published i-epsilon selector firewall

The companion 2026 Toller analysis derives the causal branches from the spectral Feynman `i epsilon` prescription and identifies the branch projections by the corresponding boundary-value/Sokhotski-Plemelj structure. This supplies a source-selected prescription to investigate next and forbids replacing the exceptional pullback by an arbitrary fitted finite part.

It does **not** by itself establish the correlated ten-wedge K5 boundary value after all shared group and spinor variables are coupled.

## Exact scoped conclusion available to the next gate

The admissible split is:

- generic rank-10 source region: standard local distribution pullback is authorized by submersion;
- frozen rank-9 exceptional source point: the pure ten-contact source summand violates the standard Hörmander wavefront/normal-set disjointness condition;
- therefore a global K5 existence theorem cannot be assembled solely from generic transversality and termwise canonical pullbacks;
- a correlated source-selected boundary-value/extension analysis is required on the exceptional set.

## Claim locks

No claim that the full source-selected causal amplitude does not exist; no causal-vertex finiteness/divergence theorem; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal `epsilon^-1` coefficient; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; no arbitrary finite part; retain the published spectral `i epsilon`.