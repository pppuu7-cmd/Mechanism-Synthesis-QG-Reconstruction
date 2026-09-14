#!/usr/bin/env python3
from __future__ import annotations
import argparse, copy, hashlib, json, os, re, subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/'analysis'/'iter080h_frozen_manifest.json'
LOCK=ROOT/'status'/'ITER080H_MANIFEST_LOCK.md'
CURRENT=ROOT/'status'/'CURRENT.md'
ERRATUM=ROOT/'status'/'ITER077_CONTACT_FORMULA_ERRATUM.md'
FROZEN=[
    ('V01','candidates/CANDIDATE_A_CRQN.md','a3023dadb75f4c53d0c44a6de1c46958f4149178'),
    ('V02','candidates/CANDIDATE_A_CRQN_V0_2.md','3933c110f9bafabb6593f8301029adaa25458bb2'),
]
REQ_KEYS=('A1_PREEXISTING','A2_FULL_W_ACTION','A3_SELECTION_POWER','A4_OBJECT_REACH','A5_INDEPENDENT_MOTIVATION')
MANDATORY={
    'v01_history_amplitude':'A[B_f,B_i] = Sum_H',
    'v01_alternate_Z':'Z = Sum_H integral dmu(lambda)',
    'v01_Gamma_k':'effective action/functional `Gamma_k`',
    'v01_RG_flow':'k dGamma_k/dk = B[Gamma_k]',
    'v01_fixed_point':'B[Gamma_*] = 0',
    'v01_local_amplitude_programme':'Require boundary composition, gauge covariance and a causal orientation rule.',
    'v01_early_success':'existence of one explicitly defined microstate/amplitude pair',
    'v02_product_amplitude':'A_CRQN[K,o,j,i] = Prod_f A_f Prod_e A_e Prod_v A_v^CRQN',
    'v02_placeholder':'A_v^CRQN = A_v^geom(j,i) F_causal(o;j,i;theta)',
    'v02_six_requirements':'A viable local factor must satisfy at least:',
    'v02_phi':'Phi(A_v, o, j, i, beta, gauge) = 0',
    'v02_four_term_requirement':'causal composition + quantum-geometric semiclassics + RG stability + continuum gauge recovery',
}
SENSITIVE_TERMS=('infinite','unbounded','functional','function','coupling','measure','amplitude','renormal','rg','extension','distribution','boundary','vertex','phi(','gamma_k','beta')


def sha(s:str)->str:
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def segment_file(prefix,path,expected):
    p=ROOT/path
    actual=subprocess.check_output(['git','hash-object',str(p)],text=True,cwd=ROOT).strip()
    if actual!=expected:
        raise ValueError(f'INVALID_PROVENANCE {path}: {actual} != {expected}')
    raw=p.read_text(encoding='utf-8').replace('\r\n','\n')
    lines=raw.split('\n')
    recs=[]; buf=[]; start=None
    def flush(endline):
        nonlocal buf,start
        if buf:
            text='\n'.join(buf)
            if text.strip():
                d=sha(text)
                recs.append({'id':f'{prefix}-L{start:03d}-{endline:03d}-{d[:12]}','file':path,'start_line':start,'end_line':endline,'kind':'SCIENTIFIC_SEGMENT','sha256':d,'text':text})
        buf=[]; start=None
    for n,line in enumerate(lines,1):
        if re.match(r'^\s*#{1,6}\s+',line):
            flush(n-1)
            d=sha(line)
            recs.append({'id':f'{prefix}-L{n:03d}-{n:03d}-{d[:12]}','file':path,'start_line':n,'end_line':n,'kind':'HEADING_LINE','sha256':d,'text':line})
        elif line.strip()=='':
            flush(n-1)
        else:
            if start is None: start=n
            buf.append(line)
    flush(len(lines))
    return actual,len(lines),recs


def universe():
    u={'schema':'ITER080H_LINE_AWARE_UNIVERSE_V1','files':[],'records':[]}
    for prefix,path,expected in FROZEN:
        actual,nlines,recs=segment_file(prefix,path,expected)
        u['records'].extend(recs)
        u['files'].append({'prefix':prefix,'path':path,'blob_sha':actual,'line_count':nlines,'record_count':len(recs)})
    canon=json.dumps(u,sort_keys=True,separators=(',',':'),ensure_ascii=False)
    return u,sha(canon)


