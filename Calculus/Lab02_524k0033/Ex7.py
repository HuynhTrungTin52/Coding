import sympy as sp

# Define the symbol
x = sp.symbols('x')

# --- Exercise 7, Part 1 ---
print("1)")

# Define the function
f1 = (x**2 - x - 2) / (x - 2)

# Find where the denominator is zero to identify potential discontinuities
denominator1 = sp.denom(f1)
discontinuities1 = sp.solve(denominator1, x)

print(f"Function 1: f(x) = {f1}")
print(f"To find where the function is discontinuous, we look for points where the denominator is zero.")
print(f"Denominator: {denominator1}")
print(f"Solving the equation {denominator1} = 0 gives x = {discontinuities1}.")
print(f"Conclusion: The function f(x) = {f1} is discontinuous at x = 2.")

print()

# --- Exercise 7, Part 2 ---
print("2)")

# Define the function
f2 = (x**2 - 2*x - 3) / (2*x - 6)

# Find where the denominator is zero
denominator2 = sp.denom(f2)
discontinuities2 = sp.solve(denominator2, x)

print(f"Function 2: f(x) = {f2}")
print(f"To find where the function is discontinuous, we look for points where the denominator is zero.")
print(f"Denominator: {denominator2}")
print(f"Solving the equation {denominator2} = 0 gives x = {discontinuities2}.")
print(f"Conclusion: The function f(x) = {f2} is discontinuous at x = 3.")
