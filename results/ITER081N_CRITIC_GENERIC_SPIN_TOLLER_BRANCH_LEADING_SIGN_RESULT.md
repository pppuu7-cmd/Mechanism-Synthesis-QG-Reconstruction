# Iter081N Critic exact result — generic-spin gamma-simple Toller branches have equal leading pole magnitude and opposite sign

Date: 2026-09-14
Status: **EXACT SOURCE-FORMULA THEOREM SCOPED TO ONE-WEDGE PURE-BOOST GAMMA-SIMPLE MINIMAL BLOCK**

## Prospective lock
Object frozen before derivation in `results/ITER081N_PRE_GATE_GENERIC_SPIN_TOLLER_BRANCH_LEADING_SIGN.md`, commit `ccf9813204edde8e69a8c15b6770af14d3e36f26`.

## Frozen source formula
Use Bianchi--Chen--Gamonal `arXiv:2604.24945v1`, Eq. (46), gamma-simple minimal block `j=l=k`, pure boost `g_beta=exp(-i beta K_z)`, `beta>0`:

`t_(jjm)^(±,rho,j)(beta) = exp[-(j ∓ i rho ± m +1) beta] * Gamma(2j+2) Gamma(± i rho ∓ m) / [Gamma(j ∓ m +1) Gamma(j+1 ± i rho)] * 2F1(j ± m +1, j+1 ∓ i rho; 1 ± m ∓ i rho; exp(-2 beta)).`

Domain:
- `j=1/2,1,3/2,...`;
- `m=-j,-j+1,...,j`;
- fixed finite real `rho != 0`;
- one-sided ordinary-function limit `beta->0+`.

Set `z=exp(-2 beta)` and `N=2j+1`.

## Plus branch
For `T^+`,

`a_+ = j+m+1`,
`b_+ = j+1-i rho`,
`c_+ = 1+m-i rho`.

Therefore exactly

`a_+ + b_+ - c_+ = 2j+1 = N > 0`.

The standard hypergeometric continuation at `z->1-` gives the leading term

`2F1(a_+,b_+;c_+;z)`
`~ [Gamma(c_+) Gamma(N)/(Gamma(a_+) Gamma(b_+))] (1-z)^(-N)`.

Multiplying by the frozen Eq. (46) prefactor and using that the exponential tends to 1 gives the coefficient of `(1-z)^(-N)`:

`A^+_(jm)(rho) = Gamma(2j+2) Gamma(2j+1) Gamma(i rho-m) Gamma(1+m-i rho)`
` / [Gamma(j-m+1) Gamma(j+m+1) Gamma(j+1+i rho) Gamma(j+1-i rho)]`.

By Euler reflection, with `u=i rho-m`,

`Gamma(i rho-m) Gamma(1+m-i rho) = pi/sin[pi(i rho-m)]`.

Since `1-exp(-2 beta) = 2 beta + O(beta^2)`, the beta-leading coefficient is

`C^+_(jm)(rho)`
`= 2^(-(2j+1)) * Gamma(2j+2) Gamma(2j+1) pi`
` / [Gamma(j-m+1) Gamma(j+m+1) Gamma(j+1+i rho) Gamma(j+1-i rho) sin(pi(i rho-m))]`.

Thus

`t^+_(jjm)(beta) = C^+_(jm)(rho) beta^(-(2j+1)) + o(beta^(-(2j+1))).`

## Minus branch
For `T^-`,

`a_- = j-m+1`,
`b_- = j+1+i rho`,
`c_- = 1-m+i rho`,

again giving

`a_- + b_- - c_- = N=2j+1`.

The identical continuation formula yields the same common denominator and the numerator pair

`Gamma(m-i rho) Gamma(1-m+i rho)`.

Euler reflection gives

`Gamma(m-i rho) Gamma(1-m+i rho) = pi/sin[pi(m-i rho)]`
`= - pi/sin[pi(i rho-m)]`.

Therefore exactly

`C^-_(jm)(rho) = - C^+_(jm)(rho)`

and