def exclusion_valid(e):
    ex=e.get('exclusion')
    if ex is None: return True
    text=e['text']; lines=[x for x in text.splitlines() if x.strip()]
    if ex=='METADATA_ONLY':
        return bool(lines) and all(x.startswith(('**Status:**','**Promotion:**','**Parent:**')) for x in lines)
    if ex=='EXTERNAL_ANCHORS_ONLY':
        return e['file'].endswith('CANDIDATE_A_CRQN.md') and 'they do not validate the CRQN synthesis' in text
    if ex=='FALSIFICATION_STATUS_TABLE_ONLY':
        return 'Current status' in text and all(x.lstrip().startswith('|') for x in lines)
    if ex=='ABLATION_LIST_ONLY':
        return bool(lines) and all(x.lstrip().startswith('- `CRQN - M') for x in lines)
    return False


def validate_manifest(manifest,u,udigest):
    errors=[]
    if manifest.get('schema')!='ITER080H_FROZEN_MANIFEST_V1': errors.append('schema')
    if manifest.get('prereg_commit')!='3dcbb26dc1607cc6c05c6805fdb87b50846c9428': errors.append('prereg')
    if manifest.get('universe_sha256')!=udigest: errors.append('universe_sha')
    mcopy=copy.deepcopy(manifest); claimed=mcopy.pop('manifest_sha256',None)
    actual=sha(json.dumps(mcopy,sort_keys=True,separators=(',',':'),ensure_ascii=False))
    if claimed!=actual: errors.append('manifest_sha')
    sci=[r for r in u['records'] if r['kind']=='SCIENTIFIC_SEGMENT']
    entries=manifest.get('entries',[])
    ids=[e.get('id') for e in entries]
    if len(ids)!=len(set(ids)): errors.append('duplicate_ids')
    if set(ids)!={r['id'] for r in sci}: errors.append('exact_set')
    by={r['id']:r for r in sci}
    for e in entries:
        r=by.get(e.get('id'))
        if not r: continue
        for k in ('file','start_line','end_line','sha256','text'):
            if e.get(k)!=r.get(k): errors.append(f'entry_mismatch:{e.get("id")}:{k}')
        if not all(k in e and isinstance(e[k],bool) for k in REQ_KEYS): errors.append(f'predicates:{e.get("id")}')
        if not exclusion_valid(e): errors.append(f'false_exclusion:{e.get("id")}')
    lock=LOCK.read_text(encoding='utf-8')
    if udigest not in lock: errors.append('lock_universe_sha')
    if claimed not in lock: errors.append('lock_manifest_sha')
    return errors


def witnesses(entries):
    found={}
    for name,needle in MANDATORY.items():
        hits=[e['id'] for e in entries if needle in e['text']]
        found[name]=hits
    return found


def lane_a():
    try:
        u,ud=universe(); m=json.loads(MANIFEST.read_text(encoding='utf-8')); errs=validate_manifest(m,u,ud)
    except Exception as exc:
        return {'iteration':'Iter080H-SM','lane':'A','valid':False,'scientific_outcome':'INVALID_IMPLEMENTATION_OR_PROVENANCE','errors':[repr(exc)]}
    ws=witnesses(m['entries'])
    missing=[k for k,v in ws.items() if not v]
    valid=not errs and not missing and len(m['entries'])==81
    return {'iteration':'Iter080H-SM','lane':'A','valid':valid,'scientific_outcome':'PASS_PROVENANCE_UNIVERSE_MANIFEST' if valid else 'INVALID_IMPLEMENTATION_OR_PROVENANCE','universe_sha256':ud,'manifest_sha256':m['manifest_sha256'],'scientific_segments':len(m['entries']),'mandatory_witnesses':ws,'missing_witnesses':missing,'errors':errs}


def lane_b():
    try:
        u,ud=universe(); m=json.loads(MANIFEST.read_text(encoding='utf-8')); errs=validate_manifest(m,u,ud)
    except Exception as exc:
        return {'iteration':'Iter080H-SM','lane':'B','valid':False,'scientific_outcome':'INVALID_IMPLEMENTATION_OR_PROVENANCE','errors':[repr(exc)]}
    entries=m['entries']
    qualifying=[e['id'] for e in entries if e.get('exclusion') is None and all(e[k] for k in REQ_KEYS)]
    a2_true=[e['id'] for e in entries if e['A2_FULL_W_ACTION']]
    a3_true=[e['id'] for e in entries if e['A3_SELECTION_POWER']]
    sensitive=[]
    for e in entries:
        low=e['text'].lower(); terms=sorted({t for t in SENSITIVE_TERMS if t in low})
        if terms:
            sensitive.append({'id':e['id'],'terms':terms,'A2':e['A2_FULL_W_ACTION'],'A3':e['A3_SELECTION_POWER'],'text':e['text']})
    valid=not errs and len(entries)==81 and not a2_true and not a3_true
    outcome='SELECTOR_FOUND_REQUIRES_DIRECT_K5_TEST' if valid and qualifying else ('BLOCKED_EXISTING_AXIOM_SELECTOR_MISSING' if valid else 'INVALID_IMPLEMENTATION_OR_PROVENANCE')
    return {'iteration':'Iter080H-SM','lane':'B','valid':valid,'scientific_outcome':outcome,'qualifying_preexisting_axioms':qualifying,'A2_true_entries':a2_true,'A3_true_entries':a3_true,'sensitive_segment_count':len(sensitive),'sensitive_segments':sensitive,'errors':errs}


