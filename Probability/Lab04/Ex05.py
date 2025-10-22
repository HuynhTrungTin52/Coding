# 1. 
values = [1, 2, 3]
probabilities = [0.2, 0.5, 0.3]

expectation = 0

# 2. Calculate the expectation E(X)
for i in range(len(values)):
	expectation += values[i] * probabilities[i]

# 3. Print the result
print(f"The expectation E(X) is: {expectation}")

# 2.
expectation_x_squared = 0
for i in range(len(values)):
	expectation_x_squared += (values[i]**2) * probabilities[i]

variance = expectation_x_squared - (expectation**2)

# 3.
print(f"The variance Var(X) is: {variance}")