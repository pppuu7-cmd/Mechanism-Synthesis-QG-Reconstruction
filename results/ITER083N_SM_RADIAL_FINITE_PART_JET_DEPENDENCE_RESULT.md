# Iter083N-SM — radial finite-part change is residue times defining-function jet

Date: 2026-09-15
Status: **PASS_EXACT_SCOPED**

## Provenance
- preregistration `c29ba0ddbaa4d6e1581db558b792565a7916a0cd`;
- external mathematical source lock `9883aed83057ff6850dab605201bccddb7c92254`;
- theorem derivation `f0a1d59956e76f135b9dac6a31d6cdf8bcbca578`;
- initial workflow/head `2007fa2868da3ef57390002df3c453cdf8bab129`;
- first run `34917581221` failed before scientific predicates because of a Python string-literal SyntaxError in a provenance check;
- syntax-only repair `095e1c98af085ad54fadb1cde2e38b2d2d6d18cd`;
- second run `34917632292` computed all scientific predicates P0-P6 successfully but failed only the P7 literal wording `not established` versus `has not been established`;
- wording-only repair/head `d35c1c3eb92456c053b27fa46a8783f28c76879b`;
- authoritative run `34917739247`, job `104218935908`, terminal success;
- artifact `10376728965`, `iter083n-radial-finite-part-jet-dependence`;
- artifact ZIP digest `sha256:da3a81a693797975ade1823d5e7554d9445358852029c926bc209281b10815d3`;
- production JSON SHA256 `9cc509a84714ff18e6687eda9b5f8e94c3ba7df1786f8cfb63866f9a8bd04553`.

No scientific predicate, threshold or theorem statement changed after preregistration.

## Classification
`ITER083N_SM_RADIAL_FINITE_PART_CHANGE_IS_RESIDUE_TIMES_DEFINING_FUNCTION_JET_AND_TANGENT_METRIC_ALONE_IS_INSUFFICIENT_FOR_K4_K5_SCOPED`

Verdict: **`PASS_EXACT_SCOPED`**.

## Exact Laurent transformation
Let

`U_rho(z)=rho^z u=A_-1/z+A_0+O(z)`

and let

`rho'=exp(phi) rho`.

Then exactly

`U_rho'(z)=exp(z phi) U_rho(z)`.

Therefore

`Res_rho'=A_-1`,

while

`FP_rho' u-FP_rho u=phi A_-1`.

Production verifies the formal coefficient bookkeeping exactly: the residue is unchanged and the finite part shifts by `phi*A_-1`.

This is a distribution-valued statement; the residue is not scalarized.

## Exact supported-jet annihilator
In one normal coordinate,

`n delta^(k)=-k delta^(k-1)`.

Iterating,

`n^q delta^(k)=(-1)^q k!/(k-q)! delta^(k-q)` for `q<=k`,

and zero for `q>k`.

Production checked all 90 pairs

`0<=k<=8`, `0<=q<=9`

with zero failures.

Hence a distribution supported on N of normal order at most omega is annihilated universally by

`I_N^(omega+1)`.

The bound is sharp in the universal supported-jet class: for every `q<=omega`, the q-th normal Taylor term can act nontrivially on an order-q derivative delta distribution.

Production verifies sharpness for omega `0,3,8`.

## Exact K3/K4/K5 thresholds
The authoritative forest normal-order ceilings are

`omega_K3=0`,

`omega_K4=3`,

`omega_K5=8`.

Therefore a conformal defining-function change `rho'=exp(phi)rho` is guaranteed to leave the finite part unchanged for **every** possible supported residue in the allowed class only if

- K3: `phi in I_N^1`;
- K4: `phi in I_N^4`;
- K5: `phi in I_N^9`.

These powers `(1,4,9)` are exact universal thresholds, not fitted values.

## What the Iter083M tangent metric fixes
For conformally related Morse–Bott defining functions with the same normalized quadratic Hessian,

`Hess_N(rho')=exp(phi|_N) Hess_N(rho)`.

Equality of normalized Hessians implies only

`phi|_N=0`,

that is, `phi in I_N`.

This is universally sufficient for K3, whose supported residue order is at most zero.

It is **not universally sufficient** for the full allowed K4 or K5 residue spaces, because normal derivatives through order 3 or 8 can detect higher normal jets of phi.

Thus the unique tangent radial geometry from Iter083M does not by itself define a universal K4/K5 finite part.

## Constant rescaling
For

`rho'=c rho`, `c>0`,

`phi=log c`, so

`FP_(c rho)u-FP_rho u=(log c) A_-1`.

An unfixed overall radial scale therefore matters whenever the actual residue is nonzero.

If a source-native exact rapidity normalization fixes the scale, this particular freedom can disappear, but the general higher-jet issue remains unless the whole nonlinear defining function is fixed or the residue annihilates the remaining change.

## Relation to Felder–Kazhdan
Felder–Kazhdan independently obtain the same structural phenomenon for Hadamard finite parts defined with Morse–Bott regularizers: conformal change of regularizer changes the finite part through a local residue term.

Their additional odd-codimension residue-vanishing theorem belongs to their differential-form singularity class. Iter083N explicitly does **not** apply it to K4 merely because `codim K4=9`; membership of the Toller singularity in that class has not been proved.

## Actual-residue firewall
This theorem classifies potential dependence across the full admissible supported-residue space. It does **not** prove that the physical Toller residue activates every order through omega.

A particular source residue may:

- have lower normal order;
- lie in a smaller symmetry sector;
- annihilate the unfixed higher defining-function jets;
- or vanish in some channels.

In such a case the actual finite part can be more independent than the universal bound suggests.

## Research consequence
The next exact positive targets are now sharply separated:

1. construct an exact nonlinear source-native defining function whose relevant jets are fixed, rather than only its Hessian;
2. compute the actual K3/K4/K5 source residues and their normal-order/symmetry support.

The exact Cartan rapidity squared is a promising first route because it is smooth at the compact locus and gives a concrete nonlinear group-theoretic defining-function candidate.

## Interpretation ceiling
No actual nonzero physical finite-part dependence is proved; no statement that the Toller residue fills the 377-dimensional ambiguity space; no automatic Felder–Kazhdan applicability; no global K5 renormalization; no regulator dependence/independence theorem for the physical amplitude; no unique extension; no generic-spin theorem; no G3/F9/G8/K5 promotion; no `NEW_PHYSICS_FOUND`; no complete-QG claim.