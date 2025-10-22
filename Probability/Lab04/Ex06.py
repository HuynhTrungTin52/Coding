import numpy as np

x = np.random.choice([0, 1, 2, 3, 4, 5], 3650, p=[0.1, 0.2, 0.3, 0.2, 0.15, 0.05])

# (a)
X = np.unique(x)
print(f"a) The values of the random variable X are: {X}")

# (b) 
counts = np.bincount(x, minlength=len(X))
P = (counts / len(x)).tolist()
print(f"b) The probability distribution P is: {P}")

# (c) 
expectation = np.mean(x)
variance = np.var(x)
std_deviation = np.std(x)

print(f"c) Expectation (Mean): {expectation:.4f}")
print(f"   Variance: {variance:.4f}")
print(f"   Standard Deviation: {std_deviation:.4f}")

# (d) 

prob_3_or_more_alt = sum(P[3:])
print(f"   (Calculated from P): {prob_3_or_more_alt:.4f}")