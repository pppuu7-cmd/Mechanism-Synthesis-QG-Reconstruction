# K5 degree-4 annihilator — corrected projective constant-2x2 closure result

Date: 2026-09-16

## Status

`PASS_EXACT_SCOPED`

Classification:

`K5_PROJECTIVE_CONSTANT2X2_CLOSURE_FALSIFIED_EXACT_SCOPED`

## Prospective contract

Preregistration:

`prereg/K5_DEG4_ANNIHILATOR_PROJECTIVE_CONSTANT2X2_CLOSURE.md`, commit `4f1e49f9d850fa7834dd189228d0787f84406f84`.

The gate was opened only after independent Critic commit `dfaf9ca72f056d2bfcb4e8bbdff8b9301f54107e` established that the historical raw closure test `B_v[N]=MN` compared homogeneous degrees 31 and 27 and therefore tested the wrong closure object.

The corrected degree-matched projective object is

`P_v[N](alpha)=B_v[N](alpha)/s1(alpha)^4`,

with `deg P=deg N=27`.

## Parent provenance

Exact parent values are locked from repaired production:

- run `35130545821`;
- job `104910177408`;
- artifact `10461780450`;
- artifact ZIP digest `sha256:d1b2bbd109aa0a3969e37e97aa3e572fc4cba368c42fdc145f94689afbc032dd`;
- production JSON SHA256 `909b2afc8474b317a424ba59f108756441bdd8cdf8888cb85763d6c368fe95b8`;
- implementation head `4e70e991ff0c5e312feac4556082e9be01afe598`;
- full all-32 / `100000` source-term object;
- invariant-dual projection retained.

Machine-readable parent point lock:

`sources/raw/k5_deg4_projective_closure_parent_point_lock.json`, commit `14b7926ada4e4dab64c542bbd7b243035f362ff4`.

## Production

Validator:

`scripts/k5_deg4_projective_constant2x2_closure.py`, commit `63538524d53aa0888effb9a5741572a9dc86150f`.

Workflow/head:

`.github/workflows/k5_deg4_projective_constant2x2_closure.yml`, head `d508fd145973a2ad4a8772368e00c5e599c5f908`.

Authoritative production:

- run `35140030858`, terminal success;
- job `104941953222`, terminal success;
- artifact `10464124390`;
- artifact ZIP digest `sha256:cbe6f218de38f816b30637e48198edf6f4c72a8ffdc3b18931e0f0f733ccf92d`;
- production JSON SHA256 `d9a86723b7baa5e947e0d21998d7468b61b5e26e90fce272bd8db07d677c05b4`.

All frozen checks and malformed controls passed.

## Exact construction

Frozen representative sums are

- `s1(fit_A)=11`;
- `s1(fit_B)=15`;
- `s1(validation_U)=10`;
- `s1(validation_G)=20`.

For every channel and point the validator computes exactly

`P=B/s1^4`.

The two fit points have nonzero exact numerator determinant

`29427625893405583852377851198976000000000000`,

so they define a unique rational constant `2x2` fit matrix:

`M_11=-407770141079347782633925616839/5747675655287960631335444630625`,

`M_12=-97672545871972311778123404484/1915891885095986877111814876875`,

`M_21=2654209224684473051911103826304/17243026965863881894006333891875`,

`M_22=-986735247126900791664537534851/5747675655287960631335444630625`.

By construction the residual vectors at `fit_A` and `fit_B` are exactly zero.

## Prospective validation

At `validation_U` the exact projective residuals are

`7025983846469736430847744951220312500000000/25334107571517181846106643`,

`73322633497930679227900303333764062500000000/76002322714551545538319929`.

Both are nonzero.

At `validation_G` the exact projective residuals are

`228137617695572295597735908822087775610266465901728402048/5497853205624388421464115234375`,

`-1520563707365418540588747900509832247312047848360862134816/5497853205624388421464115234375`.

Both are nonzero.

Hence all four prospectively frozen validation residual components are nonzero.

## Projective controls

The validator verifies exactly under `alpha -> 2 alpha`:

`N -> 2^27 N`,

`B -> 2^31 B`,

`P=B/s1^4 -> 2^27 P`,

and each closure residual scales by `2^27`. Therefore the failure cannot be created or removed by changing homogeneous representative.

The wrong denominator powers `s1^3` and `s1^5` are rejected by homogeneous-degree mismatch. The historical raw `B=MN` object is separately rejected as degree incompatible whenever `B` is nonzero.

## Scientific result

The corrected physical degree-27 projective annihilator action on the two actual invariant-dual channels does **not** close through one constant rational `2x2` matrix on the prospectively frozen fit/validation representatives.

This is the corrected successor requested by the independent Critic. The earlier raw-cone closure failure is not used as the scientific reason for this result.

## Interpretation ceiling

This result excludes only the constant two-channel projective closure ansatz. It does not prove that all projective IBP reduction fails. Polynomial/rational coefficient modules or additional channels may remain.

Finite-point falsification is sufficient to disprove a global constant-matrix identity, but finite-point agreement would not have proved one; no stronger global module theorem is assigned.

No integrated K5 period zero/nonzero theorem, no Stokes theorem, no full 217-dimensional tensor theorem, no reduction of `dim_C F_8=377`, no physical finite-part selector, no regulator-independence theorem, no F9/G3/G8 promotion, no `NEW_PHYSICS_FOUND`, and no complete-QG claim follows.

## Authorized successor

The cheapest constant projective module is now exactly excluded. The next algebraic closure gate, if pursued, must prospectively define the smallest degree-consistent polynomial/rational coefficient module and retain both invariant-dual channels. Independently, any integrated-period/Stokes route still depends on the separately corrected projective-tangent boundary-flux and corner analysis.
