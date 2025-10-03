import numpy as np
import sympy as sp

x = sp.symbols('x')
g_x_not_0 = (x**2 - x - 6) / (x - 3)
g_x_0 = 5

print("a)")
lm_x_0 = sp.limit(g_x_not_0, x, 0)
f_0 = g_x_0

print(f"Limit of g(x) as x -> 0: {lm_x_0}")
print(f"Value of g(x) at x = 0: {f_0}")

if lm_x_0 == f_0:
    print("The function is continuous at x = 0.")
else:
    print("The function is discontinuous at x = 0.")

print("\nChecking for continuity at other points...")
discontinuous_points = []
for c in np.arange(-10, 10, 1):
    if c != 0:
        lm_x_c = sp.limit(g_x_not_0, x, c)
        f_c = g_x_not_0.subs(x, c)
        if lm_x_c != f_c:
            discontinuous_points.append(c)

if len(discontinuous_points) == 0:
    print("The function is continuous for all x != 0.")
else:
    print(f"The function is discontinuous at: {discontinuous_points}")

print("b)")
f_x_not_2_not_neg2 = (x**3 - 8) / (x**2 - 4)
f_2 = 3
f_neg2 = 4

lm_x_2 = sp.limit(f_x_not_2_not_neg2, x, 2)
print(f"Limit of f(x) as x -> 2: {lm_x_2}")
print(f"Value of f(x) at x = 2: {f_2}")
if lm_x_2 == f_2:
    print("The function is continuous at x = 2.")
else:
    print("The function is discontinuous at x = 2.")

lm_x_neg2 = sp.limit(f_x_not_2_not_neg2, x, -2)
print(f"\nLimit of f(x) as x -> -2: {lm_x_neg2}")
print(f"Value of f(x) at x = -2: {f_neg2}")
if lm_x_neg2 == f_neg2:
    print("The function is continuous at x = -2.")
else:
    print("The function is discontinuous at x = -2.")

print("\nChecking for continuity at other points...")
discontinuous_points_b = []
for c in np.arange(-10, 10, 1):
    if c != 2 and c != -2:
        lm_x_c = sp.limit(f_x_not_2_not_neg2, x, c)
        f_c = f_x_not_2_not_neg2.subs(x, c)
        if lm_x_c != f_c:
            discontinuous_points_b.append(c)

if not discontinuous_points_b:
    print("The function is continuous for all x != 2 and x != -2.")
else:
    print(f"The function is discontinuous at: {discontinuous_points_b}")

print("c)")
f_x_not_2 = (x**2 - x - 2) / (x - 2)
f_2_c = 1

lm_x_2_c = sp.limit(f_x_not_2, x, 2)
print(f"Limit of f(x) as x -> 2: {lm_x_2_c}")
print(f"Value of f(x) at x = 2: {f_2_c}")
if lm_x_2_c == f_2_c:
    print("The function is continuous at x = 2.")
else:
    print("The function is discontinuous at x = 2.")

print("d)")
f_x_not_0 = 1 / x**2
f_0_d = 1

lm_x_0_d = sp.limit(f_x_not_0, x, 0)
print(f"Limit of f(x) as x -> 0: {lm_x_0_d}")
print(f"Value of f(x) at x = 0: {f_0_d}")
if lm_x_0_d == f_0_d:
    print("The function is continuous at x = 0.")
else:
    print("The function is discontinuous at x = 0.")