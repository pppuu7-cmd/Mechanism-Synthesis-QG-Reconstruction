# K5 order-eight invariant-dual / projective-IBP frontier

Date: 2026-09-16

## Controlling exact chain

1. Full all-32 invariant-dual projective object:
   - result `results/K5_ORDER8_INVARIANT_DUAL_PROJECTIVE_IBP_REACHABILITY_RESULT.md`;
   - commit `e9ed372a91ac1bd219dc7671a916c70405e9cd43`;
   - run `35036111528`;
   - classification `K5_INVARIANT_DUAL_PROJECTIVE_OBJECT_DEFINED_IBP_REDUCTION_INCOMPLETE_SCOPED`.

2. S5-equivariant regular face-tangent logarithmic module, component degree <=2:
   - result commit `ee965976e0af8f3b569407e917b0046f02b79649`;
   - exact non-radial quotient dimension zero.

3. Component degree 3:
   - first implementation permanently `INVALID_IMPLEMENTATION` by outcome-independent audit `cf618ae9a3bbe8a4b97171dce973c2a4cb1b803f` because mandatory frozen controls were not actually executed;
   - prospectively frozen control-only repair `27ffc236cf2f7e3b555811f2a1b2aa1684a61ddf`;
   - repaired run `35043530093`, artifact `10425543584`, JSON SHA256 `b4c1ea8b4aefbef905b1354b70786b7c644181d261140830291d0ff8f0f3797e`;
   - result commit `ed7a2aa05e0fa6bb75d63fa5328665059d0a012b`;
   - classification `K5_S5_FACE_TANGENT_LOG_IBP_DEG3_RADIAL_ONLY_EXACT_SCOPED`;
   - exact system `2565 x 14`, rank `11`, nullity `3`, radial dimension `3`, non-radial quotient `0`.

4. Component degree 4 — first genuine non-radial class:
   - prereg `00b5ddf78474179281380606fbc3f62ca260e337`;
   - solver `55cfdf27e616befaf39b5f3ec0d1c04d7e083669`;
   - production head `53bdd4d6adb5e470192292d7ef2616a57e15fc6e`;
   - run `35043883583`, job `104629427085`, success;
   - artifact `10426228492`, ZIP digest `sha256:37f52650a70c11f7969302294b726e611ecc74a1adbf44889699daba788db5ca`;
   - JSON SHA256 `7fe9fb47da97a5c396c69d7153d8c25c4cef2f4b95c6f4cb1850cba889bffca4`;
   - result `results/K5_ORDER8_S5_DEG4_KIRCHHOFF_ANNIHILATOR_RESULT.md`, commit `686268eddb3f0e2aece5857ef75cec52716eccc6`;
   - classification `K5_S5_DEG4_NONRADIAL_ANNIHILATOR_EXISTS_EXACT_SCOPED`.

Exact degree-four dimensions:

- complete fixed-edge cubic orbit count: 33;
- complete S5 invariant cubic quotient dimension: 7;
- logarithmic system `7180 x 40`;
- rank `32`, nullity `8`;
- radial Euler dimension `7`;
- non-radial quotient dimension `1`;
- vector-only annihilator kernel dimension `1`;
- the unique non-radial class admits `v(Psi_K5)=0` exactly.

5. Independent Critic for degree 4:
   - prospectively frozen prereg `7cde5bd6838e40b7d10fe7dd9707f04cc3198662` while Researcher production was queued;
   - Critic head `3ea822da929ebe8c4fe34c11383efd800b3979e9`;
   - run `35044426437`, job `104631081292`, success;
   - artifact `10426875582`, ZIP digest `sha256:b7f477067778424f6d37d749317096c47056e7f47af447f30816612e820ffb36`;
   - Critic JSON SHA256 `48bfa209b9f01e8e6bca351bced9211134f76f73bd46692b8078a7e4083732db`;
   - durable review `results/K5_ORDER8_S5_DEG4_KIRCHHOFF_ANNIHILATOR_INDEPENDENT_CRITIC_RESULT.md`, commit `8668ca4df577c3f8d95cf4d4d7dcce72630916f5`;
   - verdict `CONFIRMED_SCOPED`.

