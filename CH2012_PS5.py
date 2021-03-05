import math
import statistics as stat
import numpy as np
def f(a,b,x):
    z=a*(math.exp((-1)*b*x))
    return z
def f_a(a,b,x):
    z=math.exp((-1)*b*x)
    return z
def f_b(a,b,x):
    z=a*(-x)*math.exp((-1)*b*x)
    return z
def comp():
    a=20000
    b=0.03
    xi=[0,10,20,30,40,50,60,70,80,90,100,120,140,160,180,200]
    yi=[50000,20000,12000,8000,5000,3000,2000,1500,1000,700,500,300,200,125,90,70]


    ym=stat.mean(yi)
    D=[0]*16
    r=16
    c=2
    Sr=0
    St=0
    arr=[[0 for i in range(c)]for j in range(r)]
    for j in range(10):
        for i in range(16):
            D[i]=yi[i]-f(a,b,xi[i])
            arr[i][0]=f_a(a,b,xi[i])
            arr[i][1]=f_b(a,b,xi[i])
        
        
        
        A=(np.dot(np.transpose(arr),arr))
        B=np.linalg.inv(A)
        B=np.dot(B,np.transpose(arr))
        A=np.dot(B,D)
        a=a+A[0]
        b=b+A[1]
        print([a,b])
        if(A[0]/a<0.01 and A[1]/b<0.01):
            for i in range(10):
                Sr=Sr+D[i]*D[i]
                St=St+(yi[i]-ym)**2
            
            print((St-Sr)/St)
            break
    
comp()
