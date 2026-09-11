# Bridge M02 × M04 — Causal structure × quantum-geometric labels

**Iteration:** 002  
**Bridge status:** `EXISTENCE_COMPATIBILITY = PASS_EXTERNAL`; `CRQN_SAME_REALIZATION = OPEN_BLOCKED`.

## 1. Question

Can microscopic causal/Lorentzian data coexist with quantum-geometric representation data in one carrier without adding them only after the fact?

The answer at the level of **existence of a mathematical carrier is yes**. Causal spin-foam and Lorentzian group-field-theory constructions provide explicit precedents. This does not yet establish the CRQN dynamics.

## 2. External evidence that changes the v0.1 matrix

Several independent lines are relevant:

- causal spin foams were formulated as sums over branched coloured two-surfaces carrying intrinsic causal structure;
- causal evolution of spin networks joined spin-network quantum states by a discrete causal structure;
- causal versions of Lorentzian spin-foam amplitudes have been studied for decades;
- Bianchi & Martin-Dussaud (2024) identify the orientation of the spin-foam two-complex as a physical causal variable and propose a causal EPRL construction;
- Bianchi, Chen & Gamonal (2026) introduce a causal spinfoam vertex for 4D Lorentzian quantum gravity with explicit causal data and a large-spin selection of Lorentzian Regge geometries compatible with that data;
- Lorentzian Barrett-Crane/TGFT work explicitly includes spacelike, lightlike and timelike tetrahedra and analyzes local causal structure.

Therefore the previous `M02 × M04 = 0 / unknown` rating was too conservative and has been upgraded to `+2 / ESTABLISHED_EXTERNAL` for **coexistence**, while the CRQN-specific implementation remains open.

## 3. Three carrier branches

### Branch A — causal labelled 2-complex

State/history object:

`Q_A = (K, o, j, i, x)`

with:

- `K = (V,E,F)` a finite oriented 2-complex or a dual simplicial cellular complex;
- `o` causal/orientation data on the dual one-skeleton and/or local wedges/half-edges;
- `j_f` representation-like face labels encoding quantum areas/flux data;
- `i_e` intertwiner-like edge labels encoding quantum polyhedral/gluing data;
- `x` optional finite local causal labels needed to distinguish spacelike/timelike/lightlike sectors.

Candidate boundary space:

`H_boundary = direct_sum_(gamma,o_boundary) H_spin-network(gamma,o_boundary)`.

Candidate amplitude factorization:

`A[K,o,j,i] = Prod_f A_f(j_f) Prod_e A_e(j_f,i_e,o) Prod_v A_v^C(j_f,i_e,o_v)`.

CRQN requirement:

`A_v^C(o_v) != A_v^C(reverse(o_v))`

in general, so causal orientation is physical data rather than automatically averaged away into a time-symmetric projector.

**Assessment:** strongest carrier branch. Explicit coexistence evidence exists. The open problem is not whether causal and quantum-geometric data can coexist, but whether CRQN can define a distinct amplitude/RG law without collapsing to causal EPRL/TGFT.

**Verdict:** `SELECTED_FOR_CRQN_V0.2`.

### Branch B — causal labelled hypergraph

State object:

`Q_B = (H, prec, lambda)`

where a hypergraph carries causal order and higher-arity local geometric labels.

Advantages:

- flexible combinatorics;
- natural multi-cell interactions;
- suitable for rewrite/coarse-graining algorithms.

Weaknesses:

- no comparably mature 4D Lorentzian quantum-gravity amplitude with the required quantum-geometric interpretation was identified;
- gauge/geometric meaning of generic hyperedges is underdetermined;
- using hypergraphs only for computational flexibility risks replacing a physical mechanism by representation convenience.

**Verdict:** `PARKED_AS_ALTERNATIVE_CARRIER`; not selected while Branch A has stronger physics provenance.

### Branch C — causal set enriched by quantum-geometric data

State object:

`Q_C = (C, prec, lambda)`

with a locally finite poset plus finite Hilbert/representation data on events or relations.

Evidence exists from causal evolution of spin networks and quantum causal histories that causal order can organize quantum state spaces/evolution maps. This branch has conceptual appeal because causal order is maximally primitive.

Weaknesses:

- the geometric-label interpretation is less direct than in a spin-foam 2-complex;
- a unique local 4D gravitational amplitude is not supplied by causal order alone;
- enrichment can become arbitrary unless label dynamics are independently derived.

**Verdict:** `RETAIN_AS_CONTROL_BRANCH`, not primary v0.2 carrier.

## 4. CRQN v0.2 carrier decision

Use Branch A as the provisional microscopic carrier:

`CRQN_micro = oriented causal labelled 2-complex`.

This is a carrier decision only. It does **not** license importing the EPRL/Barrett-Crane/GFT vertex unchanged.

The next synthesis question is therefore sharpened from

> can M02 and M04 coexist?

to

> what new dynamical selection rule follows from the MSQGR mechanism set once the carrier is an oriented quantum-geometric 2-complex?

## 5. Novelty / collapse test

Branch A creates an immediate danger:

`CRQN -> causal EPRL/TGFT with renamed variables`.

If all of the following are inherited unchanged—state space, vertex amplitude, measure, RG flow and continuum map—then G8 must be marked `FAIL_ALREADY_REGISTERED` and Candidate A is not a new model.

To avoid artificial novelty, CRQN is allowed to be distinct only if the mechanism synthesis derives at least one nontrivial relation such as:

- a causal-consistency relation that fixes part of the vertex/edge weight;
- an RG-invariant relation linking causal labels and quantum-geometric couplings;
- a reduced relevant-coupling manifold forced jointly by causal composition and continuum gauge recovery;
- a same-parent observable relation not present in the imported source families.

The relation must be derived, not inserted to manufacture difference.

## 6. Next mathematical target

Define a causal composition functional `C[o,j,i]` and a minimal vertex ansatz

`A_v^CRQN = A_v^geom * F_causal(o_v ; j_f,i_e ; theta)`

subject to:

1. orientation reversal gives the conjugate/advanced counterpart rather than the identical amplitude;
2. gluing two compatible vertices preserves internal causal orientation;
3. large-label stationary points admit Lorentzian Regge geometry;
4. incompatible local causal/geometric assignments are suppressed or vanish;
5. the number of free causal couplings `theta` is finite and becomes subject to RG flow rather than arbitrary per-complex tuning.

At v0.2, `F_causal` is intentionally **not chosen**. Deriving or constraining it is the next research problem.

## 7. Gate update

- G1 ontology: `PARTIAL_PASS` — carrier class selected, exact equivalence/gauge category still open.
- G2 causal/Lorentz: `PARTIAL_PASS_EXTERNAL` — coexistence is established externally; CRQN recovery still open.
- G3 quantum dynamics: `OPEN_BLOCKED` — no CRQN-specific normalized amplitude.
- G8 nontriviality: `HIGH_RISK_OPEN` — likely collapse into known causal spin-foam/TGFT unless synthesis produces an additional forced relation.

## 8. Decision

**M02 × M04 does not kill Candidate A.** The bridge exists. The research bottleneck moves one level deeper to **M02 × M04 × M05**: causal quantum geometry must determine or nontrivially constrain the history amplitude rather than merely coexist in the same carrier.
