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

## Iter080E-SM — historical source-census production — INVALID_IMPLEMENTATION

Prospective object: test whether the complete frozen primary BCG/Beltran causal-Toller corpus explicitly supplies a correlated joint-K5 extension selector acting on the full Iter077Q function-space ambiguity while respecting source ordering.

- preregistration: `f1a465a059f7c4da8270bed8021f920013b7f5da`
- source snapshot: `d51f7cc0f6970670cef1e73223b30cb70b00b8c0`
- source matrix: `57de797b4db6c179a9dea7c05ef45dc0ae05f990`
- initial implementation: `5b438cfc54cfe218add8fdbe4b32269c26a763a6`
- workflow/head: `542d81dc53d4b9afae5bab3d08ad0d01da0727c2`
- initial run `34831623440`: terminal failure before aggregate, non-authoritative; failure was two brittle CURRENT prose matches in provenance Lane D
- control-only repair plan: `18cc3355d86d02b1705ce593a73560409c6e460a`
- repaired implementation/head: `ff8b1b1c4eaff1d91ad0e71f5932991b0fae81c3`
- historical terminal run: `34831723415`
- jobs: A `103936364224`, B `103936364455`, C `103936364066`, D `103936364289`, aggregate `103936438154`
- artifacts: A `10342502693` (`sha256:6a0bc056d524d9f9a833fdef8ca9b3c20e91586807340fdf55213572127cd9b6`); B `10342313058` (`sha256:0acd16487d54680887df42e91606bf3869d73837f0b604343de7fb1df085cc57`); C `10342551437` (`sha256:bef4ca1c95302f6f507e9b32319bdaea40115686ad017ace46fa380822ab2ae8`); D `10341873858` (`sha256:f3bed004b5789cbde61c353e0a6284e906d212d29e49bf86b8f5d282f2e18f69`)
- aggregate artifact: `10342288214`
- aggregate digest: `sha256:deb957247a902aa92f6c432639da02c9c8492ca54edfd430b3e94ad7a6ed42e6`
- historical durable aggregate: `analysis/iter080e_sm_aggregate_result.json`, commit `c99451e73cda9cafe63ee082a6eaf139769b79a0`
- historical Researcher result: `results/ITER080E_SM_JOINT_K5_SELECTOR_SOURCE_AUDIT_RESULT.md`, commit `f3cc75c2aba3eee9677a6d0ca8b6bd0d358397bc`
- historical Researcher classification: `ITER080E_SM_PRIMARY_CAUSAL_TOLLER_CORPUS_HAS_NO_JOINT_K5_FUNCTION_SPACE_EXTENSION_SELECTOR_SOURCE_BLOCKED_EXACT_AUDIT_SCOPED`
- independent Critic review: `results/ITER080E_ADVERSARIAL_IMPLEMENTATION_REVIEW.md`, commit `0eedd6f7630235326ef96ba75d05da44317f4d5e`
- independent Critic verdict: `INVALID_IMPLEMENTATION`
- Critic handoff commit: `a7410de505c40c40991bce7b84594e414c14b1f2`.

Researcher lane outcomes were A `PASS_SOURCE_COVERAGE`, B `BLOCKED_OBJECT_DEFINITION`, C `PASS_CLASSIFIER_CONTROLS`, D `PASS_DEPENDENCY_LOCK`, but they are not authoritative as a scientific classification.

Decisive implementation defect: Lane B reads each P1-P5 status from `analysis/iter080e_sm_joint_k5_selector_source_matrix.json`, verifies only that the matrix's own status/anchor string is present in `sources/ITER080E_SM_JOINT_K5_SELECTOR_SOURCE_SNAPSHOT.md`, and computes selector eligibility solely from those prefilled statuses. Lane A checks Git blob hashes of older evidence files but does not derive P1-P5 from their contents; Lane B never reads those older evidence files. Consequently `evidence_ok=true` is textual self-consistency between Iter080E-authored status files, not executable source evidence. This matches the preregistered invalid condition against trusting prefilled verdict/status fields.

This invalidation does not assert that a selector exists in the frozen corpus. Existing authoritative Iter077K still records that BCG `2601.23162` and `2604.24945` do not themselves supply the missing correlated common-collision prescription; Iter079A records that Beltran v2 does not select or transport the Iter077Q extension freedom. These narrower facts remain authority, while the broader P1-P5-complete Iter080E census is pending repair.

A control-only repair may preserve the unchanged scientific contract but must make Lane-B eligibility depend on source-specific frozen factual evidence, not self-authored P1-P5 status labels. Historical runs/results remain unchanged.

## Controlling upstream authority retained

`status/ITER077_CONTACT_FORMULA_ERRATUM.md` remains controlling for source formulas; historical Iter077E/F remain `NON_AUTHORITATIVE_SOURCE_LOCK_INVALID`.

Iter077I authoritative run remains `34786586785`, after the execution-invalid first run `34786550378`; its ceiling remains non-local-L1 only, not distributional nonexistence.

Iter077Q remains the controlling local extension result: `BLOCKED_INFINITE_DIMENSIONAL_EXTENSION_SELECTOR_MISSING`.

## Forward authority

First admissible Researcher action is a control-only Iter080E repair/retry under the unchanged preregistration. Every P1-P5 status must be bound to explicit source-specific frozen evidence or an independently frozen source-audit evidence structure, with eligibility dependent on those checks. Synthetic controls remain classifier controls only.

Until repaired, do not use Iter080E as an authoritative complete frozen-corpus census and do not proceed to a competing authoritative gate on the same source-census object.

If repaired Iter080E again yields no P1-P5-complete real source row, `BLOCKED_OBJECT_DEFINITION` can be restored and the next admissible Researcher gate is the anti-rescue census of the **pre-existing CRQN v0.2 model/axiom specification** for an independently motivated full-function-space selector already present before Iter077Q. This gate must not invent a new mechanism.

The source-defined CRQN v0.2 local amplitude remains blocked independently by Iter077Q/Iter077K, and the physical E3/E4/E6 causal multivertex source bridge remains separately blocked.