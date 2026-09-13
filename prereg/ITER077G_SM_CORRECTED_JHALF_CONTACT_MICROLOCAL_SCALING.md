# Iter077G-SM preregistration — corrected j=1/2 source contact, microlocal collision, and scaling threshold

**Date:** 2026-09-14  
**Status:** prospective / frozen before implementation

## Motivation and provenance

Historical `Iter077E-SM` microlocal and `Iter077F-SM` scaling gates used a mis-transcribed Appendix-D contact formula. They are quarantined by `status/ITER077_CONTACT_FORMULA_ERRATUM.md` and cannot be promoted as authoritative source-dependent results.

This corrected gate uses only:

- primary causal-vertex Appendix D Eqs. (37)-(39), frozen in `sources/CAUSAL_SPINFOAM_VERTEX_2026_CONTACT_EQ37_39_CORRECTED_SNAPSHOT.md`;
- source snapshot commit `edc8bd718c5ac381e26b57636963cfb180f3ecd7`;
- authoritative `Iter077A-SM`, `Iter077C-SM`, and canonical mixed `Iter077D-SM` results;
- the Brunetti-Fredenhagen scaling-degree extension theorem as frozen in the corrected source snapshot.

The control sector is all `j_e=1/2`, gamma-simple `rho_e=gamma/2`, with finite real `gamma != 0`. The exact rational control remains `gamma=6/5`.

No arbitrary mollifier, finite part, counterterm or scalar-incidence surrogate is allowed as a physical input.

## Lane A — exact primary-source contact coefficients

Starting from

`F_(1/2)(rho+q,rho) = ((rho+q)^2+1/4)/(rho^2+1/4)`

and source Eq. (37)

`delta^(rho,j)(x)=sum_{n=0}^{2j} [c_{n+1}/(n+1)!] (-i)^(n+1) delta^(n)(x)`,

PASS iff exact symbolic algebra gives:

1. `c_1=2 rho/(rho^2+1/4)`;
2. `c_2=2/(rho^2+1/4)`;
3. `delta^(rho,1/2)=-(2 i rho/D) delta -(1/D) delta'`, `D=rho^2+1/4`;
4. gamma-simple coefficients
   `A_gamma=-4 i gamma/(1+gamma^2)` and
   `C_gamma=-4/(1+gamma^2)`;
5. at `gamma=6/5`, `A=-120 i/61`, `C=-100/61`;
6. `C_gamma` has no finite real zero and `A_gamma` has only the zero `gamma=0`.

Any mismatch is scientific FAIL, not a formula repair.

## Lane B — corrected generic/exceptional microlocal split

Reconstruct exactly:

- the frozen `Iter077A-SM` rank-10 true-source Jacobian witness;
- the frozen `Iter077C-SM` rank-9 witness `xxxxxyyyzz` and
  `lambda=(1,-1,0,0,1,0,0,0,0,0)`.

Use the corrected ten-contact Fourier polynomial

`P_10(xi)=K_gamma prod_e (gamma+xi_e)`,

`K_gamma=[-4 i/(1+gamma^2)]^10`.

PASS iff:

1. generic witness has `rank(J)=10` and `ker J^T={0}`;
2. rank-9 witness has `rank(J)=9`, `lambda != 0`, `J^T lambda=0`;
3. exact restriction
   `P_10(t lambda)=K_gamma gamma^7 (gamma+t)^2 (gamma-t)`;
4. for finite real `gamma != 0`, this restriction is a nonzero degree-3 polynomial in `t` and therefore not rapidly decreasing along the self-stress ray;
5. consequently the standard canonical pullback is authorized locally on the rank-10 submersion region but the standard Hörmander wavefront/normal-set disjointness condition fails for the corrected ten-contact tensor at the frozen rank-9 point;
6. failure of this criterion is explicitly **not** interpreted as nonexistence of the source-selected correlated spectral boundary value.

Frozen PASS classification for this lane:

`ITER077G_SM_CORRECTED_CONTACT_GENERIC_SUBMERSION_ALLOWED_RANK9_SELFSTRESS_WAVEFRONT_COLLISION_EXACT_SCOPED`.

## Lane C — invariant highest self-stress contact order

Use the same exact Fourier restriction, rather than an arbitrary completion of target coordinates.

PASS iff:

1. `deg_t P_10(t lambda)=3` for finite real `gamma != 0`;
2. the degree equals exactly the number of nonzero entries of the frozen self-stress (`3`);
3. the leading coefficient is
   `-K_gamma gamma^7`;
4. this coefficient is nonzero for finite real `gamma != 0`;
5. at `gamma=6/5` the leading coefficient is evaluated exactly and nonzero;
6. therefore the all-spin-half target contact tensor has a genuine nonzero `n_eff=3` excess/conormal derivative channel before smooth phase, measure, spinor and boundary-intertwiner contraction.

No claim is permitted that this channel survives the **full** contracted causal vertex.

## Lane D — six-dimensional scaling-degree extension threshold

Use the canonical mixed `Iter077D-SM` nondegenerate quadratic normal form in six transverse variables.

For `n=0,1,2,3`, compute exactly

`sd_n=2(n+1)`.

PASS iff:

- `n=0`: `sd=2<6`, unique extension preserving scaling degree;
- `n=1`: `sd=4<6`, unique extension preserving scaling degree;
- `n=2`: `sd=6`, first marginal ambiguity, local derivative order at most `0`;
- `n=3`: `sd=8`, nonunique by scaling degree alone, local derivative order at most `2`;
- the unconstrained local ambiguity-space dimension through total derivative order `2` in six variables is exactly `1+6+21=28`;
- unique distributional extension is kept distinct from absolute integrability/ordinary-measure interpretation.

This lane is an extension-theory statement only. It does not assert that the source spectral `i epsilon` prescription leaves 28 free parameters; the source prescription may select or cancel a specific combination.

## Aggregate PASS

Aggregate PASS requires all lanes A-D PASS under the frozen formulas above.

Classification:

`ITER077G_SM_CORRECTED_JHALF_CONTACT_HAS_NONZERO_RANK9_N3_SELFSTRESS_CHANNEL_SD8_SOURCE_SELECTED_CORRELATED_EXTENSION_REQUIRED_EXACT_SCOPED`

## Aggregate FAIL

If the exact source formula, Fourier restriction, source ranks, or scaling table fails a frozen prediction while the object remains well-defined:

`ITER077G_SM_CORRECTED_CONTACT_MICROLOCAL_SCALING_PREDICTION_FAILS_EXACT_SCOPED`

Scientific FAIL must be preserved as a valid workflow result.

## Aggregate BLOCKED

If primary-source provenance or a required exact object is unavailable:

`ITER077G_SM_CORRECTED_CONTACT_MICROLOCAL_SCALING_BLOCKED_OBJECT_DEFINITION`

## Consequence on PASS

The local rank-9 problem is reduced to one explicit source object:

`SOURCE_SELECTED_CORRELATED_SPECTRAL_I_EPSILON_EXTENSION_OF_THE_N_EFF_3_RANK9_CONTACT_CHANNEL`.

The next admissible gate must derive that correlated extension from the published spectral prescription and then test it after the exact smooth Toller/spinor/intertwiner factors. Scaling-degree freedom alone may not be replaced by arbitrary counterterms.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no assertion that the full source-selected causal vertex fails to exist; no causal-vertex finiteness/divergence theorem; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal `epsilon^-1` coefficient; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; retain the published spectral `i epsilon`.