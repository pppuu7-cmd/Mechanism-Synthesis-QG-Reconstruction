# Iter083B-SM preregistration — filtered boundary-covariant supported-ambiguity exactness

Date: 2026-09-15

## Status

Prospective theorem/validation gate after an exploratory mathematical observation. This gate is **conditionally dependent** on an authoritative production PASS of Iter083A. If Iter083A does not obtain `PASS_EXACT_SCOPED`, no numerical promotion to 377 is authorized here.

## Question

Does the lack of a source-selected normal-coordinate splitting/connection prevent the exact dimension of the symmetry-compatible finite-order distributional ambiguity from being determined, even after the graded boundary-covariant normal-symbol multiplicities have been classified?

The proposed theorem is that in the frozen compact-symmetry K5 setting it does **not** prevent the dimension count. A preferred coefficient tuple is noncanonical, but the filtered invariant space and its dimension are intrinsic.

## Frozen authority

1. Iter077L: after common-left gauge fixing, `M=SL(2,C)^4`, `N=SU(2)^4`, `codim N=12`, source scaling degree `20`; same-scaling-degree extension differences are distributions supported on `N` with transverse normal derivative order at most `8`.
2. Iter077M: the source measure is product Haar; quotient/tubular density is invariant; `delta_N` is a legitimate source-gauge-compatible supported distribution; no source K5 finite part, subtraction, common regulator, boundary-value prescription, or gluing/composition identity selects an extension coefficient.
3. Iter077Q right-SU2 correction: node-wise compact gauge symmetry acts transitively on `N`; the scalar tangential functional freedom collapses to fiber data; `delta_N` is preserved by the node-wise action and Haar/tubular density.
4. Iter081R: the compact gauge orbit is `SU(2)^5/SU(2)_diag ~= N`; the 12-dimensional normal fiber at the identity orbit is `V=spin1_SO(3) tensor Std5_S5`; each invariant symmetric normal tensor can be realized as a principal normal symbol using an equivariant tubular neighborhood/compact-group averaging; derivatives of order `k<=8` remain within source scaling degree 20.
5. Iter083A preregistration and, only if obtained, its authoritative production result for the boundary-linear graded multiplicities

`m_k = dim (H_boundary^* tensor Sym^k V)^(SO(3) x S5)`.

## Frozen object

Let `A_<=k` be the complex vector space of source-symmetry-compatible, boundary-linear distributions on a common-collision neighborhood that

- are supported on `N`;
- have transverse normal order at most `k`;
- use the source Haar/tubular density convention;
- transform covariantly under the true 32-dimensional all-`j=1/2` boundary intertwiner space;
- obey the exact compact node gauge symmetry and `S5` relabeling symmetry frozen upstream.

No preferred normal-coordinate coefficient splitting is part of the definition.

Set `A_<=-1=0` and filter by transverse normal order.

## Theorem obligations

### T1 — intrinsic filtration

Show that normal order defines an invariant filtration

`0=A_<=-1 subset A_<=0 subset ... subset A_<=8`.

The definition must be coordinate independent. Local expressions such as

`sum_{|alpha|<=k} u_alpha(y) partial_n^alpha delta_N`

may be used only as representatives; the individual `u_alpha` are not to be declared canonical.

### T2 — principal normal symbol

For each `k`, construct the intrinsic principal-normal-symbol map

`sigma_k : A_<=k -> (H_boundary^* tensor Sym^k V)^(SO(3) x S5)`

with kernel exactly `A_<=k-1`.

Any dual/conormal convention must be reconciled explicitly. In the frozen real orthogonal `spin1 tensor Std5` representation, `V` is self-dual, so the character multiplicity is unchanged; this may not be used to conceal a density/sign twist.

### T3 — no density/orientation twist

Prove from the frozen source geometry that product Haar and the induced tubular density are preserved by the compact node action and vertex relabelings. Since distributions act on densities rather than oriented volume forms, no unmotivated determinant-sign character may be inserted.

### T4 — surjectivity by compact averaging

For every invariant principal symbol, choose any local order-`k` supported representative using a tubular neighborhood, then average it over the compact source symmetry group. Prove that averaging

