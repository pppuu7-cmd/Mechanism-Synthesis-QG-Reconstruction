#!/usr/bin/env python3
import argparse, json, pathlib, hashlib

PREDICATES = [
    "P1_CORRELATED_MULTIVARIATE",
    "P2_SOURCE_SELECTED_UNIQUE",
    "P3_ORDER_PERMUTATION_INDEPENDENT",
    "P4_TOLLER_EPRL_COMPATIBLE",
]

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidate", required=True)
    ap.add_argument("--matrix", default="research/iter066a_source_frameworks.json")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    raw = pathlib.Path(args.matrix).read_bytes()
    matrix = json.loads(raw)
    cand = matrix["candidates"].get(args.candidate)
    if cand is None:
        raise SystemExit(f"unknown candidate {args.candidate}")

    checks = {p: bool(cand[p]) for p in PREDICATES}
    complete = all(checks.values())
    result = {
        "gate": matrix["gate"],
        "candidate": args.candidate,
        "frozen_prereg_commit": matrix["frozen_prereg_commit"],
        "matrix_sha256": sha256_bytes(raw),
        "source": cand["source"],
        "source_version": cand["source_version"],
        "checks": checks,
        "complete_bridge": complete,
        "has_multivariate_framework": checks["P1_CORRELATED_MULTIVARIATE"],
        "evidence": cand["evidence"],
    }
    pathlib.Path(args.out).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
