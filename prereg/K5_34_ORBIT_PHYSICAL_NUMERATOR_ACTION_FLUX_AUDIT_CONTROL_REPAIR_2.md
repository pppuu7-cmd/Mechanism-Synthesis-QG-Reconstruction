# K5 34-orbit physical numerator/action-flux audit — control repair 2 preregistration

Status: **PROSPECTIVELY FROZEN BEFORE ANY REPAIR-2 PRODUCTION OUTCOME**.

This supersedes the unexecuted repair-1 implementation plan only for computational efficiency. No repair-1 production output has been observed. The scientific gate, witnesses, weights, primes, orbit representatives, channels, exponents, PASS/BLOCKED rule, and interpretation ceiling remain unchanged.

Parent gate preregistration: `9c42a26350e547eb02649c6ee44f8dd2477100d0`.
Failed implementation run: `35150430183` / job `104977054981`.
Repair-1 preregistration: `3143586174f977da12afc68218a2dd5064b2e2ab` (not executed).

## Frozen diagnosis

The crash occurs because the compact `LT` algebra evaluates `det(L)` through the signed Leibniz formula while retaining only one leading monomial. Exact cancellations among signed determinant terms can erase that stored monomial even when the true determinant is nonzero at the next order. This is an implementation artifact of the determinant representation, not a scientific cancellation verdict.

The repository already has an independently validated canonical Kirchhoff polynomial authority `PSI_POLY` with exactly 125 spanning-tree monomials and coefficient +1. For the K5 reduced Laplacian, this polynomial is exactly `det(L)`.

## Repair-2 execution rule

1. Keep the existing eight frozen leading-term lanes, both primes, both asymmetric weights, and S5-permuted controls unchanged.
2. Compute `Psi(alpha)` directly from the frozen authoritative `PSI_POLY`:
   `Psi = sum_{T spanning tree} prod_{e in T} alpha_e`.
   Do not compute the denominator determinant through the signed Leibniz expansion.
3. Compute `L^{-1}` by the adjugate/cofactor formula using the same LT/AD arithmetic for the 3x3 minors and divide every cofactor by the directly evaluated `Psi`.
4. The AD derivative of `Psi` is obtained automatically by evaluating the same 125-tree polynomial on the same AD alpha values; no fitted derivative or expected order is inserted.
5. Keep the existing downstream evaluation, source compression, numerator construction, projective tangent field, action formula, certification, S5 covariance checks, and all local exponent formulas unchanged.
6. Add controls requiring:
   - `len(PSI_POLY)==125` and all coefficients are exactly +1;
   - direct-tree `Psi` order equals the independently computed combinatorial `tree_order(Z)` for every proper orbit;
   - a frozen generic LT point gives exact agreement between direct-tree `Psi` and the signed determinant when no leading cancellation occurs;
   - empty/full subsets remain controls only.
7. If any later non-denominator quantity has unresolved leading cancellation, do **not** repair or retune it. Preserve the parent behavior: mark that component `BLOCKED_CANCELLATION_RESOLUTION`.
8. Any denominator failure after this repair is `INVALID_IMPLEMENTATION`, not scientific FAIL.

## Terminal classifier

Unchanged:

- `INVALID_IMPLEMENTATION` if implementation/authority/coverage controls fail;
- `K5_34_ORBIT_PHYSICAL_NUMERATOR_ACTION_FLUX_PARTIAL_BLOCKED_SCOPED` if at least one of 64 physical channel-orbit components is not certified;
- `K5_34_ORBIT_PHYSICAL_NUMERATOR_ACTION_FLUX_AUDIT_EXACT_SCOPED` only if all 64 are certified.

No global Stokes/IBP or integrated-period conclusion is authorized by this repair.
