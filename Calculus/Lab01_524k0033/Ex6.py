import numpy as np
import matplotlib.pyplot as plt

fig,axs = plt.subplots(2,5,figsize=(20,7))

def f6_a(x, k):
 return x**2+k

def cau6a(axs):
    k = np.arange(2,13,2)
    x = np.arange(-10,11,1)
    for ki in k:
        y = []
        for xi in x:
            y.append(f6_a(xi,ki))
        axs[0,0].plot(x, y, label = "k=" + str(ki) )
        axs[0,0].set_title("Cau 6a")
        axs[0,0].legend(fontsize='small')
    axs[0,0].grid()
    
def f6_b(x,k):
    return (x+k)**2

def cau6b(axs):
    k = np.arange(2,13,2)
    x = np.arange(-10,11,1)
    for ki in k:
        y = []
        for xi in x:
            y.append(f6_b(xi,ki))
        axs[0,1].plot(x, y, label = "k=" + str(ki) )
        axs[0,1].set_title("Cau 6b")
        axs[0,1].legend(fontsize='small')
    axs[0,1].grid()

import math
def f6_c(x,k):
    return k*math.sqrt(x)

def cau6c(axs):
    k = [1/3,1,3,6]
    x = np.arange(1,51,1)
    for ki in k:
        y = []
        for xi in x:
            y.append(f6_b(xi,ki))
        axs[0,2].plot(x, y, label = "k=" + str(ki) )
        axs[0,2].set_title("Cau 6c")
        axs[0,2].legend(fontsize='small')
    axs[0,2].grid()
    
def f6_d_o(x):
    return x**3


def cau6d(axs):
    x=np.arange(-2,2.1,0.1)
    y_original=[]
    for xi in x:
        y_original.append(f6_d_o(xi))
    y=np.array(y_original)
    axs[0,3].plot(x,y,label="Original")
    axs[0,3].plot(x+1,y-5,label="Shifted")
    axs[0,3].set_title("Cau 6d")
    axs[0,3].legend(fontsize='small')
    axs[0,3].grid()


def f6_e_o(x):
    return np.power(np.abs(x), 2/3)


def f6_e_s(x):
    return np.power(np.abs(x-1), 2/3)-1


def cau6e(axs):
    x = np.arange(-10,10.1,0.1) 
    axs[0,4].plot(x, (list(map(f6_e_o,x))), label = "Original")
    axs[0,4].plot(x, (list(map(f6_e_s,x))), label = "Shifted")
    axs[0,4].set_title("Cau 6e")
    axs[0,4].legend(fontsize='small')
    axs[0,4].grid()
    
def f6_f(x):
    return (1/2)*(x+1)+5

def cau6f(axs):
    x=np.arange(-10,11,0.1)
    y_original=[]
    for xi in x:
        y_original.append(f6_f(xi))
    y=np.array(y_original)
    axs[1,0].plot(x,y,label="Original")
    axs[1,0].plot(x+1,y-5,label="Shifted")
    axs[1,0].set_title("Cau 6f")
    axs[1,0].legend(fontsize='small')
    axs[1,0].grid()

def f6_g_o(x):
    return 1/(x**2)

def f6_g_s(x):
    return (1/((x+2)**2))-1

def cau6g(axs):
    x=np.linspace(-10,10,50)
    axs[1,1].plot(x,list(map(f6_g_o,x)),label="Original")
    axs[1,1].plot(x,list(map(f6_g_s,x)),label="Shifted")
    axs[1,1].set_title("Cau 6g")
    axs[1,1].legend(fontsize='small')
    axs[1,1].grid()

def f6_h_o(x):
    return 1*x**3

def f6_h_s(x):
    return 1-(x/2)**3

def cau6h(axs):
    x=np.linspace(-10,10,50)
    axs[1,2].plot(x,list(map(f6_h_o,x)),label="Original")
    axs[1,2].plot(x,list(map(f6_h_s,x)),label="Shifted")
    axs[1,2].set_title("Cau 6h")
    axs[1,2].legend(fontsize='small')
    axs[1,2].grid()

def f6_i_o(x):
    return math.sqrt(x+1)

def f6_i_s(x):
    return math.sqrt(4*x+1)

def cau6i(axs):
    x=np.linspace(0,10,50)
    axs[1,3].plot(x,list(map(f6_i_o,x)),label="Original")
    axs[1,3].plot(x,list(map(f6_i_s,x)),label="Shifted")
    axs[1,3].set_title("Cau 6i")
    axs[1,3].legend(fontsize='small')
    axs[1,3].grid()

def f6_j_o(x):
    return math.sqrt(x+1)

def f6_j_s(x):
    return 3*math.sqrt(x+1)

def cau6j(axs):
    x=np.linspace(0,10,50)
    axs[1,4].plot(x,list(map(f6_j_o,x)),label="Original")
    axs[1,4].plot(x,list(map(f6_j_s,x)),label="Shifted")
    axs[1,4].set_title("Cau 6j")
    axs[1,4].legend(fontsize='small')
    axs[1,4].grid()



cau6a(axs)
cau6b(axs)
cau6c(axs)
cau6d(axs)
cau6e(axs)
cau6f(axs)
cau6g(axs)
cau6h(axs)
cau6i(axs)
cau6j(axs)
plt.tight_layout()
plt.show()