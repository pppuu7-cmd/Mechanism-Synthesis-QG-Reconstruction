# Iter083H-SM derivation — primitive deepest K5 simple pole is Q-independent under S5

Date: 2026-09-15
Status: PRE-PRODUCTION THEOREM DERIVATION AFTER PROSPECTIVE PREREGISTRATION

Preregistration: `prereg/ITER083H_SM_PRIMITIVE_SIMPLE_K5_POLE_Q_INDEPENDENCE.md`, commit `8a959d565777bd57e5d102c467b140bd618abce0`.

## 1. Inputs already authoritative in the repository

### K5 common-collision scaling
Iter077I/Iter083F establish in the frozen all-j=1/2 source-ordered sector:

- ten K5 wedge factors;
- each wedge has leading common-collision radial degree `-2`;
- the ten-wedge leading degree is `-20`;
- after common-left gauge fixing the common-collision normal codimension is `12`;
- the normal radial volume contributes `r^11 dr`;
- finite one-wedge spectral epsilon does not alter the leading `r^-20` degree.

### Ten-edge regulator representation
Iter083G establishes exactly

`E = R^10 = [5] + [4,1] + [3,2]`

under S5 edge relabeling, and every S5-invariant symmetric nondegenerate regulator form is

`Q = a I + b A + c B`,

with one scalar eigenvalue on each of these three inequivalent irreducible sectors.

### True boundary representation
Iter083A establishes

`H_boundary^* = 2[5] + [4,1] + 2[3,2] + 2[2,2,1] + [2,1,1,1] + 2[1^5]`.

No scalar surrogate is used below.

## 2. Multivariate radial regularization of the primitive overall collision

Introduce one complex regulator per edge,

`s_e = 1 + x_e`.

In the frozen leading common radial model replace edge `r^-2` by

`r^(-2 s_e)`.

The ten-edge product contributes

`r^(-2 sum_e s_e) = r^(-20 - 2 L(x))`,

where

`L(x) = sum_e x_e`.

Take the normal Taylor coefficient of order `n` from the smooth test density / regular part. Together with the codimension-12 radial measure, its radial integral is modeled by

`I_n(x) = integral_0^1 r^(11+n-20-2L(x)) dr`

and hence, by analytic continuation,

`I_n(x) = 1 / (n - 8 - 2 L(x))`.

At the physical point `x=0`:

- if `n<8`, denominator `n-8` is nonzero;
- if `n=8`, `I_8(x) = -1/(2 L(x))`, a simple pole;
- if `n>8`, denominator `n-8` is nonzero.

Thus in this isolated primitive radial channel the only polar hyperplane through the physical point is the single simple hyperplane

`L(x)=0`.

This is not a claim that the full forest meromorphic germ has only one pole: nested K3/K4 subcollisions supply additional pole forms and are explicitly excluded from the present primitive model.

## 3. Dang–Zhang polar-germ structure used

Dang–Zhang Sec. 6.2 fixes a nondegenerate bilinear form `Q` on regulator parameter space, inducing `Q*` on the dual. Their definition of a polar germ with denominator linear forms `L_i` requires its holomorphic numerator variables `ell_j` to satisfy

`Q*(L_i, ell_j)=0`.

The direct-sum decomposition into holomorphic plus polar germs defines the projection `pi_Q` onto the holomorphic part.

For one simple denominator `L`, the relevant decomposition therefore separates the regulator dual space into

`span(L) + L^(perp,Q*)`.

## 4. Why the complement of L is Q-independent under exact S5

The covector

`L = sum_e x_e`

is fixed by every edge permutation, hence spans the unique trivial `[5]` summand in `E*`.

For any S5-invariant nondegenerate bilinear form Q, inequivalent irreducible S5 summands are mutually Q-orthogonal. Equivalently, a cross pairing between two inequivalent irreps would define a nonzero S5 intertwiner from one irrep to the dual of the other, contradicting Schur orthogonality.

Because

`E* = [5] + [4,1] + [3,2]`

