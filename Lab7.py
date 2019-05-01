"""
Class:CS2302
Author: Aldo Venzor
Assignment: Lab7
Professor: Olac Fuentes
TA: Anindita Nath
Description: For this lab we were assigned to generate a maze, and randomly remove
walls to create one path to conect every element in the maze with different 
algorithms to compare their running times.
"""

import numpy as np
import random
import time
import sys
import queue

def AdjacencyList(r,c,w):
    g=FullAL(r,c)
    for i in w:
        g[i[0]].remove(i[1])
        g[i[1]].remove(i[0])
    return g

def FullAL(r,c):
    g=[[]for a in range(r*c)]
    for i in range(c):
        for j in range(c):
            curr=j+i*c
            if i!=0:
                g[curr].append(curr-c)
            if curr%c!=0:
                g[curr].append(curr-1)
            if j!=(c-1):
                g[curr].append(curr+1)
            if i!=r-1:
                g[curr].append(curr+c)
    return g

def wallL(mr,mc):
    w=[]
    for i in range(mr):
        for j in range(mc):
            curr=j+i*mc
            if j!=mc-1:
                w.append([curr,curr+1])
            if i!=mr-1:
                w.append([curr,curr+mc])
    return w

def NumSets(S):
    c=0
    for i in S:
        if i==-1:
            c+=1
    return c

def NormalUnion(S,i,j):
    I=Find(S,i)
    J=Find(S,j)
    if I!=J:
        S[J]=I
        return True
    return False

def UnionByCompression(S,i,j):
    I=FindForCompression(S,i)
    J=FindForCompression(S,j)
    if I!=J:
        S[J]=I
        return True
    return False

def Find(S,i):
    if S[i]<0:
        return i
    return Find(S,S[i])

def FindForCompression(S,i):
    if S[i]<0:
        return i
    ans=FindForCompression(S,S[i])
    S[i]=ans
    return ans

def is_unique(r,c):
    if r==c-1:
        print("A unique path exist in the Maze")
    elif r<c-1:
        print("Path may not be existent")
    else:
        print("Exist at least one path")
        
def BreadthSearch(g,v):
    vis, prev=[False for a in range(len(g))], [-1 for b in(len(g))]
    q=queue.Queue(1)
    vis[v]=True
    while not q.empty():
        u=q.get()
        for i in g[u]:
            if not vis[i]:
                vis[i]=True
                prev[i]=u
                q.put(i)
    PathP(prev,len(g)-1)
    
def DFSS(g,v):
    vis, prev=[False for a in range(len(g))], [-1 for b in range(len(g))]
    s=[]
    s.append(v)
    vis[v]=True
    while s!=[]:
        q=s.pop()
        for i in g[q]:
            if not vis[i]:
                vis[i]=True
                prev[i]=q
                s.append(i)
    PathP(prev, len(g)-1)
    
def DFSR(g,s):
    global vr
    global pr
    vr[s]=True
    for i in g[s]:
        if not vr[i]:
            vr[i]=True
            pr[i]=s
            DFSR(g,i)
    
def PathP(prev,v):
    if prev[v]!=1:
        PathP(prev,prev[v])
        print("-",end='')
        print(v,end='')
        
def DSF(s):
    return np.zeros(s,dtype=np.int)-1
        
#Main
mr=5
mc=5
print("Number of cells: ",mr*mc)
NumWalls=int(input("How many walls would you like to remove?"))
answer=int(input("Press 1 for Standar union and 2 for Union by compression"))

w=wallL(mr,mc)
S=DSF(mr*mc)

#1
is_unique(NumWalls,(mc*mr))
while NumSets(S)>1:
    d=random.randint(0,len(w)-1)
    if answer==1:
        if NormalUnion(S,w[d][0],w[d][1]):
            w.pop(d)
    elif answer==2:
        if UnionByCompression(S,w[d][0],w[d][1]):
            w.pop(d)
    else:
        sys.exit("Not valid answer")
        
#2
g=AdjacencyList(mr,mc,w)
print("Adjacency List: ",g)
start=time.time()*1000

#3.1
"""print("\nUsing BFS: 0",end='')
BreadthSearch(g,0)
end1=time.time()*1000
print("\nRuntime with BFS: ",round((end1-start),4),"s")"""

#3.2
print("\nUsing DFSS: 0",end='')
DFSS(g,0)
end2=time.time()*1000
print("\nRuntime with DFSS: ",round((end2-start),4),"s")

#3.3
vr,pr=[False for a in range(len(g))],[-1 for b in range(len(g))]
DFSR(g,0)
print("\nUsing DFSR: 0",end='')
PathP(pr,(mc*mr)-1)
end3=time.time()*1000
print("\nRuntime with DFSR: ", round((end3-start),4),"S")

        
