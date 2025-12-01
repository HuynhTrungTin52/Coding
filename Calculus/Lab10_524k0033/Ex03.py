import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def average_value(f, a, b):
	x = sp.symbols('x')
	return sp.simplify((1/(b - a)) * sp.integrate(f, (x, a, b)))

def plot_function(ax, f_lambda, a, b, title):
	xs = np.linspace(a, b, 400)
	ys = f_lambda(xs)
	ax.plot(xs, ys, label=title)
	ax.axhline(0, color='black', linewidth=0.5)
	ax.axvline(0, color='black', linewidth=0.5)
	ax.legend()
	ax.grid(True, linestyle='--', alpha=0.4)
	ax.set_xlabel('x')
	ax.set_ylabel('f(x)')
	ax.set_title(title)

x = sp.symbols('x')

# (a)
a_a, b_a = 0, sp.sqrt(3)
f_a = x**2 - 1
avg_a = average_value(f_a, a_a, b_a)

# (b)
a_b, b_b = 0, 3
f_b = -x**2/2
avg_b = average_value(f_b, a_b, b_b)

# (c)
a_c, b_c = 0, 1
f_c = -3*x**2 - 1
avg_c = average_value(f_c, a_c, b_c)

# (d)
a_d, b_d = -2, 1
f_d = x**2 - x
avg_d = average_value(f_d, a_d, b_d)

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

plot_function(
	axs[0, 0],
	lambda t: t**2 - 1,
	float(a_a),
	float(b_a),
	"f(x)=x^2-1 on [0, √3]"
)

plot_function(
	axs[0, 1],
	lambda t: -t**2/2,
	a_b,
	b_b,
	"f(x)=-x^2/2 on [0, 3]"
)

plot_function(
	axs[1, 0],
	lambda t: -3*t**2 - 1,
	a_c,
	b_c,
	"f(x)=-3x^2-1 on [0, 1]"
)

plot_function(
	axs[1, 1],
	lambda t: t**2 - t,
	a_d,
	b_d,
	"f(x)=x^2-x on [-2, 1]"
)

plt.tight_layout()

print("Average values (exact):")
print(f"(a) {avg_a}")
print(f"(b) {avg_b}")
print(f"(c) {avg_c}")
print(f"(d) {avg_d}")

print("\nAverage values (decimal):")
print(f"(a) {float(avg_a)}")
print(f"(b) {float(avg_b)}")
print(f"(c) {float(avg_c)}")
print(f"(d) {float(avg_d)}")

plt.show()