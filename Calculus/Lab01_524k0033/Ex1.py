import math

#a
def f1_sqrt(x):
    return math.sqrt(x)

#b
def f2_3sqrt(x):
    return x**(1/3)

#c
def f3_xto2on3(x):
    return x**(2/3)

#d
def f4_eqa1(x):
    return (x**3)/3-(x**2)/2-2*x+1/3

#e
def f5_eqa2(x):
    return (2*(x**2)-3)/(7*x+4)

#f
def f6_eqa3(x):
    return (5*(x**2)+8*x-3)/(3*(x**2)+2)

#g
def f7_sin(x):
    return math.sin(x)

#h
def f8_cos(x):
    return math.cos(x)

#i
def f9_3to(x):
    return 3**x

#j
def f10_10tonminus(x):
    return 10**(-x)

#k
def f11_eto(x):
    return math.e**x

#l
def f12_log2(x):
    return math.log2(x)

#m
def f13_log10(x):
    return math.log10(x)

#n
def f14_ln(x):
    return math.log(x)
#main
print(f1_sqrt(4))
print(f2_3sqrt(27))
print(f3_xto2on3(5))
print(f4_eqa1(10))
print(f5_eqa2(10))
print(f6_eqa3(18))
print(f7_sin(20))
print(f8_cos(math.pi))
print(f9_3to(3))
print(f10_10tonminus(5))
print(f11_eto(2))
print(f12_log2(16))
print(f13_log10(100))
print(f14_ln(50))