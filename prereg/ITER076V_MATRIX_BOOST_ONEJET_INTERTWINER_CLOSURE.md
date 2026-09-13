# Iter076V preregistration — matrix relative boost one-jet and SU(2)-intertwiner closure

Date: 2026-09-13

## Purpose

Iter076U established that the minimally power-stripped **diagonal reduced** gamma-simple Toller branch has normalized one-jet `i gamma m` on both causal branches. This gate asks the stronger and more source-relevant matrix question: after retaining the magnetic dependence of the leading singular matrix, is the relative first coefficient simply `i gamma J_n`, and is a common source-node boost therefore annihilated by the exact SU(2) boundary-intertwiner closure relation?

The gate is restricted to boost-normal approaches to the singular SU(2) locus. Compact/rotation tangential derivatives at `beta=0` remain outside scope.

## Frozen source input

Use `sources/GAMMA_SIMPLE_TOLLER_MATRIX_ONEJET_INTERTWINER_SUPPLEMENT.md`, committed before implementation, together with the closed Iter076U formulas and the source Eq. (4)/(7) conventions.

For `j>0`, write

`t_m^(s)(beta)=beta^(-(2j+1))[C_m^(s)+beta D_m^(s)+o(beta)]`.

## Frozen lanes

### Lane A — source/provenance locks

PASS iff the committed supplement records:

- the source boundary state as five SU(2) intertwiners;
- Eq. (4) wedge matrix `T_{m_ba,m_ab}(g_b^-1 g_a)`;
- Eq. (7) compact covariance;
- the explicit restriction to boost-normal approaches;
- the firewall that compact/rotation tangential one-jets, nonlinear source-to-K4 curvature, and `epsilon^-1` are not established.

### Lane B — leading magnetic matrix and branch relation

Using the exact Eq. (9) leading coefficient, verify:

- `C_m^(-)=-C_m^(+)`;
- for either branch and every unit magnetic step,
  `C_m/C_(m-1)=-(j-m+1)/(j+m)`;
- the relative Iter076U coefficient gives
  `D_m/C_m=i gamma m` on both branches;
- hence, with `C=diag(C_m)`, `D=diag(D_m)` and `J_z=diag(m)`, both left and right relative operators obey
  `C^(-1)D = D C^(-1) = i gamma J_z`.

The gate may use the common rational recurrence shape with an arbitrary nonzero seed, because overall branch-dependent leading scale cancels from the relative operator.

### Lane C — compact covariance to arbitrary boost axis

Using source Eq. (7), freeze the algebraic conjugation rule for a pure boost along `n`:

`C_n=U C_z U^(-1)`, `D_n=U D_z U^(-1)`.

PASS iff the exact matrix identity reduces to

`C_n^(-1)D_n = D_n C_n^(-1) = i gamma J_n`,

where `J_n=U J_z U^(-1)`.

Exact finite-dimensional controls are required for spins `j=1/2,1,3/2,2` using at least the z axis and an opposite-axis control. The opposite direction must give `-i gamma J_z` rather than the same sign.

No compact tangential derivative is inferred.

### Lane D — node-5 common boost and intertwiner closure

Use source node `5`, whose four incident ordered wedges are `(a,5)`, `a=1..4`. At the coincident control set all neighboring `g_a=1` and perturb

`g_5(beta)=exp(beta K_n)`.

Then all four relative group elements are `exp(-beta K_n)`, so after leading-matrix extraction the first correction on the node-5 magnetic slots is

`-i gamma sum_{a=1}^4 J_n^(5a)`.

Construct exact 4-valent SU(2) invariant tensors by Clebsch-Gordan coupling for the frozen spin controls

- `(1/2,1/2,1/2,1/2)`,
- `(1/2,1,1/2,1)`,
- `(1,1,1,1)`.

Enumerate every allowed common intermediate spin `k`. PASS iff for every nonzero intertwiner control:

- total `J_z` annihilates it exactly;
- total raising and lowering operators annihilate it exactly, hence total `J_x,J_y` also vanish;
- the node-common boost relative one-jet vanishes for arbitrary direction `n`;
- componentwise magnetic support satisfies `m1+m2+m3+m4=0` wherever the intertwiner coefficient is nonzero.

The aggregate must record:

- `node_common_boost_onejet_killed_by_intertwiner=true`;
- `causal_branch_independent=true`;
- `compact_tangential_onejet_established=false`;
- `full_source_onejet_established=false`;
- `physical_source_to_K4_curvature_selected=false`;
- `epsilon_minus1_coefficient_established=false`;
- no generic finite-spin signed P3 or G3/F9/G8/K5 promotion.

## PASS classification

`ITER076V_RELATIVE_TOLLER_BOOST_ONEJET_IS_I_GAMMA_J_AND_SU2_INTERTWINER_KILLS_NODE_COMMON_BOOST_EXACT_SCOPED`

## Scientific meaning on PASS

A PASS establishes a genuine source-level cancellation mechanism for the **boost-normal, node-common** part of the factorized one-jet: the magnetic dependence found in Iter076U reorganizes into the standard SU(2) generator and is annihilated by boundary-intertwiner closure.

This is stronger than componentwise `m=0` and applies to arbitrary spins/intertwiners within the source SU(2) invariant boundary space, but it is not yet the full source one-jet because tangential compact directions and global compatibility of the leading singular factorization remain open.

## Next admissible gate

Audit the tangent decomposition at the singular SU(2) locus: determine whether compact/rotation tangential variations of the extracted leading matrix are pure SU(2) gauge/intertwiner directions and therefore also annihilated, or whether they generate independent regular one-jet data. Only after that can the full source one-jet be classified as zero or nonzero.

## FAIL classification

`ITER076V_MATRIX_BOOST_ONEJET_INTERTWINER_CLOSURE_CONFIRMATION_FAIL`

A failure is an algebra/source-compatibility result, not a physical finiteness/divergence theorem.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no full source one-jet; no physical nonlinear source-to-K4 map; no nominal `epsilon^-1` coefficient; no physical causal-vertex finiteness/divergence theorem; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; retain the source spectral `i epsilon` prescription.