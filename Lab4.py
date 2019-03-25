#CS2302
#Aldo Venzor
#Lab 4
#Olac Fuentes
#Anindita Nath
#03/24/19
#The purpose of this lab is to practice coding related with b-trees implementing some basic functions

import math

class BTree(object):
    # Constructor
    def __init__(self,item=[],child=[],isLeaf=True,max_items=5):  
        self.item = item
        self.child = child 
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items

def IsFull(T):
    return len(T.item) >= T.max_items

def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)
        
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid]) 
        rightChild = BTree(T.item[mid+1:]) 
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf) 
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf) 
    return T.item[mid], leftChild,  rightChild   

def InsertLeaf(T,i):
    T.item.append(i)  
    T.item.sort()
    
def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree    
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)

def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)
        
def PrintD(T,space):
    # Prints items and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
    else:
        PrintD(T.child[len(T.item)],space+'   ')  
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
            PrintD(T.child[i],space+'   ')

#1 Function to obtain the height of the tree
def height(T):
    if T.isLeaf:
        return 0
    return 1 + height(T.child[0])

#2 Function to store the items in the tree into a sorted list
def TreeList(T, A):
    if T.isLeaf:
        for i in range(len(T.item)):
            A.append(T.item[i])
        return
    for i in range(len(T.item)):
        TreeList(T.child[i],A)
        A.append(T.item[i])
    TreeList(T.child[len(T.item)],A)
    return A

#3 Function to look for the smallest element at a given depth, returns none if the
#given depth does not exist
def MinAtD(T,d):
    if  len(T.item)<=0:
        return None
    if d==0:
        return T.item[0]
    if T.isLeaf:
        return None
    return MinAtD(T.child[0],d-1)

#4 Function to look for the biggest element at a given depth, returns none if the
#given depth does not exist
def MaxAtD(T,d):
    if len(T.item)==0:
        return None
    if d==0:
        return T.item[-1]
    if T.isLeaf:
        return None
    return MaxAtD(T.child[-1],d-1)

#5 Function to return the number of elements at a given depth
def NumItemsD(T, d):
    if d==0:
        return 1
    if T.isLeaf:
        return 0
    c=0
    for i in range(len(T.child)):
        c+=NumItemsD(T.child[i], d-1)
    return c

#6 Function to print all the elements at a given depth
def PrintAtD(T,d):
    if d==0:
        for i in T.item:
            print(i, end=' ')
    for i in range(len(T.child)):
        PrintAtD(T.child[i],d-1)
    return

#7 Function to return the number of full nodes in a tree
def FullNodes(T):
    if len(T.item)==0:
        return 0
    if len(T.item)==T.max_items:
        return 1
    if T.isLeaf:
        return 0
    c=0
    for i in range(len(T.item)):
        c+=FullNodes(T.child[i])
    c+=FullNodes(T.child[-1])
    return c

#8 Function to return the number of full leaves in a tree
def FullLeaves(T):
    if len(T.item)==0:
        return 0
    if len(T.item)==T.max_items and T.isLeaf:
        return 1
    if T.isLeaf:
        return 0
    c=0
    for i in range(len(T.item)):
        c+=FullNodes(T.child[i])
    c+=FullNodes(T.child[-1])
    return c

#9 Function that returns the depth where a given element is found
def KeyD(T,k):
    if len(T.item)==0:
        return None
    for i in range(len(T.item)):
        if T.item[i]==k:
            return 0
        if T.item[i]>k:
            return 1+KeyD(T.child[i],k)
    if T.isLeaf:
        return -1
    return 1+KeyD(T.child[-1],k)


#Section to call and test the functions 
L = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5,105, 115, 200, 2, 45, 6]
EL=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
E=[]
T = BTree()    
for i in L:
    print('Inserting',i)
    Insert(T,i)
    PrintD(T,'') 
    #Print(T)
    print('\n####################################')
          
print(height(T))
TL=TreeList(T,[])
for i in TL:
    print(i, end=' ')
print()
print(MinAtD(T,2))
print(MaxAtD(T,2))
print(NumItemsD(T,2))
PrintAtD(T,2)
print(FullNodes(T))
print(FullLeaves(T))
print(KeyD(T,120))
