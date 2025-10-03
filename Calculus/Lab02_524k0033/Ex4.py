import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define the symbol
x = sp.symbols('x')

# Define the functions for plotting
def f(x_val):
    if x_val > 0:
        return np.sin(1/x_val)
    else:
        return 0

# Create a range of x values
x_vals_pos = np.arange(0.0001, 0.5, 0.001)
x_vals_neg = np.arange(-0.5, 0, 0.001)

# Apply the function to the x values
y_vals_pos = [f(val) for val in x_vals_pos]
y_vals_neg = [f(val) for val in x_vals_neg]

# Find the limits using SymPy
limit_right = sp.limit(sp.sin(1/x), x, 0, dir='+')
limit_left = sp.limit(0, x, 0, dir='-')

# Plot the function
plt.figure()
plt.plot(x_vals_pos, y_vals_pos, label='f(x) for x > 0')
plt.plot(x_vals_neg, y_vals_neg, label='f(x) for x < 0')
plt.plot(0, 0, 'ro', label='f(0) = 0')
plt.axvline(x=0, color='gray', linestyle='--', linewidth=0.5)
plt.axhline(y=0, color='gray', linestyle='--', linewidth=0.5)
plt.title('Plot of f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

# Print the results of the limits
print(f"Right-hand limit as x approaches 0: {limit_right}")
print(f"Left-hand limit as x approaches 0: {limit_left}")
print(f"Overall limit as x approaches 0: Does not exist because the right and left limits are not equal.")