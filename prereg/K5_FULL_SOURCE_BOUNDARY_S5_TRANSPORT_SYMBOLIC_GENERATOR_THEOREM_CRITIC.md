# K5 full-source boundary S5 symbolic theorem — independent Critic preregistration

Date: 2026-09-17
Role: independent adversarial Critic

## Target authority
Researcher prereg `4f65cff503db976b6ff52b8519e5fdaa0bf4a4f8`, control repair `73b8f65f05e3945e8c4d517e73b938cdd3299e39`, authoritative production run `35200455308`, Researcher classification `K5_FULL_SOURCE_BOUNDARY_S5_SYMBOLIC_ALL_ALPHA_TRIVIAL_CHARACTER_EXACT_SCOPED`.

## Frozen question
Independently decide whether, for the complete unprojected order-zero all-j=1/2 K5 source boundary Wick covector, simultaneous Schwinger/source/boundary permutation obeys the exact coefficient-level contragredient law

`a_p(p alpha) = A_p^(-T) a(alpha)`

for all `p in S5` on the formal domain `Psi_K5 != 0`, with trivial residual character, and whether the Researcher proof contains no witness interpolation, fitted character, fitted channel matrix, or hidden post-output convention.

## Frozen independent reconstruction requirements
1. Reconstruct the ten canonical K5 edges and all 125 coefficient-one spanning-tree monomials of `Psi_K5`; independently verify C/T invariance.
2. Reconstruct the exact 32-dimensional boundary action for generators C=(1,2,3,4,0), T=(1,0,2,3,4); verify C,T generate 120 elements and exact representation composition/inverses.
3. Reconstruct orientation-sensitive edge transport independently, including endpoint transpose `(row,col)->(col,row)` and source reversal sign for canonically reversed edges.
4. Reconstruct complete order-zero source/boundary coefficient dictionaries over all 32 components and exactly 100000 original source node-choice terms; compare transported dictionaries coefficient-by-coefficient for C and T. No numerical Schwinger witnesses or interpolation may substitute for this.
5. Independently verify formal covariance-numerator transport and the factorization of orientation character on every complete Wick monomial: source reversal contribution `g_source=prod_e s_e`, covariance pullback contribution `g_cov=prod_e s_e`, hence `g_source*g_cov=1` because all ten edges occur exactly once.
6. Required malformed odd-T controls must fail separately when omitting endpoint transpose, source reversal sign, covariance orientation sign, or when inserting an extra permutation-sign character. The historical source-fixed diagnostic object must remain a rejected control.
7. Audit executed code for forbidden finite-witness interpolation, floating tolerance, fitted phase/character, fitted 2x2 channel matrix, adaptive support, or post-hoc convention changes.

## Frozen classifications
- `CONFIRMED_EXACT_SCOPED`: all independent reconstructions and required malformed controls pass/fail as prescribed and the all-alpha rational identity follows at coefficient level on `Psi_K5 != 0`.
- `REFUTED_EXACT_SCOPED`: an exact coefficient-level counterexample to the frozen identity is produced with a machine-readable witness.
- `BLOCKED`: independent reconstruction cannot be completed without missing source authority or required data; identify the exact missing dependency.
- `INVALID_IMPLEMENTATION`: Critic executable fails to implement this frozen contract; no scientific verdict.

## Interpretation ceiling
Even `CONFIRMED_EXACT_SCOPED` establishes only coefficient-level S5 transport authority for this formal source/boundary object. It does not resolve the already-frozen physical leading-coefficient cancellation gate, does not establish global Stokes/IBP, K5 periods, a physical finite-part selector, F9/G3/G8, regulator independence, or new physics.

Frozen before Critic implementation or Critic output. Do not alter these criteria after output is visible.
