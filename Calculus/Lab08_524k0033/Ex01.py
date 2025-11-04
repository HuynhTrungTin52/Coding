f_1a = lambda x, y: x*x + x*y**3
print("f_1a(x, y) = x*x + x*y**3")
cases = [(0, 0), (-1, 1), (2, 3), (-3, -2)]
for x, y in cases:
	print(f"f_1a({x}, {y}) = {f_1a(x, y)}")
f_1b = lambda x, y,z: (x-y)/(y**2 + z**2)
print("f_1b(x, y, z) = (x-y)/(y**2 + z**2)")
cases = [(3, -1, 2), (1, 1/2, 1/4), (0, -1/3, 0), (2, 2, 100)]
for x, y, z in cases:
	print(f"f_1b({x}, {y}, {z}) = {f_1b(x, y, z)}")