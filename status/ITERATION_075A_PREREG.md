# Iter075A preregistration — quantitative nontransitive positive-real coercivity

Frozen before implementation/production.

## Scientific target
For each of the 1008 nontransitive reduced K4 face cases `(source class, cycle basis, nonempty edge subset)` already certified by Iter074B, construct an exact integer dual vector `y` with signed face columns `a_e` satisfying `a_e·y > 0`. From it certify the deterministic L1 coercive estimate

`||sum_e t_e a_e||_1 >= kappa ||t||_1` for all `t_e >= 0`,

with `kappa = min_e(a_e·y) / ||y||_infinity`.

This follows only if the componentwise certificate is exact; no numerical fit is permitted.

## Frozen panel and criteria
- source classes: `++-+`, `+-++`, `+-+-`, `+--+`;
- all four existing K4 cycle bases;
- all 63 nonempty edge subsets per class/basis: total 1008 cases;
- certificate search cap: primitive integer coordinates in `[-12,12]`, ordered by L1 norm, matching the Iter074B search discipline;
- P1: all 1008 cases have exact strict certificates;
- P2: every derived `kappa` is strictly positive;
- P3: global exact minimum `kappa >= 1/7` (a conservative inherited lower floor implied by Iter074B's terminal `delta1 >= 1/7` because `||y||inf <= ||y||1`);
- P4: the analytic coefficient proof is rechecked exactly from `sum t_e(a_e·y) >= min(a_e·y) sum t_e` and `|y·z| <= ||y||inf ||z||1`;
- P5: basis and S4 existence/status census remain invariant;
- P6 negative control: a positive-admissible transitive face must fail strict separation and must exhibit a nonzero nonnegative kernel witness, preventing a universal coercivity claim.

Frozen PASS label: `ITER075A_NONTRANSITIVE_POSITIVE_REAL_L1_COERCIVITY_EXACT_SCOPED`.
Frozen FAIL label: `ITER075A_COERCIVITY_GATE_FAIL`.

## Interpretation lock
PASS would establish only a quantitative positive-real reduced cut-space separation bound for the frozen nontransitive K4 faces. It is not an epsilon-to-zero convergence theorem, not a complex/distributional boundary-value theorem, not physical causal-vertex finiteness, and gives no K5/G3/F9/G8, complete-QG or new-physics promotion.
