# Candidate A — Causal Renormalized Quantum Network (CRQN)

**Status:** `HYPOTHESIS_ONLY / ARCHITECTURE_V0.1`  
**Promotion:** forbidden until hard gates G1–G7 have explicit same-realization evidence.

## 1. Why this candidate exists

The first synthesis selects mechanisms that (a) recur across multiple quantum-gravity programmes, (b) solve distinct required functions, and (c) are not obviously mutually contradictory at architecture level.

The selected core is intentionally small:

- M01 relational/background-independent microstructure;
- M02 microscopic causal order / Lorentzian admissibility;
- M04 quantum-geometric labels;
- M05 covariant history sum;
- M07 RG criticality;
- M12 continuum formation by coarse graining;
- M13 anomaly/gauge closure;
- M17–M18 as mandatory IR targets.

M09 entanglement/holography and M14 analyticity/unitarity are initially external consistency filters. M08 dimensional flow and M11 noncommutativity are candidate signatures, not axioms.

## 2. Microscopic state ansatz

A microscopic spatial/causal configuration is represented schematically by

`Q = (V, prec, C, lambda)`

where:

- `V` is a locally finite set of elementary events/cells;
- `prec` is an acyclic causal partial relation or an equivalent Lorentzian admissibility structure;
- `C` is a finite combinatorial incidence structure (graph, 2-complex, hypergraph or simplicial dual complex);
- `lambda` are quantum-geometric labels carried by cells/links/faces, provisionally representation/intertwiner-like data or a more general algebraic replacement.

The crucial synthesis hypothesis is not that one existing family is correct, but that **causal relational order and quantum geometric labels are two aspects of the same microstate**, rather than two theories glued together after quantization.

### G1 blocker

The exact category of admissible `(V,prec,C,lambda)` objects and their gauge/equivalence relations are not yet fixed. Therefore ontology closure is `OPEN_BLOCKED`.

## 3. Quantum history ansatz

For boundary data `B_i -> B_f`, define provisionally

`A[B_f,B_i] = Sum_H  (1/|Aut(H)|)  W_causal[H] W_geom[H] W_matter[H]`,

where the sum runs over finite labelled histories interpolating the boundary data.

Equivalent exponential notation may be used only once a microscopic action is defined:

`Z = Sum_H integral dmu(lambda) exp(i S_micro[H,lambda]) Chi_causal(H)`.

Here `Chi_causal` is not allowed to be an arbitrary after-the-fact projector. The research goal is to absorb causal admissibility into the definition of history and/or local amplitudes so that causality is structural.

### G3 blocker

Neither `W_geom` nor a unique normalized measure is currently derived. This is a candidate architecture, not yet a quantum dynamics.

## 4. Renormalization and continuum hypothesis

Introduce a coarse-graining map

`R_k : Q_micro -> Q_k`

and an effective action/functional `Gamma_k` on coarse variables. The target is a flow with a finite-dimensional UV critical surface and an IR trajectory containing an Einstein-like phase.

Schematic requirement:

`k dGamma_k/dk = B[Gamma_k]`,

with a candidate fixed point or critical manifold

`B[Gamma_*] = 0`.

CRQN does **not** assume that the functional-RG realization of asymptotic safety can simply be copied. The mechanism imported from that family is the *UV criticality criterion*. The actual beta functional must be derived for the CRQN state/history space.

### G4 blocker

No CRQN beta functional or controlled continuum critical surface has yet been computed.

## 5. Continuum reconstruction target

A valid continuum phase must supply collective variables for which

`Q_micro -> (M, g_{mu nu}, matter, ...)`

and an effective action of the form

`Gamma_IR = integral d^4x sqrt(-g) [ (M_P^2/2) R - Lambda + L_matter + sum_i c_i O_i/Lambda_QG^(d_i-4) + ... ]`.

Required properties:

1. four macroscopic dimensions in the tested regime;
2. approximate local Lorentz invariance;
3. causal propagation compatible with continuum QFT;
4. Einstein-Hilbert dominance at low curvature;
5. controlled higher-curvature/nonlocal corrections;
6. a derived Newton coupling and cosmological sector or an explicit explanation of their relevant directions.

This IR form is a target, not evidence that CRQN achieves it.

## 6. Gauge and refoliation problem

A major danger is combining a causal microstructure with quantum geometry in a way that secretly introduces an observable preferred slicing.

CRQN therefore imposes the following decision rule:

- a foliation may be used as regulator/bookkeeping;
- physical observables must become independent of that foliation in the continuum limit;
- if a preferred foliation remains physical, the model must be classified as a different symmetry theory and confronted directly with Lorentz/diffeomorphism constraints rather than described as GR recovery.

G5 remains `OPEN_BLOCKED` until the candidate constraint/gauge algebra or covariant replacement is explicit.

