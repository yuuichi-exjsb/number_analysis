#学籍番号;1203033123
#氏名:西田裕一

#経過表示

def Progress(k,x):
  print(k,end="")
  for val in x:
    print(' {:8f}'.format(val),end=" ")
  print(' ')

#ヤコビ法
def Jacobi(N,A,y,eps):
  x = [0]*N #未知数ベクトル
  z = [0]*N #途中計算用

 
 
  k = 0

  Progress(0,x)

  while True:
      sum = 0
      error = 0
      k = k+1
      for i in range(N):
        total = 0
        for j in range(N):
            if i != j:
                total += A[i][j]*x[j]

        z[i] = (y[i]-total)/A[i][i]
      sum += abs(z[i])
      error += abs(z[i]-x[i])
      for i in range(N):
          x[i] = z[i]

        
      if error <  eps*sum:
        break  
      Progress(k,x)

        
  
  return x

N = 2
A = [[5,4],[2,3]]
y = [13,8]
eps = 1.0e-8
print("学籍番号:1203033123")
print("氏名:西田裕一")
x = Jacobi(N,A,y,eps)