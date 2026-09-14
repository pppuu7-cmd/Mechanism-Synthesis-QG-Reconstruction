# Iter081F K5 causal two-wedge projection control

Date: 2026-09-14
Status: **CRITIC EXACT SOURCE-COMBINATORIAL CONTROL — NOT AN ITER081F BOUNDEDNESS OUTCOME**

## Source object
For a five-valent 4-simplex/K5 vertex, Beltran `arXiv:2603.22661v2` Eq. (8) gives, for signature convention `eta=+1`,

`epsilon_ab = sigma_a sigma_b`,

with `sigma_a in {+1,-1}` the edge time orientations at the vertex. Global reversal `sigma_a -> -sigma_a` leaves every wedge sign `epsilon_ab` invariant. Hence there are `2^(5-1)=16` distinct causal wedge-sign assignments. The same statement is encoded historically in `research/iteration-023-causal-sector-sums/causal/vertex_sigma_to_booster_masks.py`.

The causal cycle constraint is Beltran Eq. (9); for K5 it is exactly satisfied by the factorized assignments above.

## Question
For any two **distinct** wedge links of a single K5 vertex, what is the projection of the 16 globally causal `eta=+1` assignments onto their local sign pair?

## Exact theorem
For every pair of distinct wedges, the projection image is the full set

`{++, +-, -+, --}`,

and every local pair has multiplicity exactly `4` among the `16` globally causal assignments.

### Proof: adjacent wedges
Let the two wedges be `(ab)` and `(ac)` with `a,b,c` distinct. Use the global sign redundancy to set `sigma_a=+1`. Then

`epsilon_ab=sigma_b`, `epsilon_ac=sigma_c`.

The two target signs can therefore be chosen independently by choosing `sigma_b` and `sigma_c`. The remaining two vertex signs are free, giving `2^2=4` global completions for each local pair.

### Proof: disjoint wedges
Let the two wedges be `(ab)` and `(cd)` with `a,b,c,d` distinct. Gauge `sigma_a=+1`. Then `epsilon_ab=sigma_b`, so the first target sign fixes `sigma_b`. For any target second sign `y`, choose `sigma_c` freely and set `sigma_d=y sigma_c`. The fifth vertex sign is also free. Thus there are again `2*2=4` completions for each local sign pair.

These two cases exhaust all pairs of distinct links of K5.

For `eta=-1`, all wedge signs acquire the common extra minus in Beltran Eq. (8); this permutes the four local sign pairs and leaves the same uniform multiplicities.

## Scientific consequence
Causal admissibility at a single K5 vertex does **not** eliminate any of the four local two-wedge words and does not, by itself, single out any proper subset in the Iter081F algebraic atlas.

However this does **not** imply that the globally causal vertex amplitude factorizes as an equal-weight local sum over the four words. A complete causal assignment contributes a product over all wedges. After grouping the 16 full assignments by the signs on two selected wedges, the effective coefficient of a local word contains the amplitudes of the other eight wedges and is generally geometry-, branch-, boundary-, and integration-dependent. The combinatorial multiplicity `4` is not an amplitude weight theorem.

Therefore:

1. a bounded **proper** local Iter081F subset, if found, would still require a new mechanism selecting/weighting that subset; Beltran causal admissibility alone does not do so;
2. a bounded **full** local four-word sum would demonstrate the local `T^+ + T^- = D` cancellation, but cannot be promoted to the full `A_v^+` causal sum without a factorization/cancellation theorem for the other wedges;
3. a strong local no-rescue Iter081F result would remain local and would not prove unboundedness of Beltran's globally correlated `A_v^+`.

## Relation to historical Iteration 023
Historical `vertex_sigma_to_booster_masks.py` independently encodes the same K5 factorization `kappa_ab=sigma_a sigma_b` and enumerates 16 classes modulo global reversal. Historical numerical causal-sector power scans remain separate from the exact local boundedness question.

## Claim lock
This control contains no Toller asymptotic calculation and predicts no Iter081F boundedness classification. It fixes only the exact projection/multiplicity structure of source-defined K5 causal sign assignments.
