# K5 mask-511 structural divisibility / lower-coefficient gate

Status: PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION.

## Motivation
The terminal labeled mask-511 W1/W2 witness found exact ray orders r_N=19 and r_B=21 for both physical channels, but did not establish angular-polynomial identities. This gate asks the orthogonal structural question allowed by status/CURRENT.md: whether the lower t-coefficients vanish identically, rather than merely on the two frozen rays.

## Frozen scope
Only the labeled mask 511 corner, both physical channels N_1,N_2, and the already-authoritative projective K5 object / degree-27 numerator DAG / corrected non-radial degree-four Kirchhoff annihilator may be used. No boundary-S5 transport theorem is consumed or inferred. No promotion to other masks/orbits is allowed.

## Frozen test
Introduce the same mask-511 scaling parameter t used by the authoritative corner witness, but keep all non-scaled angular variables symbolic/independent. For each physical channel c=1,2:

1. Reconstruct N_c(t,w) exactly from the authoritative degree-27 numerator DAG.
2. Reconstruct B_v[N_c](t,w) exactly using the already-confirmed annihilator, with no fitted coefficients or post-hoc simplification conventions.
3. Determine exact coefficient polynomials [t^q]N_c for q=0,...,18 and [t^q]B_v[N_c] for q=0,...,20.
4. Certify identity-zero only by exact symbolic/DAG cancellation. Numerical sampling/interpolation may be used only as a negative/control diagnostic, never as an identity proof.
5. Also exhibit and hash the first nonzero coefficient if it is exactly established at q=19 for N_c and q=21 for B_v[N_c]. If the first nonzero order differs from those ray values, report that exact order instead; frozen criteria must not be changed.

## Required controls
- reproduce the authoritative W1/W2 evaluations from the symbolic coefficient representation;
- malformed control: perturb one retained DAG/source coefficient and require at least one formerly zero lower coefficient to become nonzero, or otherwise classify the control as non-discriminating/INVALID;
- channel labels and DAG hashes must match authoritative source files;
- exact arithmetic only for scientific classification.

## Frozen classifications
- `K5_MASK511_LOWER_COEFFICIENTS_STRUCTURAL_DIVISIBILITY_EXACT_SCOPED` iff, for both channels, all N coefficients q<19 and all B coefficients q<21 vanish identically and the q=19/q=21 coefficients are exactly nonzero angular polynomials.
- `K5_MASK511_RAY_CANCELLATION_NOT_ANGULAR_UNIFORM_EXACT_SCOPED` iff any prospectively targeted lower coefficient is exactly nonzero as an angular polynomial while the provenance/controls are valid.
- `K5_MASK511_STRUCTURAL_DIVISIBILITY_BLOCKED_SCOPED` if exact reconstruction cannot resolve the identities within the implementation/resource envelope without numerical inference.
- `K5_MASK511_STRUCTURAL_DIVISIBILITY_INVALID` for provenance/control/implementation failure.

## Claim locks
No all-angle integrability theorem follows from this gate alone. No global K5 cancellation/non-cancellation theorem, Stokes/IBP theorem, period theorem, physical finite-part selector, F9/G3/G8/K5 promotion, complete-QG claim, or NEW_PHYSICS_FOUND claim. The published spectral i-epsilon remains unchanged.
