# Provenance ledger — K5 projective-normal 32-orbit exact corner order

Date: 2026-09-17

## Upstream authority

- degree-four S5-equivariant Kirchhoff annihilator: Researcher result commit `686268eddb3f0e2aece5857ef75cec52716eccc6`, independently confirmed by Critic commit `8668ca4df577c3f8d95cf4d4d7dcce72630916f5`;
- corrected projective-tangent normal-flux geometry: Researcher result commit `aa8baf37f4beaadf341f2cc6cf3b31415282cc5d`, independently confirmed by Critic commit `57109026cf5bc95262395a3f42e5f121aa9be3ae`;
- projective-normal degree/support gate: prereg `96d7f3acebf37809c15c1ae104d7a98efe462fdc`, run `35215941730`, result commit `f8480064e928c0641fd53f318a0f8f0b0c704a48`, classification `K5_PROJECTIVE_NORMAL_NUMERATOR_DEGREE5_COMPLETE_SUPPORT_EXACT_SCOPED`;
- parent corner representatives, W1/W2 weights and cyclic control originate from the terminal 34-orbit audit and the already-frozen resolver prereg `d6b0e805101c8590eafac71398cc2b1466691752`.

The symbolic all-alpha full-source boundary S5 transport theorem remains Researcher-only authority. Critic static audit run `35207545326` has `scientific_verdict=null`; therefore this gate was designed to be independent of that unresolved dependency and did not evaluate physical `N_c` or `B_v[N_c]` coefficients.

## Prospective chronology

Scientific preregistration was committed before implementation or inspection of any substituted `U_Z(t)` coefficient:

`prereg/K5_PROJECTIVE_NORMAL_32ORBIT_EXACT_CORNER_ORDER.md`, commit `61d8a72c775d14356695196c50aa2395f9b9afc5`.

Implementation:

`scripts/k5_projective_normal_32orbit_exact_corner_order.py`, commit `f06ab7e1d13a3e5352f6d98518a91b7d94fba89d`.

Workflow creation commit:

`de90331d0029a7364cbc89f6fb20390f014688a2`.

Because a newly introduced workflow did not produce the intended push run, an execution-only workflow comment was committed after the workflow already existed. This did not change the scientific contract, object, weights, representatives, controls or classifier:

workflow/head `144e6233523e84da833ef683c3ce2a1c4ca17ac6`.

No scientific repair was required.

## Terminal production

- run `35221623366`, terminal `success`;
- job `105202916089`, terminal `success`;
- artifact `10497486987`, `k5-projective-normal-32orbit-exact-corner-order`;
- artifact ZIP digest `sha256:5f4bc8fc1e70d2dfa9af0857ef09eea3a3ae8a3d94af7089e7ab741f6baa0bf1`;
- full production JSON SHA256 `80e614f10a8fcc0f1e96732ca5cd27feffb7b1683f1e26be3685417635ecaba8`;
- executed script SHA256 `d0495f3f49ae1bb15fe7e5f0037bb44af30ea190c903ac0a76372e59475f8bad`.

Durable compact machine authority:

`results/raw/k5_projective_normal_32orbit_exact_corner_order_authoritative.json`, commit `b65f3fd31dd87fe4848e126fea837d9b5177e5e2`.

Durable result note:

`results/K5_PROJECTIVE_NORMAL_32ORBIT_EXACT_CORNER_ORDER_RESULT.md`, commit `fb280f5ec64d4cfb148ad1db9036afa7b01e5e17`.

## Terminal classification

`K5_PROJECTIVE_NORMAL_32ORBIT_EXACT_CORNER_ORDERS_RESOLVED_SCOPED`.

All controls passed. Route A and Route B agree exactly. Simultaneous cyclic S5 transport preserves the full coefficient vector. W1/W2 agree on exact first nonzero order for every proper orbit. No proper frozen path is exactly zero.

Order histogram: 28 orbit representatives at `r_U=1`, three at `r_U=2`, one at `r_U=3`.

Higher-order representatives are masks `127`, `255`, `495` at order 2 and mask `511` at order 3.

## Claim locks

This result resolves only the frozen-path projective-normal numerator order. It carries no physical corner finiteness/divergence verdict, no global Stokes/IBP relation, no integrated K5 period verdict, no full 217-dimensional tensor theorem, no reduction of `dim_C F_8=377`, no physical finite-part selector, no regulator independence, no F9/G3/G8/K5 promotion, no `NEW_PHYSICS_FOUND`, and no complete-QG claim.

Historical Iter077E/F remain quarantined and the published spectral `i epsilon` remains retained.