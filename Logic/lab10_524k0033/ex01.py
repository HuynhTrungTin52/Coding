Tree1=[None,2,
       7,5,
       2,6,None,9,
       None,None,5,11,None,None,4,None]

Tree2 = [None,50,
         17,76,
         9,23,54,None,
         None,14,19,None,None,72,None,None,
         None,None,12,None,None,None,None,None,None,None,67,None,None, None]

def printTree(Tree):
    level_limit = 1  
    count = -1      
    
    for val in Tree:
        count += 1
        if val:
         print(val, end=" ")
        
        if count == level_limit:
            print()        
            count = 0     
            level_limit *= 2 
        
printTree(Tree1)