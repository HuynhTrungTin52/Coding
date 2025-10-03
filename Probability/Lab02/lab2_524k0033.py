import random as rand
import itertools
from fractions import Fraction
numOfExperiment=10000

def simulaltor_dice1(n):
    count =0
    for i in range(n):
        die1=rand.randint(1,6)
        die2=rand.randint(1,6)
        if die1%2==0 and die2%2==0:
            count+=1
    return count

def simulaltor_dice2(n):
    count =0
    for i in range(n):
        die1=rand.randint(1,6)
        die2=rand.randint(1,6)
        if die1%2==0 and die2%2==1:
            count+=1
    return count

def simulaltor_dice3(n):
    count =0
    for i in range(n):
        die1=rand.randint(1,6)
        die2=rand.randint(1,6)
        if die1==die2:
            count+=1
    return count


def simulaltor_dice4(n):
    count =0
    for i in range(n):
        die1=rand.randint(1,6)
        die2=rand.randint(1,6)
        if die1==1 and die2==6:
            count+=1
    return count

def simulaltor_dice5(n):
    count =0
    for i in range(n):
        die1=rand.randint(1,6)
        die2=rand.randint(1,6)
        if die1 + die2>6:
            count+=1
    return count



print("a)",simulaltor_dice1(numOfExperiment)/numOfExperiment)
print("b)",simulaltor_dice2(numOfExperiment)/numOfExperiment)
print("c)",simulaltor_dice3(numOfExperiment)/numOfExperiment)
print("d)",simulaltor_dice4(numOfExperiment)/numOfExperiment)
print("e)",simulaltor_dice5(numOfExperiment)/numOfExperiment)



Ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
Suits = {'♡', '♢', '♣', '♠'}
Cards = list(itertools.product(Ranks , Suits))
def simulator_poker1(n):
	count = 0
	
	for i in range(n):
		allRed=True
		for j in rand.sample(range(0,52),5):
			if Cards[j][1] != '♡':
				allRed=False
		
		if allRed:
			count+=1
	return count


def simulator_poker2(n):
	count = 0
	
	for i in range(n):
		suitSeen=[]
		AllDiff=True
		for j in rand.sample(range(0,52),4):
			if Cards[j][1] in suitSeen:
				AllDiff=False
				break
			else:
				suitSeen.append(Cards[j][1])
		if AllDiff:
			count+=1
			
	return count

print("f)",simulator_poker1(numOfExperiment)/numOfExperiment)
print("g)",simulator_poker2(numOfExperiment)/numOfExperiment)


def combos(items , n):
	return {' '.join(combo) for combo in itertools.combinations(items , n)}

def cross(A,B):
    return {a+b for a in A for b in B}

urn = cross('W', '12345678') | cross('B', '123456') | cross('R', '123456789')
U6 = combos(urn, 6)

def P(event , space):
	'''The probability of an event , given a sample space of equiprobable outcomes.'''
	return Fraction(len(event & space), len(space))

b2w2r2 = {s for s in U6 if s.count('B') == 2 and s.count('W') == 2 and s.count('R') == 2}

print("h)",P(b2w2r2 , U6),"(",len(b2w2r2)/len(U6),")")