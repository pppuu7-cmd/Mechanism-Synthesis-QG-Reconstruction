# Iter083J source lock — Q-polar decomposition and universal product factorization

Date: 2026-09-15
Status: FRAMEWORK SOURCE LOCK, NOT LORENTZIAN K5 PHYSICAL AUTHORITY

## Primary mathematical source
Nguyen Viet Dang and Bin Zhang, “Renormalization of Feynman amplitudes on manifolds by spectral zeta regularization and blow-ups”, Journal of the European Mathematical Society 23 (2021), 503–556, DOI 10.4171/JEMS/1016.

Exact framework facts used:

1. In the definition of polar germs, numerator variables are required to be orthogonal to the pole linear forms with respect to the dual quadratic form Q* induced by the fixed regulator-space quadratic form Q.
2. Proposition 6.7 constructs the projection pi_p onto holomorphic germs along the polar-germ subspace.
3. Remark 6.8 states that the polar-germ subspace, hence the projection pi_p, is determined by the chosen quadratic form Q; the paper then fixes the standard Euclidean quadratic form on regulator parameter space.
4. Lemma 7.2 proves the tensor-product factorization identity

`pi_(p1+p2)(t1 tensor t2) = pi_p1(t1) tensor pi_p2(t2)`

for independent tensor-product meromorphic distributions with separate regulator blocks.

The theorem in Iter083J does not claim that Dang–Zhang themselves consider a non-Euclidean Q-family. It asks the converse structural question: if one generalizes the polar-germ construction to arbitrary nondegenerate Q while demanding the same universal tensor-product factorization, what Q are allowed?

## Exact algebraic consequence tested
For distinct regulator coordinates i,j, take a pure simple pole `1/x_i` and an independent holomorphic factor `x_j`. Decompose

`e_j^* = c_ij e_i^* + ell_perp`

with `Q*(e_i^*,ell_perp)=0`. Then

`c_ij=Q*(e_i^*,e_j^*)/Q*(e_i^*,e_i^*)`

and

`x_j/x_i = c_ij + ell_perp/x_i`.

The second term is polar by the source definition; therefore the holomorphic projection of `x_j/x_i` is the constant `c_ij`.

Universal product factorization requires that projection to equal

`pi(1/x_i) x_j = 0`,

so it forces `Q*(e_i^*,e_j^*)=0` for every independent coordinate pair covered by the universal axiom.

## MSQGR scope firewall
The published causal K5 vertex is a connected product of ten Toller functions sharing group variables; it is not itself a tensor product of ten distributions on ten independent spacetime/group factors.

Therefore Iter083J may prove uniqueness **inside a universal product-factorizing regulator-projection family**, but it may not promote that naturality axiom to source-derived physical K5 authority without a separate bridge.

Iter083G and Iter083I remain valid in the broader S5-only class.

## Forbidden implications
- Do not equate tensor-product factorization with ordinary multiplication of connected K5 wedge functions.
- Do not infer that the connected Lorentzian K5 source automatically requires every regulator coordinate split to factorize.
- Do not use overall scaling of Q as a physical normalization parameter; polar orthogonality is unchanged by a common nonzero scalar.
- Do not infer a unique physical extension solely from uniqueness of Q inside this framework.