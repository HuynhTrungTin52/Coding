import numpy as np
import matplotlib.pyplot as plt

def is_1to1(x,fx):
    codomain=[]
    
    for i in x:
        if fx(i) in codomain:
            return False
        else:
            codomain.append((fx(i)))    
    return True         


fx_a= lambda x: x**3-x/2
x=np.arange(-10,10,0.001)
print("a.x^3-x/2:",is_1to1(x,fx_a))
plt.subplot(1,2,1)
plt.plot(x,fx_a(x))
plt.title("x**3-x/2")
fx_b= lambda x: x**2+x/2
print("b.x^2+x/2:",is_1to1(x,fx_b))
plt.subplot(1,2,2)
plt.plot(x,fx_b(x))
plt.title("x**2+x/2")
plt.grid()
plt.show()