import sympy as sp 

x=sp.symbols('x')
problems=[
	3*x**4-16*x**3+18*x**2-9,
	(x+2)/(2*x*x),
	-x**3/3+x*x+3*x+4,
	(5*x**2+5)/x
	
]

for i in problems:
    print(f"Math expression : {i}")
    df=sp.diff(i,x)
    print(f"Derivative = {df}")
    cvals=sp.solve(df,x)
    print(f"Critcal values: {cvals}")
    print()
# df=sp.diff(f,x)
# print("Derivative =",df)

# cvals = sp.solve(df,x)
# print("Critical values:",cvals)