import math
import matplotlib.pyplot as plt

#1
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

X={0,1,2,3,4,5}
