# Iter076L terminal result — Regge 4-volume orientation selects the Hodge sign only semiclassically

Date: 2026-09-13

## Authority
- source supplement: `91384368b80deb3e432a2f1a32ae4d030ae53fbb`
- frozen preregistration: `96782b4fbb81e36bf8129f2c29aed78447838a3d`
- implementation: `67d9c618945205de4ee836ea31ecaf1f08ddf487`
- production/workflow head: `7ac6470c9959de272c1b1efe0b7d5def7001443d`
- run: `34780504851`
- aggregate job: `103786559383`
- aggregate artifact: `10324722242`
- aggregate artifact ZIP digest: `sha256:36795aa715631ea8f3eb99fc99bf19aff6b88e5c84eb0fdd91fa32db19a61673`

Raw lane artifacts consumed by the aggregate job:
- A: artifact `10324966967`, digest `sha256:df571a357083254b0ff43461a088d475fb1f5096f1ee54f4c61a8daa15fe50a0`
- B: artifact `10324438415`, digest `sha256:c40d68bde36831d37a75ecb9d1adac66fe8b26ea6c7abbdd054620c07cf83a81`
- C: artifact `10325445609`, digest `sha256:59971ecaf2215a61c2f84743abb8aef1bea833362c09ac101d10884dcc832772`
- D: artifact `10324591482`, digest `sha256:5636b1574451355c0d98c4b7f4409e97dd7b6aa26d03e750656117615cb829ac`

## Frozen scientific classification

`ITER076L_REGGE_4VOLUME_ORIENTATION_SELECTS_HODGE_SIGN_SEMICLASSICAL_EXACT_BRIDGE_STILL_BLOCKED_SCOPED`

Scope: `SEMICLASSICAL_ONLY`.

## Terminal facts

All four prospectively frozen lanes pass and aggregate output is `valid=true`.

1. The oriented four-vector determinant carries exactly the missing sign character: all `24/24` S4 permutations obey `omega(p.X)=sgn(p) omega(X)`, with `12` preserving and `12` reversing orientation.
2. Multiplying the unique Iter076H/K Hodge line by the Regge orientation sign selects one of the two lifts `+H/-H`. Each lift obeys the frozen twisted covariance law; transporting `omega` as a pseudoscalar makes the selected family covariant, and orientation reversal exchanges the two and only the two lifts. The orientation-blind control is rejected.
3. Across all five gauge roots and all `120` S5 relabelings per root, pseudoscalar transport is covariant in `600/600` checks. There are `300` induced odd-S4 cases, and the deliberately wrong fixed-omega control fails in all `300/300`.
4. The provenance firewall passes: combinatorial `sigma/kappa` and Regge orientation remain distinct source levels; the bridge is semiclassical; the 2026 causal paper does not establish the proper-vertex 4-volume orientation as an exact Eq.(4) selector; no exact signed-P3 promotion is allowed here.

## Interpretation lock

Iter076L resolves the **mathematical character** of the missing sign at the semiclassical Regge boundary: oriented nonzero 4-volume has exactly the pseudoscalar transformation law needed to choose the global sign of the Hodge line.

It does **not** resolve the exact source-provenance blocker. The causal Eq.(4) integrand still lacks an established contraction/orientation object proven to produce this selector before stationary-phase/Regge reconstruction. Therefore physical signed `SOURCE_TO_K4_PUSHFORWARD` remains blocked on an exact Eq.(4)-level bridge.

The nominal `epsilon^-1` source numerator/Jacobian coefficient remains `BLOCKED_OBJECT_DEFINITION`. No F9/G3/G8/K5 promotion, causal-vertex finiteness/divergence theorem, complete-QG claim, or new-physics claim follows.
