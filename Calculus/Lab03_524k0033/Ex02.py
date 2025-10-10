import sympy as sp
#Ex2

def findTangent(x,f,df,pointX,pointY,title):
	#Find the equation of the tangent line at the point (2,5) => a = 2, f(a) = f(2) = 2*2+1 = 5
	slope = df.subs(x, pointX)  # = df(2) <=> df(a) <=> f'(a)
	y_tangentLine = slope*(x - pointX) + pointY  #y = f'(a)(x - a) + f(a)
	sp.plot(f, y_tangentLine, (x, -5, 5),title=title)  #draw graph

#The tangent line to y = f(x) at point ( a, f(a) ) is the line passing through (a, f(a)) with slope f'(a)

x = sp.symbols('x')
f = x*x + 1
df = sp.diff(f, x)
findTangent(x,f,df,2,5,"a)")

f=x-2*x*x
df= sp.diff(f,x)
findTangent(x,f,df,1,-1,"b)")


f = x/(x-2)
df = sp.diff(f, x)
findTangent(x, f, df, 3, 3, "c)")


g = 8/(x**2)
dg = sp.diff(g, x)
findTangent(x, g, dg, 2, 2, "d)")


g = sp.sqrt(x)
dg = sp.diff(g, x)
findTangent(x, g, dg, 4, 2, "e)")


t = sp.symbols('t')
h = t**3 + 3*t
dh = sp.diff(h, t)
findTangent(t, h, dh, 1, 4, "f)")


f = 8/sp.sqrt(x-2)
df = sp.diff(f, x)
findTangent(x, f, df, 6, 4, "g)")


z = sp.symbols('z')
g = 1 + sp.sqrt(4 - z)
dg = sp.diff(g, z)
findTangent(z, g, dg, 3, 2, "h)")