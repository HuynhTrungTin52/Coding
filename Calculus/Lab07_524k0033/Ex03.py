import sympy as sp

x = sp.symbols('x')
fa = sp.cos(x)

#sympy.series(expr, x, x0, n)
taylor_poly = sp.series(fa, x, x0=(sp.pi/3) , n=6)
print('Taylor series of f(x) at pi/3 : ', taylor_poly)


fb = sp.ln(x)

#sympy.series(expr, x, x0, n)
taylor_poly_b = sp.series(fb, x, x0=2, n=10)
print('Taylor series of f(x) at 2 : ', taylor_poly_b)


fc = sp.exp(x)

#sympy.series(expr, x, x0, n)
taylor_poly_c = sp.series(fc, x, x0=3, n=12)
print('Taylor series of f(x) at 3 : ', taylor_poly_c)