import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')

problems = [
	("a", x**2 - 2*x - 5, 0, 2),
	("b", 3*x + x**3 + 5, -4, 4),
	("c", sp.sin(x) + 3*x**2, -2, 2),
	("d", sp.exp(x**2) + 3*x, -1, 1),
	("e", x**3 - 3*x, -3, 0),
	("f", x**3 - 3*x, 0, 3),
	("g", sp.sin(x), 0, sp.pi),
	("h", sp.sin(2*x), 0, 2),
	("i", sp.cos(x), sp.pi/2, 3*sp.pi/2),
	("j", sp.tan(x)**2, -sp.pi/4, sp.pi/4),
	("k", sp.exp(x)*sp.sin(x), 0, sp.pi),
	("l", x**4 - 3*x**2, -4, 0),
	("m", x**4 - 3*x**2, 0, 4),
	("n", x**5 - 5*x**3, -4, 0),
	("o", x**6 - 5*x**2, -1, 1),
	("p", x**3 - 9*x, -3, 0),
	("q", x**3 - 9*x, 0, 3),
	("r", x**3 + 9*x, -1, 1),
]

def critical_points(f, a, b):
	df = sp.diff(f, x)
	pts = []
	for guess in np.linspace(float(a), float(b), 60):
		try:
			r = sp.nsolve(df, guess, tol=1e-14, maxsteps=50)
			if r.is_real:
				rv = float(r)
				if rv >= float(a) - 1e-8 and rv <= float(b) + 1e-8:
					if all(abs(rv - float(c)) > 1e-6 for c in pts):
						pts.append(sp.nsimplify(rv))
		except Exception:
			pass
	pts.extend([sp.nsimplify(a), sp.nsimplify(b)])
	return sorted(pts, key=lambda v: float(v))

cols = 3
rows = int(np.ceil(len(problems)/cols))
fig, axes = plt.subplots(rows, cols, figsize=(14, 28))
axes = axes.flatten()

for idx, (label, f, a, b) in enumerate(problems):
	ax = axes[idx]
	a_f = float(a)
	b_f = float(b)
	xs = np.linspace(a_f, b_f, 400)
	f_lamb = sp.lambdify(x, f, 'numpy')
	ys = f_lamb(xs)
	ax.plot(xs, ys, 'b-')
	cps = critical_points(f, a, b)
	cp_vals = [f_lamb(float(c)) for c in cps]
	# find maxima
	max_y = max(cp_vals)
	max_pts = [float(c) for c, yv in zip(cps, cp_vals) if abs(yv - max_y) < 1e-9]
	ax.plot(max_pts, [max_y]*len(max_pts), 'ro')
	for mx in max_pts:
		ax.annotate(f"({mx:.3g},{max_y:.3g})", (mx, max_y),
					textcoords="offset points", xytext=(5,5), fontsize=8, color='red')
	ax.set_title(label)
	ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()