# Iter077Q-SM derivation — infinite-dimensional source-compatible tangential extension ambiguity

**Date:** 2026-09-14

Prospective contract: `prereg/ITER077Q_SM_INVARIANT_TANGENTIAL_EXTENSION_AMBIGUITY_DIMENSION.md`, commit `df7d9167067d21be7b5ff1fdafa5aa9cea7ac39d`.

## Upstream authority

Iter077L establishes that after the source gauge fixing the common-collision submanifold is

`N = SU(2)^4 subset SL(2,C)^4`,

with real codimension `12` and transverse scaling degree `20`. Same-scaling-degree extensions exist and differences may contain normal derivatives through order `8`, with coefficient data along `N` subject to any additional independently imposed conditions.

Iter077M constructs the actual-boundary supported ambiguity

`F_SU2(y;Psi) delta_N(x)`

and proves compatibility with the frozen source ordering, common left `SL(2,C)` gauge symmetry, true spin/intertwiner boundary structure and fixed causal data. Its independent compact-boundary control finds nonzero true boundary functionals, so `F_SU2(.;Psi_0)` is not identically zero for at least one actual minimal-sector boundary state `Psi_0`.

The present gate introduces no new physical condition. It asks only how large the already-allowed coefficient space is under the same constraints.

## Invariant tangential scalar

Before gauge fixing, on the invariant common-collision set

`S={g : g_b^-1 g_a in SU(2) for every a,b}`,

define

`Q(g)=sum_(a<b) tr_1/2(g_b^-1 g_a)`.

Here `tr_1/2` is the trace in the fundamental `SU(2)` representation, evaluated on the relative compact element.

### Common-left gauge invariance

Under the exact source gauge action `g_a -> H g_a`, `H in SL(2,C)`,

`(H g_b)^-1(H g_a)=g_b^-1 g_a`.

Every summand, hence `Q`, is unchanged exactly.

### Vertex-relabeling invariance

For any permutation `pi in S_5`, the unordered pair set `{a,b}` is permuted bijectively. Therefore

`sum_(a<b) tr(g_b^-1 g_a)`

is unchanged after simultaneous relabeling of all vertex/group labels. This is stronger than covariance under any causal-label-preserving subgroup.

### Smoothness

On `S/SL(2,C) ~= N=SU(2)^4`, every relative group element is compact and trace is analytic. Thus `Q` and every power `Q^n` are smooth bounded tangential functions on compact `N`.

## Exact nonconstancy

On the frozen path in `N`,

`g_1=g_3=g_4=g_5=I`,

`g_2=diag(e^{it},e^{-it})`,

there are six unordered pairs among the four identity vertices, each contributing `tr(I)=2`, and four pairs involving vertex 2, each contributing `2 cos(t)`. Hence exactly

`Q(t)=12+8 cos(t)`.

Therefore `Q` is nonconstant. Along this path its image contains the interval `[4,20]`.

## Infinite-dimensional coefficient subspace

Freeze one actual boundary state `Psi_0` for which the Iter077M compact restriction

`F(y)=F_SU2(y;Psi_0)`

is not identically zero. For each nonnegative integer `n`, define

`c_n(y)=Q(y)^n F(y)`.

Suppose a finite linear relation exists:

`sum_(n=0)^m a_n c_n(y)=0` for all `y in N`.

Then

`P(Q(y)) F(y)=0`, `P(z)=sum a_n z^n`.

Because `F` is smooth and nonzero somewhere, there is a nonempty open set `U subset N` on which `F != 0`; hence `P(Q(y))=0` on `U`.

`N=SU(2)^4` is connected and real analytic. `Q` is real analytic and globally nonconstant. A real-analytic function that is constant on a nonempty open subset of a connected analytic manifold is constant everywhere; therefore `Q|_U` is not constant. Its image contains infinitely many points (indeed a local interval on a suitable path). A polynomial vanishing on such a set is identically zero. Thus every `a_n=0`.

Therefore `{Q^n F}_{n>=0}` is linearly independent. The admissible tangential coefficient space already contains a countably infinite-dimensional subspace.

## Supported distribution family

For any Iter077L same-scaling-degree extension `A_ext`, define

`A_ext,{a_n} = A_ext + sum_(n=0)^m a_n Q(y)^n F_SU2(y;Psi) delta_N(x)`.

Every finite member of this family:

1. agrees with the source-ordered ten-Toller product off `N` because the added term is supported on `N`;
2. preserves source ordering because it is an extension term added only after the one-wedge Toller functions and off-collision K5 product are fixed;
3. preserves fixed causal labels because `Q` is independent of them and the same coefficient rule is used in every relabelled sector;
4. preserves common-left `SL(2,C)` gauge covariance because both the support and `Q` are functions only of relative elements;
5. preserves the true spin-network boundary object and linearity in `Psi` because `Q^n` is a scalar tangential multiplier of the already-authorized `F_SU2(y;Psi)`;
6. preserves relabeling covariance because `Q` is fully `S_5` invariant;
7. has transverse scaling degree `12` in the added `delta_N` term, since multiplication by a smooth tangential function does not alter transverse scaling degree. Adding it to an extension of scaling degree `20` remains in the same maximal scaling-degree class.

This already proves an infinite-dimensional source-compatible subspace without using the higher normal derivatives through order 8; those can only enlarge the raw mathematical extension space before extra conditions.

## Adversarial checks

- The result is not obtained from a scalar K4/K5 surrogate; it uses the actual `N`, actual compact boundary functional and exact source gauge action frozen in Iter077M.
- It is not a statement that every smooth coefficient is physical. It states that the constraints already present in CRQN v0.2 do not reduce the displayed invariant family.
- Full permutation invariance of `Q` prevents the result from depending on a post-hoc selected wedge.
- Compactness of `N` prevents growth of `Q^n` from introducing a tangential infinity for any fixed `n`.
- The theorem does not use the nonterminal Iter078O control workflow and cannot conflict with its future verdict.

## Scientific consequence

The constant coefficient `c` exhibited in Iter077M is only one direction in a much larger ambiguity. Under the source-backed constraints currently available, the local K5 extension problem is not a one-counterterm problem: it contains at least a countably infinite-dimensional smooth tangential subspace already at normal-derivative order zero.

A predictive continuation therefore requires an independently motivated new principle that restricts a function space (for example a genuinely source-derived composition/renormalization/covariance condition), not merely a fitted scalar finite part. No such new selector is introduced here.