import time
st=time.time()

def prime(x):
    if x%2!=0:
        for i in range(3,x,2):
            if x%i==0:
                break
        else:
            return x


    

mx=0
for n in range(1001,1000000,2):
    if prime(n)==n:
        
        s=str(n)
        l=len(s)
        lt=0
        tri=l*(l+1)/2
        for i in range(l):
            lt+=int(s[i])
        if lt==tri:
            mx=n
print(mx)

et=time.time()
print(et-st)
    
    
