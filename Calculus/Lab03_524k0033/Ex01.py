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

dd = sp.diff(kd, z)
print("d)", dd)

ke = sp.sqrt(3*z)
de = sp.diff(ke, z)
print("e)", de)

kf = sp.sqrt(2*z + 1)
df_k = sp.diff(kf, z)
print("f)", df_k)