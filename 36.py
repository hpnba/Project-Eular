import time
st=time.time()

n=11
tot=0
def check1(x):
    s=str(x)
    l=len(s)

    for i in range(0,int(l/2)):
        if s[i]!=s[l-i-1]:
            break
    else:
        return x

def check2(x):
    s=str(bin(x))
    l=len(s)

    for i in range(0,int(l/2)-1):
        if s[i+2]!=s[l-i-1]:
            break
    else:
        return x

for i in range(1,1000000):
    if check1(i)==i:
        if check2(i)==i:
            tot+=i
print(tot)

et=time.time()
print(et-st)
        

    
