# Iter078M-RG result — no full-rank Jacobian witness in the three prospectively frozen generic controls

**Date:** 2026-09-14

## Provenance

- Prospective preregistration: `prereg/ITER078M_RG_GENERIC_SELECTOR_JACOBIAN_RANK.md`, commit `4e3cf30e94e5ad6a6a0aafd399357fd10b119c78`.
- Implementation: `distributional/iter078m_rg_generic_selector_rank.py`, commit `e491c3684278bbdc45bbfc221cd066485f270bac`.
- Workflow/production head: `.github/workflows/iter078m_rg_generic_selector_rank.yml`, commit `695f3bf0753512f73f81ab6f100605a770ba51ee`.
- Authoritative run: `34791083678`.
- Aggregate artifact: `10328207562`, digest `sha256:9ad6f4c49a2840e7a2fdb6e8807c8e71da911ddbc029c99f3c557379d404bb82`.
- Lane artifacts:
  - A `10328745682`, digest `sha256:1944b9fc2b75543b51367551b07e8ea417dab1b0c677a468113a4e878afdddd9`;
  - B `10327966908`, digest `sha256:19fbf598bd2a089278f28b415d2df0195d4c881a3ad84b98f30bf53d7a8c42ca`;
  - C `10328701181`, digest `sha256:ef1214d79f00b2270b1ba0aad1259e71756841b498517465a5bb04ab2a511219`;
  - L `10327597913`, digest `sha256:b0f4942b7f2fb16f4a252b90d74f88bfaa51c713ebfe1437ed2de5f22d303ece`.

## Classification

`ITER078M_RG_NO_FULL_RANK_WITNESS_IN_FROZEN_GENERIC_CONTROLS`

Scientific verdict: **INCONCLUSIVE_GENERIC_RANK**.

## Exact findings

The exact Jacobian of the fixed-all-`j=1/2` degree-5 EPRL-edge-weight control map was evaluated at the four prospectively frozen tensors:

- A: `C_i=i+1`;
- B: `C_i=(-1)^popcount(i)(i+1)`;
- C: `C_i=(i+1)^2`;
- L: compact Iter077N tensor.

All four exact ranks over `Q` are `31`, with nullity `1`.

No lane produced a rank-32 witness, so no nonzero determinant certificate was obtained.

Jacobian checksums:

- A: `0f83d9c5bb64401a62750b12ac1ae730c948eedc516040a0ea54b0141cb7a78a`;
- B: `387ed43e0a7f6fd54c6e1f1eb0397ea0e5ebc46be9d9fff4e0603b4afbc29e2f`;
- C: `aa77c943857dc5978f63651cf4b7a8ed165bff81fbee9f2b4b31beae4a3c332a`;
- L: `58369f1b75ccbb61cb5a6277521b541f8dd73c223fc5d3b1c9a7d889d667a764`.

## Interpretation ceiling

The result does **not** prove that the map has generic rank 31 or that its Jacobian determinant vanishes identically. The preregistration explicitly froze only three generic-control tensors plus L; failure to find a rank-32 witness in that finite set is not a rank-ceiling theorem.

However, the repeated exact rank-31 outcome at algebraically very different frozen points makes a structural identity a high-information next hypothesis.

## Exact next admissible step

Do not add more unconstrained random samples first. Prospectively test whether the map obeys a universal output linear relation:

1. compute exact primitive **left** null vectors of the Jacobian at A/B/C/L;
2. determine whether they are identical/proportional;
3. if a common left vector `w` exists, form the exact homogeneous polynomial `P_w(C)=w·R(C)` coefficientwise by enumerating the complete tensor-network monomials;
4. prove or refute `P_w(C)≡0` exactly.

If the polynomial identity holds, it gives a structural image hyperplane and a global rank ceiling `<=31`; if it fails, the repeated rank-31 samples remain local coincidences and a broader prospective witness search becomes admissible.