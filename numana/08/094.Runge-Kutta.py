#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Eular法 
#学籍番号:1203033123
#氏名;西田裕一


# In[ ]:


import matplotlib
import matplotlib.pyplot as plot
from math import*


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


def Draw(x,y):
    fig  = plot.figure()
    graph  = fig.add_subplot()
    graph.plot(x,y)
    graph.scatter(x,y,s=30)
    plot.show()


# In[4]:


def f1(t,Y1,Y2):
    return Y2


# In[5]:


def f2(t,Y1,Y2):
    return (-16*Y1)+(-10)*Y2


# In[10]:


def RK4(T,N,Y,Y1,Y2):
    dt = T/N
    x = [0]*(N+1)
    y = [0]*(N+1)
    
    y[0] = Y
    
    for j in range(N+1):
        t = j*dt
        x[j] = t
        k1_1 = f1(t,Y1,Y2)
        k1_2 = f2(t,Y1,Y2)
        
        k2_1 = f1(t+dt/2,Y1+dt/2*k1_1,Y2+dt/2*k1_2)
        k2_2 = f2(t+dt/2,Y1+dt/2*k1_1,Y2+dt/2*k1_2)
            
        k3_1 = f1(t+dt/2,Y1+dt/2*k2_1,Y2+dt/2*k2_2)
        k3_2 = f2(t+dt/2,Y1+dt/2*k2_1,Y2+dt/2*k2_2)
        
        k4_1 = f1(t+dt/2,Y1+dt/2*k3_1,Y2+dt/2*k3_2)
        k4_2 = f2(t+dt/2,Y1+dt/2*k3_1,Y2+dt/2*k3_2)
       
        Y1 += dt/6*(k1_1+2*k2_1+2*k3_1+k4_1)
        Y2 += dt/6*(k1_2+2*k2_2+2*k3_2+k4_2)
        
        y[j] = Y1
    
    x[N] = N *dt
    return x,y


# In[11]:


T = 1
N = 10
Y = 1
Y1 = 1
Y2 = 0

x,y = RK4(T,N,Y,Y1,Y2)
Draw(x,y)

print("{0:5d} {1:6.4f} {2:8.6f}".format(N,T/N,y[N]))


# In[12]:


T = 2
N = 10
Y = 1
Y1 = 1
Y2 = 0

x,y = RK4(T,N,Y,Y1,Y2)
Draw(x,y)

print("{0:5d} {1:6.4f} {2:8.6f}".format(N,T/N,y[N]))

