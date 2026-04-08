def waytochoose(n,k):
    if k==0 or n==k:
        return 1
    return waytochoose(n-1,k)+waytochoose(n-1,k-1)

i=0
n=50

def calculateOff(a,b):
    return (abs(a-b)/((a+b)/2))*100

# print("Demo:",waytochoose(5,1))
lastPercentageOff=calculateOff(waytochoose(n,1),1000)
print(lastPercentageOff)
while(i<=n):
    i+=1
    if(lastPercentageOff>calculateOff(waytochoose(n,i),1000)):
        print(f"Sinbad must pick {i} members to find the closest combinations to 1000({waytochoose(n,i)})")
        lastPercentageOff=calculateOff(waytochoose(n,i),1000)
        break
    # else:
    #     print(waytochoose(50,i))