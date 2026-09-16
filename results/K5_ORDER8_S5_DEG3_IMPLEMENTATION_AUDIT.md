# K5 S5 degree-three logarithmic IBP gate — implementation audit

Date: 2026-09-16

Reviewed frozen contract: `prereg/K5_ORDER8_S5_DEG3_FACE_TANGENT_LOG_IBP_SYZYGY.md`, commit `b93145159d9535992208a15a56c33b13732ad155`.

Reviewed implementation: `scripts/k5_order8_s5_deg3_log_ibp_syzygy.py`, commit `9ac72afa36ca5ea6cc4b92c995b7458d239eff03`.

Workflow head: `5de959438e6a8079f31f2e8924e55aeddeedf1ab`, run `35042066501` was still non-terminal at audit time. No substantive run value, rank, nullity, or scientific classification was used in this audit.

## Frozen-control mismatch

The preregistration requires the same validator to:

1. reject at least one non-face-tangent field;
2. reject at least one S5-breaking field;
3. reject at least one fake logarithmic field;
4. run a synthetic homogeneous symmetric fixture through the same construction and exhibit a genuine non-radial degree-three logarithmic direction.

The frozen implementation does not satisfy that mandatory control contract:

- `fake_logarithmic_rejected` is genuinely evaluated;
- `face_tangent_by_alpha_factor` is hard-coded `True` rather than a malformed-candidate rejection;
- there is no S5-breaking malformed-candidate rejection path;
- `synth=True` is assigned analytically and the synthetic polynomial is not passed through the same matrix/nullspace construction.

Thus `valid=all(checks.values()) and all(controls.values())` can become true without executing three mandatory frozen controls.

## Verdict

`INVALID_IMPLEMENTATION`

This is an outcome-independent implementation verdict. It does **not** state whether the degree-three K5 logarithmic quotient is radial-only or non-radial. Any arithmetic emitted by run `35042066501` may be used only as exploratory/debug information until a prospectively frozen control-only repair reproduces the scientific solve with all mandatory controls actually executed.

## Authorized repair

A control-only repair may retain without change:

- the K5 125-tree Kirchhoff object;
- the complete fixed-edge-stabilizer orbit construction;
- the complete S5-invariant quadratic quotient basis;
- exact rational coefficient matching;
- the original scientific outcome labels and interpretation ceiling.

The repaired implementation must additionally execute the missing malformed face/S5 controls and send the synthetic fixture through the same generic matrix/nullspace engine. No scientific threshold, ansatz, object, or outcome definition may change.
