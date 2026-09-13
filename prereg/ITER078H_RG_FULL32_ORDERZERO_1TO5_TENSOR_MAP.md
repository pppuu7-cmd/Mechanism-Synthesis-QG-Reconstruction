# Iter078H-RG preregistration — exact full-32 order-zero ambiguity map under the versioned 1-to-5 measure

**Date:** 2026-09-14

## Scope

This is a finite-spin **control truncation** of the experimental `CRQN v0.3-R0` measure skeleton from Iter078F. It is not the full causal-Toller RG map.

Its purpose is to answer a high-information structural question without selecting a Toller finite part: if the local order-zero extension ambiguity is an arbitrary 32-component boundary tensor as proved by Iter078G, what does one exact 1-to-5 contraction do to that full tensor space when all internal and external face spins are frozen to `j=1/2`?

## Frozen 1-to-5 tensor network

Fine vertices are `v_a`, `a=0,...,4`. Each has:

- one external tetrahedron carrying boundary intertwiner `e_a in {0,1}`;
- four internal tetrahedra shared with `v_b`, carrying `k_ab=k_ba in {0,1}`.

At every fine vertex use the same universal local tensor

`C[k0,k1,k2,k3,k4]`, `k_i in {0,1}`,

with exact 32 components. Local slot convention:

- slot 0 = the external tetrahedron (opposite the inserted central primal vertex);
- slots 1..4 = the four internal tetrahedra, ordered by ascending neighboring fine-vertex label `b != a`.

This is a frozen labelled-simplex convention; no recoupling/basis convention may be changed after seeing the result.

## Frozen internal measure

Use the Iter078F EPRL convolution weights in the fixed-spin control:

- all ten internal face spins are `j=1/2`, giving common face factor `2^10`;
- each internal tetrahedron intertwiner `k_ab` has edge weight `d_k=2k_ab+1`, i.e. `1` for `k=0`, `3` for `k=1`.

Define the exact degree-5 polynomial map `R_EPRL: C^32 -> C^32` by

`R_EPRL(C)[e_0,...,e_4] = 2^10 * sum_{k_ab in {0,1}} prod_(a<b)(2k_ab+1) * prod_(a=0)^4 C[ e_a, k_a,b1, k_a,b2, k_a,b3, k_a,b4 ]`,

where `b1<...<b4` are the neighbors of `a`.

Boundary normalization factors common to coarse/fine matching are not included; they cannot change rank or proportionality tests in this gate.

## Frozen BF/compact control tensor

Let `L in Z^32` be the exact stripped compact K5 tensor from Iter077N:

`L[k_0,...,k_4] = compact_eval(k_0,...,k_4)`

with all edge matrices equal to the identity. Iter077N already established `16/32` nonzero entries.

## Lanes

### Lane A — map/source lock

Verify:

- 32 local tensor components;
- 32 output components;
- exactly `2^10=1024` internal intertwiner assignments per output;
- internal EPRL edge weights `1,3` and common face factor `2^10`;
- frozen compact tensor has the same exact checksum/nonzero count as Iter077N.

### Lane B — exact BF-vector image

Compute `R_EPRL(L)` exactly.

Test whether there exists a single exact rational `K` such that

`R_EPRL(L)=K L`.

- If yes, record `K` exactly and the corresponding one-ray fixed-point scaling equation `t = K t^5` after common boundary normalization is frozen.
- If no, record an exact pair of components witnessing non-proportionality.

No prediction of proportionality is frozen; either outcome is scientific information.

### Lane C — exact Jacobian rank at L

For the degree-5 map compute the exact integer Jacobian

`J_{alpha beta} = partial R_alpha / partial C_beta |_(C=L)`.

Compute exact rank over `Q` and nullity. If rank<32, emit an exact right-nullspace witness. If rank=32, emit a nonzero determinant or exact full-rank certificate.

Interpretation: this is only local sensitivity of the finite-spin pure-ambiguity control map near `L`.

### Lane D — measure sensitivity control

Repeat Lane B and Jacobian rank with **unit internal edge weights** `d_k=1`, keeping every other tensor-network datum fixed.

This is an intentionally non-EPRL negative/control measure. Its purpose is to test whether closure/rank conclusions depend materially on the newly proposed internal measure, as required by the Iter078C/D adversarial qualification.

## Aggregate outcomes

The gate always records the exact map diagnostics; it does not force a predetermined PASS/FAIL based on BF proportionality.

Classification family:

- if EPRL-weighted `L` is an eigen-ray:
  `ITER078H_RG_FULL32_FIXED_JHALF_ORDERZERO_MAP_BF_TENSOR_EIGENRAY_EXACT_CONTROL_SCOPED`;
- if not:
  `ITER078H_RG_FULL32_FIXED_JHALF_ORDERZERO_MAP_BF_TENSOR_NOT_CLOSED_EXACT_CONTROL_SCOPED`.

Append Jacobian rank/nullity and measure-sensitivity data to the result.

`INVALID_IMPLEMENTATION` if any frozen count/checksum/source lock fails.

## Interpretation ceiling

This gate freezes all internal spins to `j=1/2`, omits the Lorentzian source vertex `A_ref`, and studies only the order-zero ambiguity tensor network. It cannot establish a CRQN fixed point, full theory-space closure, generic-spin behavior, convergence of spin sums, regulator independence, G3 or continuum physics.

Its value is diagnostic: it tests whether even the simplest exact 32-dimensional ambiguity sector behaves as a closed/effective RG direction under the newly versioned measure.