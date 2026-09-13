# Primary-source snapshot — exact Toller restrictor and Lorentzian saddle-orientation bridge

**Acquired:** 2026-09-13  
**Purpose:** freeze the amplitude-level source facts needed after terminal Iter076M, before any Iter076N implementation.

## Primary authorities

1. Eugenio Bianchi, Chaosong Chen, Mauricio Gamonal, **“Causal spinfoam vertex for 4d Lorentzian quantum gravity”**, arXiv:`2601.23162`, *Phys. Rev. D* **113**, 126020 (2026).
   - https://arxiv.org/html/2601.23162
   - https://doi.org/10.1103/fwql-t4yr
2. John W. Barrett, Richard J. Dowdall, Winston J. Fairbairn, Frank Hellmann, Roberto Pereira, **“Lorentzian spin foam amplitudes: graphical calculus and asymptotics”**, arXiv:`0907.2440`, *Class. Quant. Grav.* **27**, 165009 (2010).
   - https://arxiv.org/abs/0907.2440

The exact causal-vertex facts and the semiclassical critical-point facts are kept separate below.

## Exact finite-spin Toller restrictor

The 2026 source gives the coherent-spinor representation of a Toller matrix in Eq. (17). For wedge sign `kappa_ab=sigma_a sigma_b`, the exact integrand contains

`theta(kappa_ab * B(z,g)) + kappa_ab * delta^(rho,j)(B(z,g))`,

multiplying the usual oscillatory/damping factors. Appendix C Eq. (32) defines the real function

`B(z,g) = log( <g^dagger z|g^dagger z> / <z|z> )`.

Appendix D Eq. (36) derives the same restrictor directly from the Feynman `i epsilon` representation:

`Theta_(kappa,rho,j)[x] = theta(kappa*x) + kappa*delta^(rho,j)(x)`.

Thus the wedge causal sign occurs in an **exact amplitude-level restriction of the integration domain**. This is stronger than mere constructibility of an orientation sign from the integration variables.

The distributional term is supported only at `B=0`; no claim below replaces it by a fitted or regularized bulk contribution.

## Non-degenerate Lorentzian critical locus

For a boundary state peaked on a non-degenerate Lorentzian Regge 4-simplex, the 2026 source assumes non-vanishing 4-volume and hence `beta_ab != 0` on every wedge used in the saddle analysis.

The EPRL stationary equations have two critical points. At them Eq. (14) gives

`B_ab^(+/-) = +/- s_a s_b beta_ab`, with `beta_ab > 0`,

where the `+/-` sign is global, the same for every wedge.

For the causal vertex, the product of exact Heaviside factors restricts the integration region. The source states that the `-` critical point never lies in that region. The `+` critical point lies in the region exactly when

`sigma_a sigma_b = s_a s_b`

for all wedges. Eq. (18) then yields the single oscillatory term `exp(+ i S_Regge / hbar)`; incompatible causal data are suppressed faster than every power in the large-spin parameter.

This establishes source-level **saddle selection by the exact Toller restrictor** on the non-degenerate Lorentzian Regge critical locus.

## Parity relation of the two Lorentzian EPRL critical points

The Lorentzian EPRL asymptotics literature establishes that, for geometric Lorentzian 4-simplex boundary data, the two non-degenerate critical solutions correspond to parity-related 4-simplex reconstructions and carry opposite Regge phases. The original authority is Barrett et al., arXiv:`0907.2440`; the result is also restated in the Fairbairn–Hellmann–Pereira asymptotic analysis.

A spacetime parity transformation has determinant `-1`. Therefore any genuine orientation pseudoscalar, including the Iter076M candidate

`Omega_sigma(g) = sgn det([1; sigma_a F_a])`, `F_a = ghat_a T`,

changes sign between parity-related non-degenerate configurations, while global `sigma -> -sigma` leaves it invariant because four vector rows change sign.

This parity statement is the bridge from “one of two EPRL saddles” to “one of two opposite orientation-pseudoscalar sectors”.

## Scope firewall

The exact object is the Toller restrictor. The identification of the selected saddle with one sign of `Omega_sigma` uses the Lorentzian non-degenerate critical-point/parity reconstruction and is therefore a **saddle-locus statement**.

This snapshot does not establish that the finite-spin off-saddle integrand is globally a function of `Omega_sigma`, does not define `Omega_sigma` at degeneracy, and does not promote an exact physical signed source-to-K4 pushforward P3.

No nominal `epsilon^-1` coefficient, finiteness/divergence theorem, F9/G3/G8/K5 promotion, physical-sector theorem away from the frozen locus, complete-QG claim, or new-physics claim follows.
