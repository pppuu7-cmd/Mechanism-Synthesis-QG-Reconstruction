# Iter080D-SM control-only universal theorem repair — terminal result

**Date:** 2026-09-14

## Provenance

- Unchanged prospective preregistration: `a61780f9f84cf2ecff0e4a09993322f37e310d4c`.
- Historical invalid implementation remains preserved and non-authoritative.
- Control-only repair plan commit: `4039d69cd2e2e2da595a14e6a5f56f7d06f5e9b2`.
- Repaired implementation / production head: `31bc800aca1b8c6179b96eef0d0ec71b106dfe53`.
- Authoritative repaired run: `34830802802`.
- Jobs: lane A `103933439707`, lane B `103933439970`, lane C `103933440040`, aggregate `103933485071`.
- Aggregate artifact: `10342436008`.
- Aggregate digest: `sha256:731a83d348b89689fc51b22ce610b377079d6cc40617a8f87040054ca768bad4`.

All three lanes and aggregate completed successfully. Green CI is execution evidence only; scientific promotion below follows the unchanged frozen contract plus the repaired executable universal certificate.

## Repair validation

Lane A now computes the actual Git blob SHA-1 of the checked-out `sources/ITER077Q_SM_INVARIANT_TANGENTIAL_AMBIGUITY_DERIVATION.md` and requires equality with the frozen source-lock blob SHA `1b15464e8f7d5ae9d87932938f76de1ac8f3351f`.

Lane B PASS no longer depends on a finite grid of `(m,R)` examples. It encodes exact affine symbolic expressions in the basis `[m,R,1]` and makes PASS depend on the identities

- `N = m + R - 1`, coefficients `[1,1,-1]`;
- `dim W_N = N + 1 = m + R`, coefficients `[1,1,0]`;
- `rank(L|W_N) <= dim C^m = m`;
- `dim ker(L|W_N) >= dim W_N - m = R`, coefficients `[0,1,0]`.

The certificate is quantified for every fixed finite integer `m>=0` and every integer `R>=1`; no selected numerical `m,R` instantiation is used to certify universality. Frozen finite projection examples remain controls only.

Lane C retains the unchanged scope controls, including the growing-condition-family negative control and explicit exclusions of function-valued, differential/spectral/microlocal and nonlinear selector classes.

## Terminal classification

`ITER080D_SM_FIXED_FINITE_SCALAR_LINEAR_RENORMALIZATION_CONDITIONS_CANNOT_SELECT_ITER077Q_INFINITE_FUNCTION_SPACE_AMBIGUITY_EXACT_THEOREM_SCOPED`

Verdict: `PASS_EXACT_SCOPED`.

For the authoritative Iter077Q ambiguity space `W=span_C{h_n:n>=0}`, every selector consisting of a fixed finite number of scalar-valued complex-linear conditions `L:W->C^m` has an infinite-dimensional kernel. For arbitrary `R>=1`, restriction to `W_N=span{h_0,...,h_N}` with `N=m+R-1` gives `dim W_N=m+R`; since rank is at most `m`, rank-nullity gives kernel dimension at least `R`. Since `R` is arbitrary, such an `L` cannot be injective and cannot uniquely select the K5 extension.

## Scope / claim ceiling

This result excludes only a fixed finite family of scalar-valued complex-linear renormalization/selection conditions. It does **not** exclude function-valued or infinite condition families, differential/spectral/microlocal equations, nonlinear selectors, or a genuinely source-derived joint-K5 extension prescription. It does not prove a unique K5 extension, physical causal-vertex finiteness/divergence, regulator independence, E7/E8, G3, RG, F9/G8/K5 promotion, complete quantum gravity, or new physics.

## Next admissible front

Do not repeat finite permutation symmetry, invariant-polynomial multipliers, fixed finite scalar counterterm/normalization examples, larger-V gauge-orbit counting, or the already-closed KKL/BCG/Beltrán E3/E4/E6 corpus scan. The next high-value gate is a prospectively frozen primary-source audit for a genuinely function-valued, differential, spectral, or microlocal **joint-K5 extension condition** acting on the full Iter077Q tangential ambiguity space. One-wedge equations or representation identities do not qualify without a theorem bridging them to the correlated joint-K5 extension problem.