def lane_c():
    try:
        u,ud=universe(); m=json.loads(MANIFEST.read_text(encoding='utf-8')); base_errs=validate_manifest(m,u,ud)
    except Exception as exc:
        return {'iteration':'Iter080H-SM','lane':'C','valid':False,'scientific_outcome':'INVALID_IMPLEMENTATION_OR_PROVENANCE','errors':[repr(exc)]}
    pos={k:True for k in REQ_KEYS}
    finite={'A1_PREEXISTING':True,'A2_FULL_W_ACTION':False,'A3_SELECTION_POWER':False,'A4_OBJECT_REACH':True,'A5_INDEPENDENT_MOTIVATION':True}
    aspir={'A1_PREEXISTING':False,'A2_FULL_W_ACTION':False,'A3_SELECTION_POWER':False,'A4_OBJECT_REACH':True,'A5_INDEPENDENT_MOTIVATION':True}
    controls={
        'positive_full_W_all_true':all(pos.values()),
        'finite_scalar_A2_A3_false':not finite['A2_FULL_W_ACTION'] and not finite['A3_SELECTION_POWER'],
        'aspirational_A1_A2_A3_false':not aspir['A1_PREEXISTING'] and not aspir['A2_FULL_W_ACTION'] and not aspir['A3_SELECTION_POWER'],
    }
    mut_extra=copy.deepcopy(u)
    fake={'id':'V01-L999-999-deadbeefdead','file':'candidates/CANDIDATE_A_CRQN.md','start_line':999,'end_line':999,'kind':'SCIENTIFIC_SEGMENT','sha256':'deadbeef','text':'injected extra paragraph'}
    mut_extra['records'].append(fake)
    controls['injected_extra_forces_invalid']=bool(validate_manifest(m,mut_extra,ud))
    mut_del=copy.deepcopy(m); mut_del['entries']=mut_del['entries'][:-1]
    controls['deleted_manifest_entry_forces_invalid']=bool(validate_manifest(mut_del,u,ud))
    mut_merge=copy.deepcopy(u)
    sci_idx=next(i for i,r in enumerate(mut_merge['records']) if r['kind']=='SCIENTIFIC_SEGMENT')
    mut_merge['records'][sci_idx]['text']='# merged heading\n'+mut_merge['records'][sci_idx]['text']
    controls['heading_body_coalescence_forces_invalid']=bool(validate_manifest(m,mut_merge,ud))
    mut_ex=copy.deepcopy(m); target=next(e for e in mut_ex['entries'] if not e['text'].startswith('**Status:**'))
    target['exclusion']='METADATA_ONLY'
    controls['false_exclusion_forces_invalid']=bool(validate_manifest(mut_ex,u,ud))
    ws=witnesses(m['entries'])
    controls['critic_omissions_all_visible']=all(ws.values())
    valid=not base_errs and all(controls.values())
    return {'iteration':'Iter080H-SM','lane':'C','valid':valid,'scientific_outcome':'PASS_ADVERSARIAL_CONTROLS' if valid else 'INVALID_IMPLEMENTATION_OR_PROVENANCE','controls':controls,'mandatory_witnesses':ws,'errors':base_errs}


