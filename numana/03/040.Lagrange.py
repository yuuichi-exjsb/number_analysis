import matplotlib
import matplotlib.pyplot as plt

def Draw(xs,xe,px,py,lx,ly):
    fig = plt.figure()
    graph = fig.add_subplot()
    graph.set_xlim(xs,xe)

    graph.plot(lx,ly)
    graph.scatter(px,py,s=30,c= "red")

    plt.show()

#ラグランジュ補間関数
def Lagrange(N,px,py,x):
    y = 0.0
    for j in range(N):
        lj = 1.0
        for i in range(N):
            if i != j:
                lj = lj*(x-px[i])/(px[j]-px[i])
        
        y = y + px[j]*lj
    
    return y


N = 3
px = [0.2,0.6,0.4]
py = [0.3,0.8,0.4]
M = 10
lx = []
ly = []

for i in range(0,M+1):
    x = i/M
    y = Lagrange(N,px,py,x)
    #print("{0:.3f} {1:.3f}".format(x,y))
    lx += [x]
    ly += [y]

Draw(0.0,1.0,px,py,lx,ly)