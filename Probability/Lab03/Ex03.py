import itertools as it 
from fractions import Fraction
def P(event,space):
    return Fraction(len([value for value in event if value in space]),len(space))

heart='♡'
diamond='⟡'
spade='♤'
club='♧'
rank=['1','2','3','4','5','6','7','8','9','10','J','Q','K']
suite=[heart,diamond,spade,club]
#a
deck=[list(a+b) for a in rank for b in suite]
print("a)",len(deck))

#b
B=list(it.combinations(deck,3))
print("b)",len(B))

#c
A1=[s for s in B if sum('K' in card for card in s)>0 and sum('K' in card for card in s)<3]
print("c)",len(A1))

#d
A2=[s for s in B if sum('K' in card for card in s)>0]
print("d)",len(A2))

#e
print(Fraction(4800,52))
print("e) P(A1)=",P(A1,B),", P(A2)=",P(A2,B))