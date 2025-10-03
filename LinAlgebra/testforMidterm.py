import numpy as np
import math
def isPrime(num):
    if num <= 1:
        return False
    for i in range(2,(int(math.sqrt(num))+1)):
        if num % i == 0 :
            return False
    return True

def findMaxPrime(matrixA):
    maxR=0
    for row in range(len(matrixA)):
        counter=0
        for col in range(len(matrixA[0])):
            if (isPrime(matrixA[row][col])):
                counter+=1
        if(counter>maxR):
            maxR=counter
    return maxR

def countPrimeRow(vectorA):
    return sum(1 for num in vectorA if isPrime(num))

def countOddsInRow(vectorA):
    counter=0    
    temp=0
    for i in range(len(vectorA)):
        if (vectorA[i]%2!=0):
                temp+=1
        else:
                if(temp>counter):
                    counter=temp
                temp=0
    if(temp>counter):
            counter=temp
    return counter
print("Task 1 :")
np.random.seed(25)
print("-Matrix A:")
A=np.random.randint(1,101,size=(10,10))
print(A)
print()
print("-Matrix B:")
B=np.random.randint(1,21,size=(2,10))
print(B)
print()
print("-Matrix C:")
C=np.random.randint(1,21,size=(10,2))
print(C) 
print()
print("a)Calculate A+A^T+CB+(B^T)*(C^T)")
print("The result is=")
print(A+A.T+np.dot(C,B)+np.dot(B.T,C.T))#Correct
print()
print("b)Calculate A/10+(A/11)^2+(A/12)/3...+(A/19)^10")
print("The result is=")
res=A/10
for i in range(2,11):
    res+=np.linalg.matrix_power(A/(10+i-1),i)
print(res)#Correct
print()
print("c)Save the odd numbers in A to a new vector")
print("The result is :")
oddVector=np.array([num for row in A for num in row if num % 2 != 0])
print(oddVector)
print()
print("d)Save the prime numbers in A to a new vector")
primeVector=np.array([num for row in A for num in row if isPrime(num)])
print("The result is :")
print(np.array(primeVector))
print()
print("e)Find the rows with the most prime numbers and print them")
MaxPV=findMaxPrime(A)
primeVectors=[]
for i in range(len(A)):
    if countPrimeRow(A[i])==MaxPV :
        primeVectors.append(A[i])
print(np.array(primeVectors))
print()
print("f)Print the row with the longest contiguous odd numbers sequence")
for i in range(len(A)):
    oddCounter=[countOddsInRow(row) for row in A]
oddVectors=[]
for i in range(len(A)):
    if oddCounter[i]==max(oddCounter):
        oddVectors.append(A[i])
print(np.array(oddVectors))