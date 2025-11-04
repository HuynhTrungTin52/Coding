import sympy as sp
t = sp.symbols('t')

# (a) w = x^2 + y^2, x = cos(t), y = sin(t), t = pi
x = sp.cos(t)
y = sp.sin(t)
w = x**2 + y**2
dwt = sp.simplify(sp.diff(w, t))
print("a) dw/dt =", dwt)
print("   dw/dt at t = pi ->", dwt.subs(t, sp.pi))
print()

# (b) w = x^2 + y^2, x = cos(t)+sin(t), y = cos(t)-sin(t), t = 0
x = sp.cos(t) + sp.sin(t)
y = sp.cos(t) - sp.sin(t)
w = x**2 + y**2
dwt = sp.simplify(sp.diff(w, t))
print("b) dw/dt =", dwt)
print("   dw/dt at t = 0  ->", dwt.subs(t, 0))
print()

# (c) w = x/z + y/z, x = cos^2(t), y = sin^2(t), z = 1/t, t = 3
x = sp.cos(t)**2
y = sp.sin(t)**2
z = 1/t
w = x/z + y/z
dwt = sp.simplify(sp.diff(w, t))
print("c) dw/dt =", dwt)
print("   dw/dt at t = 3  ->", dwt.subs(t, 3))
print()

# (d) w = 2*y*e^{-x} - ln(z), x = ln(t^2+1), y = atan(t), z = e^t, t = 1
x = sp.log(t**2 + 1)
y = sp.atan(t)
z = sp.exp(t)
w = 2*y*sp.exp(-x) - sp.log(z)
dwt = sp.simplify(sp.diff(w, t))
print("d) dw/dt =", dwt)
print("   dw/dt at t = 1  ->", dwt.subs(t, 1))
print()

# (e) w = z - sin(x*y), x = t, y = ln(t), z = e^{t-1}, t = 1
x = t
y = sp.log(t)
z = sp.exp(t - 1)
w = z - sp.sin(x*y)
dwt = sp.simplify(sp.diff(w, t))
print("e) dw/dt =", dwt)
print("   dw/dt at t = 1  ->", dwt.subs(t, 1))