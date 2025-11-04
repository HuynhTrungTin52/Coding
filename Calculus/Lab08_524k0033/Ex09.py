import numpy as np
import sympy as sp
import math
import matplotlib.pyplot as plt

x, y = sp.symbols('x, y')
f_xy = x*x - x*y + y*y/2 + 3    #z = f(x,y)

dfx = sp.diff(f_xy, x)  #partial derivative with regard to x
dfy = sp.diff(f_xy, y)  #partial derivative with regard to y
x0 = 3
y0 = 2
z0 = f_xy.subs(x, x0).subs(y, y0) #f(x0, y0)

#formula of the tangent plane to the surface f(x,y) at the point (x0 y0 z0):
   #z = z0 + fx'(x0, y0) * (x-x0) + fy'(x0, y0)*(y-y0)  
z = z0 + dfx.subs(x, x0).subs(y, y0)*(x-x0) + dfy.subs(x, x0).subs(y, y0)*(y-y0)
print("z = ", z)

#draw
fxy = lambda x, y: x*x - x*y + y*y/2 + 3
f_tangent = lambda x, y: 4*x - y - 2

x = np.arange(-10, 10.1, 0.1)
y = x.copy()
X,Y = np.meshgrid(x, y)
Z = fxy(X, Y)
Z_tangent = f_tangent(X, Y)

ax = plt.axes(projection ='3d')
ax.plot_surface(X, Y, Z, cmap = 'hot', linewidth=0)
ax.plot_surface(X, Y, Z_tangent, cmap = 'Blues', linewidth=0)
plt.show()