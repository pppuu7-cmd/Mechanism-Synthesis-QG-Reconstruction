# Iter081G Critic exact K5 causal cycle-space identity

Date: 2026-09-14
Status: **EXACT SOURCE-COMBINATORIAL IDENTITY; NO ACTUAL-K5 SINGULARITY VERDICT**

## Source input
For a five-valent K5 vertex, Beltran `arXiv:2603.22661v2` Eq. (8) gives causal wedge signs

`epsilon_ab = eta sigma_a sigma_b`,

with `sigma_a in {+1,-1}`. Global reversal of all `sigma_a` leaves the wedge assignment unchanged, giving 16 assignments for each fixed `eta`.

Beltran Eq. (26) realizes a complete orientation assignment by a product of Toller matrices over all wedges. Eq. (36) sums the globally admissible `eta=+1` assignments.

This note studies only the exact discrete branch-sum algebra before group integration and before boundary contraction.

## Algebraic variables
For every K5 wedge/edge `e=(ab)`, write its two branch factors abstractly as

`x_e := T_e^(+)`,
`y_e := T_e^(-)`.

Define

`a_e := (x_e+y_e)/2`,
`b_e := (x_e-y_e)/2`.

Then for `eta=+1`,

`t_e^(sigma_a sigma_b) = a_e + b_e sigma_a sigma_b`.

The source identity `T^+ + T^- = D` implies `a_e=D_e/2`; no representation law is assumed for `b_e`.

## Exact eta=+1 causal sum
Gauge the global reversal by fixing `sigma_1=+1` and define

`C_+ := sum_{sigma_2,...,sigma_5=+-1} prod_{e=(ab) in E(K5)} (a_e+b_e sigma_a sigma_b)`.

Expanding in edge subsets `S subseteq E(K5)` gives a spin monomial

`prod_v sigma_v^(deg_S(v))`.

Summation over the four free vertex signs kills the term unless every vertex has even degree in `S`. (If vertices 2--5 have even degree, the handshaking parity lemma forces vertex 1 even as well.) Therefore

`C_+ = 16 * sum_{S in Z_1(K5;F2)} [ prod_{e in S} b_e ] [ prod_{e notin S} a_e ]`,

where `Z_1(K5;F2)` is the binary cycle space, equivalently the set of Eulerian/even-degree spanning subgraphs of K5.

Since K5 is connected with `|E|=10`, `|V|=5`, its cycle-space dimension is

`10-5+1=6`,

so the causal sum contains exactly `2^6=64` Eulerian-subgraph channels.

This is an exact identity, not a numerical power-counting observation.

## eta=-1 sector
For `eta=-1`, each wedge sign is reversed, so

`a_e+b_e sigma_a sigma_b -> a_e-b_e sigma_a sigma_b`.

Hence

`C_- = 16 * sum_{S in Z_1(K5;F2)} (-1)^|S| [ prod_{e in S} b_e ] [ prod_{e notin S} a_e ]`.

Thus the sum of both causal signature sectors is

`C_+ + C_- = 32 * sum_{S Eulerian, |S| even} [prod_{e in S} b_e][prod_{e notin S} a_e]`.

It still contains nontrivial cycle-space channels in general.

## Comparison with the unrestricted EPRL branch sum
Summing independently over all `2^10` wedge branch assignments instead gives

`C_all = prod_e (x_e+y_e) = prod_e D_e = 2^10 prod_e a_e`.

Therefore the unrestricted sum projects onto the empty `b`-subgraph only, whereas Beltran's globally causal sector sum projects onto the K5 cycle space.

This makes precise why `causal sum` and `full branch sum restoring EPRL` are different operations.

## Important structural observation
The full K5 edge set itself is Eulerian because every K5 vertex has degree 4. Therefore `C_+` contains the all-edge channel

`16 prod_{e in E(K5)} b_e`.

The same channel also survives `C_+ + C_-` because `|E(K5)|=10` is even.

This observation is purely algebraic. It is **not yet** a physical singularity theorem: a future test must use actual source-ordered Toller matrix entries on a realizable K5 group-incidence path and then perform the required boundary contraction. No arbitrary independent wedge values may be promoted to a K5 configuration.

## Relation to historical Iteration 023
Historical `research/iteration-023-causal-sector-sums` numerically sums the 16 factorized K5 sign classes and their co-causal partners on the full ten-wedge magnetic carrier. The exact cycle-space decomposition above was not found as a durable theorem in the current repository search and is strictly stronger at the discrete branch-combinatorics level, while remaining weaker than a full source-ordered amplitude theorem.

## Consequence for the research front
A source-faithful causal rescue cannot be assessed only by local proper subsets. The globally causal K5 sum has a fixed cycle-space structure. The next physically stronger gate should test whether the nonempty Eulerian `b`-channels, especially the all-edge channel, survive on an **actual K5 incidence path and full frozen boundary contraction**.

## Claim lock
No claim is made here that Beltran `A_v^+` diverges, that the all-edge channel is nonzero after boundary contraction, that no cancellation occurs among matrix/boundary components, or that the joint K5 distributional extension is selected or obstructed. Those require a prospectively frozen source-ordered K5 gate.
