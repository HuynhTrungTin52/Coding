from fractions import Fraction

#Given the sequence arithmetic sequence: 5, 20, 35, 50, 65, ... find d, an, a55 and which term equals 230
# an = a1 + (n − 1)d
print("a)")
d = 20 - 5
a1 = 5
a_n = lambda n: a1 + (n-1)*d

a55 = a_n(55)
print("a55=", a55)
n=0
while True:
	if a_n(n) == 230:
		print(f"The term equal to 230 is a{n}")
		break
	else:
		n += 1
  
  
print("b)")
a1_g = Fraction(120, 1)
r = Fraction(60, 120)  
a_n_g = lambda n: a1_g * r**(n - 1)

a10 = a_n_g(10)
print("r =", r)
print("a10 =", a10)

target = Fraction(15, 32)
ratio = target / a1_g

n = None
k = 0
while k < 100:
	if r**k == ratio:
		n = k + 1
		break
	k += 1

if n is not None:
	print(f"The term equal to {target} is a{n}")
else:
	print(f"No integer term <=100 equals {target}")