#学籍番号:1203033123
#氏名:西田裕一

#SOQ法における収束判定を備えた解法

#経過表示
def Progress(k,x):
  print(k,end="")
  for val in x:
    print(' {:8f}'.format(val),end=" ")
  print(' ')

#SOR法
def SOR(N,A,y,omega,eps):
  x = [0]*N #未知数ベクトル
  new_x = [0]*N #x[i-1]を格納する配列
  k = 0 #繰り返した数
  Progress(0,x)


  while True:
    k = k+1
    sum = 0
    error = 0
    for i in range(N):
      total = 0
      for j in range(N):
        if i != j:
          total += A[i][j]*x[j]

      new_x[i] = omega*(y[i]-total)/A[i][i] + (1-omega)*x[i]   
      
      sum += abs(new_x[i])
      error += abs(new_x[i] - x[i])
    
    #for i in range(N):
      x[i] = new_x[i]


    if error < eps*sum:
      break
    Progress(k,x)
  
  return x

N = 2
A = [[5,4],[2,3]]   
y = [13,8]
omega = 1.2
eps = 1.0e-8#収束判定値

print("学籍番号:1203033123")
print("氏名:西田裕一")
x = SOR(N,A,y,omega,eps)