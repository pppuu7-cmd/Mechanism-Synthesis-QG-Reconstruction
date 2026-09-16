# AUTOMATION B adversarial review — K5 projective constant-2x2 closure

Date: 2026-09-16
Reviewed Researcher result: `K5_PROJECTIVE_CONSTANT2X2_CLOSURE_FALSIFIED_EXACT_SCOPED`
Mandatory Critic verdict: **`CONFIRMED_SCOPED`**

## Researcher authority reviewed

Prospective Researcher contract:

`prereg/K5_DEG4_ANNIHILATOR_PROJECTIVE_CONSTANT2X2_CLOSURE.md`, commit `4f1e49f9d850fa7834dd189228d0787f84406f84`.

Authoritative Researcher production:

- run `35140030858`, terminal success;
- job `104941953222`, terminal success;
- workflow/head `d508fd145973a2ad4a8772368e00c5e599c5f908`;
- artifact `10464124390`;
- artifact ZIP digest `sha256:cbe6f218de38f816b30637e48198edf6f4c72a8ffdc3b18931e0f0f733ccf92d`;
- production JSON SHA256 `d9a86723b7baa5e947e0d21998d7468b61b5e26e90fce272bd8db07d677c05b4`;
- durable Researcher result commit `5fc64e1bf971923e7a85f42bc21e72a89af31512`;
- Researcher provenance ledger commit `6b63ae7f9744afb4de4e19c6201c89c9041afbce`.

The parent exact action artifact `10461780450` was independently downloaded during this review. Its ZIP digest reproduced `sha256:d1b2bbd109aa0a3969e37e97aa3e572fc4cba368c42fdc145f94689afbc032dd`; the exact N/B values at all four frozen points agree byte-for-value with `sources/raw/k5_deg4_projective_closure_parent_point_lock.json`. Thus the new point lock is genuinely traceable to the terminal parent artifact rather than only self-asserted metadata.

## Independent Critic production

Critic preregistration was frozen before Critic implementation:

`prereg/K5_DEG4_PROJECTIVE_CONSTANT2X2_CLOSURE_INDEPENDENT_CRITIC_REVIEW.md`, commit `be913c29d80a34753b028b516f3fa1d7db1dd764`.

Critic implementation commit `fbcadd6abf513b8157d8d246d99d933a7b0e5f58`; workflow/head `0acc35547f9c221604a4de47a330d0fbddc47bd6`.

Terminal Critic production:

- run `35143795639`, success;
- job `104954616238`, success;
- artifact `10465504381`;
- ZIP digest `sha256:43576ec5b973673a95d075bcd56f834ede057dce0edbb3d197769aeecf38f606`;
- Critic JSON SHA256 `45ea06a1025b76af2ae9c2767fa3a979f74efc0c7c53e752f1cdec043b04b9dc`.

All frozen Critic checks and controls passed.

## Exact adversarial reconstruction

The corrected object is the projective degree-matched numerator

`P_v[N]=B_v[N]/s1^4`,

not the historical heterogeneous raw-cone comparison `B_v[N]=M N`. Parent authority gives `deg N=27`, `deg B=31`, hence `deg P=27`.

The four frozen positive representatives are unchanged:

- fit_A `(2,1,1,1,1,1,1,1,1,1)`, `s1=11`;
- fit_B `(1,2,1,3,1,2,1,1,2,1)`, `s1=15`;
- validation_U `(1,1,1,1,1,1,1,1,1,1)`, `s1=10`;
- validation_G `(2,3,1,2,1,3,2,1,2,3)`, `s1=20`.

The independently reconstructed fit determinant is

`29427625893405583852377851198976000000000000 != 0`,

so fit_A/fit_B determine one unique rational constant `2x2` matrix. The independently recovered matrix exactly equals the Researcher matrix. Fit residuals vanish identically by construction.

At validation_U the exact residuals are

`7025983846469736430847744951220312500000000 / 25334107571517181846106643`,

`73322633497930679227900303333764062500000000 / 76002322714551545538319929`.

At validation_G the exact residuals are

`228137617695572295597735908822087775610266465901728402048 / 5497853205624388421464115234375`,

`-1520563707365418540588747900509832247312047848360862134816 / 5497853205624388421464115234375`.

All four are nonzero. One exact nonzero validation component already disproves a global constant-matrix identity; here all four survive.

## Counterexample-first attacks

No rescue survives within the frozen constant-module object:

1. **Projective representative rescaling.** Because N and P have the same homogeneous degree 27, the validation residual scales by `lambda^27`. Independent `lambda=2` control reproduces this exactly, so changing the homogeneous representative cannot turn the counterexample into zero.
2. **Constant channel-basis change.** Under a fixed invertible basis change `C`, `N'=CN`, `P'=CP`, `M'=CMC^-1` and the residual becomes `Cr`. The Critic executed an exact nontrivial rational basis change and the validation counterexamples remain nonzero. Thus the failure is not an artifact of the chosen invariant-dual basis.
3. **Wrong projective power.** `s1^3` gives degree 28 and `s1^5` gives degree 26, so neither is the frozen degree-27 projective object.
4. **Historical raw B closure.** `deg B=31` versus `deg N=27`; it remains quarantined as the wrong object and is not used to confirm this result.
5. **Point/state selection.** Fit and validation representatives were prospectively frozen before the corrected gate, both invariant-dual channels are retained, and the parent object remains full all-32 / 100000 source terms. No representative boundary state was substituted.

## Scientific meaning

The two actual invariant-dual degree-27 projective channels do not form a module under this annihilator with one alpha-independent rational `2x2` coefficient matrix. This is an exact finite-witness falsification of that global constant-matrix identity.

It does **not** establish failure of polynomial or rational alpha-dependent coefficient modules, does not prove no larger finite channel module exists, and does not produce an integrated-period relation. The result is pointwise algebraic; the independent projective boundary/Stokes route remains separately blocked by the corrected tangent-flux implementation/review chain.

## Verdict

**`CONFIRMED_SCOPED`**

The Researcher classification `K5_PROJECTIVE_CONSTANT2X2_CLOSURE_FALSIFIED_EXACT_SCOPED` is independently confirmed exactly in its frozen scope.

## Authorized next gate

Highest downstream unlock is not an unbounded search over larger algebraic modules. First complete the already-preregistered **control-only repair of `K5_SCHWINGER_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING`** and obtain a fresh independent Critic review, because that unlocks the 34-orbit physical action-flux audit and the global projective Stokes/IBP route.

A parallel algebraic successor is admissible only if prospectively bounded: `K5_DEG4_ANNIHILATOR_MINIMAL_PROJECTIVE_COEFFICIENT_MODULE`, with the coefficient class (specific polynomial degree bound and/or specified rational denominator family), channel content, fit/holdout strategy and PASS/FAIL criteria frozen before computation. Do not run an open-ended sequence of increasingly flexible fits.

K5 integrated periods, the remaining S5/full order-eight tensor, finite-part selection, regulator independence, F9/G3/G8 and all later CRQN arrows remain locked.
