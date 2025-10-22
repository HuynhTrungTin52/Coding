import random
import math
#1)
x=[random.randint(1,6) for i in range (10000)]
X=set(x)
# print(x)
# print(X)

#2)
Occur={
	1 : x.count(1),
	2 : x.count(2),
	3 : x.count(3),
	4 : x.count(4),
	5 : x.count(5),
	6 : x.count(6),
}

print(Occur)

#3)
P=[round(Occur[i+1]/len(x)*100,2) for i in range(6)]
print(P)