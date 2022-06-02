#ニュートン法による解の推定
#1203033123 西田裕一

from math import*

def f(x):
  return exp(-x)-x*x

#f(x)の導関数
def g(x):
  return -exp(-x)-2*x

#初期値
x=1
eps = 1.0e-6
n = 0

print("学籍番号:1203033123 西田裕一")

while True:
  print("{0:2d} {1:.15f}".format(n,x))
  new_x = x -f(x)/g(x)
  n = n+1

  if abs(new_x-x)<eps*abs(new_x):
    break
  x = new_x

print("{0:2d} {1:.15f}".format(n,new_x))