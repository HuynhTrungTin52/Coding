import itertools as it
from fractions import Fraction as f
def cross(A,B):
    return {a+b for a in A for b in B}

urn=list(cross('W','12345') | cross('B','12') | cross('R','123'))
u3=list(it.combinations(urn,3))
sample_space_size=len(u3)
#a
same_color_combinations = [combo for combo in u3 if len(set([ball[0] for ball in combo])) == 1]
print("a)Picking 3 balls of the same colour :",f(len(same_color_combinations),sample_space_size))

#b
print("b)Picking 3 balls of different colour :",1-f(len(same_color_combinations),sample_space_size))

#c
sameish_color_combinations = [combo for combo in u3 if len(set([ball[0] for ball in combo])) == 2]
print("c)Only 2 balls are the same colour :",f(len(sameish_color_combinations),sample_space_size))

#d
twoRedoneWhite=[combo for combo in u3 if sum(1 for i in combo if i.startswith('W'))==1 and sum(1 for i in combo if i.startswith('R'))==2]
print("d) 2 red balls, 1 white ball :",f(len(twoRedoneWhite),sample_space_size))

#e
threeWhiteBalls=[combo for combo in u3 if sum(1 for i in combo if i.startswith('W'))==3]
print("e) 3 white balls :",f(len(threeWhiteBalls),sample_space_size))