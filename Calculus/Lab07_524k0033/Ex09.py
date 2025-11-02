import sympy as sp
#Exercise 9: Determinate if the following series is convergent or divergent.
#9a: 4^n
n = sp.symbols('n')
seriesa = sp.Sum(4**n, (n, 1, sp.oo) )
converged = seriesa.is_convergent()

print("a)")
if converged:
  print("Convergent")
else:
  print("NOT Convergent")
  
seriesb=sp.Sum(5/(2**n),(n,1,sp.oo))
converged=seriesb.is_convergent()

print("b)")
if converged:
  print("Convergent")
else:
  print("NOT Convergent")
