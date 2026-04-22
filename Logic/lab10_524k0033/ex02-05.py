#2
class bNode(object):
 def __init__(self,data=None):
  self.left = None
  self.right = None
  self.data = data
  
A1=bNode(2)
A1.left=bNode(7)
A1.right=bNode(5)
B1=A1.left
C1=A1.right
B1.left=bNode(2)
B1.right=bNode(6)
C1.right=bNode(9)
D1=B1.left
E1=B1.right
F1=C1.right
E1.left=bNode(5)
E1.right=bNode(11)
F1.left=bNode(4)
G1=E1.left
H1=E1.right
I1=F1.left

A2=bNode(50)
A2.left=bNode(17)
A2.right=bNode(76)
B2=A2.left
C2=A2.right
B2.left=bNode(9)
B2.right=bNode(23)
C2.left=bNode(54)
D2=B2.left
E2=B2.right
F2=C2.left
D2.right=bNode(14)
E2.left=bNode(19)
F2.right=bNode(72)
G2=D2.right
H2=E2.left
I2=F2.right
G2.left=bNode(12)
I2.left=bNode(67)

#3
def NLR(root):
 if root:
     print(root.data, end=" ")
     NLR(root.left)
     NLR(root.right)
     
def LNR(root):
 if root:
     LNR(root.left)
     print(root.data, end=" ")
     LNR(root.right)
     
def LRN(root):
 if root:
     LRN(root.left)
     LRN(root.right)
     print(root.data, end=" "),
     
#4

def breadthFirstSearch(root, target_data):
    if not root:
        return
    
    queue = [root]
    path_traveled = [] 
    
    while queue:
        current = queue.pop(0) 
        path_traveled.append(current.data)
        
        if current.data == target_data:
            print(f"BFS found '{target_data}'. Path traveled: {path_traveled}")
            return path_traveled
            
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
            
    print(f"BFS could not find '{target_data}'. Path traveled: {path_traveled}")
    return path_traveled


def depthFirstSearch(root, target_data):
    if not root:
        return
        
    stack = [root]
    path_traveled = []
    
    while stack:
        current = stack.pop() 
        path_traveled.append(current.data)
        
        if current.data == target_data:
            print(f"DFS found '{target_data}'. Path traveled: {path_traveled}")
            return path_traveled
            
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
            
    print(f"DFS could not find '{target_data}'. Path traveled: {path_traveled}")
    return path_traveled

#5

def breadthFirstSearchV(vector_tree, target_data):
    if len(vector_tree) <= 1:
        return
        
    queue = [1] 
    path_traveled = []
    
    while queue:
        idx = queue.pop(0)
        
        if idx < len(vector_tree) and vector_tree[idx] is not None:
            current_data = vector_tree[idx]
            path_traveled.append(current_data)
            
            if current_data == target_data:
                print(f"Vector BFS found '{target_data}'. Path traveled: {path_traveled}")
                return path_traveled
                
            left_idx = 2 * idx
            right_idx = 2 * idx + 1
            
            if left_idx < len(vector_tree):
                queue.append(left_idx)
            if right_idx < len(vector_tree):
                queue.append(right_idx)
                
    print(f"Vector BFS could not find '{target_data}'. Path traveled: {path_traveled}")
    return path_traveled