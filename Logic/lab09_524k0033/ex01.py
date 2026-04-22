import numpy as np

def mPlus(A,B):
    return A+B

def mMinus(A,B):
    return A-B

def mMultiply(A,B):
    res=np.zeros((len(A),len(B[0])))
    for i in range(len(A)):          
     for j in range(len(B[0])):   
        for k in range(len(B)):   
         res[i][j] += A[i][k] * B[k][j]
    return res
def mTranspose(A):
    return [[int(x) for x in row] for row in zip(*A)]


A=np.array([[1,2],[3,4]])
B=np.array([[2,0],[1,2]])
FA=np.array([[1,4,6,10],[2,7,5,3]])
FB=np.array([[1,4,6],[2,7,5],[9,0,11],[3,1,0]])
print(mTranspose(FA))