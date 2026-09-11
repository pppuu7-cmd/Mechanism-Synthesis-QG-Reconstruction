#!/usr/bin/env python3
"""Feature-level novelty audit for CRQN.

Novelty remains BLOCKED unless CRQN adds an explicit relation/observable not covered by a
source family or a trivial union of source families.  This is a fail-closed control, not a
bibliometric proof of novelty.
"""
from __future__ import annotations
import argparse, itertools, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MATRIX=ROOT/"data"/"known_family_feature_matrix_v0_1.json"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",default="results/novelty_overlap.json")
    args=ap.parse_args()
    data=json.loads(MATRIX.read_text(encoding="utf-8"))
    target=set(data["candidate_current_features"])
    families=data["families"]
    single=[]
    for fam in families:
        covered=target & set(fam["features"])
        single.append({"family":fam["name"],"covered":sorted(covered),"fraction":len(covered)/len(target) if target else 1.0})
    single.sort(key=lambda x:(-x["fraction"],x["family"]))
    min_cover=None
    for n in range(1,len(families)+1):
        for combo in itertools.combinations(families,n):
            union=set().union(*(set(f["features"]) for f in combo))
            if target <= union:
                min_cover=[f["name"] for f in combo]
                break
        if min_cover: break
    required=set(data["required_for_g8_novelty"])
    already=set().union(*(set(f["features"]) for f in families))
    candidate_has_unique=sorted(required & target)
    out={
        "candidate_features":sorted(target),
        "best_single_family_overlap":single[:5],
        "minimum_source_family_cover":min_cover,
        "all_current_features_covered_by_source_union":min_cover is not None,
        "required_novel_features":sorted(required),
        "candidate_currently_has_required_novel_features":candidate_has_unique,
        "novel_features_not_already_in_source_matrix":sorted(required-already),
        "verdict":"G8_BLOCKED_CONVERGENCE_ONLY" if min_cover is not None and not candidate_has_unique else "G8_REOPEN",
        "scope":"feature-level audit; literature matrix must be updated when source evidence changes"
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding="utf-8")
    print(json.dumps(out,indent=2))

if __name__=="__main__":main()
