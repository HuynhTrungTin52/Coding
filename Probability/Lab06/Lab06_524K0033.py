import math
import matplotlib.pyplot as plt

#1
print("1)")
def pmf_binom(k,n,p):
    num_comb=math.comb(n,k)
    return round(num_comb*p**k*(1-p)**(n-k),5)

def plot_pmf_binom(n,p):
    K=list(range(0,n+1))
    P_binom = [pmf_binom(k,n,p) for k in K]
    # print(P_binom)
    plt.plot(K,P_binom,'-o')
    axes = plt.gca()
    axes.set_xlim([0,n])
    axes.set_ylim([0,1.1*max(P_binom)])
    plt.title('PMF of Bin(%i, %.2f)' % (n,p))
    plt.xlabel("Number of k of sucesses")
    plt.ylabel('Probability of k sucesses')
    plt.show()

p=0.1 #Probability of a machine broken
n=5 # Number of machines
k= 2 # Two machines are broken in one session

print("a) Odds of 2 machines are broken in one session",pmf_binom(k,n,p))
# plot_pmf_binom(n,p)

X=[0,1,2,3,4,5]
P_binom = [pmf_binom(x, n, p) for x in X]
plt.bar(X, P_binom)
plt.title('Probability Distribution of X')
plt.xlabel('Number of broken machines (X)')
plt.ylabel('Probability')
plt.show()

#2)
print("2)")
def pmf_poisson(k,lam):
    return round(((lam**k)*math.e**(-lam))/math.factorial(k),5)

lam=3
k=2
print("a)2 calls in 1 minute :",pmf_poisson(k,lam))

X=[1,2,3,4,5]
P_poisson = [pmf_poisson(x,lam) for x in X]
plt.bar(X, P_poisson)
plt.title('Probability Distribution of X')
plt.xlabel('Number of calls in a minute (X)')
plt.ylabel('Probability')
plt.show()

#3)
def pmf_geo(p,x):
    return p*(1-p)**(x-1) 

p=0.4
print("a)Third time the charm:",pmf_geo(p,3))
X=[i for i in range(1,11)]
P_geo = [pmf_geo(p,x) for x in X]
plt.bar(X, P_geo)
plt.title('Probability Distribution of X')
plt.xlabel('Chances the shot hit x try(X)')
plt.ylabel('Probability')
plt.show()