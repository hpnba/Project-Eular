import math
import time
st=time.time()
tot=0
n=3
while n<10000000:
    num=0
    s=str(n)
    l=len(s)
    for i in range(l):
        num+=math.factorial(int(s[i]))
    if num==n:
        tot+=num
        print(num)
    n+=1
                            



et=time.time()
print(tot)
print(et-st)

                            
