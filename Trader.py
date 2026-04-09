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


def grouping(CS,bests):
    GR=[]
    for i in range(0,len(CS)):
        k=random.randint(0,len(bests)-1)
        GR.append(bests[k])
    return GR

def distributing(CS,GR):
    c=len(CS[0])
    r=len(CS)
    for i in range(0,r):
        if i != GR[i]:
            k=random.randint(1,int(round(c*0.2)))
            for j in range(0,k):
                s=int(random.randint(0,c-1))
                CS[i,s]=CS[GR[i],s]
    return CS

def IE(CS,GR):
    c=len(CS[0])
    r=len(CS)
    for i in range(0,r):
        if i == GR[i]:
            k=random.randint(1,int(round(c*0.2)))
            for j in range(0,k):
                s=int(random.randint(0,c-1))
                r=int(random.randint(0,len(GR)-1))
                CS[i,s]=CS[GR[r],s]
    return CS

def retailing(CS,itr,noi):
    c=len(CS[0])
    r=len(CS)
    for i in range(r):
        k=int(max(1,100-round(itr/noi*100)))
        for j in range(0,k):
            s=int(random.randint(0,c-1))
            CS[i,s]=int(random.randint(1,50))
    return CS

def CheckImprovments(CS,SC,BR,BRS):
    r=len(CS)
    c=len(CS[0])
    for i in range(r):
        if BRS[i]>SC[i]:
            CS[i]=BR[i]
            SC[i]=BRS[i]
    return CS,SC

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
        nob=1000
        PL=5
        T=51
        CS=Initial(nob,PL)
        SC=score(CS,GS,T)
        noi=100
        ham=[]
        nog=10
        for i in range(0,noi):
            bests=SelectBests(SC,nog)
            GR=grouping(CS,bests)
            BR=copy.deepcopy(CS)
            BR=distributing(BR,GR)
            BRS=score(BR,GS,T)
            CS,SC=CheckImprovments(CS,SC,BR,BRS)
            BR=copy.deepcopy(CS)
            BR=IE(BR,GR)
            BRS=score(BR,GS,T)
            CS,SC=CheckImprovments(CS,SC,BR,BRS)
            BR=copy.deepcopy(CS)
            BR=retailing(BR,i,noi)
            BRS=score(BR,GS,T)
            CS,SC=CheckImprovments(CS,SC,BR,BRS)
            V=max(SC)
            ham.append(V)
        nog=10
        bests=SelectBests(SC,nog)
        F=open('RST/TR_Bests_'+DT+'_'+str(rn)+'.txt','w')
        for be in bests:
            F.write(str(CS[be])+'\n')
        F.close()
        F=open('RST/TR_ham_'+DT+'_'+str(rn)+'.txt','w')
        for h in ham:
            F.write(str(h)+'\n')
        F.close()
        print('Iteartion '+str(rn)+' finished')
        # x=list(range(1,len(ham)+1))
        # plt.plot(x,ham)
        # plt.xlabel('#Iteration',fontsize=12)
        # plt.ylabel('Score',fontsize=12)
        # plt.title('The convergence of Trader')
        # plt.show()