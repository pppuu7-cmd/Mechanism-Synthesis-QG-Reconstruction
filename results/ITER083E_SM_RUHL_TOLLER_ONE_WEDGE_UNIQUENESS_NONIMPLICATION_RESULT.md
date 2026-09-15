# Iter083E-SM — Ruhl/Toller one-wedge analytic uniqueness does not lift to a joint K5 extension selector

Date: 2026-09-15

Status: **PASS_EXACT_SCOPED**

## Prospective provenance

- preregistration: `prereg/ITER083E_SM_RUHL_TOLLER_ONE_WEDGE_UNIQUENESS_NOT_JOINT_K5_SELECTOR.md`, commit `6aedbc1075f1ca9d2dd71e22a21172f74e914322`;
- public-source lock: `sources/ITER083E_PUBLIC_SOURCE_LOCK.md`, commit `fadc43d4107b687352520afc98952c5a22dac6cb`;
- machine-readable source lock: `sources/raw/iter083e_public_source_lock.json`, commit `94df21f665e4b038b3919b8d444a397764b5ef17`;
- theorem derivation: `sources/ITER083E_SM_RUHL_TOLLER_ONE_WEDGE_UNIQUENESS_NONIMPLICATION_DERIVATION.md`, commit `577759d30131e99e26092889cde0b893dab606db`;
- validator: `scripts/iter083e_ruhl_toller_one_wedge_nonimplication.py`, commit `c73aff9461df5d016bace3ff520524d6b4b420c4`;
- workflow/head: `.github/workflows/iter083e_ruhl_toller_one_wedge_nonimplication.yml`, commit `b64fc20f00e0165cbe10cdd75dc6a28416fcd6d0`;
- GitHub Actions run `34911549126`, terminal success;
- job `104199927491`, terminal success;
- artifact `10374825487`, `iter083e-ruhl-toller-one-wedge-nonimplication`;
- artifact ZIP digest `sha256:9e33393b72e166dcb92b49a7b524acf2fca33074ca1897d96a6e5de9e67bdcb0`;
- production JSON SHA256 `3f3c3dca902ff6fabdcf2dff8d8f447ac14677ab13ea6b4ff9dc06a1a7087ead`.

## Classification

`ITER083E_SM_RUHL_TOLLER_ONE_WEDGE_ANALYTIC_UNIQUENESS_DOES_NOT_LIFT_TO_JOINT_K5_EXTENSION_SELECTOR_SCOPED`

Verdict: **`PASS_EXACT_SCOPED`**.

## Exact public-source distinction

The Toller companion `arXiv:2604.24945` proves uniqueness of the reduced Toller splitting in a **single complex spectral variable `rho`**.

The frozen source conditions are:

- upper/lower-half-plane asymptotic decay in `rho`;
- matching to the reduced Wigner `d`-matrix in the opposite half-plane;
- finitely many simple Toller poles in the `rho` plane;
- `t^+ + t^- = d`;
- the Feynman functional `I_epsilon^(+/-)`, an integral over one variable `tilde rho`, which projects onto the unique admissible branch.

The uniqueness proof explicitly applies this one-variable projector to trial functions `u_+(rho,beta),u_-(rho,beta)` satisfying those conditions.

The same source explicitly states that the full Toller matrices do **not** form a representation of `SL(2,C)`:

`T^(+/-)(g1 g2) != sum T^(+/-)(g1) T^(+/-)(g2)`.

They retain the additive identity

`T^+ + T^- = D`.

The causal-vertex source `arXiv:2601.23162v1` then constructs a fixed-sector K5 vertex only after the elementary branches are fixed, by multiplying the ten factors

`product_(a<b) T^(sigma_a sigma_b)(g_b^-1 g_a)`

and integrating the four remaining `SL(2,C)` group variables after common-left gauge fixing.

Thus source-level one-wedge uniqueness and the downstream ten-factor common-collision extension are different mathematical stages.

## Constructive non-implication

Let `u_kappa` denote the frozen off-collision ten-wedge product/boundary-contracted distribution on `M\N`, and let `U_kappa` be one admissible same-scaling-degree extension across the common-collision submanifold `N`.

