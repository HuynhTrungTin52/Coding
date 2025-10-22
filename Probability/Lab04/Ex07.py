import random
import numpy as np
from collections import Counter

num_experiments = 10000
num_coins = 2

# a) 
x = [sum(random.choices([0, 1], k=num_coins)) for _ in range(num_experiments)]

# b) 
X = sorted(list(set(x)))

# c) 
counts = Counter(x)
P = [counts[val] / num_experiments for val in X]

# d) 
expectation = np.mean(x)
variance = np.var(x)
std_deviation = np.std(x)

# e) 
prob_at_least_one_head = 1 - P[X.index(0)]

print(f"(a) Total number of experiments: {len(x)}")


print(f"(b) Values of random variable X: {X}")


print("(c) Probability Distribution Function (P):")
for val, prob in zip(X, P):
	print(f"    P(X={val}) = {prob:.4f}")


print("(d) Characteristic Parameters:")
print(f"    Expectation (Mean): {expectation:.4f}")
print(f"    Variance: {variance:.4f}")
print(f"    Standard Deviation: {std_deviation:.4f}")


print(f"(e) Probability to have at least one head: {prob_at_least_one_head:.4f}")


