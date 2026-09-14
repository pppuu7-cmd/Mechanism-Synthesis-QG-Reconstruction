# Iter080 provenance ledger

**Date:** 2026-09-14

This ledger records authority and scope for the Iter080 K5 extension-selector line. It does not alter the controlling Iter077 source/erratum ledger.

## Iter080A-SM — finite K5 permutation covariance selector test — AUTHORITATIVE PASS, EXACT SCOPED

- preregistration: `19f03d40929c7f7fc7aa9c82eed6485646028876`
- implementation: `eaef2c647c338767622187b293b0b3f476b60103`
- workflow/production head: `431e3cc4056c06885cf0ba4c468ff886ba2bb9a3`
- terminal run: `34820372854`
- lane jobs: A `103900365276`, B `103900365214`, C `103900365168`, D `103900364995`
- aggregate job: `103900533687`
- aggregate artifact: `10337479168`
- digest: `sha256:981c7a994ee481fbe3663c66054cfb1ea7a956933f4f5452f480c8cd1eb5dcce`
- result: `results/ITER080A_SM_K5_FINITE_PERMUTATION_SELECTOR_RESULT.md`, commit `4b5ed558225819e8eaf36798d15de7a007f39964`
- classification: `ITER080A_SM_FINITE_K5_PERMUTATION_COVARIANCE_LEAVES_INFINITE_DIMENSIONAL_TANGENTIAL_EXTENSION_AMBIGUITY_EXACT_SCOPED`
- independent Critic review: `CONFIRMED_SCOPED`, commit `50e00424ba3cd25489cb238cabb6c27097fbf7f4`.

Exact witness `F=sum_(a<b)|Tr(g_a^-1 g_b)|^2` is common-left invariant and invariant under all 120 K5 label permutations. On the frozen compact path `F=24+16 cos^2(t)`, so its powers remain linearly independent. Finite K5 permutation covariance therefore cannot be the missing Iter077Q extension selector. This is scoped robustness evidence and does not strengthen Iter077Q's dimensional lower bound or define a physical extension.

## Iter080D-SM — historical implementation invalidation preserved

- prospective preregistration: `a61780f9f84cf2ecff0e4a09993322f37e310d4c`
- source lock: `24e4f8a33efe9305e62656bf942157b00223ca62`
- initial implementation: `965a9dbcb4fe44b0148a8a7d6317e2d307691dc1`
- workflow: `1d561cfe4e076f3d2674ebe0fc06c9ecaa6391c4`
- initial failed run: `34826699091`, non-authoritative
- first repair head: `849eddbac5fab7dd44fdea3b6d2b3f083a8e9c9a`
- historical successful run: `34826763762`
- historical aggregate artifact: `10339603905`, digest `sha256:835762c129e220d66cb7dab7b2e7a19da98e6f1b8e60e32cdf80764d71b78f36`
- historical Researcher result: `results/ITER080D_SM_FINITE_SCALAR_SELECTOR_OBSTRUCTION_RESULT.md`, commit `f20f3cfc3e17b4981c85482bf0ab874dbbf91672`
- Critic implementation review: `INVALID_IMPLEMENTATION`, commit `5893f567c8683e239862d754d6496c15f41528bd`

The historical successful run remains non-authoritative because executable Lane B sampled a finite grid instead of making PASS depend on the universal rank-nullity certificate required by the frozen preregistration. This chronology is retained and is not rewritten.

## Iter080D-SM — control-only universal repair — AUTHORITATIVE PASS, EXACT SCOPED

The scientific contract was unchanged.

- control-only repair plan: `4039d69cd2e2e2da595a14e6a5f56f7d06f5e9b2`
- repaired implementation / production head: `31bc800aca1b8c6179b96eef0d0ec71b106dfe53`
- authoritative run: `34830802802`
- jobs: A `103933439707`, B `103933439970`, C `103933440040`, aggregate `103933485071`
- aggregate artifact: `10342436008`
- digest: `sha256:731a83d348b89689fc51b22ce610b377079d6cc40617a8f87040054ca768bad4`
- durable result: `results/ITER080D_SM_CONTROL_ONLY_UNIVERSAL_REPAIR_RESULT.md`, commit `e77b2c39562f8c4128ae22eaa4fcc6f22ac1af01`
- independent Critic review commit: `fad81e63a7c5b71a02a4bbc1a6b6a90e18c6c3d9`
- current classification: `ITER080D_SM_FIXED_FINITE_SCALAR_LINEAR_RENORMALIZATION_CONDITIONS_CANNOT_SELECT_ITER077Q_INFINITE_FUNCTION_SPACE_AMBIGUITY_EXACT_THEOREM_SCOPED`
- verdict: `PASS_EXACT_SCOPED`.

The repaired executable certificate quantifies over every fixed finite integer `m>=0` and arbitrary `R>=1`: with `N=m+R-1`, `dim W_N=m+R`, rank at most `m`, so `dim ker(L|W_N)>=R`. Since `R` is arbitrary, every fixed finite scalar-valued complex-linear selector `L:W->C^m` has infinite-dimensional kernel. Scope excludes function-valued/infinite condition families, differential/spectral/microlocal equations, nonlinear selectors, and genuinely source-derived joint-K5 prescriptions.

