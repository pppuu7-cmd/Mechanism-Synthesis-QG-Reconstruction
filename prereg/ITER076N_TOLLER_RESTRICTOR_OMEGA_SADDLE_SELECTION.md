# Iter076N preregistration — does the exact Toller restrictor select an Omega sector on the Lorentzian saddle locus?

Date: 2026-09-13

## Purpose

Iter076M establishes that the exact causal-vertex variable set `(g_a,sigma_a)` admits a non-degenerate global orientation pseudoscalar

`Omega_sigma(g) = sgn Delta_sigma(g)`,

`Delta_sigma(g)=det([1; sigma_a F_a])`, `F_a=ghat_a T`,

with the required gauge/relabeling/global-reversal behavior. Iter076M explicitly leaves physical signed P3 blocked because availability of a function is weaker than evidence that the amplitude selects its sign.

The newly frozen source snapshot `sources/CAUSAL_SPINFOAM_VERTEX_2026_TOLLER_RESTRICTOR_SADDLE_ORIENTATION_SNAPSHOT.md` records a stronger amplitude fact: the exact coherent-spinor Toller integrand contains a causal Heaviside restrictor, and on non-degenerate Lorentzian Regge critical data that exact restrictor admits only one of the two EPRL saddles. The two Lorentzian EPRL critical solutions are parity-related.

This prospective gate tests whether those facts provide amplitude-selection provenance for **one sign of the Iter076M orientation pseudoscalar on the non-degenerate Lorentzian Regge saddle locus**, while keeping finite-spin off-saddle P3 blocked.

No production output for Iter076N exists at preregistration time. Frozen criteria below may not be changed after viewing results.

## Source authority and scope

Use only:
- `sources/CAUSAL_SPINFOAM_VERTEX_2026_SOURCE_SNAPSHOT.md`;
- `sources/CAUSAL_SPINFOAM_VERTEX_2026_REGGE_ORIENTATION_SUPPLEMENT.md`;
- `sources/CAUSAL_SPINFOAM_VERTEX_2026_TOLLER_RESTRICTOR_SADDLE_ORIENTATION_SNAPSHOT.md`;
- durable Iter076M result for the definition and covariance of `Omega_sigma`.

Exact source facts:
- `kappa_ab=sigma_a sigma_b`;
- Eq.(17)/(36) restrictor `theta(kappa_ab B_ab)+kappa_ab delta^(rho,j)(B_ab)`;
- `B(z,g)=log(<g^dagger z|g^dagger z>/<z|z>)`;
- the delta term has support at `B=0`.

Critical-locus facts:
- non-degenerate Lorentzian data have `beta_ab>0`;
- `B_ab^(+/-)=+/- s_a s_b beta_ab`, with one global `+/-`;
- the causal source selects the `+` saddle exactly when `sigma_a sigma_b=s_a s_b` for every wedge and excludes the `-` saddle;
- the two non-degenerate Lorentzian EPRL critical solutions are parity-related.

The exact restrictor must not be re-described as an exact off-saddle function of `Omega_sigma` unless such an identity is independently derived. That is outside this gate.

## Frozen lanes

### Lane A — exact restrictor provenance lock

Verify the committed source snapshot contains all of the following exact-level ingredients without substituting a surrogate:
1. `kappa_ab=sigma_a sigma_b`;
2. `theta(kappa_ab * B) + kappa_ab * delta^(rho,j)(B)`;
3. `B=log(<g^dagger z|g^dagger z>/<z|z>)`;
4. boundary support of the distributional term at `B=0`.

PASS iff all four source locks are present. Any replacement by `beta+i*epsilon`, an inserted Levi-Civita sign, or an ad hoc projector is FAIL.

### Lane B — exhaustive K5 causal-saddle sign census

Enumerate all five-edge signs `s_a in {+/-1}` except the all-equal assignments, which cannot represent a finite non-degenerate Lorentzian 4-simplex satisfying normal closure. Enumerate all `sigma_a in {+/-1}`.

For all ten wedges set the sign of `beta_ab` to positive and evaluate the restrictor arguments at the two source critical branches:

`kappa_ab B_ab^(+) ~ (sigma_a sigma_b)(s_a s_b)`,

`kappa_ab B_ab^(-) ~ -(sigma_a sigma_b)(s_a s_b)`.

PASS iff:
- for every compatible pair satisfying `sigma_a sigma_b=s_a s_b` on all wedges, all ten `+` arguments are positive and all ten `-` arguments are negative;
- every incompatible pair rejects the `+` branch on at least one wedge;
- no assignment of source-factorizable `kappa_ab=sigma_a sigma_b` makes all ten `-` arguments positive.

Record exact counts.

### Lane C — parity-to-Omega bridge

Use the exact Iter076M affine determinant definition on a deterministic non-degenerate set of five future timelike vectors. Exhaust all `32` source `sigma` assignments.

Apply a genuine spacetime parity reflection with determinant `-1` and verify:
1. `Delta_sigma(PF)=-Delta_sigma(F)` for every assignment;
2. `Omega_sigma(PF)=-Omega_sigma(F)` wherever nonzero;
3. global causal reversal leaves the selector invariant: `Omega_{-sigma}(F)=Omega_sigma(F)`;
4. no tested control is degenerate.

Together with the frozen source theorem that the two Lorentzian critical points are parity-related, PASS means the two source critical branches occupy opposite `Omega` sectors.

### Lane D — scope/firewall controls

Construct an explicitly degenerate control by making two weighted affine columns dependent. Verify `Delta_sigma=0` and do not assign `Omega_sigma` there.

PASS iff the aggregate records all of the following as hard locks:
- `selected_scope = NONDEGENERATE_LORENTZIAN_REGGE_SADDLE_LOCUS`;
- exact Toller restrictor is finite-spin source structure;
- identification of its selected branch with an `Omega` sign is saddle/parity reconstruction only;
- finite-spin generic off-saddle signed P3 is **not** promoted;
- degenerate, Euclidean and vector-geometry sectors are not promoted by this gate;
- nominal `epsilon^-1` coefficient remains unestablished.

## Frozen interpretation

If A-D all pass, classify:

`ITER076N_EXACT_TOLLER_RESTRICTOR_SELECTS_ONE_OMEGA_SECTOR_ON_NONDEGENERATE_LORENTZIAN_REGGE_SADDLE_LOCUS_SCOPED`

Meaning: the exact causal Toller amplitude supplies genuine amplitude-selection provenance for one member of the parity-related orientation pair on the non-degenerate Lorentzian Regge saddle locus. Combined with Iter076M, the selected saddle has a definite `Omega_sigma` sign, so the earlier global-sign ambiguity of the Hodge line is resolved **on that saddle locus**.

This does not establish an exact finite-spin off-saddle signed source-to-K4 pushforward P3.

If the exact restrictor locks fail, classify:
`ITER076N_SOURCE_RESTRICTOR_PROVENANCE_FAIL`.

If the causal sign census fails, classify:
`ITER076N_CAUSAL_SADDLE_SELECTION_FAIL`.

If parity does not flip the Iter076M selector, classify:
`ITER076N_PARITY_OMEGA_BRIDGE_FAIL`.

Technical/runtime errors are `INFRASTRUCTURE_OR_NUMERICAL_FAIL`, not scientific FAIL.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no generic finite-spin signed P3; no nominal `epsilon^-1` coefficient; no physical causal-vertex finiteness/divergence theorem; no F9/G3/G8/K5 promotion; no physical-sector theorem outside the explicitly frozen non-degenerate Lorentzian Regge saddle locus.
