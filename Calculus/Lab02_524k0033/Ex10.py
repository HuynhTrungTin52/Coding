import sympy as sp
x = sp.Symbol('x')
f_a = sp.sin(x) / x
L_a = sp.limit(f_a, x, 0)
print(f"(a) L = {L_a}")

f_b = (x**2 + x - 6) / (x**2 - 4)
L_b = sp.limit(f_b, x, 2)
print(f"(b) L = {L_b}")