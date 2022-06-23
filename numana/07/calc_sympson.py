#!/usr/bin/env python
# coding: utf-8

# In[20]:


#数値解析第10回課題　レポート6
#シンプソン則による積分
#学籍番号:1203033123
#氏名: 西田裕一

from math import*

#a-bは積分範囲
#fは関数　高階関数で導入
#pは収束判定値の指数部
#mulはSにかける値
#subはSから低く値
def sympson(a,b,f,p,mul,sub):
    N = 2
    eps = 10**(-p)
    h = (b-a)/2
    T = h*(f(a)+2*f((a+b)/2)+f(b))/2
    S = h*(f(a)+4*f((a+b)/2)+f(b))/3

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
        mul_S = mul*S
        sub_S = mul_S-sub
        print("{0:4d} {1:.12f} {2:.12f}".format(N,sub_S,abs(pi-sub_S)))


# In[21]:


print("学籍番号:1203033123")
print("氏名:西田裕一")
print("シンプソン則積分による円周率(1)の推定")
print("   N       T         真値との誤差")

def f(x):
    return sqrt(1-x**2)

a = 0
b = 1
sympson(a,b,f,6,4,0)
print("===========================")


# In[22]:


print("シンプソン則積分による円周率(2)の推定")
print("   N       T         真値との誤差")

def f1(x):
    return sqrt(1-x**2)

a = 0
b = 0.5
sub = (3*sqrt(3))/2
sympson(a,b,f1,14,12,sub)
print("===========================")


# In[27]:


print("台形則積分による円周率(3)の推定")
print("   N       T         真値との誤差")

def f2(x):
    return 1/((x**2)+1)

a = 0
b = 1
sub = 0
sympson(a,b,f2,16,4,sub)
print("===========================")

