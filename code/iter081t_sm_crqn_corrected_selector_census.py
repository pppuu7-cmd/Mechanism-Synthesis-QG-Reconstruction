#!/usr/bin/env python3
import hashlib, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
CORPUS = [ROOT/'candidates/CANDIDATE_A_CRQN.md', ROOT/'candidates/CANDIDATE_A_CRQN_V0_2.md']
PREREG = ROOT/'prereg/ITER081T_SM_CRQN_RIGHT_SU2_INVARIANT_JET_SELECTOR_CENSUS.md'
CURRENT = ROOT/'status/CURRENT.md'
OUT = ROOT/'results/raw/iter081t_sm_aggregate.json'

POSITIVE_CONTROL = '''Local K5 extension selector. Let c_1,...,c_28 be the scalar SO(3) x S5 invariant normal-jet coefficients through order 8. Impose c_1=0, c_2=0, c_3=0, c_4=0, c_5=0, c_6=0, c_7=0, c_8=0, c_9=0, c_10=0, c_11=0, c_12=0, c_13=0, c_14=0, c_15=0, c_16=0, c_17=0, c_18=0, c_19=0, c_20=0, c_21=0, c_22=0, c_23=0, c_24=0, c_25=0, c_26=0, c_27=0, c_28=0. The 28x28 coefficient matrix is the identity and hence full rank. The rule is node-wise right-SU(2), S5 and boundary covariant and is applied after full boundary contraction at K5 extension.'''
NEGATIVE_CONTROL = 'Require causal composition + RG stability + continuum gauge recovery.'

def sha256_bytes(b): return hashlib.sha256(b).hexdigest()

def blocks(text):
    # Exhaustive nonempty paragraph/code/list blocks split only on blank lines.
    return [b.strip() for b in re.split(r'\n\s*\n', text) if b.strip()]

def features(text):
    low=text.lower()
    # Necessary evidence families for Q1-Q5. Q2/Q3 require target/reach + selection certificate.
    explicit_object = bool(re.search(r'\b(equation|normalization|boundary[- ]value|differential|spectral|extension|amplitude|operator|condition|rule)\b', low))
    target = ('normal-jet' in low or 'normal jet' in low or ('c_1' in low and 'c_28' in low) or ('order 8' in low and 'coefficient' in low))
    selection = (('28x28' in low or '28 x 28' in low or 'full rank' in low) and ('28' in low)) or ('uniqueness' in low and target)
    symmetry = ('su(2)' in low or 'su2' in low) and ('s5' in low) and ('boundary' in low) and ('covariant' in low)
    source_order = ('after full boundary contraction' in low and ('k5' in low) and ('extension' in low))
    return dict(Q1=explicit_object,Q2=target,Q3=selection,Q4=symmetry,Q5=source_order)

def qualifies(text):
    f=features(text)
    return all(f.values())

def main():
    invalid=[]
    if not PREREG.exists(): invalid.append('missing prereg')
    if not CURRENT.exists(): invalid.append('missing CURRENT')
    else:
        cur=CURRENT.read_text(encoding='utf-8')
        for token in ['RIGHT_SU2_COVARIANT_K5_INVARIANT_NORMAL_JET_COEFFICIENT_SELECTOR','Total demonstrated scalar invariant normal-jet dimension through order 8','28']:
            if token not in cur: invalid.append('missing CURRENT target lock: '+token)
    entries=[]
    for path in CORPUS:
        if not path.exists():
            invalid.append('missing corpus '+str(path.relative_to(ROOT))); continue
        raw=path.read_bytes(); text=raw.decode('utf-8')
        bs=blocks(text)
        if not bs: invalid.append('empty corpus '+str(path.relative_to(ROOT)))
        for i,b in enumerate(bs,1):
            entries.append({'file':str(path.relative_to(ROOT)),'block':i,'sha256':sha256_bytes(b.encode()),'features':features(b),'qualifies':qualifies(b),'text':b})
    pc=qualifies(POSITIVE_CONTROL)
    nc=qualifies(NEGATIVE_CONTROL)
    if not pc: invalid.append('positive synthetic control failed')
    if nc: invalid.append('negative synthetic control failed')
    positives=[e for e in entries if e['qualifies']]
    corpus_meta=[]
    for p in CORPUS:
        if p.exists(): corpus_meta.append({'file':str(p.relative_to(ROOT)),'sha256':sha256_bytes(p.read_bytes()),'blocks':len(blocks(p.read_text(encoding='utf-8')))})
    if invalid:
        classification='ITER081T_SM_INVALID'; verdict='INVALID_IMPLEMENTATION_OR_PROVENANCE'
    elif positives:
        classification='ITER081T_SM_CRQN_PREEXISTING_CORRECTED_INVARIANT_JET_SELECTOR_FOUND_EXACT_SCOPED'; verdict='PASS_PREEXISTING_SELECTOR_FOUND'
    else:
        classification='ITER081T_SM_CRQN_V0_1_V0_2_HAS_NO_PREEXISTING_CORRECTED_INVARIANT_JET_SELECTOR_BLOCKED_EXACT_CENSUS_SCOPED'; verdict='BLOCKED_EXISTING_CANDIDATE_SELECTOR_MISSING'
    agg={'schema':'iter081t-sm-v1','classification':classification,'verdict':verdict,'invalid_reasons':invalid,'corpus':corpus_meta,'block_count':len(entries),'qualifying_count':len(positives),'qualifying_blocks':positives,'positive_control':pc,'negative_control_rejected':not nc,'all_blocks':entries}
    OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(agg,indent=2,sort_keys=True),encoding='utf-8')
    print(json.dumps({k:agg[k] for k in ['classification','verdict','invalid_reasons','block_count','qualifying_count','positive_control','negative_control_rejected']},indent=2))
    if invalid: return 2
    return 0

if __name__=='__main__': sys.exit(main())
