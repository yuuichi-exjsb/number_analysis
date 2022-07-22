#!/usr/bin/env python
# coding: utf-8

# In[34]:


#Eular法 
#学籍番号:1203033123
#氏名;西田裕一


# In[ ]:


import matplotlib
import matplotlib.pyplot as plot
from math import*


# In[35]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[41]:


def Draw(x,y):
    fig  = plot.figure()
    graph  = fig.add_subplot()
    graph.plot(x,y)
    graph.scatter(x,y,s=30)
    plot.show()


# In[37]:


def f1(t,Y1,Y2):
    return Y2


# In[38]:


def f2(t,Y1,Y2):
    return (-16*Y1)+(-10)*Y2


# In[39]:


def Eular(T,N,Y,Y1,Y2):
    dt = T/N
    x = [0]*(N+1)
    y = [0]*(N+1)
    y[0] = Y

    for j in range(N):
        t = j*dt
        x[j] = t
        new_Y1 = Y1+dt*f1(t,Y1,Y2)
        new_Y2 = Y2+dt*f2(t,Y1,Y2)
        
        Y1 = new_Y1
        Y2 = new_Y2
        
        y[j+1] = Y1
    x[N] = N*dt

    return x,y


# In[42]:


T = 1
N = 10
Y = 1
Y1 = 1
Y2 = 0
x,y = Eular(T,N,Y,Y1,Y2)
Draw(x,y)

print("{0:5d} {1:6.4f} {2:8.6f}".format(N,T/N,y[N]))


# In[43]:


T = 2
N = 10
Y = 1
Y1 = 1
Y2 = 0

x,y = Eular(T,N,Y,Y1,Y2)
Draw(x,y)

print("{0:5d} {1:6.4f} {2:8.6f}".format(N,T/N,y[N]))

