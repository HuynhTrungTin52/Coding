import numpy as np

import matplotlib.pyplot as plt


def uniform_cdf(x, a=0.0, b=1.0):
	x = np.asarray(x, dtype=float)
	if b == a:
		return np.where(x < a, 0.0, 1.0)
	return np.where(x < a, 0.0, np.where(x > b, 1.0, (x - a) / (b - a)))


# 1. create x values from 0 to 1
x = np.linspace(0.0, 1.0, 101)
# 2. compute the cdf using the formula
a, b = 0.0, 1.0
cdf = uniform_cdf(x, a, b)
np.set_printoptions(precision=3, suppress=True)
print("x values:", x)
print("CDF values:", cdf)
plt.figure(figsize=(6, 3))
plt.step(x, cdf, where="post", label=f"Uniform({a},{b}) CDF")
plt.xlabel("x")
plt.ylabel("F(x)")
plt.title("CDF of Uniform Distribution on [0, 1]")
plt.ylim(-0.05, 1.05)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()