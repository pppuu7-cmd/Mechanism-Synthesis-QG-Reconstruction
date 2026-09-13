# Iter075E preregistration — exact Appendix-D branch-flip kernel identity

Date: 2026-09-13

## Frozen objective

Upgrade the Iter075C/075D high-precision held-out relation to an exact algebraic certificate for the Appendix-D polynomial/Feynman kernel family, without extending it to a full `SL(2,C)` Toller-function inversion law.

For admissible nonnegative half-integers `j,l` with `j+l` integer, define

`P_jl(x;rho) = product_{n=0}^{j+l} (i x - (n-j))/(i rho - (n-j))`

and

`K_s(j,l) = s/(x-rho-i s epsilon) * P_jl(x;rho)`

(up to source-common normalization irrelevant to the identity).

The frozen target is

`P_jl(x;rho) = conjugate(P_lj(x;rho))`

for real `x,rho`, and consequently

`K_s(j,l) = -conjugate(K_-s(l,j))`.

## Frozen exact proof obligations

1. Index-set map: `{n-l | n=0..j+l}` under `q -> -q` equals `{n-j | n=0..j+l}` exactly.
2. Conjugating every factor of `P_lj` at real `x,rho` maps it to the corresponding factor of `P_jl` under that index bijection.
3. The Feynman pole prefactor obeys exact branch-flip/minus/conjugation under `s -> -s` with fixed real spectral contour and unchanged `epsilon>0`.
4. Exhaustive symbolic controls for all `2j,2l in [0,16]` with `j+l` integer must return exact zero residuals.
5. Inadmissible parity pairs (`j+l` half-integer) are excluded, not fitted or coerced.
6. A deliberately wrong same-branch conjugation must fail on at least one unequal-spin admissible pair, preventing accidental collapse to the old Iter059 equal-spin law.

## Frozen interpretation

- PASS: `ITER075E_APPENDIXD_BRANCHFLIP_KERNEL_IDENTITY_EXACT_SCOPED`.
- SCIENTIFIC FAIL: `ITER075E_APPENDIXD_BRANCHFLIP_KERNEL_IDENTITY_OBSTRUCTED_SCOPED` if any exact proof obligation fails.
- INFRA/IMPLEMENTATION FAIL only for inability to execute the exact symbolic checks; no threshold relaxation is permitted.

Even PASS is an exact identity for the source Appendix-D polynomial/Feynman-kernel factor only. It does not by itself establish the complete branch/order-reversal law for unequal-spin Toller functions on `SL(2,C)`, does not select a physical causal sector, and does not promote K5/G3/F9/G8 or imply vertex finiteness/divergence/new physics.
