import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

Ntrials = 1000
prob = 0.01
K = 1000
lam_val = Ntrials * prob

np.random.seed(42)
data_binom = np.random.binomial(Ntrials, prob, size=K)
data_poiss = np.random.poisson(lam_val, size=K)

all_k = np.sort(np.unique(np.concatenate((data_binom, data_poiss))))

counts_binom = Counter(data_binom)
density_binom = np.array([counts_binom.get(k, 0) for k in all_k]) / K

counts_poiss = Counter(data_poiss)
density_poiss = np.array([counts_poiss.get(k, 0) for k in all_k]) / K

plt.figure(figsize=(11, 6))
width = 0.35
x = all_k

plt.bar(x - width/2, density_binom, width, alpha=0.7, 
        label=f"Binomial: n={Ntrials}, p={prob}")

plt.bar(x + width/2, density_poiss, width, alpha=0.7, 
        label=f"Poisson: $\\lambda$={lam_val}")

plt.title("Comparison of Sampled Binomial and Poisson Distributions (Bar Chart/PMF)")
plt.xlabel("k (Number of Successes)")
plt.ylabel("Sample Density / Estimated PMF")
plt.xticks(x)
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

print("-" * 50)
print(f"n={Ntrials}, p={prob}, lambda={lam_val}")
print(f"Binomial mean: {np.mean(data_binom):.4f}, theory={Ntrials*prob}")
print(f"Poisson mean: {np.mean(data_poiss):.4f}, theory={lam_val}")
print(f"Binomial variance: {np.var(data_binom):.4f}, theory={Ntrials*prob*(1-prob):.4f}")
print(f"Poisson variance: {np.var(data_poiss):.4f}, theory={lam_val}")
print("-" * 50)