def waytochooseP(n,k):
    if k==0 or k==n:
        return 1
    
    return n*waytochooseP(n-1,k-1)

i=0
n=50

def calculateOff(a,b):
    return (abs(a-b)/((a+b)/2))*100

# print("Demo:",waytochooseP(50,3))
lastPercentageOff=calculateOff(waytochooseP(n,1),10000)
# print(lastPercentageOff)
while(i<=n):
    i+=1
    if(lastPercentageOff>calculateOff(waytochooseP(n,i),10000)):
        print(f"Sinbad must pick {i} members to find the closest combinations to 10000({waytochooseP(n,i)})")
        lastPercentageOff=calculateOff(waytochooseP(n,i),10000)
        break