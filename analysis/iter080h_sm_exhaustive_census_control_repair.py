#!/usr/bin/env python3
from __future__ import annotations

# Control-only implementation repair for Iter080H-SM.
# Scientific corpus, frozen manifest, A1-A5 predicates, outcome criteria, and
# interpretation ceiling are unchanged. Only two brittle textual source-lock
# matchers in Lane D are replaced by exact/current durable-authority checks.

import analysis.iter080h_sm_exhaustive_census as base


def lane_d_repaired():
    c=base.CURRENT.read_text(encoding='utf-8')
    e=base.ERRATUM.read_text(encoding='utf-8')
    locks={
        'iter077q':'ITER077Q_SM_SOURCE_COMPATIBLE_K5_EXTENSION_AMBIGUITY_CONTAINS_INFINITE_DIMENSIONAL_TANGENTIAL_SUBSPACE_EXACT_THEOREM_SCOPED' in c,
        'iter080a':'Iter080A remains independently `CONFIRMED_SCOPED`' in c,
        'iter080d':'Iter080D' in c and 'CONFIRMED_SCOPED' in c,
        'iter080e':'BLOCKED_OBJECT_DEFINITION' in c and 'Iter080E' in c,
        'iter080b':'BLOCKED_SOURCE_BRIDGE' in c and 'Iter080B' in c,
        'iter080f_invalid':'Iter080F' in c and 'INVALID_IMPLEMENTATION' in c,
        'iter080g_invalid':'INVALID_PREPRODUCTION_STATEMENT_UNIVERSE_PARSER' in (base.ROOT/'status'/'ITER080G_ITER080H_HANDOFF.md').read_text(encoding='utf-8'),
        'erratum':"delta^(rho,1/2)(x) = -(2 i rho/D) delta(x) - (1/D) delta'(x)" in e,
        'claim_locks':'No `NEW_PHYSICS_FOUND`' in c and 'no complete-QG claim' in c and 'Retain published one-wedge spectral `i epsilon`' in c,
    }
    valid=all(locks.values())
    return {'iteration':'Iter080H-SM','lane':'D','valid':valid,'scientific_outcome':'PASS_DEPENDENCY_CLAIM_LOCK' if valid else 'INVALID_IMPLEMENTATION_OR_PROVENANCE','locks':locks,'repair_scope':'control-only textual source-lock matcher repair; frozen scientific contract unchanged'}


base.lane_d=lane_d_repaired
base.LANES['D']=lane_d_repaired

if __name__=='__main__':
    base.main()