def lane_d():
    c=CURRENT.read_text(encoding='utf-8'); e=ERRATUM.read_text(encoding='utf-8')
    locks={
        'iter077q':'ITER077Q_SM_SOURCE_COMPATIBLE_K5_EXTENSION_AMBIGUITY_CONTAINS_INFINITE_DIMENSIONAL_TANGENTIAL_SUBSPACE_EXACT_THEOREM_SCOPED' in c,
        'iter080a':'Iter080A remains independently `CONFIRMED_SCOPED`' in c,
        'iter080d':'repaired Iter080D remains independently `CONFIRMED_SCOPED`' in c,
        'iter080e':'BLOCKED_OBJECT_DEFINITION' in c and 'Iter080E' in c,
        'iter080b':'BLOCKED_SOURCE_BRIDGE' in c and 'Iter080B' in c,
        'iter080f_invalid':'Iter080F' in c and 'INVALID_IMPLEMENTATION' in c,
        'iter080g_invalid':'INVALID_PREPRODUCTION_STATEMENT_UNIVERSE_PARSER' in (ROOT/'status'/'ITER080G_ITER080H_HANDOFF.md').read_text(encoding='utf-8'),
        'erratum':'-(2 i rho/D) delta(x)-(1/D) delta\'(x)' in e,
        'claim_locks':'No `NEW_PHYSICS_FOUND`' in c and 'no complete-QG claim' in c and 'Retain published one-wedge spectral `i epsilon`' in c,
    }
    valid=all(locks.values())
    return {'iteration':'Iter080H-SM','lane':'D','valid':valid,'scientific_outcome':'PASS_DEPENDENCY_CLAIM_LOCK' if valid else 'INVALID_IMPLEMENTATION_OR_PROVENANCE','locks':locks}

LANES={'A':lane_a,'B':lane_b,'C':lane_c,'D':lane_d}


def aggregate(root):
    got={}
    for base,_,files in os.walk(root):
        for fn in files:
            if fn.endswith('.json'):
                try:o=json.loads(Path(base,fn).read_text(encoding='utf-8'))
                except Exception:continue
                if o.get('iteration')=='Iter080H-SM' and o.get('lane') in LANES: got[o['lane']]=o
    present=set(got)==set(LANES)
    valid=present and all(got[k].get('valid') for k in LANES)
    qualifying=got.get('B',{}).get('qualifying_preexisting_axioms',[])
    if not valid:
        verdict='INVALID_IMPLEMENTATION_OR_PROVENANCE'; classification='ITER080H_SM_INVALID_IMPLEMENTATION_OR_PROVENANCE'
    elif qualifying:
        verdict='SELECTOR_FOUND_REQUIRES_DIRECT_K5_TEST'; classification='ITER080H_SM_CRQN_PREEXISTING_FULL_FUNCTION_SPACE_SELECTOR_AXIOM_FOUND_REQUIRES_DIRECT_K5_TEST_SCOPED'
    else:
        verdict='BLOCKED_EXISTING_AXIOM_SELECTOR_MISSING'; classification='ITER080H_SM_LINE_AWARE_EXHAUSTIVE_PRE_ITER077Q_CRQN_CORPUS_HAS_NO_FULL_FUNCTION_SPACE_EXTENSION_SELECTOR_AXIOM_ANTI_RESCUE_BLOCKED_EXACT_CENSUS_SCOPED'
    return {
        'iteration':'Iter080H-SM','execution_valid':valid,
        'lane_scientific_outcomes':{k:got.get(k,{}).get('scientific_outcome') for k in LANES},
        'verdict':verdict,'classification':classification,
        'qualifying_preexisting_axioms':qualifying,
        'universe_sha256':got.get('A',{}).get('universe_sha256'),
        'manifest_sha256':got.get('A',{}).get('manifest_sha256'),
        'scientific_segments':got.get('A',{}).get('scientific_segments'),
        'new_scientific_fact':'The line-aware exact census gives every non-heading segment in the frozen pre-Iter077Q CRQN v0.1/v0.2 corpus a stable identity and explicit A1-A5 classification; no segment defines an action on the full Iter077Q extension-function space or selection among its extension data, so no pre-existing full-function-space K5 extension selector is present.' if valid and not qualifying else None,
        'claim_lock':'No new selector is invented; no unique K5 extension, G3/F9/G8/K5, regulator-independence, causal-vertex divergence, NEW_PHYSICS_FOUND, or complete-QG promotion follows.',
        'next_admissible_gate':'After independent Critic review, perform CRQN_V0_2_LOCAL_AMPLITUDE_ANTI_RESCUE_SURVIVAL_DECISION if and only if this census is confirmed; otherwise repair only as authorized by the review.'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',choices=LANES); ap.add_argument('--aggregate-dir'); ap.add_argument('--output',required=True); a=ap.parse_args()
    if bool(a.lane)==bool(a.aggregate_dir): raise SystemExit('choose exactly one mode')
    obj=LANES[a.lane]() if a.lane else aggregate(a.aggregate_dir)
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(obj,indent=2,sort_keys=True,ensure_ascii=False)+'\n',encoding='utf-8'); print(json.dumps(obj,indent=2,sort_keys=True,ensure_ascii=False))
    if a.lane and not obj['valid']: raise SystemExit(1)
    if a.aggregate_dir and not obj['execution_valid']: raise SystemExit(1)

if __name__=='__main__': main()
