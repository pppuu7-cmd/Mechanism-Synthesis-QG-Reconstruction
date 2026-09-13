# Iteration 069B preregistration — held-out K4 joint-spectral ray validation

Date: 2026-09-13

This gate is frozen **before implementation and production** and is independent of the symbolic output of Iter069A.

## Question

Does the reduced source-backed K4 joint-spectral rational family exhibit the same generic polynomial growth on a new exact held-out matrix of physical causal classes, tree bases, source nuisance points, and nondegenerate radial directions?

## Frozen source cases

Two new exact held-out cases:

- `H6`: gamma=`37/100`, epsilon=`41/1000`, external K4 flow `k=(17/100,-29/100,21/100,-9/100)`.
- `H7`: gamma=`173/100`, epsilon=`137/1000`, external K4 flow `k=(-26/100,34/100,-11/100,3/100)`.

Both flows sum exactly to zero.

## Frozen physical causal classes

Use the eight edge-orientation classes represented by

`sigma=(+,sigma1,sigma2,sigma3)`

and derive the six denominator signs in edge order `01,02,03,12,13,23` as

`kappa_ab=sigma_a*sigma_b`.

Sigma labels:

`++++, +++-, ++-+, ++--, +-++, +-+-, +--+, +---`.

No sign pattern is fitted or selected after output.

## Frozen tree bases and directions

Tree/cycle bases:

`S0, S1, P0, P1`.

Primitive cycle directions:

- `V1=(1,2,3)`
- `V2=(2,-1,3)`
- `V3=(3,1,-2)`

For every lane, the implementation must derive all six edge slopes from the exact incidence solve and fail closed if any slope vanishes.

## Frozen matrix

`2 cases x 8 sigma classes x 4 trees x 3 directions = 192 exact lanes`.

For each lane substitute `y=lambda*v` into both the source kernel and the F=1 no-contact denominator control, cancel exactly as rational functions of real `lambda`, and record:

- source numerator/denominator degrees and net degree;
- control numerator/denominator degrees and net degree;
- exact source/control leading coefficients;
- exact six edge slopes;
- causal sign vector derived from sigma.

## Frozen predicates

Every lane must satisfy:

1. all six edge slopes are nonzero;
2. source net radial degree is exactly `+6`;
3. no-contact control net radial degree is exactly `-6`;
4. source leading coefficient is nonzero;
5. control leading coefficient is nonzero.

Aggregate-only predicate:

6. for each fixed `(case,tree,direction)`, the exact source leading coefficient is identical across all eight physical causal sigma classes.

## Frozen classification

All 192 lanes and aggregate predicates pass:

`ITER069B_K4_JOINT_SPECTRAL_HELDOUT_GENERIC_GROWTH_PLUS6_CAUSAL_SIGN_INDEPENDENT`

Otherwise:

`ITER069B_HELDOUT_ASYMPTOTIC_REVIEW`.

## Scope locks

This validates only generic radial asymptotics of the reduced source-backed joint-spectral rational family. It does not define a multivariate boundary value, does not prove a full Toller or causal-vertex divergence theorem, and does not authorize a sequential finite part, preferred tree/order, counterterm, K5, G3, F9, or G8 promotion.
