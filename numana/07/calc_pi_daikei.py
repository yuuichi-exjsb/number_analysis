#!/usr/bin/env python
# coding: utf-8

# In[47]:


#数値解析第10回課題　レポート6
#台形則積分による円周率の推定
#学籍番号:1203033123
#氏名: 西田裕一

from math import*
 
#a-bは積分範囲
#fは関数　高階関数で導入
#pは収束判定値の指数部
#mulはTにかける値
#subはTから低く値
def Daikei(a,b,f,p,mul,sub):
    N = 1
    eps = 10**(-p)
    h = (b-a)
    T = h*(f(a)+f(b))/2
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
        
        mul_T = mul*T
        sub_T = mul_T-sub
        print("{0:4d} {1:.12f} {2:.12f}".format(N,sub_T,abs(pi-sub_T)))
        


# In[48]:


print("学籍番号:1203033123")
print("氏名:西田裕一")
print("台形則積分による円周率(1)の推定")
print("   N       T         真値との誤差")

def f(x):
    return sqrt(1-x**2)

a = 0
b = 1
Daikei(a,b,f,5,4,0)
print("===========================")


# In[49]:


print("台形則積分による円周率(2)の推定")
print("   N       T         真値との誤差")

def f1(x):
    return sqrt(1-x**2)

a = 0
b = 0.5
sub = (3*sqrt(3))/2
Daikei(a,b,f1,8,12,sub)
print("===========================")


# In[50]:


print("台形則積分による円周率(3)の推定")
print("   N       T         真値との誤差")

def f1(x):
    return 1/((x**2)+1)

a = 0
b = 1
sub = 0
Daikei(a,b,f1,7,4,sub)
print("===========================")