is multiplicity-free, every invariant Q/Q* is block scalar and

`L^(perp,Q*) = [4,1] + [3,2]`

for every nondegenerate S5-invariant Q.

The three sector eigenvalues of Q may vary, but they cannot rotate the trivial line into a nontrivial sector. Therefore the decomposition

`E* = span(L) direct_sum ([4,1]+[3,2])`

needed by a one-denominator polar germ is independent of the Iter083G Q-shape parameters.

## 5. True boundary-valued linear numerator channels

Let the holomorphic numerator be an S5-equivariant `H_boundary^*`-valued germ

`h(x)=h_0+h_1(x)+h_2(x)+...`,

with `h_m` homogeneous of regulator degree m.

The linear term is an equivariant map

`h_1 in Hom_S5(E,H_boundary^*)`.

Using the exact decompositions,

`E = [5]+[4,1]+[3,2]`,

`H_boundary^* = 2[5]+[4,1]+2[3,2]+...`,

Schur pairing gives

`dim Hom_S5(E,H_boundary^*) = 2 + 1 + 2 = 5`.

These five channels split as:

- two maps from the trivial regulator input `[5]` to the two trivial boundary copies;
- one map from regulator `[4,1]`;
- two maps from regulator `[3,2]`.

Thus the physical vector-valued problem contains three genuine nontrivial regulator-linear channels. They are retained, not scalarized away.

## 6. Evaluated finite part of h/L

Consider

`F_Q(x)=h(x)/L(x)`.

### Degree zero numerator
`h_0/L` is a pure polar germ: the numerator is constant and has no nonpolar variable. Therefore

`pi_Q(h_0/L)=0`.

### Degree one numerator
Decompose the regulator input of `h_1` using the Q-independent S5 splitting

`E = E_triv direct_sum E_nontriv`.

The trivial-input part is necessarily of the form

`h_1^triv(x)=L(x) C`

for a fixed vector `C in (H_boundary^*)^S5` (the exact normalization of C depends only on the convention for L, not on Q).

Hence

`h_1^triv/L = C`

is holomorphic and contributes the constant C.

The nontrivial-input part depends only on regulator linear forms in

`[4,1]+[3,2] = L^(perp,Q*)`.

Therefore

`h_1^nontriv/L`

is a polar germ in the Dang–Zhang sense and is annihilated by `pi_Q`.

So

`ev_0 pi_Q(h_1/L)=C`

for every S5-invariant nondegenerate Q.

### Higher numerator degree
For `m>=2`, division by one linear denominator lowers homogeneous degree by exactly one in any holomorphic term produced by cancelling one factor of L. Such holomorphic terms have degree at least one and vanish under evaluation at x=0. Terms without a cancellable L remain polar.

Thus

`ev_0 pi_Q(h_m/L)=0`, m>=2.

Combining all degrees,

`ev_0 pi_Q(h/L)=C`,

where C is the trivial-regulator component of the linear numerator. This value is independent of the three S5-invariant Q-sector eigenvalues.

## 7. Meaning of the result

Iter083G proves that the Q input is not fixed by S5 symmetry on the full ten-variable meromorphic-germ space.

Iter083H shows that this Q freedom is nevertheless invisible to the **isolated one-simple-pole primitive overall K5 finite part** because the unique pole direction is the trivial regulator irrep and invariant Q cannot mix it with nontrivial sectors.

Therefore any actual Q-dependence relevant to K5 must come from structure not present in this primitive model, most notably:

- simultaneous independent pole forms from nested K3/K4/K5 collisions;
- higher pole multiplicity;
- a non-S5-covariant prescription;
- or additional nontrivial regularization data.

The natural next target is the resolved forest polar geometry, not another single-pole computation.

## 8. Scope locks

No full K5 meromorphic continuation theorem; no assertion that actual nested K5 renormalization is Q-independent; no unique physical selector; no generic-spin theorem; no all-strata patching theorem; no regulator independence; no G3/F9/G8/K5 promotion; no NEW_PHYSICS_FOUND; no complete-QG claim.