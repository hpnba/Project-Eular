import time
st=time.time()
m=1
product=1
n=0
l=0
le=0
while True:
    n+=1
    s=str(n)
    l+=len(s)
    if m>le and m<=l:
        product*=int(s[m-le-1])
        print(s[m-le-1])
        m*=10
        if m==1000000:
            break

    le=l
print(product)
et=time.time()
print(et-st)
