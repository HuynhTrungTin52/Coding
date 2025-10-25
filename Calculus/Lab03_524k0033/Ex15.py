import sympy as sp

t = sp.Symbol('t')
s = 24*t - 0.8*t**2
v = sp.diff(s, t)
a = sp.diff(v, t)

print("s(t) =", s)
print("v(t) =", v)
print(f"a(t) ={a:.2f}")
t_max = sp.solve(v, t)[0]
s_max = s.subs(t, t_max)
print(f"\nrock reach its highest point when v(t) = 0: t = {t_max:.2f} (sec)")
print(f"Highest point: s({t_max:.2f}) = {s_max:.2f} (m)")