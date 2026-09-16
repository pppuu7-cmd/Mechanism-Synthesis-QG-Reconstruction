# K5 34-orbit physical numerator/action-flux audit

Date: 2026-09-16
Status: PROSPECTIVELY FROZEN BEFORE PHYSICAL CORNER VALUATIONS

## AUTHORITY / DEPENDENCIES

Authorized by controlling full-symbolic Critic review of corrected projective tangent-flux geometry, latest controlling verdict `CONFIRMED_SCOPED` (Critic repair run 35149251634; artifact 10468826978).

Physical numerator authority: `results/K5_INVARIANT_DUAL_DEG27_CANONICAL_DAG_RESULT.md`, commit `666aa6e61f62bbfff456f6be7995ce3a65f2b633`, full all-32 / 100000-source-term invariant-dual rank-two object, homogeneous degree 27.

Annihilator/action authority: unique non-radial degree-four S5-equivariant Kirchhoff annihilator `v(Psi_K5)=0`; exact action

`B_v[N]=s1 v(N)+{s1[div v +(1/2)sum_i q_i]-3S}N`,

`v_i=alpha_i q_i`, `S=sum_i v_i`, and physical projective action numerator `P_v[N]=B_v[N]/s1^4`. Since `s1` has nonzero order on every proper face chart used below, `ord_t P_v[N]=ord_t B_v[N]`.

Projective integrand authority:

`Omega_9 * prod_e alpha_e^(1/2) * N_c(alpha) / Psi_K5(alpha)^(21/2)`.

## OBJECT / 34 ORBITS

Enumerate all 1024 subsets of the 10 K5 edges and quotient exactly by the induced S5 action from all 120 vertex permutations. Canonical representative is the lexicographically least 10-bit mask in each orbit. This construction must yield exactly 34 orbits whose sizes sum to 1024. The empty and full edge sets are retained only as nonphysical controls. The remaining 32 proper orbits are the physical projective corner-orbit audit set.

For an orbit representative `Z`, `k=|Z|`, use the blow-up ray

`alpha_e(t)=t*w_e` for `e in Z`, `alpha_e(t)=w_e` otherwise,

with frozen asymmetric weights

`w=(2,3,5,7,11,13,17,19,23,29)`

in canonical edge order `(01,02,03,04,12,13,14,23,24,34)`. A second independent witness uses

`w'=(31,37,41,43,47,53,59,61,67,71)`.

These rays are witnesses only; generic face orders may be certified only when an exact structural lower bound is attained by a nonzero leading coefficient.

## FROZEN ORDERS, KEPT SEPARATE

For every proper orbit and each channel `c=1,2`, compute and store separately:

1. `g(Z)=k-1`, the already-confirmed projective geometric Jacobian/form order, reproduced mechanically as a control rather than inserted as a physical numerator result.
2. `rPsi(Z)=ord_t Psi_K5(alpha(t))`, independently from the 125-tree Kirchhoff polynomial (equivalently the minimum number of Z-edges in a spanning tree), with exact positive leading coefficient control.
3. `rN_c(Z)=ord_t N_c(alpha(t))` as a **generic face order certificate**, not merely a sample-ray order.
4. `rB_c(Z)=ord_t B_v[N_c](alpha(t))`; `rP_c=rB_c` on these proper charts because `ord_t s1=0`.
5. projective measure/denominator contribution
   `m(Z)=k/2-(21/2)*rPsi(Z)`.
6. interior integrability exponent
   `I_c(Z)=g(Z)+m(Z)+rN_c(Z)`.
   Local radial integrability criterion is `I_c>-1`; `I_c=-1` is logarithmic; `I_c<-1` divergent.
7. corrected tangent-flux exponent using the exact projective normal component `u_Z=sum_{e in Z} u_e`:
   `F_c(Z)=g(Z)+ord_t u_Z(Z)+m(Z)+rN_c(Z)`.
   This is the local boundary-flux scaling for the original physical integrand. It is not a global Stokes conclusion.
8. action-integrand exponent
   `A_c(Z)=g(Z)+m(Z)+rP_c(Z)`.

No one of these quantities may be substituted for another.

## GENERIC FACE CERTIFICATE RULE

The implementation must use the canonical degree-27 DAG / exact action algebra to propagate a structural t-adic lower bound for `N_c` and `B_c`. It must independently evaluate exact t-adic coefficients on both frozen asymmetric angular witnesses over two fixed large primes (`1000003`, `1000033`).

A generic order is certified only if:

- both modular witnesses give the same lowest nonzero order;
- that order equals the structural lower bound;
- denominators are invertible modulo both primes;
- S5-related representative/permuted-weight controls reproduce the order.

If these conditions fail for an orbit/channel, classify that component `BLOCKED_CANCELLATION_RESOLUTION` and do not infer an integrability verdict for that component. Do not tune weights or primes after output.

## CONTROLS

- exact 34-orbit enumeration, orbit sizes sum 1024;
- empty/full masks are nonphysical controls only;
- 125 spanning trees and unit positive Kirchhoff coefficients;
- S5 covariance on at least one nontrivial permutation for every proper orbit;
- both invariant-dual physical channels retained;
- all32/source-term authority retained;
- wrong `Psi` exponent, wrong half-density exponent, raw-ambient `v_Z` replacing projective `u_Z`, and vector-vs-dual projection are explicit rejected controls;
- `s1` order zero on every proper face witness;
- no physical conclusion from a representative scalar boundary state;
- no global Stokes/integrated-period conclusion.

## PASS / FAIL / BLOCKED

`K5_34_ORBIT_PHYSICAL_NUMERATOR_ACTION_FLUX_AUDIT_EXACT_SCOPED` if all 32 proper orbits and both channels receive certified generic `rN`, `rB/rP`, `u_Z`, and all derived exponents with every control passing.

`K5_34_ORBIT_PHYSICAL_NUMERATOR_ACTION_FLUX_PARTIAL_BLOCKED_SCOPED` if geometry/Psi/orbit data are exact but at least one physical numerator/action generic order cannot be certified under the frozen certificate rule. The exact certified subset remains usable only in its stated scope.

`SCIENTIFIC_FAIL_EXACT_SCOPED` only for an exact contradiction of the already-authorized local formula/object, not merely a divergent corner.

`INVALID_IMPLEMENTATION` for missing orbit coverage, wrong object, hard-coded physical valuations, missing channel, missing controls, or execution/provenance failure.

A divergent physical corner is a scientific data outcome of this audit, not automatically a failure of the parent theory; interpretation must state the precise local integrability consequence only.

## INTERPRETATION CEILING

Even full PASS does not establish global projective Stokes/IBP, an integrated K5 period relation, full 217-dimensional order-eight tensor behavior, reduction of `dim_C F_8=377`, a physical finite-part selector, regulator independence, F9/G3/G8, `NEW_PHYSICS_FOUND`, or complete quantum gravity.
