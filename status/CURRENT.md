# Current MSQGR research state

**Date:** 2026-09-12

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- First MSQGR-derived prospective selector: Causal Cylindrical Intertwining (CCI)
  - `P_b'^± iota_b'b = iota_b'b P_b^±`
  - common-space/linearized form: `P_± R - R P_± = 0`
- Physical F9 (`CAUSAL_ANALYTICITY_RG_INVARIANT`): `BLOCKED`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY` until physical F9/F10 evidence exists
- Active programme front: `ITERATION_039 / S5_INVARIANT_DISTRIBUTIONAL_EXTENSION_JETS`

## Closed structural results relevant to the current front

1. The repository has a source-backed Lorentzian EPRL/Toller computational carrier with explicit causal/co-causal branches and exact additive control `T+ + T- = D`.
2. Generic ordinary-function collision power counting gives `q≈-2,-6,-12,-20` for k=2,3,4,5 causal collision clusters; EPRL controls remain regular. Causal-sector sums and tested j=1/2 boundary-intertwiner contractions do not remove the k=4,5 powers.
3. The published Appendix-D Feynman boundary primitive is reproduced. For j=1/2, `delta^(rho,1/2)=-i*c1*delta-(c2/2)*delta_prime`, and `Theta_+ + Theta_- = 1` is validated on smooth tests.
4. Iter026: the logarithmic k=3 leading term is nearly antipodally odd on tested generic angular sectors, but k=4 and k=5 have antipodal ratio 1.0 across all tested boundary/gamma/seed rows; simple principal-value parity cancellation is therefore not a generic k=4,5 mechanism.
5. Iter027: a Christensen positive absolute-value K5 spanning-tree proof cannot close for the Toller carrier. Exact graph geometry requires max edge exponent `M>=5/2`, while full 2x2 Toller operator norms give local power `p≈2`, hence single-edge weighted radial integrability only for `m<~3/2`. This is a no-go for that proof strategy, not a physical divergence theorem.
6. Iter028/029: naive products of wedge boundary singular terms are structurally obstructed in the tested linearized common-spectral geometry. K3,K4,K5 complete collision graphs have cycle/conormal left-nullities `1,3,6`; spanning-tree controls are transverse. All 16 K5 source causal sectors retain rank 4 / nullity 6. A source-backed correlated i-epsilon boundary value or a physically fixed distributional extension remains required.
7. Iter030–035 explored finite-part ambiguity on the six-dimensional K5 cycle sector. Full S5 averaging isotropizes a generic quadratic cycle metric; explicit microscopic symmetry breaking restores shape. Iter035 authoritative run `34692215902` completed 32/32 SUCCESS after an infrastructure-only JSON serialization fix.
8. Iter036 authoritative run `34694254523`, merge `3bdda03eb0087d20f6c4601b7d69320bbd94ec8f`: source causal sectors form S5 orbits `5+0`, `4+1`, `3+2`; complete S5 orbit averaging removes quadratic cycle-metric shape, while within-orbit bias restores it.
9. Iter037 authoritative run `34694558711`, merge `bcbae58c751b436819480792d0ab35acf84c51bc`: `dim Sym^2(Cycle_K5)^A5=2` versus S5 dimension 1. Actual j=1/2 Toller blocks satisfy `T_s(g^{-1}) = eps T_s(g)^T eps^{-1}` and equivalently `T_s(g^{-1}) = T_{-s}(g)^dagger` to ~1e-15 on training/holdout edges.

## Iter038 — full small-spin boundary-contracted S5 covariance

Authoritative run `34694739107`, commit `fff6514000d0620b1617af8711e28172795ce216`: **6/6 lanes terminal SUCCESS**.

The run tested gamma `0.2,1.2,2.0` x seeds `83,149`, with six even and six odd permutations per lane, three causal representatives and four boundary states. Raw artifacts satisfy all preregistered numerical gates. Example artifact `10298322565` (`gamma=0.2`, `seed=83`) reports:

- max even causal relative error `2.014e-14`;
- max odd causal relative error with epsilon duality `2.212e-14`;
- max EPRL permutation-control error `1.957e-14`;
- max KAK reconstruction error `2.226e-15`;
- verdict `FULL_SMALL_SPIN_CAUSAL_CARRIER_S5_COVARIANT`.

Scientific classification: **PASS for the tested regular pointwise j=1/2 boundary-contracted carrier**. This closes the objection that odd-permutation covariance is merely an edge-level convention artifact.

It does **not** establish covariance, existence, uniqueness, or finiteness of the singular multiwedge distributional extension.

## Active Iter039 — S5-invariant distributional-extension jet audit

Preregister commit `805eb2f2ae69ddc27a62859d61bef12772240238`; computation commit `df02a2a49cc3912256cc99fb71a4e80b88037847`; workflow commit `bea6e15fdc9a4204deadb1435fae8d0e37f4a13d`.

Authoritative run: `34695173734`.

Seventeen independent degrees `d=0..16` are computed in parallel for the exact K5 cycle representation. Each lane evaluates `dim Sym^d(Cycle_K5)^G` for S5, A5 and the three fixed causal-sector stabilizers. Numerical integrality/orthogonality is separated from the scientific discriminator.

The degree range is frozen from the j=1/2 Appendix-D source singular content: ten wedge factors contain delta and delta-prime terms; nominal common-scaling degree ranges up to 20 in four independent relative directions, giving a power-counting local derivative budget through degree 16. This does not assume the naive product exists.

Frozen discriminator: `S5_SYMMETRY_ONLY_EXTENSION_UNIQUE_THROUGH_16` iff the S5 invariant multiplicity is <=1 at every degree `0..16`. Failure is a scientific negative result for **symmetry-only uniqueness**, not a physical divergence statement.

## Claim locks

- no `NEW_PHYSICS_FOUND`;
- no claim that the causal EPRL vertex is nonperturbatively divergent or finite;
- no universal no-go theorem for causal EPRL;
- no physical F9 promotion from surrogate/symmetry evidence alone;
- no G8 novelty promotion before physical F9/F10 evidence;
- regular carrier S5 covariance does not imply a unique singular distributional extension;
- no arbitrary counterterm may be promoted to physical evidence.
