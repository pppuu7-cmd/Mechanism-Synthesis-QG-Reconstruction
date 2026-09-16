# K5 projective blow-up normal-flux scaling — terminal scoped result

Date: 2026-09-16

Prospective preregistration: `06fc09a0355e6cc15889ac9f244ab03d4cb86569`.
Analytic derivation: `d756f0507c8b7816344fd75b1f8882bca071ede5`.
Independent exact verifier implementation: `a0b2ba1da34a7488af21b647a3213a4f39841de3`.
Workflow/head: `b94733dda1083db76eb3a8abd64f6a43c60e788b`.
Production run: `35087556685` (`success`).
Artifact: `10441874454`.
Artifact ZIP digest: `sha256:3b46f9647ba064b4951e830671123753a270fbdf522b77f8e1e4b910d6d6c59c`.
Result JSON SHA256: `2e3e02377c1a5a5fd294ec9a8aff4a389f1df06688546b03167ba2b2802f84ca`.

Frozen terminal classification:

`K5_PROJECTIVE_BLOWUP_NORMAL_FLUX_SCALING_DERIVED_EXACT_SCOPED`

All frozen checks passed. For every proper Schwinger corner with `k=|Z|`, the projective blow-up scalar measure has exponent `k-1`. For a face-tangent logarithmic field `v_e=alpha_e q_e`, the normal radial component satisfies `v(t)=t Q_Z`, hence the geometric normal-flux exponent is `(k-1)+ord_t(v(t))`, with `ord_t(v(t))>=1`; equivalently, after factoring `v(t)=t Q_Z`, it is `k+ord_t(Q_Z)`.

The exact Jacobian ratios for `k=1,...,9` are alternating `+1,-1,+1,-1,+1,-1,+1,-1,+1`; the `k=1` scalar exponent is exactly zero. Controls reject using scalar exponent `k`, omitting the normal `t` factor, and treating the full edge set as a physical projective boundary. `Z=empty` and `Z=E(K5)` remain provenance/homogeneity controls, not physical projective corners.

Scope lock: this result fixes only the projective blow-up/normal-flux scaling convention. It does not determine physical corner vanishing, integrated Stokes authority, either invariant-dual K5 period, a physical finite part, F9/G3, or NEW_PHYSICS_FOUND. The 34-orbit audit still requires exact lowest nonvanishing coefficients/valuations of the actual physical `N_1,N_2` and `N_c Q_Z`, including exact cancellations and the physical dual/covector S5 transport.