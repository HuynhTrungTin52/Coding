import itertools as it
import random
from fractions import Fraction as f
numOfExperiment=10000

heart='♡'
diamond='⟡'
spade='♤'
club='♧'
rank=['1','2','3','4','5','6','7','8','9','10','J','Q','K']
suite=[heart,diamond,spade,club]
deck=[[a,b] for a in rank for b in suite]
# print(deck)

#a
suma=0
for i in range(numOfExperiment):
    drawn_cards=random.sample(deck, 4)
    first_suit = drawn_cards[0][1]
    if all(card[1] == first_suit for card in drawn_cards):
        suma += 1

print("a) Four suites:",f(suma,numOfExperiment))


#b
sumb=0
for i in range(numOfExperiment):
    drawn_cards=random.sample(deck, 4)
    drawn_suits=[card[1] for card in drawn_cards]
    # print(drawn_cards)
    if len(set(drawn_suits))==4:
        # print(drawn_cards)
        sumb += 1

print("b) Different suites:",f(sumb,numOfExperiment))

#c
sumc=0
for i in range(numOfExperiment):
    drawn_cards=random.sample(deck, 4)
    drawn_color=["red" if card[1]==heart or card[1]==diamond else "black" for card in drawn_cards]
    # print(drawn_cards,"        ",drawn_color)
    if len(set(drawn_color))==1:
        # print(drawn_cards)
        sumc += 1

print("c) Same colour:",f(sumc,numOfExperiment))

#d
sumd=0
for i in range(numOfExperiment):
    drawn_cards=random.sample(deck, 4)
    first_rank = drawn_cards[0][0]
    if all(card[0] == first_rank for card in drawn_cards):
        # print(drawn_cards)
        sumd += 1

print("d) Four ranks :",f(sumd,numOfExperiment))

#e and f
sume=0
sumf=0
for i in range(numOfExperiment):
    drawn_cards=random.sample(deck, 4)
    face_card=['J','Q','K']
    drawn_type=["face" if card[0] in face_card else "number" for card in drawn_cards]
    # print(drawn_cards,"        ",drawn_type)
    
    if len(set(drawn_type))==1:
        if(drawn_type[0]=="number"):
            sume += 1
        else:
            sumf+=1
print("e) Four numbers",f(sume,numOfExperiment))
print("f) Four face",f(sumf,numOfExperiment))