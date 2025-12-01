import math

def H(t) :
	return math.sqrt(t + 1) + 5 * (t ** (1.0 / 3.0))

def average_height_a_b(a, b) :

	def F(t) :
		return (2.0 / 3.0) * (t + 1) ** 1.5 + (15.0 / 4.0) * (t ** (4.0 / 3.0))
	return (F(b) - F(a)) / (b - a)


t_values = [0, 4, 8]
heights = {t: H(t) for t in t_values}
avg_height = average_height_a_b(0.0, 8.0)
print("a)Heights:")
for t in t_values:
	print(f"t = {t}: H(t) = {heights[t]:.2f}")
print(f"\nb)Average height on [0, 8]: {avg_height:.2f}")
