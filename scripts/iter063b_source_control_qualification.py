#!/usr/bin/env python3
import pathlib,re,json,hashlib
ROOT=pathlib.Path('.')
skip={'.git','.venv','venv','__pycache__'}
text_files=[]
for p in ROOT.rglob('*'):
    if not p.is_file() or any(part in skip for part in p.parts): continue
    if p.suffix.lower() not in {'.md','.txt','.tex','.json','.yaml','.yml','.py'}: continue
    try: txt=p.read_text(errors='strict')
    except Exception: continue
    text_files.append((p,txt))
patterns={
 'source_id':re.compile(r'(doi\s*[:/]?|arxiv\s*[: ]|https?://|source snapshot|immutable source)',re.I),
 'causal_object':re.compile(r'(causal.{0,40}vertex|direct.{0,40}vertex|T[ _^]*[+−-].{0,80}T[ _^]*[-−]|branch-resolved)',re.I|re.S),
 'eprl_relation':re.compile(r'(EPRL.{0,140}(sum|recover|standard|limit|orientation|branch)|(?:sum|recover|standard|limit|orientation|branch).{0,140}EPRL)',re.I|re.S),
 'conventions':re.compile(r'(kappa|κ).{0,120}(ordered|wedge|spectral|branch|eta|η)|(ordered|wedge|spectral|branch|eta|η).{0,120}(kappa|κ)',re.I|re.S),
 'basis_independent':re.compile(r'(tree|cycle[- ]basis|permutation|order independence|basis independence)',re.I)
}
hits={k:[] for k in patterns}
for p,txt in text_files:
    lines=txt.splitlines()
    for k,pat in patterns.items():
        for m in pat.finditer(txt):
            ln=txt.count('\n',0,m.start())+1
            snippet=' '.join(lines[max(0,ln-2):min(len(lines),ln+1)])[:500]
            hits[k].append({'file':str(p),'line':ln,'snippet':snippet})
            if len(hits[k])>=20: break
qualified=all(hits[k] for k in patterns)
# Stronger relation requirement: at least one file contains source-id, causal object, EPRL relation, and conventions together.
qualified_files=[]
for p,txt in text_files:
    if all(patterns[k].search(txt) for k in ('source_id','causal_object','eprl_relation','conventions')):
        qualified_files.append(str(p))
if not qualified_files: qualified=False
if qualified:
    cls='ITER063B_SOURCE_CONTROL_QUALIFIED'
elif not hits['source_id']:
    cls='ITER063B_SOURCE_CONTROL_BLOCKED_NO_IMMUTABLE_SOURCE'
elif not hits['eprl_relation'] or not qualified_files:
    cls='ITER063B_SOURCE_CONTROL_BLOCKED_MISSING_EXPLICIT_RELATION'
elif not hits['conventions']:
    cls='ITER063B_SOURCE_CONTROL_BLOCKED_MISSING_CONVENTIONS'
else:
    cls='ITER063B_SOURCE_CONTROL_BLOCKED_MISSING_EXPLICIT_RELATION'
out={'iteration':'Iter063B','classification':cls,'qualified':qualified,'qualified_files':qualified_files,'hit_counts':{k:len(v) for k,v in hits.items()},'hits':hits,'files_scanned':len(text_files),'prereg_commit':'75fb19ed4644ca422a3954ef8e231d8e35c92fc4','interpretation':'source qualification only; no causal amplitude/EPRL numerical PASS and no K5/G3/F9/G8 promotion'}
path='iter063b_source_control_qualification.json'; pathlib.Path(path).write_text(json.dumps(out,indent=2,sort_keys=True))
print(json.dumps({k:v for k,v in out.items() if k!='hits'},indent=2,sort_keys=True))
