# Iter083N provenance-correct retry — independent Critic review preregistration

Date: 2026-09-15

Status: **PROSPECTIVELY FROZEN BEFORE CRITIC IMPLEMENTATION / PRODUCTION OUTPUT**

## Object under review

Only the fresh repaired Researcher production is reviewable authority:

- Researcher head `15472a83a6fc5e73c10b050649578822b65558cf`;
- run `34925157771`, job `104241540969`;
- artifact `10379901560`, digest `sha256:ac44a7a209847a097902904bb7114ffafa40edc8d40d8f15324b0c66204f0384`;
- production JSON SHA256 `b5e1f14e728c1ee9342a5433084b6c1d122faad4af360ffbcd627f60a76cd9ec`;
- Researcher result commit `7e194bd7d6e074e03f4393a6357d06824aedc745`.

Historical Iter083N remains `INVALID_PROVENANCE`; run `34925091322` remains `INVALID_IMPLEMENTATION`. Neither may be rehabilitated.

## Frozen independent checks

The Critic implementation must reconstruct rather than trust Researcher booleans.

C0 provenance: verify all identifiers above plus parent prereg `c29ba0ddbaa4d6e1581db558b792565a7916a0cd`, source lock `cf9d17cc8dae087f2c59ff0adb9f8aeff8ef7533`, theorem derivation `70a756c9c7c66f822d0e5933e9522b2d359dafe8`, and controlling Iter083M Critic `e7623cb5303ea49894e480e2fc4a884df44e7713`.

C1 Laurent reconstruction: independently multiply `(1+z phi+O(z^2))(A_-1/z+A_0+O(z))`; require residue unchanged and finite-part shift exactly `phi A_-1`.

C2 supported-jet reconstruction: independently derive and test `n^q delta^(k)=(-1)^q k!/(k-q)! delta^(k-q)` for `q<=k`, zero for `q>k`, for all `0<=k<=8`, `0<=q<=9`; require 90/90 exact identities.

C3 universal threshold/sharpness: independently require the universal annihilator threshold `I_N^(omega+1)` and explicit nonzero witnesses below threshold for every `omega in {0,3,8}`; therefore K3/K4/K5 thresholds must be exactly `1,4,9`.

C4 Iter083M implication: independently verify that equality of normalized tangent quadratic Hessians for `rho'=exp(phi)rho` fixes only `phi|_N=0` (`phi in I_N`) in the frozen conformal comparison, not higher normal jets. Require conclusion: universally sufficient for K3 but not for the full allowed K4/K5 residue classes.

C5 constant scaling control: independently require `rho'=c rho` to shift finite part by `(log c) A_-1`.

C6 physical firewall: reject any inference that the actual source-ordered Toller residue is nonzero, maximal-order, or sensitive to remaining jets. Explicitly retain lower-order, annihilator, vanishing-residue, and exact nonlinear source-radius possibilities.

C7 source/theorem firewall: do not import Felder-Kazhdan odd-codimension residue vanishing into K4 without membership proof; do not promote a generic radial regularization theorem to a source-authorized physical selector.

C8 adversarial malformed controls: the same Critic machinery must reject at least: stale historical Iter083N as authority; all residues forced to order zero; tangent metric claimed to fix full finite part for omega>0; actual K5 dependence asserted without an actual residue; FK parity imported without class membership; threshold weakened below omega+1.

## Frozen classifications

- all C0-C8 exact and controls effective -> `ITER083N_PROVENANCE_CORRECT_RETRY_CRITIC_CONFIRMED_SCOPED`, verdict `CONFIRMED_SCOPED`;
- scientific reconstruction contradicts Researcher under valid provenance -> `SCIENTIFIC_FAIL_SCOPED`;
- malformed/ineffective controls or implementation defect -> `INVALID_IMPLEMENTATION`;
- authority/provenance mismatch -> `INVALID_PROVENANCE`;
- required source object unavailable -> `BLOCKED`.

No frozen criterion may be changed after production output is inspected.

## Claim ceiling

Even `CONFIRMED_SCOPED` does not establish actual nonzero physical finite-part dependence, an actual Toller residue theorem, a source-authorized selector, unique K5 extension, regulator dependence/independence, global forest patching, G3/F9/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete QG.

Iter083O remains downstream-quarantined until this review is terminal and `status/CURRENT.md` is reconciled.