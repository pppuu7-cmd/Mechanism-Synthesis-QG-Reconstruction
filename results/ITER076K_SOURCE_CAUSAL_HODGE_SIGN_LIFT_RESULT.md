# Iter076K terminal result — causal sigma/kappa do not fix the global Hodge sign

Date: 2026-09-13

## Authority
- frozen preregistration before implementation: `afcbd9d13833c7e4a2ff997ad49f3959726ad236`
- initial implementation: `3a6099e30c0d1760b0d09c925c4b9dfb3c444a35`
- initial production head: `70ca50aecee1be7ebf911d434dbc262112f64716`
- initial run `34776382876`: non-authoritative for scientific classification because Lane A used an orientation-blind edge permutation action rather than the frozen oriented-edge representation from Iter076H
- minimal control-only repair / authoritative head: `62000d2100e7d44b442f67b1e4118707bd1a9879`
- authoritative retry run: `34779234892`
- aggregate job: `103783117527`
- aggregate artifact: `10324660667`
- aggregate artifact ZIP digest: `sha256:f4f51b24d519488580d06fc15ebf3c52cbe4f439a3abaae18ad79d34ba1c9dac`

Raw authoritative lane artifacts consumed by the aggregate job:
- A: artifact `10323539592`, digest `sha256:0dcf74bcef012cdeb03e0a922731022ecbf84ed6ced02a20401c63722000698a`
- B: artifact `10324470587`, digest `sha256:6b9d6ae79693cfd5adee8a162c751fc0626c6947267ffcbefa5ebecff2cfb14e`
- C: artifact `10325100043`, digest `sha256:c936adf05cc47f7461b9785fe3680ef96df6dc8c5b8edce4b3b72bffcf092ae8`
- D: artifact `10324875294`, digest `sha256:d968790ebb37743f95206731a8fcd499c6f53cfed65cdacf468009339887f1ce`

## Frozen scientific classification

`ITER076K_SOURCE_K5_INCIDENCE_AND_CAUSAL_SIGMA_FIX_HODGE_LINE_NOT_GLOBAL_SIGN_BLOCKED_ORIENTATION_PSEUDOSCALAR_SCOPED`

## Terminal facts

All four prospectively frozen authoritative lanes pass after the minimal representation repair; the aggregate output is `valid=true`.

1. With the fixed Iter076J complementary-edge support and the exact oriented-edge S4 action from Iter076H, the signed-lift solution space is exactly the expected one-dimensional line: the two admissible lifts are global opposites `+H` and `-H`.
2. Exhaustive source-causal `sigma_a` census finds no nonzero selector `q(sigma)` satisfying the required sign-equivariance under S4. Odd stabilizers obstruct such a selector.
3. The induced source wedge signs `kappa_ij=sigma_i sigma_j` likewise do not supply a nonzero global sign-equivariant selector, including the global `sigma -> -sigma` redundancy.
4. Raw label order can choose a Levi-Civita sign for one labelled tetrahedron but is an extra convention and fails as invariant source physics under odd relabelings/root changes.

## Interpretation lock

Iter076J source-provenances the **unsigned** complementary-edge support. Iter076H source-independent algebra fixes the unique sign-twisted Hodge line. Iter076G/I fix the relevant reversal character but not the matrix support. Iter076K now closes the discrete causal-sign question: the actual causal data `sigma_a` and `kappa_ab` do not choose the remaining global sign.

Therefore the exact remaining signed-P3 blocker is an explicit source orientation/pseudoscalar, or an equivalent sign extracted from the full source contraction/intertwiner/group-variable structure. The causal edge signs must not be silently reinterpreted as a 4-simplex Levi-Civita orientation.

`SOURCE_TO_K4_PUSHFORWARD` remains unestablished as a physical signed map. The nominal `epsilon^-1` source numerator/Jacobian coefficient remains `BLOCKED_OBJECT_DEFINITION`: neither zero, nonzero, nor divergent is authorized.

No F9/G3/G8/K5 promotion, causal-vertex finiteness/divergence theorem, physical sector selection, complete-QG claim, or new-physics claim follows.
