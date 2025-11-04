import sympy as sp

x, y = sp.symbols('x y')

# Put your functions here. Edit/add keys to match parts (a)-(f) from the problem image.
funcs = {
	'a': x*sp.sin(y) + y*sp.sin(x) + x*y,
	'b': sp.log(2*x + 3*y),
	'c': x*y**2 + x**2*y**3 + x**3*y**4,
	# example for another part (edit if different in your image)
	# 'd': <your expression>,
	# 'e': <your expression>,
	'f': sp.exp(x) + x*sp.log(y) + y*sp.log(x),
}

for label, f in funcs.items():
	f_xy = sp.diff(sp.diff(f, x), y)
	f_yx = sp.diff(sp.diff(f, y), x)
	diff = sp.simplify(f_xy - f_yx)

	print(f"Part {label}: f = {f}")
	print(f"  f_xy = {sp.expand(f_xy)}")
	print(f"  f_yx = {sp.expand(f_yx)}")
	print(f"  f_xy - f_yx simplified = {diff}")
	if diff == 0:
		print("  => f_xy = f_yx (equal)\n")
	else:
		print("  => f_xy != f_yx (not equal)\n")