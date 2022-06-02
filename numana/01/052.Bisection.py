#2022/0421
#二分法による方程式の解の推定
#1203033123 西田裕一
from math import*

def f(x):
  return exp(-x)-x*x

#初期値の設定
a = 1
b = 0
eps = 1.0e-6
n = 0

print("学籍番号:1203033123  西田裕一")
#反復
while True:
  c = (a+b)/2
  #cは点a,bの中点
  n += 1
  print("{0:2d}　{1:.7f}".format(n,c))

  if abs(a-b)/2 < eps:
    break
  fc = f(c)


  if fc >0:
    b=c
  elif fc<0:
    a = c
  else:
    break


#終了
print("\c=",c)