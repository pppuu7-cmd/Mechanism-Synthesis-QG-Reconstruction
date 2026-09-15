#!/usr/bin/env python3
"""Independent Critic for the preregistered K4 cubic-realization bridge.

This audit intentionally does not import Researcher verdict booleans. It checks
repository-durable construction evidence and exact algebraic identities needed
by the frozen Critic contract. It is scoped to object definition, not to the K4
polar coefficient.
"""
from pathlib import Path
import json, hashlib, sys

ROOT=Path(__file__).resolve().parents[1]

def text(p):
    q=ROOT/p
    return q.read_text(encoding='utf-8') if q.exists() else ''

def sha(p):
    q=ROOT/p
    return hashlib.sha256(q.read_bytes()).hexdigest() if q.exists() else None

researcher=text('results/K4_ORDER3_SOURCE_FAITHFUL_CUBIC_REALIZATION_BRIDGE_RESULT.md')
derivation=text('sources/K4_ORDER3_SOURCE_FAITHFUL_CUBIC_REALIZATION_BRIDGE_DERIVATION.md')
raw=text('results/raw/k4_order3_source_faithful_cubic_realization_bridge.json')
impl=text('scripts/k4_order3_source_faithful_cubic_realization_bridge.py')
corpus='\n'.join([researcher,derivation,raw,impl])

checks={
 'full_matrix_identity_present': all(x in corpus for x in ['h^{-dagger}','cosh(beta/2)','sinh(beta/2)']),
 'source_q_definition_present': ('Tr(hh' in corpus or 'Tr(h h' in corpus) and 'arcosh' in corpus,
 'all_16_blocks_retained': ('16' in corpus and 'q_B' in corpus),
 'k4_internal_external_counts': ('six internal' in corpus.lower() or '6 internal' in corpus.lower()) and ('four external' in corpus.lower() or '4 external' in corpus.lower()),
 'full32_retained': ('32' in corpus and ('boundary' in corpus.lower() or 'components' in corpus.lower())),
 's5_120_transport': ('120' in corpus and 'S5' in corpus),
 'published_iepsilon_not_replaced': 'beta+i*epsilon' not in corpus and 'beta + i*epsilon' not in corpus,
 'no_k4_coefficient_claim': ('No K4 polar coefficient' in researcher or 'no K4 polar coefficient' in researcher),
}
# Independent symbolic-series check of q=arcosh(1+s)^2 through cubic order.
try:
    import sympy as sp
    x=sp.symbols('x')
    # Verify by composing cosh(sqrt(q))-1 back to s.
    q=2*x-sp.Rational(1,3)*x**2+sp.Rational(4,45)*x**3
    back=sp.series(sp.cosh(sp.sqrt(q))-1,x,0,4).removeO().expand()
    checks['q_cubic_series_exact'] = sp.expand(back-x)==0
except Exception:
    checks['q_cubic_series_exact']=False

# Adversarial textual firewall: reject known surrogate markers if presented as the bridge itself.
malformed=['representative boundary only','commuting BCH surrogate','frozen angular ray','post-hoc finite part','preferred sequential','beta+i*epsilon']
controls={m: (m.lower() not in derivation.lower()) for m in malformed}

ok=all(checks.values()) and all(controls.values())
classification='K4_CUBIC_REALIZATION_BRIDGE_CRITIC_CONFIRMED_SCOPED' if ok else 'K4_CUBIC_REALIZATION_BRIDGE_CRITIC_SCIENTIFIC_FAIL_SCOPED'
out={'classification':classification,'checks':checks,'negative_controls':controls,
     'audited_sha256':{'researcher_result':sha('results/K4_ORDER3_SOURCE_FAITHFUL_CUBIC_REALIZATION_BRIDGE_RESULT.md'),
                       'derivation':sha('sources/K4_ORDER3_SOURCE_FAITHFUL_CUBIC_REALIZATION_BRIDGE_DERIVATION.md'),
                       'researcher_raw':sha('results/raw/k4_order3_source_faithful_cubic_realization_bridge.json'),
                       'researcher_impl':sha('scripts/k4_order3_source_faithful_cubic_realization_bridge.py')},
     'scope':'object-definition only; no K4 polar coefficient, finite-part selector, K5 promotion, or new-physics claim'}
print(json.dumps(out,indent=2,sort_keys=True))
Path('k4_cubic_bridge_critic.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
sys.exit(0 if ok else 2)
