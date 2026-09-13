# Iter078D-RG preregistration — coefficientwise 1-to-5 RG map and the pure BF supported channel

**Date:** 2026-09-14

## Scientific question

Can the minimal one-parameter witness family

`A_c = A_0 + c L`

already define a coefficientwise `1 -> 5` causal refinement/RG map without an additional gauge-volume regulator, given that Iter078C identifies `L` with the SU(2) Ooguri/BF 15j channel?

This gate is deliberately independent of the unknown reference extension `A_0`: it isolates the highest coupling coefficient `c^5` in the five-vertex refined amplitude.

## Frozen upstream authority

- Iter077N: `L` survives the integrated vertex and standard gluing.
- Iter078B: all 32 coarse causal boundary patterns admit compatible acyclic `1 -> 5` fine orientations; therefore causal combinatorics do not block the refinement.
- Iter078C: the pure supported sector is the SU(2) Ooguri/BF 15j state-sum channel, up to explicit local coefficient/basis/gauge-normalization factors.

External theorem/source authority:

- Bonzom, Livine, Speziale, *Recurrence relations for spin foam vertices*, arXiv:0911.2204: the 4D Ooguri 15j model is topological/Pachner related, while the naive `1 -> 5` move is divergent because four bulk flatness delta functions are redundant, producing a `delta(I)^4`-type gauge-volume factor. A regularized/gauge-fixed move is obtained by fixing the corresponding Fourier/spin data.

## Frozen refined expansion

For five fine vertices `v=1,...,5`, use one universal formal coupling `c` and expand

`R_1to5[A_c] = Contract_Fine[ product_v (A_0,v + c L_v) ]`

as a formal polynomial in `c`:

`R_1to5[A_c] = R_0 + c R_1 + c^2 R_2 + c^3 R_3 + c^4 R_4 + c^5 R_5`.

By multilinearity,

`R_5 = Contract_Fine[ product_v L_v ]`.

No lower-power mixed sector contributes to the formal coefficient `R_5`.

## Frozen object identification

Under the standard SU(2) BF internal representation/intertwiner contractions used in Iter078C,

`R_5`

is exactly the Ooguri/BF `1 -> 5` refined 4-simplex amplitude in the supported channel, times explicit nonzero basis normalizations and the common local coefficient stripped from `L`.

## Positive control

The regularized/gauge-fixed BF recurrence obtained by fixing the four redundant Fourier/spin variables must be finite as a formal Pachner identity in the cited theorem's scope. This control distinguishes gauge-volume divergence from a failure of the 15j recoupling algebra itself.

## Negative / adversarial controls

1. Do not infer that the full causal amplitude diverges for every numerical `c != 0`; cancellation between different powers at a specially chosen numerical value is not excluded by this formal-coefficient gate.
2. Do not allow mixed `A_0/L` sectors to cancel `R_5` **as a formal polynomial coefficient**, since they carry different powers of the independently frozen coupling `c`.
3. Do not set `delta(I)^4` or the resulting BF normalization factor to one without a specified gauge fixing/regulator.
4. Do not interpret BF gauge fixing as already selecting the K5 extension coefficient `c`.

## PASS

PASS iff the exact formal-coupling argument plus the external BF Pachner theorem establishes:

- the `c^5` coefficient is the pure BF `1 -> 5` amplitude;
- the naive unregularized coefficient contains the known `delta(I)^4` gauge-volume divergence;
- therefore the naive coefficientwise causal refinement map on `{A_0,cL}` is not a finite defined RG map for nonzero formal `c` until a BF-compatible gauge fixing/regulator is frozen.

Classification:

`ITER078D_RG_PURE_C5_BF_CHANNEL_MAKES_NAIVE_1TO5_COEFFICIENTWISE_MAP_GAUGE_VOLUME_DIVERGENT_DELTAI4_REGULATOR_REQUIRED_THEOREM_SCOPED`

## FAIL

FAIL iff the cited Ooguri `1 -> 5` coefficient is finite without gauge fixing in the same normalization, or if `R_5` is not the BF channel identified in Iter078C.

## BLOCKED

BLOCKED iff the BF/internal-weight matching needed for the `R_5` identification cannot be frozen unambiguously.

## Interpretation ceiling

A PASS does not prove that CRQN cannot be renormalized and does not force `c=0`. It proves that the first natural coefficientwise `1 -> 5` RG map is mathematically incomplete without a gauge-volume prescription even before mixed-sector closure is addressed.

The next admissible step on PASS is to freeze a source/theorem-backed gauge fixing of the four redundant BF flatness modes (or an equivalent regulator) and then ask whether the regularized `c^5` channel plus mixed sectors close on a controlled coupling space.

No RG fixed point, regulator independence, G3, continuum, Einstein, matter or complete-QG claim follows.