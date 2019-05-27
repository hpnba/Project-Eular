from time import time
import math
t=time()
def dev(n):
    f=0
    for i in range(1,int(math.floor(math.sqrt(n)+1))):
        if n%i==0:
            f+=2
            if n%i==i:
                f-=1
        else:
            continue
    return f

x=1
y=2
while dev(x)<500:
    x+=y
    y+=1
print(x)
tt=time()-t
print(tt)                         



    
