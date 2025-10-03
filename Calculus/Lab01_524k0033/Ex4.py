import matplotlib.pyplot as plt
import numpy as np
import math

fig,axs = plt.subplots(2,3)
range=np.arange(-10,10.1,0.1)
#4i
fx_4i=lambda x: -x**3
x_arrayi=range
y_arrayi=list(map(fx_4i,x_arrayi)) 
axs[0,0].plot(x_arrayi,y_arrayi,color="cyan")
axs[0,0].set_title("4i")
print("4i. f(x) is decreasing a x-values belong to(-inf,inf)")

#4j
fx_4j= lambda x : -(1/x**2)
x_arrayj=range
y_arrayj=list(map(fx_4j,x_arrayj)) 

axs[1,0].plot(x_arrayj,y_arrayj,color="pink")
axs[1,0].set_title("4j")
print("4j. f(x) is decreasing a x-values belong to(-inf,inf)")

#4k
fx_4k=lambda x: -(1/x)
x_arrayk=range
y_arrayk=list(map(fx_4k,x_arrayk))
axs[0,1].plot(x_arrayk,y_arrayk,color="lime")
axs[0,1].set_title("4k")
print("4k. f(x) is decreasing a x-values belong to(-inf,inf)")

#4l
fx_4l=lambda x: -(1/abs(x))
x_arrayl=range
y_arrayl=list(map(fx_4l,x_arrayl))
axs[1,1].plot(x_arrayl,y_arrayl,color="orange")
axs[1,1].set_title("4l")
print("4l. f(x) is decreasing a x-values belong to(-inf,inf)")

#4m
fx_4m=lambda x: math.sqrt(abs(x))
x_arraym=range
y_arraym=list(map(fx_4m,x_arraym))
axs[0,2].plot(x_arraym,y_arraym,color="red")
axs[0,2].set_title("4m")
print("4m. f(x) is decreasing a x-values belong to(-inf,inf)")

#4n
fx_4n=lambda x: math.sqrt(abs(-x))
x_arrayn=range
y_arrayn=list(map(fx_4n,x_arrayn))
axs[1,2].plot(x_arrayn,y_arrayn,color="black")
axs[1,2].set_title("4n")
print("4n. f(x) is decreasing a x-values belong to(-inf,inf)")

for row in axs:
    for ax in row:
    	ax.grid()

plt.tight_layout()
plt.show()