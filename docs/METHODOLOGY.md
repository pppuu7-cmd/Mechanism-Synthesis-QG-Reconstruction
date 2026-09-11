# MSQGR Methodology v0.1

## 1. Unit of analysis

A **source family** is an established research programme. A **mechanism** is a physically operative ingredient that can in principle be expressed independently of the family label.

Every mechanism record must contain:

- normalized mechanism ID and name;
- source families in which it appears;
- physical function;
- role: `ORIGIN`, `DYNAMICS`, `TRANSPORT`, `CONSTRAINT`, `EMERGENT_SIGNATURE`, or `IR_TARGET`;
- ontological commitment;
- required symmetry/causal assumptions;
- mathematical carrier (graph, field, algebra, amplitude, RG flow, etc.);
- evidence/status class;
- known failure modes;
- candidate compatibility notes.

## 2. Role separation

The highest-risk error in mechanism synthesis is confusing a rule that **constrains** a theory with a rule that **creates** its microscopic data.

Example pattern:

`chosen entropy/action functional -> equilibrium/consistency law -> field equations`

is not equivalent to

`finite microscopic law -> unique entropy/action functional -> quantum dynamics`.

Therefore no `TRANSPORT` or `CONSTRAINT` mechanism may be used as the sole `ORIGIN` mechanism unless an independent derivation upgrades its status.

## 3. Recurrence score

For a normalized mechanism m define a provisional priority score

`P(m) = R + F + B + E - C - D`,

where:

- `R`: independent-family recurrence;
- `F`: functional necessity (does it close a required QG task?);
- `B`: bridge value between microscopic and continuum descriptions;
- `E`: empirical/phenomenological contact potential;
- `C`: conflict burden with other high-priority mechanisms;
- `D`: redundancy/decorative burden.

The score is only a search heuristic. It is not Bayesian evidence that the mechanism is physically true.

## 4. Compatibility matrix

For mechanisms `m_i`, `m_j`, define

`C_ij in {-2,-1,0,+1,+2}`

with meanings:

- `+2`: explicit mathematical coexistence known in one realization;
- `+1`: plausible compatibility / known bridge exists but not fully closed;
- `0`: unknown / insufficiently specified;
- `-1`: significant tension requiring a nontrivial bridge;
- `-2`: direct contradiction under the current definitions.

Compatibility is checked in seven channels:

1. ontology;
2. causal/Lorentz structure;
3. gauge/diffeomorphism structure;
4. state/Hilbert-space or path-integral carrier;
5. dynamics and measure;
6. coarse-graining/RG;
7. continuum and observable map.

A pair is not globally compatible merely because one channel passes.

## 5. Candidate synthesis

Candidate generation is a constrained set-cover problem. A candidate must cover at minimum:

- microscopic degrees of freedom;
- causal structure;
- quantum dynamics;
- UV control or UV completion criterion;
- coarse-graining/continuum formation;
- symmetry/gauge consistency;
- normalized observable map;
- GR + QFT infrared recovery.

The objective is to minimize the number of independent assumptions while avoiding duplicate mechanisms that solve the same task.

## 6. Ablation rule

For candidate M with mechanisms `{m_1,...,m_n}`, construct `M \ m_i` for every component.

A mechanism survives only if its removal causes at least one named failure:

- loss of causality;
- loss of quantum-geometric degrees of freedom;
- loss of continuum formation;
- loss of UV control;
- loss of gauge/diffeomorphism closure;
- loss of observable normalization;
- loss of IR recovery;
- loss of a discriminating prediction.

Otherwise it is marked `REDUNDANT_PENDING_REMOVAL`.

## 7. Same-realization rule

No candidate can claim combined success from disconnected constructions. In particular, the following chain must eventually be explicit in one model:

`microstate -> dynamics/measure -> coarse graining -> continuum effective action -> normalized observables -> IR gravity/matter`.

If any arrow is supplied only by analogy to another framework, the chain is `BLOCKED` at that arrow.

## 8. First hard gates

### G1 — ontology closure
The microscopic variables and equivalence/gauge relations are explicitly defined.

### G2 — Lorentz/causal closure
Causal admissibility is not merely imposed by an uncontrolled preferred structure. If a foliation is used as a regulator, its physical disappearance must be demonstrated.

### G3 — quantum-dynamics closure
A normalized amplitude/measure or Hamiltonian/constraint dynamics is specified, not only kinematics.

### G4 — RG/continuum closure
A coarse-graining map and candidate continuum critical surface are defined. Numerical dimensional flow alone is not sufficient.

### G5 — symmetry/anomaly closure
The continuum gauge/diffeomorphism/refoliation structure must emerge without an uncontrolled anomaly.

### G6 — IR Einstein/QFT closure
The low-energy effective action must contain the Einstein-Hilbert sector with controlled corrections and a matter sector whose propagation/causality can be compared to observation.

### G7 — observable closure
At least one normalized cross-scale observable must be derived from the same realization rather than imported.

### G8 — nontriviality / beyond-comparator gate
The candidate must eventually exhibit a relation or prediction not equivalent to relabeling an already registered framework.

## 9. Independence protocol

MSQGR may use RQIR/KMQGB only after a candidate has been generated by the mechanism procedure. RQIR/KMQGB can reject, block, or rank candidates but may not be used to silently tune the mechanism atlas until a chosen candidate passes.

## 10. Evidence language

Use only:

- `ESTABLISHED_EXTERNAL`
- `DERIVED_MSQGR`
- `REPRODUCED_EXECUTABLE`
- `HYPOTHESIS_ONLY`
- `OPEN_BLOCKED`
- `REJECTED`

No repository document may upgrade `HYPOTHESIS_ONLY` to `ESTABLISHED` without an explicit evidence trail.
