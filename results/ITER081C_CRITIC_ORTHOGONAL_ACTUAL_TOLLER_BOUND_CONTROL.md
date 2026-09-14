# Iter081C Critic orthogonal exact control — actual gamma-simple Toller branch vs Han projected contraction

Status: **exact Critic control following prospective object freeze; not a Researcher-A verdict.**
Date: 2026-09-14
Prospective object freeze: `results/ITER081C_PRE_GATE_ACTUAL_TOLLER_BOUND_OBJECT.md`, commit `f0ade03bc5f64cbab7d395e24d07e883b6c218a1`.

## Frozen source formula
Bianchi--Chen--Gamonal arXiv:2604.24945v1 Eq. (46) gives, for gamma-simple `k=j`, `rho=gamma j`, `l=j`, pure boost `g_beta=exp(-i beta K_z)`, `beta>0`,

`t_{jjm}^{(±,rho,j)}(beta) = exp[-(j ∓ i rho ± m +1) beta] * Gamma(2j+2) Gamma(± i rho ∓ m) / (Gamma(j ∓ m +1) Gamma(j+1 ± i rho)) * 2F1(j ± m +1, j+1 ∓ i rho; 1 ± m ∓ i rho; exp(-2 beta)).`

The prospectively frozen path is
`j=k=m=1/2`, `rho=gamma/2`, fixed real `gamma>0`, branch `+`, `beta>0`, `beta -> 0+`.

## Exact simplification
For the frozen labels,
- `a = j+m+1 = 2`,
- `b = j+1-i rho = 3/2-i rho`,
- `c = 1+m-i rho = 3/2-i rho = b`.

Since `z=e^(-2 beta)` lies in `(0,1)` for every `beta>0`, the standard exact identity
`2F1(a,b;b;z)=(1-z)^(-a)`
applies without analytic-continuation ambiguity. Therefore

`t_+(beta) = exp[-(2-i rho) beta] * Gamma(3) Gamma(i rho-1/2) / Gamma(3/2+i rho) * (1-e^(-2 beta))^(-2).`

Using `Gamma(3)=2` and twice the gamma recurrence,
`Gamma(3/2+i rho)=(1/2+i rho)(-1/2+i rho) Gamma(-1/2+i rho)`.
Thus

`Gamma(i rho-1/2)/Gamma(3/2+i rho) = -1/(rho^2+1/4)`

and the actual Toller matrix element is exactly

`t_+(beta) = -[2/(rho^2+1/4)] exp[-(2-i rho) beta] / (1-e^(-2 beta))^2.`

## Exact magnitude and counterexample
For real `rho`,

`|t_+(beta)| = [2/(rho^2+1/4)] e^(-2 beta)/(1-e^(-2 beta))^2
              = 1/[2(rho^2+1/4) sinh^2(beta)]
              = 2/[(1+gamma^2) sinh^2(beta)]`,

where in the last equality `rho=gamma/2`.

For a pure z boost the projected operator `P_j T^+(g_beta) P_j` contains this diagonal entry, hence

`||P_j T^+(g_beta) P_j|| >= |t_+(beta)|`.

Therefore, for every fixed finite `gamma>0`,

`0 < beta < asinh(sqrt(2/(1+gamma^2)))`

implies

`||P_j T^+(g_beta) P_j|| > 1`.

Moreover,

`|t_+(beta)| ~ 2/[(1+gamma^2) beta^2]` as `beta -> 0+`,

so the projected Toller branch is unbounded on the frozen path. There is no finite uniform projected-operator bound on `beta>0`, in particular no Han-type contraction `||P_j T^+ P_j||<=1`.

## Interpretation
This is stronger than Iter081B's abstract additive countermodel: it is an explicit counterexample using the **actual gamma-simple Toller formula**. It identifies the exact place where Han's unitarity-based proof cannot survive a direct branch replacement. The `beta^-2` singularity is also consistent with the already-authoritative minimal-spin local behavior underlying the Iter077I collision obstruction, but that consistency is not needed for the proof above.

## Scope / anti-overclaim
The result proves only an actual projected-operator contraction counterexample for the prospectively frozen `j=k=m=1/2`, `rho=gamma/2`, `T^+`, pure-boost path. It does not yet prove:
- that every full causal branch face trace violates `|tau|<=d_k^2` after summing magnetic indices;
- that all branch assignments or spins behave identically;
- that no newly renormalized causal face functional can exist;
- that the full causal stack diverges;
- that the Iter077Q `W` ambiguity is selected or eliminated;
- regulator independence, G3, E7/E8, F9/G8/K5 promotion, GR recovery or new physics.

## Recommended independent Researcher successor
Automation A should prospectively reproduce this exact path as `ITER081C_SM_ACTUAL_TOLLER_BRANCH_HAN_PROJECTED_CONTRACTION_GATE`, checking Eq. (46), the hypergeometric identity, gamma recurrence and operator-norm inference independently. If confirmed, the direct Han projected-contraction route is scientifically closed on an actual Toller branch, and any causal Han-style face-stack construction must introduce a different bound/renormalization/functional or genuinely new source authority rather than reuse Han's unitary contraction argument.