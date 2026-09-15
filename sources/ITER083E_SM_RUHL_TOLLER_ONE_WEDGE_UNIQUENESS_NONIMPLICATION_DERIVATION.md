# Iter083E-SM theorem derivation — one-wedge Ruhl/Toller uniqueness does not select the joint K5 extension

Date: 2026-09-15

Prospective contract: `prereg/ITER083E_SM_RUHL_TOLLER_ONE_WEDGE_UNIQUENESS_NOT_JOINT_K5_SELECTOR.md`, commit `6aedbc1075f1ca9d2dd71e22a21172f74e914322`.

Public-source lock: `sources/ITER083E_PUBLIC_SOURCE_LOCK.md`, commit `fadc43d4107b687352520afc98952c5a22dac6cb`; machine-readable mirror `sources/raw/iter083e_public_source_lock.json`, commit `94df21f665e4b038b3919b8d444a397764b5ef17`.

## 1. Two different uniqueness problems

The Toller companion proves a one-wedge theorem. For fixed representation labels and `beta>0`, the two reduced functions `t^+/- (rho,beta)` are uniquely determined by meromorphy in the single complex variable `rho`, prescribed upper/lower-half-plane asymptotics, matching to the reduced Wigner function, a finite simple-pole set, and `t+ + t-=d`. The Feynman functional integrates one variable `tilde rho` and projects onto the unique admissible branch.

The K5 problem is downstream. The causal vertex first fixes ten elementary Toller matrices and then forms

`P_kappa(g_2,...,g_5)= product_(a<b) T^(kappa_ab)(g_b^-1 g_a)`

(with boundary contraction), followed by the four gauge-fixed `SL(2,C)` integrations. The common-collision extension problem concerns the distribution defined by this already-fixed product near

`N=SU(2)^4 subset SL(2,C)^4`.

Thus Ruhl uniqueness acts in one spectral variable of an elementary factor; K5 extension ambiguity acts in the distributional completion of a ten-factor function on the joint group-variable space.

## 2. Restriction sequence and supported kernel

Let `u_kappa` denote one fixed-sign K5 distribution on `M\N`, and let `Ext(u_kappa)` be the affine space of source-symmetry-compatible same-scaling-degree extensions across `N` in the frozen all-`j=1/2` class.

Restriction gives

`R : Ext(u_kappa) -> {u_kappa}`.

The translation space of its kernel is exactly the supported ambiguity classified by Iter083B:

`ker(R)_translations = F_8`, `dim_C F_8=377`.

Hence for any extension `U_kappa` and any nonzero `a in F_8`,

`U'_kappa=U_kappa+a`

is a distinct admissible extension with

`U'_kappa|_(M\N)=U_kappa|_(M\N)=u_kappa`.

## 3. One-wedge analytic data factor through the off-collision source construction

Every source quantity entering the Ruhl/Toller uniqueness theorem is already fixed before `Ext(u_kappa)` is chosen:

- each elementary `t^+/- (rho,beta)`;
- its meromorphy in `rho`;
- its Toller-pole set;
- its one-wedge asymptotic decay and matching;
- the one-variable `I_epsilon^+/-` projector;
- `t+ + t-=d` and `T+ + T-=D`.

The translation `U_kappa -> U_kappa+a` changes only a distribution supported on the simultaneous final collision `N`. It does not modify any elementary factor `T^(kappa_ab)(g)` as a function on `SL(2,C)`, and therefore cannot change any of the one-wedge spectral data above.

Formally, if `J` denotes the map from a K5 extension to the tuple of source-fixed one-wedge analytic data, then

`J(U_kappa+a)=J(U_kappa)` for every `a in F_8`.

Therefore every condition in the one-wedge uniqueness theorem is constant on the full affine `F_8` orbit of joint extensions.

This is an exact non-implication: a set of constraints constant on an affine 377-dimensional family cannot select one member of that family.

## 4. Why a representation composition law cannot supply the missing implication

The companion paper explicitly states

`T^+/- (g1 g2) != sum T^+/- (g1) T^+/- (g2)`.

Thus the Toller matrices are not an `SL(2,C)` representation. One cannot import the Wigner-D composition law and argue that uniqueness of each factor algebraically propagates into a unique distributional product on the dependent K5 arguments `g_b^-1 g_a`.

This non-representation fact is not the source of the ambiguity; Iter083B already classifies the ambiguity. Its role is to close a tempting but source-invalid route for deriving a joint selector from ordinary representation composition.

## 5. The source's remaining explicit inter-branch relation is also insufficient

The companion retains the additive identity

`T+ + T-=D`.

Iter083C proves constructively that for every `a in F_8` the sectorwise top-Boolean deformation

`Delta_kappa=(product_e kappa_e)a`

is annihilated by every nonempty partial sign-sum identity generated from that relation. Hence adding the complete additive hierarchy does not distinguish the translated joint extensions.

Iter083D further proves that the source-defined unit causal sums retain the exact 377-dimensional ambiguity.

Consequently the source package

`one-wedge Ruhl uniqueness + one-wedge i epsilon projector + Toller additivity + source causal sum`

is jointly constant along a nonzero, in fact 377-dimensional, common-collision extension family in the frozen sector.

## 6. What would evade the theorem

The argument would not apply to a genuinely joint condition whose value changes under `U -> U+a`. Examples include a source-authorized correlated multivariable boundary value, a common K5 regulator with a proved unique distributional limit, a multiplication theorem controlling the ten-factor product at the shared collision, or a composition/gluing/differential/positivity/RG condition proved to act injectively enough on `F_8`.

No such theorem is included in the audited one-wedge uniqueness argument or causal-vertex definition. If later primary authority supplies one, it becomes the next object to test rather than being ruled out by Iter083E.

## 7. Theorem

Within the frozen all-`j=1/2`, common-K5-collision, boundary-linear, compact-node-gauge/S5-covariant same-scaling-degree class:

**Ruhl/Toller one-wedge analytic uniqueness and its Feynman `i epsilon` representation do not imply uniqueness of the joint K5 distributional extension.**

More strongly, all source-defined one-wedge analytic data are invariant under translation by the full `F_8`, `dim_C F_8=377`; the known additive and unit causal-sum relations do not reduce this kernel by Iter083C-D.

Candidate classification:

`ITER083E_SM_RUHL_TOLLER_ONE_WEDGE_ANALYTIC_UNIQUENESS_DOES_NOT_LIFT_TO_JOINT_K5_EXTENSION_SELECTOR_SCOPED`.

Production/review promotion remains required.

## Interpretation ceiling

This is not a proof that no correlated multivariable prescription exists or can work. It is not a causal-vertex distributional nonexistence theorem, a generic-spin theorem, an all-strata patching theorem, a regulator-(in)dependence theorem, a multivertex E3/E4/E6 theorem, G3/F9/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete quantum gravity.
