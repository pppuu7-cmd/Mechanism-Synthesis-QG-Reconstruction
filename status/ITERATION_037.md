# Iteration 037 — oriented-simplex symmetry gate

Status: **PREREGISTERED / RUNNABLE**

Date: 2026-09-12

## Closed input: Iter036

Authoritative run `34694254523`, merge commit `3bdda03eb0087d20f6c4601b7d69320bbd94ec8f`.

All **34/34** jobs completed SUCCESS: one exact rational representation-theory lane, one exact source-sign covariance lane and 32 random-SPD stress profiles.

Exact source causal data:

- 16 sectors modulo global reversal split under S5 as orbit sizes `1 + 5 + 10`;
- stabilizers have orders `120, 24, 12` for `5+0,4+1,3+2`;
- all `16 x 120 = 1920` factorized wedge-sign covariance checks pass;
- scalar weights depending only on causal orbit type are S5 invariant.

Exact symmetric-tensor dimensions on the 6D K5 cycle space:

- `5+0`: invariant Sym^2 dimension `1`, hence `0` shape parameters after fixing scale;
- `4+1`: dimension `2`, hence `1` shape parameter;
- `3+2`: dimension `4`, hence `3` shape parameters.

Nevertheless, the full S5 orbit average of every stabilizer-invariant basis tensor lies on the unique S5-invariant metric line. All 32 numerical profiles confirm: fixed nontrivial sectors retain shape, complete equal-within-orbit sums isotropize to numerical precision, arbitrary positive weights *between* the three complete causal orbit types remain isotropic, while an explicit within-orbit bias restores shape.

Interpretation remains locked: this is a finite-K5 source symmetry mechanism, not yet a property of the physical Toller/Feynman carrier.

## New physical issue

The published causal vertex is built on an oriented 4-simplex and uses per wedge

`T^(sigma_a sigma_b)(g_b^{-1} g_a)`.

Iter036 used the full S5 relabeling group. But an orientation-preserving simplex relabeling is conservatively only A5. Odd permutations reverse simplex orientation and can reverse oriented wedge arguments. Because Toller matrices are positive/negative boost-frequency pieces rather than group representations, odd permutations may require a nontrivial branch/duality transformation.

Therefore Iter037 must decide whether full S5 isotropization is physically justified or whether only A5 is automatically available.

## 037A — exact A5 cycle-metric theorem

Using exact rational K5 cycle representation:

1. compute `dim Sym^2(Cycle)^A5` and the determinant-normalized residual shape count;
2. compute A5 causal orbits/stabilizers for `5+0,4+1,3+2`;
3. compute the image dimension after A5-averaging each stabilizer-invariant tensor space;
4. adjoin one odd permutation and check whether the invariant metric space collapses to the unique S5 line.

No floating rank decisions are allowed.

## 037B/C — actual j=1/2 Toller orientation reversal

For generic separated Lorentz elements and gamma `0.2,1.2,2.0`, two independent seeds each:

- build full `2x2` Toller blocks for `g` and `g^{-1}`;
- preregister a finite candidate family: same/swap branch, transpose/conjugate/adjoint and epsilon-sandwiched versions, fixed phases `1,-1,+i,-i`;
- choose the best candidate only on five training edges;
- freeze it and require relative Frobenius error `<2e-8` on five disjoint holdout edges;
- independently require the EPRL control `D(g^{-1}) = D(g)^dagger` to `<2e-10`.

## Interpretation lock

- If A5 leaves a residual metric shape and Toller reversal requires a branch swap/duality, Iter036's S5 ambiguity removal cannot be promoted until that odd-permutation transformation is propagated through the transported boundary intertwiners and full vertex functional.
- If A5 alone already gives one invariant metric line, the S5/odd issue is less consequential for finite-part shape.
- A resolved local Toller inverse law is not by itself the full simplex covariance theorem.
- No G3/F9/G8 promotion from Iter037 alone.
