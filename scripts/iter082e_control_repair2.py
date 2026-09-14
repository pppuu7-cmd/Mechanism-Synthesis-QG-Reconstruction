#!/usr/bin/env python3
"""Control-only repair 2 for Iter082E.

The scientific implementation is unchanged. This driver patches exactly one
previously preregistered negative-control wiring error: a malformed cubic
coefficient tied to absolute label 0 must not be permuted with the data.
"""
from pathlib import Path
import hashlib

src_path=Path("scripts/iter082e_nonlinear_tubular_chart_overlap.py")
src=src_path.read_text(encoding="utf-8")
old="""        lhs=transform_nodes(permute_nodes(nodes,p),coeff,\n                            None if cubic_scales is None else [cubic_scales[p.index(i)] for i in range(5)])\n        rhs=permute_nodes(transform_nodes(nodes,coeff,cubic_scales),p)\n"""
new="""        lhs=transform_nodes(permute_nodes(nodes,p),coeff,cubic_scales)\n        rhs=permute_nodes(transform_nodes(nodes,coeff,cubic_scales),p)\n"""
count=src.count(old)
if count!=1:
    raise SystemExit(f"INVALID_REPAIR_TARGET_COUNT:{count}")
patched=src.replace(old,new)
if "[cubic_scales[p.index(i)]" in patched:
    raise SystemExit("INVALID_REPAIR_RESIDUAL_PERMUTED_SCALE")
Path("artifacts/iter082e").mkdir(parents=True,exist_ok=True)
Path("artifacts/iter082e/repaired_implementation.py").write_text(patched,encoding="utf-8")
Path("artifacts/iter082e/repair2_patch.sha256").write_text(hashlib.sha256(patched.encode()).hexdigest()+"  repaired_implementation.py\n",encoding="utf-8")
code=compile(patched,"iter082e_repaired_implementation.py","exec")
exec(code,{"__name__":"__main__","__file__":"iter082e_repaired_implementation.py"})
