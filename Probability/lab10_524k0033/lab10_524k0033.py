from matplotlib.ticker import MaxNLocator
import math
import random as rand
import re
import matplotlib.pyplot as plt
import numpy as np
import itertools as it 
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




#2
print("\n2)")
x = np.linspace(-4, 4, 1000)
def pdf_norm(x,mu,sigma):
    return (1/math.sqrt(2*math.pi*sigma*sigma))*math.exp(-(((x-mu)**2)/(2*sigma*sigma)))

def cdf_norm(x,mu,sigma):
    return (1/2)*(1+math.erf((x-mu)/(sigma*math.sqrt(2))))

pdf_values=[pdf_norm(i,0,1) for i in x]
cdf_values=[cdf_norm(i,0,1) for i in x]


fig,ax=plt.subplots(1,2,figsize=(10,10))
plt.figure(1)
ax[0].set_ylabel("Probability Density")
ax[0].set_xlabel("X")
ax[0].plot(x,pdf_values)
ax[0].set_title("2a)PDF of Normal Distribution")

ax[1].set_ylabel("Cumulative Probability")
ax[1].set_xlabel("X")
ax[1].plot(x,cdf_values)
ax[1].set_title("2b)CDF of Normal Distribution")

print(f"c)P(2<X<7) :{cdf_norm(7,3,4)-cdf_norm(2,3,4):.2f}")



fig,ax=plt.subplots(1,3,figsize=(10,10))
plt.figure(2)
fig.suptitle("Exercise 3")
ax[0].set_ylabel("Toothpaste Sales")
ax[0].set_xlabel("Months")
x,y=np.loadtxt("Probability/lab10_524k0033/company-sales_data.csv", delimiter=",", unpack=True,skiprows=1,usecols=(0,3))
ax[0].plot(x,y)

ax[1].set_ylabel("Shampoo Sales")
ax[1].set_xlabel("Months")
x,y=np.loadtxt("Probability/lab10_524k0033/company-sales_data.csv", delimiter=",", unpack=True,skiprows=1,usecols=(0,5))
ax[1].plot(x,y)

ax[2].set_ylabel("Facecream Sales")
ax[2].set_xlabel("Months")
x,y=np.loadtxt("Probability/lab10_524k0033/company-sales_data.csv", delimiter=",", unpack=True,skiprows=1,usecols=(0,2))
ax[2].plot(x,y)

plt.figure(3)
plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
text="That day, I went to the store near the big park, needing to get some household items under the warm, high sun in the blue sky, observing many people and a happy dog chasing a red ball, which reminded me of the simple things that make life good. I entered the shop, grabbed a cart, and quickly found all the things on my list, including fresh milk, bread, green apples, and yellow bananas, before heading to the front where a nice woman scanned my purchases. We had a brief conversation, I paid the reasonable price with paper bills, and then I pushed my bags out toward the exit, feeling glad the trip was successful and looking forward to being back home to eat and rest, experiencing the calm and peaceful nature of everyday life."
words=re.sub(r'[^\w\s]', '', text).lower().split()
dictionary = {}
for word in words:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary.update({word: 1})
plt.xlabel("Words")
x=list(dictionary.keys())
plt.ylabel("Occurences")
y=list(dictionary.values())
mylist = [key for key, val in dictionary.items() for _ in range(val)]
plt.hist(mylist,bins=30,alpha=0.5)
plt.title("Exercise 4")
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=15))
plt.tick_params(axis='x', which='major', labelsize=5)


plt.tight_layout()
plt.show()