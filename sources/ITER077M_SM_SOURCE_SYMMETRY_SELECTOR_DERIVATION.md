# Iter077M-SM source derivation — symmetry-compatible supported ambiguity

**Date:** 2026-09-14

## Source facts

Prospective contract: `prereg/ITER077M_SM_SOURCE_SYMMETRY_EXTENSION_SELECTOR.md`.

Primary source: Bianchi, Chen, Gamonal, *Causal spinfoam vertex for 4d Lorentzian quantum gravity*, arXiv:2601.23162.

The source defines, for fixed causal labels `sigma_a`, a vertex linear functional on spin-network boundary states by

`A_sigma(Psi) = integral prod_(a=2)^5 dg_a prod_(a<b) T^(sigma_a sigma_b)(g_b^-1 g_a)`

with magnetic indices contracted with the five boundary intertwiners. It states that the common `SL(2,C)` redundancy is gauge-fixed by setting one group variable to the identity. The integrand before gauge fixing depends only on relative elements `g_b^-1 g_a`.

The same source explicitly states in its Discussion that finiteness of the causal model still has to be investigated because Toller poles can introduce new divergences. It also states that the paper focuses on a single vertex and that the many-vertex theory is a future step. No joint K5 normalization, subtraction, finite-part, common regulator, or gluing/composition identity selecting a local extension coefficient is stated.

The companion Toller paper fixes the one-wedge Toller functions; it does not add a K5-supported normalization rule.

## Gauge-invariant common-collision set

Before gauge fixing, define

`S = {g : g_b^-1 g_a in SU(2) for all a,b}`.

Under the source global gauge action

`g_a -> h g_a`, `h in SL(2,C)`,

all relative elements are unchanged:

`(h g_b)^-1 (h g_a) = g_b^-1 g_a`.

Therefore `S` is invariant under the exact same common gauge symmetry as the source integrand.

After choosing the source gauge `g_1=1`, every point of `S` has the four remaining variables in `SU(2)`, so

`S / SL(2,C) ~= N = SU(2)^4`.

The product Haar density and its quotient/tubular density are invariant under the common action. The delta distribution supported on this invariant submanifold is therefore a legitimate gauge-invariant supported distribution; in the source gauge it is denoted `delta_N`.

## Boundary coefficient from the actual boundary representation

The source boundary state is defined by the ten spins and five SU(2)-invariant intertwiners. On `N`, all relative group elements are compact. Restricting the spin-`j` block of the principal-series Wigner matrix to `SU(2)` gives the ordinary spin-`j` Wigner matrix. Hence the usual compact spin-network contraction

`F_SU2(y;Psi)`

formed from the same ten spin labels, the same five boundary intertwiners, and the relative compact matrices is a smooth linear functional of the actual source boundary state. No scalar K4/K5 surrogate or representative intertwiner is introduced.

Because the intertwiners are SU(2)-invariant tensors, this coefficient has the same boundary gauge/intertwiner structure as the compact restriction of the ordinary EPRL spin-network integrand.

## One-parameter extension family

Let `A_ext` be any local same-scaling-degree extension supplied by the Iter077L theorem on a common-collision patch. Define

`A_ext,c = A_ext + c F_SU2(y;Psi) delta_N(x)`

for constant `c`.

This is used only as a mathematical uniqueness counterexample, not proposed as a physical modification.

### Support check

`delta_N` is supported on the common-collision set. Therefore all `A_ext,c` agree with the exact source-ordered ten-Toller product at every point off `N`. The one-wedge Toller functions, causal signs and source ordering are unchanged.

### Scaling check

There are 12 normal boost coordinates. The transverse delta `delta_N` has scaling degree 12. Multiplication by the smooth tangential coefficient `F_SU2` preserves this degree. Iter077L has `sd_N(A_ext)=20`. Therefore

`sd_N(A_ext,c)=20`

for every finite `c`; adding this term does not violate the same-scaling-degree extension class.

### Global gauge check

The pre-gauge version `F_SU2 delta_S` is supported on an invariant set defined entirely through relative elements and is invariant under common left `SL(2,C)` multiplication. Gauge fixing gives the displayed `F_SU2 delta_N` representative.

### Fixed causal-data check

The construction is performed separately for one frozen causal sector. It neither sums over `sigma_a` nor changes any `sigma_a sigma_b`. The supported term may be assigned the same coefficient rule in every relabelled copy if permutation covariance is later imposed; the primary source does not state a local extension normalization tying that coefficient to zero.

## Source-selector audit

The primary causal-vertex paper:

- proposes Eq. (4) as the single-vertex amplitude;
- explicitly says causal-vertex finiteness must still be investigated;
- explicitly treats many-vertex construction as future work;
- contains no stated subtraction condition, K5 finite part, common K5 regulator, collision boundary-value prescription, or gluing/composition identity that fixes `c`.

This is stronger than a keyword absence: the Discussion itself identifies finiteness and many-vertex dynamics as unresolved future directions.

## Consequence

The family `A_ext,c` gives an explicit source-compatible local nonuniqueness witness under the constraints that are actually present in the published single-vertex construction. Therefore global gauge invariance, use of the true boundary spin/intertwiner representation, fixed causal labels, and one-wedge Feynman source ordering do not by themselves select a unique K5 extension.

This does not show that future gluing, cylindrical consistency, renormalization-group fixed-point conditions, reflection/causal composition, or another independently motivated principle cannot fix `c`. Those would be additional constraints and must be prospectively tested rather than read back into the existing source.