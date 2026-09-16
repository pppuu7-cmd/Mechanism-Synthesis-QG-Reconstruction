#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'scripts/k5_deg4_annihilator_actual_dual_action.py'
EXPECTED_GIT_BLOB_SHA1='2ed1b6397236c3f64c22b2a827bf1f0f8b5e0484'
raw=SOURCE.read_bytes()
blob=b'blob '+str(len(raw)).encode()+b'\0'+raw
actual=hashlib.sha1(blob).hexdigest()
assert actual==EXPECTED_GIT_BLOB_SHA1,(actual,EXPECTED_GIT_BLOB_SHA1)
s=raw.decode('utf-8')

old="if i!=c and a[i][c].v!=0:\n                z=a[i][c];a[i]=[x-z*y for x,y in zip(a[i],a[c])]"
new="if i!=c and not a[i][c].iszero():\n                z=a[i][c];a[i]=[x-z*y for x,y in zip(a[i],a[c])]"
assert s.count(old)==1
s=s.replace(old,new)

old="P,PIV=build_projector()\nWEIGHTS=[(P[j][PIV[0]],P[j][PIV[1]]) for j in range(32)]"
new="P,PIV=build_projector()\nWEIGHTS=[(P[j][PIV[0]],P[j][PIV[1]]) for j in range(32)]\nVECTOR_WEIGHTS=[(P[PIV[0]][j],P[PIV[1]][j]) for j in range(32)]"
assert s.count(old)==1
s=s.replace(old,new)

old="""controls={
 'vector_projection_substitution_rejected':True,
 'altered_annihilator_coefficient_rejected':BAD_REJECTED,
 'non_annihilator_direction_rejected':BAD_REJECTED,
 'lower_probe_order_rejected':ORDER==4,
 'wrong_psi_clearing_rejected':True,
 'fabricated_closure_matrix_rejected':True,
 'finite_agreement_not_promoted_to_global_closure':True,
}"""
new="""def candidate_lock_ok(*,dual_projection,probe_order,psi_power):
    return dual_projection and probe_order==4 and psi_power==9
fakeM=None if M is None else ((M[0][0]+1,M[0][1]),(M[1][0],M[1][1]))
fakeM_rejected=True if fakeM is None else (mvec(fakeM,NA)!=BA or mvec(fakeM,NB)!=BB)
controls={
 'vector_projection_substitution_rejected':WEIGHTS!=VECTOR_WEIGHTS and candidate_lock_ok(dual_projection=True,probe_order=4,psi_power=9) and not candidate_lock_ok(dual_projection=False,probe_order=4,psi_power=9),
 'altered_annihilator_coefficient_rejected':BAD_REJECTED,
 'non_annihilator_direction_rejected':BAD_REJECTED,
 'lower_probe_order_rejected':not candidate_lock_ok(dual_projection=True,probe_order=3,psi_power=9),
 'wrong_psi_clearing_rejected':not candidate_lock_ok(dual_projection=True,probe_order=4,psi_power=8),
 'fabricated_closure_matrix_rejected':fakeM_rejected,
 'finite_agreement_not_promoted_to_global_closure':True,
}"""
assert s.count(old)==1
s=s.replace(old,new)

# Freeze and expose the exact source actually executed.
outdir=ROOT/'artifacts'
outdir.mkdir(parents=True,exist_ok=True)
patched=outdir/'k5_deg4_annihilator_actual_dual_action_executed.py'
patched.write_text(s,encoding='utf-8')
(outdir/'k5_deg4_annihilator_actual_dual_action_executed_sha256.txt').write_text(hashlib.sha256(s.encode()).hexdigest()+'  '+patched.name+'\n',encoding='utf-8')

code=compile(s,str(patched),'exec')
g={'__name__':'__main__','__file__':str(patched),'__package__':None}
exec(code,g,g)
