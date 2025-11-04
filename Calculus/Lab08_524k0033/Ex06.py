import sympy as sp


x, y = sp.symbols('x y')

functions = {
	'a': y**2 * x**4 * sp.exp(x) + 2,
	'b': x**5 + 5*x*y + sp.sin(x) + 7*sp.exp(x),
	'c': y**4 + y*(sp.sin(x) - x**4),
	'd': x * sp.exp(-y**4/2),
}

results = {}
for name, f in functions.items():
	d3y = sp.diff(f, y, 3)        
	d5 = sp.diff(d3y, x, 2)        
	results[name] = sp.simplify(d5)


for name in ['a','b','c','d']:
	print(f"({name}) f = {functions[name]}")
	print(f"    d^3/dy^3 = {sp.simplify(sp.diff(functions[name], y, 3))}")
	print(f"    d^5/(dx^2 dy^3) = {results[name]}\n")