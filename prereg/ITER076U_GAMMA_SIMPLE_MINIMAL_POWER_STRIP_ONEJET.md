# Iter076U preregistration — gamma-simple Toller identity singular order and minimal power-strip one-jet

Date: 2026-09-13

## Purpose

Iter076T established source-faithfully that an individual causal Toller branch need not be a regular Taylor germ at the group identity and that a pole-stripped source control can have a nonzero one-jet. The next step is to move from the Barrett-Crane control to the actual gamma-simple reduced Toller branch displayed in Eq. (9) of the causal-vertex source.

This gate tests the leading identity singular order and the first derivative of the **minimally power-stripped normalized wedge-level germ**. It deliberately stops before boundary-intertwiner contraction and before any physical source-to-K4 interpretation.

## Frozen source and scope

Use `sources/GAMMA_SIMPLE_TOLLER_IDENTITY_ASYMPTOTIC_SUPPLEMENT.md`, committed before implementation.

Frozen parameter scope:

- `j` positive half-integer;
- `m=-j,-j+1,...,j`;
- real `gamma != 0`;
- `n:=2j+1 >= 2` integer.

For each branch the source Eq. (9) is written as

`t_±(beta)=exp(-E_± beta) P_± 2F1(a_±,b_±;c_±;exp(-2 beta))`,

with the exact parameter definitions recorded in the supplement.

## Frozen lanes

### Lane A — source parameter locks

PASS iff the committed supplement contains:

- the Eq. (9) gamma-simple branch form;
- the exact `E_±`, `a_±`, `b_±`, `c_±` definitions;
- positive-half-integer `j`, admissible `m`, real nonzero `gamma` scope;
- the explicit firewall that the wedge-level power-strip is not a unique physical full-vertex factorization.

### Lane B — exact hypergeometric singular order and first recurrence

For both branches verify symbolically:

`c_±-a_±-b_± = -(2j+1) = -n`.

With `w=1-exp(-2 beta)`, the hypergeometric differential equation is

`w(1-w)F_ww + [n+1-(a+b+1)w]F_w - abF = 0`.

For the leading singular ansatz

`F=A0 w^(-n)(1+r w+...)`,

verify the exact first recurrence

`r=(n c-a b)/(n-1)`

and its branch reductions

`r_+=-(1+i gamma)(j-m)/2`,

`r_-=-(1-i gamma)(j+m)/2`.

PASS also requires `n>=2` in the frozen half-integer scope, so the first recurrence is non-resonant. No claim about absence of later logarithmic terms is allowed.

### Lane C — minimally power-stripped normalized one-jet

Define

`C_± = lim_(beta->0+) beta^n t_±(beta)`

and the algebraic control germ

`G_±(beta)=beta^n t_±(beta)/C_±`.

Using only the exact first singular recurrence and

`w=2 beta(1-beta+O(beta^2))`,

verify

`G_±'(0+) = n-E_±+2r_±`.

PASS iff both branches simplify identically to

`G_+'(0+) = G_-'(0+) = i gamma m`.

Consequently:

- `m=0` gives zero one-jet;
- for `m!=0` and `gamma!=0`, the wedge-level one-jet is nonzero;
- causal branch sign alone does not flip this minimally normalized one-jet.

This does not promote `G_±` to the physical full numerator.

### Lane D — discrete half-integer census, Wigner control, and firewall

Enumerate exact admissible `(j,m)` pairs for

`j in {1/2,1,3/2,2,5/2,3}`.

PASS iff:

- the symbolic branch formula reduces to `i gamma m` for every enumerated pair and both branches;
- all and only `m=0` cases have identically zero minimal-power one-jet;
- all `m!=0` cases are generically nonzero for `gamma!=0`;
- the smooth gamma-simple Wigner Eq. (8) identity derivative is independently reconstructed as
  `d'(0) = -i gamma j m/(j+1)` in the source phase convention, and is not substituted for the Toller power-stripped one-jet;
- the implementation records:
  - `unique_physical_Toller_factorization_established=false`;
  - `full_boundary_intertwiner_onejet_established=false`;
  - `arbitrary_group_tangent_onejet_established=false` because KAK coordinates are singular at identity;
  - `physical_source_to_K4_curvature_selected=false`;
  - `epsilon_minus1_coefficient_established=false`;
  - no generic finite-spin signed P3 or G3/F9/G8/K5 promotion.

## PASS classification

`ITER076U_GAMMA_SIMPLE_TOLLER_MINIMAL_POWER_STRIP_ONEJET_EQUALS_I_GAMMA_M_BOTH_BRANCHES_EXACT_SCOPED`

## Scientific meaning on PASS

The exact Eq. (9) gamma-simple reduced Toller branch has leading identity singular order `beta^(-(2j+1))`. Removing only that leading power and normalizing its leading coefficient produces a finite right one-jet equal to `i gamma m` for both causal branches.

Thus the remaining possibility for eliminating the relevant source one-jet is no longer generic branch evenness. It must come from stronger structure: magnetic-index/intertwiner contraction, covariant treatment of arbitrary tangent directions, or the actual nonlinear source-to-K4 map.

## Next admissible gate

Audit whether the `i gamma m` wedge-level coefficient is annihilated by exact SU(2)-intertwiner contraction / node-wise magnetic closure in the source boundary amplitude, while keeping boost versus rotation generator insertions distinct. A PASS there may eliminate a class of source one-jet contamination; a FAIL/survival result would require explicit boundary-state-dependent one-jet data.

## FAIL classification

`ITER076U_GAMMA_SIMPLE_MINIMAL_POWER_STRIP_ONEJET_CONFIRMATION_FAIL`

Technical/source-algebra failure only; no physical divergence/finiteness interpretation.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no physical full numerator one-jet; no physical nonlinear source-to-K4 map; no nominal `epsilon^-1` coefficient; no physical causal-vertex finiteness/divergence theorem; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; retain the source spectral `i epsilon` prescription.