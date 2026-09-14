# Iter081Z Critic exploratory exact control — nested K3/K4 boundary-contraction witnesses

Date: 2026-09-14
Status: **EXACT CRITIC EXPLORATORY CONTROL, NOT PROSPECTIVELY FROZEN SCIENTIFIC GATE**

## Provenance warning
This calculation was explored before a dedicated preregistration was committed. It is therefore not promoted as an authoritative terminal scientific gate. It is a concrete adversarial hypothesis for independent prospectively frozen reproduction by Researcher A or a successor gate.

## Source-leading input
Use exactly the all-`j=1/2` source-leading Toller matrix from authoritative Iter077I, stripped only by common nonzero scalar/denominator factors:

`M(v) = [[v_z, -v_x-i v_y],[-v_x+i v_y,-v_z]]`.

The full wedge leading factor is a nonzero scalar times `M(v)/|v|^3`, hence homogeneous degree `-2` in the relative boost vector `v`.

Use exactly Iter077I's five-node SU(2)-invariant intertwiner basis tensors and exact Gaussian-integer contraction rules.

## K4 nested witness
Take a four-node collision cluster `B={0,1,2,3}` with internal directions

`a_0=(0,0,0)`,
`a_1=(1,2,3)`,
`a_2=(2,3,5)`,
`a_3=(3,5,7)`,

and an external fifth-node direction

`b=(5,7,11)`.

Consider the nested scaling

`X_i=r a_i`, `i=0,1,2,3`,
`X_4=s b`,

with `r/s ->0` and then `s->0+`.

At leading order in `r/s`:

- six internal K4 edge numerators use `M(a_i-a_j)`;
- four cross-edge numerators use the common nonzero matrix `M(-b)`.

All denominator directions are nonzero.

Exact Iter077I-style Gaussian-integer contraction of this ten-edge nested leading tensor gives **32/32 nonzero boundary basis components**.

For the first basis component `(0,0,0,0,0)`, the stripped exact contraction is

`-775101600`.

Thus the nested coefficient is certainly nonzero.

### Partial-stratum implication
For fixed sufficiently small `s>0`, first take `r->0`. The source-ordered fully boundary-contracted coefficient of the K4 internal singularity is an ordinary off-collision function `C_4(s)` of the external configuration, built from the six internal leading matrices and the exact finite Toller matrices on the four cross edges.

The BCG source small-boost asymptotics imply

`C_4(s) = c_4 s^-8 + lower nested order`,

where `c_4` is precisely the nonzero nested contraction above (times nonzero source scalar/direction factors). Therefore `C_4(s)` is not identically zero; for sufficiently small fixed nonzero `s` there exist actual partial-K4 configurations with `C_4(s)!=0`.

The internal K4 singularity then has

`q_4=-12`, `d_4=9`, `q_4+d_4=-3`,

so that fully boundary-contracted partial stratum is not locally absolutely L1 for those configurations.

## K3 nested witness
Take `B={0,1,2}` with

`a_0=(0,0,0)`, `a_1=(1,2,3)`, `a_2=(2,3,5)`,

and two external directions

`b_3=(3,5,7)`, `b_4=(5,7,11)`.

Use

`X_i=r a_i`, `i=0,1,2`,
`X_3=s b_3`, `X_4=s b_4`,

with `r/s->0`, then `s->0+`.

At nested leading order:

- three internal K3 edges use `M(a_i-a_j)`;
- three edges from the cluster to node 3 use `M(-b_3)`;
- three edges from the cluster to node 4 use `M(-b_4)`;
- edge `(3,4)` uses `M(b_3-b_4)`.

All directions are nonzero.

Exact Gaussian-integer contraction gives **24/32 nonzero boundary basis components** for this witness.

For boundary component `(0,0,0,0,0)`, the stripped contraction is

`-962813280`.

Therefore at least one, indeed at least 24, boundary components have a nonzero nested coefficient.

For fixed sufficiently small external scale/configuration, the partial-K3 coefficient function has asymptotic

`C_3(s)=c_3 s^-14 + lower nested order`, `c_3!=0`

for those components. Hence it is not identically zero and is nonzero at some actual fixed external configurations.

The internal K3 singularity has

`q_3=-6`, `d_3=6`, `q_3+d_3=0`,

so it is logarithmically non-L1 when this coefficient is nonzero.

## Causal branch transport
At the nested all-edge leading level each branch flip multiplies the corresponding `M` factor by `-1`. For every proper causal K5 assignment `epsilon_ab=eta sigma_a sigma_b`, the product over ten branch signs is `+1`. Therefore the nested leading coefficients above are the same for all proper causal assignments at the final `s->0` leading order. This is only a nested-leading sign statement; the exact finite-s partial coefficient functions can differ between assignments away from the deeper collision.

## Scientific hypothesis generated
If independently reproduced prospectively, these witnesses would upgrade the forest picture from carrier power counting to actual fully boundary-contracted source-ordered partial-stratum results:

- K4: non-L1 partial collision exists for all 32 boundary basis components in the exhibited nested family;
- K3: logarithmic partial collision exists for at least 24/32 components in the exhibited nested family.

They would establish that a global K5 extension really does require subdivergence treatment before the deepest K5 extension, rather than this being only a carrier-level precaution.

## Claim ceiling
Because this was not prospectively frozen, do not cite it as final authoritative proof. It does not classify all K3/K4 boundary components, all external configurations, generic spin, or all strata; it does not define a forest subtraction or selector. It is an exact control/hypothesis for independent reproduction.
