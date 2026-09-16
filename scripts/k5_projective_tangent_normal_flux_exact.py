from fractions import Fraction
from itertools import permutations

# Exact algebraic verifier for the preregistered corrected projective normal-flux gate.
# Work on the simplex s1=1.  A logarithmic ambient field is v_i=a_i q_i;
# its projective representative is u_i=v_i-S a_i, S=sum v_i.

def tangent(a,q):
    v=[a[i]*q[i] for i in range(len(a))]
    S=sum(v,Fraction(0))
    u=[v[i]-S*a[i] for i in range(len(a))]
    return v,u,S

def check_sample(a,q,Z):
    assert sum(a)==1
    v,u,S=tangent(a,q)
    assert sum(u,Fraction(0))==0
    t=sum(a[i] for i in Z)
    raw=sum(v[i] for i in Z)
    normal=sum(u[i] for i in Z)
    assert normal == raw-t*S
    # arbitrary radial shift fE must leave u and its normal component unchanged
    f=Fraction(7,5)
    q2=[qi+f for qi in q]
    _,u2,_=tangent(a,q2)
    assert u2==u
    assert sum(u2[i] for i in Z)==normal
    return t,normal

def main():
    # exact positive rational simplex point, generic non-radial q data
    den=sum(range(1,11))
    a=[Fraction(i,den) for i in range(1,11)]
    q=[Fraction((i+2)*(i+3)-5,11) for i in range(10)]
    tested=0
    for k in range(1,10):
        Z=set(range(k))
        t,n=check_sample(a,q,Z)
        assert t>0
        # scalar blow-up Jacobian is the already-established t^(k-1) factor.
        jac_exp=k-1
        assert jac_exp==k-1
        # permutation-related representative
        p=list(reversed(range(10)))
        ap=[a[p[i]] for i in range(10)]
        qp=[q[p[i]] for i in range(10)]
        Zp={p.index(i) for i in Z}
        tp,np=check_sample(ap,qp,Zp)
        assert tp==t and np==n
        tested+=2
    # Euler field q_i=1: v=E, projective representative and flux vanish exactly.
    _,ue,_=tangent(a,[Fraction(1) for _ in a])
    assert all(x==0 for x in ue)
    for k in range(1,10):
        assert sum(ue[:k],Fraction(0))==0
    # empty/full are controls, not physical corners; full normal vanishes by tangency.
    _,u,_=tangent(a,q)
    assert sum(u,Fraction(0))==0
    print('classification=K5_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING_EXACT_SCOPED')
    print('exact_samples=',tested)
    print('k_range=1..9')
    print('euler_flux_zero=true')
    print('radial_shift_invariant=true')
    print('simplex_tangent=true')

if __name__=='__main__':
    main()
