# Result — exact projective-normal corner order on all 32 proper K5 subset orbits

Date: 2026-09-17

## Frozen gate

Prospective preregistration: `prereg/K5_PROJECTIVE_NORMAL_32ORBIT_EXACT_CORNER_ORDER.md`, commit `61d8a72c775d14356695196c50aa2395f9b9afc5`.

The gate was opened while the full-source boundary S5 symbolic theorem remained pending independent Critic scientific reconstruction. Therefore this calculation was deliberately restricted to the independently confirmed annihilator/projective-normal geometry and did not consume the unconfirmed boundary transport theorem or evaluate physical `N_c`/`B_v[N_c]` coefficients.

## Production authority

- workflow/head: `144e6233523e84da833ef683c3ce2a1c4ca17ac6`;
- run `35221623366`, terminal `success`;
- job `105202916089`, terminal `success`;
- artifact `10497486987`, `k5-projective-normal-32orbit-exact-corner-order`;
- artifact ZIP digest `sha256:5f4bc8fc1e70d2dfa9af0857ef09eea3a3ae8a3d94af7089e7ab741f6baa0bf1`;
- full production JSON SHA256 `80e614f10a8fcc0f1e96732ca5cd27feffb7b1683f1e26be3685417635ecaba8`;
- executed script SHA256 `d0495f3f49ae1bb15fe7e5f0037bb44af30ea190c903ac0a76372e59475f8bad`.

Durable compact machine authority: `results/raw/k5_projective_normal_32orbit_exact_corner_order_authoritative.json`.

## Exact object

For every proper K5 subset-orbit representative `Z`, with the parent-audit frozen linear corner path

`alpha_e(t)=W_e t` for `e in Z`, `alpha_e(t)=W_e` otherwise,

we evaluate the complete exact degree-at-most-five polynomial

`U_Z^W(t) = [s1 V_Z - S A_Z](alpha(t))`,

where `v_e=alpha_e q_e`, `V_Z=sum_(e in Z)v_e`, `A_Z=sum_(e in Z)alpha_e`, `S=sum_e v_e`, and `s1=sum_e alpha_e`.

Two asymmetric frozen weights are used exactly as in the parent 34-orbit audit:

`W1=(2,3,5,7,11,13,17,19,23,29)`,

`W2=(31,37,41,43,47,53,59,61,67,71)`.

The cyclic S5 control transports both subset and weight vector simultaneously.

## Controls

All frozen controls passed. In particular:

- ten K5 edges, stabilizer order 12, 33 cubic fixed-edge orbits and 33 annihilator coefficients were reconstructed;
- all `q_e` are homogeneous degree 3 and all `v_e` homogeneous degree 4;
- the 125-tree `Psi_K5` was reconstructed and exact `v(Psi_K5)=0` verified;
- exactly 34 subset orbits and 32 proper representatives were recovered;
- every proper multivariate `U_Z` is nonzero homogeneous degree 5, reproducing the prior degree/support authority;
- Route A (multivariate `U_Z` then exact substitution) and independent Route B (substitute each `q_e` first and then build the univariate projective numerator) agree coefficient-by-coefficient for all frozen lanes;
- simultaneous cyclic S5 transport preserves the complete coefficient vector for W1 and W2;
- W1 and W2 agree on zero/nonzero state and first nonzero order on all 32 proper orbits;
- raw `V_Z`, malformed `s1 V_Z-2S A_Z`, an altered annihilator coefficient, a wrong corner path and wrong cyclic weight transport are all detected/rejected;
- no physical-corner finiteness/divergence, global Stokes/IBP or integrated-period verdict is emitted.

## Terminal result

Classification:

`K5_PROJECTIVE_NORMAL_32ORBIT_EXACT_CORNER_ORDERS_RESOLVED_SCOPED`.

All 32 proper-orbit frozen paths are exact nonzero. The first-nonzero-order histogram is

- order `1`: 28 orbits;
- order `2`: 3 orbits;
- order `3`: 1 orbit.

The four higher-order representatives are:

1. orbit index 18, mask `127`, `k=7`, bits `[0,1,2,3,4,5,6]`: `r_U=2`;
2. orbit index 29, mask `255`, `k=8`, bits `[0,1,2,3,4,5,6,7]`: `r_U=2`;
3. orbit index 30, mask `495`, `k=8`, bits `[0,1,2,3,5,6,7,8]`: `r_U=2`;
4. orbit index 31, mask `511`, `k=9`, bits `[0,1,2,3,4,5,6,7,8]`: `r_U=3`.

For the `k=9` representative the frozen exact vectors are

`W1: (0,0,0,232317840,115106800,0)`,

`W2: (0,0,0,122486107098,32083267142,0)`.

Thus the corrected projective normal component generically starts linearly on most orbit types, but exact lower-order cancellations raise its vanishing order on four high-codimension orbit types. No proper frozen path is annihilated identically.

## Scientific consequence

One of the three target families of the already-frozen `K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION` now has its exact frozen-path order resolved independently of the pending boundary-transport Critic: `U_Z` needs no further cancellation search on these 32 orbit representatives.

This does **not** authorize substantive consumption of the parent resolver yet because its physical `N_c` and `B_v[N_c]` targets still depend on coefficient-level source/boundary transport authority, whose independent Critic scientific reconstruction remains pending.

## Interpretation ceiling

No physical corner is classified finite/logarithmic/divergent by this result alone. No local K5 amplitude finiteness/divergence theorem, global projective Stokes/IBP theorem, invariant-dual K5 period result, full 217-dimensional tensor theorem, reduction of `dim_C F_8=377`, physical finite-part selector, regulator-independence theorem, F9/G3/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete-QG claim follows.