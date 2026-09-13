# Iter076N terminal result — exact Toller restrictor selects one Omega sector on the non-degenerate Lorentzian Regge saddle locus

Date: 2026-09-13

## Authority

- exact Toller-restrictor / saddle-orientation source snapshot: `cf9b1182a7f6f0b996b69aa78a0d58e7276eac96`
- frozen preregistration: `eb4f6f655b8bfeb872d6e5b945308d0c2887f9a9`
- implementation: `8e47c093ce54ea511f54bbd9b0864426508c0c42`
- production/workflow head: `b3dc5e64b5aa706c8c836d366859017d8a913c57`
- authoritative run: `34781543192` (`success`)
- aggregate job: `103789370946`
- aggregate artifact: `10324993593`
- aggregate artifact ZIP digest: `sha256:6fd653c302afc865c33296b1f540d3f9a7cc92ae48424f207ddb6a63ae22ef30`

Raw lane artifacts consumed by the aggregate job:
- A: job `103789350486`, artifact `10325586980`, digest `sha256:d0728c8938e12c30eb93c7fe15430b20aeedb3a69f62ca89bb7090b960c83b5f`
- B: job `103789350370`, artifact `10324444566`, digest `sha256:54402579956fe16ff8ca712cc7f00fb4fcae1736a39f807c99a2ab0c48b67ba5`
- C: job `103789350454`, artifact `10325296861`, digest `sha256:346473d7f6f1f3daeb6234396719d18dcc1b529d24655d07992e40fc08b8bea7`
- D: job `103789350461`, artifact `10324589073`, digest `sha256:d9073b019783caa57e47b394d112d677439938e94b6d64d79a3ddf3c4455d008`

## Frozen scientific classification

`ITER076N_EXACT_TOLLER_RESTRICTOR_SELECTS_ONE_OMEGA_SECTOR_ON_NONDEGENERATE_LORENTZIAN_REGGE_SADDLE_LOCUS_SCOPED`

All four prospectively frozen lanes pass and the aggregate output is `valid=true`.

## Terminal facts

### Lane A — exact amplitude provenance

The committed source locks pass without a surrogate or inserted projector. The source-level coherent-spinor Toller structure contains:

- source factorization `kappa_ab=sigma_a sigma_b`;
- the exact restriction `theta(kappa_ab B)+kappa_ab delta^(rho,j)(B)`;
- the exact source definition `B(z,g)=log(<g^dagger z|g^dagger z>/<z|z>)`;
- distributional support at `B=0`.

No `beta+i*epsilon` replacement and no inserted Levi-Civita projector were used.

### Lane B — exhaustive K5 causal-saddle census

The frozen census covers all `30` non-all-equal Regge causal-sign assignments and all `32` source `sigma` assignments, for `960` pairs total.

Exact counts:
- causal-compatible pairs: `60`;
- incompatible pairs: `900`;
- `+` critical branch admitted pairs: `60`;
- `-` critical branch admitted pairs: `0`;
- compatible `+` wedge checks positive: `600/600`;
- compatible `-` wedge checks negative: `600/600`;
- incompatible pairs rejecting the `+` branch on at least one wedge: `900/900`.

Thus source-factorizable causal wedge signs admit precisely the causal-compatible `+` critical branch and never the global `-` branch on the frozen non-degenerate Lorentzian saddle locus.

### Lane C — parity to Omega

For a deterministic exact-rational non-degenerate control family, all `32/32` source causal assignments remain non-degenerate. A genuine parity transformation with determinant `-1` gives

`Delta_sigma(PF) = -Delta_sigma(F)`

for `32/32` assignments, hence flips `Omega_sigma` in `32/32`. Global causal reversal leaves the selector invariant in `32/32` cases. The source lock that the two non-degenerate Lorentzian EPRL critical points are parity-related also passes.

Therefore the two parity-related Lorentzian critical branches lie in opposite `Omega_sigma` sectors.

### Lane D — scope firewall

The explicit degenerate control gives `Delta_sigma=0`, and `Omega_sigma` is left undefined rather than fitted or regularized.

The terminal scope is exactly:

`NONDEGENERATE_LORENTZIAN_REGGE_SADDLE_LOCUS`.

The result explicitly does not promote:
- generic finite-spin off-saddle signed P3;
- the degenerate sector;
- Euclidean critical geometry;
- vector geometry;
- the nominal `epsilon^-1` coefficient.

## Interpretation lock

Iter076M showed that the exact causal-vertex variables contain a gauge- and relabeling-compatible orientation pseudoscalar. Iter076N now supplies the missing **amplitude-selection provenance on the non-degenerate Lorentzian Regge saddle locus**: the exact Toller restrictor selects only one of the two parity-related EPRL critical branches, while those branches carry opposite values of the Iter076M orientation pseudoscalar.

Consequently, on this frozen saddle locus, the global `+H/-H` ambiguity left by Iter076K is no longer free: the causal amplitude selects one orientation sector and therefore one member of the signed Hodge line, modulo the already-fixed convention relating the selected `Omega_sigma` sign to the named `+H` representative.

This is not an exact finite-spin off-saddle signed source-to-K4 pushforward theorem. The exact finite-spin object is the Toller restrictor; identifying its selected critical branch with an `Omega_sigma` sign uses the non-degenerate Lorentzian critical-point/parity reconstruction.

The next exact question is whether the full finite-spin Toller support itself fixes `Omega_sigma` away from stationary points, or whether both orientation sectors remain in exact support and the sign selection is intrinsically saddle-level. That question must be prospectively tested before any generic finite-spin P3 promotion.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no generic finite-spin signed P3; no nominal `epsilon^-1` coefficient; no physical causal-vertex finiteness/divergence theorem; no F9/G3/G8/K5 promotion; no physical-sector theorem outside the explicitly frozen non-degenerate Lorentzian Regge saddle locus.
