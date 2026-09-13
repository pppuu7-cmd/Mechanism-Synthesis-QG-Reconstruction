# Iter076T result — naive Toller identity one-jet is singular; pole-stripped Barrett-Crane branch has generic nonzero one-jet

**Date:** 2026-09-13

## Authority

- source supplement: `802853169630bc4ea748cf0ffca50bae6d0735d9`
- prospective preregistration: `e61ccd6d83cc20ac6abcbc77f27c5914927fca01`
- initial implementation: `6f557dfce73eec477d77600097eed29b07f2a1d7`
- workflow head: `fd928d59f1b4d0528e76aaaadedcdbfc36662f10`
- control-only exponential canonicalization repair: `e27da85bb0a10af0d348551f9250c07d6cadaf40`
- authoritative run: `34782925764`
- jobs: A `103793090420`, B `103793090454`, C `103793090402`, D `103793090449`, aggregate `103793128359`

Artifacts:

- A: `10325398247`, digest `sha256:1c6c152f46583b4ab107d895b7e63a469952ef031641d0d0d05cdd456c5bc270`
- B: `10326110074`, digest `sha256:4191c097555e56cd3422e9cae8d9d1d6d9514b7eb2a7eb709e93772e529a3493`
- C: `10325048412`, digest `sha256:7ba33b63e0b1c76644a4dbb24eb9e70de1a83fdce325b056782d95d3f335d6ef`
- D: `10324778851`, digest `sha256:cb2ccfce55e21ff77f636f7f50afdcb8040f78d0655ea8cc2bc918e8440c462e`
- aggregate: `10325830790`, digest `sha256:82cea03755a4050b35245a05fd1ff58866d0fca56733a5c0ec6dc31f51a2aed8`

The first run exposed only a symbolic canonicalization deficiency in the exact additive-identity check: SymPy did not automatically rewrite the exponential difference as a sine. The repair changed only the normalization used by `exact_zero`; no frozen scientific predicate, formula, threshold, or interpretation changed. The authoritative rerun passes all A/B/C/D lanes and aggregate.

## Frozen classification

`ITER076T_NAIVE_TOLLER_IDENTITY_ONEJET_SINGULAR_POLE_STRIPPED_BC_BRANCH_HAS_GENERIC_NONZERO_ONEJET_EXACT_SCOPED`

## Exact facts

1. The source additive relation `T^(+)+T^(-)=D` and second-kind / positive-negative frequency character are locked from the primary-source supplement.
2. In the exact Barrett-Crane control,

   `t_+(beta)=+(1/(2 i rho)) exp(+i rho beta)/sinh(beta)`,

   `t_-(beta)=-(1/(2 i rho)) exp(-i rho beta)/sinh(beta)`.

   Hence

   `lim beta*t_+ = +1/(2 i rho)` and `lim beta*t_- = -1/(2 i rho)`.

   The individual causal branches are therefore not regular Taylor germs at the group identity.
3. Their exact sum is the smooth Wigner control

   `d(beta)=sin(rho beta)/(rho sinh(beta)) = 1-(rho^2+1)beta^2/6+O(beta^4)`,

   with zero linear term. Smoothness/evenness of the sum cannot be assigned to either individual branch.
4. For the explicit Barrett-Crane pole-strip

   `N_+=(+2 i rho beta)t_+`, `N_-=(-2 i rho beta)t_-`,

   both regular factors satisfy `N_+(0)=N_-(0)=1` and

   `N_+'(0)=+i rho`, `N_-'(0)=-i rho`,

   which are generically nonzero for `rho != 0`.
5. The independent source-derived Appendix-D `j=1/2` contact polynomial also has a generically nonzero linear coefficient `c1=2 rho/(rho^2+1/4)`, but this spectral/contact variable is not identified with the K4/source-cut group-coordinate one-jet.

## Scientific consequence

The source one-jet required after Iter076R-S cannot be defined as the ordinary derivative of an individual causal Toller branch at the identity. A singular/contact factor must first be separated. Moreover, source-backed regular branch factors need not be even: neither the even Haar density nor the smooth Wigner branch sum can justify setting the individual causal branch numerator one-jet to zero.

This result does **not** select a unique physical factorization for the gamma-simple EPRL branch and does not establish the full boundary-intertwiner-contracted numerator one-jet.

## Next admissible gate

Use the exact gamma-simple Eq.(9) hypergeometric form for `j>0`. Determine its identity singular order and the first coefficient of the minimally power-stripped normalized germ. The derivation must retain the branch labels and magnetic number `m`, and must stop before interpreting a wedge-level regular germ as the full physical numerator one-jet.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no physical full numerator one-jet; no physical nonlinear source-to-K4 map; no nominal `epsilon^-1` coefficient; no physical causal-vertex finiteness/divergence theorem; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; retain the source spectral `i epsilon` prescription.