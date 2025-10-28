import sympy
import numpy as np
import matplotlib.pyplot as plt

# --- Step 1: Set up symbolic variables and functions ---

# Define 'x' as a symbolic variable
x = sympy.symbols('x')

# Set the constant A. We will use A = 10 as before.
A = 10

# Define the functions f(x) and g(x) using sympy
f = x**2 - 2*A*x - A**2
g = -x**2 + 4*A*x + A**3

print(f"Using SymPy with A = {A}")
print(f"f(x) = {f}")
print(f"g(x) = {g}")
print("-" * 30)

# --- Step 2: Solve for intersection points symbolically ---

# Create the equation f(x) = g(x)
# SymPy's Eq function creates an equality
equation = sympy.Eq(f, g)
print(f"Equation to solve: {equation}")

# Solve the equation for x
# The result will be a list of symbolic solutions
x_solutions = sympy.solve(equation, x)

print("Symbolic x-solutions:")
print(x_solutions)

# --- Step 3: Calculate y-coordinates for each x-solution ---

intersection_points = []
for x_sol in x_solutions:
    # Substitute the x-solution back into f(x) to find the y-coordinate
    y_sol = f.subs(x, x_sol)
    intersection_points.append((x_sol, y_sol))

print("\nSymbolic intersection points (x, y):")
# We can use sympy.simplify to clean up the y-coordinate expression
for point in intersection_points:
    print(f"({point[0]}, {sympy.simplify(point[1])})")

print("\nNumerical intersection points (x, y):")
# Store numerical values for plotting
numerical_points = []
for point in intersection_points:
    # .evalf() evaluates the symbolic expression to a float
    x_num = point[0].evalf()
    y_num = point[1].evalf()
    numerical_points.append((x_num, y_num))
    print(f"({x_num:.2f}, {y_num:.2f})")

# --- Step 4: Plot the functions and intersection points ---

# Convert the symbolic sympy functions into numerical functions
# This allows them to be used with a NumPy array
f_num = sympy.lambdify(x, f, 'numpy')
g_num = sympy.lambdify(x, g, 'numpy')

# Generate a smooth range of x values for the plot
# We base the range on the numerical x-solutions
x1_num = float(numerical_points[0][0])
y1_num = float(numerical_points[0][1])
x2_num = float(numerical_points[1][0])
y2_num = float(numerical_points[1][1])

x_range = np.linspace(x1_num - 10, x2_num + 10, 400)
y_f = f_num(x_range)
y_g = g_num(x_range)

# Create the plot using matplotlib
plt.figure(figsize=(10, 6))
# Use latex formatting for the labels, pulling from the sympy functions
plt.plot(x_range, y_f, label=f'$f(x) = {sympy.latex(f)}$')
plt.plot(x_range, y_g, label=f'$g(x) = {sympy.latex(g)}$')

# Mark the intersection points
plt.plot(x1_num, y1_num, 'ko', markersize=8, label=f'Intersection 1 ({x1_num:.2f}, {y1_num:.2f})')
plt.plot(x2_num, y2_num, 'ko', markersize=8, label=f'Intersection 2 ({x2_num:.2f}, {y2_num:.2f})')

# Add titles, labels, a grid, and a legend
plt.title(f'Intersection of f(x) and g(x) using SymPy (A = {A})')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid(True)
plt.legend()
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.show()