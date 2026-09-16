# Provenance ledger — independent Critic review of K5 projective constant-2x2 closure

Date: 2026-09-16

## Researcher gate

- preregistration `prereg/K5_DEG4_ANNIHILATOR_PROJECTIVE_CONSTANT2X2_CLOSURE.md`, commit `4f1e49f9d850fa7834dd189228d0787f84406f84`;
- parent-point lock `sources/raw/k5_deg4_projective_closure_parent_point_lock.json`, commit `14b7926ada4e4dab64c542bbd7b243035f362ff4`;
- implementation `scripts/k5_deg4_projective_constant2x2_closure.py`, commit `63538524d53aa0888effb9a5741572a9dc86150f`;
- workflow/head `d508fd145973a2ad4a8772368e00c5e599c5f908`;
- run `35140030858`, terminal success;
- job `104941953222`, terminal success;
- artifact `10464124390`;
- artifact ZIP digest `sha256:cbe6f218de38f816b30637e48198edf6f4c72a8ffdc3b18931e0f0f733ccf92d`;
- production JSON SHA256 `d9a86723b7baa5e947e0d21998d7468b61b5e26e90fce272bd8db07d677c05b4`;
- durable result commit `5fc64e1bf971923e7a85f42bc21e72a89af31512`;
- Researcher provenance/front ledger commit `6b63ae7f9744afb4de4e19c6201c89c9041afbce`.

## Parent artifact verification

The Critic independently downloaded parent action artifact `10461780450`. Downloaded ZIP SHA256 reproduced

`d1b2bbd109aa0a3969e37e97aa3e572fc4cba368c42fdc145f94689afbc032dd`.

The exact N/B values for fit_A, fit_B, validation_U and validation_G in the downloaded JSON match the post-prereg parent point lock exactly. Parent production JSON SHA256 remains

`909b2afc8474b317a424ba59f108756441bdd8cdf8888cb85763d6c368fe95b8`.

Thus Researcher input values are bound to the terminal parent artifact, not merely copied metadata.

## Critic gate

- Critic prereg `be913c29d80a34753b028b516f3fa1d7db1dd764`;
- Critic implementation `fbcadd6abf513b8157d8d246d99d933a7b0e5f58`;
- workflow/head `0acc35547f9c221604a4de47a330d0fbddc47bd6`;
- run `35143795639`, terminal success;
- job `104954616238`, terminal success;
- artifact `10465504381`;
- artifact ZIP digest `sha256:43576ec5b973673a95d075bcd56f834ede057dce0edbb3d197769aeecf38f606`;
- Critic JSON SHA256 `45ea06a1025b76af2ae9c2767fa3a979f74efc0c7c53e752f1cdec043b04b9dc`;
- durable raw summary commit `91ecff809a2ac583928de76c2475f0dd6e16a1a2`;
- controlling review commit `b7f96d219a1cfa6029edbaf96a16045c1a4bfeef`.

## Exact independent result

The Critic independently recomputed the fit determinant, fit matrix and all four validation residual components from the parent artifact values. The fit determinant is nonzero and all four validation residual components are exactly nonzero. A nontrivial constant channel-basis change preserves the counterexample, and a homogeneous representative rescaling multiplies the residual by `lambda^27` rather than removing it.

Verdict: **`CONFIRMED_SCOPED`**.

## Source/claim locks retained

Source order remains one-wedge spectral/spinor integration -> Toller function -> ten-Toller product -> full boundary contraction -> K5 group/distributional object. `status/ITER077_CONTACT_FORMULA_ERRATUM.md` remains controlling and historical Iter077E/F remain quarantined. Published one-wedge spectral `i epsilon` is unchanged.

No polynomial/rational-module closure theorem, Stokes theorem, integrated K5 period result, full 217D tensor theorem, reduction of `dim_C F_8=377`, finite-part selector, regulator independence, F9/G3/G8 promotion, `NEW_PHYSICS_FOUND`, or complete-QG claim is authorized.
