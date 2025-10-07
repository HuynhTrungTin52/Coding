from fractions import Fraction
def P(event,space):
    return Fraction(len([value for value in event if value in space]),len(space))

S = [('Thanh', 'Nữ'), ('Hồng', 'Nữ'), ('Thương', 'Nữ'), ('Đào', 'Nữ'), ('My', 'Nữ'), ('Yến', 'Nữ'), ('Hạnh', 'Nữ'),('My', 'Nữ'), ('Vy', 'Nữ'), ('Tiên', 'Nữ'), ('Thanh', 'Nam'), ('Thanh', 'Nam'), ('Bình', 'Nam'), ('Nhật', 'Nam'), ('Hào', 'Nam'), ('Đạt', 'Nam'), ('Minh', 'Nam')]

A=[t for t in S if t[0]=='Thanh']
print("a)",A)
B=[f for f in S if f[1]=='Nữ']
print("b)",B)
A_B = list(set(A) & set(B))
print("C)",A_B)
P_A=P(A,S)
P_B=P(B,S)
P_A_B=P(A_B,S)
print("c) P_A=",P_A,", P_B=",P_B,", P_A_B=",P_A_B)
#Thanh, given we know this is a female
P_AgivenB=P_A_B/P_B
print("d)",P_AgivenB)