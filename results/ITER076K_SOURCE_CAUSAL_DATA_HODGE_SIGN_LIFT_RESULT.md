# Iter076K terminal result — source causal data fix the Hodge line, not the global sign

Date: 2026-09-13

## Authority
- preregistration: `afcbd9d13833c7e4a2ff997ad49f3959726ad236`
- implementation: `3a6099e30c0d1760b0d09c925c4b9dfb3c444a35`
- initial production head: `70ca50aecee1be7ebf911d434dbc262112f64716`, run `34776382876` — non-authoritative for scientific classification because Lane A used an orientation-blind edge action rather than the frozen oriented-edge representation
- minimal control-only repair: `62000d2100e7d44b442f67b1e4118707bd1a9879`
- authoritative production/workflow head: `62000d2100e7d44b442f67b1e4118707bd1a9879`
- authoritative run: `34779234892`
- aggregate job: `103783117527`
- aggregate artifact: `10324660667`
- aggregate digest: `sha256:f4f51b24d519488580d06fc15ebf3c52cbe4f439a3abaae18ad79d34ba1c9dac`

Raw lane artifacts consumed:
- A: job `103783061832`, artifact `10323539592`, digest `sha256:0dcf74bcef012cdeb03e0a922731022ecbf84ed6ced02a20401c63722000698a`
- B: job `103783061927`, artifact `10324470587`, digest `sha256:6b9d6ae79693cfd5adee8a162c751fc0626c6947267ffcbefa5ebecff2cfb14e`
- C: job `103783061939`, artifact `10325100043`, digest `sha256:c936adf05cc47f7461b9785fe3680ef96df6dc8c5b8edce4b3b72bffcf092ae8`
- D: job `103783061886`, artifact `10324875294`, digest `sha256:d968790ebb37743f95206731a8fcd499c6f53cfed65cdacf468009339887f1ce`

## Frozen scientific classification
`ITER076K_SOURCE_K5_INCIDENCE_AND_CAUSAL_SIGMA_FIX_HODGE_LINE_NOT_GLOBAL_SIGN_BLOCKED_ORIENTATION_PSEUDOSCALAR_SCOPED`

The authoritative aggregate is valid and all four prospectively frozen lanes pass.

## Terminal facts
1. **Lane A — signed Hodge line.** Exactly two signed lifts satisfy the frozen complement support, `H^2=I`, and the exact twisted covariance law. They are the global opposites `+H` and `-H`, represented in the three complementary-pair signs by `[1,-1,1]` and `[-1,1,-1]`. Thus the admissible signed-lift space is one Hodge line with one unresolved global `Z2` sign.
2. **Lane B — source causal `sigma` census.** Over the `32` configurations including both values of the gauge-root causal variable, every configuration has an odd stabilizer in the relevant `S4` action. The exhaustive sign-equivariant selector census returns `selector_count=0`. Therefore no function of the frozen source causal `sigma` data can covariantly choose between `+H` and `-H`.
3. **Lane C — induced wedge-sign `kappa` census.** After the global `sigma -> -sigma` redundancy there are `8` unique internal `kappa` configurations. Every one has an odd stabilizer, and the exhaustive selector census again returns `selector_count=0`. The induced causal branch data therefore cannot supply the missing pseudoscalar either.
4. **Lane D — label-order/root controls.** All five gauge roots were checked. The deliberately added label-order orientation is preserved by the `12` even relabelings and flips under the `12` odd relabelings; the unsigned complement remains covariant, the orientation-blind same-sign control is rejected, and the signed lift requires an additional orientation choice. Raw label order therefore cannot be promoted to invariant source physics.
5. **Aggregate.** `A=B=C=D=true`, `valid=true`. The frozen PASS classification is attained exactly.

## Interpretation lock
Iter076J source-provenances the unique **unsigned** complementary-edge support. Iter076K now source-provenances the corresponding **signed Hodge line and twist character**, but proves that the actual Eq.(4) causal data `sigma_a` and `kappa_ab=sigma_a sigma_b` do not select its global sign in a relabeling-covariant way.

This is a negative provenance result, not a failure of the Hodge structure: the obstruction is precisely the absence, within the frozen exact source data, of an orientation-odd pseudoscalar capable of distinguishing `+H` from `-H`.

The source causal variables must not be silently reinterpreted as a Levi-Civita orientation of the 4-simplex, and raw label order must not be used as physical orientation data.

The next admissible provenance step is to locate and prospectively test an explicit source-backed orientation/contraction object with the required odd-relabeling character. Semiclassical Regge normals or proper-vertex 4-volume orientation may be candidates only after their provenance and scope are separately frozen; they do not retroactively change this result.

## Claim locks
This result does **not** establish physical source-to-K4 pushforward P3, the source numerator/Haar-Jacobian quadratic jet, the nominal `epsilon^-1` coefficient, causal-vertex finiteness/divergence, G3/F9/G8/K5, physical sector selection, complete QG, or new physics.

The nominal `epsilon^-1` coefficient remains `BLOCKED_OBJECT_DEFINITION`: neither zero, nonzero nor divergent is authorized.
