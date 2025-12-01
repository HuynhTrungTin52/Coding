import sympy as sp
import numpy as np

import matplotlib.pyplot as plt

x, y = sp.symbols('x y')

# (a)
f_a = x**3 - 3*sp.sin(x)*sp.cos(x)
I_a = sp.integrate(f_a, (x, 0, sp.pi/2))
I_a_simplified = sp.simplify(I_a)

# (b) 
f_b = sp.sin(x**2)**2
I_b = sp.integrate(f_b, (x, 0, 1))  
I_b_numeric = sp.N(I_b)

t = sp.Symbol('t')
C_val = sp.fresnelc(2/sp.sqrt(sp.pi))
I_b_closed = sp.Rational(1,2) - sp.sqrt(sp.pi)/4 * C_val

g = lambda z: z + 1
inside_c = 1 + g(x**2) + g(x)**2               
f_c = sp.sqrt(sp.simplify(inside_c))
I_c = sp.integrate(f_c, (x, 0, 3))
I_c_numeric = sp.N(I_c)

f_d = x**2 * y
I_d = sp.integrate(f_d, (x, 0, 3), (y, 1, 2))
I_d_numeric = sp.N(I_d)

print("Integral (a):", I_a_simplified, "≈", sp.N(I_a_simplified))
print("Integral (b):", "~", I_b_numeric)
print("Integral (b):", "~", sp.N(I_b_closed))
print("Integral (c):", "~", I_c_numeric)
print("Double Integral (d):","~", I_d_numeric)

f_a_num = sp.lambdify(x, f_a, 'numpy')
f_b_num = sp.lambdify(x, f_b, 'numpy')
f_c_num = sp.lambdify(x, f_c, 'numpy')
f_d_num = sp.lambdify((x, y), f_d, 'numpy')

xa = np.linspace(0, np.pi/2, 400)
xb = np.linspace(0, 1, 400)
xc = np.linspace(0, 3, 400)
x_d = np.linspace(0, 3, 120)
y_d = np.linspace(1, 2, 120)
X_d, Y_d = np.meshgrid(x_d, y_d)
Z_d = f_d_num(X_d, Y_d)

fig = plt.figure(figsize=(10, 8))
axs = [
	fig.add_subplot(2, 2, 1),
	fig.add_subplot(2, 2, 2),
	fig.add_subplot(2, 2, 3),
	fig.add_subplot(2, 2, 4, projection='3d')
]

# (a)
axs[0].plot(xa, f_a_num(xa))
axs[0].set_title("(a) Integrand: x^3 - 3 sin(x) cos(x)")
axs[0].set_xlabel("x")
axs[0].set_ylabel("f_a(x)")
axs[0].grid(alpha=0.3)

# (b)
axs[1].plot(xb, f_b_num(xb))
axs[1].set_title("(b) Integrand: sin(x^2)^2")
axs[1].set_xlabel("x")
axs[1].set_ylabel("f_b(x)")
axs[1].grid(alpha=0.3)

# (c)
axs[2].plot(xc, f_c_num(xc))
axs[2].set_title("(c) Integrand: sqrt(2x^2 + 2x + 3)")
axs[2].set_xlabel("x")
axs[2].set_ylabel("f_c(x)")
axs[2].grid(alpha=0.3)

# (d) Surface plot
axs[3].plot_surface(X_d, Y_d, Z_d, cmap='viridis')
axs[3].set_title("(d) Integrand: x^2 y")
axs[3].set_xlabel("x")
axs[3].set_ylabel("y")
axs[3].set_zlabel("f_d(x,y)")

plt.tight_layout()
plt.show()
