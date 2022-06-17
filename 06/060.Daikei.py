#!/usr/bin/env python
# coding: utf-8

# In[1]:


#数値解析第9回課題　レポート5
#台形則による積分
#学籍番号:1203033123
#氏名: 西田裕一

from math import*


# In[2]:


def f1(x):
    return exp(x)


# In[3]:


def f2(x):
    return cos(x)


# In[11]:


def Daikei(a,b,f):
    N = 1
    eps = 1.0e-7
    h = (b-a)
    T = h*(f(a)+f(b))/2
    print("{0:4d} {1:.12f}".format(N,T))

    while True:
        N = 2*N
        h = h/2
        s = 0
        for i in range(1,int(N/2)+1):
            i = (2*i)-1
            s += f(a+i*h)
        new_T = (T/2)+h*s
        if abs(new_T-T)<abs(new_T)*eps:
            break

        T = new_T
        print("{0:4d} {1:.12f}".format(N,T))


# In[15]:


print("学籍番号:1203033123")
print("氏名:西田裕一")
print("台形則によるexp(x)の積分")
print("   N       T")
a = 0
b = 1
Daikei(a,b,f1)
print("===========================")


# In[16]:


print("台形則によるcos(x)の積分")
print("   N       T")
a = 0
b = 2
Daikei(a,b,f2)

