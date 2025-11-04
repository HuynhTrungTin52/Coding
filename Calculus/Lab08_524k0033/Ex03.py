import sympy as sp

x, y = sp.symbols('x y')

problems = [
	('a', 2*x**2 - 3*y - 4),
	('b', (x**2 - 1)*(y + 2)),
	('c', x**2 - x*y + y**2),
	('d', 5*x*y - 7*x**2 - y**2 + 3*x - 6*y + 2),
	('e', (x*y - 1)**2),
	('f', (2*x - 3*y)**3),
	('g', sp.sqrt(x**2 + y**2)),
	('h', (x**3 + y)**(sp.Rational(2, 3))),
	('i', 1/(x + y)),
	('j', x/(x**2 + y**2)),
	('k', (x + y)/(x*y - 1)),
	('l', sp.atan(y/x)),
	('m', sp.exp(x + y + 1)),
	('n', sp.exp(-x)*sp.sin(x + y)),
	('o', sp.log(x + y)),
]

for label, f in problems:
	dfx = sp.simplify(sp.diff(f, x))
	dfy = sp.simplify(sp.diff(f, y))
	print(f"{label}) f(x,y) = {f}")
	print("   ∂f/∂x =", dfx)
	print("   ∂f/∂y =", dfy)
	print()