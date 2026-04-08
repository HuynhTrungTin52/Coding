def richest(x):
    if len(x)==1:
        return x[0]
    
    return max(x[len(x)-1],richest(x[:-1]))


people=[1000000,5000,27800,798126]
print(richest(people))