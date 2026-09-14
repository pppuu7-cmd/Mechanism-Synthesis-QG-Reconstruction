#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE_PATH = ROOT / "analysis" / "iter080f_sm_crqn_existing_axiom_selector_census.py"

spec = importlib.util.spec_from_file_location("iter080f_base", BASE_PATH)
assert spec and spec.loader
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)


def instant(s: str | None):
    if not s:
        return None
    return datetime.fromisoformat(s.replace("Z", "+00:00")).astimezone(timezone.utc)


def lane_a_repaired() -> dict:
    rows = []
    valid = True
    q_expected = instant(base.ITER077Q_DATE)
    for key, f in base.FROZEN.items():
        p = ROOT / f["path"]
        actual_blob = base.blob(p)
        try:
            actual_origin_date = base.git("show", "-s", "--format=%cI", f["origin"])
        except subprocess.CalledProcessError:
            actual_origin_date = None
        actual_i = instant(actual_origin_date)
        expected_i = instant(f["origin_date"])
        row = {
            "candidate": key,
            "path": f["path"],
            "expected_blob": f["blob"],
            "actual_blob": actual_blob,
            "origin_commit": f["origin"],
            "expected_origin_date": f["origin_date"],
            "actual_origin_date": actual_origin_date,
            "same_instant_after_utc_normalization": bool(actual_i and expected_i and actual_i == expected_i),
            "predates_iter077q": bool(actual_i and q_expected and actual_i < q_expected),
        }
        row["ok"] = actual_blob == f["blob"] and row["same_instant_after_utc_normalization"] and row["predates_iter077q"]
        valid = valid and row["ok"]
        rows.append(row)
    try:
        q_date = base.git("show", "-s", "--format=%cI", base.ITER077Q_COMMIT)
    except subprocess.CalledProcessError:
        q_date = None
    q_ok = bool(instant(q_date) and q_expected and instant(q_date) == q_expected)
    valid = valid and q_ok
    return {
        "iteration": "Iter080F-SM",
        "lane": "A",
        "repair": "CONTROL_ONLY_TIMEZONE_NORMALIZATION",
        "valid": valid,
        "scientific_outcome": "PASS_PROVENANCE_TIMING" if valid else "INVALID_PROVENANCE",
        "candidate_rows": rows,
        "iter077q": {
            "commit": base.ITER077Q_COMMIT,
            "expected_date": base.ITER077Q_DATE,
            "actual_date": q_date,
            "same_instant_after_utc_normalization": q_ok,
        },
    }

base.lane_a = lane_a_repaired
base.LANES["A"] = lane_a_repaired

if __name__ == "__main__":
    base.main()
