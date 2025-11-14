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
    f2 = sp.diff(i, x, 2)
    for c in cvals:
        try:
            f_val = i.subs(x, c)
        except Exception:
            continue
        if f_val.has(sp.zoo):
            continue
        second = f2.subs(x, c)
        if second > 0:
            print(f"  Local minimum at x={c}, f(x)={sp.simplify(f_val)}")
        elif second < 0:
            print(f"  Local maximum at x={c}, f(x)={sp.simplify(f_val)}")
        else:
            print(f"  Inconclusive at x={c} (f''={second})")
    print()