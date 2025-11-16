import sympy as sp

x, m = sp.symbols('x m', real=True)

f = x**3 - 3*m*x**2 + 3*(m**2 - 1)*x - (m**2 - 1)
f1 = sp.diff(f, x)
f2 = sp.diff(f1, x)

m_candidates = sp.solve(sp.Eq(f1.subs(x, 1), 0), m)

m_valid = [val for val in m_candidates if f2.subs({x: 1, m: val}) < 0]

print("Candidates from f'(1)=0:", m_candidates)
print("Values of m for which y has a maximum at x0=1:", m_valid)  