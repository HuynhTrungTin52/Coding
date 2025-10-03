import sympy as sp
import math
x= sp.symbols('x')
#f1a
f1a = abs(x**2 -x -7)
lm=sp.limit(f1a,x,3)
print("a)",lm)
#f1b
f1b= abs(x-1)/(x**2-1)
lm=sp.limit(f1b,x,1)
print("b)",lm)
#f1c
f1c = math.e**(1/x)
lm=sp.limit(f1c,x,1)
print("c)",lm)
#f1d
f1d= (x**4-16)/(x-2)
lm=sp.limit(f1d,x,2)
print("d)",lm)
#f1e
f1e = (x**3-x**2-5*x-3)/(x+1)**2
lm=sp.limit(f1e,x,-1)
print("e)",lm)
#f1f
f1f= (x**2-9)/(sp.sqrt(x**2+7)-4)
lm=sp.limit(f1f,x,3)
print("f)",lm)
#f1g
f1g = abs(x)/(sp.sin(x))
lm=sp.limit(f1g,x,1)
print("g)",lm)
#f1h
f1h = (1-sp.cos(x))/(x*sp.sin(x))
lm=sp.limit(f1h,x,0)
print("h)",lm)
#f1i
f1i = 2*x**2/(3-3*sp.cos(x))
lm=sp.limit(f1i,x,0)
print("i)",lm)
#f1j
f1j= ((3*x)/(-1+x))**x
lm=sp.limit(f1j,x,sp.oo)
print("j)",lm)
#f1j
f1k= (1-2/(3+x))**x
lm=sp.limit(f1k,x,sp.oo)
print("k)",lm)
#f1l
f1l= (1/x)**(1/x)
lm=sp.limit(f1l,x,sp.oo)
print("l)",lm)
#f1m
f1m= (x**(1/3)+(1+x)**(1/3))/(-sp.sqrt(x)+sp.sqrt(1+x))
lm=sp.limit(f1m,x,sp.oo)
print("m)",lm)
#f1n
f1n= sp.factorial(x)/x**x
lm=sp.limit(f1n,x,sp.oo)
print("n)",lm)
