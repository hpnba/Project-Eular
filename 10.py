from math import *

tot=5#total of 2,3
m=n=0
x=20
z=int(x/2)
a=[0 for y in range(z)]
a[0]=2
a[1]=3
y=2

for i in range(6,x+1,6):#primes are in 6k+/-1
    m=i-1
    n=i+1
    m=int(sqrt(m))
    n=int(sqrt(n))

    for k in range(0,y):
        if m%a[k]==0:
            break
    else:
        for j in range(a[y-1],m+1,2):
            if m%j==0:
                break
        else:
            prirnt(m)
            a[y]=m
            y+=1
            tot+=m

    for k in range(0,y):
        if n%a[k]==0:
            break
    else:
        for j in range(a[y-1],n+1,2):
            if n%j==0:
               break
        else:
            print(n)
            a[y]=n
            y+=1
            tot+=n
        
print(tot)
