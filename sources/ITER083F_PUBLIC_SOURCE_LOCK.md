# Iter083F public-source lock — finite spectral epsilon and the j=1/2 small-boost singularity

Date audited: 2026-09-15

Purpose: freeze only source formulas and their direct finite-epsilon contour consequence used by prospective Iter083F. The common-epsilon ten-wedge construction is an exploratory new construction, not part of the published causal-vertex definition.

## Source A — Bianchi, Chen, Gamonal, `arXiv:2604.24945`

### A1. Finite-epsilon functional

Eq. (16) defines

`P_jl(rho_tilde;rho) = product_(n=0)^(j+l) [i rho_tilde-(n-j)]/[i rho-(n-j)]`.

Eq. (17) defines, before taking any epsilon limit,

`I_epsilon^(+-)[f] = integral_R d rho_tilde/(2 pi i) [+- P_jl(rho_tilde;rho)/(rho_tilde-rho -+ i epsilon)] f(rho_tilde)`.

The surrounding contour argument states:

- `P_jl t^+` and `P_jl t^-` have their Toller poles cancelled;
- for `I_epsilon^+[t^+]`, the only remaining pole is `rho_tilde=rho+i epsilon`, enclosed by the upper contour;
- for `I_epsilon^+[t^-]`, the contour closes in the lower half-plane and the shifted pole is outside, so the cross term vanishes;
- analogously for `I_epsilon^-`.

Although the paper writes the final statements with `lim_(epsilon->0+)`, the residue calculation preceding that limit is pointwise in fixed admissible `epsilon>0`. Therefore the direct finite-epsilon consequence of the stated contour argument is

`I_epsilon^+[d] = P_jl(rho+i epsilon;rho) t^+(rho+i epsilon,beta)`,

`I_epsilon^-[d] = P_jl(rho-i epsilon;rho) t^-(rho-i epsilon,beta)`.

This finite-epsilon object is used only as an exploratory candidate regulator in Iter083F.

### A2. Gamma-simple specialization

Around Eqs. (45)-(46), the paper specializes to

`k=j=l`, `rho=gamma j`.

For the frozen minimal-spin sector,

`j=l=k=1/2`, `rho=gamma/2`.

### A3. Explicit Table-II j=1/2 branches

For `k=j=l=1/2`, `m=+1/2`, Table II gives

`t^+(rho,beta) = - exp(+i rho beta) / [2 sinh(beta)^2 (rho+i/2)(rho-i/2)]`,

`t^-(rho,beta) = + exp(-i rho beta) [cosh(beta)+2 i rho sinh(beta)] / [2 sinh(beta)^2 (rho+i/2)(rho-i/2)]`.

For `m=-1/2`, Table II gives

`t^+(rho,beta) = + exp(+i rho beta) [cosh(beta)-2 i rho sinh(beta)] / [2 sinh(beta)^2 (rho+i/2)(rho-i/2)]`,

`t^-(rho,beta) = - exp(-i rho beta) / [2 sinh(beta)^2 (rho+i/2)(rho-i/2)]`.

These formulas exhibit the one-wedge `beta^-2` singularity directly.

### A4. j=1/2 kernel

Substituting `j=l=1/2` into Eq. (16) gives exactly

`P_(1/2,1/2)(rho_tilde;rho) = (rho_tilde^2+1/4)/(rho^2+1/4)`.

This follows because the two factors are `(i rho_tilde+1/2)(i rho_tilde-1/2)` divided by the same expression at `rho`, and the common minus sign cancels.

### A5. Direct finite-epsilon formulas

Set `rho_+=rho+i epsilon`, `rho_-=rho-i epsilon`. Multiplying the Table-II branches by the kernel cancels the entire shifted denominator `rho_+/-^2+1/4`.

The resulting fixed-epsilon functions are

`I_epsilon^+[d]_(m=+1/2) = - exp(+i rho beta) exp(-epsilon beta) / [2(rho^2+1/4)sinh(beta)^2]`,

`I_epsilon^+[d]_(m=-1/2) = + exp(+i rho beta) exp(-epsilon beta) [cosh(beta)-2 i rho sinh(beta)+2 epsilon sinh(beta)] / [2(rho^2+1/4)sinh(beta)^2]`,

`I_epsilon^-[d]_(m=+1/2) = + exp(-i rho beta) exp(-epsilon beta) [cosh(beta)+2 i rho sinh(beta)+2 epsilon sinh(beta)] / [2(rho^2+1/4)sinh(beta)^2]`,

`I_epsilon^-[d]_(m=-1/2) = - exp(-i rho beta) exp(-epsilon beta) / [2(rho^2+1/4)sinh(beta)^2]`.

Thus `exp(-epsilon beta)=1+O(beta)`, `cosh(beta)=1+O(beta^2)`, and `sinh(beta)=beta+O(beta^3)`. Every branch has the same nonzero `beta^-2` leading coefficient as at epsilon zero.

### A6. Barrett-Crane example as a non-authoritative cross-check

The paper's `j=k=l=m=0` example similarly gives a finite-epsilon residue with exponential factor `exp(-epsilon beta)` multiplying the usual `1/sinh(beta)` behavior. This is consistent with the mechanism above but is **not** used as authority for the physical frozen j=1/2 result.

## Source B — Bianchi, Chen, Gamonal, `arXiv:2601.23162v1`

The causal-vertex paper defines each elementary Toller matrix by first taking the one-wedge Feynman limit `epsilon->0+`, then forms the ten-factor K5 vertex product and group integrals.

Therefore keeping one common finite epsilon in all ten spectral integrals and multiplying/integrating before the limit is a new exploratory construction, not the published source order.

## Repository authority used downstream

- Iter077I: at epsilon zero the full frozen j=1/2 Toller matrix has the same beta^-2 magnitude `2/(1+gamma^2)` in each branch, and the ten-wedge frozen angular contraction is nonzero at order `r^-20`.
- Iter077L/M: common collision codimension is 12 and source scaling degree is 20.
- Iter083B: same-scaling-degree supported ambiguity dimension is 377.
- Iter083E: one-wedge epsilon uniqueness is not a joint K5 selector; a genuinely joint construction remains an open target.

## Claim locks

1. `epsilon` in this test is a shift in the spectral variable `rho`, not in the group-normal rapidity `beta`.
2. A factor `exp(-epsilon beta)` tends to one at the collision and is not UV damping there.
3. No factor `exp(-epsilon/beta)` occurs in the source contour prescription.
4. The common finite-epsilon ten-wedge construction is not claimed as published authority.
5. Failure of this simple candidate does not rule out all correlated K5 regulators.
