from sympy import isprime
from math import gcd,lcm
#1
def nextPrime(n):
    while(True):
        n+=1
        if(isprime(n)):
            return n
        
print(nextPrime(8))

#2
def primeFact(n):
    arr=[]
    i=1
    while(n!=1):
        i+=1
        while(n%i==0):
            arr.append(i)
            n/=i
    return arr

print(primeFact(61))


#3
def printPrimeTil(n):
    for i in range(2,n):
        if(isprime(i)):
            print(i,end=" ")

printPrimeTil(11)

#4
a=1000
b=20
print(gcd(a,b))
#If this is not allowed
def myGCD(a,b):
    i=1
    max=i
    while(i<a or i<b):
            if a % i == 0 and b % i ==0:
                max=i
            i+=1
    return max
print(myGCD(a,b))

#5
a=19
b=21
print(lcm(a,b))
#if this is not allowed
def myLCM(a,b):
    return int(abs(a*b)/gcd(a,b))
print(myLCM(a,b))

#6
print(bin(111)[2:])

#7
def frac10to2(a):
    precision=10
    res = "0."
    frac = a

    for _ in range(precision):
        temp = frac * 2
        integer_part = int(temp)
        frac = temp - integer_part
        
        res += str(integer_part)
        if frac == 0:
            break
            
    return res

print(frac10to2(0.35))

#8
print(hex(12)[2:])

#9
def convertbase(a, base1, base2):
    dec = 0
    for digit in a:
        dec = dec * base1 + digit
    if dec == 0:
        return [0]
    res = []
    while dec > 0:
        res.append(dec % base2)
        dec //= base2
    return res[::-1]

print(convertbase([1,1,1],2,3))