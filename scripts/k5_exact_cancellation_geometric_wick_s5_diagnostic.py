#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
RESOLVER=ROOT/'scripts/k5_34_orbit_exact_leading_coefficient_cancellation_resolution.py'
PREREG='4262e9b55308ba9128eeca2cd195ae0672772bed'

spec=importlib.util.spec_from_file_location('resolver_geom_s5',RESOLVER)
r=importlib.util.module_from_spec(spec); assert spec.loader is not None; spec.loader.exec_module(r)
core=r.core
CYCLE=tuple(r.CYCLE)
WITNESSES={'W1':tuple(r.W1),'W2':tuple(r.W2)}

def invperm(p): return tuple(p.index(i) for i in range(len(p)))
def edge_sign(p,i):
    a,b=core.EDGES[i]
    return 1 if p[a] < p[b] else -1

def series(alpha):
    aa=[r.D(Fraction(x),0) for x in alpha]
    L=r.build_L(aa); psi=r.psi_direct(aa)
    if psi.v==0: raise ZeroDivisionError('generic psi zero')
    B0=r.inv_cofactor(L,psi)
    return r.inverse_series(B0)

def cov_series(Bser):
    return {(i,j):tuple(r.dot_mat(core.ROWS[i],Bser[n],core.ROWS[j]).v for n in range(r.ORDER+1))
            for i in range(10) for j in range(i+1,10)}

def transform_types(types,p):
    out=[None]*10
    for i,(a,b) in enumerate(types):
        j=core.ep(p,i)
        out[j]=(a,b) if edge_sign(p,i)==1 else (b,a)
    return tuple(out)

def transform_tcw(d,p):
    out={}; collision=False
    for types,w in d.items():
        k=transform_types(types,p)
        if k in out and out[k]!=w: collision=True
        out[k]=w
    return out,collision

def recompress(tcw):
    mc=defaultdict(lambda:[[Fraction(0),Fraction(0)],[Fraction(0),Fraction(0)]])
    for types,w in tcw.items():
        for mt,z in core.compatible(types):
            for ch in (0,1):
                if w[ch]:
                    zz=core.cscale(w[ch],z)
                    mc[mt][ch][0]+=zz[0]; mc[mt][ch][1]+=zz[1]
    return {mt:((c[0][0],c[0][1]),(c[1][0],c[1][1])) for mt,c in mc.items() if any(c[ch] != [0,0] for ch in (0,1))}

def projected_with_match(Bser,match):
    cov={(i,j):[r.dot_mat(core.ROWS[i],Bser[n],core.ROWS[j]) for n in range(r.ORDER+1)] for i in range(10) for j in range(i+1,10)}
    ch=[[(r.D(0),r.D(0)) for _ in range(r.ORDER+1)] for _ in range(2)]
    for mt,(c0,c1) in match.items():
        ser=[(r.D(1),r.D(0))]+[(r.D(0),r.D(0)) for _ in range(r.ORDER)]
        for ij in mt: ser=r.csmul(ser,[(x,r.D(0)) for x in cov[ij]])
        for n,x in enumerate(ser):
            for ci,c in enumerate((c0,c1)):
                if c!=(0,0): ch[ci][n]=r.cadd(ch[ci][n],(c[0]*x[0]-c[1]*x[1],c[0]*x[1]+c[1]*x[0]))
    return tuple(tuple((z[0].v,z[1].v) for z in lane) for lane in ch)

def check_direction(alpha,p):
    palpha=tuple(r.core.perm_weights(alpha,p))
    B=series(alpha); BP=series(palpha)
    C=cov_series(B); CP=cov_series(BP)
    mism=[]
    for (i,j),vals in C.items():
        ii,jj=core.ep(p,i),core.ep(p,j); key=(min(ii,jj),max(ii,jj)); s=edge_sign(p,i)*edge_sign(p,j)
        rhs=tuple(Fraction(s)*x for x in vals)
        if CP[key]!=rhs:
            mism.append({'pair':[i,j],'target_pair':[ii,jj],'base':[str(x) for x in vals],'target':[str(x) for x in CP[key]],'expected':[str(x) for x in rhs]})
            if len(mism)>=12: break
    tcw_t,col=transform_tcw(core.TCW,p); match_t=recompress(tcw_t)
    source_control=(not col and match_t==core.MATCH_COEFF)
    proj=projected_with_match(B,core.MATCH_COEFF)
    projp=projected_with_match(BP,match_t)
    proj_equal=(proj==projp)
    pm=[]
    if not proj_equal:
        for ch in range(2):
            for n in range(r.ORDER+1):
                if proj[ch][n]!=projp[ch][n]:
                    pm.append({'channel':ch+1,'series_order':n,'base':[str(x) for x in proj[ch][n]],'target':[str(x) for x in projp[ch][n]]})
    return {'permuted_alpha':[str(x) for x in palpha],
            'covariance_exact':not mism,'covariance_mismatch_sample':mism,
            'source_orientation_transpose_recompression_exact':source_control,
            'projected_channel_series_exact':proj_equal,'projected_mismatch_sample':pm[:12]}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); args=ap.parse_args()
    ip=invperm(CYCLE); lanes={}
    for name,a in WITNESSES.items():
        lanes[name]={'cycle':check_direction(a,CYCLE),'inverse':check_direction(a,ip)}
    checks={
      'ten_edges':len(core.EDGES)==10,
      'cycle_permutation':sorted(CYCLE)==list(range(5)),
      'inverse_permutation':sorted(ip)==list(range(5)),
      'source_controls_exact':all(x[d]['source_orientation_transpose_recompression_exact'] for x in lanes.values() for d in ('cycle','inverse')),
      'all_series_constructed':True,
    }
    valid=all(checks.values())
    covall=all(x[d]['covariance_exact'] for x in lanes.values() for d in ('cycle','inverse'))
    projall=all(x[d]['projected_channel_series_exact'] for x in lanes.values() for d in ('cycle','inverse'))
    if not valid: cls='INVALID_IMPLEMENTATION'
    elif not covall: cls='REDUCED_LAPLACIAN_S5_COVARIANCE_FAIL_EXACT'
    elif not projall: cls='PROJECTED_WICK_CHANNEL_S5_COVARIANCE_FAIL_EXACT'
    else: cls='GEOMETRIC_WICK_S5_EXACT'
    out={'gate':'K5_EXACT_CANCELLATION_GEOMETRIC_WICK_S5_DIAGNOSTIC','prereg_commit':PREREG,
         'cycle':list(CYCLE),'inverse_cycle':list(ip),'witnesses':{k:[str(x) for x in v] for k,v in WITNESSES.items()},
         'lanes':lanes,'checks':checks,'classification':cls,'physical_corner_coefficients_used':False,'scientific_verdict':None}
    p=Path(args.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2,sort_keys=True))
    return 2 if cls=='INVALID_IMPLEMENTATION' else 0

if __name__=='__main__': raise SystemExit(main())
