import numpy as np
from scipy.integrate import quad

import matplotlib.pyplot as plt

# (a) 
def f1(x):
	return x**2 * np.cos(x)

def area_f1():
	return quad(lambda t: np.abs(f1(t)), -4, 9, limit=200)[0]

# (b)
a = 0.5
def g(x):
	return np.exp(-a * x**2)

def area_g():
	val, _ = quad(lambda t: g(t), -np.inf, np.inf, limit=200)
	return val


area1 = area_f1()
area2 = area_g()
x1 = np.linspace(-4, 9, 1000)
x2 = np.linspace(-6, 6, 1000)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].plot(x1, f1(x1), label='f(x) = x^2 cos(x)')
axes[0].axhline(0, color='black', linewidth=0.8)
axes[0].set_title(f'(a) f(x)=x^2 cos(x), Area ≈ {area1:.6f}')
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].legend(loc='best')

axes[1].plot(x2, g(x2), label='g(x) = exp(-a x^2), a=1/2')
axes[1].axhline(0, color='black', linewidth=0.8)
axes[1].set_title(f'(b) g(x)=e^(-a x^2), Area over R ≈ {area2:.6f}')
axes[1].set_xlabel('x')
axes[1].set_ylabel('g(x)')
axes[1].legend(loc='best')
plt.tight_layout()
plt.show()