# Current MSQGR research state

**Date:** 2026-09-16

## Global scientific ceiling

Candidate remains `CRQN v0.2`, `CARRIER_SELECTED` only for established source-backed F1-F8 carrier/mechanism structure.

Predictive local K5 amplitude remains `BLOCKED_CURRENT_CANDIDATE_LOCAL_AMPLITUDE`; physical F9/G3 and every downstream QG arrow remain blocked.

Frozen all-`j=1/2` same-scaling-degree supported-extension freedom remains

`dim_C F_8 = 377`.

No current result selects a physical finite part, removes this 377-dimensional freedom, proves regulator independence, global patching, a complete K5 amplitude, `NEW_PHYSICS_FOUND`, or complete QG.

## Controlling source/order authority

Source ordering remains

`one-wedge spectral/spinor integration -> Toller function -> product of ten Toller matrices -> full boundary contraction -> K5 group/distributional object`.

Historical source-lock-invalid Iter077E/F remain quarantined under `status/ITER077_CONTACT_FORMULA_ERRATUM.md`. Iter077I authoritative source-order lock remains corrected run `34786586785` from alias head `102fc7268b732bead5dfcf6d61fe4479ae1d3030`; failed historical run `34786550378` is not authority. Published one-wedge spectral `i epsilon` remains locked.

K3 simple residue is exact zero and independently confirmed. K4 simple order-3 residue is exact zero and independently confirmed.

## Full all-32 invariant-dual K5 projective object

`results/K5_ORDER8_INVARIANT_DUAL_PROJECTIVE_IBP_REACHABILITY_RESULT.md`, commit `e9ed372a91ac1bd219dc7671a916c70405e9cd43`, defines two invariant dual/covector projective channels

`Omega_9 * prod_e alpha_e^(1/2) * N_c(alpha) / Psi_K5(alpha)^(21/2)`

with `deg N_c=27`, `deg Psi_K5=4`, full all-32/100000-source-term contraction and invariant-dual rank two. Integrated periods remain unknown.

Terminal reusable numerator-DAG authority is `results/K5_INVARIANT_DUAL_DEG27_CANONICAL_DAG_RESULT.md`, commit `666aa6e61f62bbfff456f6be7995ce3a65f2b633`, run `35044686796`, artifact `10426617568`, canonical DAG SHA256 `f8eaaa5c7923497a67f0354a2d59475f4b6d82022e032fc005c1d9d2add69992`.

## Degree-four Kirchhoff annihilator

The unique non-radial degree-four S5-equivariant class is independently confirmed, with `v(Psi_K5)=0`. Researcher authority commit `686268eddb3f0e2aece5857ef75cec52716eccc6`; independent Critic commit `8668ca4df577c3f8d95cf4d4d7dcce72630916f5`.

Exact projective-gauge action uses

`B_v[N]=s1 v(N)+{s1[div v +(1/2)sum_i q_i]-3S}N`,

with `v_i=alpha_i q_i`, `S=sum_i v_i`, `s1=sum_i alpha_i`.

Historical Researcher raw-uniform normalization was independently falsified: at raw uniform `s1=10`, not `1`, and

`B_v[N_c]=-1500N_c`.

Repaired normalization Critic run `35049858473`, artifact `10429566785`, ZIP digest `sha256:490f05d243fc16ead6ac2f1f0cd16e60d6a8adccf7cca25368ab3317e580c43a`, verdict `SCIENTIFIC_FAIL_CONFIRMED` for the historical factor-ten equality.

## Repaired Researcher action gate — terminal, but constant-closure interpretation not authorized

Parent preregistration: `prereg/K5_DEG4_ANNIHILATOR_ACTUAL_DUAL_NUMERATOR_POINTWISE_ACTION.md`, commit `2111b42adc1ab79247c72d0043e5332b24eb7679`.

