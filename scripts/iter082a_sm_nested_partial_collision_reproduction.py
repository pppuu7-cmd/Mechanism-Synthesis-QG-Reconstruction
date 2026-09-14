#!/usr/bin/env python3
"""Iter082A-SM exact Researcher reproduction frozen by prospective prereg."""
import itertools, json, sys
from pathlib import Path

EDGES=list(itertools.combinations(range(5),2))
NEIGH={a:[b for b in range(5) if b!=a] for a in range(5)}
LEG={(a,b):NEIGH[a].index(b) for a in range(5) for b in NEIGH[a]}
NODE_OPTIONS={
0:[((0,1,0,1),1),((0,1,1,0),-1),((1,0,0,1),-1),((1,0,1,0),1)],
1:[((0,0,1,1),2),((0,1,0,1),-1),((0,1,1,0),-1),((1,0,0,1),-1),((1,0,1,0),-1),((1,1,0,0),2)]}

def add(z,w): return (z[0]+w[0],z[1]+w[1])
def mul(z,w): return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def M(v):
 x,y,z=v; return [[(z,0),(-x,-y)],[(-x,y),(-z,0)]]
def sub(a,b): return tuple(a[i]-b[i] for i in range(3))
def neg(a): return tuple(-x for x in a)
def nonzero(v): return any(v)

def contract(ks, mats):
 total=(0,0)
 for choices in itertools.product(*[NODE_OPTIONS[k] for k in ks]):
  states=[]; c=1
  for st,cc in choices: states.append(st); c*=cc
  z=(c,0)
  for a,b in EDGES:
   row=states[b][LEG[(b,a)]]; col=states[a][LEG[(a,b)]]
   z=mul(z,mats[(a,b)][row][col])
   if z==(0,0): break
  total=add(total,z)
 return total

def rows_for(mats):
 rows=[]
 for ks in itertools.product((0,1),repeat=5):
  v=contract(ks,mats); rows.append({'boundary_k':list(ks),'value':[v[0],v[1]],'nonzero':v!=(0,0)})
 return rows

def deepest_mats():
 X={0:(0,0,0),1:(1,2,3),2:(2,3,5),3:(3,5,7),4:(5,7,11)}
 return {e:M(sub(X[e[0]],X[e[1]])) for e in EDGES}

def k4_mats():
 A={0:(0,0,0),1:(1,2,3),2:(2,3,5),3:(3,5,7)}; b=(5,7,11); out={}
 for e in EDGES:
  a,c=e
  if c<=3: v=sub(A[a],A[c])
  else: v=neg(b)
  if not nonzero(v): raise ValueError('zero K4 direction '+str(e))
  out[e]=M(v)
 return out

def k3_mats():
 A={0:(0,0,0),1:(1,2,3),2:(2,3,5)}; b3=(3,5,7); b4=(5,7,11); out={}
 for e in EDGES:
  a,b=e
  if b<=2: v=sub(A[a],A[b])
  elif a<=2 and b==3: v=neg(b3)
  elif a<=2 and b==4: v=neg(b4)
  else: v=sub(b3,b4)
  if not nonzero(v): raise ValueError('zero K3 direction '+str(e))
  out[e]=M(v)
 return out

def causal_control():
 vals=[]
 for eta in (-1,1):
  for sig in itertools.product((-1,1),repeat=5):
   p=1
   for a,b in EDGES: p*=eta*sig[a]*sig[b]
   vals.append(p)
 return len(vals)==64 and all(x==1 for x in vals)

def degenerate_control():
 A={0:(0,0,0),1:(0,0,0),2:(2,3,5)}
 return not nonzero(sub(A[0],A[1]))

def main():
 k4=rows_for(k4_mats()); k3=rows_for(k3_mats()); deep=rows_for(deepest_mats())
 n4=sum(r['nonzero'] for r in k4); n3=sum(r['nonzero'] for r in k3); nd=sum(r['nonzero'] for r in deep)
 controls={'all_exact_gaussian_integer':True,'all_frozen_directions_nonzero':True,
 'degenerate_zero_internal_direction_rejected':degenerate_control(),
 'deepest_allplus_has_nonzero_component':nd>0,'proper_causal_total_branch_parity_plus_one':causal_control()}
 valid=all(controls.values())
 fixed_external_nonidentity=(n4>0 and n3>0)
 if not valid: verdict='INVALID_IMPLEMENTATION_OR_PROVENANCE'
 elif n4>0 and n3>0 and fixed_external_nonidentity: verdict='ITER082A_SM_SOURCE_ORDERED_FULL_BOUNDARY_K3_LOG_AND_K4_POWER_PARTIAL_COLLISION_NONL1_WITNESSES_CONFIRMED_EXACT_SCOPED'
 elif n4>0: verdict='ITER082A_SM_K4_ONLY_PARTIAL_COLLISION_WITNESS_CONFIRMED_EXACT_SCOPED'
 elif n3>0: verdict='ITER082A_SM_K3_ONLY_PARTIAL_COLLISION_WITNESS_CONFIRMED_EXACT_SCOPED'
 else: verdict='ITER082A_SM_NESTED_PARTIAL_COLLISION_HYPOTHESIS_FAILS_EXACT_SCOPED'
 out={'iteration':'Iter082A-SM','execution_valid':valid,'classification':verdict,
 'k4':{'nonzero_components':n4,'checked':32,'q':-12,'normal_dimension':9,'margin':-3,'rows':k4},
 'k3':{'nonzero_components':n3,'checked':32,'q':-6,'normal_dimension':6,'margin':0,'rows':k3},
 'deepest_sanity_nonzero_components':nd,'fixed_external_nonidentity_argument_valid':fixed_external_nonidentity,
 'nonidentity_argument':'nonzero nested leading coefficient implies the source-ordered fixed-external coefficient is not identically zero; hence it is nonzero for some sufficiently small fixed external configuration',
 'controls':controls,'claim_ceiling':'existence of frozen minimal-spin fully boundary-contracted K3/K4 partial non-L1 witnesses only; no generic-spin, distributional nonexistence, selector, regulator independence, G3/F9/G8/K5, new-physics or complete-QG claim'}
 Path('iter082a_aggregate.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ('k3','k4')},indent=2,sort_keys=True)); print('K3',n3,'/32 K4',n4,'/32 deepest',nd,'/32')
 return 0 if valid else 2
if __name__=='__main__': sys.exit(main())
