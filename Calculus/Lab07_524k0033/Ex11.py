import sympy as sp

#Ex11: a_n = 28000*(1 + 0.03)**n
#need to find a1 a2 a3
a_n = lambda n: 28000*(1 + 0.03)**n
# Calculate the salaries for the first 3 years
salaries = [a_n(n) for n in range(1, 4)]
print(salaries)