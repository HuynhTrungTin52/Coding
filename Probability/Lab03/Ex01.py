import itertools as it 
from fractions import Fraction

def P(event,space):
    return Fraction(len(event & space),len(space))
# 3 cats
Gender=['M','F']
S=set([p for p in it.product(Gender,repeat=3)])
print("a)",S)
print("b)",len(S))
#At least one female cat
B={s for s in S if 'F' in s}
print("c)",B)
#All three female cats
A={s for s in S if s.count('F')==3}
print("d)",A)
#First female, others female 
A_B={s for s in S if s in A and s in B}
P_A_Given_B=P(A_B,S)/P(B,S)
print("e)",P_A_Given_B)