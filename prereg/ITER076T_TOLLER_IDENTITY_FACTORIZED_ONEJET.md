# Iter076T preregistration — Toller identity singularity and factorized branch one-jet

Date: 2026-09-13

## Purpose

Iter076R-S show that a source one-jet cannot be bypassed by Haar evenness or K4 symmetry: a symmetry-allowed quadratic curvature channel exists and generic one-jet contamination survives the exact transitive-face restriction complex.

The next object must therefore be defined correctly at source level. The individual causal Toller branch is not automatically a smooth Taylor germ at the group identity. The exact Barrett-Crane source control contains `1/sinh(beta)`, so a naive derivative of `t^(+/-)(beta)` at `beta=0` is singular even though the branch sum is smooth.

This gate tests only this object-definition issue and a source-backed pole-stripped control. It does not define the full EPRL/Toller boundary-contracted numerator one-jet.

## Frozen sources

Use `sources/TOLLER_IDENTITY_FACTORIZATION_SOURCE_SUPPLEMENT.md`, committed before implementation, and the existing source-derived `distributional/jhalf_iepsilon_validation.py`.

Primary-source facts frozen in the supplement:

1. `T^(+) + T^(-) = D`.
2. Reduced Toller branches are functions of the second kind and admit a positive/negative boost-frequency interpretation.
3. Exact Barrett-Crane control for `rho != 0`:

   `t_+(beta) = +(1/(2 i rho)) exp(+i rho beta)/sinh(beta)`

   `t_-(beta) = -(1/(2 i rho)) exp(-i rho beta)/sinh(beta)`

   `d(beta) = sin(rho beta)/(rho sinh(beta))`.

No statement about a unique physical factorization of the gamma-simple EPRL branch is frozen here.

## Frozen lanes

### Lane A — source/provenance locks

PASS iff the committed supplement contains the additive relation, second-kind/frequency interpretation, exact Barrett-Crane branch formulas, and explicit scope lock that the physical EPRL/intertwiner one-jet is not yet defined.

The existing Appendix-D `j=1/2` file must also contain the exact source-derived coefficients

`c1 = 2 rho/(rho^2+1/4)`, `c2 = 2/(rho^2+1/4)`

and the contact term `-i c1 delta - (c2/2) delta'`.

### Lane B — exact identity singularity and smooth branch sum

With symbolic real `rho != 0`, verify exactly:

- `lim_(beta->0) beta t_+(beta) = +1/(2 i rho)`;
- `lim_(beta->0) beta t_-(beta) = -1/(2 i rho)`;
- therefore neither individual branch is a regular Taylor germ at `beta=0`;
- `t_+ + t_- = d` identically;
- `lim_(beta->0) d(beta)=1`;
- `d'(0)=0`;
- `d(beta)=1-(rho^2+1) beta^2/6+O(beta^4)`.

### Lane C — pole-stripped Barrett-Crane branch control

Define only for this exact control

`N_+(beta)=(+2 i rho beta)t_+(beta)`,

`N_-(beta)=(-2 i rho beta)t_-(beta)`.

PASS iff exactly:

- both are regular at `beta=0`;
- `N_+(0)=N_-(0)=1`;
- `N_+'(0)=+i rho`;
- `N_-'(0)=-i rho`;
- the quadratic coefficient of both is `-(rho^2/2+1/6)`;
- for symbolic `rho != 0`, neither one-jet is identically zero.

This is a counterexample to universal individual-branch evenness, not a claim that this pole-strip is the unique physical EPRL factorization.

### Lane D — independent contact control and firewall

Reconstruct the `j=1/2` Appendix-D polynomial algebraically and verify its exact linear coefficient

`c1=2 rho/(rho^2+1/4)`.

PASS iff:

- the exact product polynomial equals the frozen expansion;
- `c1` is generically nonzero and vanishes only at `rho=0` on the real line;
- the implementation records that the Appendix-D variable is spectral/contact data and is not identified with a K4/source-cut group-coordinate one-jet;
- `naive_branch_derivative_at_identity_is_valid_onejet=false`;
- `universal_individual_branch_evenness_established=false`;
- `physical_EPRL_Toller_intertwiner_onejet_established=false`;
- `physical_nonlinear_source_to_K4_curvature_selected=false`;
- `epsilon_minus1_coefficient_established=false`;
- no generic finite-spin signed P3 or G3/F9/G8/K5 promotion.

## PASS classification

If A-D all pass:

`ITER076T_NAIVE_TOLLER_IDENTITY_ONEJET_SINGULAR_POLE_STRIPPED_BC_BRANCH_HAS_GENERIC_NONZERO_ONEJET_EXACT_SCOPED`

## Scientific meaning on PASS

A PASS establishes that the missing source one-jet cannot be defined as the ordinary derivative of an individual causal Toller branch at the identity, and that source-backed regular branch factors need not be even. Consequently, neither Haar evenness nor smoothness of the branch sum `D` can set the full causal branch numerator one-jet to zero.

The next admissible gate is to derive a **gamma-simple EPRL branch factorization** from the source Eq.(9)/companion closed form: isolate its leading identity singular/contact factor for general `j,m`, determine whether the remaining regular factor has a finite one-jet, and only then propagate that object through boundary-intertwiner contraction and source cut coordinates.

## FAIL classification

Any frozen exact or source-lock predicate fails:

`ITER076T_TOLLER_IDENTITY_FACTORIZED_ONEJET_CONFIRMATION_FAIL`

This is an algebra/source-provenance failure, not a physical finiteness/divergence result.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no physical full numerator one-jet; no physical nonlinear source-to-K4 map; no nominal `epsilon^-1` coefficient; no physical causal-vertex finiteness/divergence theorem; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; retain the source spectral `i epsilon` prescription.