import sympy as sp
import matplotlib.pyplot as plt

n = sp.symbols('n', integer=True)

seq_a = 1 - (0.2)**n
seq_b = 2 * n / (n**2 + 1)
seq_c = ((-1)**(n-1)) / (5**n)
seq_d = 1 / sp.factorial(n + 1)

seq_e = [1]  
for i in range(1, 5):
	seq_e.append(5 * seq_e[-1] - 3)

seq_f = [2] 
for i in range(1, 5):
	seq_f.append(seq_f[-1] / (seq_f[-1] + 1))

n_values = range(1, 6)
a_values = [seq_a.subs(n, i).evalf() for i in n_values]
e_values = seq_e
f_values = seq_f
d_values = [seq_d.subs(n, i).evalf() for i in n_values]
b_values = [seq_b.subs(n, i).evalf() for i in n_values]
c_values = [seq_c.subs(n, i).evalf() for i in n_values]

print("First 5 terms of sequence a:", a_values)
print("First 5 terms of sequence b:", b_values)
print("First 5 terms of sequence c:", c_values)
print("First 5 terms of sequence d:", d_values)
print("First 5 terms of sequence e:", e_values)
print("First 5 terms of sequence f:", f_values)

plt.figure(figsize=(10, 6))
plt.plot(n_values, a_values, label="a_n = 1 - (0.2)^n")
plt.plot(n_values, b_values, label="a_n = 2n / (n^2 + 1)")
plt.plot(n_values, c_values, label="a_n = (-1)^(n-1) / 5^n")
plt.plot(n_values, d_values, label="a_n = 1 / (n+1)!")
plt.plot(n_values, e_values, label="a_1 = 1, a_(n+1) = 5a_n - 3")
plt.plot(n_values, f_values, label="a_1 = 2, a_(n+1) = a_n / (a_n + 1)")

plt.xlabel("n")
plt.ylabel("a_n")
plt.title("First 5 Terms of Sequences")
plt.legend()
plt.grid()
plt.show()