import sympy as sp

x=sp.symbols('x')
fa=4-x*x
df=sp.diff(fa,x) 
h = sp.symbols('h')
for a in (-3, 0, 1):
	deriv_at_a = sp.limit((fa.subs(x, a + h) - fa.subs(x, a)) / h, h, 0)
	print("f'({}) = {}".format(a, deriv_at_a))