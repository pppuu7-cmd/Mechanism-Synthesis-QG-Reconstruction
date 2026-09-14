# Iter081C pre-gate object — actual gamma-simple Toller branch vs Han contraction bound

Status: **Critic prospective object freeze only; no Researcher verdict.**
Date: 2026-09-14

## Motivation fixed before simplification
Iter081B is independently `CONFIRMED_SCOPED`: Han's unitary-representation face-stack bound cannot be inherited merely from `D=T^(+)+T^(-)`. The highest-value next question is whether the **actual** gamma-simple Toller branch itself satisfies or violates a Han-type projected-operator contraction bound.

## Frozen primary formula
Use Bianchi--Chen--Gamonal arXiv:2604.24945v1 Eq. (46), for `gamma`-simple representations `k=j`, `rho=gamma j`, `l=j`, pure boost `g_beta=exp(-i beta K_z)`, `beta>0`:

`t_{jjm}^{(±,rho,j)}(beta) = exp[-(j ∓ i rho ± m +1) beta] * Gamma(2j+2) Gamma(± i rho ∓ m) / ( Gamma(j ∓ m +1) Gamma(j+1 ± i rho) ) * 2F1(j ± m +1, j+1 ∓ i rho; 1 ± m ∓ i rho; exp(-2 beta)).`

For a pure z boost, `P_j T^(±)(g_beta) P_j` is diagonal in the magnetic index and contains this reduced matrix element.

## Frozen test point/path
- minimal nonzero EPRL spin: `j=k=1/2`;
- Barbero--Immirzi parameter: arbitrary fixed real `gamma>0`;
- `rho=gamma/2` (keep symbolic; no posthoc fit);
- magnetic index: `m=+1/2`;
- branch: `+`;
- group path: `g_beta=exp(-i beta K_z)`, `beta>0`, with one-sided limit `beta -> 0+`;
- observable: the actual diagonal matrix element `t_{1/2,1/2,1/2}^{(+,rho,1/2)}(beta)` and hence the operator norm lower bound `||P_j T^+(g_beta) P_j|| >= |t|`.

## Frozen comparison criterion
Han's standard proof uses unitarity of `D` and orthogonal projection to obtain a contraction at each projected wedge factor and ultimately `|tau_k^(h)| <= d_k^2`. The successor test asks whether the actual selected Toller branch has any uniform Han-type projected-operator contraction `||P_j T^+(g) P_j|| <= 1` on this path.

Classify the path result only as one of:
1. `ACTUAL_TOLLER_PROJECTED_CONTRACTION_SURVIVES_ON_FROZEN_PATH` if the exact formula proves the bound on all `beta>0` and has a finite `beta->0+` limit compatible with it;
2. `ACTUAL_TOLLER_PROJECTED_CONTRACTION_COUNTEREXAMPLE_ON_FROZEN_PATH` if the exact formula proves `|t|>1` for any admissible `beta>0`, or diverges as `beta->0+`;
3. `ANALYTIC_CONTROL_INSUFFICIENT` if the exact simplification/asymptotic cannot be established rigorously.

## Required controls
- Use the actual BCG Eq. (46); do not use Iter081B's abstract `D=I, T+=2I, T-=-I` witness.
- Preserve `beta>0`; the limit is one-sided and must not be silently evaluated at the singular locus.
- Distinguish failure of a projected-operator contraction from failure of every possible causal face functional. A branch-operator counterexample blocks direct reuse of Han's unitarity proof but does not by itself prove that every trace/product construction violates `d_k^2` after cancellations or new renormalization.
- Do not infer a full K5 amplitude, W-selector, multivertex theorem, regulator independence or causal-stack no-go.
- If an exact hypergeometric identity is used, state it before applying it and verify parameter matching exactly.

## Claim ceiling
At most this gate may establish an **actual Toller branch counterexample to Han's projected-operator contraction on the frozen gamma-simple path**. Any statement about a full face trace, all spins, all branches, arbitrary group elements, causal stack impossibility, or Iter077Q selection requires a later prospective gate.