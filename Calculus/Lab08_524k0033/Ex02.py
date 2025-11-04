import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-6, 6.1, 0.1)
y = x.copy()
X, Y = np.meshgrid(x, y)

f1 = lambda X, Y: np.cos(X) * np.cos(Y) * np.exp(-np.sqrt(X**2 + Y**2) / 4)
den = X**2 + Y**2
den_safe = np.where(den == 0, 1e-12, den)  
f2 = lambda X, Y: - X * Y**2 / den_safe
f3 = lambda X, Y: X * Y * (X**2 - Y**2) / den_safe
f4 = lambda X, Y: Y**2 - Y**4 - X**2

Z1 = f1(X, Y)
Z2 = f2(X, Y)
Z3 = f3(X, Y)
Z4 = f4(X, Y)

fig = plt.figure(figsize=(14, 10))

ax = fig.add_subplot(2, 2, 1, projection='3d')
ax.plot_surface(X, Y, Z1, cmap='viridis', linewidth=0, antialiased=True)
ax.set_title(r'(a) $f(x,y)=\cos x\cos y\,e^{-\sqrt{x^2+y^2}/4}$')

ax = fig.add_subplot(2, 2, 2, projection='3d')
ax.plot_surface(X, Y, Z2, cmap='plasma', linewidth=0, antialiased=True)
ax.set_title(r'(b) $f(x,y)=-\dfrac{x y^2}{x^2+y^2}$')

ax = fig.add_subplot(2, 2, 3, projection='3d')
ax.plot_surface(X, Y, Z3, cmap='inferno', linewidth=0, antialiased=True)
ax.set_title(r'(c) $f(x,y)=\dfrac{x y (x^2-y^2)}{x^2+y^2}$')

ax = fig.add_subplot(2, 2, 4, projection='3d')
ax.plot_surface(X, Y, Z4, cmap='magma', linewidth=0, antialiased=True)
ax.set_title(r'(d) $f(x,y)=y^2 - y^4 - x^2$')

plt.tight_layout()
plt.show()
