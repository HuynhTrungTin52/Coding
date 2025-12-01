import math
import random as rand

numOfExperiment=10000
# rand.seed(1) 
#For tests
x=[]
for i in range(numOfExperiment):
    die1=rand.randint(1,6)
    die2=rand.randint(1,6)
    #a)
    x.append(die1+die2)
#b)
X=range(2,13)

#c) Probability Mass Function
Occur={res:x.count(res) for res in X}
# print(Occur)
P=[round(Occur[i]/len(x),2) for i in range(2,13)]
print("c)")
for i in X:
    print(f"P(X={i})={P[i-2]}")

#d) 
EX=0
Var=0
for i in range(len(X)):
    EX+=X[i]*P[i]
print("d)")
print("Expected value:",round(EX,2))
for i in range(len(X)):
	Var+=(X[i]-EX)*(X[i]-EX)*P[i]
print("Variance:",round(Var,2))
print("Standard deviation:",round(math.sqrt(Var),2))