## 7. Entanglement and holography: deliberately demoted from origin

Entanglement entropy, causal-diamond equilibrium and holographic relations may become powerful tests of a continuum phase. They are not currently used to specify the microscopic action.

Reason: an equilibrium or information law can map a chosen entropy/constitutive functional into field equations without uniquely deriving the microscopic quantum hard structure. CRQN therefore treats M09 as `CONSTRAINT` until a same-parent derivation upgrades it.

## 8. Dimensional flow: prediction target, not input

Several quantum-gravity programmes exhibit or discuss scale-dependent effective dimension. CRQN will therefore calculate spectral/walk/Hausdorff-type dimensions if a stochastic or propagator structure becomes defined, but it will not tune its microdynamics to reproduce a preferred short-distance number.

A dimensional flow is useful only if derived from the same ensemble and measure that generate the continuum phase.

## 9. First falsification matrix

| Test | Pass condition | Current status |
|---|---|---|
| G1 ontology | exact microstate class + equivalence relations | OPEN_BLOCKED |
| G2 causal/Lorentz | causal rule structural; no uncontrolled preferred frame | OPEN_BLOCKED |
| G3 quantum dynamics | normalized amplitude/measure and composition rule | OPEN_BLOCKED |
| G4 RG/continuum | defined coarse graining + critical continuum trajectory | OPEN_BLOCKED |
| G5 gauge/anomaly | continuum gravitational gauge structure closes | OPEN_BLOCKED |
| G6 IR Einstein/QFT | EH + matter recovered with controlled corrections | OPEN_BLOCKED |
| G7 observable | normalized same-realization cross-scale observable | OPEN_BLOCKED |
| G8 nontriviality | relation not reducible to one source framework | NOT_YET_TESTED |

## 10. Mandatory ablations

Once a minimal executable model exists, run:

- `CRQN - M02`: does acceptable causality re-emerge without microscopic causal structure?
- `CRQN - M04`: are geometric labels necessary or can geometry emerge from bare order/incidence alone?
- `CRQN - M05`: can canonical dynamics replace the covariant history sum without loss?
- `CRQN - M07`: is UV criticality actually required once the discrete history sum is nonperturbatively defined?
- `CRQN - M12`: can a continuum phase arise without an explicit coarse-graining/phase-transition mechanism?

If two mechanisms are functionally interchangeable, they must form separate candidate branches rather than coexist redundantly.

## 11. Near-term derivation programme

### A. Fix the micro-object
Compare three concrete carriers without mixing them prematurely:

1. causal labelled 2-complex;
2. causal labelled hypergraph;
3. locally finite causal set enriched by finite geometric representation data.

Select one by closure and calculability, not aesthetics.

### B. Define the smallest local amplitude
Require boundary composition, gauge covariance and a causal orientation rule. Determine whether a spin-foam/GFT-like vertex amplitude can be generalized without importing its full parent theory.

### C. Build one coarse-graining map
Choose a finite truncation and derive how couplings/weights transform under graph/history blocking.

### D. Compute one same-realization observable
Preferred first targets:

- two-point boundary geometry correlator;
- spectral dimension from the same ensemble;
- effective Regge/Einstein term under coarse graining.

### E. Only then submit CRQN to frozen external funnels
Use RQIR/KMQGB as independent judges after the candidate has internally fixed its definitions.

## 12. What would count as early success?

Not agreement with every school. Early success would be the existence of one explicitly defined microstate/amplitude pair that simultaneously has:

- intrinsic causal admissibility;
- quantum-geometric degrees of freedom;
- a computable coarse-graining transformation;
- a nontrivial continuum candidate;
- no immediate gauge/Lorentz contradiction.

## 13. What would kill Candidate A quickly?

Candidate A should be rejected or split if any of the following proves structural:

- causal order cannot coexist with the required quantum geometric amplitude without a preferred-frame pathology;
- continuum gauge symmetry requires fine tuning of an unbounded number of independent couplings;
- no phase/critical surface supports four-dimensional semiclassical geometry;
- the combined state space reduces exactly to an already-known framework with no new relation or explanatory compression;
- matter must be attached by an unrelated post hoc sector;
- normalized observables cannot be defined from the same microscopic measure.

## 14. External anchors for the mechanism choices

Initial literature anchors include reviews of causal sets (Surya, Living Reviews in Relativity 2019), loop/spin-foam quantum geometry (Rovelli; Perez), group field theory and its relation to spin foams/discrete quantum geometry, causal dynamical triangulations (Ambjorn & Loll 2024), asymptotic-safety RG programmes, noncommutative quantum spacetime, and modern holographic quantum-information approaches. These sources justify that the mechanisms occur in the literature; they do not validate the CRQN synthesis.
