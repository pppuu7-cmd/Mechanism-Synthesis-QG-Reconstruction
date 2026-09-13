# Iter078D-RG result — naive coefficientwise 1-to-5 map is undefined in the pure `c^5` BF channel without gauge fixing

**Date:** 2026-09-14

## Provenance

- Prospective preregistration: `prereg/ITER078D_RG_BF_CHANNEL_1TO5_GAUGE_VOLUME.md`, commit `71a8c52bbc2b46a83ebb3f57908e1a4e028261a8`.
- Source/theorem derivation: `sources/ITER078D_RG_BF_1TO5_GAUGE_VOLUME_DERIVATION.md`, commit `2a3f4f05e04c27cad58e76d11460c7334e0d2d42`.
- Upstream exact causal-refinement authority: Iter078B-RG.
- Upstream BF-channel identification: Iter078C-RG.

## Classification

`ITER078D_RG_PURE_C5_BF_CHANNEL_MAKES_NAIVE_1TO5_COEFFICIENTWISE_MAP_GAUGE_VOLUME_DIVERGENT_DELTAI4_REGULATOR_REQUIRED_THEOREM_SCOPED`

Scientific verdict: **PASS** for the preregistered theorem/formal-coupling statement.

## Findings

For one universal local witness coupling

`A_c = A_0 + c L`,

five-vertex refinement is multilinear and therefore has a formal expansion

`R_1to5[A_c] = R_0 + c R_1 + c^2 R_2 + c^3 R_3 + c^4 R_4 + c^5 R_5`.

The highest coefficient is uniquely

`R_5 = Contract_Fine[L_1 L_2 L_3 L_4 L_5]`.

No unknown `A_0` or mixed sector enters this coefficient.

Iter078C identifies `L` with the SU(2) Ooguri/BF 15j vertex tensor. Hence `R_5` is the Ooguri BF `1 -> 5` amplitude in the supported channel, up to explicit nonzero boundary-basis/local normalization factors.

The 4D BF Pachner analysis of Bonzom-Livine-Speziale shows that the naive Ooguri `1 -> 5` move has four redundant bulk flatness delta functions and therefore a `delta(I)^4`-type gauge-volume divergence. A finite recurrence is obtained only after gauge fixing/regularizing those four redundant modes.

Therefore the naive coefficientwise causal refinement map is **not a finite defined map on the formal coupling `c`** until a BF-compatible gauge-volume prescription is frozen.

## Adversarial qualification

- This does not prove the full numerical causal amplitude diverges at every chosen `c != 0`.
- Mixed sectors cannot cancel the `c^5` coefficient **as a formal coupling coefficient**, but cancellation after assigning one special numerical value of `c` is not excluded by this gate.
- The result does not force `c=0`.
- Setting the BF gauge-volume factor to one without a specified gauge fixing/regulator is invalid.
- The known gauge-fixed BF recurrence is a positive control showing that the obstruction is a missing normalization/gauge prescription, not failure of the 15j recoupling algebra.

## New scientific fact

The first same-boundary causal `1 -> 5` RG experiment is now localized to a concrete mathematical obstruction. Causal partial order is admissible, but the pure supported topological channel makes the unregularized refinement map coefficientwise ill-defined. Thus **BF gauge-volume fixing is logically prior to any mixed-sector beta function or fixed-point search**.

## CRQN chain effect

The path is now:

`local nonunique K5 extension`
-> `supported ambiguity survives integrated vertex`
-> `causal 1->5 orientation exists`
-> `supported ambiguity contains BF 15j channel`
-> `naive c^5 refinement coefficient has delta(I)^4 gauge volume`
-> `BF-compatible gauge fixing/regulator required`
-> `mixed-sector closure ?`
-> `RG fixed point ?`
-> `regulator independence ?`
-> `G3/continuum ?`.

## Claim ceiling

No RG fixed point, no proof of nonrenormalizability, no unique K5 extension, no regulator independence, no G3, no continuum/Einstein/matter/observable result.

## Exact next admissible step

Prospectively freeze one theorem-backed gauge fixing of the four redundant BF flatness modes for the `1 -> 5` supported sector, including its normalization convention, and test:

1. whether the regularized pure `c^5` coefficient is finite and nonzero;
2. whether its normalization is independent of which four redundant modes/spins are gauge-fixed, up to the theorem's expected equivalence;
3. whether the resulting prescription can be embedded consistently into the **mixed** Lorentzian causal/BF refinement sectors without reordering the source Toller construction.

Only after this regulator/gauge-fixing gate should mixed-sector closure or a beta function for `c` be attempted.