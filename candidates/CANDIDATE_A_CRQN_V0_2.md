# Candidate A — CRQN v0.2

**Status:** `HYPOTHESIS_ONLY / CARRIER_SELECTED`  
**Parent:** `CANDIDATE_A_CRQN.md` v0.1

## Change from v0.1

The M02 × M04 bridge has passed at the level of external mathematical coexistence. CRQN v0.2 therefore selects an **oriented causal labelled 2-complex** as its provisional microscopic carrier.

## Microscopic carrier

`Q = (K,o,j,i,x)`

where

- `K=(V,E,F)` is a finite 2-complex / dual cellular complex;
- `o` is dynamical causal/orientation data;
- `j_f` are quantum-geometric representation-like face labels;
- `i_e` are intertwiner-like edge labels;
- `x` is an optional finite local causal sector label when spacelike/timelike/lightlike data require it.

The boundary state space is provisionally

`H_B = direct_sum_(gamma,o_B) H_gamma,o_B`.

No claim is made yet that the final group, representation category, simplicity map or boundary inner product is identical to EPRL or Barrett-Crane.

## History amplitude target

`A_CRQN[K,o,j,i] = Prod_f A_f Prod_e A_e Prod_v A_v^CRQN`.

The v0.2 task is not to choose `A_v^CRQN` freely. The mechanism-synthesis programme must determine whether the joint requirements of causal composition, quantum geometry, RG closure and continuum gauge recovery constrain it.

Write only as a placeholder

`A_v^CRQN = A_v^geom(j,i) F_causal(o;j,i;theta)`.

`F_causal` is **unknown**. Copying an existing causal EPRL/TGFT factor without a synthesis-derived relation is forbidden as a novelty claim.

## Required causal-amplitude properties

A viable local factor must satisfy at least:

1. time/orientation reversal is not automatically identical to the original causal transition amplitude;
2. gluing compatible local histories preserves causal orientation and boundary composition;
3. large-quantum-number stationary points include Lorentzian Regge geometries with compatible causal data;
4. locally inconsistent causal/geometric assignments are dynamically suppressed or excluded;
5. causal couplings form a finite RG-controlled set rather than arbitrary complex-dependent weights;
6. continuum observables must not retain an unphysical preferred discretization/foliation.

## Current gate state

- G1 ontology: `PARTIAL_PASS`.
- G2 causal/Lorentz compatibility: `PARTIAL_PASS_EXTERNAL`.
- G3 quantum dynamics: `OPEN_BLOCKED`.
- G4 RG/continuum: `OPEN_BLOCKED`.
- G5 gauge/refoliation: `OPEN_BLOCKED`.
- G6 IR Einstein/QFT: `OPEN_BLOCKED`.
- G7 same-realization observable: `OPEN_BLOCKED`.
- G8 nontriviality: `HIGH_RISK_OPEN`.

## Immediate research equation

The next problem is to determine whether there exists a finite relation

`Phi(A_v, o, j, i, beta, gauge) = 0`

that is jointly required by:

`causal composition + quantum-geometric semiclassics + RG stability + continuum gauge recovery`.

If the only solutions are existing causal spin-foam/GFT vertices modulo reparameterization, CRQN fails G8 and becomes a convergence result rather than a new theory.

If the conditions select a smaller submanifold or new relation among vertex/edge couplings, that relation becomes the first genuinely MSQGR-derived dynamical content.
