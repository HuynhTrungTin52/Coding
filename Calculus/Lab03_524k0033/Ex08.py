import sympy as sp

# Ex08

# 8a: similar to Ex2
# Find the tangent line of f(x) at the tangent point (x0, y0):
# x0 = 3 ---> y0 = f(x0) = f(3)
x = sp.symbols('x')
f = x**3 - 3*x + 1
df = sp.diff(f, x)

x0 = 3
slope = df.subs(x, x0)            # f'(x0)
y0 = f.subs(x, x0)
tangentLine_8a = slope*(x - x0) + y0  # y = f'(x0)(x - x0) + f(x0)

print(f"f(x) = {sp.expand(f)}")
print(f"f'({x0}) = {slope}")
print(f"Tangent line at x = {x0}: y = {sp.expand(tangentLine_8a)}")

# plot 8a and solve 8b & 8c


# Ex 8b:
sol_8b = sp.solve(sp.Eq(df, 9), x)        
tangent_lines_8b = []
print("Ex 8b: f'(x) = 9 at x =", sol_8b)
for xi in sol_8b:
	yi = f.subs(x, xi)
	line = sp.expand(9*(x - xi) + yi)    
	tangent_lines_8b.append(line)
	print(f"  tangent at x = {xi}: y = {line}")

# Ex 8c: 
t = sp.symbols('t')
a = sp.Rational(2, 3)
b = -1
eq = sp.Eq(b, df.subs(x, t)*(a - t) + f.subs(x, t))
sol_8c = sp.solve(eq, t)
tangent_lines_8c = []
print("Ex 8c: tangent points t solving line-through-A condition:", sol_8c)
for tv in sol_8c:
	m = df.subs(x, tv)
	y_tv = f.subs(x, tv)
	line = sp.simplify(m*(x - tv) + y_tv)
	tangent_lines_8c.append(line)
	print(f"  tangent at t = {tv}: slope = {m}, y = {line}")

all_lines = [tangentLine_8a] + tangent_lines_8b + tangent_lines_8c
sp.plot(f, *all_lines, (x, -5, 5))