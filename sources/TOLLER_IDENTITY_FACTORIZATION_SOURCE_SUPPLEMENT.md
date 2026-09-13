# Toller identity factorization source supplement

Date: 2026-09-13

## Primary sources

1. E. Bianchi, C. Chen, M. Gamonal, **Causal spinfoam vertex for 4d Lorentzian quantum gravity**, arXiv:2601.23162 (2026), published as Phys. Rev. D 113, 126020 (2026).
2. E. Bianchi, C. Chen, M. Gamonal, **Toller matrices and the Feynman i-epsilon in spinfoams**, arXiv:2604.24945 (2026), published as Phys. Rev. D 114, 046014 (2026).

This supplement records only source facts needed to define the next local factorization gate. Algebraic series below are derived from the displayed source formulas and are explicitly marked as derived controls.

## Source locks

### S1 — additive branch relation

Both papers state the exact additive relation

`T^(+) + T^(-) = D`,

where `D` is the Lorentz-group Wigner matrix. The individual Toller objects are not themselves group representations.

### S2 — second-kind / frequency character

The companion paper identifies the reduced Toller matrices with Ruhl's functions of the second kind and, in its boost-eigenvalue representation, with the positive- and negative-frequency components of the Wigner reduced matrix. The branch split is therefore analytic/distributional data and is not equivalent to splitting a smooth representation matrix into two ordinary Taylor germs at the identity.

### S3 — exact Barrett-Crane branch control

For the exact special case `k=j=l=0`, `rho != 0`, Eq. (10) of the causal-vertex paper gives

`t^(+)(beta) = +(1/(2 i rho)) exp(+i rho beta)/sinh(beta)`,

`t^(-)(beta) = -(1/(2 i rho)) exp(-i rho beta)/sinh(beta)`,

and

`d(beta) = sin(rho beta)/(rho sinh(beta))`.

The source also has `t^(+) + t^(-) = d`.

## Derived exact local controls

The following are elementary series consequences of S3 and are not quoted source statements.

### D1 — individual branches are not regular Taylor germs at beta=0

Using

`1/sinh(beta) = 1/beta - beta/6 + O(beta^3)`,

one obtains

`t^(+)(beta) = 1/(2 i rho beta) + 1/2 + O(beta)`,

`t^(-)(beta) = -1/(2 i rho beta) + 1/2 + O(beta)`.

Hence each individual branch has a simple `1/beta` singularity at the identity in this exact source-backed control. The ordinary derivative `d t^(+/-)/d beta |_(beta=0)` is therefore not a valid smooth one-jet object.

### D2 — the branch sum is smooth and has zero linear term

The singular pieces cancel in

`d(beta) = sin(rho beta)/(rho sinh(beta))`

and

`d(beta) = 1 - (rho^2 + 1) beta^2/6 + O(beta^4)`.

Thus smooth evenness of the Wigner sum does not imply evenness of a regularized/factorized individual branch numerator.

### D3 — canonical pole-stripped branch control has a generic nonzero one-jet

For this exact Barrett-Crane branch only, define the dimensionless pole-stripped regular factors

`N_+(beta) := (+2 i rho beta) t^(+)(beta)`,

`N_-(beta) := (-2 i rho beta) t^(-)(beta)`.

Then exactly

`N_+(beta) = exp(+i rho beta) beta/sinh(beta)`,

`N_-(beta) = exp(-i rho beta) beta/sinh(beta)`,

so

`N_+(beta) = 1 + i rho beta - (rho^2/2 + 1/6) beta^2 + O(beta^3)`,

`N_-(beta) = 1 - i rho beta - (rho^2/2 + 1/6) beta^2 + O(beta^3)`.

Therefore

`N_+'(0) = +i rho`,

`N_-'(0) = -i rho`,

which is nonzero for generic `rho != 0`.

This is a source-backed exact counterexample to any universal claim that a regular factor attached to an individual Toller branch must be even at the identity.

## Independent Appendix-D/contact control already in the repository

The source-derived `j=1/2` Appendix-D polynomial used by `distributional/jhalf_iepsilon_validation.py` is

`F = 1 + c1 sigma q + (c2/2)(sigma q)^2`,

with

`c1 = 2 rho/(rho^2 + 1/4)`,

`c2 = 2/(rho^2 + 1/4)`,

and

`delta^(rho,1/2) = -i c1 delta - (c2/2) delta'`.

For generic `rho != 0`, `c1 != 0`. This control lives in the spectral/contact variable and must **not** be identified with the source group-coordinate/cut-space one-jet. Its role is only to exclude an unsupported universal source-evenness assumption.

## Scope lock

This supplement does **not** define the physical EPRL/Toller wedge numerator one-jet, the full boundary-intertwiner contraction one-jet, the nonlinear source-to-K4 curvature, or the nominal `epsilon^-1` coefficient. It only proves that:

1. the naive derivative of an individual Toller branch at the identity can be ill-defined because of the branch singularity;
2. smoothness/evenness of `T^(+)+T^(-)=D` cannot be transferred to an individual causal branch;
3. an exact source-backed pole-stripped branch control can have a nonzero regular one-jet.

The next source-faithful task is to define which singular/contact factor is removed in the gamma-simple EPRL/Toller wedge and how the remaining regular factor enters the full boundary/intertwiner contraction.