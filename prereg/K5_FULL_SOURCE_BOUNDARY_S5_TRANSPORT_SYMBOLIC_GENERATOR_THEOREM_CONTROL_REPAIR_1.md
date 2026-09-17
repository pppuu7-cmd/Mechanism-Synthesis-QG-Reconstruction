# Control-only repair 1 — symbolic full-source boundary S5 transport theorem

Date: 2026-09-17

Parent scientific preregistration remains unchanged:

`prereg/K5_FULL_SOURCE_BOUNDARY_S5_TRANSPORT_SYMBOLIC_GENERATOR_THEOREM.md`, commit `4f65cff503db976b6ff52b8519e5fdaa0bf4a4f8`.

Historical production attempt `35200249024` is terminal workflow failure and scientifically `INVALID_IMPLEMENTATION`. It produced no scientific verdict. Its exact structural controls showed: generated group size 120, 125-tree `Psi`, exact C/T covariance transport, C formal pattern equality, but T formal pattern equality failed while the validator's `remove source reversal sign` malformed control was not rejected. Therefore the attempt cannot be interpreted as either PASS or scientific FAIL.

## Frozen diagnosis before repair

The implementation placed the canonical-edge orientation character in the source-pattern layer but compared that layer directly with the contragredient boundary law while separately verifying the covariance orientation law. For any complete Wick term, however, every one of the ten K5 edges occurs exactly once in a perfect matching. Under a vertex permutation `p`:

- the source matrix reversal contributes the universal factor
  `g_source = product_e s_e`;
- pullback of the five covariance factors contributes
  `g_cov = product_e s_e`;
- hence the complete formal Wick monomial carries
  `g_source * g_cov = (product_e s_e)^2 = 1`.

For the odd transposition both individual factors are `-1`; omitting both can therefore spuriously imitate the correct complete sign while omitting either one separately is malformed. The historical validator tested a raw subfactor rather than the complete formal Wick coefficient object frozen by the parent theorem.

This is an implementation/control-placement error, not a change to the parent hypothesis, exact physical object, generators, source authority, PASS/FAIL meanings, or interpretation ceiling.

## Frozen repair

1. Retain the exact symbolic covariance-numerator identity already implemented.
2. In the formal source/boundary dictionary comparison, include the mechanically known universal covariance matching orientation factor together with the source reversal factor before comparison to `A_p^(-T)`. No covariance numerical value is substituted; this remains a formal coefficient-level comparison.
3. Keep source endpoint transpose on canonically reversed edges unchanged.
4. Add separate malformed controls:
   - omit transpose while retaining both orientation factors -> rejected;
   - omit only source reversal sign while retaining covariance orientation factor -> rejected;
   - omit only covariance orientation factor while retaining source reversal sign -> rejected;
   - omit both orientation factors and/or hold the source fixed -> cannot be accepted as a valid implementation path, even if an accidental character cancellation occurs in a subfactor.
5. Preserve exact C/T covariance polynomial transport, all-32/100000-term coverage, group-size 120, no numerical alpha witnesses, no interpolation, no fitted phase and no fitted 2x2 matrix.

## Scientific contract unchanged

The only admissible scientific classifications remain exactly those frozen by the parent preregistration:

- `K5_FULL_SOURCE_BOUNDARY_S5_SYMBOLIC_ALL_ALPHA_TRIVIAL_CHARACTER_EXACT_SCOPED`;
- `K5_FULL_SOURCE_BOUNDARY_S5_SYMBOLIC_TRANSPORT_OBSTRUCTION_EXACT_SCOPED`;
- non-scientific invalid/provenance/infrastructure outcomes.

No result from run `35200249024` may be promoted or used as a substantive value except the completed implementation diagnostics stated above.
