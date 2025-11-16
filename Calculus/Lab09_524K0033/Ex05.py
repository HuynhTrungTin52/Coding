import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def golden_search_trace(f, a, b, tol):
    tau = (math.sqrt(5) - 1) / 2
    d = b - a
    trace = []
    while (b - a) >= tol:
        d *= tau
        x1 = b - d
        x2 = a + d
        fx1 = f(x1)
        fx2 = f(x2)
        trace.append((a, b, x1, x2, fx1, fx2))
        if fx1 <= fx2:
            b = x2
        else:
            a = x1
    return a, b, trace

f = lambda x: x*x
a0, b0 = -2, 1
tol = 0.5
a, b, steps = golden_search_trace(f, a0, b0, tol)
minimum_estimate = (f(a) + f(b)) / 2
print("Estimated minimum value =", minimum_estimate)

# Animation
xs = np.linspace(a0 - 1, b0 + 1, 400)
ys = f(xs)

fig, ax = plt.subplots()
ax.plot(xs, ys, 'k')
interval_line, = ax.plot([], [], 'b', lw=3, label='[a,b]')
x1_point, = ax.plot([], [], 'ro', label='x1')
x2_point, = ax.plot([], [], 'go', label='x2')
ax.legend()
ax.set_title("Golden Section Search Iterations")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")

def init():
    interval_line.set_data([], [])
    x1_point.set_data([], [])
    x2_point.set_data([], [])
    return interval_line, x1_point, x2_point

def update(i):
    a_i, b_i, x1, x2, fx1, fx2 = steps[i]
    interval_line.set_data([a_i, b_i], [f(a_i), f(b_i)])
    x1_point.set_data([x1], [fx1])
    x2_point.set_data([x2], [fx2])
    ax.set_xlim(xs.min(), xs.max())
    ax.set_ylim(0, ys.max()*1.1)
    ax.set_title(f"Iteration {i+1}: a={a_i:.3f}, b={b_i:.3f}")
    return interval_line, x1_point, x2_point

# print(a,b)
ani = FuncAnimation(fig, update, frames=len(steps), init_func=init, interval=1200, blit=True, repeat=False)

plt.show()
