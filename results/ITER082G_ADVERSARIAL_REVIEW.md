# Iter082G adversarial review — supported-jet Čech descent

**Date:** 2026-09-15

## RESULT_REVIEWED

Researcher result: `results/ITER082G_SM_K5_SUPPORTED_JET_CECH_DESCENT_RESULT.md`, result commit `617d2a02a3b09e20eb81a7dced1f5ec5e4f843f6`.

Frozen chronology:

- preregistration `2cfc7ec27905fc60eb3fe133d827dbf9e579232d`;
- implementation `0dbded5bb0cc463dca726af2477f2c38fca5dbd4`;
- production workflow/head `fd108d7c6d0ffee8681ef7cbfb20ef261cec3a45`;
- Actions run `34901591129`, terminal `success`;
- job `104168566499`, terminal `success`;
- artifact `10370872893`;
- artifact ZIP digest `sha256:e9e71e981554f3c4c24da26f12dc8e609d8fda2df80fc3219ba7b0b616189853`;
- aggregate JSON SHA256 `135b8c6c6a0ba37a2d32a352cbfcc885459b294f0711f765cfaa0aa269fc69bf`.

Researcher classification: `K5_SUPPORTED_JET_CECH_DESCENT_EXACTLY_SOLVABLE_WITH_GLOBAL_JET_GAUGE_FREEDOM_SCOPED`, Researcher verdict `PASS_EXACT_SCOPED`.

## FROZEN-CONTRACT AUDIT

The preregistration prospectively freezes an explicitly **abstract scalar normal-order** module

`J_k = span{e_0,...,e_omega_k}`

with `(omega_3,omega_4,omega_5)=(0,3,8)`, direct-summed over the 16 divergent K3/K4/K5 blocks. It does not claim that this is the full right-SU2 invariant tensor/distributional normal-jet module.

The three-chart nerve has vertices `X,V,W` with all pairwise and triple overlaps present. The exact transition matrices are generated from the frozen radial restrictions

- `X->V = sinh`, `V->X = asinh`;
- `X->W = tanh`, `W->X = atanh`;
- `V->W = v/sqrt(1+v^2)`, `W->V = w/sqrt(1-w^2)`;

through the required finite jet order. The rational series hard-coded in the implementation match these expansions through degree 9.

For each module, the implementation constructs `2 dim(J_k)` deterministic 1-cocycles by freely choosing basis data on `XV` or `VW` and defining `XW` by the twisted cocycle equation. Because the nerve is the full 2-simplex and the transition system satisfies the cocycle, this spans the complete vector space of twisted 1-cocycles for the frozen module.

The explicit solver

- fixes the harmless gauge `b_X=0`;
- sets `b_V=-T_VX a_XV` and `b_W=-T_WX a_XW`;
- verifies all three overlap equations exactly over `Q`;
- then adds an arbitrary globally transported vector and verifies the coboundary is unchanged.

By linearity, exact coboundary reconstruction of the generated basis proves reconstruction for every 1-cocycle in the frozen finite-dimensional module. This is an algebraic theorem for the frozen object, not merely a numerical sample.

## ADVERSARIAL ATTACKS

### 1. Full physical normal-jet object attack

The frozen `J_k` is not the corrected physical right-SU2 invariant tensor normal-jet object. In particular the repository separately retains invariant scalar normal-jet dimensions `d_0..d_8=[1,0,1,0,3,0,7,0,16]` and a demonstrated deepest scalar invariant subspace/lower bound 28, whereas the Iter082G deepest abstract order module has dimension 9. Therefore Iter082G cannot be promoted to a full physical Čech-H1 theorem.

This is a scope limitation already stated by the Researcher, not a contradiction of the frozen theorem.

### 2. Nerve-topology counterexample

The exactness result depends on the frozen full three-chart 2-simplex. If one removes the triple overlap so the nerve becomes a 3-cycle, a nontrivial `H^1` can exist even for constant scalar coefficients. Thus “supported-jet Čech H1 vanishes” is not atlas-topology-independent. The Researcher does not make that overclaim.

### 3. Distributional transformation-law attack

Actual supported distributions generally transform with the dual/pushforward law, Jacobian/density factors and tensor/right-SU2 structure, not merely by scalar polynomial pullback `f(t)->f(phi(t))`. Iter082G explicitly freezes the latter as an abstract scalar normal-order control and expressly excludes a global distributional patching theorem. Therefore this wrong-object witness blocks physical promotion but does not falsify the scoped algebra.

