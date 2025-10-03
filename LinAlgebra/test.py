#j) 1/2 1/5 1/10 1/17
#Rule : Fraction with the denominator + odd numbers(Incremental)


import numpy as np
import fractions as frac
n=int(input("Enter the range of elements as n :"))
startNum=2
res=[1/startNum]
incrementOdd=3
print(frac.Fraction((res[0])).limit_denominator(startNum),end="  ")
for i in range(1,n,1):
  startNum+=incrementOdd
  res.append(1/startNum)
  incrementOdd+=2
  print(frac.Fraction((res[i])).limit_denominator(startNum),end="  ")