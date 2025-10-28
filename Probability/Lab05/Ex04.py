import itertools as it
from fractions import Fraction as f
def cross(A,B):
    return [[a+b] for a in A for b in B]

#a
urn=cross('W','12345')+ cross('B','12')+cross('R','123')

#b
u3=list(it.permutations(urn,3))
# print(u3)

#c
white1blue1red1=[combo for combo in u3 if len(set([ball[0][0] for ball in combo])) == 3]
# print(white1blue1red1)

#d
P = f(len(white1blue1red1), len(u3))
print(P)