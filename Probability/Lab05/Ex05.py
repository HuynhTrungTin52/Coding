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

d5=list(it.combinations(deck,5))
def is_straight(hand):
    rank_map = {
        '1': 14, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13
    }
    suits = {card[1] for card in hand}
    if len(suits) == 1:
        return False
    num_ranks = {rank_map[r] for r in [card[0] for card in hand]}
    if len(num_ranks) != 5:
        return False
    if num_ranks == {14, 2, 3, 4, 5}:
        return True
    if (max(num_ranks) - min(num_ranks)) == 4:
        return True
    return False

#a
straight_theory=[hand for hand in d5 if is_straight(hand)]
print("Theoretical probability :",f(len(straight_theory),len(d5)))

#b
sum=0
for i in range(numOfExperiment):
    drawn_cards=random.sample(deck,5)
    if(is_straight(drawn_cards)):
        # print(drawn_cards)
        sum+=1
print("Pratical probability :",f(sum,numOfExperiment))