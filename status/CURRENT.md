# Current MSQGR research state

**Date:** 2026-09-12

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- First MSQGR-derived prospective selector: Causal Cylindrical Intertwining (CCI)
- Physical F9 (`CAUSAL_ANALYTICITY_RG_INVARIANT`): `BLOCKED`
- G3 quantum dynamics: `OPEN`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`
- Active programme front: `ITERATION_043 / SOURCE_FAITHFUL_FINITE_EPSILON_AND_CYCLIC_EXTENSION`

## Closed results controlling the current front

1. A source-backed Lorentzian EPRL/Toller carrier exists with explicit causal/co-causal branches and exact `T+ + T- = D` control. Native Toller kernels, direct ten-wedge topology and real Lorentzian backend have been independently validated.
2. Ordinary-function collision power counting gives approximately `q=-2,-6,-12,-20` for k=2,3,4,5 causal clusters. Tested causal-sector sums and full j=1/2 boundary-intertwiner contractions do not remove the k=4,5 powers. This is not a physical divergence theorem.
3. Appendix-D Feynman boundary primitives are reproduced. For j=1/2, `delta^(rho,1/2)=-i*c1*delta-(c2/2)*delta_prime`; the general-j derivative order terminates at `2j`; `Theta_+ + Theta_- = 1` holds on smooth tests.
4. Iter026: simple antipodal/PV cancellation is not generic for the dangerous high-collision strata.
5. Iter027: the Christensen positive absolute K5 spanning-tree proof cannot close for the Toller beta^-2 carrier. This is a no-go for that proof strategy only.
6. Iter028/029: naive complete-graph products of wedge boundary distributions fail the standard transversality/Hormander criterion; K5 cycle/conormal nullity is 6. A correlated/source-backed Feynman extension is required.
7. Iter034-038: the tested regular pointwise j=1/2 boundary-contracted carrier is genuinely S5 covariant, including odd permutations/orientation reversal.
8. Iter039 run `34695173734`: S5 symmetry alone does not fix local jets. S5 invariant dimensions d=0..16 are `[1,0,1,0,4,0,9,2,20,9,38,23,74,51,125,101,211]`; first ambiguity beyond the unique quadratic invariant is d=4.
9. Iter040 run `34695321410`: quotienting by quadratic descendants leaves primitive dimensions `[0,0,3,0,5,2,11,7,18,14,36,28,51,50,86]` for d=2..16. Therefore quadratic isotropization does not generate the invariant ring.
10. Iter041 run `34695499357`, 24/24 SUCCESS: actual j=1/2 Appendix-D source sectors reach higher extension budgets. For complete K5, `omega=6..16`; even the all-delta sector has omega=6. Higher-order ambiguity is therefore source-relevant at superficial scaling level.
11. Iter042A run `34695777621`, 14/14 SUCCESS: the simple edge-local j=1/2 source derivative budget strongly reduces the primitive space: d4 `3/3`, d6 `3/5`, d7 `0/2`, d8 `1/11`, d9 `0/7`, d10 `0/18`. Source support does not select the surviving coefficients.
12. Iter042B run `34695777605`, 3/3 SUCCESS: Molien/Hilbert coefficients reproduce Iter039/040; the truncated plethystic fingerprint has generator-like positive coefficients at d2,d4,d6,d7,d8,d9,d10,d11 and first relation-like negative coefficient at d12. This is representation-theory compression only.

## Active Iter043 — source-faithful finite-epsilon/contact diagnostics

Merge commit `150836e4c9d51794d3139ced15ef49c2235039d6`, PR #43. Three independent workflows are active:

- **Iter043A**, run `34696402859`, 12 lanes: derive and validate the exact finite-spectral-i-epsilon j=1/2 one-wedge distribution identity. Preregistered discriminator: the delta-prime coefficient `-sigma*c2/2` remains exactly epsilon-independent after the exact spectral transform. A PASS would show that finite epsilon on each wedge separately does not erase the contact layer, while leaving joint multi-wedge spectral integration open.
- **Iter043B**, run `34696402864`, 4 lanes: resolve the d=4/d=6 source-compatible primitive span into unlabeled S5 edge-subgraph orbit bases for future Feynman coefficient selection.
- **Iter043C**, run `34696402856`, 1 lane: quantify regulator-path dependence of the simplest cyclic all-delta K3 product under independent Gaussian mollification, with a transverse tree control. This tests naive regulator dependence, not the physical correlated Feynman prescription.

## Next allowed gate

If Iter043 confirms persistent one-wedge contact structure and naive cyclic regulator dependence, proceed to the **joint K3 multi-wedge spectral/Feynman boundary-value problem**, performing the correlated spectral/test-function integration before taking the epsilon limit or multiplying boundary-supported distributions. Only after K3 regulator/order consistency is controlled should the programme advance to K4/K5 forests and ultimately a physical CCI/F9 test.

## Claim locks

- no `NEW_PHYSICS_FOUND`;
- no claim that the causal EPRL vertex is nonperturbatively divergent or finite;
- no universal no-go theorem for causal EPRL;
- no physical F9 promotion from symmetry/source-support/distributional surrogates;
- no G8 novelty promotion before physical F9/F10 evidence;
- no arbitrary counterterm/finite part may be promoted to physical evidence;
- fixed causal-sector conclusions may not borrow `T+ + T- = D` cancellation without proof.
