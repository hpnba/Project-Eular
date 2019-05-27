import time

st=time.time()

prime=[0 for i in range(int(1000000))]
prime[0]=2
nop=1
def pri(x):
    for i in range(3,x,2):
        if x%i==0:
            break
    else:
        return x
for j in range(3,1000000,2):
    if pri(j)==j:
        prime[nop]=j
        nop+=1
print(nop)

et=time.time()
print(et-st)
