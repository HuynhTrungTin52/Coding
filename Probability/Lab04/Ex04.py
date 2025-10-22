# 1. 
values = [1, 2, 3]
probabilities = [0.2, 0.5, 0.3]

expectation = 0

# 2. Calculate the expectation E(X)
for i in range(len(values)):
	expectation += values[i] * probabilities[i]

# 3. Print the result
print(f"The expectation E(X) is: {expectation}")