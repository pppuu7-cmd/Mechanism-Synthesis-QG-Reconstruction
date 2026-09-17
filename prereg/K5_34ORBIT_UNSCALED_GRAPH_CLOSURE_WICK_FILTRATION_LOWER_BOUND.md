# K5 34-orbit unscaled-graph closure Wick-filtration lower bound

Status: **PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION OR OUTPUT**.
Date: 2026-09-17

## Role and motivation

This is an outcome-blind preparation gate for the already-frozen `K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION` (`d6b0e805101c8590eafac71398cc2b1466691752`). It is motivated by the terminal mask-511 theorem `K5_MASK511_UNSCALED_EDGE_FORCES_Q18_ZERO_EXACT_SCOPED`, but it must be reconstructed for every proper K5 subset orbit and must not assume that the mask-511 order extrapolates.

The goal is to prove a channel-independent exact **lower bound** on the physical numerator filtration before any cancellation between retained source coefficients. A valid bound can shrink the coefficient window needed by the 64-component resolver. It is not itself a cancellation resolver and cannot certify an exact first nonzero order unless combined with a separate nonzero witness/authority.

This gate consumes no partial values from direct q18 run `35259123078` and no pending Boundary-S5 Critic verdict.

## Frozen source/object authority

Use unchanged:

- canonical ten-edge K5 ordering from the corrected Iter077I all-`j=1/2` source authority;
- exact Kirchhoff polynomial `Psi_K5` with 125 coefficient-one spanning-tree monomials;
- canonical degree-27 physical numerator construction with all 32 boundary components / 100000 original source terms and the frozen 945 retained perfect matchings;
- exact rational arithmetic;
- the same 32 proper S5 subset-orbit representatives used by the terminal 34-orbit parent audit;
- the frozen corner scaling `alpha_e(t)=t W_e` on the subset `Z` and unscaled `alpha_e=W_e` on `U=E\Z` only as a filtration definition. No numerical weight evaluation is needed for the theorem.

Do **not** consume coefficient-level Boundary-S5 transport, physical channel cancellation results, q18 shard values, or any result of the future 64-component production.

## Frozen graph-theoretic definitions

For each proper scaled-edge subset `Z subset E(K5)`, let `U=E\Z` be the unscaled-edge subgraph on all five vertices.

Let:

- `c(U)` be the number of connected components of the unscaled subgraph;
- `d_Z = c(U)-1`, equivalently the exact minimum mask-filtration order of `Psi_K5` (to be independently checked against the 125-tree polynomial);
- `a_Z = max(d_Z-1,0)`;
- `H_Z = cl(U)` be the graphic-matroid closure of `U`, i.e. every K5 edge whose two endpoints lie in the same connected component of `U`;
- for a retained perfect matching `M` of the ten source edge slots,
  `m_Z(M) = # {pairs {e,f} in M : e in H_Z or f in H_Z}`;
- `mu_Z = min_M m_Z(M)` over the frozen 945 retained perfect matchings.

For `d_Z=0` this gate claims no closure-kernel boost; only the trivial degree lower bound is allowed.

## Frozen theorem to test

For every proper orbit representative with `d_Z >= 1`, prove exactly:

1. Writing the reduced Laplacian as `L(t)=L_0+t L_1`, the row/column span of `L_0` is the incidence span of the connected components of `U`.
2. The leading adjugate grade is at least `a_Z=d_Z-1`, and its grade-`a_Z` part `A_a` obeys
   `A_a L_0 = 0` and `L_0 A_a = 0`.
3. Hence for every edge `e in H_Z`, its reduced incidence row `r_e` lies in the incidence span of `U`, so
   `r_e A_a = 0` and `A_a r_e^T = 0`.
4. For the exact cleared covariance hierarchy
   `BN_n = (-adj(L) Q)^n adj(L)`, every covariance numerator has the generic lower bound
   `ord_t C_{ef,n} >= (n+1) a_Z`,
   and if `e in H_Z` or `f in H_Z`, then
   `ord_t C_{ef,n} >= (n+1) a_Z + 1`.
5. For determinant factors
   `F_j = Psi^j [s^j](det(L+sQ)/Psi)^(-3/2)`, prove
   `ord_t F_j >= j a_Z` for `j=0,...,4`.
   It is sufficient to use `ord_t D_r >= max(d_Z-r,0)` for `D_r=[s^r]det(L+sQ)` and the exact frozen expansion of `F_j`.
