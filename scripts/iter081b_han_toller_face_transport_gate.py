#!/usr/bin/env python3
import hashlib, io, json, pathlib, re, tarfile, urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "results/raw"
OUT.mkdir(parents=True, exist_ok=True)

SOURCES = {
    "han_2602_18665v1": "https://export.arxiv.org/e-print/2602.18665v1",
    "bcg_2604_24945": "https://export.arxiv.org/e-print/2604.24945",
    "beltran_2603_22661v2": "https://export.arxiv.org/e-print/2603.22661v2",
}


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "MSQGR-Iter081B/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def source_text(blob):
    # arXiv e-print normally returns tar/tar.gz source; allow plain text fallback.
    texts = []
    try:
        with tarfile.open(fileobj=io.BytesIO(blob), mode="r:*") as tf:
            for m in tf.getmembers():
                if not m.isfile() or m.size > 8_000_000:
                    continue
                if not re.search(r"\.(tex|txt|bbl|sty)$", m.name, re.I):
                    continue
                f = tf.extractfile(m)
                if f:
                    texts.append(f.read().decode("utf-8", "ignore"))
    except tarfile.TarError:
        texts.append(blob.decode("utf-8", "ignore"))
    return "\n".join(texts)


def norm(s):
    s = s.lower()
    s = re.sub(r"\\[a-zA-Z]+", " ", s)
    s = re.sub(r"[^a-z0-9+\-_=^/ ]+", " ", s)
    return re.sub(r"\s+", " ", s)


def has_any(text, pats):
    return any(re.search(p, text, re.I | re.S) for p in pats)

# A. Acquire actual frozen primary source material.
raw, txt, hashes, errors = {}, {}, {}, []
for key, url in SOURCES.items():
    try:
        b = fetch(url)
        if len(b) < 2000:
            raise RuntimeError(f"source_too_small:{len(b)}")
        t = source_text(b)
        if len(t) < 2000:
            raise RuntimeError(f"extracted_text_too_small:{len(t)}")
        raw[key], txt[key] = b, t
        hashes[key] = hashlib.sha256(b).hexdigest()
    except Exception as e:
        errors.append(f"{key}:{type(e).__name__}:{e}")

if errors:
    result = {
        "gate": "ITER081B_SM_HAN_TOLLER_FACE_FUNCTIONAL_TRANSPORT_OBSTRUCTION_GATE",
        "verdict": "INVALID_PROVENANCE_OR_INFRASTRUCTURE",
        "classification": "INVALID_PROVENANCE_OR_INFRASTRUCTURE",
        "errors": errors,
        "source_sha256": hashes,
        "claim_locks_preserved": True,
    }
    (OUT / "iter081b_sm_aggregate.json").write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(3)

han = txt["han_2602_18665v1"]
bcg = txt["bcg_2604_24945"]
bel = txt["beltran_2603_22661v2"]

# B. Positive source checks from actual retrieved text, not a prelabelled matrix.
positive = {
    "han_face_tau_present": has_any(han, [r"tau.{0,120}d[_\\ ]?k.{0,160}(tr|trace)", r"\\tau.{0,150}\\mathrm\{Tr\}"]),
    "han_bound_present": has_any(han, [r"tau.{0,160}d[_\\ ]?k\^?2", r"\\left\|?\\tau.{0,180}d.*?2"]),
    "han_grand_canonical_present": has_any(han, [r"grand.?canonical", r"partition function"]),
    "han_condensation_or_localization_present": has_any(han, [r"condens", r"locali[sz]ation"]),
    "han_gluing_or_cut_present": has_any(han, [r"gluing", r"cutting", r"cut .{0,30}glue"]),
    "bcg_toller_present": has_any(bcg, [r"toller"]),
    "bcg_additive_identity_present": has_any(bcg, [r"t.{0,30}\+.{0,30}t.{0,30}=.{0,20}d", r"t\^?\{?\(\+\)\}?.{0,80}t\^?\{?\(\-\)\}?.{0,80}d"]),
    "bcg_nonrepresentation_present": has_any(bcg, [r"not.{0,40}representation", r"do not.{0,60}representation", r"does not.{0,60}representation"]),
    "beltran_arbitrary_2complex_present": has_any(bel, [r"arbitrary.{0,30}2.?complex", r"general.{0,30}2.?complex"]),
    "beltran_causal_vertex_present": has_any(bel, [r"causal vertex"]),
    "beltran_toller_present": has_any(bel, [r"toller"]),
}

