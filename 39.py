import time
st=time.time()

mc=0
mx=0


for p in range(1,1000):
    count=0
    for a in range(1,p-2):
        for b in range(1,a):
            c=(a**2+b**2)**(1/2)
            if a+b+c>p:
                break
            if a+b+c==p:
                count+=1
    if count>mc:
        mc=count
        mx=p
print(mx,mc)

et=time.time()
print(et-st)
                
            
