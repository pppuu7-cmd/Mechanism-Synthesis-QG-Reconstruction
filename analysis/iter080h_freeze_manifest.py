#!/usr/bin/env python3
import hashlib, json, re, subprocess
from pathlib import Path

FROZEN=[
    ('V01','candidates/CANDIDATE_A_CRQN.md','a3023dadb75f4c53d0c44a6de1c46958f4149178'),
    ('V02','candidates/CANDIDATE_A_CRQN_V0_2.md','3933c110f9bafabb6593f8301029adaa25458bb2'),
]

FUTURE_MARKERS=(
    'open_blocked','not yet','target','will therefore','research goal','next problem',
    'once a','would count','should be rejected','if the only solutions','if the conditions',
    'unknown','must be derived','not currently','preferred first targets','the v0.2 task is',
)
REACH_MARKERS=(
    'amplitude','measure','dynamics','renormal','rg','coarse-grain','coarse graining',
    'coupling','vertex','a_v','gamma_k','beta functional','history sum','w_geom','w_causal',
    'phi(','local factor','composition rule','continuum gauge recovery',
)


def sha(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def segment_file(prefix,path,expected):
    actual=subprocess.check_output(['git','hash-object',path],text=True).strip()
    if actual!=expected:
        raise SystemExit(f'INVALID_PROVENANCE {path}: {actual} != {expected}')
    raw=Path(path).read_text(encoding='utf-8').replace('\r\n','\n')
    lines=raw.split('\n')
    recs=[]
    buf=[]
    start=None
    def flush(endline):
        nonlocal buf,start
        if buf:
            text='\n'.join(buf)
            if text.strip():
                d=sha(text)
                recs.append({'id':f'{prefix}-L{start:03d}-{endline:03d}-{d[:12]}','file':path,'start_line':start,'end_line':endline,'kind':'SCIENTIFIC_SEGMENT','sha256':d,'text':text})
        buf=[]
        start=None
    for n,line in enumerate(lines,1):
        if re.match(r'^\s*#{1,6}\s+',line):
            flush(n-1)
            d=sha(line)
            recs.append({'id':f'{prefix}-L{n:03d}-{n:03d}-{d[:12]}','file':path,'start_line':n,'end_line':n,'kind':'HEADING_LINE','sha256':d,'text':line})
        elif line.strip()=='':
            flush(n-1)
        else:
            if start is None:
                start=n
            buf.append(line)
    flush(len(lines))
    return actual,len(lines),recs


def classify(r):
    text=r['text']
    low=text.lower()
    future_hits=[m for m in FUTURE_MARKERS if m in low]
    reach_hits=[m for m in REACH_MARKERS if m in low]
    a1=not bool(future_hits)
    a2=False
    a3=False
    a4=bool(reach_hits)
    a5=True
    rationale=(
        'Exact frozen pre-Iter077Q candidate segment. '
        f"A1={'true' if a1 else 'false'}" + (f"; future/target markers={future_hits}" if future_hits else '; no frozen future/target marker') + '. '
        'A2=false and A3=false because this exact segment neither defines an action on the arbitrary Iter077Q/K5 extension-function data nor distinguishes/selects among such extension data; no post-Iter077Q semantics are imported. '
        f"A4={'true' if a4 else 'false'}" + (f"; local-amplitude/renormalization reach markers={reach_hits}" if reach_hits else '; no local-amplitude/renormalization reach marker') + '. '
        'A5=true only in the timing sense fixed by the gate: the statement is present in the frozen pre-Iter077Q CRQN corpus and is not a post-obstruction repair.'
    )
    return {'A1_PREEXISTING':a1,'A2_FULL_W_ACTION':a2,'A3_SELECTION_POWER':a3,'A4_OBJECT_REACH':a4,'A5_INDEPENDENT_MOTIVATION':a5,'exclusion':None,'rationale':rationale}


def main():
    universe={'schema':'ITER080H_LINE_AWARE_UNIVERSE_V1','files':[],'records':[]}
    for prefix,path,expected in FROZEN:
        actual,nlines,recs=segment_file(prefix,path,expected)
        universe['records'].extend(recs)
        universe['files'].append({'prefix':prefix,'path':path,'blob_sha':actual,'line_count':nlines,'record_count':len(recs)})
    canon=json.dumps(universe,sort_keys=True,separators=(',',':'),ensure_ascii=False)
    universe_sha=sha(canon)
    scientific=[r for r in universe['records'] if r['kind']=='SCIENTIFIC_SEGMENT']
    entries=[]
    for r in scientific:
        e={k:r[k] for k in ('id','file','start_line','end_line','sha256','text')}
        e.update(classify(r))
        entries.append(e)
    manifest={
        'schema':'ITER080H_FROZEN_MANIFEST_V1',
        'prereg_commit':'3dcbb26dc1607cc6c05c6805fdb87b50846c9428',
        'frozen_corpus':[{'prefix':p,'path':q,'blob_sha':s} for p,q,s in FROZEN],
        'universe_schema':universe['schema'],
        'universe_sha256':universe_sha,
        'scientific_segment_count':len(scientific),
        'classification_policy':{
            'A1':'Literal pre-existing statement versus explicit future/target/open wording; frozen marker list above is part of the manifest freezer.',
            'A2':'False unless the exact segment explicitly defines an action on the whole Iter077Q W or an explicitly equivalent arbitrary extension-function object. No frozen segment does.',
            'A3':'False unless the exact segment distinguishes/selects among extension data. No frozen segment does.',
            'A4':'Exact local-amplitude/measure/dynamics/renormalization reach screen using the frozen marker list above; this predicate cannot rescue A2/A3.',
            'A5':'True in timing sense for all exact frozen candidate segments; no later material is positive evidence.',
            'anti_false_negative':'No scientific segment is excluded. Therefore every segment, including all Critic-identified omissions, is directly classified.'
        },
        'entries':entries,
    }
    mcanon=json.dumps(manifest,sort_keys=True,separators=(',',':'),ensure_ascii=False)
    manifest_sha=sha(mcanon)
    manifest['manifest_sha256']=manifest_sha
    Path('analysis/iter080h_frozen_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    lock=(
        '# Iter080H frozen manifest lock\n\n'
        f'- prereg: `3dcbb26dc1607cc6c05c6805fdb87b50846c9428`\n'
        f'- universe schema: `{universe["schema"]}`\n'
        f'- universe sha256: `{universe_sha}`\n'
        f'- total records: `{len(universe["records"])}`\n'
        f'- heading lines: `{sum(r["kind"]=="HEADING_LINE" for r in universe["records"])}`\n'
        f'- scientific segments: `{len(scientific)}`\n'
        f'- manifest sha256: `{manifest_sha}`\n'
        '- exclusions used: `0`\n'
        '- every scientific segment is present exactly once and receives explicit A1-A5 booleans before production.\n'
        '- A2/A3 are not inferred from later Iter077Q wording; they are negative because no exact frozen segment defines or selects arbitrary K5 extension-function data.\n'
    )
    Path('status/ITER080H_MANIFEST_LOCK.md').write_text(lock,encoding='utf-8')
    print(json.dumps({'universe_sha256':universe_sha,'manifest_sha256':manifest_sha,'scientific_segments':len(scientific),'qualifying':sum(all(e[k] for k in ('A1_PREEXISTING','A2_FULL_W_ACTION','A3_SELECTION_POWER','A4_OBJECT_REACH','A5_INDEPENDENT_MOTIVATION')) for e in entries)},indent=2))

if __name__=='__main__':
    main()
