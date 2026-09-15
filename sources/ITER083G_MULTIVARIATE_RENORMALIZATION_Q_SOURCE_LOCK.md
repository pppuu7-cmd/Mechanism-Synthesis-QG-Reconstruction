# Iter083G source lock — multivariate meromorphic renormalization and regulator-space quadratic form

Date: 2026-09-15
Status: SOURCE/FRAMEWORK LOCK, NOT MSQGR PHYSICAL AUTHORITY

## Mathematical framework source
Nguyen Viet Dang and Bin Zhang, “Renormalization of Feynman amplitudes on manifolds by spectral zeta regularization and blow-ups”, Journal of the European Mathematical Society 23 (2021), 503–556, DOI 10.4171/JEMS/1016.

Relevant exact source facts from Sections 6.2–6.3:

1. Proposition 6.7 constructs a projection pi_p from distributions valued in meromorphic germs with linear poles to distributions valued in holomorphic germs.
2. Remark 6.8 states that pi_p is uniquely determined by the vector subspace of polar germs, and that the polar germs are in turn uniquely determined by the choice of the quadratic form Q on R^p fixed in that section.
3. Immediately afterward the authors fix the Euclidean/canonical form Q(x)=sum_i |x_i|^2 for their construction.
4. Definition 6.10 defines the renormalization map by first applying pi_|E(G)| to the multivariate regularized amplitude and then evaluating the holomorphic germ at s0=(1,...,1).
5. Theorem 6.11 proves consistency/locality properties for the resulting family of renormalization maps in the paper’s Euclidean Feynman-amplitude setting.

Therefore this framework provides a mathematically precise example in which a multivariable holomorphic-part projection uses a quadratic form on regulator-parameter space as part of the construction.

It does NOT state that this Q is physically selected for the Lorentzian spinfoam K5 object.

## Additional regularization-dependence source
Giovanni Felder and David Kazhdan, “Regularization of divergent integrals”, Selecta Mathematica 24 (2018), 157–186, arXiv:1611.05057.

Their abstract/source statement explicitly studies the dependence of Hadamard finite parts on the choice of regularization and expresses that dependence through a local residue map. This is used only as independent evidence that finite-part constructions generally carry regularization data unless extra structure removes it.

No Felder–Kazhdan theorem is being transplanted as an exact formula for the K5 Toller product in Iter083G.

## MSQGR source scope
The published Rühl/Toller / causal-vertex source chain used in this repository defines one-wedge Toller functions and then the ten-wedge K5 product. Iter083E-F established that the published one-wedge analytic uniqueness and spectral Feynman epsilon do not provide a joint-K5 extension selector or collision regulator.

No currently validated MSQGR primary-source lock specifies:

- a 10-variable complex-power analytic regularization of the K5 product;
- a quadratic form Q on the ten edge regulator parameters;
- a holomorphic-germ projection pi_Q for the K5 collision;
- a minimal-subtraction/finite-part normalization selecting the 377 supported coefficients.

Thus Dang–Zhang is tested only as a candidate mathematical repair class.

## Exact implication allowed in Iter083G
If a Q-based multivariate projection of this type is proposed for the ten K5 edge parameters, exact K5 relabeling symmetry can constrain Q to the S5-invariant symmetric forms. Iter083G asks whether that constraint uniquely fixes Q up to overall scale.

## Forbidden implications
- Do not infer that the actual K5 regularized meromorphic germ satisfies all hypotheses of the Dang–Zhang Euclidean Green-kernel theorem without a separate construction.
- Do not infer that different admissible Q necessarily produce different K5 amplitudes.
- Do not infer that a natural Euclidean Q is source-derived physical authority.
- Do not identify regulator-parameter Q with the Lorentzian group metric or with the one-wedge spectral epsilon.
- Do not promote existence of a mathematical renormalization map to unique physical normalization.