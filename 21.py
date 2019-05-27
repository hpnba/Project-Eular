tot=0

for i in range(2,10000):
    a=b=0
    for j in range(1,i):
        if (i%j==0):
            a+=j
    for k in range(1,a):
        if(a%k==0):
            b+=k
    if b==i and a!=b:
        tot+=i
print(tot)


