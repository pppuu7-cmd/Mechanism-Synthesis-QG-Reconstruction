#!/usr/bin/env python3
import argparse, hashlib, json, pathlib

PREDICATES = [
    "Q1_JOINT_PHYSICAL_FAMILY",
    "Q2_CHECKABLE_EXISTENCE_HYPOTHESES",
    "Q3_UNIQUE_SOURCE_SELECTOR",
    "Q4_DISTRIBUTIONAL_EPRL_BRIDGE",
]


def load_matrix(path):
    raw = pathlib.Path(path).read_bytes()
    obj = json.loads(raw)
    return obj, hashlib.sha256(raw).hexdigest()


def audit_candidate(matrix, matrix_sha, candidate):
    row = next(r for r in matrix["candidates"] if r["candidate"] == candidate)
    checks = row["checks"]
    if set(checks) != set(PREDICATES):
        raise SystemExit("invalid predicate set")
    complete = all(bool(checks[p]) for p in PREDICATES)
    theorem_route = bool(checks["Q2_CHECKABLE_EXISTENCE_HYPOTHESES"] and checks["Q3_UNIQUE_SOURCE_SELECTOR"])
    return {
        "gate": matrix["gate"],
        "frozen_prereg_commit": matrix["frozen_prereg_commit"],
        "matrix_sha256": matrix_sha,
        "candidate": candidate,
        "source": row["source"],
        "source_version": row["source_version"],
        "checks": checks,
        "complete_selector_bridge": complete,
        "conditional_theorem_route": theorem_route,
        "missing": [p for p in PREDICATES if not checks[p]],
        "evidence": row["evidence"],
    }


def aggregate(matrix, matrix_sha, input_dir):
    rows = []
    for row in matrix["candidates"]:
        p = pathlib.Path(input_dir) / f'{row["candidate"]}.json'
        got = json.loads(p.read_text())
        if got["matrix_sha256"] != matrix_sha or got["frozen_prereg_commit"] != matrix["frozen_prereg_commit"]:
            raise SystemExit(f"provenance mismatch: {p}")
        rows.append(got)
    complete = [r["candidate"] for r in rows if r["complete_selector_bridge"]]
    conditional = [r["candidate"] for r in rows if r["conditional_theorem_route"]]
    if complete:
        classification = "ITER067A_BOUNDARY_VALUE_SELECTOR_ROUTE_QUALIFIED"
    elif conditional:
        classification = "ITER067A_THEOREM_ROUTE_EXISTS_PHYSICAL_HYPOTHESES_UNPROVEN"
    else:
        classification = "ITER067A_BOUNDARY_VALUE_SELECTOR_ROUTE_NOT_YET_AVAILABLE"
    missing_histogram = {p: sum(p in r["missing"] for r in rows) for p in PREDICATES}
    return {
        "gate": matrix["gate"],
        "frozen_prereg_commit": matrix["frozen_prereg_commit"],
        "matrix_sha256": matrix_sha,
        "lanes": len(rows),
        "classification": classification,
        "complete_selector_bridges": complete,
        "conditional_theorem_routes": conditional,
        "missing_histogram": missing_histogram,
        "rows": rows,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--matrix", required=True)
    ap.add_argument("--candidate")
    ap.add_argument("--input-dir")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    matrix, sha = load_matrix(args.matrix)
    if args.candidate:
        result = audit_candidate(matrix, sha, args.candidate)
    else:
        if not args.input_dir:
            raise SystemExit("--input-dir required for aggregate")
        result = aggregate(matrix, sha, args.input_dir)
    pathlib.Path(args.out).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
