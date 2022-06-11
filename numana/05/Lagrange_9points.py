#!/usr/bin/env python
# coding: utf-8

# In[1]:


#学籍番号:1203033123
#氏名:西田裕一
#レポート4-2 
#ラグランジュ補間による9点の推定
import matplotlib
import matplotlib.pyplot as plt
from math import*

def Draw(xs,xe,px,py,lx,ly):
    fig = plt.figure()
    graph = fig.add_subplot()
    graph.set_xlim(xs,xe)

    graph.plot(lx,ly)
    graph.scatter(px,py,s=30,c= "red")

    plt.show()

#ラグランジュ補間関数
def Lagrange(N,px,py,x):
    y = 0.0
    for j in range(N):
        lj = 1.0
        for i in range(N):
            if i != j:
                lj = lj*(x-px[i])/(px[j]-px[i])
        
        y = y + py[j]*lj
    
    return y
N = 9
px = [-1.0,-0.75,-0.5,-0.25,0.0,0.25,0.5,0.75,1.0]
py = [0.0,0.5,1.0,0.5,0.0,-0.5,-1.0,-0.5,0.0]
M = 100
lx = []
ly = []

for i in range(-M,M+1):
    x = i/M
    y = Lagrange(N,px,py,x)
    #print("{0:.3f} {1:.3f}".format(x,y))
    lx += [x]
    ly += [y]

Draw(-1.0,1.0,px,py,lx,ly)

