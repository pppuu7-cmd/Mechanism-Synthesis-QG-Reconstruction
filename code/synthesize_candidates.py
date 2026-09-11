#!/usr/bin/env python3
"""Enumerate minimal MSQGR mechanism sets under explicit coverage and compatibility rules.

This is a methodology scaffold, not a physics solver. It makes the synthesis logic auditable:
mechanisms are selected because they cover declared functions and do not contain declared hard
conflicts. Unknown compatibility remains visible rather than silently treated as evidence.
"""

from __future__ import annotations

import csv
import itertools
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / "data" / "mechanism_atlas_v0_1.csv"
COMPAT = ROOT / "data" / "compatibility_v0_1.csv"

# Functions required for an architecture-level candidate. These are intentionally distinct so
# recurrence does not allow one fashionable mechanism to be counted several times for free.
COVERAGE = {
    "M01": {"RELATIONAL"},
    "M02": {"CAUSAL"},
    "M03": {"MICRO_DISCRETENESS"},
    "M04": {"QUANTUM_GEOMETRY"},
    "M05": {"QUANTUM_DYNAMICS"},
    "M06": {"COMBINATORIAL_DYNAMICS"},
    "M07": {"UV_CONTROL"},
    "M09": {"INFORMATION_CONSTRAINT"},
    "M12": {"CONTINUUM"},
    "M13": {"SYMMETRY_CLOSURE"},
    "M14": {"OBSERVABLE_CONSISTENCY"},
    "M16": {"MATTER_GRAVITY_PARENT"},
}

REQUIRED = {
    "RELATIONAL",
    "CAUSAL",
    "QUANTUM_GEOMETRY",
    "QUANTUM_DYNAMICS",
    "UV_CONTROL",
    "CONTINUUM",
    "SYMMETRY_CLOSURE",
}

# Candidate generation excludes IR targets and pure emergent signatures as independent causes.
ELIGIBLE = {"M01", "M02", "M03", "M04", "M05", "M06", "M07", "M09", "M12", "M13", "M14", "M16"}


def load_atlas():
    with ATLAS.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    return {r["mechanism_id"]: r for r in rows}


def load_compatibility():
    table = {}
    with COMPAT.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            key = tuple(sorted((row["mechanism_a"], row["mechanism_b"])))
            table[key] = int(row["score"])
    return table


def pair_score(a, b, compat):
    if a == b:
        return 2
    return compat.get(tuple(sorted((a, b))), 0)  # unknown stays neutral/blocked


def covered(combo):
    out = set()
    for mid in combo:
        out |= COVERAGE.get(mid, set())
    return out


def hard_conflict(combo, compat):
    return any(pair_score(a, b, compat) <= -2 for a, b in itertools.combinations(combo, 2))


def soft_tensions(combo, compat):
    return [(a, b) for a, b in itertools.combinations(combo, 2) if pair_score(a, b, compat) == -1]


def unknown_pairs(combo, compat):
    return [(a, b) for a, b in itertools.combinations(combo, 2) if tuple(sorted((a, b))) not in compat]


def compatibility_sum(combo, compat):
    return sum(pair_score(a, b, compat) for a, b in itertools.combinations(combo, 2))


def enumerate_minimal():
    atlas = load_atlas()
    compat = load_compatibility()
    eligible = sorted(mid for mid in ELIGIBLE if mid in atlas)

    winners = []
    for n in range(1, len(eligible) + 1):
        for combo in itertools.combinations(eligible, n):
            if not REQUIRED <= covered(combo):
                continue
            if hard_conflict(combo, compat):
                continue
            winners.append(combo)
        if winners:
            break

    ranked = sorted(
        winners,
        key=lambda c: (
            len(soft_tensions(c, compat)),
            len(unknown_pairs(c, compat)),
            -compatibility_sum(c, compat),
            c,
        ),
    )
    return ranked, atlas, compat


def main():
    ranked, atlas, compat = enumerate_minimal()
    if not ranked:
        raise SystemExit("No architecture covers the required functions under current rules.")

    print(f"Minimal architecture size: {len(ranked[0])}")
    print(f"Number of minimal architectures: {len(ranked)}")
    print()
    for i, combo in enumerate(ranked[:20], 1):
        print(f"#{i}: {', '.join(combo)}")
        print(f"  compatibility_sum={compatibility_sum(combo, compat)}")
        print(f"  soft_tensions={soft_tensions(combo, compat)}")
        print(f"  unknown_pairs={unknown_pairs(combo, compat)}")
        print("  mechanisms:")
        for mid in combo:
            print(f"    {mid}: {atlas[mid]['mechanism_name']}")
        print()


if __name__ == "__main__":
    main()
