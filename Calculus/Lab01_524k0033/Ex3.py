f1 = lambda x: x+5
f2 = lambda x:x**2-3

print("a. f1(f2(0)) :",f1(f2(0)))
print("b. f2(f1(0)) :",f2(f1(0)))
print("c. f1(f1(-5)) :",f1(f1(-5)))
print("d. f2(f2(2)) :",f2(f2(2)))