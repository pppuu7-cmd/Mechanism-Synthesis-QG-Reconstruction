# Mixed compact/boost polar-KAK jet supplement

Date: 2026-09-13

## Source convention

The causal-vertex source Eq. (7) uses the Cartan decomposition

`g = U_1 exp(beta sigma_z/2) U_2`

and

`T(g)=D^j(U_1) t(beta) D^j(U_2)`.

Iter076V-W-X have already fixed the gamma-simple leading singular matrix `C_z`, the radial relative one-jet `i gamma J_z`, pure node-direction cancellations, and the nontrivial angular response of the leading normal-direction family.

This supplement derives one concrete mixed compact/boost group path in the defining `2x2` representation in order to fix the coefficient with which the normal-direction connection enters the first subleading Toller term.

## Frozen mixed path

Use Hermitian boost and anti-Hermitian compact generators

`B := sigma_z/2`,

`A := -i alpha sigma_y/2`,

with real nonzero mixing parameter `alpha`, and define

`g(t):=exp[t(A+B)]`, `t>0`.

Let `g=u p` be its polar decomposition, with `u` unitary and `p=(g^dagger g)^(1/2)` positive Hermitian.

## Derived exact second-order polar jet

Baker-Campbell-Hausdorff gives

`log(g^dagger g)=2 t B - t^2 [A,B] + O(t^3)`

and therefore

`log p = t B - (t^2/2)[A,B] + O(t^3)`.

For the frozen Pauli generators,

`[A,B] = alpha sigma_x/2`,

so

`log p = t sigma_z/2 - alpha t^2 sigma_x/4 + O(t^3)`.

The radial boost magnitude is

`beta(t)=t+O(t^3)`,

while its unit normal is

`n(t)=z - (alpha/2)t x + O(t^2)`.

Choose

`R(t)=exp(+i alpha t sigma_y/4)`.

Then

`R(t) B R(t)^(-1) = B - alpha t sigma_x/4 + O(t^2)`

and hence

`p = R(t) exp[t B] R(t)^(-1) + O(t^3)`

at the required jet order.

The unitary polar factor obeys

`log u = t A + O(t^3)`.

Therefore a compatible Cartan jet is

`U_1(t)=u(t)R(t)=exp(-i alpha t sigma_y/4)+O(t^2)`,

`U_2(t)=R(t)^(-1)=exp(-i alpha t sigma_y/4)+O(t^2)`.

Thus the original compact rotation angle `alpha t` is split equally: each Cartan compact factor carries angle `alpha t/2` at first order.

## Induced first subleading Toller matrix

For spin `j`, write the reduced gamma-simple branch in the boost-z frame as

`t_red(t)=t^(-n)[C + t D + o(t)]`, `n=2j+1`,

with the closed Iter076V relation

`D C^(-1)=C^(-1)D=i gamma J_z`.

Using

`D^j(U_1)=1-i(alpha t/2)J_y+O(t^2)`,

`D^j(U_2)=1-i(alpha t/2)J_y+O(t^2)`,

the full matrix along the frozen mixed path is

`T(g(t)) = t^(-n) [ C + t T_1 + o(t) ]`,

where

`T_1 = -i(alpha/2) J_y C + D - i(alpha/2) C J_y`.

Equivalently, after right factoring the leading matrix,

`T_1 C^(-1) = -i(alpha/2) J_y + i gamma J_z - i(alpha/2) C J_y C^(-1)`.

The first two displayed relative terms are ordinary common SU(2) generators at source node 5 and are annihilated by the invariant node-5 intertwiner when summed over the four incident wedges. The last term is the nontrivial leading-matrix angular response.

## Boundary tensor after node-5 closure

Let

`F_z := i_5 [tensor_e C_{j_e}]`

be the four outgoing leading tensor after node-5 contraction. For the four incident wedges, the common mixed path produces the surviving first-order term

`-(i alpha/2) F_z [sum_e J_y^(e)]`.

This is exactly the transverse angular-response channel tested in Iter076X, now with a source-group-path coefficient fixed to `alpha/2`.

The frozen exploratory prediction is therefore inherited from Iter076X:

- the two `(1/2,1/2,1/2,1/2)` exact intertwiner controls vanish;
- the other five frozen exact controls survive;
- the result is proportional to `alpha` and vanishes at `alpha=0`;
- overall causal-branch leading scales do not change the zero/nonzero classification.

## Scope firewall

This path is a local source-group control, not the physical source-to-K4 map. It proves that the nontrivial normal-bundle connection of Iter076X is not merely formal: a concrete mixed compact/boost source path feeds it at first subleading radial order.

It does not establish:

- a unique coordinate choice for all mixed paths;
- the full ten-wedge correlated collision coefficient;
- the physical nonlinear source-to-K4 curvature;
- the nominal `epsilon^-1` coefficient.

The next step after exact confirmation is to determine whether this mixed connection datum can be represented covariantly on the full source cut-space jet and how it transforms under the K4 Hodge/Sym2 bridge.