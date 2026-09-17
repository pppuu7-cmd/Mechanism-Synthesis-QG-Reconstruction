# K5 full-source boundary S5 transport object definition — terminal Researcher result

Date: 2026-09-17

Classification: **`K5_FULL_SOURCE_BOUNDARY_S5_CONTRAGREDIENT_TRIVIAL_CHARACTER_EXACT_SCOPED`**.

Researcher status: **`PASS_EXACT_SCOPED`**. Independent Critic review is required before this result is consumed as confirmed authority by the parent exact-cancellation resolver.

## Prospective authority

Scientific preregistration: `prereg/K5_FULL_SOURCE_BOUNDARY_S5_TRANSPORT_OBJECT_DEFINITION.md`, commit `6ac6e7749783b78fb0966450a91d8042c1ad0ca4`.

Parent exact-cancellation gate: prereg commit `d6b0e805101c8590eafac71398cc2b1466691752`.

Implementation commits:

- shard evaluator `c0869be5c5de1c903a679a9d9df2287b36b6daa8`;
- aggregate classifier `68621727648c59ac4ad4ed991fcfe2ec53895288`;
- workflow/head `12e30757258ef95fca6e3e72838e231644e6a7d5`.

Production run `35194864447` is terminal success. All six exact shards and the aggregate job are terminal success. Aggregate job `105115788058`; aggregate artifact `10485701611`; ZIP digest `sha256:b08b3b72ca257a35927ce727b3808d0d73db99eb2d8b96dd0f39592cbd3c320d`; aggregate result JSON SHA256 `28cd3d43c7872a842f36d2cb4e6969923ed045c3d47e79d15d703424509dae6a`.

Durable machine aggregate: `results/raw/k5_full_source_boundary_s5_transport_authoritative.json`.

## Exact object tested

The gate retained the source ordering

`one-wedge spectral/spinor integration -> Toller function -> product of ten Toller matrices -> full boundary contraction -> K5 group/distributional object`.

At order zero it evaluated the complete unprojected boundary Wick covector in all 32 all-`j=1/2` boundary components, with exactly `100000` original source node-choice terms per complete vector and exact rational/Gaussian-rational arithmetic.

A vertex permutation was applied simultaneously to Schwinger edge variables and to source wedge endpoint/orientation data. On a canonically reversed target edge the source endpoint entry was transposed `(row,col)->(col,row)` before contraction, with the exact source sign from `M(-v)=-M(v)` tracked mechanically. The boundary amplitude was then compared as a covector against the exact independently reconstructed 32-dimensional boundary action.

Two independently organized target constructions were required before any representation verdict:

1. edge-local transformed source-entry metrics;
2. transported source-entry patterns followed by Wick reconstruction.

They agreed componentwise in every frozen lane.

## Frozen lanes

Two generic positive Schwinger witnesses were frozen before output:

- `W1=(2,3,5,7,11,13,17,19,23,29)`;
- `W2=(31,37,41,43,47,53,59,61,67,71)`.

Each was tested under:

- even five-cycle `C=(1,2,3,4,0)`;
- inverse cycle `Cinv=(4,0,1,2,3)`;
- odd transposition `T=(1,0,2,3,4)`.

The cycle and inverse each reverse four canonical K5 edges and have permutation sign `+1`. The transposition reverses one canonical edge and has permutation sign `-1`.

## Exact result

All frozen implementation and malformed controls passed:

- complete 32-component / 100000-source-term coverage;
- exact boundary action inverses and `T^2=I`;
- Reynolds rank two and pivots `[1,4]`;
- exact bilateral cycle invariance of the Reynolds projector;
- exact source matrix reversal `M(-v)=-M(v)`;
- exact orientation-reversal parity count;
- exact source-pattern round trips;
- exact equality of the two independent target constructions;
- exact authoritative versus weighted coordinate extraction;
- source-fixed repair-5 mismatch retained rather than overwritten;
- omission of row/column transpose rejected on the frozen odd-transposition negative control.

For the even cycle lanes both prospectively frozen characters coincide and both therefore pass. The odd transposition resolves the ambiguity:

- `W1_T`: trivial character exact = true; orientation/sign character exact = false;
- `W2_T`: trivial character exact = true; orientation/sign character exact = false.

Hence over every frozen lane the full-source target satisfies

`a_p(p alpha) = A_p^(-T) a(alpha)`

with **no additional `sgn(p)` character** once the physical orientation-sensitive source-entry transport and its reversal signs are included explicitly.

The two invariant-dual pivot coordinates are unchanged between base and transported target at both frozen witnesses, as a downstream control; the full 32-vector equality, not the projected coordinates, decides the classification.

## New scientific fact

The earlier terminal `BOUNDARY_S5_REPRESENTATION_UNRESOLVED_EXACT` result is now localized: it arose for the deliberately source-fixed alpha-permuted diagnostic object. When the source wedge endpoint/orientation data are transported simultaneously, the complete 32-component source object is exactly compatible on the frozen generators/witnesses with the ordinary contragredient boundary law and **does not carry an extra orientation sign character**.

Thus there is no obstruction at this gate requiring a fitted phase or a nontrivial constant two-channel mixing matrix. The latter remains forbidden by the independent source-vector authority `A_cycle W=W I_2`.

## Scope and interpretation ceiling

This is an exact scoped object-definition result on the prospectively frozen generic witnesses and generators. It is not by itself a symbolic all-alpha theorem, and it is not yet independent Critic authority. The odd transposition distinguishes the only two prospectively allowed source characters, but no claim is made about arbitrary post-hoc characters or mechanisms.

No physical Schwinger-corner exponent, local finiteness/divergence classification, global projective Stokes/IBP theorem, invariant-dual K5 period value, full 217-dimensional tensor theorem, reduction of `dim_C F_8=377`, physical finite-part selector, regulator-independence theorem, F9/G3/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete-QG claim follows. Published one-wedge spectral `i epsilon` remains retained.

The next admissible step is an independent adversarial Critic review of this exact source/boundary transport result. Only if confirmed may the parent exact-leading-coefficient cancellation resolver consume the repaired full-source transport law.
