import numpy as np
arr = []

length = int(input("Enter the number of elements: "))
for i in range(length):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

print("Array:", arr)

output=[]
for i in range(length-1):
    equalZero=[]
    for j in range(i+1,length):
        if arr[i]+arr[j]==0:
            if np.isin(arr[i],output) or np.isin(arr[j],output):
                
                continue
            else:
                equalZero.append(arr[i])
                equalZero.append(arr[j])
                
  				
    if equalZero:
        output.append(equalZero)

print("Output :")
print(output)