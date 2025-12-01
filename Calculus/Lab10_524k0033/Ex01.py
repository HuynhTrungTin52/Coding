import sympy as sp

x = sp.symbols('x', positive=True)

antiderivatives = {}
definite = {}

# (a)
f_a = x**3 + 2*x**2 + 3
antiderivatives['a'] = sp.integrate(f_a, x)
definite['a'] = sp.integrate(f_a, (x, 1, 2))

# (b)
f_b = x**-3 + x**-2 + x*sp.sqrt(x)
antiderivatives['b'] = sp.integrate(f_b, x)
definite['b'] = sp.integrate(f_b, (x, 1, 4))

# (c)
f_c = x + x**(-sp.Rational(1,2)) + x**-1
antiderivatives['c'] = sp.integrate(f_c, x)
definite['c'] = sp.integrate(f_c, (x, 1, 4))

# (d)
f_d = 2/(1 + x**2)
antiderivatives['d'] = sp.integrate(f_d, x)  
definite['d'] = sp.integrate(f_d, (x, 1, 2))

# (e)
f_e = x + 2*x**3
antiderivatives['e'] = sp.integrate(f_e, x)
definite['e'] = sp.integrate(f_e, (x, 1, 2))

# (f)
f_f = x**(sp.Rational(3,2)) - 1
antiderivatives['f'] = sp.integrate(f_f, x)
definite['f'] = sp.integrate(f_f, (x, 0, 1))

# (g)
f_g = 1 - 2/sp.sin(x)**2
antiderivatives['g'] = sp.integrate(f_g, x) 
definite['g'] = sp.integrate(f_g, (x, sp.pi/4, sp.pi/2))

# (h) 
f_h = 1/(sp.sin(x)**2 * sp.cos(x)**2)  
antiderivatives['h'] = -2*sp.cot(2*x)  
definite['h'] = sp.integrate(f_h, (x, sp.pi/4, sp.pi/2))  # diverges

# (i)
f_i = sp.exp(x) - sp.sec(x)**2
antiderivatives['i'] = sp.integrate(f_i, x)  
definite['i'] = sp.integrate(f_i, (x, 0, sp.pi/2))  

# (j)
f_j = 2*sp.exp(x) + sp.exp(-x)
antiderivatives['j'] = sp.integrate(f_j, x)
definite['j'] = sp.integrate(f_j, (x, 0, sp.log(2)))

# (k)
f_k = 2**x + 2/x
antiderivatives['k'] = sp.integrate(f_k, x) 
definite['k'] = sp.integrate(f_k, (x, 1, 2))

# (l)
f_l = x**2 * (x - 1)**2
antiderivatives['l'] = sp.integrate(f_l, x)
definite['l'] = sp.integrate(f_l, (x, 0, 1))

# (m)
f_m = 1/(x*(x+1))
antiderivatives['m'] = sp.integrate(f_m, x) 
definite['m'] = sp.integrate(f_m, (x, 1, 2))

# (n)
f_n = sp.Abs(1 - x)
antiderivatives['n'] = sp.integrate(f_n, x)
definite['n'] = sp.integrate(f_n, (x, 0, 2))

# (o)
f_o = sp.Abs(2*x - x**2)
antiderivatives['o'] = sp.integrate(f_o, x)
definite['o'] = sp.integrate(f_o, (x, 0, 3))

# (p)
f_p = sp.sqrt(x**2 - 3*x + 2)
F_p = ((x - sp.Rational(3,2))/2)*f_p - sp.Rational(1,8)*sp.log(x - sp.Rational(3,2) + f_p)
antiderivatives['p'] = F_p
definite['p'] = sp.simplify(F_p.subs(x,4) - F_p.subs(x,2))

# (q)
f_q = sp.sqrt(1 + sp.cos(2*x))
antiderivatives['q'] = sp.simplify(sp.integrate(f_q, x)) 
definite['q'] = sp.integrate(f_q, (x, 0, sp.pi))

for k in sorted(definite):
	print(f"({k}) Antiderivative: {antiderivatives[k]}")
	print(f"({k}) Definite integral: {sp.simplify(definite[k])}")
	print()

print("(h) improper integral (divergence expected):", definite['h'])
print("(i) improper integral (divergence expected):", definite['i'])