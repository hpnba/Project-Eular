c=0
d=0
nm=0
p=0

def prime(x):
    if x==2:
        p+=1
    elif x>2:
        for i in range(3,int(x**(1/2))+1,2):
            if x%i==0:
                break
        else:
            p+=1
    return p

for a in range(-41,41):
    for b in range(-41,41):
        for n in range(42):
            nm=a*n+b
            if nm%2!=1:
                continue
            nm+=n**2
            prime(nm)
        if prime(nm)>mx:
            c=a
            d=b
        p=0

print(c,d,c*d)
            
        
        
