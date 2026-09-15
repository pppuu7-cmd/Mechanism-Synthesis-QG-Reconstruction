# Superseding adversarial review repair 1 — nested blow-up Jacobian defect

Date: 2026-09-15

Supersedes the verdict of `results/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_ADVERSARIAL_REVIEW.md` at commit `d22ee01756a59f7e31e9fe643d3679e02c4850f6`.
Repair preregistration: `prereg/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_CRITIC_REPAIR_1.md`, commit `148dd5130c448420419a807826fdfd84bb1228ef`.

Verdict: **REJECTED_SCIENTIFIC_PENDING_REPAIR**.

This is a rejection of the current B4/B6 proof/production, not a no-go theorem against the meromorphic bridge construction.

## Exact defect

The Researcher correctly decomposed the normal space along a maximal nested chain `K3 subset K4 subset K5` into orthogonal increments of real dimensions

`6 + 3 + 3 = 12`.

It then incorrectly identified the powers of the nested blow-up boundary defining functions as

`(6-1,3-1,3-1)=(5,2,2)`.

Those are the polar powers for three independent absolute radial variables on the orthogonal summands. They are not the Jacobian powers for the hierarchical boundary variables of the nested blow-up used in the Mellin argument.

At a maximal nested corner the scaling is

`u5 ~ rho5`,

`u4 ~ rho5 rho4`,

`u3 ~ rho5 rho4 rho3`,

with dimensions `dim u3=6`, `dim u4=3`, `dim u5=3`.

Hence the physical 12-dimensional normal density has hierarchical scaling

`rho5^11 rho4^8 rho3^5 d rho5 d rho4 d rho3`

up to a smooth nonzero angular factor. Ordered by the nested faces `(K3,K4,K5)`, the correct powers are

`(5,8,11)`.

## Why this is scientific rather than cosmetic

Frozen B4 requires the transformed Haar density/Jacobian to be derived explicitly. The production validator instead certified the wrong tuple `(5,2,2)`. Therefore B4 was not established by the reviewed production.

B6 used the same wrong hierarchical density powers in its resolved Mellin argument. Although a corrected continuation argument appears available, it requires a fresh derivation and production and cannot be retroactively substituted into the frozen PASS.

## Consistency check supporting repairability

For `j=1/2`, each internal wedge contributes radial order `-2`.

Along a maximal nested chain:

- the 3 K3-internal edges give cumulative `rho3^-6 rho4^-6 rho5^-6`;
- the 3 additional K4-internal edges give an additional `rho4^-6 rho5^-6`, so K4 total is `rho4^-12 rho5^-12`;
- the 4 additional K5-internal edges give `rho5^-8`, so K5 total is `rho5^-20`.

Combining with the corrected Haar powers yields

`rho3^(5-6)=rho3^-1`,

`rho4^(8-12)=rho4^-4`,

`rho5^(11-20)=rho5^-9`.

Thus the corrected blow-up geometry reproduces the authoritative superficial divergence degrees

`omega=(0,3,8)`

for K3/K4/K5. This strongly suggests repair rather than falsification of the whole meromorphic bridge.

## Regulator incidence forms required in the repair

If `lambda_B` is attached to each divergent block `B`, then on a face for a cluster `C`, `q_B` vanishes with that face precisely when `B subseteq C`. Therefore the boundary exponent shift is the incidence linear form

`L_C(lambda)=sum_(B subseteq C, |B|>=3) lambda_B`.

In particular, on a maximal `K3 subset K4 subset K5` chain:

- `L_K3=lambda_K3`;
- `L_K4=lambda_K4 + sum_(four K3 subsets of K4) lambda_K3`;
- `L_K5=lambda_K5 + sum_(five K4) lambda_K4 + sum_(ten K3) lambda_K3`.

The full 16-by-16 map `lambda -> L` is triangular by block size with unit diagonal and is therefore invertible. This is the natural coordinate system in regulator space for the corrected normal-crossing Mellin analysis.

At the origin the relevant pole-producing Taylor orders are exactly

- K3: order `0` from `rho3^(L_K3-1)`;
- K4: order `3` from `rho4^(L_K4-4)`;
- K5: order `8` from `rho5^(L_K5-9)`.

These match Iter083N's formal annihilator thresholds but are not yet promoted to actual source polar coefficients until repaired production succeeds.

## Current authority state

Until fresh repaired production is terminal and independently reviewed:

- `BRIDGE_AUTHORITY_CONFIRMED_SCOPED` is **not authoritative**;
- the positive construction remains a repair candidate;
- the earlier Iter083P-qualified blocker is reopened only narrowly at B4/B6;
- no physical finite part or selector is authorized.

## Required next action

Implement the prospectively frozen repair obligations of commit `148dd513...`, rerun the unchanged B1-B9 gate, then review the corrected result. No downstream polar-normal-jet gate is authorized before that sequence closes.