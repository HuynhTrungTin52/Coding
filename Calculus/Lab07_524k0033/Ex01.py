#Ex1a: xn = 4n + 1
x_n = lambda n: 4*n + 1
n_values = range(11) #n from 0 to 10
print( list (map(x_n, n_values)) )
# Ex1b: xn = 3^n
x_n_geometric = lambda n: 3**n
print(list(map(x_n_geometric, n_values)))

# Ex1c: xn = n^3
x_n_cubic = lambda n: n**3
print(list(map(x_n_cubic, n_values)))

def fibonacci_sequence(n):
	sequence = [0, 1]
	for i in range(2, n):
		sequence.append(sequence[-1] + sequence[-2])
	return sequence[:n]

print(fibonacci_sequence(11))