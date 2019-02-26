#CS2302
#Aldo Venzor
#Lab 2
#Olac Fuentes
#Anindita Nath
#02/25/2019
#The purpose of this program is to sort a Linked List using different sorting methods, and to return the mid point

from random import random

#Node Functions
class Node(object):
    # Constructor
    def __init__(self, item, next=None):  
        self.item = item
        self.next = next 
        
#List Functions
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None
        
#Returns the element in the middle possition of a linked list after being sorted        
def MidPoint(L):
    t=L.head
    len=getLength(L)
    for i in range(len):
        if i==int(len/2):
            return(t.item)
        t=t.next

#This method makes an exact copy of a given linked list        
def CopyList(L):
	NewList = List()
	t = L.head
	while t is not None: 
		Append(NewList, t.item) 
		t = t.next
	return NewList      

#Checks is a linked list is empty        
def IsEmpty(L):  
    return L.head == None

def Append(L,x): 
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next
        
def PrintList(L):
    # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line 

#Returns the length of a linked list    
def getLength(L):
    if IsEmpty(L):
        return 0
    temp=L.head
    count=0
    while temp is not None:
        count+=1
        temp=temp.next
    return count

#Bubble sort
def BS(L):
    keepDoing=True
    while keepDoing:
        t=L.head    
        while t.next is not None:
            if t.item>t.next.item:
                temp=t.item
                t.item=t.next.item
                t.next.item=temp
                keepDoing=False
            t=t.next
        keepDoing=not keepDoing
    PrintList(L)
    t=L.head
    len=(getLength(L))
    for i in range(len):
        if i==int(len/2):
            print(t.item)
        t=t.next

#Merge sort        
def MS(L):
	len = getLength(L) 
	if len <= 1: 
		return L
	L1 = List() 
	L2 = List() 
	t = CopyList(L) 
	count=0
	for i in range(len//2): 
		Append(L1, t.head.item) 
		t.head = t.head.next
		count+=1
	while count < len: 
		Append(L2, t.head.item) 
		t.head = t.head.next
		count+=1
	LeftL = List() 
	LeftL = MS(L1) 
	RightL = List() 
	RightL = MS(L2) 
	TotalL = List() 
	while getLength(TotalL)!=len: 
		if IsEmpty(RightL): 
			Append(TotalL, LeftL.head.item)
			LeftL.head = LeftL.head.next
		elif IsEmpty(LeftL): 
			Append(TotalL, RightL.head.item)
			RightL.head = RightL.head.next
		elif RightL.head.item < LeftL.head.item: 
			Append(TotalL, RightL.head.item)
			RightL.head = RightL.head.next
		else: 
			Append(TotalL, LeftL.head.item)
			LeftL.head = LeftL.head.next 
	return TotalL

#Quick sort
def QS(L):
	if getLength(L)<=1: 
		return L
	piv = L.head.item 
	L1 = List() 
	L2 = List() 
	t = L.head.next 
	while t is not None: 
		if t.item < piv: 
			Append(L1, t.item)
		else: 
			Append(L2, t.item)
		t = t.next
	SmallSide = List() 
	SmallSide = QS(L1) 
	BigSide = List() 
	BigSide = QS(L2) 
	t2 = List() 
	if IsEmpty(SmallSide): 
		Append(t2, piv)
		t2.head.next = BigSide.head
		t2.tail = BigSide.tail
		return t2
	elif IsEmpty(BigSide): 
		Append(SmallSide, piv)
		return SmallSide
	else: 
		Append(SmallSide, piv)
		SmallSide.tail.next = BigSide.head
		SmallSide.tail = BigSide.tail
		return SmallSide
    
#Modified quick sort
def MQS(L, median):
	piv = L.head.item 
	L1 = List() 
	L2 = List() 
	t = L.head.next
	while t is not None: 
		if t.item < piv: 
			Append(L1, t.item)
		else: 
			Append(L2, t.item)
		t = t.next
	if getLength(L1)<median: 
		return MQS(L2, median-getLength(L1)-1)
	elif getLength(L1)>median: 
		return MQS(L1, median) 
	else:
		return piv
    
L = List()
for i in range(5):
    x=int(random()*10)
    Append(L,x)
    
PrintList(L)
#BS(L)
#PrintList(MS(L))
#MidPoint(MS(L))
#PrintList(QS(L))
#MidPoint(QS(L))
#median=int(MidPoint(L))
#PrintList(QS(L))
#print(MQS(L,median))
