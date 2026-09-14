# Iter082H-SM — full scalar invariant-symbol Čech descent result

Date: 2026-09-15

## Authoritative classification

`K5_FULL_SCALAR_INVARIANT_SYMBOL_CECH_DESCENT_EXACT_WITH_GLOBAL_JET_GAUGE_FREEDOM_SCOPED`

Verdict: **`PASS_EXACT_SCOPED`**.

This result is scoped to the complete scalar `SO(3) x S_n` invariant-symbol modules of the frozen K3/K4/K5 normal representations. It is not a theorem for representation-valued boundary-covariant coefficient maps and not a global physical distributional patching theorem.

## Prospective / production chain

Scientific preregistration before implementation:

- prereg commit `84ad84d6bd2d85d5be52c99a51a1677820754996`;
- `prereg/ITER082H_SM_FULL_INVARIANT_SYMBOL_CECH_DESCENT.md`.

Initial implementation / production:

- implementation commit `7928299da37a08a7f7769999bbba18feb6e36cd9`;
- production commit `41d7ba64906dc4a5e03d25b618659e95a4fb9f63`;
- run `34907033113`, terminal success;
- artifact `10372739062`, digest `sha256:d854e0e395d209a17bb61d18d5c8897e840e1f5bc2b33895f07645b19db83074`.

The raw artifact was consumed before classification. Two P6 malformed controls were found to be hard-coded as `rejected=true` rather than evaluated by the same validators. The first green run was therefore quarantined as `INVALID_IMPLEMENTATION_NEGATIVE_CONTROL_WIRING` in `results/ITER082H_FIRST_GREEN_QUARANTINE.md`, commit `b2cbf2f93456ad10016074418c82b8e8add1c325`. It is not scientific authority.

Control-only repair was prospectively frozen before repair implementation:

- repair prereg commit `28157952d4848675b13e7900b5bfbf8875e5026f`;
- repair implementation commit `8b9fdfaf485f30d50bbb3e13702690554e86a5c9`;
- repaired production commit `b30f722d7c81527eadddfd03675fd725ed3fd465`;
- authoritative run `34907151340`, job `104186367690`, terminal success;
- authoritative artifact `10373251058`;
- artifact ZIP digest `sha256:f0598f2b958f62bb81732abfdf89170570789ab3d8cd6a956a8793b7aac5d195`;
- extracted aggregate JSON SHA256 `1cc88a536ca26c04369499d0d5fbb956616b4b7345d7ed5f96acf8ac13c3edbc`.

No scientific criterion was changed after production inspection.

## Exact invariant-symbol modules

The Iter081R exact Molien/character construction was generalized prospectively from S5 to S3/S4/S5 for

`V_n = spin1_SO(3) tensor Std_n_Sn`

at the frozen normal orders `(omega_3,omega_4,omega_5)=(0,3,8)`.

The exact invariant multiplicities are:

- K3 / n=3: `d=[1]`, cumulative invariant-symbol dimension **1**;
- K4 / n=4: `d=[1,0,1,0]`, cumulative invariant-symbol dimension **2**;
- K5 / n=5: `d=[1,0,1,0,3,0,7,0,16]`, cumulative invariant-symbol dimension **28**.

The K5 row exactly reproduces authoritative Iter081R.

This is a material correction relative to the Iter082G abstract surrogate dimensions `(1,4,9)`: Iter082G was a valid theorem on its explicitly frozen abstract `omega+1` modules, but those dimensions are not the physical corrected invariant-symbol dimensions. The old surrogate is explicitly rejected by the Iter082H negative control.

## Full-module Čech audit

The six X/V/W radial finite-jet transitions were independently re-audited:

- all pairwise inverse identities hold exactly through the frozen degree;
- all six oriented triple-overlap cocycle identities hold exactly;
- every transition has the frozen identity linear term;
- exact S_n covariance passes `6/6`, `24/24`, `120/120` for n=3,4,5;
- exact signed-permutation O(3) controls have zero failures;
- analytic equivariance follows from `F(Rv)=phi(<Rv,Rv>)Rv=R F(v)` and use of the identical node law.

Because these maps are equivariant, their pullbacks preserve the full scalar invariant-symbol submodules. Because the three-chart nerve is a complete 2-simplex and the transition operators are invertible with exact triple cocycle, the local system can be X-trivialized without choosing a preferred invariant basis.

The deterministic full-module 1-cocycle spanning audit then gives:

- K3: 2 basis 1-cocycles, all exact coboundaries, global gauge dimension 1;
- K4: 4 basis 1-cocycles, all exact coboundaries, global gauge dimension 2;
- K5: 56 basis 1-cocycles, all exact coboundaries, global gauge dimension 28.

Every overlap residual is exactly zero. The normal-order filtration has no lowering. Adding an arbitrary globally transported vector in the complete invariant-symbol module leaves the Čech coboundary unchanged.

Therefore the corrected invariant-symbol ambiguity patches algebraically across the explicit X/V/W finite-jet atlas, but **Čech solvability does not select its coefficients**.

## Repaired controls

All frozen malformed controls are rejected. In particular, after the prospectively frozen control-only repair:

- the synthetic singular transition with linear coefficient 0 is mechanically rejected by the same identity-linear/invertibility validator used on the positive atlas;
- the synthetic order-lowering map `8 -> 6` is mechanically rejected by the same `output_degree >= input_degree` filtration predicate;
- corrupt triple map, preferred vertex label, old `omega+1` surrogate-as-full-module claim, and Čech-gauge-as-selector claim are rejected.

The preferred-label control preserves only the 24-element stabilizer rather than all 120 S5 permutations.

## Scientific meaning

Iter082H removes the next algebraic **scalar invariant-symbol Čech-H1** blocker. It strengthens Iter082G from an abstract scalar normal-order surrogate to the corrected full scalar invariant-symbol modules demonstrated by Iter081R for the frozen K3/K4/K5 sectors.

It does **not** establish:

- a unique K5 extension or physical finite-part selector;
- completeness for representation-valued or boundary-covariant coefficient maps;
- actual distributional partition-of-unity patching on physical `SL(2,C)^4`;
- continuity/topological completeness of the physical distribution space;
- partition-of-unity independence for singular Toller amplitudes;
- causal-vertex finiteness/divergence;
- regulator independence;
- G3/F9/G8/K5 promotion;
- `NEW_PHYSICS_FOUND`;
- complete quantum gravity.

## Next analytic blocker

The remaining patching problem is no longer the scalar invariant-symbol Čech algebra. The next admissible analytic target is

`K5_ACTUAL_DISTRIBUTIONAL_PARTITION_OF_UNITY_PATCHING_AND_BOUNDARY_COEFFICIENT_TRANSPORT`

with explicit local distribution spaces, pullback/pushforward and density/Jacobian laws, source ordering, topology/continuity, and inter-stratum compatibility. All finite coefficients and subtraction/analytic scales must remain symbolic.

The independent deepest selector blocker remains

`RIGHT_SU2_COVARIANT_K5_INVARIANT_NORMAL_JET_COEFFICIENT_SELECTOR`.
