import math

def fibonacci_b(i):
	# Golden ratio
	phi = 1.618034
	# Calculate the ith Fibonacci number using formula B
	fibonacci_number = (phi**i - (1 - phi)**i) / math.sqrt(5)
	return round(fibonacci_number)

# Example usage
i = int(input("Enter the position of the Fibonacci number (i): "))
print(f"The {i}th Fibonacci number is: {fibonacci_b(i)}")