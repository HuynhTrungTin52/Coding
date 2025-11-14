import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')

problems = [
    ("(Example)", (x-2)*(x+3)*(x-1),-5,5), #x**4/2-4*x*x + 5
	("(a)", x**3 - 27*x, 0, 5),
	("(b)", sp.Rational(3,2)*x**4 - 4*x**3 + 4, 0, 3),
	("(c)", sp.Rational(1,2)*x**4 - 4*x**2 + 5, 1, 3),
	("(d)", sp.Rational(5,2)*x**4 - sp.Rational(20,3)*x**3 + 6, -1, 3),
]

def extrema(expr, a, b):
	df = sp.diff(expr, x)
	crit = sp.solve(sp.Eq(df,0), x)
	crit_in_interval = [c for c in crit if c.is_real and a <= c <= b]
	pts = crit_in_interval + [a, b]
	vals = [sp.N(expr.subs(x, t)) for t in pts]
	i_max = int(np.argmax(vals))
	i_min = int(np.argmin(vals))
	return pts, vals, pts[i_max], vals[i_max], pts[i_min], vals[i_min]

fig, axes = plt.subplots(2,3, figsize=(10,6))
axes = axes.ravel()
for idx,(label, f, a, b) in enumerate(problems):
	pts, vals, x_max, y_max, x_min, y_min = extrema(f, a, b)
	print(label, "f(x) =", f, f"[{a},{b}]")
	print("  critical (incl endpoints):", pts)
	print("  values:", vals)
	print("  abs max:", (x_max, y_max))
	print("  abs min:", (x_min, y_min))
	ax = axes[idx]
	xs = np.linspace(a, b, 400)
	f_lambda = sp.lambdify(x, f, 'numpy')
	ys = f_lambda(xs)
	ax.plot(xs, ys)
	ax.plot([x_max],[y_max],'ro')
	ax.plot([x_min],[y_min],'gs')
	ax.set_title(label)
	ax.grid(True)

for j in range(len(problems), len(axes)):
	fig.delaxes(axes[j])
plt.tight_layout()
plt.show()