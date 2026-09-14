# Iter081R-SM provenance ledger

Date: 2026-09-14

## Scientific purpose
Repair the K5 extension-ambiguity classification after historical Iter077Q was re-reviewed as `INVALID_SOURCE_LOCK` for omitting exact node-wise compact gauge symmetry.

## Prospective chain
- controlling source-lock review: `c0ae0ef208a3eccef4ece7960cdf5337e7d5fa2e`;
- preregistration: `18945b681978cf22a8253a6489034e68a1cae372`;
- implementation: `62c8ee3ac378ddc96df8263cb56c38ae76988517`;
- production workflow/head: `22f87a8cb1e5a87285066ac658e7823b223a3bc9`.

Preregistration is an ancestor of production and is distinct from production head.

## Authoritative execution
- Actions run: `34882711232`, terminal `completed/success`;
- job: `104105657918`, `exact-invariant-jet-count`, terminal `success`;
- artifact: `10363029817`, `iter081r-sm-invariant-jets`;
- artifact ZIP digest: `sha256:260017c1b2ac7186f8f2d5e10a499f40293315fec3d26ad174f3ba67726bf8a8`;
- downloaded artifact JSON SHA256: `ede1d88e1cabf8ca7c545aa88172ddd425e31a9e6ccd8376e45f382d9c4ab939`;
- durable normalized raw copy commit: `48674739d726f96aad68466cf230b5f1fe061f96`;
- durable result commit: `5fe42e766aab2660b36c654502a029930db28890`.

## Authoritative output
Classification:
`ITER081R_SM_RIGHT_SU2_S5_INVARIANT_NORMAL_JET_SPACE_NONTRIVIAL_EXACT_SCOPED`.

Production verdict label: `PASS_EXACT_SCOPED`.

Exact invariant dimensions by normal derivative degree 0..8:
`[1,0,1,0,3,0,7,0,16]`.

Total demonstrated scalar invariant jet dimension through order 8: `28`.

All preregistered controls passed, including exact S5 class-size sum, integer/nonnegative final dimensions, quadratic invariant, even-order Laplacian-family lower bounds, and active S5 projection negative control.

## Scope lock
The number 28 is the dimension of a demonstrated scalar `SO(3) x S5` invariant normal-symbol/jet subspace in the frozen minimal-sector collision problem. It is a lower bound on the complete source-compatible extension ambiguity, not an exact total-dimension theorem. Historical Iter077Q infinite tangential `W` is non-authoritative after the right-SU2 source-lock correction.
