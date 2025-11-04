import sympy as sp

x, y = sp.symbols('x y')

problems = [
	('a', x + y + x*y),
	('b', sp.sin(x*y)),
	('c', x**2 * y + sp.cos(y) + y*sp.sin(x)),
	('d', x*sp.exp(y) + y + 1),
	('e', sp.log(x + y)),
	('f', sp.atan(y/x)),
	('g', x**2 * sp.tan(x*y)),
	('h', y * sp.exp(x**2 - y)),
	('i', x * sp.sin(x**2 * y)),
	('j', (x - y)/(x**2 + y)),
]

for label, f in problems:
	dfx = sp.simplify(sp.diff(f, x))
	dfy = sp.simplify(sp.diff(f, y))
	dfxx = sp.simplify(sp.diff(dfx, x))
	dfyy = sp.simplify(sp.diff(dfy, y))
	dfxy = sp.simplify(sp.diff(dfx, y))
	print(f"{label}) f(x,y) = {f}")
	print("   ∂f/∂x =", dfx)
	print("   ∂f/∂y =", dfy)
	print("   ∂²f/∂x² =", dfxx)
	print("   ∂²f/∂y² =", dfyy)
	print("   ∂²f/∂x∂y =", dfxy)
	print()