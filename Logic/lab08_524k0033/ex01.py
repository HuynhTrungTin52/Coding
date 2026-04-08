
def thieves(x):
    return x+thievesHelper(1,x)

def thievesHelper(i,x):
    if i>=x-1:
        return i
    return i+thievesHelper(i+1,x)

i=0
# print(-499460>=0)
remainingThieves=40
while(True):
    i+=1
    remainingThieves-=thieves(i)
    if(remainingThieves>=0):
        print(f"On day {i}, Alibaba sent {thieves(i)} thieves")
        
    else:
        print(f"And on day {i}, Alibaba had ran out of thieves")
        break
    