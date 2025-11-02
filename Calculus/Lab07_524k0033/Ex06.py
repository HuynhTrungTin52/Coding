import sympy as sp
#a
n = sp.symbols('n')
a_n = 1 - 0.2**n  
#b
b_n = n**3 / (n**3 + 1)
print("b) Limit of the sequence b_n = ", sp.limit_seq(b_n, n))

#c
c_n = (3 + 5*n**2) / (n + n**2)
print("c) Limit of the sequence c_n = ", sp.limit_seq(c_n, n))

#d
d_n = n**3 / (n + 1)
print("d) Limit of the sequence d_n = ", sp.limit_seq(d_n, n))

#e
e_n = sp.exp(1/n)
print("e) Limit of the sequence e_n = ", sp.limit_seq(e_n, n))

#f
f_n = sp.sqrt((n + 1) / (9*n + 1))
print("f) Limit of the sequence f_n = ", sp.limit_seq(f_n, n))

#g
g_n = (-1)**(n+1) * n / (n + sp.sqrt(n))
print("g) Limit of the sequence g_n = ", sp.limit_seq(g_n, n))

#h
h_n = sp.tan(2*n*sp.pi / (1 + 8*n))
print("h) Limit of the sequence h_n = ", sp.limit_seq(h_n, n))

#i
i_n = sp.factorial(2*n - 1) / sp.factorial(2*n + 1)
print("i) Limit of the sequence i_n = ", sp.limit_seq(i_n, n))

#j
j_n = sp.ln(2*n**2 + 1) - sp.ln(n**2 + 1)
print("j) Limit of the sequence j_n = ", sp.limit_seq(j_n, n))
