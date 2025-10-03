#import modules
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-9,5)
y=x**2
z=x+5
plt.plot(x,y,z,'r')
plt.plot(x,z*z,'k')
plt.plot([-3,-3],[0,80],label="Totally in the middle")
plt.legend()
plt.show()