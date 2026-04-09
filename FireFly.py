def Initial(N,PL):
    CS=np.zeros([N,PL])
    for i in range(N):
        F=list(range(1,51))
        for j in range(PL):
            r=np.random.randint(0,len(F))
            CS[i,j]=F[r]
            del F[r]
    return CS

def GetGraph(FP):
    F=open(FP,'r')
    L=F.readlines()
    F.close()
    Graph=np.zeros([51,51])
    for D in L:
        s=D.replace('\n','').replace(']','').split('[')
        for i in range(1,len(s)):
            item=s[i].split(',')
            a,b,c=int(item[0])-1,int(item[1])-1,int(item[2])
            Graph[a,b]=Graph[a,b]+c
    return Graph

def score(CS,G,T):
    SC=[]
    for i in range(len(CS)):
        P=[]
        for j in range(0,len(CS[i])):
            if int(CS[i,j]-1) not in P:
                P.append(int(CS[i,j]-1))
        P.append(T-1)
        s=0
        for j in range(1,len(P)):
            r=P[j-1]
            c=P[j]
            s=s+G[r,c]
            if G[r,c]==0:
                s=0
                break
        SC.append(s)
    return SC

def SelectBests(SC,nog):
    bests=[]
    S=copy.deepcopy(SC)
    BS=list(range(0,len(SC)))
    for j in range(0,nog):
        ma=max(S)
        inx=S.index(ma)
        bests.append(BS[inx])
        del S[inx]
        del BS[inx]
    return bests

def Movement(CS,SC,bests):
    flag=[]
    for i in range(len(CS)):
        flag.append(0)
    c=len(CS[0])
    r=len(CS)
    for i in range(0,r):
        if i not in bests:
            k=bests[random.randint(0,len(bests)-1)]
            A=random.randint(0,c-1)
            for j in range(0,A):
                s=int(random.randint(0,c-1))
                CS[i,s]=CS[k,s]
    return CS 

def RandomWalk(CS,bests,RW):
    c=len(CS[0])
    r=len(CS)
    for i in range(r):
        if i not in bests:
            for j in range(0,RW):
                s=int(random.randint(0,c-1))
                CS[i,s]=int(random.randint(1,50))
    return CS

import numpy as np
import random
import copy
import matplotlib.pyplot as plt
Data=['BF','CL','GB','RB','TP']
Data=['TP']
for DT in Data:
    FP='Data/'+DT+'.txt'
    GS=GetGraph(FP)
    for rn in range(1,51):
        nof=1000
        PL=5
        T=51
        CS=Initial(nof,PL)
        SC=score(CS,GS,T)
        noi=100
        ham=[]
        nob=20
        bests=SelectBests(SC,nob)
        step=noi//PL
        for i in range(0,noi):
            RW=max(1,PL-i//PL)
            bests=SelectBests(SC,nob)
            CS=Movement(CS,SC,bests)
            CS=RandomWalk(CS,bests,RW)
            SC=score(CS,GS,T)
            V=max(SC)
            ham.append(V)
        nog=10
        bests=SelectBests(SC,nog)
        F=open('RST/FF_Bests_'+DT+'_'+str(rn)+'.txt','w')
        for be in bests:
            F.write(str(CS[be])+'\n')
        F.close()
        F=open('RST/FF_ham_'+DT+'_'+str(rn)+'.txt','w')
        for h in ham:
            F.write(str(h)+'\n')
        F.close()
        print('Iteartion '+str(rn)+' finished')
        # x=list(range(1,len(ham)+1))
        # plt.plot(x,ham)
        # plt.xlabel('#Iteration',fontsize=12)
        # plt.ylabel('Score',fontsize=12)
        # plt.title('Convergence of FireFly')
        # plt.show()