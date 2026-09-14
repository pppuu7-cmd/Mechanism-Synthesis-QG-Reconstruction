# Iter081N Critic pre-gate — generic-spin gamma-simple Toller branch leading-sign relation

Date: 2026-09-14
Status: **PROSPECTIVE CRITIC SOURCE-FORMULA OBJECT FREEZE — NO RESULT YET**

## Motivation
Iter081E proves the selected-branch small-boost singularity explicitly at `j=1/2`. Iter077I/K5 causal-sum corollaries use the special `j=1/2` leading relation `T^- ~ -T^+`. Before making any generic-spin statement, test whether this opposite-leading-sign relation follows directly from the general gamma-simple BCG hypergeometric formula for arbitrary finite spin.

## Frozen source formula
Use Bianchi--Chen--Gamonal `arXiv:2604.24945v1`, Eq. (46), in the gamma-simple minimal block `j=l=k`, pure boost `g_beta=exp(-i beta K_z)`, `beta>0`:

`t_(jjm)^(±,rho,j)(beta) = exp[-(j ∓ i rho ± m +1) beta] * Gamma(2j+2) Gamma(± i rho ∓ m) / [Gamma(j ∓ m +1) Gamma(j+1 ± i rho)] * 2F1(j ± m +1, j+1 ∓ i rho; 1 ± m ∓ i rho; exp(-2 beta)).`

Freeze:
- `j in {1/2,1,3/2,...}`;
- `m=-j,-j+1,...,j`;
- finite real `rho != 0` (EPRL gamma-simple specialization may later set `rho=gamma j`);
- one-sided ordinary-function limit `beta->0+`.

## Exact question
For each allowed `(j,m,rho)`, determine the strongest leading asymptotic

`t^±_(jjm)(beta) = C^±_(jm)(rho) beta^(-p_j) + o(beta^(-p_j))`

and test:

1. whether `p_j=2j+1`;
2. whether `C^+_(jm)(rho)` is finite and nonzero;
3. whether `C^-_(jm)(rho)=-C^+_(jm)(rho)` exactly.

## Allowed identities
Use only standard exact hypergeometric continuation at `z->1-` with `a+b-c=2j+1>0`, Gamma recurrence/reflection identities, and `1-exp(-2 beta)~2 beta`. No numerical fit may establish the theorem.

## Controls
After the symbolic derivation, check at least `j=1/2,1,3/2,2` and multiple `m` values numerically or symbolically as regression controls. The existing Iter081E `j=1/2` formula is a required positive consistency check but is not to be imported as the generic proof.

## Claim ceiling
A positive result would establish only a **one-wedge generic-spin leading branch-sign lemma** in the gamma-simple minimal block and, conditionally, the sign transport of any already-nonzero K5 leading tensor. It would NOT establish:
- nonzero full boundary contraction at generic spin;
- generic-spin K5 non-L1 behavior;
- generic-spin scaling degree of the fully contracted vertex;
- all collision strata;
- distributional nonexistence/divergence;
- regulator independence;
- a unique extension selector;
- G3/F9/G8/K5 or complete QG.

Any K5 consequence must explicitly retain the condition that the corresponding all-plus leading boundary contraction is nonzero.
