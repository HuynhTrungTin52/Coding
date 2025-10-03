import numpy as np

def large_index(split_array):
    indexAt=0
    for i in range(len(split_array)):
        sum_vec=0
        sum_vec=sum(split_array[i])
        try:
            if(sum_vec>max_vec):
                max_vec=sum_vec
                indexAt=i
        except NameError as e :
            max_vec=sum_vec
            indexAt=i
    return indexAt

m=int(input("Enter m :"))
if(m<=0):
    print("Error, cannot split an array by",m)
    exit(1)
arr = []

length = int(input("Enter the number of elements: "))
for i in range(length):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

print("Array:", arr)
print("M:",m)

splittedArr=np.array_split(arr,m)
print("Arrays are split into :")
for i in splittedArr:
    print(i,end=" ")
print()
indexx=large_index(splittedArr)
print()
print("The array split up with the largest sum :")
print(splittedArr[indexx],"sum = ",sum(splittedArr[indexx]))