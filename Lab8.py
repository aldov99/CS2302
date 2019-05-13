"""
Class:CS2302
Author: Aldo Venzor
Assignment: Lab8
Professor: Olac Fuentes
TA: Anindita Nath
Description: For this lab we were required to create a program to identify trigonometic
identitied testing different functions with all combinations frpm -pi to pi. Then,
we were required to solve the partition problem using backtracking.
"""

import random
import numpy as np
from math import *

def cUnion(S,S1,S2):
    if len(S1)+len(S2)!=len(S):
        return False
    sum=0
    sbSum=0
    for i in S1:
        if i not in S:
            return False
    for i in S2:
        if i not in S:
            return False
    return True

def Disjunction(S,S1,S2):
    if len(S1)<len(S2):
        for i in S1:
            if i in S2:
                return False
        for i in S2:
            if i in S1:
                return False
        return True
    
def bPartition(S,S1,l,g):
    if g==0:
        return True,[],[]
    if g<0 or l<0:
        return False,[],[]
    a, SS, S2= bPartition(S,S1,l,g-S[l])
    if a:
        SS.append(S[l])
        S1[l]=0
        S2=[]
        for i in range(len(S1)):
            if S1[i]!=0:
                S2.append(S1[i])
        return True,SS,S2
    else:
        return bPartition(S,S1,l-1,g)
    
def rEqual(f, t=1000,tol=0.0001):
    ans=[[]for i in range(len(f))]
    for i in range(len(f)):
        ans[i]=[True for i in range(len(f))]
    for i in range(len(f)):
        for j in range(len(f)):
            for k in range(t):
                t1=random.uniform(-pi,pi)
                f1=eval(f[i])
                f2=eval(f[j])
                if np.abs(f1-f2)>tol:
                    ans[i][j]=False
                    break
    return ans

#Main
tIdentities=['sin(t)', 'cos(t)','tan(t)','1/cos(t)','-sin(t)','-cos(t)','-tan(t)'
             ,'sin(-t)','cos(-t)','tan(-t)','(sin(t))/(cos(t))','(2)*(sin(t/2))*(cos(t/2))'
             ,'sin(t)*sin(t)','1-((cos(t))*(cos(t)))','(1-cos(t)*cos(t))/2','1/(cos(t))']
comparisons=rEqual(tIdentities)

print('Trigonometic functions that equal each other:')
for i in range(len(comparisons)):
    for j in range(len(comparisons[i])):
        if comparisons[i][j]:
            print('[',tIdentities[i],':',tIdentities[j],']')
            
S=[1,2,4,5,9,10,12,3]
S1=[S[i]for i in range(len(S))]
sum=0
for i in range(len(S)):
    sum+=S[i]
PSS,SS1,SS2=(bPartition(S,S1,len(S)-1,sum/2))
S1=0
S2=0
if PSS:
    u=cUnion(S,SS1,SS2)
    d=Disjunction(S,SS1,SS2)
    if u and d:
        print('Subset found in set= ',S)
        print('Subset 1; ', SS1)
        print('Subset 2: ', SS2)
    else:
        if u is False:
            print('No set found in set= ',S)
        else:
            print('No set found in set= ',S)
else:
    print('No set was foundt in set= ',S)

