import sympy as sp
import math
#3.1
print("3.1)")
x = sp.symbols('x')
f3_1 = 1/( 1 + 2**(1/x) )
lmRight = sp.limit(f3_1, x, 0, '+')
print ("Right limit = " , lmRight )
lmLeft = sp.limit(f3_1, x, 0, '-')
print ("Left limit = " , lmLeft )

print()

#3.2
f3_2 = (x**2+x)/(sp.sqrt(x**3+x**2))
lmRight = sp.limit(f3_2, x, 0, '+')
print ("Right limit = " , lmRight )
lmLeft = sp.limit(f3_2, x, 0, '-')
print ("Left limit = " , lmLeft )