Authoritative Iter083B proves that the translation space of admissible supported extension differences is

`F_8`, `dim_C F_8=377`.

For any nonzero

`a in F_8`,

set

`U'_kappa=U_kappa+a`.

Then

`U'_kappa|_(M\N)=U_kappa|_(M\N)=u_kappa`,

but `U'_kappa != U_kappa`.

The translation by `a` occurs only at the **final simultaneous K5 collision**. It changes none of the ten elementary Toller functions. Therefore `U_kappa` and `U'_kappa` have exactly the same source-defined one-wedge data:

- the same `t^+/- (rho,beta)`;
- the same meromorphic structure in `rho`;
- the same Toller poles;
- the same one-wedge asymptotics and matching;
- the same one-variable Feynman `i epsilon` projection;
- the same `t^++t^-=d` / `T^++T^-=D` elementary relation.

Hence the entire Ruhl/Toller one-wedge uniqueness theorem is **constant on every affine translate `U+F_8`** of the joint K5 extension problem.

A collection of conditions constant on a 377-dimensional affine family cannot select one member of that family.

## Why ordinary representation composition cannot close the gap

The Wigner `D` matrices are representations, but the companion source explicitly denies the corresponding composition law for Toller `T` matrices.

Therefore one cannot infer a joint product-extension selector by importing

`D(g1g2)=D(g1)D(g2)`

into the Toller factors on the dependent K5 arguments `g_b^-1 g_a`.

This non-representation fact is not itself the origin of the extension ambiguity; its role is to close an otherwise tempting unsupported route from one-wedge uniqueness to product uniqueness.

## Harmonic-analysis statement does not define singular multiplication

The companion also notes that Toller matrices form useful objects in the inverse Fourier transform of distributions on `SL(2,C)`. That is a linear harmonic-analysis statement about representing distributions/functions.

It does not supply a multiplication theorem or common-collision extension rule for the product of ten singular factors. The present ambiguity arises precisely because the ten already-defined factors produce a joint `sd_N=20` singularity at a codimension-12 common collision; two extensions can differ by an element of `F_8` while agreeing identically off that locus.

Linear uniqueness of each factor/basis representation therefore does not eliminate the kernel of the restriction map for the nonlinear product-extension problem.

## Known source relations do not restore selector power

Authoritative Iter083C proves that the complete hierarchy generated additively from

`T^+ + T^- = D`

is blind to an `F_8` top-Boolean supported mode.

Authoritative Iter083D proves that the source-defined unit causal sums also retain the exact 377-dimensional ambiguity.

Therefore the currently source-defined package

`one-wedge Ruhl uniqueness + one-wedge Feynman i epsilon + Toller additivity + source causal summation`

still does not select any of the 377 frozen joint common-collision coefficients.

## Production checks

All P0-P7 passed.

Production independently records:

- one-wedge uniqueness variable: `rho`;
- number of spectral integration variables in the Feynman projector: `1`;
- K5 Toller factors: `10`;
- `Toller is SL(2,C) representation = false`;
- frozen joint supported ambiguity dimension: `377`;
- supported basis translations checked with unchanged one-wedge signature: `377`.

All nine negative controls passed, including rejection of corrupted source manifests asserting a Toller representation, a ten-variable Feynman projector, or a source-stated joint K5 uniqueness theorem.

## Remaining legitimate selector class

Iter083E does **not** exclude a new genuinely joint condition that acts nontrivially on `F_8`, such as:

- a correlated multivariable boundary value involving the ten dependent wedges/group variables;
- a common K5 regulator with a uniquely proved distributional limit;
- a multiplication theorem controlling the ten Toller factors at the shared collision;
- a composition/gluing normalization;
- a differential, analytic, positivity or RG constraint that removes the supported kernel.

Such a source-authorized law would be new information beyond the audited one-wedge uniqueness theorem and is the next legitimate selector target.

## Interpretation ceiling

This is a scoped non-implication theorem, not a proof of nonexistence of all possible selectors. It does not establish distributional nonexistence of the causal vertex, generic-spin completeness, all-strata global patching, regulator dependence/independence, multivertex E3/E4/E6 closure, G3/F9/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete quantum gravity.