`t^-_(jjm)(beta) = -C^+_(jm)(rho) beta^(-(2j+1)) + o(beta^(-(2j+1))).`

## Nonvanishing
All factorial-type factors `Gamma(j±m+1)` are finite and nonzero because `j±m` are nonnegative integers. `Gamma(j+1±i rho)` is finite and nonzero.

For real `rho != 0`, `sin[pi(i rho-m)]` is nonzero:
- for integer `m`, it is proportional to `i sinh(pi rho)`;
- for half-integer `m`, it is proportional to `cosh(pi rho)`.

Hence

`C^+_(jm)(rho) != 0`

for every allowed `j,m` and every finite real `rho != 0`.

## Exact theorem
For the frozen gamma-simple minimal pure-boost block,

`p_j = 2j+1`,

and for every allowed magnetic index

`t^-_(jjm)(beta) / t^+_(jjm)(beta) -> -1`

as `beta->0+`.

Classification:

`ITER081N_SM_GENERIC_SPIN_GAMMA_SIMPLE_MINIMAL_TOLLER_BRANCHES_HAVE_NONZERO_BETA_MINUS_2J_PLUS1_LEADING_POLES_WITH_EXACT_OPPOSITE_SIGN_THEOREM_SCOPED`.

## Symbolic regression controls
The closed coefficient reproduces the preregistered low-spin controls exactly.

For `j=1/2`:
- `m=-1/2`: `C^+=+2/(4 rho^2+1)=+1/[2(rho^2+1/4)]`;
- `m=+1/2`: `C^+=-2/(4 rho^2+1)=-1/[2(rho^2+1/4)]`.

The `m=+1/2` value is exactly the Iter081E coefficient from
`|t_+|=1/[2(rho^2+1/4)sinh^2 beta]`, and the two magnetic signs reproduce the Iter081E two-wedge control.

For `j=1`:
- `m=-1`: `C^+=3 i/[4 rho(rho^2+1)]`;
- `m=0`: `C^+=-3 i/[2 rho(rho^2+1)]`;
- `m=+1`: `C^+=3 i/[4 rho(rho^2+1)]`.

For `j=3/2`, writing `P=16 rho^4+40 rho^2+9`:
- `m=-3/2,-1/2,+1/2,+3/2` gives respectively `C^+=(-24,+72,-72,+24)/P`.

For `j=2`, writing `R=rho(rho^4+5 rho^2+4)`:
- `m=-2,-1,0,+1,+2` gives respectively `C^+=(-15 i/4,+15 i,-45 i/2,+15 i,-15 i/4)/R`.

In every listed control the independently reduced minus coefficient is exactly `-C^+`.

## Conditional K5 implication — deliberately not promoted
The theorem strongly suggests a generic-spin extension of the Iter077I branch-sign transport: if, on a source-faithful K5 common-collision path, all required wedge blocks are in this minimal gamma-simple sector and an all-plus fully contracted leading boundary coefficient is independently proved nonzero, then replacing a wedge branch `+` by `-` changes its **leading reduced boost block** by a sign.

However this note does **not** promote that observation to a generic-spin K5 theorem. A full K5 statement additionally requires control of the SU(2) KAK rotations, representation-index contractions, possibly unequal edge spins/powers, the common radial scaling, and the nonvanishing of the complete boundary contraction. None of those generic-spin hypotheses is established here.

## Claim ceiling
This result does NOT establish:
- generic-spin K5 non-L1 behavior;
- nonzero generic-spin full boundary contractions;
- a generic-spin causal orientation-sum obstruction;
- all collision strata;
- a causal-vertex divergence/nonexistence theorem;
- a joint-K5 extension selector;
- regulator independence;
- causal multivertex closure, G3, F9/G8/K5, `NEW_PHYSICS_FOUND`, or complete QG.

It is an exact one-wedge source-formula theorem: the two Toller branches have the same nonzero leading pole of order `2j+1` and opposite coefficient in every finite-spin gamma-simple minimal diagonal boost block with real `rho!=0`.
