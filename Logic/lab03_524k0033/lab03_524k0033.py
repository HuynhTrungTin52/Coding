def allPositive(lis):
    return all(x>0 for x in lis)

def atLeastOneEven(lis):
    return any(x%2==0 for x in lis)

def notAllEven(lis):
    return any(x%2!=0 for x in lis)

def isPrime(n): return not any(n % i == 0 for i in range(2,n))

def predPrime(lis):
    return all(isPrime(x) for x in lis)

def eachListOneEven(lists):
    return all(any(x % 2 == 0 for x in lst) for lst in lists)

def oneNumberGreater(lis):
    return all(any(y>x for y in lis) for x in lis )

def XplusYdivisibleby5andYisgreaterthanX(lis):
    return all(any(((x+y)%5==0) and (y>x) for y in lis) for x in lis )

def uniqueOutput(lis):
    return not(any(any(y[0]==tup[0] for y in lis if y!=tup) for tup in lis))





lis=[(3,2),(2,3),(1,5),(4,6),(-10,10)]
print(uniqueOutput(lis))

# for i in tuplestuff(lis):
# 	for x in i:
# 		print(x,end=",")
# 	print()


# for tup in lis:
#     print(tup[0],end=",")
#     for y in lis:
#         # print("Checking if ",tup," is equal to ",y)
#         if(y==tup):
#             # print("SKIP")
#             continue
#         print(y[0])