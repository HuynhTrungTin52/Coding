import itertools as it

dice1=[1,2,3,4,5,6]
dice2=[1,2,3,4,5,6]
lists=[]
lits=[]
for i in dice1:
    for j in dice2:
        sym=i+j
        if sym ==5 and i not in lists and j not in lists:
            lists.append(i)
            print(i,"+",j)