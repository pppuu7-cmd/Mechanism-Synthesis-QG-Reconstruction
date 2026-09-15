#!/usr/bin/env python3
"""Control-only repair 1 for Iter083A.

Scientific formulas and frozen predicates are unchanged. This driver repairs
(1) outcome-biased P6 validation and (2) the frozen PASS/FAIL/INVALID verdict
taxonomy, prospectively frozen in prereg/ITER083A_CONTROL_ONLY_REPAIR_1.md.
"""
from pathlib import Path
import sys

src_path = Path("scripts/iter083a_boundary_covariant_jet_character_validation.py")
src = src_path.read_text(encoding="utf-8")

old_p6 = '    p6 = len(odd_open) > 0\n'
new_p6 = (
    '    # P6 is outcome-neutral: it requires the scalar-vs-boundary comparison to be\n'
    '    # computed and reported degree-by-degree; the opened-order list may be empty.\n'
    '    p6 = (\n'
    '        degrees == list(range(9))\n'
    '        and len(direct) == 9\n'
    '        and len(scalar) == 9\n'
    '        and odd_open == [k for k in degrees if scalar[k] == 0 and direct[k] > 0]\n'
    '    )\n'
)
if src.count(old_p6) != 1:
    raise SystemExit(f"INVALID_REPAIR_P6_TARGET_COUNT:{src.count(old_p6)}")
src = src.replace(old_p6, new_p6)

old_verdict = '''    passed = all(predicates.values())\n\n    verdict = "PASS_EXACT_SCOPED" if passed else "INVALID_IMPLEMENTATION"\n    classification = (\n        "K5_BOUNDARY_COVARIANT_INVARIANT_NORMAL_SYMBOL_CHARACTER_CLASSIFICATION_EXACT_SCOPED"\n        if passed\n        else "K5_BOUNDARY_COVARIANT_NORMAL_SYMBOL_CLASSIFICATION_INVALID_IMPLEMENTATION"\n    )\n'''
new_verdict = '''    # Frozen taxonomy: malformed inputs/controls are implementation-invalid;\n    # valid exact representation-theory mismatch is scientific FAIL.\n    implementation_valid = p0 and p7\n    scientific_pass = all([p1, p2, p3, p4, p5, p6])\n    passed = implementation_valid and scientific_pass\n    if not implementation_valid:\n        verdict = "INVALID_IMPLEMENTATION"\n        classification = "K5_BOUNDARY_COVARIANT_NORMAL_SYMBOL_CLASSIFICATION_INVALID_IMPLEMENTATION"\n    elif scientific_pass:\n        verdict = "PASS_EXACT_SCOPED"\n        classification = "K5_BOUNDARY_COVARIANT_INVARIANT_NORMAL_SYMBOL_CHARACTER_CLASSIFICATION_EXACT_SCOPED"\n    else:\n        verdict = "FAIL_EXACT_SCOPED"\n        classification = "K5_BOUNDARY_COVARIANT_NORMAL_SYMBOL_CLASSIFICATION_FAIL_EXACT_SCOPED"\n'''
if src.count(old_verdict) != 1:
    raise SystemExit(f"INVALID_REPAIR_VERDICT_TARGET_COUNT:{src.count(old_verdict)}")
src = src.replace(old_verdict, new_verdict)

# Record repaired implementation for artifact/provenance inspection.
out_impl = Path("results/raw/iter083a_repaired_implementation.py")
out_impl.parent.mkdir(parents=True, exist_ok=True)
out_impl.write_text(src, encoding="utf-8")

sys.argv[0] = str(src_path)
code = compile(src, str(src_path), "exec")
exec(code, {"__name__": "__main__", "__file__": str(src_path)})
