import math,random

def findGCD(r0,r1):
    if r0==0:
        return r1
    return findGCD(r1 % r0,r0)

def extendedGCD(n,a):
    n0 = n
    a0 = a
    t0 = 0 #y
    t = 1
    s0 = 1 #x
    s = 0
    q = math.floor(n0 / a0)
    r = n0 - q * a0
    while r > 0:
        s_temp = s0 - q * s
        s0 = s
        s = s_temp
        temp = t0 - q * t
        # if temp >= 0:
        #     temp = temp % n
        # else:
        #     if temp < 0:
        #         temp = n - ((-temp) % n)
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
    return (a0,s,t)

# print(extendedGCD(1024,173))

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

list=[random.randint(1, 100) for _ in range(10)]
# print(find_mod_inverses(list,10))

def coprimes_and_inverses(n):
    my_dict={}
    
    for num in [random.randint(1, 100) for _ in range(10)]:
        if(findGCD(num,n)==1):
            my_dict[(num,n)]=mod_inverse(num,n)
    return my_dict

print(coprimes_and_inverses(5))