## Iter080E-SM — joint-K5 primary selector census — AUTHORITATIVE BLOCKED_OBJECT_DEFINITION

Prospective object: test whether the complete frozen primary BCG/Beltran causal-Toller corpus explicitly supplies a correlated joint-K5 extension selector acting on the full Iter077Q function-space ambiguity while respecting source ordering.

- preregistration: `f1a465a059f7c4da8270bed8021f920013b7f5da`
- source snapshot: `d51f7cc0f6970670cef1e73223b30cb70b00b8c0`
- source matrix: `57de797b4db6c179a9dea7c05ef45dc0ae05f990`
- initial implementation: `5b438cfc54cfe218add8fdbe4b32269c26a763a6`
- workflow/head: `542d81dc53d4b9afae5bab3d08ad0d01da0727c2`
- initial run `34831623440`: terminal failure before aggregate, non-authoritative; failure was two brittle CURRENT prose matches in provenance Lane D, not a scientific result
- control-only repair plan: `18cc3355d86d02b1705ce593a73560409c6e460a`
- repaired implementation/head: `ff8b1b1c4eaff1d91ad0e71f5932991b0fae81c3`
- authoritative run: `34831723415`
- jobs: A `103936364224`, B `103936364455`, C `103936364066`, D `103936364289`, aggregate `103936438154`
- artifacts: A `10342502693` (`sha256:6a0bc056d524d9f9a833fdef8ca9b3c20e91586807340fdf55213572127cd9b6`); B `10342313058` (`sha256:0acd16487d54680887df42e91606bf3869d73837f0b604343de7fb1df085cc57`); C `10342551437` (`sha256:bef4ca1c95302f6f507e9b32319bdaea40115686ad017ace46fa380822ab2ae8`); D `10341873858` (`sha256:f3bed004b5789cbde61c353e0a6284e906d212d29e49bf86b8f5d282f2e18f69`)
- aggregate artifact: `10342288214`
- aggregate digest: `sha256:deb957247a902aa92f6c432639da02c9c8492ca54edfd430b3e94ad7a6ed42e6`
- durable aggregate: `analysis/iter080e_sm_aggregate_result.json`, commit `c99451e73cda9cafe63ee082a6eaf139769b79a0`
- durable result: `results/ITER080E_SM_JOINT_K5_SELECTOR_SOURCE_AUDIT_RESULT.md`, commit `f3cc75c2aba3eee9677a6d0ca8b6bd0d358397bc`
- classification: `ITER080E_SM_PRIMARY_CAUSAL_TOLLER_CORPUS_HAS_NO_JOINT_K5_FUNCTION_SPACE_EXTENSION_SELECTOR_SOURCE_BLOCKED_EXACT_AUDIT_SCOPED`
- verdict: `BLOCKED_OBJECT_DEFINITION`.

Lane outcomes: A `PASS_SOURCE_COVERAGE`; B `BLOCKED_OBJECT_DEFINITION`; C `PASS_CLASSIFIER_CONTROLS`; D `PASS_DEPENDENCY_LOCK`. No real primary-source row satisfies all five frozen selector requirements P1-P5.

BCG arXiv:2601.23162 supplies the one-wedge spectral branch and the formal ten-Toller single-vertex product/group-integral expression, but no explicit correlated joint-K5 collision extension/finite part/contour/interchange/uniqueness prescription on the full Iter077Q `W`. BCG arXiv:2604.24945 supplies one-wedge/local Toller analytic identities but no such joint selector. Beltran arXiv:2603.22661v2 supplies arbitrary-2-complex causality and generalized causal local vertices but no joint Iter077Q collision-extension selector or uniqueness theorem.

Scientific ceiling: this is a source-object-definition obstruction for the frozen corpus, not a theorem that no selector or causal-vertex distribution can exist. It does not establish divergence, regulator independence, E7/E8, G3, RG, continuum, spin-2, GR, matter/QFT, predictions, new physics, or complete quantum gravity.

## Controlling upstream authority retained

`status/ITER077_CONTACT_FORMULA_ERRATUM.md` remains controlling for source formulas; historical Iter077E/F remain `NON_AUTHORITATIVE_SOURCE_LOCK_INVALID`.

Iter077I authoritative run remains `34786586785`, after the execution-invalid first run `34786550378`; its ceiling remains non-local-L1 only, not distributional nonexistence.

Iter077Q remains the controlling local extension result: `BLOCKED_INFINITE_DIMENSIONAL_EXTENSION_SELECTOR_MISSING`.

## Forward authority

Do not repeat finite K5 permutation symmetry, fixed-finite-scalar selectors, neighboring invariant-polynomial witnesses, or the frozen BCG/Beltran primary-source selector census absent genuinely new/revised primary authority.

The source-defined CRQN v0.2 local amplitude still lacks a unique full-function-space joint-K5 selector. The independent physical E3/E4/E6 causal multivertex source bridge also remains blocked.

The next admissible Researcher gate is an anti-rescue census of the **pre-existing CRQN v0.2 model/axiom specification** for an independently motivated full-function-space selector already present before the Iter077Q obstruction was identified. This gate must not invent a new mechanism. If no such pre-existing selector exists, CRQN v0.2 remains blocked at the local-amplitude arrow until genuinely new/revised primary authority or a separately motivated, prospectively testable candidate version is introduced.
