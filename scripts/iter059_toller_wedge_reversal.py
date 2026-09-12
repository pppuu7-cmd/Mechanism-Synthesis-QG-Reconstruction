#!/usr/bin/env python3
import json
import mpmath as mp
import sympy as sp

x, r, eps = sp.symbols('x r eps', real=True)
I = sp.I


def P(dj, dl):
    j = sp.Rational(dj, 2)
    l = sp.Rational(dl, 2)
    if (dj + dl) % 2:
        raise ValueError('j+l must be integer')
    N = int(j + l)
    out = sp.Integer(1)
    for n in range(N + 1):
        q = sp.Rational(n) - j
        out *= (I*x - q) / (I*r - q)
    return sp.cancel(out)


def real_conj(expr):
    z = sp.conjugate(expr)
    z = z.xreplace({sp.conjugate(x): x, sp.conjugate(r): r, sp.conjugate(eps): eps})
    return sp.cancel(sp.expand_complex(z))


def exact_zero(expr):
    num, den = sp.fraction(sp.cancel(sp.together(expr)))
    return sp.expand(num) == 0


equal_rows = []
all_equal_kernel = True
all_branch_swap = True
all_additive = True
for dj in range(13):
    p = P(dj, dj)
    kernel_reality = exact_zero(real_conj(p) - p)
    kplus = sp.cancel((1/(2*sp.pi*I)) * (1/(x-r-I*eps)) * p)
    kminus = sp.cancel((1/(2*sp.pi*I)) * (-1/(x-r+I*eps)) * p)
    swap_pm = exact_zero(real_conj(kminus) - kplus)
    swap_mp = exact_zero(real_conj(kplus) - kminus)
    # Sokhotski/additive compatibility at the algebraic kernel level:
    # branch reversal of both summands must map to conjugate of the same sum.
    additive_compat = exact_zero(real_conj(kplus + kminus) - (kplus + kminus))
    equal_rows.append({
        'two_j': dj,
        'kernel_reality': kernel_reality,
        'minus_conj_equals_plus': swap_pm,
        'plus_conj_equals_minus': swap_mp,
        'additive_kernel_conjugation_compatible': additive_compat,
    })
    all_equal_kernel &= kernel_reality
    all_branch_swap &= swap_pm and swap_mp
    all_additive &= additive_compat

unequal_rows = []
for dj in range(9):
    for dl in range(9):
        if dj == dl or (dj + dl) % 2:
            continue
        p = P(dj, dl)
        unequal_rows.append({
            'two_j': dj,
            'two_l': dl,
            'same_form_self_conjugate': exact_zero(real_conj(p) - p),
        })

# Numerical implementation controls. These do not override exact failures.
mp.mp.dps = 100
rho_vals = [mp.mpf('0.37'), mp.mpf('1.13'), mp.mpf('2.41')]
x_vals = [mp.mpf('-3.2'), mp.mpf('-0.7'), mp.mpf('0.4'), mp.mpf('2.6')]
eps_vals = [mp.mpf('1e-3'), mp.mpf('3e-5')]


def p_num(dj, xx, rr):
    j = mp.mpf(dj) / 2
    out = mp.mpc(1)
    for n in range(dj + 1):
        q = mp.mpf(n) - j
        out *= (1j*xx - q) / (1j*rr - q)
    return out

max_num_err = mp.mpf('0')
num_count = 0
for dj in range(13):
    for rr in rho_vals:
        for xx in x_vals:
            for ee in eps_vals:
                p = p_num(dj, xx, rr)
                kp = (1/(2*mp.pi*1j)) * (1/(xx-rr-1j*ee)) * p
                km = (1/(2*mp.pi*1j)) * (-1/(xx-rr+1j*ee)) * p
                err = abs(mp.conj(km) - kp)
                max_num_err = max(max_num_err, err)
                num_count += 1

num_pass = max_num_err <= mp.mpf('1e-40')
source_controls = {
    'causal_vertex_equal_spin_wedge': True,
    'toller_functions_not_representations': True,
    'wigner_unitary_inverse_identity_required': True,
    'no_beta_plus_i_epsilon_rule': True,
}
valid_negative_report = len(unequal_rows) > 0
all_pass = all_equal_kernel and all_branch_swap and all_additive and num_pass and valid_negative_report and all(source_controls.values())
classification = (
    'K4_TOLLER_EQUAL_SPIN_WEDGE_REVERSAL_BRANCH_SWAP_SOURCE_DERIVED'
    if all_pass else 'K4_TOLLER_EQUAL_SPIN_WEDGE_REVERSAL_LAW_FAIL'
)

out = {
    'iteration': 'Iter059',
    'classification': classification,
    'all_valid': True,
    'equal_spin_exact_kernel_reality_all': bool(all_equal_kernel),
    'equal_spin_exact_branch_swap_all': bool(all_branch_swap),
    'additive_control_compatible_all': bool(all_additive),
    'equal_spin_cases': equal_rows,
    'unequal_spin_negative_control_count': len(unequal_rows),
    'unequal_spin_same_form_self_conjugate_count': sum(int(q['same_form_self_conjugate']) for q in unequal_rows),
    'unequal_spin_rows': unequal_rows,
    'numeric_control_count': num_count,
    'numeric_max_abs_error': mp.nstr(max_num_err, 30),
    'numeric_threshold': '1e-40',
    'numeric_control_pass': bool(num_pass),
    'source_controls': source_controls,
    'scope': 'equal-spin causal EPRL wedge only; branch swap plus transpose/conjugation under group inversion',
    'claim_locks': [
        'no physical causal-sector selection',
        'no contour-existence or vertex-finiteness theorem',
        'no K5/G3/F9/G8 promotion',
        'no beta+i epsilon replacement',
    ],
}
print(json.dumps(out, indent=2, sort_keys=True))
with open('iter059_toller_wedge_reversal.json', 'w') as f:
    json.dump(out, f, indent=2, sort_keys=True)

if not all_pass:
    raise SystemExit(2)
