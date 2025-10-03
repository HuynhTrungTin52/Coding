def isREF(matrix):
    
    allZeroAtRow=-1
    lastRowwithNum=0
    leadingEntryAtColumn=-1
    lastrow=-1
    for row in range(Row):
        allZero=True    
        for column in range(Column):
            if(matrix[row][column]!=0):
                allZero=False
                if(column>leadingEntryAtColumn and row!=lastrow):
                    
                    lastrow=row
                    leadingEntryAtColumn=column
                else:
                    return False
                lastRowwithNum=row
                break
        if(allZero):
            allZeroAtRow=row
                
    
    if(lastRowwithNum>allZeroAtRow and allZeroAtRow>-1):
            return False     

def findLeftNonZeroCol(matrix):
    for column in range(Column):
        for row in range(Row):
            if(matrix[row][column]!=0):
                return column
    return -1

def interChangeRows(matrix,rowZero,rowNonZero):
    # for column in range(Column):
    #     print("[",rowZero,"]")
        matrix[rowZero][0],matrix[rowNonZero][]=matrix[rowNonZero][1],matrix[rowZero][0]



Row = int(input("Enter the number of rows:"))
Column = int(input("Enter the number of columns:"))

matrix = []
print("Enter the entries row wise:")

for row in range(Row):    
    a = []
    
    for column in range(Column):   
        a.append(int(input()))
    matrix.append(a)

print(matrix)

for row in range(Row):
    for column in range(Column):
        print(matrix[row][column], end=" ")
    print()

if(isREF(matrix)==False):
    print("The matrix above is not in Row echeleon form !")

print("The leftmost non-zero column is :")

nonZeroColumn=findLeftNonZeroCol(matrix)
for row in range(Row):
    for column in range(Column):
        if(column==nonZeroColumn):
            print("[",matrix[row][column],"]",end=" ")
        else :
            print(matrix[row][column], end=" ")
    print()

if(matrix[0][nonZeroColumn]==0):
    print("Interchanging the rows...")
    interChangeRows(matrix,0,nonZeroColumn)

for row in range(Row):
    for column in range(Column):
        print(matrix[row][column], end=" ")
    print()