- preserves support on `N`;
- preserves normal order;
- preserves the invariant principal symbol;
- yields a source-symmetry-compatible representative.

Therefore `sigma_k` is surjective on the invariant space even though no canonical splitting is selected.

### T5 — exact sequence and dimension additivity

Establish the short exact sequence

`0 -> A_<=k-1 -> A_<=k -> G_k -> 0`,

where

`G_k=(H_boundary^* tensor Sym^k V)^(SO(3) x S5)`.

Conclude inductively

`dim A_<=8 = sum_{k=0}^8 dim G_k = sum_{k=0}^8 m_k`.

The conclusion is about dimension and existence of equivariant splittings, not a preferred physical coefficient basis.

### T6 — tangential-distribution collapse

Explicitly exclude a hidden infinite-dimensional tangential sector. Use transitivity of the compact node action on `N=SU(2)^5/SU(2)_diag`: invariant distributional sections of the relevant homogeneous finite-rank bundle are determined by finite fiber data at one point (equivalently by isotropy-invariant fiber data). Do not assume coefficient smoothness as the sole reason for finiteness.

### T7 — scaling-degree ceiling

Verify that an order-`k` derivative of `delta_N` has transverse scaling degree `12+k`, so all `0<=k<=8` lie within the source bound 20 and no higher order is authorized by the frozen theorem.

## Conditional numerical target

Only if Iter083A obtains an authoritative production PASS with

`m_0..m_8 = (2,0,5,1,22,10,72,48,217)`,

the theorem predicts

`dim_C A_<=8 = 377`.

This target is already known from exploratory work and therefore is a replication target, not a blinded discovery.

## Adversarial controls

The theorem/review must reject each of the following:

1. `CANONICAL_SPLITTING_FROM_AVERAGING`: compact averaging can produce an equivariant splitting but does not make it source-selected or canonical.
2. `SCALAR_28_IS_COMPLETE`: Iter081R scalar 28-dimensional subspace is not the full boundary-linear frozen sector if Iter083A opens representation-valued channels.
3. `HIDDEN_TANGENTIAL_FUNCTION_SPACE`: arbitrary functions/distributions along `N` are incompatible with transitive node-gauge invariance; prove the homogeneous-space statement.
4. `DENSITY_SIGN_TWIST`: do not insert orientation signs into a density-valued source measure.
5. `SELECTOR_FROM_DIMENSION`: knowing the exact ambiguity-space dimension does not select a unique physical extension.
6. `FINITE_PART_FROM_ONE_WEDGE_IEPSILON`: one-wedge causal/Feynman prescription does not by itself supply a joint K5 extension selector.
7. `GLOBAL_VERTEX_FROM_LOCAL_PATCH`: this theorem concerns the frozen common-collision supported ambiguity sector; it does not prove existence/uniqueness of a globally patched physical vertex across every singular stratum.
8. `OTHER_SPINS_COMPLETE`: no generic-spin or all-boundary-sector completeness claim is authorized.

## PASS classification

If T1-T7 and all adversarial controls are satisfied, and Iter083A has authoritative production PASS:

`ITER083B_SM_FILTERED_BOUNDARY_COVARIANT_SUPPORTED_AMBIGUITY_DIMENSION_EXACT_SCOPED`

Verdict: `PASS_EXACT_SCOPED`.

If T1-T7 hold but Iter083A is not yet authoritative, verdict is

`PROVED_CONDITIONAL_PENDING_ITER083A_PRODUCTION`.

If a genuine source density/transport twist or noncompact/nontransitive symmetry invalidates T2-T6, verdict is `BLOCKED_OBJECT_DEFINITION` with the exact failed obligation identified.

## Interpretation ceiling

Even an exact 377-dimensional result would mean only: in the frozen all-`j=1/2`, common-K5-collision, boundary-linear, exact compact-gauge/S5-covariant, same-scaling-degree sector, the full filtered supported extension-difference space through order 8 has that dimension.

It would **not** supply a finite-part/selector, choose the physical 377 coefficients, prove causal-vertex divergence/nonexistence, establish regulator independence, complete other collision strata, prove generic-spin completeness, establish multivertex gluing, G3/F9/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete quantum gravity.