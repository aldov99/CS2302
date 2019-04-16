#CS2302
#Aldo Venzor
#Lab 6
#Olac Fuentes
#Anindita Nath
#04/016/19
#For this lab we were needed to build a maze using a Disjoint Set Forest, then 
#create a path to connect every element in the maze selecting randomly a wall and using 
# Normal Union and Union by Size

import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate 
import random
import time

def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1

def dsfToSetList(S):
    #Returns aa list containing the sets encoded in S
    sets = [ [] for i in range(len(S)) ]
    for i in range(len(S)):
        sets[find(S,i)].append(i)
    sets = [x for x in sets if x != []]
    return sets

def find(S,i):
    # Returns root of tree that i belongs to
    if S[i]<0:
        return i
    return find(S,S[i])

def find_c(S,i): #Find with path compression 
    if S[i]<0: 
        return i
    r = find_c(S,S[i]) 
    S[i] = r 
    return r

def union(S,i,j):
    # Joins i's tree and j's tree, if they are different
    ri = find(S,i) 
    rj = find(S,j)
    if ri!=rj:
        S[rj] = ri
        
def union_c(S,i,j):
    # Joins i's tree and j's tree, if they are different
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        S[rj] = ri
        
def union_by_size(S,i,j):
    # if i is a root, S[i] = -number of elements in tree (set)
    # Makes root of smaller tree point to root of larger tree 
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        if S[ri]>S[rj]: # j's tree is larger
            S[rj] += S[ri]
            S[ri] = rj
        else:
            S[ri] += S[rj]
            S[rj] = ri
            
def NumSets(S):
    if S is None:
        return 0
    sum=0
    for i in S:
        if i==-1:
            sum+=1
    return sum

def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0  
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols   
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off') 
    ax.set_aspect(1.0)
    
def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w

#Methot to remove walls using normal union
def NormalUnion(A):
    while NumSets(A)!=1:
        d=random.randint(0,len(walls)-1)
        if union(A,walls[d][0],walls[d][1])!=False:
            print('Removing wall ',walls[d])
            walls.pop(d)
    print(A)

#Method to remove walls using Union by Size    
def UnionBySize(B):
    while NumSets(B)!=1:
        d=random.randint(0,len(walls)-1)
        if union_by_size(B,walls[d][0],walls[d][1])!=False:
            print('Removing wall ',walls[d])
            walls.pop(d)
    print(B)

if __name__ == "__main__":    
    A=DisjointSetForest(1000)
    
    plt.close("all")
    maze_rows=40
    maze_cols=25
    
    walls = wall_list(maze_rows,maze_cols)

    draw_maze(walls,maze_rows,maze_cols,cell_nums=True) 

    print('Do you wnat to use Normal Union or Union by Size?')
    print('Press 1 for Normal Union')
    print('Press 2 for Union by Size')
    ans=int(input('Answer: '))
    
    if ans==1:
        time1=time.time()
        NormalUnion(A)
        time2=time.time()
        RT=time2-time1
        print('Running time = ',RT)
    if ans==2:
        time1=time.time()
        UnionBySize(A)
        time2=time.time()
        RT=time2-time1
        print('Running time = ', RT)
    elif ans!=1 and ans!=2:
        print('Invalid input')
    
    

    draw_maze(walls,maze_rows,maze_cols) 

