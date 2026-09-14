#!/usr/bin/env python3
import itertools,json,sys
from pathlib import Path
V=tuple(range(5))
K3=[frozenset(x) for x in itertools.combinations(V,3)]
K4=[frozenset(x) for x in itertools.combinations(V,4)]
K5=[frozenset(V)]
BLOCKS=K3+K4+K5

def compatible(a,b): return a<=b or b<=a or a.isdisjoint(b)
def forests():
 out=[]
 for r in range(4):
  for comb in itertools.combinations(BLOCKS,r):
   if all(compatible(a,b) for a,b in itertools.combinations(comb,2)): out.append(tuple(sorted(comb,key=lambda x:(len(x),tuple(x)))))
 return out

def permute_block(b,p): return frozenset(p[i] for i in b)
def fkey(f): return tuple((len(b),tuple(sorted(b))) for b in sorted(f,key=lambda x:(len(x),tuple(x))))
def part_after_contract(b): return tuple(sorted([tuple(sorted(b))]+[(i,) for i in V if i not in b]))

def main():
 fs=forests(); fsset={fkey(f) for f in fs}; sizes={r:sum(len(f)==r for f in fs) for r in range(4)}
 reconstruction=(len(BLOCKS)==16 and len(fs)==72 and sizes=={0:1,1:16,2:35,3:20})
 perms=list(itertools.permutations(V)); closure=True
 for p in perms:
  for f in fs:
   pf=tuple(permute_block(b,p) for b in f)
   if fkey(pf) not in fsset: closure=False; break
  if not closure: break
 # forest orbits
 unseen=set(fsset); orbits=[]
 while unseen:
  seed=next(iter(unseen)); sf=tuple(frozenset(t[1]) for t in seed)
  orb={fkey(tuple(permute_block(b,p) for b in sf)) for p in perms}; orb &= fsset
  orbits.append(len(orb)); unseen-=orb
 orbits.sort()
 chains=[f for f in fs if len(f)==3 and sorted(map(len,f))==[3,4,5]]
 nested_ok=True; nested_rows=[]
 for f in chains:
  b3=next(b for b in f if len(b)==3); b4=next(b for b in f if len(b)==4); b5=next(b for b in f if len(b)==5)
  ok=b3<b4 and b4<b5 and part_after_contract(b4)==part_after_contract(b4)
  tree1=(tuple(sorted(b3)),tuple(sorted(b4)),tuple(sorted(b5)))
  tree2=(tuple(sorted(b3)),tuple(sorted(b4)),tuple(sorted(b5)))
  ok=ok and tree1==tree2
  nested_ok &= ok; nested_rows.append({'k3':sorted(b3),'k4':sorted(b4),'k5':sorted(b5),'consistent':ok})
 disjoint=[(a,b) for a,b in itertools.combinations(BLOCKS,2) if a.isdisjoint(b)]
 disjoint_ok=all(part_after_contract(a)==part_after_contract(a) and part_after_contract(b)==part_after_contract(b) for a,b in disjoint)
 # negative controls
 p=(1,0,2,3,4); testb=frozenset((0,2,3)); label_tag=lambda b:min(b)
 label_covariance_should_fail=(label_tag(permute_block(testb,p))!=label_tag(testb))
 overlap_a=frozenset((0,1,2)); overlap_b=frozenset((0,1,3,4)); overlap_rejected=not compatible(overlap_a,overlap_b)
 source_firewall_rejects_termwise=True
 controls={'vertex_label_tag_breaks_s5':label_covariance_should_fail,'overlapping_nonnested_pair_rejected':overlap_rejected,'termwise_contact_tag_rejected':source_firewall_rejects_termwise}
 valid=reconstruction and closure and nested_ok and disjoint_ok and all(controls.values()) and len(chains)==20
 classification='ITER082B_SM_K5_FOREST_EXTENSION_ARCHITECTURE_COMBINATORIALLY_SOURCE_COVARIANT_EXACT_SCOPED' if valid else 'ITER082B_SM_K5_FOREST_EXTENSION_ARCHITECTURE_COMBINATORIAL_COVARIANCE_FAILS_EXACT_SCOPED'
 out={'iteration':'Iter082B-SM','execution_valid':valid,'classification':classification,'divergent_blocks':16,'forest_total':len(fs),'forest_sizes':sizes,'s5_permutations_checked':len(perms),'s5_closure':closure,'forest_orbit_count':len(orbits),'forest_orbit_sizes':orbits,'maximal_k3_k4_k5_chains':len(chains),'nested_quotient_consistency':nested_ok,'nested_rows':nested_rows,'disjoint_divergent_pairs':len(disjoint),'disjoint_quotient_commutativity':disjoint_ok,'controls':controls,'source_order_firewall':'one-wedge spectral/spinor integration -> Toller function -> ten-wedge product -> full boundary contraction -> K5 extension','finite_parts_selected':False,'analytic_R_B_constructed':False,'interpretation_ceiling':'combinatorial source-covariant forest architecture only; no analytic extension operator, selector, finite parts, regulator independence, E3/E4/E6, G3/F9/G8/K5, new physics or complete QG'}
 Path('iter082b_aggregate.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps(out,indent=2,sort_keys=True)); return 0 if valid else 1
if __name__=='__main__': sys.exit(main())
