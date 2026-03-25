import math

def findGCD(r0,r1):
    if r0==0:
        return r1
    return findGCD(r1 % r0,r0)

def extendedGCD(n,a):
    n0 = n
    a0 = a
    t0 = 0
    t = 1
    q = math.floor(n0 / a0)
    r = n0 - q * a0
    while r > 0:
        temp = t0 - q * t
        if temp >= 0:
            temp = temp % n
        else:
            if temp < 0:
                temp = n - ((-temp) % n)
        t0 = t
        t = temp
        n0 = a0
        a0 = r
        q = math.floor(n0 / a0)
        r = n0 - q * a0
    if a0 != 1:
        print("a has no inverse in Z_n")
    else:
        aminus1 = t % n
        print("a has an inverse of", aminus1)
    return (a0,q)

print(extendedGCD(22,14))

def mod_inverse(a,n):
    n0 = n
    a0 = a
    t0 = 0
    t = 1
    q = math.floor(n0 / a0)
    r = n0 - q * a0
    while r > 0:
        temp = t0 - q * t
        if temp >= 0:
            temp = temp % n
        else:
            if temp < 0:
                temp = n - ((-temp) % n)
        t0 = t
        t = temp
        n0 = a0
        a0 = r
        q = math.floor(n0 / a0)
        r = n0 - q * a0
    if a0 != 1:
        return None
    else:
        aminus1 = t % n
        return aminus1

def find_mod_inverses(numbers,n):
    my_dict={}
    for num in numbers:
        my_dict[(num,n)]=mod_inverse(num,n)
    return my_dict

list=[1,2,3,4,5]