6. For every retained perfect matching and every source-series partition entering the degree-27 numerator, the five covariance factors use all ten source edge slots exactly once. Therefore every matching contribution obeys
   `ord_t contribution >= 9 a_Z + m_Z(M)`.
7. Consequently, before any cancellation between retained matching/source coefficients and independently of the two physical invariant-dual channels,
   `N_c in F^(LB_Z)` for both channels, where
   `LB_Z = 9 a_Z + mu_Z` for `d_Z>=1`.

For `d_Z=0`, record only `LB_Z=0` unless a separate exact argument is prospectively frozen.

## Required exact controls

- reconstruct exactly 34 K5 subset orbits and the same 32 proper representatives as the parent audit;
- verify all orbit sizes sum to 1024 and proper-orbit sizes sum to 1022;
- reconstruct `d_Z` both from unscaled graph components and independently from the exact 125-tree polynomial; they must agree on all 32 proper representatives;
- reconstruct the exact frozen 945 retained perfect matching set from the source/DAG authority and verify every matching covers edge slots `0,...,9` exactly once;
- independently verify `H_Z` by graph components and by rational row-span membership of reduced incidence rows;
- for each `d_Z>=1` orbit, verify exact leading-adjugate annihilation of the `H_Z` incidence rows;
- verify the covariance lower-bound statement for all edge pairs and source orders `n=0,...,4` by exact sparse-polynomial filtration, without evaluating physical channel coefficients;
- verify the determinant-factor lower bound for `j=0,...,4` by exact sparse-polynomial filtration;
- verify `mu_Z` both by direct enumeration of all 945 retained matchings and by an independent combinatorial lower-bound/reconstruction route where possible;
- mask `511` must reproduce the already-authoritative lower bound `LB_511=19` but this is a positive control only, not the proof of the all-orbit theorem.

## Negative/malformed controls

At minimum reject separately:

1. treating an edge connecting different components of `U` as if it belonged to `H_Z`;
2. deleting the `+1` covariance boost for an `H_Z` endpoint;
3. replacing the retained 945 matching set by an incomplete subset while claiming the same `mu_Z` authority;
4. using `ceil(|U|/2)` as equality for `mu_Z` without checking closure edges and the actual retained matching set;
5. importing any physical numerator coefficient or Boundary-S5 transport result as proof of the structural lower bound.

An implementation that cannot detect these malformed cases is invalid.

## Frozen classifications

- `K5_34ORBIT_UNSCALED_GRAPH_CLOSURE_WICK_FILTRATION_LOWER_BOUND_EXACT_SCOPED` only if all 32 proper orbits are reconstructed, every required exact control passes, and the stated `LB_Z` bound is proved for both physical channels without using their coefficients.
- `K5_34ORBIT_UNSCALED_GRAPH_CLOSURE_BOUND_REFUTED_EXACT_SCOPED` if an exact counterexample to any theorem step is produced for a proper orbit with a machine-readable mask/edge/pair/order witness.
- `BLOCKED_OBJECT_DEFINITION` if a required frozen source/matching/corner object is unavailable; name the exact missing primitive.
- `INVALID_IMPLEMENTATION` for incomplete orbit/matching coverage, arithmetic/provenance defects, failed malformed controls, or any use of forbidden downstream/partial scientific values.

## Interpretation ceiling

A PASS establishes only exact channel-independent **lower bounds** for physical numerator mask filtrations on the 32 frozen proper K5 subset-orbit representatives. It does not establish exact `r_N` where no separate nonzero witness exists; it says nothing by itself about exact `r_B`, projective-normal order, flux cancellation, local integrability, global Stokes/IBP, K5 periods, physical finite-part selection, `dim_C F_8=377` reduction, regulator independence, F9/G3/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete quantum gravity.

## Activation / concurrency rule

This preregistration is preparation only while the independent Boundary-S5 Critic scientific reconstruction and direct q18 construction are non-terminal. Do not launch a competing authoritative production merely because this contract exists. It may be executed as a cheap structural preflight when doing so does not duplicate the active Researcher gate, or consumed to optimize the already-frozen 64-component resolver only after the dependency DAG authorizes that resolver.