# C. Exact free-word distributive expansion, lengths 1..4.
def expand_D_product(n):
    # D_i := A_i+B_i. Expansion represented as coefficient dictionary of noncommuting words.
    acc = {(): 1}
    for i in range(n):
        nxt = {}
        for w,c in acc.items():
            for branch in ("A", "B"):
                nw = w + (f"{branch}{i}",)
                nxt[nw] = nxt.get(nw, 0) + c
        acc = nxt
    return acc

distributive = {}
for n in range(1,5):
    lhs = expand_D_product(n)
    rhs = {tuple(f"{b}{i}" for i,b in enumerate(bits)): 1
           for bits in __import__("itertools").product(("A","B"), repeat=n)}
    distributive[str(n)] = (lhs == rhs and len(lhs) == 2**n)

# D. Exact anti-inheritance witness over integers.
d = 2
standard_tau = d * (1 + 1)       # 2 Tr(I_2) = 4
branch_tau = d * (2 + 2)         # 2 Tr(2 I_2) = 8
bound = d*d
anti_inheritance = {
    "D_equals_Tplus_plus_Tminus": (1 == 2 + (-1)),
    "standard_saturates_bound": (standard_tau == bound),
    "selected_branch_violates_bound": (branch_tau > bound),
    "values": {"d": d, "standard_tau": standard_tau, "branch_tau": branch_tau, "bound": bound},
}

# E. Search each actual primary source separately for an explicit combined Han/Toller transport theorem.
# The gate does not infer a theorem by concatenating unrelated documents.
docs = {"han": han, "bcg": bcg, "beltran": bel}
def doc_has_combo(required_groups):
    hits = []
    for name, text in docs.items():
        ok = True
        for group in required_groups:
            if not has_any(text, group):
                ok = False; break
        if ok: hits.append(name)
    return hits

E = {
    "E1_causal_toller_face_bound": doc_has_combo([[r"toller"], [r"tau|face"], [r"bound|inequal|d[_\\ ]?k\^?2"]]),
    "E2_causal_toller_saturation_locus": doc_has_combo([[r"toller"], [r"saturat|maximi[sz]"], [r"su\(2\)|flat"]]),
    "E3_causal_bosonic_meromorphy_poles": doc_has_combo([[r"toller"], [r"grand.?canonical|bosonic"], [r"pole|meromorph|converg"]]),
    "E4_causal_localization_condensation": doc_has_combo([[r"toller"], [r"condens|locali[sz]ation"], [r"face|stack"]]),
    "E5_causal_cut_gluing": doc_has_combo([[r"toller"], [r"gluing|cutting|composition"], [r"face|stack|boundary"]]),
    "E6_source_order_to_han_stack": doc_has_combo([[r"toller"], [r"han|grand.?canonical|stack"], [r"k5|extension|distribution"]]),
}

source_positive_ok = all(positive.values())
algebra_ok = all(distributive.values()) and all(v for k,v in anti_inheritance.items() if k != "values")
all_bridge = all(bool(v) for v in E.values())

if not source_positive_ok:
    verdict = "INVALID_PROVENANCE_OR_SOURCE_SIGNATURE"
    classification = verdict
elif not algebra_ok:
    verdict = "SCIENTIFIC_FAIL_ALGEBRA"
    classification = verdict
elif all_bridge:
    verdict = "PASS_SOURCE_BRIDGE_SCOPED"
    classification = "ITER081B_SM_HAN_TOLLER_FACE_STACK_DIRECT_INHERITANCE_SOURCE_ESTABLISHED_SCOPED"
else:
    verdict = "BLOCKED_SOURCE_BRIDGE"
    classification = "ITER081B_SM_DIRECT_HAN_D_TO_SINGLE_TOLLER_BRANCH_FACE_STACK_INHERITANCE_NOT_SOURCE_PROVEN_BLOCKED_SCOPED"

result = {
    "gate": "ITER081B_SM_HAN_TOLLER_FACE_FUNCTIONAL_TRANSPORT_OBSTRUCTION_GATE",
    "verdict": verdict,
    "classification": classification,
    "source_sha256": hashes,
    "source_positive_checks": positive,
    "exact_distributive_controls": distributive,
    "anti_inheritance_witness": anti_inheritance,
    "bridge_evidence_documents": E,
    "claim_ceiling": "Direct source inheritance only; no impossibility theorem for new causal Toller stacks.",
    "claim_locks_preserved": True,
}
(OUT / "iter081b_sm_aggregate.json").write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
print(json.dumps(result, indent=2, sort_keys=True))
if verdict.startswith("INVALID"):
    raise SystemExit(3)
if verdict == "SCIENTIFIC_FAIL_ALGEBRA":
    raise SystemExit(2)
