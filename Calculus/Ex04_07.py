import sympy as sp

x = sp.symbols('x')

cos_series = sp.series(sp.cos(x), x, 0, 6)
print("Maclaurin series for cos(x) up to order 6:")
print(sp.simplify(cos_series))

exp_series = sp.series(sp.exp(x), x, 0, 12)
print("\nMaclaurin series for e^x up to order 12:")
print(sp.simplify(exp_series))

inverse_series = sp.series(1 / (1 - x), x, 0, 12)
print("\nMaclaurin series for 1 / (1 - x) up to order 12:")
print(sp.simplify(inverse_series))

arctan_series = sp.series(sp.tan(x)**-1, x, 0, 12)
print("\nMaclaurin series for tan^(-1)(x) up to order 12:")
print(sp.simplify(arctan_series))