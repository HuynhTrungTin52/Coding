import itertools as it
# your code
def cross(A, n):
    return {a+str(b+1) for a in A for b in range(n)}

urn = cross('W', 8) | cross('B', 6) | cross('R', 9)

def get_x(n):
    return int(( n / 99 ) * 4 + 6)

x = get_x(33)

U = list(it.combinations(urn,x))
for hand in U:
    if hand[0][0]=='R':
        print(hand)