Critic independently reconstructed `det L` and the 125-tree polynomial, all cubic orbit data, the `7180 x 40` matrix and the vector-only kernel. It read the Researcher-emitted 33 coefficients and directly verified exact zero, non-radial independence, face tangency and all 120 S5 transports.

## Current object bottleneck

The two physical invariant-dual channels have exact structural form

`Omega_9 * prod_e alpha_e^(1/2) * N_c(alpha) / Psi_K5(alpha)^(21/2)`, `deg N_c=27`,

but `N_1,N_2` were not previously materialized as reusable exact coefficient objects.

Object audit: `sources/K5_INVARIANT_DUAL_DEG27_NUMERATOR_MATERIALIZATION_AUDIT.md`, commit `ecebc3670c63fe877e2ec5eddd84bc36252b3430`.

Prospective canonical-DAG gate:

- prereg `faa436e10301ecb92f2e4558411f0d1af6f4594f`;
- implementation `ce6aa550f706c1f1980787b9e6ab455e9749b5f6`;
- workflow head `d094ee6204845592ac395a67b94501461e98e4ff`;
- run `35044686796` currently authoritative for this materialization attempt; partial values must not be used while non-terminal.

The frozen canonical DAG contains exact `Psi`, polynomial `adj L`, edge covariance numerators, source radius `Q=L_uniform/5`, source-entry coefficients, full-32 source contraction and dual Reynolds data. Acceptance requires exact reproduction of the old all-32 uniform result, independent `00000` nonuniform controls at two rational points, and exact degree-27 homogeneity.

## Projective action derivation

Exact derivation: `sources/K5_DEG4_ANNIHILATOR_PROJECTIVE_GAUGE_ACTION_DERIVATION.md`, commit `97e71f0c20173b0c387461ff7f860baa12897fcd`.

For confirmed annihilator `v_i=alpha_i q_i`, define

`s1=sum_i alpha_i`, `S=sum_i v_i`, `c=S/s1`, `u_i=v_i-c alpha_i`.

Then `sum_i u_i=0` and `u` is tangent to `s1=1`. For

`F_N=W N/Psi^(21/2)`, `W=prod_i alpha_i^(1/2)`,

one has exactly

`div(u F_N)=W/Psi^(21/2) * { v(N)+[div v +(1/2)sum_i q_i -3S/s1]N }`.

A homogeneous projective representative is

`B_v[N]=s1 v(N)+{s1[div v +(1/2)sum_i q_i]-3S}N`,

appearing as `B_v[N]/s1^4`.

Open codimension-one face flux vanishes because `u_i~alpha_i` and `W~alpha_i^(1/2)`, but this does **not** yet justify global Stokes at higher-codimension Schwinger corners where `Psi` may vanish. Complete corner power counting / sector audit is mandatory before dropping all boundary terms.

## Highest-information next gates

1. Finish the already-frozen canonical-DAG materialization run for `N_1,N_2`.
2. Prospectively freeze annihilator action on those exact numerator DAGs:
   - compute `B_v[N_1],B_v[N_2]` exactly or by an equivalent hashable differentiated DAG;
   - test exact zero/nonzero and whether the action closes in a finite numerator module;
   - do not infer integrated relations before boundary authority.
3. In parallel/next, audit all higher-codimension Schwinger boundary scaling strata for the gauge-projected annihilator flux.
4. Only if that Stokes boundary gate closes, use the IBP relation to reduce/evaluate the two invariant-dual projective periods.

## Still unresolved

- the two invariant-dual integrated K5 periods;
- the full 217-dimensional order-eight tensor/annihilator;
- the complete `dim_C F_8=377` physical extension selector;
- global multistratum patching;
- causal multivertex bridge;
- G3 quantum dynamics, regulator removal, RG/refinement, continuum/spin-2/GR/matter/prediction chain.

No `NEW_PHYSICS_FOUND` or complete-QG claim is authorized.
