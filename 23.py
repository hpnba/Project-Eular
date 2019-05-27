import time
st=time.time()

def abundant(x):
    tot=1
    z=int(x**(1/2))
    for i in range(2,z+1):
        if x%i==0:
            tot+=i
            if x/i!=i:
                tot+=(x/i)
    if tot>x:
        return x
    else:
        return  False
y=0
ab=[0 for i in range(6965)]
for i in range(12,28124):
    if abundant(i)==i:
        ab[y]=i
        y+=1


num=0
a=0
n=[0 for i in range(6965**2)]
for i in range(6965):
    for j in range(i,6965):
        num=ab[i]+ab[j]
        if num>28124:
            break
        else:
            n[a]=num
            a+=1
n=set(n)
n=sorted(n)

total=0
b=0
for i in range(28124):
    if n[b]==i:
        b+=1
        continue
    total+=i
print(total)
        

et=time.time()
print(et-st)
