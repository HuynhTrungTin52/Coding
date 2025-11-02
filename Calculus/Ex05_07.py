import sympy as sp

n = sp.symbols('n')
expressions = [(4 * n**2 + 1) / (3 * n**2 + 2),sp.sqrt(n**2 + 1) - n,sp.sqrt(2 * n + sp.sqrt(n)) - sp.sqrt(2 * n + 1),(3 * 5**n - 2 * n) / (4**n + 2.5**n),(n * sp.sin(sp.sqrt(n))) / (n**2 + n - 1)]

for idx, expr in enumerate(expressions, 1):
	result = sp.limit(expr, n, sp.oo)
	print(f"Problem {idx}: {result}")
