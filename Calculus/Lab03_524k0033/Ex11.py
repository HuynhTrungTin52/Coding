import sympy as sp
import numpy as np
#Ex4

x = sp.symbols('x')


dx = sp.symbols('dx')  # Δx
x0 = 0                 # need to calculate f'(0)

fa = x * sp.sin(1 / x)
fa0=0
dfa_x0 = (fa.subs(x, x0 + dx) - fa0) / dx
limit_vala = sp.limit(dfa_x0, dx, 0)


fb = x**2 * sp.sin(1/x)
fb0=0
dfb_x0 = (fb.subs(x, x0 + dx) - fb0) / dx
limit_valb = sp.limit(dfb_x0, dx, 0)



def checkDiff(limit_val,function):
	if isinstance(limit_val, sp.AccumBounds):
		print(f"{function} is not differentiable")
	else:
		print(f"{function} is differentiable")
		
checkDiff(limit_vala,fa)
checkDiff(limit_valb,fb)
