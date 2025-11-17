import numpy as np
import random

# Example: your Student ID 523H0154 => get code: 0154
a = 0 # two first digits in our code   => 01
b = 31 # two last digits in our code   => 54
population_data = list(np.random.normal(a, b, 10000))
n = 50 

pop_var_actual = np.var(population_data)
pop_var_theoretical = b**2
print(f"Actual population variance: {pop_var_actual:.4f}")

sample = np.random.choice(population_data, n, replace=False)
s2 = np.var(sample, ddof=1)
print(f"Sample variance (n-1): {s2:.4f}")

runs = 10000
var_n_list = []       
var_n1_list = []      

for _ in range(runs):
    smp = np.random.choice(population_data, n, replace=False)
    var_n_list.append(np.var(smp, ddof=0))   
    var_n1_list.append(np.var(smp, ddof=1))  

mean_var_n  = np.mean(var_n_list)
mean_var_n1 = np.mean(var_n1_list)

print(f"True theoretical variance: {pop_var_theoretical}")
print(f"Mean biased estimate   (divide by n=50):  {mean_var_n:.4f}")
print(f"Mean unbiased estimate (divide by n-1=49): {mean_var_n1:.4f}")