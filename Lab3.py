#CS2302
#Aldo Venzor
#Lab 3
#Olac Fuentes
#Anindita Nath
#03/08/2019
#The purpose of this lab, is to execute some functions related with trees based on lists

class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item,end = ' ')
        InOrder(T.right)
  
def InOrderD(T,space):
    # Prints items and structure of BST
    if T is not None:
        InOrderD(T.right,space+'   ')
        print(space,T.item)
        InOrderD(T.left,space+'   ')
  

#2 This function recieves aa tree and a number, the purpose is to return the value if
#it is present in the tree, return none otherwise. This process shoul be done with out
#using recursion
def FindIter(Tree,k):
    T=Tree
    while T is not None:
        if T.item==k:
            return T.item
        elif T.item>k:
            T=T.left
        else:
            T=T.right
    return None

#3 This function builds a balanced binary search tree using a sorted list
def ListTree(A):
    if not A:
        return None
    mid=len(A)//2
    T=BST(A[mid])
    T.left=ListTree(A[:mid])
    T.right=ListTree(A[mid+1:])
    return T

#4 This function builds a sorted list using a binary search tree
def TreeList(T, A=[]):
    if T is not None:
        TreeList(T.left, A)
        A+=[T.item]
        TreeList(T.right,A)
    return A

#5 This three functions are used to print the elements of a binary search tree
#ordered by depth
def Height(T): 
    if T is None: 
        return 0 
    else : 
        lDepth = Height(T.left) 
        rDepth = Height(T.right) 
  
        if (lDepth > rDepth): 
            return lDepth+1
        else: 
            return rDepth+1
        
def PrintDepth(T):
    h=Height(T)
    for i in range(h):
        print('Depth', i ,end=' ')
        GivenDepth(T,i+1)
        print()
        
def GivenDepth(T,i):
    if T is None:
        return
    if i==1:
        print(T.item, end=' ')
    elif i>1:
        GivenDepth(T.left, i-1)
        GivenDepth(T.right, i-1)
        
#Main. To call the fuctions used in this lab, and to test the outputs of each function
T = None
count=0
sum=0
A = [70, 50, 90, 130, 150, 40, 10, 30, 100, 180, 45, 60, 140, 42]
for a in A:
    T = Insert(T,a)
 
InOrderD(T,'    ') 

print(FindIter(T,70))
List=[1,2,3,4,5,6,7]
Tree=ListTree(List)
InOrderD(Tree,'   ')
L=[]
L=TreeList(T,L)
for i in range(len(L)):
    print(L[i],end=' ')
print()
PrintDepth(T)
