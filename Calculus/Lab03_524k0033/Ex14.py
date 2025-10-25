import sympy as sp

# Ex14.py

t = sp.symbols('t')
b_sym = 10**6 + 10**4 * t - 10**3 * t**2
b_prime_sym = sp.diff(b_sym, t)

b = sp.lambdify(t, b_sym, 'math')
b_prime = sp.lambdify(t, b_prime_sym, 'math')

times = [0, 5, 10]
for tt in times:
	print(f"t = {tt} hours:")
	print(f"  b(t)      = {int(b(tt)):,} bacteria")
	print(f"  b'(t)     = {int(b_prime(tt)):,} bacteria/hour\n")
