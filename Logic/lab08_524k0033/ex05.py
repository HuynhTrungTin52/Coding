def total_characters(n):
    if n == 1:
        return 1
    else:
        return (2**(n-1)) + total_characters(n - 1)

res = total_characters(547)
print(res) 
