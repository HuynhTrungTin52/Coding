# This script solves Exercise 2 from Lab04.ex.pdf.
# It graphs all functions from Exercise 1 in a single figure with subplots
# and shows the limit points on the graph where possible.

import sympy as sp
from sympy.abc import x
import matplotlib.pyplot as plt
import numpy as np
import warnings

# Suppress the UserWarning from sympy's plotting module, which is not an error
warnings.filterwarnings("ignore", category=UserWarning)

# Exercise 1 functions and their limits
problems = [
    # (a)
    (sp.Abs(x**2 - x - 7), 3, r'$lim_{x\rightarrow3}|x^{2}-x-7|$'),
    # (b)
    (sp.Abs(x - 1) / (x**2 - 1), 1, r'$lim_{x\rightarrow1}\frac{|x-1|}{x^{2}-1}$'),
    # (c)
    (sp.exp(1/x), 1, r'$lim_{x\rightarrow1}\sqrt[x]{e}$'),
    # (d)
    ((x**4 - 16) / (x - 2), 2, r'$lim_{x\rightarrow2}\frac{x^{4}-16}{x-2}$'),
    # (e)
    ((x**3 - x**2 - 5*x - 3) / (x + 1)**2, -1, r'$lim_{x\rightarrow-1}\frac{x^{3}-x^{2}-5x-3}{(x+1)^{2}}$'),
    # (f)
    ((x**2 - 9) / (sp.sqrt(x**2 + 7) - 4), 3, r'$lim_{x\rightarrow3}\frac{x^{2}-9}{\sqrt{x^{2}+7}-4}$'),
    # (g)
    (sp.Abs(x) / sp.sin(x), 1, r'$lim_{x\rightarrow1}\frac{|x|}{sin(x)}$'),
    # (h)
    ((1 - sp.cos(x)) / (x * sp.sin(x)), 0, r'$lim_{x\rightarrow0}\frac{1-cosx}{xsinx}$'),
    # (i)
    ((2*x**2) / (3 - 3*sp.cos(x)), 0, r'$lim_{x\rightarrow0}\frac{2x^{2}}{3-3cosx}$'),
    # (j)
    (((3 + x) / (-1 + x))**x, sp.oo, r'$lim_{x\rightarrow\infty}(\frac{3+x}{-1+x})^{x}$'),
    # (k)
    ((1 - 2/(3+x))**x, sp.oo, r'$lim_{x\rightarrow\infty}(1-\frac{2}{3+x})^{x}$'),
    # (l)
    ((1/x)**(1/x), sp.oo, r'$lim_{x\rightarrow\infty}\sqrt[x]{\frac{1}{x}}$'),
    # (m)
    ((-sp.cbrt(x) + sp.cbrt(1+x)) / (-sp.sqrt(x) + sp.sqrt(1+x)), sp.oo, r'$lim_{x\rightarrow\infty}\frac{-\sqrt[3]{x}+\sqrt[3]{1+x}}{-\sqrt{x}+\sqrt{1+x}}$'),
    # (n)
    (sp.factorial(x) / x**x, sp.oo, r'$lim_{x\rightarrow\infty}\frac{x!}{x^{x}}$'),
]

# Set up the subplot grid with a larger figure size
fig, axes = plt.subplots(nrows=4, ncols=4, figsize=(18, 18))
axes = axes.flatten()

# Title for the entire figure, moved slightly up
fig.suptitle('Graphs of Functions from Exercise 1 with Limit Points', fontsize=18, y=1.02)

for i, (func, x_val, title) in enumerate(problems):
    ax = axes[i]
    
    # Calculate the limit using sympy's limit function
    limit_val = sp.limit(func, x, x_val)
    
    # Determine the appropriate plotting range
    if x_val == sp.oo:
        x_range = np.linspace(0.1, 10, 500)
    elif x_val == 0:
        x_range = np.linspace(-2, 2, 500)
        # Handle division by zero for functions like 1/x
        if x_val in x_range:
            x_range = np.delete(x_range, np.where(x_range == x_val))
    else:
        x_range = np.linspace(x_val - 2, x_val + 2, 500)
        # Handle removable discontinuities by plotting around the x_val
        if x_val in x_range:
            x_range = np.delete(x_range, np.where(x_range == x_val))

    try:
        # Convert sympy expression to a numpy-friendly function
        f_lambda = sp.lambdify(x, func, 'numpy')
        y_range = f_lambda(x_range)
        ax.plot(x_range, y_range)

        # Plot the limit point if it's a real number
        if isinstance(limit_val, (sp.Number, int, float)) and limit_val.is_real:
            ax.scatter([x_val], [limit_val], color='red', s=100, zorder=5)
            ax.set_title(f'Problem {chr(ord("a") + i)}: Limit is {round(limit_val, 3)}', fontsize=10)
        elif limit_val == sp.oo or limit_val == -sp.oo:
            ax.set_title(f'Problem {chr(ord("a") + i)}: Limit is $\infty$', fontsize=10)
        else:
            ax.set_title(f'Problem {chr(ord("a") + i)}: Limit does not exist', fontsize=10)

        # Set plot title and labels
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.grid(True, linestyle='--')
        ax.set_ylim([-5, 5] if x_val != sp.oo else None)
        
    except Exception as e:
        ax.set_title(f"Problem {chr(ord('a') + i)}: Error plotting", fontsize=10)
        print(f"Error plotting problem {chr(ord('a') + i)}: {e}")

# Remove any empty subplots
for i in range(len(problems), len(axes)):
    fig.delaxes(axes[i])

# Use subplots_adjust for better spacing
plt.subplots_adjust(wspace=0.3, hspace=0.5)
plt.show()