Control-only normalization/performance repair: `prereg/K5_DEG4_ANNIHILATOR_ACTUAL_DUAL_NUMERATOR_POINTWISE_ACTION_CONTROL_REPAIR_1.md`, commit `500fd80d900c99f71c66869dfe99fa4f35adc5f5`.

Historical run `35045552470` is terminal cancelled and has no substantive authority.

Repaired production:
- head `4e70e991ff0c5e312feac4556082e9be01afe598`;
- run `35130545821`, success;
- job `104910177408`, success;
- artifact `10461780450`;
- ZIP digest `sha256:d1b2bbd109aa0a3969e37e97aa3e572fc4cba368c42fdc145f94689afbc032dd`;
- production JSON SHA256 `909b2afc8474b317a424ba59f108756441bdd8cdf8888cb85763d6c368fe95b8`.

Researcher classification was

`K5_DEG4_ANNIHILATOR_ACTION_NONZERO_CONSTANT2X2_CLOSURE_FALSIFIED_EXACT_SCOPED`.

The exact nonzero action part survives: at raw uniform

`N_1=-7038281250000000000`,
`N_2=-5474218750000000000`,

`B_1=10557421875000000000000`,
`B_2=8211328125000000000000`,

so `B_v[N_c]=-1500N_c` and both channels are nonzero.

### Independent Critic review — controlling

Critic prereg `8dbccbe6d50631ba02ba44f0f8edcf6698ea16ca`.

Critic implementation `06514e58c5f57d391216babf5c45dbc958eafaf4`; workflow/head `601b438f806950ce3ac5dde903ed55b76bf81159`.

Critic production:
- run `35131574930`, terminal success;
- job `104913612191`, terminal success;
- artifact `10460848396`;
- ZIP digest `sha256:f6b20aac04ac480deaa3e02df71b30fb1c7664c248fada502e6c3a348d0cb9d3`;
- Critic JSON SHA256 `a8ee6def9dd2690fc315df069784398fedd9bc09ed36b076fe7abb726af79d8c`.

Controlling review: `results/K5_DEG4_ANNIHILATOR_ACTUAL_DUAL_ACTION_REPAIR1_ADVERSARIAL_REVIEW.md`, commit `dfaf9ca72f056d2bfcb4e8bbdff8b9301f54107e`.

Mandatory Critic verdict:

`REQUIRES_NEW_PREREGISTERED_GATE`.

Reason: the Researcher closure subtest compares homogeneous `deg B=31` directly to a constant matrix times homogeneous `deg N=27`. Once `B` is nonzero this raw-cone closure is impossible by grading alone. Under `alpha -> lambda alpha`, `B` scales as `lambda^31` while `MN` scales as `lambda^27`. The Critic exact `lambda=2` witness gives nonzero residuals in both channels independent of the Researcher fitted matrix.

The already-existing projective-gauge derivation defines the actual degree-27 projective numerator as

`P_v[N]=A_v[N]/s1^3=B_v[N]/s1^4`.

Therefore the repaired Researcher gate does **not** establish failure of constant closure for the physical degree-27 projective module. Its raw `B=M N` failure is exact but grading-automatic. The interpretation that richer physical projective coefficient modules/additional channels are required is not downstream authority.

Authorized successor object: prospectively test constant closure for `P_v[N]=B_v[N]/s1^4`, or an exactly equivalent common-simplex `s1=1` representation with representatives normalized before fitting/testing. This is an OBJECT/HYPOTHESIS change and must be a new preregistered gate.

## Schwinger boundary/Stokes firewall

The obsolete raw-ambient projective normal-flux formula is independently `SCIENTIFIC_FAIL_CONFIRMED`. For

`Omega_9=i_E(dalpha_1 wedge ... wedge dalpha_10)`

only the projective vector-field class modulo Euler-radial fields matters. On `s1=1`, the tangent representative is

`u_i=v_i-(S/s1)alpha_i`.

