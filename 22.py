import time
st=time.time()

tot=0
t=0
f=open('names.txt','r')
f=f.read().split(',')
name=sorted(f)
m=len(name)


for j in range(0,m):
    l=len(name[j])
    for i in name[j]:
        if i=='"':
            continue
        a=i
        t+=(ord(i)-64)
    
    tot+=(j+1)*t
    t=0

print(tot)

et=time.time()
print(et-st)

##while True:
##
##    a=f.read(1)
##    if not a:
##        n+=1
##        print(t)
##        tot+=n*t
##        print("End",n,t)
##        break
##    if a=='"':
##        continue
##    if a==",":
##        n+=1
##        tot+=n*t
##        t=0
##        continue
##    t+=(ord(a)-64)
##
##print(tot)




