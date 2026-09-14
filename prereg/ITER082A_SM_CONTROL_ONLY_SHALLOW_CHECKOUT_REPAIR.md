# Iter082A-SM control-only repair prereg

Date: 2026-09-14

Historical production run `34889953575` failed before scientific execution because `actions/checkout@v4` used its default shallow history (`fetch-depth: 1`), so the chronology guard could not resolve prereg commit `53cd6cea982192b80fe0e23434866dda97f46002` and exited with `fatal: Not a valid commit name`.

This is an infrastructure/provenance-control failure only. No Iter082A scientific output was produced and no frozen scientific criterion is changed.

The only permitted repair is to fetch full git history (`fetch-depth: 0`) so the already-frozen chronology checks can execute unchanged. Script `scripts/iter082a_sm_nested_partial_collision_reproduction.py`, K3/K4 witnesses, classifications, controls, and claim ceiling remain frozen unchanged.
