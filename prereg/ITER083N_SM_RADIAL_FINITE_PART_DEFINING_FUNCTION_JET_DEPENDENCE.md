# Iter083N-SM preregistration — radial finite-part dependence on higher defining-function jets

Date: 2026-09-15
Status: PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION/PRODUCTION

## Scientific question
Iter083M fixes a unique invariant **tangent quadratic** radial geometry on every K3/K4/K5 normal fiber. Is that sufficient to make a one-parameter analytic/Hadamard finite part unique, or can two conformally related Morse-Bott defining functions with the same tangent quadratic form still differ through higher normal jets and hence shift supported counterterms?

## Candidate analytic regularization
Let rho be a smooth nonnegative Morse-Bott defining function for one collision stratum N, with the Iter083M quadratic Hessian. Consider a meromorphic distribution family

`U_rho(z)=rho^z u = A_-1/z + A_0 + O(z)`

near z=0, with at most a simple pole. Define the finite part as `FP_rho u=A_0`.

For a conformal change

`rho'=exp(phi) rho`,

we have identically

`U_rho'(z)=exp(z phi) U_rho(z)`.

## External mathematical source lock
Felder–Kazhdan, “Regularization of divergent integrals”, proves in the Morse-Bott/Hadamard setting that finite-part dependence under conformal change of regularizer is expressed by a local residue term. The external theorem is motivation/crosscheck; applicability of its full differential-form hypotheses to the Toller object is not assumed.

## Prospective predicates
P0 AUTHORITY_LOCK: consume Iter083M radial geometry and Iter083B/Iter082D normal-order ceilings `omega=(0,3,8)` / `F_8` without promoting a finite part.

P1 LAURENT_TRANSFORMATION: exact formal Laurent multiplication must give

`Res_rho'=A_-1`,

`FP_rho' u - FP_rho u = phi A_-1`.

The residue is unchanged; the finite part shifts by multiplication of the supported residue distribution by phi.

P2 SUPPORTED_JET_ANNIHILATOR: for distributions supported on N of normal order at most omega, every smooth phi in `I_N^(omega+1)` annihilates them. Conversely, for every `q<=omega`, a nonzero q-th normal jet of phi can act nontrivially on some order-q supported derivative distribution. Use exact identities such as

`n^q delta^(k) = (-1)^q k!/(k-q)! delta^(k-q)` for q<=k,

and zero for q>k.

P3 UNIVERSAL_INDEPENDENCE_THRESHOLDS: the sufficient-and-sharp universal conformal-equivalence thresholds for all possible residues of order <=omega are

- K3 omega=0: `phi in I_N^1`;
- K4 omega=3: `phi in I_N^4`;
- K5 omega=8: `phi in I_N^9`.

P4 TANGENT_METRIC_SCOPE: if rho and rho' have the same Morse-Bott quadratic Hessian and are conformally related, then `phi|_N=0`, so Iter083M tangent normalization supplies only the first threshold `phi in I_N^1`. This is universally sufficient for K3 but not, by itself, for the full allowed K4/K5 residue spaces.

P5 CONSTANT_RESCALING_CONTROL: if `rho'=c rho`, c>0 constant, then

`FP_(c rho)u-FP_rho u=(log c) A_-1`.

Thus any unfixed overall radial scale matters whenever the residue is nonzero. If source rapidity normalization fixes c, this particular freedom is absent but higher-jet freedom remains.

P6 ACTUAL_RESIDUE_FIREWALL: do not infer that the physical Toller residue activates every allowed derivative channel. The theorem classifies potential defining-function dependence for the whole supported residue space. Actual independence can be stronger if `phi A_-1=0` for the source residue.

P7 FELDER_KAZHDAN_SCOPE: source lock must record the external finite-part/residue dependence theorem and also retain its hypothesis gap. In particular, odd-codimension residue-vanishing results from that differential-form class must NOT be promoted automatically to the K4 Toller object without proving membership in the required singularity class.

## Negative controls
- reject the false claim that a unique tangent metric automatically fixes the finite part for omega>0;
- reject treating all supported residues as order zero;
- reject claiming actual K5 scheme dependence without the source residue;
- reject importing the Felder–Kazhdan odd-codimension simplification to K4 without an applicability proof;
- retain the possibility that an exact nonlinear source radial function fixes all relevant jets;
- retain the possibility that the actual residue annihilates the defining-function change;
- retain global forest/patching blockers.

## Expected classification if PASS
`ITER083N_SM_RADIAL_FINITE_PART_CHANGE_IS_RESIDUE_TIMES_DEFINING_FUNCTION_JET_AND_TANGENT_METRIC_ALONE_IS_INSUFFICIENT_FOR_K4_K5_SCOPED`

Verdict: `PASS_EXACT_SCOPED`.

## Research consequence if PASS
The next positive selector target becomes sharply defined: either construct an exact nonlinear source-derived Morse-Bott radial function (fixing the required higher jets), or compute the actual K3/K4/K5 residue distributions and prove that their contraction with the unfixed higher-jet changes vanishes. Merely fixing the tangent invariant metric is not enough in the general supported-residue class.

## Interpretation ceiling
No actual nonzero physical finite-part dependence; no full applicability of Felder–Kazhdan to Toller amplitudes; no unique extension; no global renormalization; no regulator independence/dependence theorem for the physical amplitude; no generic-spin theorem; no G3/F9/G8/K5 promotion; no NEW_PHYSICS_FOUND; no complete-QG claim.