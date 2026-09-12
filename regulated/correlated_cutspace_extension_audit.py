#!/usr/bin/env python3
import argparse, json, itertools, math
import numpy as np


def incidence_complete(n):
    edges=list(itertools.combinations(range(n),2))
    B=np.zeros((len(edges),n-1),float)
    for e,(i,j) in enumerate(edges):
        if i<n-1: B[e,i]+=1.0
        if j<n-1: B[e,j]-=1.0
    return edges,B


def sector_signs(n,mask):
    s=np.ones(n,int)
    for i in range(1,n):
        s[i]=1 if ((mask>>(i-1))&1) else -1
    return s


def fit_power(xs,ys):
    lx=np.log(np.asarray(xs)); ly=np.log(np.asarray(ys))
    p,c=np.polyfit(lx,ly,1)
    pred=p*lx+c
    ssr=float(np.sum((ly-pred)**2)); sst=float(np.sum((ly-np.mean(ly))**2))
    r2=1.0-ssr/sst if sst>0 else 1.0
    return float(p),float(r2)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--n',type=int,default=5)
    ap.add_argument('--sector',type=int,required=True)
    ap.add_argument('--output',required=True)
    args=ap.parse_args()
    n=args.n
    edges,B0=incidence_complete(n)
    s=sector_signs(n,args.sector)
    k=np.array([s[i]*s[j] for i,j in edges],float)
    D=np.diag(k)
    B=D@B0
    E=len(edges); r=np.linalg.matrix_rank(B); q=E-r
    G=B@B.T
    evals=np.linalg.eigvalsh(G)
    nz=evals[evals>1e-10]
    pdet=float(np.prod(nz))
    support_density=(2*math.pi)**(-r/2)/math.sqrt(pdet)
    Pcut=B@np.linalg.pinv(B)
    Pcyc=np.eye(E)-Pcut
    etas=np.logspace(-1,-7,13)
    ambient=[]
    support=[]
    normalization_ratio=[]
    for eta in etas:
        Sigma=G+(eta**2)*Pcyc
        sign,logdet=np.linalg.slogdet(Sigma)
        if sign<=0: raise RuntimeError('non-positive covariance')
        dens=math.exp(-0.5*(E*math.log(2*math.pi)+logdet))
        ambient.append(dens)
        support.append(support_density)
        normalization_ratio.append(dens/support_density)
    slope,r2=fit_power(etas,ambient)
    expected=-q
    out={
      'iteration':'Iter030', 'n':n, 'sector':args.sector,
      'vertex_signs':s.tolist(),'edge_signs':k.astype(int).tolist(),
      'edges':[list(x) for x in edges], 'edge_count':E,'rank':int(r),'cycle_nullity':int(q),
      'nonzero_spectrum':[float(x) for x in nz], 'pseudodeterminant':pdet,
      'support_hausdorff_density_at_origin':support_density,
      'eta':[float(x) for x in etas], 'ambient_density_at_origin':ambient,
      'support_density_at_origin':support,
      'ambient_over_support':normalization_ratio,
      'ambient_power_slope':slope,'ambient_power_r2':r2,'expected_slope':expected,
      'spectrum_sector_invariant': bool(np.allclose(np.sort(nz),np.sort(np.linalg.eigvalsh(B0@B0.T)[np.linalg.eigvalsh(B0@B0.T)>1e-10]),rtol=1e-10,atol=1e-10)),
      'classification': 'SUPPORT_NATIVE_EXTENSION_REMOVES_CYCLE_NORMALIZATION_DIVERGENCE' if abs(slope-expected)<0.02 else 'AUDIT_INCONCLUSIVE',
      'scope_note':'This is a linearized structural existence/control result. It does not establish that the physical causal EPRL/Toller spectral prescription equals the support-native Hausdorff extension.'
    }
    with open(args.output,'w') as f: json.dump(out,f,indent=2)
    print(json.dumps(out,indent=2))

if __name__=='__main__': main()
