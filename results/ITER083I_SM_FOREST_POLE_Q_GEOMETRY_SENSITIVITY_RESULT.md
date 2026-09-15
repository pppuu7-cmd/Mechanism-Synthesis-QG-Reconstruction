# Iter083I-SM — authoritative K3/K4/K5 forest pole complements see S5-invariant Q shape

Date: 2026-09-15
Status: **PASS_EXACT_SCOPED**

## Provenance
- preregistration `b3f2111f72c24620fd7e008b322cfd5b9ed962fa`;
- validator initial `9fd8d409a15358498404b67ed4f79c99815a9957`, pre-production literal-lock repair `e0efca3f103ba5bb6010f3fff64d1d4f507cda13`;
- workflow/head `b418516df09ddf85deda2298c3add57c4e6cc9ec`;
- Actions run `34915925995`, job `104213388315`, terminal success;
- artifact `10376346398`, ZIP digest `sha256:ef891667cb6e36b7f492ebaae525caddfe5e477f14b1c5ff68cfca000b131db6`;
- production JSON SHA256 `3e432ba36d3bf6d04b2f6dd9894eb234ccd7fdae7842abf09d6c0534f722b733`.

## Classification
`ITER083I_SM_AUTHORITATIVE_K3_K4_K5_FOREST_POLE_COMPLEMENTS_SEE_S5_INVARIANT_Q_SHAPE_SCOPED`

Verdict: **PASS_EXACT_SCOPED**.

## Authoritative forest and pole forms
Iter082D supplies 10 K3 blocks, 5 K4 blocks and 1 K5 block, total 16, with 20 maximal chains `B3 subset B4 subset B5`. The corresponding normal dimensions and critical Taylor orders are

- K3: `d=6`, 3 internal edges, `omega=0`;
- K4: `d=9`, 6 internal edges, `omega=3`;
- K5: `d=12`, 10 internal edges, `omega=8`.

For edge regulators `s_e=1+x_e`, every critical block radial factor has the simple pole

`-1/(2 L_B)`,

with

`L_B=sum_(e internal to B) x_e`.

Production regenerated all 16 covectors and all 20 chains and verified exact S5 closure.

## Metrics compared
The exact positive S5-invariant metrics from Iter083G are

`Q1=I`,

`Q2=I+(1/10) A_L(K5)`.

Polar covectors use the dual pairings represented by `Q1^-1` and `Q2^-1`.

## Primitive K5 control
For `L_K5=sum_all_edges x_e`, `Q2^-1 L_K5=(5/8)L_K5`. Thus the primitive overall pole retains the same orthogonal complement, exactly as proved by Iter083H. Iter083I therefore does not manufacture a contradiction with the primitive theorem.

## Proper-stratum sensitivity
For canonical K4 block `B4={0,1,2,3}` and external edge-coordinate witness `z=e_04`, production gives

`<L_B4,z>_(Q1*)=0`,

`<L_B4,z>_(Q2*)=-15/88`.

For canonical K3 block `B3={0,1,2}` and `z=e_03`, production gives

`<L_B3,z>_(Q1*)=0`,

`<L_B3,z>_(Q2*)=-25/176`.

Thus even a proper simple subgraph pole has a Q-dependent polar complement when viewed in the full ten-edge regulator space.

## Maximal-chain sensitivity
For the canonical chain

`{0,1,2} subset {0,1,2,3} subset {0,1,2,3,4}`

and

`z=-e_04+e_34`,

production gives against `(L3,L4,L5)`:

under Q1*: `(0,0,0)`;

under Q2*: `(5/22,0,0)`.

Therefore the common orthogonal complement of the actual nested pole span changes with Q.

All 20 maximal chains were generated from the canonical chain by S5 and the witness was transported by the same permutation. The exact Q1/Q2 pattern was reproduced on **20/20** chains.

## Independent Gram crosscheck
For the canonical chain,

`G1=[[3,3,3],[3,6,6],[3,6,10]]`, `det(G1)=36`.

For Q2*,

`G2=[[465/176,195/88,15/8],[195/88,195/44,15/4],[15/8,15/4,25/4]]`,

`det(G2)=10125/484`.

Both pole spans are nondegenerate. The result is therefore not an artifact of linear dependence or a changed Gram normalization only; an explicit orthogonal-complement witness changes membership.

## Scientific meaning
Iter083H showed that the special deepest primitive K5 simple pole lies entirely in the trivial regulator sector and is Q-independent.

Iter083I shows that this simplification does **not** extend to the authoritative proper/nested forest pole arrangement. Generic positive S5-invariant Q choices change the polar complement geometry already on K3/K4 strata and on every maximal K3-K4-K5 chain.

This is **geometric scheme sensitivity** of the Q-based holomorphic projection class. It does not yet prove a nonzero difference between physical renormalized amplitudes: actual residues/numerator components may vanish in the Q-sensitive directions.

## Next exact target
The most productive next question is whether a stronger locality/factorization/naturality requirement on the family of regulator metrics forces the invariant metric to the Euclidean ray `Q proportional I`. If yes, the Q-sensitivity detected here is removed inside that stronger scheme class. Separately, source-faithful residue calculations are needed before claiming nonzero physical scheme dependence.

## Interpretation ceiling
No actual nonzero physical counterterm shift; no full K5 meromorphic continuation; no unique physical selector; no generic-spin theorem; no regulator independence; no all-strata global renormalization theorem; no G3/F9/G8/K5 promotion; no `NEW_PHYSICS_FOUND`; no complete-QG claim.