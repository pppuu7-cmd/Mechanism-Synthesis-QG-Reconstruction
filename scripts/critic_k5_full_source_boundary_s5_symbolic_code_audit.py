#!/usr/bin/env python3
from pathlib import Path
import argparse, hashlib, json, re
ROOT=Path(__file__).resolve().parents[1]
TARGET=ROOT/'scripts/k5_full_source_boundary_s5_transport_symbolic_theorem.py'
PREREG=ROOT/'prereg/K5_FULL_SOURCE_BOUNDARY_S5_TRANSPORT_SYMBOLIC_GENERATOR_THEOREM_CRITIC.md'
RAW=ROOT/'results/raw/k5_full_source_boundary_s5_transport_symbolic_theorem_authoritative.json'
FORBIDDEN={
 'floating_tolerance':r'(?i)(isclose|allclose|rtol|atol|1e-\d+)',
 'numerical_fit':r'(?i)(lstsq|polyfit|curve_fit|least_squares)',
 'random_witness':r'(?i)(random\.|numpy\.random|np\.random)',
 'fitted_character':r'(?i)(fit.{0,20}(character|phase)|character.{0,20}fit)',
 'fitted_2x2':r'(?i)(fit.{0,20}2x2|2x2.{0,20}fit)',
}
def sha256(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
 text=TARGET.read_text(); pre=PREREG.read_text(); raw=json.loads(RAW.read_text()) if RAW.exists() else None
 hits={k:[m.group(0) for m in re.finditer(rx,text)] for k,rx in FORBIDDEN.items()}
 controls={
  'critic_prereg_present':'independent Critic preregistration' in pre,
  'target_present':TARGET.exists(),
  'raw_authority_present':raw is not None,
  'no_forbidden_static_hits':not any(hits.values()),
  'fraction_exact_arithmetic':'from fractions import Fraction' in text,
  'no_numpy_import':'import numpy' not in text and 'from numpy' not in text,
  'no_scipy_import':'import scipy' not in text and 'from scipy' not in text,
  'explicit_100000_control':'100000' in text,
  'explicit_125_control':'125' in text,
  'explicit_120_control':'120' in text,
  'malformed_controls_present':all(x in text for x in ['no_transpose_rejected','no_source_sign_rejected','no_covariance_orientation_sign_rejected','extra_sign_rejected']),
 }
 out={'status':'PASS_CODE_AUDIT_SCOPED' if all(controls.values()) else 'FAIL_CODE_AUDIT_SCOPED','scientific_verdict':None,'controls':controls,'forbidden_hits':hits,'target_sha256':sha256(TARGET),'raw_sha256':sha256(RAW) if RAW.exists() else None,'scope':'Independent static audit only; does not satisfy frozen reconstruction requirements 1-6 and cannot confirm/refute the theorem.'}
 Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
