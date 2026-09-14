# Iter081F-SM prospective pre-gate — two-wedge causal branch-subset boundedness

Status: **CRITIC-AUTHORIZED PROSPECTIVE OBJECT; frozen before Researcher implementation/production.**
Date: 2026-09-14

## Scientific motivation

Iter081E is now Researcher-authoritative and independently `CONFIRMED_SCOPED`: an actual BCG `T^+` branch violates Han's projected contraction on the frozen pure-boost path, and the natural two-wedge `(+,+)` branch term violates Han's `d_j^2=4` face bound.

The most immediate source-motivated rescue is not another single branch. BCG gives `D=T^(+)+T^(-)`. Beltran's orientation construction recovers ordinary EPRL-KKL by summing wedge orientations, while a causal amplitude retains only orientation assignments satisfying the causal condition. Therefore cancellations among branch assignments are a genuine source-motivated possibility.

This gate asks a deliberately local necessary question: on the exact minimal two-wedge pure-boost control, can any **proper unit-weight subset** of the four branch assignments remove the near-identity singularity, or is boundedness restored only by the full branch sum that reconstructs the ordinary Wigner/EPRL object?

## Historical non-duplication audit

The old branch `research/iteration-023-causal-sector-sums` was inspected before this freeze.

Relevant historical objects:
- `causal/vertex_sigma_to_booster_masks.py` enumerates 16 correlated 4-simplex sign classes `kappa_ab=sigma_a sigma_b` and maps them to booster masks.
- `.github/workflows/causal-sector-sum-power.yml` runs numerical scans over `gamma={0.2,1.2,2.0}` and random seeds.
- `vertex/causal_sector_sum_power.py` constructs `Cplus16`, `Cminus16`, `Cboth32`, `EPRL`, and fixed-all-plus products on the **full ten-wedge magnetic-basis carrier**, then estimates collision slopes on generic cluster rays.
- Its own guardrail states that the power scan does not replace exact distributional `i epsilon` integration or boundary-intertwiner contraction.

That historical branch does **not** provide an equation-level symbolic theorem for the 15 nonempty subsets of the four two-wedge assignments from BCG Eq. (46), and therefore is not authoritative for the present gate. It may be cited only as prior sign-correlation/numerical motivation.

## Frozen source object

Primary source formula: Bianchi--Chen--Gamonal arXiv:2604.24945v1 Eq. (46), gamma-simple Toller matrices.

Freeze:
- `j=k=1/2`;
- arbitrary fixed finite real `rho>0`;
- pure boost `g_beta=exp(-i beta K_z)`;
- `beta>0`, one-sided limit `beta->0+`;
- both diagonal magnetic components `m=+1/2,-1/2`;
- branches `epsilon in {+,-}`.

For `epsilon1,epsilon2 in {+,-}`, define the exact two-wedge branch term

`tau_{epsilon1 epsilon2}(beta) := 2 sum_{m=±1/2} t_m^(epsilon1)(beta) t_m^(epsilon2)(beta)`.

The factor `2=d_j` is frozen to match the same natural two-wedge trace normalization used in Iter081E.

Do not import simplified Iter081C/D/E expressions as truth labels. Researcher implementation must reconstruct both plus and minus branch functions directly from the frozen source formula and verify all special-function reductions it uses.

## Frozen subset universe

Let

`B = {++, +-, -+, --}`.

For every nonempty subset `S subseteq B`, define the unit-weight sum

`Tau_S(beta) := sum_{b in S} tau_b(beta)`.

All `2^4-1 = 15` nonempty subsets must be tested. No post-result subset selection is allowed.

The full set is

`S_full = {++, +-, -+, --}`.

The implementation must independently verify the exact identity

`Tau_S_full = 2 sum_m [t_m^+ + t_m^-]^2`,

and then connect `[t_m^+ + t_m^-]` to the standard Wigner matrix only through the source identity `T^+ + T^- = D`.

## Frozen boundedness test

For every subset, determine the exact Laurent/one-sided asymptotic structure near `beta=0+` far enough to decide boundedness.

A subset is `BOUNDED_ON_FROZEN_PATH` only if all negative powers of beta cancel and the one-sided limit is finite.

A subset is `UNBOUNDED_ON_FROZEN_PATH` if an exact nonzero coefficient of any negative beta power survives.

If symbolic control cannot decide, classify that subset `INSUFFICIENT` rather than use a floating-point fit as authority.

## Mandatory controls

1. Derive `T^+` and `T^-` entries from BCG Eq. (46) or the exact source-related plus/minus formula, not from Critic exploratory coefficients.
2. Verify `T^+ + T^- = D` on the frozen matrix elements independently.
3. Verify the full four-assignment sum is the ordinary two-wedge projected Wigner/EPRL control and is compatible with Han's standard bounded object.
4. Enumerate all 15 nonempty subsets mechanically.
5. Use exact symbolic coefficients/limits for scientific classification.
6. Numerical values at several rational `rho` may be regression controls only.
7. Include a deliberately bounded full-sum control and a known unbounded single-branch control so the classifier can distinguish them.
8. Record the exact source/provenance chain and the old Iteration-023 audit above.

## Frozen classifications

### Strong local no-rescue result
`ITER081F_SM_TWO_WEDGE_UNIT_WEIGHT_PROPER_BRANCH_SUBSETS_ALL_UNBOUNDED_FULL_SUM_BOUNDED_EXACT_SCOPED`

Allowed only if:
- every one of the 14 proper nonempty subsets is proved `UNBOUNDED_ON_FROZEN_PATH`;
- the full four-assignment sum is proved `BOUNDED_ON_FROZEN_PATH`;
- the full sum is explicitly tied to `D=T^++T^-` and therefore to the standard Wigner/EPRL control.

### Proper-subset rescue exists
`ITER081F_SM_TWO_WEDGE_PROPER_UNIT_WEIGHT_BRANCH_SUBSET_BOUNDED_RESCUE_EXISTS_EXACT_SCOPED`

Allowed if at least one proper nonempty subset is exactly bounded on the frozen path. The exact subset(s) must be listed, but no global causal interpretation may be added unless independently source-derived.

### Insufficient
`ITER081F_SM_TWO_WEDGE_BRANCH_SUBSET_BOUNDEDNESS_INSUFFICIENT_SCOPED`

Use if exact symbolic control fails for one or more subsets needed to distinguish the above outcomes.

### Invalid
`INVALID_IMPLEMENTATION_OR_PROVENANCE`

Use for source mismatch, preassigned subset outcomes, incomplete subset enumeration, posthoc criterion change, numerical-only promotion, or use of the old Iteration-023 numerical scan as a substitute for the exact frozen object.

## Claim ceiling

Even the strong no-rescue classification is only a theorem about this **minimal two-wedge, minimal-spin, identical-pure-boost, unit-weight subset universe**.

It does **not** prove:
- Beltran's global causal `A^+` diverges;
- every causal vertex/face is unbounded;
- correlated full-vertex orientation constraints cannot cancel singularities;
- arbitrary complex or geometry-dependent branch weights cannot help;
- subtraction, renormalization or a new causal face functional is impossible;
- a joint-K5 extension selector exists or fails;
- E3/E4/E6 composition, regulator independence, G3, F9/G8, RG/E9 or complete QG.

The scientific value is narrower: it tests whether the most elementary **unit-weight partial branch-sum** rescue can restore the exact Han-type boundedness already lost in Iter081E without summing all branches back to the ordinary EPRL object.

## Authorized Researcher action

Automation A may implement and run this exact gate prospectively. Critic must review the terminal result before any promotion to a causal face-functional claim.