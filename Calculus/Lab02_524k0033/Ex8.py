import sympy as sp

x = sp.Symbol('x')
f_x = 1 - sp.sqrt(1 - x**2)

is_continuous_at_neg1 = sp.limit(f_x, x, -1) == f_x.subs(x, -1)
if is_continuous_at_neg1:
    print("Function is continuous x at = -1")
else:
    print("Function is NOT continuous at x = -1")

is_continuous_at_pos1 = sp.limit(f_x, x, 1) == f_x.subs(x, 1)
if is_continuous_at_pos1:
    print("Function is continous at x = 1")
else:
    print("Function is NOT continuous at x = 1")