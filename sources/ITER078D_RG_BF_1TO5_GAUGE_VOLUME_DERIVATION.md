# Iter078D-RG source/theorem derivation — pure `c^5` BF channel and the naive 1-to-5 gauge volume

**Date:** 2026-09-14

Prospective contract: `prereg/ITER078D_RG_BF_CHANNEL_1TO5_GAUGE_VOLUME.md`, commit `71a8c52bbc2b46a83ebb3f57908e1a4e028261a8`.

## Formal-coupling separation

For a universal local witness coupling `c`, write at every fine vertex

`A_c = A_0 + c L`.

The same-boundary five-vertex refinement is multilinear in its local vertex tensors, so

`R_1to5[A_c] = sum_(r=0)^5 c^r R_r`.

The highest coefficient is uniquely

`R_5 = Contract_Fine[L_1 L_2 L_3 L_4 L_5]`.

No mixed sector containing any `A_0` contributes to `R_5`. Therefore the mathematical status of this formal coefficient can be determined without choosing the unknown reference extension `A_0`.

## BF identification

Iter078C established that `L` is the SU(2) Ooguri/BF K5 15j vertex tensor in the repository boundary convention, up to nonzero node normalizations/signs and the overall supported-extension coefficient.

With the corresponding SU(2) internal representation/intertwiner contractions, `R_5` is therefore the Ooguri 4D BF amplitude for the `1 -> 5` subdivision of one 4-simplex, up to explicitly tracked nonzero basis factors.

Iter078B independently established that all frozen coarse causal boundary patterns admit compatible acyclic fine orientations. Hence no causal-orientation obstruction invalidates this pure supported sector before the BF amplitude is evaluated.

## External 4D BF Pachner theorem / divergence

Valentin Bonzom, Etera Livine and Simone Speziale, *Recurrence relations for spin foam vertices*, arXiv:0911.2204, analyze Pachner-move identities for the SU(2) 15j/Ooguri model.

The source states that in 4D Ooguri BF the 2-4 and 1-5 moves are divergent because of redundant SU(2) flatness delta functions in the bulk. For the naive 1-5 move specifically, four delta functions are redundant, giving a divergence of the form

`delta(I)^4`.

The same work constructs a regularized/gauge-fixed 1-5 relation by fixing one Fourier/spin label for each of the four redundant delta functions. This preserves the underlying topological recurrence while removing the explicit redundant gauge volume.

Thus the divergence is a gauge/redundancy normalization issue of the unregularized BF move, not a failure of the local 15j invariant tensor.

## Consequence for the formal causal RG map

Because `R_5` is exactly the pure BF 1-5 channel, the unregularized formal coefficient is not a finite object:

`R_5 ~ delta(I)^4 * (regularized BF boundary tensor)`

schematically in the source normalization.

Therefore an attempted coefficientwise refinement map

`R_1to5[A_0+cL]`

cannot be treated as a finite polynomial map on `c` before specifying how the four redundant BF flatness modes are gauge-fixed or regulated.

Mixed coefficients `R_0,...,R_4` cannot repair this statement at the level of a formal power series because they multiply different powers of the independently frozen coupling `c`. This does not exclude cancellation after assigning a special numerical value to `c`; it only shows that such a cancellation would not define the coefficientwise RG map or its beta function without first regularizing the separate coefficients.

## Positive control

The gauge-fixed/fixed-spin recurrence in arXiv:0911.2204 is the prospective positive control: after the four redundant flatness modes are fixed, the 1-5 BF recurrence becomes a well-defined relation in the theorem's scope. This confirms that the next object to define is a regulator/gauge-fixing convention, not a new local 15j tensor.

## Scientific consequence

The first natural causal 1-to-5 refinement map is blocked at a higher layer than causal combinatorics but before mixed-sector RG closure: its pure supported BF coefficient carries a known redundant gauge volume. This is independently motivated gauge fixing required by the refinement itself; it may not be silently normalized away.