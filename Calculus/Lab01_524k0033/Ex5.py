import numpy as np
import math
import matplotlib.pyplot as plt

f1_x = lambda x: math.sqrt(1-((abs(x)-1)**2))
f2_x = lambda x: -3*math.sqrt(1-math.sqrt((abs(x))/2))
range=np.arange(-2,2,0.00001)
f1_colour="magenta"
f2_colour="red"

x_array1=range
x_array2=range

y_array1=list(map(f1_x,x_array1))
y_array2=list(map(f2_x,x_array2))

plt.plot(x_array1,y_array1,color=f1_colour)
plt.plot(x_array2,y_array2,color=f2_colour)

plt.show()