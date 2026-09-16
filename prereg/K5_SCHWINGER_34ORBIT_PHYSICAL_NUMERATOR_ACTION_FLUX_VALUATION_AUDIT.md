# Prospective preregistration — K5 34-orbit Schwinger physical numerator/action-flux valuation audit

Status: FROZEN BEFORE IMPLEMENTATION/PRODUCTION.

## Scientific question
Determine, orbit-by-orbit over the 34 S5 orbit types of labeled edge subsets Z of K5, whether the confirmed degree-4 face-tangent Kirchhoff annihilator admits a justified higher-codimension Schwinger boundary/Stokes treatment when acting on the two actual all-32 invariant-dual degree-27 numerators N1,N2.

This gate is independent of the still-open constant-2x2 pointwise closure retry. It MUST NOT infer an integrated period relation merely from pointwise action identities.

## Frozen inputs
- newest-main canonical degree-27 physical numerator DAG and its exact hashes/provenance;
- confirmed unique modulo-radial degree-4 S5-equivariant face-tangent logarithmic class v with v(Psi_K5)=0;
- exact denominator valuation lemma ord_Z Psi_K5 = c(K5\\Z)-1;
- complete 1024 labeled edge subsets reduced to exactly 34 S5 orbit types;
- projective integrands Omega_9 prod_e alpha_e^(1/2) N_c / Psi_K5^(21/2), c=1,2;
- exact projective-gauge action/flux formula from controlling main.

## Frozen exhaustive audit
For every one of the 34 S5 orbit representatives and both physical channels:
1. reconstruct the representative Z and verify its full S5 orbit exhaustively against all 1024 labeled subsets;
2. recompute ord_Z Psi_K5 combinatorially from spanning trees and independently verify c(K5\\Z)-1;
3. compute exact simultaneous scaling valuation ord_Z N_c from the canonical DAG, without generic-point substitution or fitted cancellation;
4. compute exact simultaneous scaling valuation of the action/normal-flux numerator induced by the confirmed annihilator, retaining all cancellations exactly;
5. combine numerator, prod alpha^(1/2), denominator and projective/normal measure scaling explicitly; record the resulting boundary exponent/valuation and whether the corresponding corner flux is provably vanishing, finite/nonzero-possible, divergent/nonintegrable, or unresolved;
6. verify all members of each S5 orbit give the same classified valuation after covariant transport;
7. preserve N1 and N2 separately; no post-hoc linear combination may be fitted to cancel a boundary contribution.

## Mandatory controls
- all 1024 subsets covered exactly once by the 34 orbit partition;
- denominator valuation independently recomputed rather than imported as a label;
- at least one deliberately corrupted Psi valuation must be rejected;
- at least one deliberately corrupted numerator/action valuation must be rejected;
- at least one broken S5 transport/orbit representative must be rejected;
- single-edge faces must reproduce the already-established pointwise zero open-face flux behavior;
- raw homogeneous scaling and simplex gauge must never be mixed; homogeneity checks are mandatory.

## Frozen classifications
Only one of:
- K5_SCHWINGER_34ORBIT_PHYSICAL_ACTION_FLUX_ALL_CORNERS_VANISH_EXACT_SCOPED
- K5_SCHWINGER_34ORBIT_PHYSICAL_ACTION_FLUX_NONVANISHING_CORNER_FOUND_EXACT_SCOPED
- K5_SCHWINGER_34ORBIT_PHYSICAL_ACTION_FLUX_NONINTEGRABLE_CORNER_FOUND_EXACT_SCOPED
- K5_SCHWINGER_34ORBIT_PHYSICAL_ACTION_FLUX_AUDIT_INCONCLUSIVE_SCOPED
- INVALID_GATE
- INFRASTRUCTURE_OR_NUMERICAL_FAILURE

The first classification requires an exact vanishing certificate for every audited corner/orbit and both channels under the frozen scaling analysis. A finite-grid/sample-only observation is insufficient.

## Claim firewall
Even ALL_CORNERS_VANISH does not by itself establish a physical finite-part selector, K5 period zero/nonzero, regulator independence, unique supported extension, F9/G3/G8, NEW_PHYSICS_FOUND, or complete quantum gravity. Promotion to an integrated projective IBP/Stokes relation requires a separate prospectively preregistered gate and independent review of the global Stokes hypotheses.

No frozen criterion in this file may be changed after viewing substantive production output.