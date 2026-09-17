#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CORE=ROOT/'scripts/k5_34_orbit_exact_leading_coefficient_core.py'
spec=importlib.util.spec_from_file_location('k5_34_exact_core',CORE)
c=importlib.util.module_from_spec(spec);assert spec.loader is not None;spec.loader.exec_module(c)


def same_poly(a,b):return a.d==b.d


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--shard',type=int,required=True);ap.add_argument('--nshards',type=int,default=8);ap.add_argument('--output',required=True);args=ap.parse_args()
    assert args.nshards==8 and 0<=args.shard<args.nshards
    stat=c.static_checks();classes=c.class_representatives();rows=[]
    assigned=[x for x in c.proper_orbits() if x[0]%args.nshards==args.shard]
    print('SHARD',args.shard,'assigned',[(x[0],x[1]) for x in assigned],flush=True)
    for pos,(idx,mask,size,k) in enumerate(assigned,1):
        print('ORBIT',idx,'mask',mask,'k',k,'routeA W1/W2',flush=True)
        a1=c.route_a(mask,c.W1);a2=c.route_a(mask,c.W2)
        mp=c.core.pmask(mask,c.CYCLE)
        s1=c.route_a(mp,c.WP1);s2=c.route_a(mp,c.WP2)
        route_checks={}
        for tag,a in (('W1',a1),('W2',a2),('S5_W1',s1),('S5_W2',s2)):
            for n,v in a['checks'].items():route_checks[f'{tag}_{n}']=bool(v)
        s5={}
        for ch in (0,1):
            s5[f'ch{ch+1}_W1_N_full_coefficients']=same_poly(a1['channels'][ch]['N'],s1['channels'][ch]['N'])
            s5[f'ch{ch+1}_W1_B_full_coefficients']=same_poly(a1['channels'][ch]['B'],s1['channels'][ch]['B'])
            s5[f'ch{ch+1}_W2_N_full_coefficients']=same_poly(a2['channels'][ch]['N'],s2['channels'][ch]['N'])
            s5[f'ch{ch+1}_W2_B_full_coefficients']=same_poly(a2['channels'][ch]['B'],s2['channels'][ch]['B'])
        key=(size,k);is_class_rep=classes[key]==(idx,mask);second=None
        if is_class_rep:
            print('ORBIT',idx,'independent interpolation route',key,flush=True)
            b=c.route_b_interpolation(mask,c.W1)
            second={'class':[size,k],'mask':mask,'channels':[],'all_exact':True}
            for ch in (0,1):
                n_ok=same_poly(b[ch]['N'],a1['channels'][ch]['N']);b_ok=same_poly(b[ch]['B'],a1['channels'][ch]['B'])
                second['channels'].append({
                    'channel':ch+1,'N_exact':n_ok,'B_exact':b_ok,
                    'N_sha256':c.vector_hash(b[ch]['N'],c.N_DEG),'B_sha256':c.vector_hash(b[ch]['B'],c.B_DEG),
                })
                second['all_exact'] &= n_ok and b_ok
        chrows=[]
        for ch in (0,1):
            w1=c.lane_serial(a1['channels'][ch]);w2=c.lane_serial(a2['channels'][ch])
            agreeN=(w1['N_exact_zero']==w2['N_exact_zero'] and w1['rN']==w2['rN'])
            agreeB=(w1['B_exact_zero']==w2['B_exact_zero'] and w1['rB']==w2['rB'])
            chrows.append({'channel':ch+1,'W1':w1,'W2':w2,'W1_W2_N_state_order_agree':agreeN,'W1_W2_B_state_order_agree':agreeB})
        rows.append({
            'orbit_index':idx,'mask':mask,'bits':[i for i in range(10) if (mask>>i)&1],'k':k,'orbit_size':size,
            'class':[size,k],'class_validation_representative':is_class_rep,'channels':chrows,
            'route_checks':route_checks,'s5_full_coefficient_checks':s5,'second_path':second,
            's5_transformed_mask':mp,
        })
        print('ORBIT',idx,'done',pos,'/',len(assigned),flush=True)
    out={
        'gate':'K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION_SHARD',
        'prereg_commit':c.PRE,'shard':args.shard,'nshards':args.nshards,'status':'SHARD_COMPLETE_EXACT_CONTROL_ONLY',
        'scientific_classification':None,'static_checks':stat,'rows':rows,
        'source_terms':c.SOURCE_TERMS,'retained_matchings':len(c.MATCH_COEFF),
        'degree_ceiling_N':c.N_DEG,'degree_ceiling_B':c.B_DEG,
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('SHARD_STATUS=SHARD_COMPLETE_EXACT_CONTROL_ONLY')

if __name__=='__main__':main()
