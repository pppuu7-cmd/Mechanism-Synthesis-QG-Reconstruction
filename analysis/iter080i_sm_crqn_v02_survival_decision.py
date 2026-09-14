#!/usr/bin/env python3
import hashlib, json, pathlib, subprocess, sys

FROZEN = {
  "results/ITER077Q_SM_INVARIANT_TANGENTIAL_AMBIGUITY_RESULT.md": {
    "blob":"26aa90965ccfe495f55df2f4c190f7bbe09093f4",
    "need":["INFINITE_DIMENSIONAL_TANGENTIAL_SUBSPACE","infinite-dimensional"]},
  "results/ITER080A_SM_K5_FINITE_PERMUTATION_SELECTOR_RESULT.md": {
    "blob":"a7c1878cc2963f5a5010510c8c348211b32e05a1",
    "need":["FINITE_PERMUTATION","does not"]},
  "results/ITER080D_SM_CONTROL_ONLY_UNIVERSAL_REPAIR_RESULT.md": {
    "blob":"1dbae540309e9bcb85facfe39a38200e91b7e728",
    "need":["FIXED_FINITE_SCALAR_LINEAR","cannot"]},
  "results/ITER080E_SM_CONTROL_ONLY_SOURCE_PREDICATE_REPAIR_RESULT.md": {
    "blob":"505bb79507a6cf85b248e582d1e294ff9587240f",
    "need":["BLOCKED_OBJECT_DEFINITION","selector"]},
  "results/ITER080H_SM_LINE_AWARE_EXHAUSTIVE_PRE_ITER077Q_SELECTOR_CENSUS_RESULT.md": {
    "blob":"dd101a9d0683542d47f8ec37fe7331152f0375a4",
    "need":["BLOCKED_EXISTING_AXIOM_SELECTOR_MISSING","full"]},
  "results/ITER080H_ADVERSARIAL_REVIEW.md": {
    "blob":"9271acd82ad2a691f643f0c5c493b5ad45abbd6b",
    "need":["CONFIRMED_SCOPED"]},
  "candidates/CANDIDATE_A_CRQN_V0_2.md": {
    "blob":"3933c110f9bafabb6593f8301029adaa25458bb2",
    "need":["CRQN"]},
}
CLASSIFICATION = "ITER080I_SM_CRQN_V0_2_LOCAL_K5_AMPLITUDE_REMAINS_BLOCKED_BY_UNSELECTED_INFINITE_DIMENSIONAL_EXTENSION_AMBIGUITY_SUCCESSOR_CANDIDATE_REQUIRED_EXACT_DEPENDENCY_SCOPED"

def blob(path):
    return subprocess.check_output(["git","rev-parse",f"HEAD:{path}"], text=True).strip()

def main():
    lane = sys.argv[1] if len(sys.argv)>1 else "aggregate"
    checks=[]
    for path,spec in FROZEN.items():
        p=pathlib.Path(path)
        ok=p.exists()
        actual=blob(path) if ok else None
        text=p.read_text(errors="replace") if ok else ""
        tokens={t:(t.lower() in text.lower()) for t in spec["need"]}
        row={"path":path,"expected_blob":spec["blob"],"actual_blob":actual,
             "blob_ok":actual==spec["blob"],"tokens":tokens,
             "content_sha256":hashlib.sha256(text.encode()).hexdigest() if ok else None}
        checks.append(row)
    provenance=all(r["blob_ok"] for r in checks)
    semantic=all(all(r["tokens"].values()) for r in checks)
    prereg=pathlib.Path("prereg/ITER080I_SM_CRQN_V0_2_LOCAL_AMPLITUDE_ANTI_RESCUE_SURVIVAL_DECISION.md")
    prereg_ok=prereg.exists() and "P1-P6" in prereg.read_text() and CLASSIFICATION in prereg.read_text()
    if not provenance or not prereg_ok:
        verdict="INVALID_PROVENANCE"
        classification="INVALID_PROVENANCE"
    elif not semantic:
        verdict="SURVIVES_THIS_GATE_NOT_ESTABLISHED_BLOCKER"
        classification=verdict
    else:
        verdict="BLOCKED_CURRENT_CANDIDATE_LOCAL_AMPLITUDE"
        classification=CLASSIFICATION
    out={"schema":"ITER080I_DEPENDENCY_SURVIVAL_V1","lane":lane,"provenance_ok":provenance,
         "semantic_frozen_predicates_present":semantic,"prereg_lock_ok":prereg_ok,
         "posthoc_selector_added":False,"verdict":verdict,"classification":classification,
         "checks":checks,
         "claim_locks":{"new_physics_found":False,"complete_qg":False,"unique_k5_extension":False,
                         "g3_pass":False,"f9_promotion":False,"g8_promotion":False}}
    print(json.dumps(out,indent=2,sort_keys=True))
    if verdict=="INVALID_PROVENANCE": return 2
    return 0

if __name__=="__main__": raise SystemExit(main())