### 4. S5 covariance attack

The executable P4 enumerates all 120 permutations only at the block-label set level. It does not re-run every descent residual under each permutation. However the transition matrices depend only on block size `k`, and the solver contains no absolute block label. Consequently the descent equations are analytically equivariant under the same block relabeling. The implementation is weaker than a fully duplicated 120-permutation residual audit, but the frozen P4 statement follows from the label-blind code structure plus the enumerated block-set closure. No preferred-label rescue was found; the explicit preferred-label negative control survives only 24/120 permutations and is rejected.

### 5. Nested-filtration attack

The code defines the 20 maximal `K3 subset K4 subset K5` chains but P5 is operationally only the preregistered blockwise condition: each transition preserves degree filtration and never maps input degree `j` to output degree `<j`. There is no inter-stratum restriction/gluing morphism between `J_3`, `J_4`, and `J_5` in the frozen object. Therefore Iter082G must not be cited as a theorem about coupled K3/K4/K5 tensor-jet restriction maps. Within the actual frozen direct-sum object, the no-lowering predicate is exact.

### 6. Hidden selector attack

The solver gauge `b_X=0` is an algebraic gauge choice used to construct one representative. The implementation then adds a nonzero arbitrary globally transported vector and verifies the overlap coboundary is unchanged. Hence the construction does not secretly select finite physical coefficients. The free global supported-jet mode remains.

### 7. Source-order / regulator / branch attacks

Iter082G acts only on the post-source-order extension ambiguity module. It does not multiply wedge contact distributions, exchange distributional limits, alter the published one-wedge spectral `i epsilon`, choose a causal branch, claim cancellation, or infer regulator independence. The Iter077 contact-formula erratum and historical Iter077E/F quarantine therefore remain unaffected.

## PROVENANCE AUDIT

The preregistration predates implementation and production. The Actions log checks out exactly `fd108d7c6d0ffee8681ef7cbfb20ef261cec3a45`, runs the frozen implementation, hashes the preregistration and implementation, prints the exact aggregate, and uploads five provenance/artifact files. The terminal artifact metadata reports the same run head and ZIP digest as the durable result. No post-hoc threshold, state, boundary component, finite coefficient or scale selection is present in the reviewed chain.

## VERDICT

`CONFIRMED_SCOPED`

The Researcher result is correct for the prospectively frozen abstract scalar normal-order modules on the explicit full three-chart `X/V/W` nerve. It establishes that the frozen twisted 1-cocycle space is exact and retains a global 0-cochain gauge mode. It does **not** establish full right-SU2 invariant tensor-jet descent or physical distributional patching.

## QUALIFICATIONS

1. Treat Iter082G as an algebraic control on an abstract scalar order module, not as the physical distribution space.
2. Do not promote the result to arbitrary atlas topology; the full-triple-overlap nerve is essential.
3. Do not interpret P5 as an inter-stratum K3/K4/K5 restriction-map theorem; no such morphisms are frozen here.
4. S5 equation covariance is supported analytically by label-blind construction plus block-set enumeration, not by a full 120-fold re-evaluation of every residual.
5. The result supplies no selector: the global supported-jet gauge freedom is deliberately retained.

## AUTHORIZED_NEXT_GATE

Highest information-gain successor is **not** another scalar Čech repetition. Prospectively freeze one of:

- a corrected right-SU2 invariant tensor normal-jet Čech/descent object with its module, transition action, inter-stratum maps and gauge quotient defined before implementation; or
- an actual distribution-space partition-of-unity/descent gate with local distribution spaces, overlap pullback/pushforward law, Jacobians/density weights, continuity/topology and source-ordering fixed before computation.

If the physical module or overlap action cannot be source-defined, the successor must return `BLOCKED_OBJECT_DEFINITION`; it must not replace the missing object by the scalar `J_k` surrogate. All finite coefficients/scales remain symbolic and atlas/descent compatibility remains admissibility, never a selector equation.

## CLAIM LOCKS

Unchanged: no `NEW_PHYSICS_FOUND`; no complete-QG claim; no unique K5 extension; no physical finite-part selector; no exact total extension-space dimension; no theorem that 28/16 conditions suffice; no generic-spin fully contracted non-L1 theorem; no causal-vertex finiteness/divergence theorem; no full tensor-jet/global distributional patching theorem; no regulator independence; no G3/F9/G8/K5 promotion; retain the published spectral `i epsilon` in its source scope.