# Iter081Y-SM prereg — invariant counterterm geometry on K3/K4/K5 collision strata

Status: **PROSPECTIVE CRITIC GEOMETRY GATE — CONDITIONAL ON PHYSICAL STRATUM NONVANISHING**
Date: 2026-09-14

## Motivation
Iter081R classifies scalar invariant normal jets at the deepest K5 compact collision and finds a finite 28-dimensional lower bound because, after exact node-wise compact gauge quotient, no noncompact external normal variables remain along the deepest stratum.

A stratified forest treatment introduces partial collision blocks. Their supported counterterm coefficients may vary along external tangential directions. Before any selector claim, classify this geometry exactly.

## Frozen block geometry
For a connected collision block `B` of size `k=3,4,5` in the linearized five-node boost configuration modulo common translation:

- normal fiber to `Delta_B`:
  `V_k = spin1_SO(3) tensor Std_k_Sk`, dimension `3(k-1)`;
- j=1/2 leading scaling degree from internal edges:
  `sd_k = 2*C(k,2)=k(k-1)`;
- superficial normal derivative allowance:
  `omega_k = sd_k - 3(k-1)=(k-1)(k-3)`;
- external tangential normal-space dimension after collapsing B:
  `t_k = 12-3(k-1)=3(5-k)`.

Thus:
- k=3: `sd=6`, codim=6, `omega=0`, `t=6`;
- k=4: `sd=12`, codim=9, `omega=3`, `t=3`;
- k=5: `sd=20`, codim=12, `omega=8`, `t=0`.

## Frozen invariant normal-jet count
For each k, count

`d_n^(k)=dim Sym^n(V_k)^(SO(3) x S_k)`

for `0<=n<=omega_k`, using the same exact character/Molien method as Iter081R.

Prospective controls:
- k=3 must give only `d_0=1` because `omega=0`;
- k=4 must independently determine `d_0..d_3` and verify a unique quadratic metric invariant exists;
- k=5 must reproduce Iter081R `[1,0,1,0,3,0,7,0,16]`.

## Tangential coefficient-space question
This gate classifies geometry only. For a supported distribution on `Delta_B`, each allowed invariant normal jet may be multiplied by a coefficient distribution/function along the quotient stratum.

Determine the residual source-symmetry action on the external tangential boost variables after internal compact gauge quotient:

- k=4: one external node relative to the collapsed 4-block, represented by `Y in R^3`, modulo diagonal SO(3), so scalar invariant coefficient functions may depend on `|Y|^2` away from deeper collision `Y=0`;
- k=3: two external nodes relative to the collapsed 3-block, represented by `(Y_4,Y_5) in (R^3)^2`, modulo diagonal SO(3) and exchange of the two external singleton labels, so scalar invariant coefficient functions may depend on smooth symmetric combinations of `|Y_4|^2`, `|Y_5|^2`, `Y_4·Y_5` away from their own deeper diagonals.

Show explicitly that these invariant function spaces are infinite-dimensional as smooth function spaces by exhibiting polynomial families, while keeping the statement **conditional**: such coefficient freedom is physically relevant only if the fully boundary-contracted source amplitude actually requires extension on the corresponding k=3/k=4 stratum.

## Frozen classifications
- `ITER081Y_SM_PARTIAL_STRATA_HAVE_FINITE_INVARIANT_NORMAL_JET_TYPES_BUT_FUNCTION_VALUED_EXTERNAL_TANGENTIAL_COEFFICIENT_SPACES_EXACT_GEOMETRY_SCOPED` if the normal-jet counts and residual tangential quotient are exact and nonconstant invariant coefficient families exist for k=3,4.
- `INVALID_OBJECT_DEFINITION` for geometry/representation/counting failure.

## Claim ceiling
This gate does NOT prove physical k=3/k=4 non-L1 behavior after full boundary contraction. It does not say those function-valued counterterms are actually needed in the source amplitude. It classifies the allowed geometry **if** a partial-stratum extension is required. Only k=5 non-L1 survival is currently exact boundary-complete (Iter077I). No selector, renormalization scheme, regulator independence, G3/F9/G8/K5, new physics or complete-QG claim follows.
