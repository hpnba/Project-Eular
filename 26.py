x=float(1/31)
n=[0 for i in range(1000)]
y=0
count=0
t=0
print(x)
while True:
    x=x*10
    z=x%10
    if z==0:
        break
    z=int(z)
    n[y]=z
    for i in range(y):
        if n[i]==n[y]:
            
            t+=1
            if t==30:
                count=y-i
                break
    y+=1
    if t==30:
        break

print(count)


    
