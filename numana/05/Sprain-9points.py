#!/usr/bin/env python
# coding: utf-8

# In[1]:


#学籍番号:1203033123
#氏名:西田裕一
#レポート4-2
#スプライン補完による9点からの推定

import matplotlib
import matplotlib.pyplot as plot
import numpy as np
from math import *


def Gauss(N,A,y):
    x=[0]*N
    
    for k in range(N-1):
        m=0
        for i in range (k,N):
            if m < abs(A[i][k]):
                m = abs(A[i][k])
                l=i
            if l!=k:
                for n in range(k,N):
                    A[k][n],A[l][n] = A[l][n],A[k][n]
                y[k],y[l] = y[l],y[k]
        for i in range(k+1,N):
            alpha = A[i][k]/A[k][k]
            for j in range(k+1,N):
                A[i][j]-=alpha*A[k][j]
            y[i]-=alpha*y[k]
        
    x[N-1] = y[N-1]/A[N-1][N-1]
    
    for i in range(N-2,-1,-1):
        s=0
        for k in range (i+1,N):
            s +=A[i][k]*x[k]
        x[i]=(y[i]-s)/A[i][i]
    return x

def Draw(xmax,xmin,px,py,a,b,c,d):
    fig = plot.figure()
    graph = fig.add_subplot()
    N = len(a)
    graph.set_xlim(px[0],px[N])
    
    dx = (xmax-xmin)/len(a)
    for j in range(N):
        xj = px[j]; xk = px[j+1]
        qx = []; qy = []
        M = 8
        for i in range(M+1):
            x = xj + dx*i/M
            y = a[j]*(x-xj)*(x-xj)*(x-xj)+b[
                                              j]*(x-xj)*(x-xj)+c[j]*(x-xj)+d[j]
            qx +=[x]
            qy +=[y]
            
        graph.plot(qx,qy)
    graph.scatter(px,py,s=30,c="red")
    
    
    plot.show()
    
def NaturalSpline(N,px,py):
    h = [0]*N
    for j in range(N):
        h[j] = px[j+1]-px[j]
    v = [0]*N
    for j in range(N):
        v[j] = 6*((py[j+1]-py[j])/h[j]-(py[j]-py[j-1])/h[j-1])
    A = []
    for i in range(N-1):
        A += [[0]*(N-1)]
    for i in range(N-1):
        A[i][i]=2*(h[i]+h[i+1])
    for i in range(N-2):
        A[i][i+1]= h[i+1]
        A[i+1][i] = h[i]
    y = [0]*(N-1)
    for i in range (N-1):
        y[i] = v[i+1]
    
    x= Gauss(N-1,A,y)
    
    u=[0]+x+[0]
    
    b = [0]*N
    for j in range(N):
        b[j]=u[j]/2
    a = [0]*N
    for j in range(N):
        du = u[j+1]-u[j]
        dx = px[j+1]-px[j]
        a[j] = du/(6*dx)
    d = [0]*N
    for j in range(N):
        d[j] = py[j]
    c = [0]*N
    for j in range(N):
        dy = (py[j+1]-py[j])
        dx = px[j+1]-px[j]
        c[j] = dy/dx-dx*(2*u[j]+u[j+1])/6
    
    return a,b,c,d

xs = -1.0
xe = 1.0
N = 8
px = [-1.0,-0.75,-0.5,-0.25,0.0,0.25,0.5,0.75,1.0]
py =[0.0,0.5,1.0,0.5,0.0,-0.5,-1.0,-0.5,0.0]

a,b,c,d = NaturalSpline(N,px,py)
                
Draw(xe,xs,px,py,a,b,c,d)

