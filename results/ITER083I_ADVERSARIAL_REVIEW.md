# Iter083I adversarial review

Date: 2026-09-15
Verdict: **CONFIRMED_SCOPED**

Reviewed result: `results/ITER083I_SM_FOREST_POLE_Q_GEOMETRY_SENSITIVITY_RESULT.md`.

## 1. Prospective integrity
The target numbers and witnesses were frozen in preregistration `b3f2111f72c24620fd7e008b322cfd5b9ed962fa` before production. The only implementation repair occurred before the first workflow and changed a literal dependency phrase only. Run `34915925995` is the first production execution and passed all predicates and controls.

## 2. Forest-authority attack
The gate does not invent a new subgraph family. It uses exactly the Iter082D authoritative architecture: 10 K3, 5 K4, 1 K5, 20 maximal chains and `omega=(0,3,8)`.

The pole covector formula follows from the same frozen scaling data:

`d_B + omega_B - 2 |E(B)| = 0`,

so edgewise analytic regularization gives the critical denominator `-2 L_B`.

## 3. Metric-validity attack
Both Q1 and Q2 are exact positive S5-invariant metrics certified independently in Iter083G. Q2 is not a scalar multiple of Q1. Hence the sensitivity witness is not created by an inadmissible or symmetry-breaking metric.

## 4. Primitive-K5 consistency attack
For the full K5 pole vector, Q2^-1 acts by scalar `5/8`. Therefore the full-pole complement does not change. This agrees exactly with Iter083H.

The new sensitivity begins only when proper/nested pole directions are introduced.

## 5. Proper-stratum attack
The K4 witness `e_04` is outside the canonical K4 internal edge set and is Q1-orthogonal to `L_K4`, but has exact Q2* pairing `-15/88`. The K3 witness analogously changes from zero to `-25/176`.

Thus Q dependence is already present in the polar geometry of proper subgraph poles embedded in the full regulator space.

This is stronger than merely observing different Gram matrix entries.

## 6. Maximal-chain attack
The canonical witness `-e_04+e_34` belongs to the Q1* common orthogonal complement of `L3,L4,L5` but not to the Q2* complement. Exact Q2* pairings are `(5/22,0,0)`.

All 20 maximal chains are one S5 orbit, and production transports both the chain and witness. The same exact pattern occurs on 20/20 chains.

No preferred chain was selected post hoc.

## 7. Linear-dependence attack
Both chain Gram matrices have nonzero determinant:

`36` and `10125/484`.

Therefore the changed complement is not caused by rank loss or a degenerate pole set.

## 8. “Changed polar geometry means changed amplitude” — REJECTED
This implication is not justified and is not claimed. A specific meromorphic K5 germ could have residues/numerator components that vanish on all Q-sensitive directions, in which case two projection geometries could still yield the same evaluated amplitude.

Iter083I therefore establishes **available scheme sensitivity of the projection geometry**, not a nonzero physical counterterm difference.

## 9. Stronger locality/factorization loophole — HIGH VALUE
The Q2 witness works precisely because Q2 couples regulator coordinates associated with different edges. A natural family of multivariate projections satisfying product-factorization on independent regulator coordinate blocks may forbid such off-block couplings.

This is the highest-value next theorem candidate. If a natural family `Q_p` is required to obey direct-sum compatibility under arbitrary independent regulator-block concatenation, then all coordinate off-diagonal terms are forced to zero, and permutation symmetry makes all diagonal entries equal. Thus `Q_p` is proportional to the Euclidean metric.

Whether that full naturality axiom is physically/source-authorized for the connected Lorentzian K5 vertex remains a separate scope question.

## 10. Conclusion
The exact scoped statement survives adversarial review:

**proper and nested authoritative K3/K4/K5 pole complements depend on the allowed S5-invariant regulator-metric shape, while the primitive full K5 simple pole does not.**

The next efficient step is to test the stronger product-factorizing/natural family of regulator metrics and then separately test whether K5 source locality actually licenses that stronger axiom.

No nonzero physical scheme dependence, full K5 renormalization theorem, regulator independence, unique selector, generic-spin theorem, G3/F9/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete-QG claim follows.