import sympy as sp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def newton_method(f_sym, x_sym, p0, tol, max_iter, stop_after_n=None):
w
    df_sym = sp.diff(f_sym, x_sym)

    f = sp.lambdify(x_sym, f_sym, 'numpy')
    df = sp.lambdify(x_sym, df_sym, 'numpy')
    
    p_current = float(p0) 
    results = [] 
    
    print(f"Starting Newton's method for f(x) = {f_sym}")
    print(f"f'(x) = {df_sym}")
    print(f"p0 = {p0}, tolerance = {tol}, max_iter = {max_iter}\n")

    for i in range(max_iter + 1):
        f_val = f(p_current)
        
        results.append((i, p_current, f_val))

        if abs(f_val) < tol:
            print(f"Success: Tolerance |f(p_i)| < {tol} reached at iteration {i}.")
            return results
        
        if stop_after_n is not None and i == stop_after_n:
            print(f"Stopping after required {stop_after_n} iterations.")
            return results

        df_val = df(p_current)
        
        if df_val == 0:
            print(f"Error: Derivative is zero at p_{i}={p_current}. Method fails.")
            return results
            
        p_current = p_current - f_val / df_val

    print(f"Failure: Method did not converge within {max_iter} iterations.")
    return results

def print_table(results):

    df = pd.DataFrame(results, columns=['Iteration (i)', 'p_i', 'f(p_i)'])

    df['p_i'] = df['p_i'].map('{:,.12f}'.format)
    df['f(p_i)'] = df['f(p_i)'].map('{:.2e}'.format)
    print(df.to_string(index=False))

def plot_results(f_sym, x_sym, results, title):

    f = sp.lambdify(x_sym, f_sym, 'numpy')
    
    p_values = [res[1] for res in results]
    
    p_min, p_max = min(p_values), max(p_values)
    margin = abs(p_max - p_min) * 0.5 + 1.0
    x_vals = np.linspace(p_min - margin, p_max + margin, 400)
    y_vals = f(x_vals)
    
    plt.figure(figsize=(12, 7))

    plt.plot(x_vals, y_vals, label=f'$f(x) = {sp.latex(f_sym)}$', lw=2)

    plt.axhline(0, color='black', linestyle='--', lw=1)
    
    for i in range(len(results) - 1):
        p_i = results[i][1]
        f_p_i = results[i][2]
        p_i_plus_1 = results[i+1][1]
        
        plt.plot(p_i, f_p_i, 'ro')
        plt.text(p_i, f_p_i, f'  $p_{i}$')
        plt.plot([p_i, p_i_plus_1], [f_p_i, 0], 'g--')
        plt.plot([p_i_plus_1, p_i_plus_1], [0, results[i+1][2]], 'r:', lw=0.8)

    p_last = results[-1][1]
    f_p_last = results[-1][2]
    plt.plot(p_last, f_p_last, 'ro', label='Iteration points $(p_i, f(p_i))$')
    plt.text(p_last, f_p_last, f'  $p_{len(results)-1}$')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()


x = sp.symbols('x')


#a)
f_a = 2*x**3 + 3*x - 1
p0_a = 2.0
tol_a = 1e-8
max_iter_a = 100

results_a = newton_method(f_a, x, p0_a, tol_a, max_iter_a)
print_table(results_a)
plot_results(f_a, x, results_a, "Newton's Method for $f(x) = 2x^3 + 3x - 1$")


#b)
f_b = x**3 - 4
p0_b = 2.0
tol_b = 1e-10 
max_iter_b = 100
stop_iter_b = 3 

results_b = newton_method(f_b, x, p0_b, tol_b, max_iter_b, stop_after_n=stop_iter_b)
print_table(results_b)
plot_results(f_b, x, results_b, "Newton's Method for $f(x) = x^3 - 4$ (3 Iterations)")