The scalar blow-up Jacobian exponent `t^(k-1)` is retained, but raw `v(t)` is not the projective normal flux.

The first corrected tangent-flux Researcher implementation/run `35104985610` is independently `INVALID_IMPLEMENTATION`; it did not mechanically execute the frozen differential-form/blow-up obligations.

A prospectively frozen control-only repair now exists:

`prereg/K5_SCHWINGER_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING_CONTROL_REPAIR_1.md`.

It requires explicit `Vol`, `Omega_9`, contractions, genuine blow-up pullback, two genuinely distinct projective charts, radial/Euler invariance and exceptional leading-zero controls. Until terminal repaired production plus independent review, the 34-orbit physical numerator/action-flux audit remains blocked from substantive corner classification.

No global Stokes/IBP or integrated K5 period theorem is authorized.

## Current survival chain

`F1-F8 carrier`
`-> source-ordered K5 off-collision object`
`-> exact supported ambiguity F_8, dim=377`
`-> source-faithful 16-parameter meromorphic germ CONFIRMED`
`-> K3 residue ZERO_EXACT CONFIRMED`
`-> K4 residue ZERO_EXACT CONFIRMED`
`-> K5 Schwinger/projective reduction VALIDATED`
`-> full all-32 invariant-dual projective object DEFINED`
`-> unique degree-4 non-radial Kirchhoff annihilator CONFIRMED`
`-> physical N_1,N_2 degree-27 DAG MATERIALIZED`
`-> raw-uniform normalization SCIENTIFIC_FAIL_CONFIRMED; corrected action NONZERO`
`-> raw homogeneous B=constant-M*N closure impossible by grading; NOT projective closure authority`
`-> projective degree-27 P=B/s1^4 closure ?`
`-> scalar corner Jacobian k-1 retained`
`-> obsolete raw-v projective flux SCIENTIFIC_FAIL_CONFIRMED`
`-> corrected projective-tangent flux first implementation INVALID_IMPLEMENTATION; repair pending`
`-> 34-orbit physical numerator/action-flux audit BLOCKED`
`-> global projective Stokes/IBP relation ?`
`-> invariant-dual K5 projective periods ?`
`-> remaining S5/full order-eight tensor ?`
`-> physical finite-part / joint-K5 selector ?`
`-> global patching ?`
`-> causal E3/E4/E6 ?`
`-> quantum dynamics G3 ?`
`-> regulator removal / independence ?`
`-> RG/refinement ?`
`-> continuum 3+1 Lorentzian geometry ?`
`-> massless spin-2 ?`
`-> Einstein/GR ?`
`-> matter/QFT IR ?`
`-> normalized falsifiable prediction ?`.

## Highest-information next work

1. Prospectively freeze `K5_DEG4_ANNIHILATOR_PROJECTIVE_DEG27_CLOSURE` using exact object `P_v[N]=B_v[N]/s1^4` or a mathematically equivalent common-simplex representation. Freeze whether the closure coefficient class is constant, polynomial or rational before output; do not reuse raw heterogeneous representatives without normalization.
2. In parallel, execute the already-frozen control-only repair of `K5_SCHWINGER_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING` and require a new independent Critic review.
3. Do not issue substantive 34-orbit corner classifications, global Stokes identities or integrated K5 period claims until corrected projective tangent geometry is terminal and independently reviewed.
4. If invariant-dual periods eventually vanish, continue remaining S5 sectors; invariant-sector vanishing alone does not prove the full 217-dimensional tensor zero.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no unique physical K5 extension; no physical finite-part selector; no integrated K5 order-eight zero/nonzero theorem; no one-parameter physical `A_-1`; no regulator independence; no generic-spin completion; no global all-strata patching theorem; no causal-vertex finiteness/divergence theorem; no G3/F9/G8/K5 promotion; no fitted subtraction constants/scales or preferred finite parts without independent authority. Retain published one-wedge spectral `i epsilon`.
