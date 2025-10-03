import math
import numpy as np
np.set_printoptions(legacy='1.25')


#a
def fx_2a(x):
    return 2+((x**2)/((x**2)+4))

def cau2a():
    #min is the first item, max is the second item
    minmax=[fx_2a(-2),fx_2a(-2)]
    for x in np.arange(-1.9,2.1,0.1):
        if(fx_2a(x)<minmax[0]):
            minmax[0]=fx_2a(x)
        if(fx_2a(x)>minmax[1]):
            minmax[1]=fx_2a(x)
    res=[round(x,5) for x in minmax]
    return res

print("2.a:",cau2a()[0],"<= x <=",cau2a()[1])

#b
def fx_2b(x):
    return math.sqrt(5*x+10)

def cau2b():
    #min is the first item, max is the second item
    minmax=[fx_2b(0),fx_2b(0)]
    for x in np.arange(0.1,5.1,0.1):
        if(fx_2b(x)<minmax[0]):
            minmax[0]=fx_2b(x)
        if(fx_2b(x)>minmax[1]):
            minmax[1]=fx_2b(x)
    res=[round(x,5) for x in minmax]
    return res

print("2.b",cau2b()[0],"<= x <=",cau2b()[1])

#c
def fx_2c(x):
    return (2)/((x**2)-16)

def cau2c():
    #min is the first item, max is the second item
    minmax=[fx_2c(5),fx_2c(5)]
    for x in np.arange(5.1,10.1,0.1):
        if(fx_2c(x)<minmax[0]):
            minmax[0]=fx_2c(x)
        if(fx_2c(x)>minmax[1]):
            minmax[1]=fx_2c(x)
    res=[round(x,5) for x in minmax]
    return res

print("2.c:",cau2c()[0],"<= x <=",cau2c()[1])

#d
def fx_2d(x):
    return (x**4)+3*(x**2)-1

def cau2d():
    #min is the first item, max is the second item
    minmax=[fx_2d(-3),fx_2d(-3)]
    for x in np.arange(-2.9,3.1,0.1):
        if(fx_2d(x)<minmax[0]):
            minmax[0]=fx_2d(x)
        if(fx_2d(x)>minmax[1]):
            minmax[1]=fx_2d(x)
    res=[round(x,5) for x in minmax]
    return res

print("2.d:",cau2d()[0],"<= x <=",cau2d()[1])
#e
def fx_2e(x):
    if x >=0:
        return x
    else:
        return -x
    
def cau2e():
    #min is the first item, max is the second item
    minmax=[fx_2e(-3),fx_2e(-3)]
    for x in np.arange(-2.9,3.1,0.1):
        if(fx_2e(x)<minmax[0]):
            minmax[0]=fx_2e(x)
        if(fx_2e(x)>minmax[1]):
            minmax[1]=fx_2e(x)
    res=[round(x,5) for x in minmax]
    return res
        
print("2.e :",cau2e()[0],"<= x <=",cau2e()[1])