# Iter076 provenance ledger — canonical Iter076U and historical sibling

**Date:** 2026-09-14

This ledger resolves an iteration-name collision without rewriting prospective artifacts, workflow history, classifications, or commit SHAs.

## Canonical sequential Iter076U

The canonical sequential `Iter076U` in the main scientific chain is the gamma-simple minimal-power-strip gate:

- preregistration: `14928f1bd1a0dcb95149ebd6bbabf0171f9f3e3a`;
- durable result: `results/ITER076U_GAMMA_SIMPLE_MINIMAL_POWER_STRIP_ONEJET_RESULT.md`;
- durable result commit: `0767d2a246178fad79ed748aa5508f6de6f7bf61`;
- authoritative run: `34783135619`;
- classification: `ITER076U_GAMMA_SIMPLE_TOLLER_MINIMAL_POWER_STRIP_ONEJET_EQUALS_I_GAMMA_M_BOTH_BRANCHES_EXACT_SCOPED`.

This is the `T -> U -> V` sequential dependency used by the current frontier.

## Historical sibling alias: Iter076U-JH

A separate, prospectively frozen `j=1/2` pre-group-integration contraction witness gate was historically also labeled `Iter076U`. To avoid future ambiguity, all new prose/status references SHALL use the stable alias **`Iter076U-JH`** for that historical sibling. Existing filenames, JSON iteration labels, workflow names, frozen classifications, commits, and artifacts retain their original `Iter076U` strings for provenance integrity.

Historical authority:

- frozen preregistration file: `prereg/ITER076U_JHALF_INTERTWINER_CONTRACTED_ONEJET.md`;
- preregistration commit: `194f840db2104143ae697c062bc34846ab60759a`;
- initial parallel implementation: `5112ff5a73cfc6c53283cffa6adee11b4fa5f994`;
- authoritative exact-`j=1/2` backend/workflow head: `b5bac67f1bb66b5efd50b5f51ae80e31c4f85968`;
- authoritative run: `34783261007`;
- aggregate job: `103794143009`;
- aggregate artifact: `10325906100`;
- artifact digest: `sha256:ad6bd272790a1f0e4d61247c6a2c247806eda4c4d1be8e55ef271ffd793845e2`.

Frozen verdict:

`ITER076U_NO_INTERTWINER_CONTRACTED_ONEJET_WITNESS_ON_FROZEN_JHALF_PATHS_INCONCLUSIVE_SCOPED`

The run was valid: all fixed A/C/D controls passed, all eight census shards were present, `4096` contracted cases were tested, maximum KAK reconstruction error was `3.1401849173675503e-16`, and the robust witness count was `0` at both `gamma=0.4` and `gamma=1.2`.

This is an **INCONCLUSIVE sibling result**, not evidence that the contracted one-jet is zero. It established neither a general-spin theorem nor the four-group integrated one-jet, the physical nonlinear source-to-K4 map, or the nominal `epsilon^-1` coefficient.

## Naming rule

- `Iter076U` = canonical gamma-simple minimal-power-strip gate.
- `Iter076U-JH` = historical `j=1/2` contracted preintegration sibling.
- `Iter076U-JH` is not an omitted sequential iteration and does not supersede canonical `Iter076U`.
- Do not renumber or edit the frozen historical preregistration solely to repair the label collision.

No scientific claim lock is changed by this ledger.
