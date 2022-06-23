#!/usr/bin/env python
# coding: utf-8

# In[8]:


#数値解析第9回課題　レポート5
#台形則による積分
#学籍番号:1203033123
#氏名: 西田裕一

from math import*


# In[9]:


def f1(x):
    return exp(x)


# In[10]:


def f2(x):
    return cos(x)


# In[15]:


def sympson(a,b,f):
    N = 2
    eps = 1.0e-14
    h = (b-a)/2
    T = h*(f(a)+2*f((a+b)/2)+f(b))/2
    S = h*(f(a)+4*f((a+b)/2)+f(b))/3

    print("{0:4d} {1:.12f}".format(N,S))

    while True:
        N = 2*N
        h = h/2
        s = 0
        for i in range(1,int(N/2)+1):
            i = (2*i)-1
            s += f(a+i*h)
        new_T = (T/2)+h*s
        new_S = (4*new_T-T)/3
        if abs(new_S-S)<abs(new_S)*eps:
            break

        T = new_T
        S = new_S
        print("{0:4d} {1:.12f}".format(N,S))


# In[20]:


print("学籍番号:1203033123")
print("氏名:西田裕一")
print("シンプソン則によるexp(x)の積分")
print("   N       S")
a = 0
b = 1
sympson(0,1,f1)
print("==============================")


# In[21]:


print("シンプソン則によるcos(x)の積分")
print("   N       S")
a = 0
b = 2
sympson(0,2,f2)

