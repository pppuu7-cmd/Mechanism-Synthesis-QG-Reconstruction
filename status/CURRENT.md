# Current MSQGR research state

**Date:** 2026-09-12

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- First MSQGR-derived prospective selector: Causal Cylindrical Intertwining (CCI)
  - `P_b'^± iota_b'b = iota_b'b P_b^±`
  - common-space/linearized form: `P_± R - R P_± = 0`
- Physical F9 (`CAUSAL_ANALYTICITY_RG_INVARIANT`): `BLOCKED`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY` until physical F9/F10 evidence exists
- Active programme front: `ITERATION_038 / FULL_SMALL_SPIN_CAUSAL_CARRIER_S5_COVARIANCE`

## Closed structural results relevant to the current front

1. The repository has a source-backed Lorentzian EPRL/Toller computational carrier with explicit causal/co-causal branches and the exact additive control `T+ + T- = D`.
2. Generic ordinary-function collision power counting gives `q≈-2,-6,-12,-20` for k=2,3,4,5 causal collision clusters; EPRL controls remain regular. Causal-sector sums and tested j=1/2 boundary-intertwiner contractions do not remove the k=4,5 powers.
3. The published Appendix-D Feynman boundary primitive is reproduced. For j=1/2, `delta^(rho,1/2)=-i*c1*delta-(c2/2)*delta_prime`, and `Theta_+ + Theta_- = 1` is validated on smooth tests.
4. Iter026: the logarithmic k=3 leading term is nearly antipodally odd on tested generic angular sectors, but k=4 and k=5 have antipodal ratio 1.0 across all tested boundary/gamma/seed rows; simple principal-value parity cancellation is therefore not a generic k=4,5 mechanism.
5. Iter027: a Christensen positive absolute-value K5 spanning-tree proof cannot close for the Toller carrier. Exact graph geometry requires max edge exponent `M>=5/2`, while full 2x2 Toller operator norms give local power `p≈2`, hence single-edge weighted radial integrability only for `m<~3/2`. This is a no-go for that proof strategy, not a physical divergence theorem.
6. Iter028/029: naive products of wedge boundary singular terms are structurally obstructed in the tested linearized common-spectral geometry. K3,K4,K5 complete collision graphs have cycle/conormal left-nullities `1,3,6`; spanning-tree controls are transverse. All 16 K5 source causal sectors retain rank 4 / nullity 6. A source-backed correlated i-epsilon boundary value or a physically fixed distributional extension remains required.
7. Iter030–035 explored finite-part ambiguity on the six-dimensional K5 cycle sector. The key stable conclusion from Iter034/035 is that a uniform full S5 average isotropizes a generic cycle metric, but explicit microscopic symmetry breaking restores shape. Iter035 authoritative run `34692215902` completed 32/32 SUCCESS after an infrastructure-only JSON serialization fix.

## Iter036 — source causal orbit symmetry

Authoritative run `34694254523`, merge commit `3bdda03eb0087d20f6c4601b7d69320bbd94ec8f`: **34/34 SUCCESS**.

Exact source data `sigma_a=+-1` modulo global reversal split under S5 into causal orbits:

- `5+0`: orbit 1, stabilizer order 120;
- `4+1`: orbit 5, stabilizer order 24;
- `3+2`: orbit 10, stabilizer order 12.

All `16 x 120 = 1920` factorized wedge-sign covariance checks pass.

Exact stabilizer-invariant symmetric-tensor dimensions on the 6D K5 cycle space:

- `5+0`: dimension 1 -> 0 shape parameters after scale;
- `4+1`: dimension 2 -> 1 shape parameter;
- `3+2`: dimension 4 -> 3 shape parameters.

Nevertheless every stabilizer-invariant basis tensor becomes proportional to the unique S5 metric after a complete S5 orbit average. Thirty-two random-SPD profiles confirm this numerically over condition targets 3..10000. Arbitrary positive relative weights **between complete causal orbit types** remain isotropic; a bias **inside** a nontrivial orbit restores shape.

Classification: `SOURCE_CAUSAL_ORBIT_SYMMETRY_CAN_REMOVE_CYCLE_METRIC_SHAPE_IF_FULL_S5_COVARIANCE_IS_PHYSICAL`.

## Iter037 — oriented-simplex symmetry and Toller reversal

Authoritative run `34694558711`, merge commit `bcbae58c751b436819480792d0ab35acf84c51bc`: **7/7 SUCCESS**.

Exact oriented subgroup result:

- `dim Sym^2(Cycle_K5)^A5 = 2`;
- therefore one determinant-normalized cycle shape parameter survives orientation-preserving A5 symmetry;
- `dim Sym^2(Cycle_K5)^S5 = 1`;
- adding one odd permutation to A5 reduces the invariant dimension from 2 to 1;
- after A5 causal-orbit averaging, every causal type still has a two-dimensional invariant metric image, hence one residual shape parameter.

Thus odd-permutation/orientation-reversal covariance is physically decisive for the symmetry-based finite-part ambiguity removal.

Actual j=1/2 gamma-simple Toller blocks on generic separated Lorentz elements satisfy to ~1e-15 across gamma 0.2,1.2,2.0 and two independent seeds:

`T_s(g^{-1}) = eps T_s(g)^T eps^{-1}`,

with the numerically equivalent convention form

`T_s(g^{-1}) = T_{-s}(g)^dagger`.

The EPRL control obeys `D(g^{-1})=D(g)^dagger` to the same precision. Candidate reversal laws were selected on five training edges and frozen before five holdout edges.

## Current decisive target — Iter038

`FULL_BOUNDARY_CONTRACTED_ODD_PERMUTATION_COVARIANCE_NOT_YET_ESTABLISHED`

Iter038 propagates the established edge reversal law through the complete j=1/2 K5 boundary tensor network. For each S5 relabeling it:

1. relabels Lorentz groups and source causal signs;
2. regauges to new `g_0=1`;
3. recomputes all ten actual Toller edge matrices;
4. applies epsilon duality to both endpoint half-edge indices whenever the canonical edge orientation reverses;
5. transports/reorders all five four-valent intertwiner tensors;
6. contracts the full K5 network;
7. compares with the original causal and EPRL amplitudes.

Matrix: gamma `0.2,1.2,2.0` x two seeds, each with six even and six odd permutations, three causal representatives and four boundary states.

If Iter038 passes, the full *regular pointwise small-spin carrier* supports the S5 symmetry required by Iter036 despite oriented-edge conventions. The next hard gate is then covariance/uniqueness of the **singular correlated Feynman/distributional extension** itself.

## Claim locks

- no `NEW_PHYSICS_FOUND`;
- no claim that the causal EPRL vertex is nonperturbatively divergent or finite;
- no universal no-go theorem for causal EPRL;
- no physical F9 promotion from surrogate/symmetry evidence alone;
- no G8 novelty promotion before physical F9/F10 evidence;
- Iter036/037 are exact or numerical finite-K5 carrier/symmetry results, not a theorem fixing the full multiwedge distributional extension;
- a PASS of Iter038 will still not establish the integrated vertex or all-spin/coherent-state covariance.
