import sympy as sp

x = sp.symbols('x')
print("a)")
f_a = x**2 - 7

c_a = 1

# 1. Is f(c) defined?
f_c_a = f_a.subs(x, c_a)
print(f"Condition 1: f({c_a}) = {f_c_a}")

# 2. Does the limit of f(x) as x -> c exist?
limit_a = sp.limit(f_a, x, c_a)
print(f"Condition 2: The limit of f(x) as x approaches {c_a} is {limit_a}")

# 3. Does lim f(x) == f(c)?
is_continuous_a = (limit_a == f_c_a)
print(f"Condition 3: Does lim f(x) == f(c)? {is_continuous_a}")

if is_continuous_a:
    print(f"\nConclusion for (a): The function f(x) is continuous at c={c_a}.")
else:
    print(f"\nConclusion for (a): The function f(x) is not continuous at c={c_a}.")
    
    
print()
print("b)")
f_b = sp.sqrt(2*x - 3)

c_b = 2


# 1. Is f(c) defined?
f_c_b = f_b.subs(x, c_b)
print(f"Condition 1: f({c_b}) = {f_c_b}")

# 2. Does the limit of f(x) as x -> c exist?
limit_b = sp.limit(f_b, x, c_b)
print(f"Condition 2: The limit of f(x) as x approaches {c_b} is {limit_b}")

# 3. Does lim f(x) == f(c)?
is_continuous_b = (limit_b == f_c_b)
print(f"Condition 3: Does lim f(x) == f(c)? {is_continuous_b}")

if is_continuous_b:
    print(f"\nConclusion for (b): The function f(x) is continuous at c={c_b}.")
else:
    print(f"\nConclusion for (b): The function f(x) is not continuous at c={c_b}.")