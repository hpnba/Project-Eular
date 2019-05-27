import time

stime=time.time()

s=[0 for x in range(9801)]
y=0
for i in range(2,101):
    for j in range(2,101):
        s[y]=i**j
        y+=1
s=set(s)
s=sorted(s,key=int)
print(len(s))

etime=time.time()
print(etime-stime)

