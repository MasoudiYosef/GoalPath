def DFS(node, V, F, G, n,T,ST):
    if V[node] == 0:
        T = T + 1
        V[node] = T
        for j in range(n):
            if G[node, j] == 1:
                T=DFS(j, V, F, G, n,T,ST)
        T = T + 1
        F[node] = T
        ST.append(node)
    return T

def DFS2(node, V, G, n, GR):
    if V[node] == 0:
        V[node] = GR
        for j in range(n):
            if G[node, j] == 1:
                DFS2(j, V, G, n, GR)

def DFS3(node, V, F, G, n, T, Flag):
    if V[node] == 1:
        Flag=1
    if V[node] == 0:
        T = T + 1
        V[node] = 1
        for j in range(n):
            if G[node, j] == 1:
                T,Flag=DFS3(j, V, F, G, n, T, Flag)
        T = T + 1
        F[node] = T
    return T,Flag

def AllPossible(Nodes,V,index,LS):
    if index<len(V):
        V[index]=1
        ls=[]
        for i in range(index+1):
            if V[i]==1:
                ls.append(Nodes[i])
        if ls not in LS:
            LS.append(ls)
        AllPossible(Nodes,V,index+1,LS)
        V[index]=0
        AllPossible(Nodes,V,index+1,LS)

def FilterGraph(G,Nodes,n):
    FG=copy.copy(G)
    for N in range(n-1,-1,-1):
        if N not in Nodes:
            FG=np.delete(FG, N, axis=0)
            FG=np.delete(FG, N, axis=1)
    return FG

def ReadGraph(FN):
    F = open(FN, 'r')
    L = F.readlines()
    F.close()
    G = np.zeros([len(L), len(L)])
    for i in range(len(L)):
        s = L[i].replace('\n', '').split(',')
        for j in range(len(s)):
            G[i, j] = int(s[j])
    return G

def Transpose(G):
    r = len(G)
    c = len(G[0])
    TG = np.zeros([c, r])
    for i in range(r):
        for j in range(c):
            TG[j, i] = G[i, j]
    return TG

def SCC(G):
    n = len(G)
    V = []
    F = []
    NG=[]
    for i in range(n):
        V.append(0)
        F.append(0)
        NG.append(0)
    T = 0
    ST=[]
    GR=1
    for i in range(len(V)):
        if V[i]==0:
            DFS(i, V, F, G, n,T,ST)
    TG=Transpose(G)
    V = []
    for i in range(n):
        V.append(0)
    GR=1
    for i in range(len(ST)-1,-1,-1):
        if V[ST[i]]==0:
            DFS2(ST[i], V, TG, n, GR)
            GR+=1
    return V


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

import numpy as np
import copy