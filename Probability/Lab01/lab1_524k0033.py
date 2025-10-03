from collections import Counter
import itertools as it
import numpy as np

#Ex1
num_code=np.arange(0,10,1)
code_length=4
permute_a=list(it.permutations(num_code.tolist(),code_length))
print("1.Given a code with 4 digits and digits ranging between 0-9, there is",len(permute_a),"different permutations if one digit may be used")

#Ex2
A={1,2,3,4,5}
num_length=3
num_3_digit=list(it.permutations(A,num_length))
print("2.Given a set ranging 1-5 and 3 possible digits can be formed without repetitions, there is",len(num_3_digit),"possbilities")

#Ex3
def cross(A,B):
    return {a+b for a in A for b in B}

urn=list(cross('W','12345678') | cross('B','123456') | cross('R','123456789'))

print("Given an urn with 8 white balls, 6 black balls, 9 red balls")
	#a
len_U3=len(list(it.combinations(urn,3)))
print("3a.There is",len_U3,"possible cases when picking 3 balls")
	#b
a=[]
for i in list(it.combinations(urn,3)):
    if i[0][0]!=i[1][0] and i[0][0]!=i[2][0] and i[1][0]!=i[2][0]:
        a.append(i)
print("3b.There is",len(a),"cases where each balls are differently colored")
	#c
a=[]
for i in list(it.permutations(urn,3)):
    if i[0][0]=='W' and i[-1][0]=='R':
        a.append(i)
print("3c.There is",len(a),"cases of the first ball being white and second being red")

#Ex4
m_shelf=cross('M','1234')
p_shelf=cross('P','123')
c_shelf=cross('C','12')
l_shelf=cross('L','1')
shelf=[m_shelf,p_shelf,c_shelf,l_shelf]
total_arrangements=len(list(it.permutations(m_shelf)))*len(list(it.permutations(p_shelf)))*len(list(it.permutations(c_shelf)))*len(list(it.permutations(l_shelf)))*len(list(it.permutations(shelf)))
print("4. There is ",total_arrangements,"cases for each books to align with its own category")

#Ex5
men_size=list(cross('M','123456'))
women_size=list(cross('W','123456789'))
total_size=men_size+women_size
committee_size=5
a=[]
for i in list(it.combinations(total_size,committee_size)):
    countW=0
    countM=0
    for j in i:
        if j[0]=='W':
            countW+=1
        else:
            countM+=1
    if(countM==3 and countW==2):
        a.append(i)
print("5. There are",len(a),"cases where the committee picks 3 men and 2 women")

#Ex6
deck=list(list(cross('H','1234567890JQK')) + list(cross('D','1234567890JQK')) + list(cross('S','1234567890JQK')) + list(cross('C','1234567890JQK')))
#Let 0=10
#a
poker_5=list(it.combinations(deck,5))
len_poker_5=len(poker_5)
print("5a.Len of poker of 5 cards :",len_poker_5)
#b
three_of_a_kind=[]
for i in poker_5:
    rank=[card[1] for card in i]
    rank_count=Counter(rank)
    if 3 in rank_count.values():
        if len(rank_count)==3:
            three_of_a_kind.append(i)
print("5b.There is",len(three_of_a_kind),"cases where you can make 3 of a kind from a deck of cards")