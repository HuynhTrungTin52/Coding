import sympy as sp

#Ex4

x = sp.symbols('x')
f = -2*x*x / 3 + x
dx = sp.symbols('dx')  # Δx
x0 = 0                 # need to calculate f'(0)

df_x0 = ( f.subs(x, x0 + dx) - f.subs(x, x0) ) / dx  # The fraction in the definition
print("By limit - Derivative of f(x) at x0: ", sp.limit(df_x0, dx, 0))