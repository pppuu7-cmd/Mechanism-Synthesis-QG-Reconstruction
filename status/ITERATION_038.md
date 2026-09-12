# Iteration 038 — full small-spin causal-carrier S5 covariance

Status: **PREREGISTERED / RUNNABLE**

Date: 2026-09-12

## Closed inputs

### Iter036 — source causal orbit symmetry

Run `34694254523`: **34/34 SUCCESS**.

Exact invariant symmetric dimensions on the six-dimensional K5 cycle space under fixed causal-sector stabilizers were:

- S5 `5+0`: 1 -> 0 shape parameters after fixing scale;
- S5 `4+1`: 2 -> 1 shape parameter;
- S5 `3+2`: 4 -> 3 shape parameters.

Every stabilizer-invariant basis tensor becomes proportional to the unique S5 metric after a complete S5 orbit average. All 32 numerical profiles confirmed that equal-within-orbit covariance removes shape, arbitrary positive weights between the three complete causal orbit types do not restore it, and an explicit within-orbit bias does restore shape.

### Iter037 — oriented simplex / Toller reversal

Run `34694558711`: **7/7 SUCCESS**.

Exact A5 result:

- `dim Sym^2(Cycle_K5)^A5 = 2`, hence **one residual determinant-normalized shape parameter** survives orientation-preserving symmetry alone;
- S5 invariant dimension is 1;
- A5 plus any tested odd generator returns invariant dimension 1;
- A5 causal orbits remain sizes `1,5,10`, but their stabilizers have orders `60,12,6`;
- after A5 orbit averaging, every causal type still has a two-dimensional invariant metric image, i.e. one residual shape parameter.

Therefore the odd-permutation/orientation-reversal sector is physically decisive for removing the final finite-part ambiguity.

Actual j=1/2 gamma-simple Toller blocks on generic group elements satisfy, to ~1e-15 across gamma `0.2,1.2,2.0` and two seeds,

`T_s(g^{-1}) = eps T_s(g)^T eps^{-1}`,

with the equivalent convention relation

`T_s(g^{-1}) = T_{-s}(g)^dagger`.

The EPRL control satisfies `D(g^{-1})=D(g)^dagger` to the same precision. Training/holdout separation was used; every job passed.

These local edge identities do not yet prove odd-permutation covariance of the full boundary-contracted causal vertex.

## Iter038 gate

Use the actual j=1/2 K5 boundary carrier from Iter024, with three causal representatives (`5+0`, `4+1`, `3+2`) and four recoupling-basis five-node boundary states.

For each random S5 relabeling:

1. relabel all five Lorentz group variables and causal sigma signs;
2. regauge the transformed configuration to new `g_0=1` without changing any relative group element;
3. recompute all ten Toller edge matrices from the transformed groups;
4. whenever the canonical orientation of an edge reverses, apply the established epsilon duality to the corresponding half-edge index at **both** endpoint node tensors;
5. transport each four-valent intertwiner tensor to the new node and permute its four half-edge slots to the new canonical neighbour ordering;
6. contract the full K5 tensor network;
7. compare with the original amplitude.

Six even and six odd permutations are tested per job, including identity and a simple transposition. Matrix: gamma `0.2,1.2,2.0` x two independent seeds = six jobs.

### Frozen gates

- max even causal covariance relative error `<2e-8`;
- max odd causal covariance relative error with epsilon duality `<2e-8`;
- max EPRL permutation-control error `<2e-8`;
- KAK reconstruction error `<1e-10`.

## Interpretation lock

A PASS would establish full S5 covariance of the **generic pointwise j=1/2 boundary-contracted carrier** after the correct half-edge dual transport. Together with Iter036/037A, this would remove the objection that the S5 isotropization mechanism relies on an unphysical odd-label symmetry at the regular carrier level.

It would still **not** prove that the singular multiwedge Feynman/distributional extension preserves that covariance, nor prove the integrated causal vertex finite. That distributional extension covariance becomes the next hard gate. No G3/F9/G8 promotion from Iter038 alone.
