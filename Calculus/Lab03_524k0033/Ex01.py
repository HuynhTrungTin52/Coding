import sympy as sp

x=sp.symbols('x')
fa=4-x*x
df=sp.diff(fa,x) #f'
print("a)",df)

fb=(x-1)**2+1
df=sp.diff(fb,x)
print("b)",df)

t=sp.symbols('t')
gc=1/(t*t)
dg=sp.diff(gc,t)
print("c)",dg)

z=sp.symbols('z')
kd=(1-z)/(2*z)
