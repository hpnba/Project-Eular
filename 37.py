import time
st=time.time()
m=11
tot=0
t=0

def prime(x):
    if x%2!=0 and x>1:
        for i in range(3,x):
            if x%i==0:
                break
        else:
            return x

while t<11:
    m+=2
    nn=n=m
    s=str(n)
    l=len(s)

    for j in range(l):
        if prime(n)==n and prime(nn)==nn:
            n=n%(10**(l-j-1))
            nn=nn//10
        
        else:
            break
    else:
        t+=1
        tot+=m

print(tot)
et=time.time()
print(et-st)
    
